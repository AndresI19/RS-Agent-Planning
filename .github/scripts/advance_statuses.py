#!/usr/bin/env python3
"""
advance_statuses.py — Advance project items from Todo → Ready when all blockers are closed.

Triggered by the advance-statuses GitHub Actions workflow on every issue close.
Reads "## Blocked By" sections written by git-plan.py to determine dependencies.

Required env vars (set by the workflow):
  GH_TOKEN        — classic PAT or fine-grained token with repo + project access
  PROJECT_OWNER   — GitHub username that owns the project
  PROJECT_NUMBER  — integer project number (e.g. "5")
"""

import json
import os
import re
import sys

import requests

OWNER          = os.environ["PROJECT_OWNER"]
PROJECT_NUMBER = int(os.environ["PROJECT_NUMBER"])
REPO           = os.environ.get("GITHUB_REPOSITORY", f"{OWNER}/RS-Agent-Planning")
TOKEN          = os.environ["GH_TOKEN"]

GRAPHQL_URL = "https://api.github.com/graphql"
REST_BASE   = "https://api.github.com"


def _headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _check(resp, context=""):
    if resp.status_code == 401:
        print("ERROR: GH_TOKEN is invalid or has expired.")
        print("  Update the PROJECT_TOKEN repository secret with a fresh token.")
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR: GitHub API {resp.status_code}{f' ({context})' if context else ''}")
        try:
            print(f"  {resp.json().get('message', resp.text[:300])}")
        except Exception:
            print(f"  {resp.text[:300]}")
        sys.exit(1)


def graphql(query, variables=None):
    resp = requests.post(
        GRAPHQL_URL,
        headers={**_headers(), "Content-Type": "application/json"},
        json={"query": query, "variables": variables or {}},
        timeout=30,
    )
    _check(resp, "graphql")
    data = resp.json()
    if "errors" in data:
        print(f"ERROR: GraphQL errors: {data['errors']}")
        sys.exit(1)
    return data


def is_closed(issue_number):
    resp = requests.get(f"{REST_BASE}/repos/{REPO}/issues/{issue_number}",
                        headers=_headers(), timeout=10)
    _check(resp, f"issue #{issue_number}")
    return resp.json().get("state", "").upper() == "CLOSED"


def parse_blocked_by(body):
    """Extract issue numbers from a '## Blocked By' section in an issue body."""
    if not body or "## Blocked By" not in body:
        return []
    section = body.split("## Blocked By", 1)[1]
    section = re.split(r"\n##\s", section)[0]
    return [int(m) for m in re.findall(r"#(\d+)", section)]


def main():
    query = """
query($login: String!, $number: Int!) {
  user(login: $login) {
    projectV2(number: $number) {
      id
      fields(first: 20) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id name
            options { id name }
          }
        }
      }
      items(first: 100) {
        nodes {
          id
          fieldValues(first: 20) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue {
                name
                field { ... on ProjectV2SingleSelectField { name } }
              }
            }
          }
          content {
            ... on Issue { number title state body }
          }
        }
      }
    }
  }
}"""
    data    = graphql(query, {"login": OWNER, "number": PROJECT_NUMBER})
    project = data["data"]["user"]["projectV2"]

    status_field = next((n for n in project["fields"]["nodes"] if n.get("name") == "Status"), None)
    if not status_field:
        print("Status field not found — nothing to do.")
        return

    field_id   = status_field["id"]
    option_ids = {o["name"]: o["id"] for o in status_field["options"]}
    ready_id   = option_ids.get("Ready")
    if not ready_id:
        print("'Ready' option not found — nothing to do.")
        return

    mutation = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId
    itemId: $itemId
    fieldId: $fieldId
    value: { singleSelectOptionId: $optionId }
  }) {
    projectV2Item { id }
  }
}"""

    advanced = 0
    for item in project["items"]["nodes"]:
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
            graphql(mutation, {
                "projectId": project["id"],
                "itemId":    item["id"],
                "fieldId":   field_id,
                "optionId":  ready_id,
            })
            print(f"  → #{content['number']} {content['title']}: Todo → Ready")
            advanced += 1

    print(f"\n{advanced} item(s) advanced to Ready.")


if __name__ == "__main__":
    main()
