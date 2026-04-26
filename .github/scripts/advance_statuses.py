#!/usr/bin/env python3
"""
advance_statuses.py — Advance project items from Todo → Ready when all blockers are closed.

Triggered by the advance-statuses GitHub Actions workflow on every issue close.
Reads "## Blocked By" sections written by git-plan.py to determine dependencies.

Required env vars (set by the workflow):
  GH_TOKEN        — classic PAT with repo + project scopes
  PROJECT_OWNER   — GitHub username that owns the project
  PROJECT_NUMBER  — integer project number (e.g. "5")
"""

import json
import os
import re
import subprocess
import sys


OWNER          = os.environ["PROJECT_OWNER"]
PROJECT_NUMBER = int(os.environ["PROJECT_NUMBER"])
REPO           = os.environ.get("GITHUB_REPOSITORY", f"{OWNER}/RS-Agent-Planning")


def gh(*args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: gh {' '.join(str(a) for a in args[:4])} failed")
        print(result.stderr.strip())
        sys.exit(1)
    return result.stdout.strip()


def graphql(query):
    return json.loads(gh("api", "graphql", "-f", f"query={query}"))


def parse_blocked_by(body):
    """Extract issue numbers from a '## Blocked By' section in an issue body.

    Expects lines like '- #6 Some title' under the heading.
    Stops parsing at the next markdown heading.
    """
    if not body or "## Blocked By" not in body:
        return []
    section = body.split("## Blocked By", 1)[1]
    section = re.split(r"\n##\s", section)[0]
    return [int(m) for m in re.findall(r"#(\d+)", section)]


def is_closed(issue_number):
    state = gh("issue", "view", str(issue_number),
               "--repo", REPO, "--json", "state", "--jq", ".state")
    return state.strip().upper() == "CLOSED"


def main():
    q = f"""
query {{
  user(login: "{OWNER}") {{
    projectV2(number: {PROJECT_NUMBER}) {{
      id
      fields(first: 20) {{
        nodes {{
          ... on ProjectV2SingleSelectField {{
            id name
            options {{ id name }}
          }}
        }}
      }}
      items(first: 100) {{
        nodes {{
          id
          fieldValues(first: 20) {{
            nodes {{
              ... on ProjectV2ItemFieldSingleSelectValue {{
                name
                field {{ ... on ProjectV2SingleSelectField {{ name }} }}
              }}
            }}
          }}
          content {{
            ... on Issue {{ number title state body }}
          }}
        }}
      }}
    }}
  }}
}}"""
    data = graphql(q)["data"]["user"]["projectV2"]
    project_id = data["id"]

    status_field = next((n for n in data["fields"]["nodes"] if n.get("name") == "Status"), None)
    if not status_field:
        print("Status field not found — nothing to do.")
        return

    field_id   = status_field["id"]
    option_ids = {o["name"]: o["id"] for o in status_field["options"]}
    ready_id   = option_ids.get("Ready")
    if not ready_id:
        print("'Ready' option not found — nothing to do.")
        return

    advanced = 0
    for item in data["items"]["nodes"]:
        content = item.get("content") or {}
        if not content or content.get("state", "").upper() == "CLOSED":
            continue

        current_status = next(
            (fv["name"] for fv in item["fieldValues"]["nodes"]
             if fv.get("field", {}).get("name") == "Status"),
            None
        )
        if current_status != "Todo":
            continue

        blockers = parse_blocked_by(content.get("body") or "")
        if not blockers:
            continue

        if all(is_closed(n) for n in blockers):
            mutation = f"""
mutation {{
  updateProjectV2ItemFieldValue(input: {{
    projectId: "{project_id}"
    itemId: "{item['id']}"
    fieldId: "{field_id}"
    value: {{ singleSelectOptionId: "{ready_id}" }}
  }}) {{
    projectV2Item {{ id }}
  }}
}}"""
            gh("api", "graphql", "-f", f"query={mutation}")
            print(f"  → #{content['number']} {content['title']}: Todo → Ready")
            advanced += 1

    print(f"\n{advanced} item(s) advanced to Ready.")


if __name__ == "__main__":
    main()
