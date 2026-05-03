# Claude Desktop QA validation

End-to-end manual QA pass for the MCP server. Issue: AndresI19/RS-Agent-Planning#17.

The 12 prompts below exercise every MCP tool through Claude Desktop, complementing the offline unit tests (#28) and the SSE smoke test (`scripts/smoke_test_tools.py`). Run top-to-bottom, mark each Result, log any Failures at the bottom, and convert each failure into a follow-up issue via `/todo`.

## Last run

- **Date**:
- **Server commit**: (output of `git -C ~/git-workspace/claude-workspace/rs-mcp-server rev-parse --short HEAD`)
- **Claude Desktop version**:
- **Operator**:

## Setup checklist

- [ ] `make start` from `rs-mcp-server` — server up at `http://localhost:8000/sse`.
- [ ] Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, equivalent on Linux/Windows) points at the SSE endpoint.
- [ ] MCP icon shows green / connected in Claude Desktop's status bar.
- [ ] `make logs` running in a second terminal so each tool invocation can be cross-checked against `tool_call_start` log lines.

---

## search_wiki

### 1. RS3 happy path

**Prompt**: "What is Necromancy in RuneScape 3?"
**Expected tool**: `search_wiki(query~"Necromancy", game="rs3")`
**Expected response**: Cites RS3 Wiki, includes a paragraph about the Necromancy skill (RS3's combat-style skill released in late 2023).
**Result**: _Pass / Fail / Note_

### 2. OSRS happy path

**Prompt**: "Tell me about Zulrah in OSRS."
**Expected tool**: `search_wiki(query~"Zulrah", game="osrs")`
**Expected response**: Cites OSRS Wiki, mentions the boss / serpent / Zul-Andra location.
**Result**: _Pass / Fail / Note_

### 3. No-results path

**Prompt**: "What is zzznotathingthatexists in OSRS?"
**Expected tool**: `search_wiki(query~"zzznotathingthatexists", game="osrs")`
**Expected response**: "No results found for 'zzznotathingthatexists' on the OSRS wiki."
**Result**: _Pass / Fail / Note_

---

## get_item_price

### 4. OSRS happy path

**Prompt**: "What's the current Grand Exchange price of an abyssal whip in OSRS?"
**Expected tool**: `get_item_price(item_name~"abyssal whip", game="osrs")`
**Expected response**: Shows `**Abyssal whip** (OSRS Grand Exchange)` with `Instant buy:` and `Instant sell:` lines, both in gp.
**Result**: _Pass / Fail / Note_

### 5. RS3 lowercase (regression for #31)

**Prompt**: "How much is an abyssal whip in RS3?"
**Expected tool**: `get_item_price(item_name~"abyssal whip", game="rs3")`
**Expected response**: Shows `**Abyssal whip** (RS3 Grand Exchange)` with `Price:` and trend lines. Title MUST be capitalized "Abyssal whip" — proves the case-sensitivity fix from #31 works through the live tool, not just unit tests.
**Result**: _Pass / Fail / Note_

### 6. Unknown item

**Prompt**: "What's the price of a nosuchitem in RS3?"
**Expected tool**: `get_item_price(item_name~"nosuchitem", game="rs3")`
**Expected response**: "Item 'nosuchitem' not found on the RS3 Grand Exchange."
**Result**: _Pass / Fail / Note_

---

## get_player_stats

### 7. OSRS happy path

**Prompt**: "What are Lynx Titan's stats in OSRS?"
**Expected tool**: `get_player_stats(username~"Lynx Titan", game="osrs")`
**Expected response**: `**Lynx Titan** (OSRS Hiscores)` header with `Total level:` summary and the 23-skill table indented below.
**Result**: _Pass / Fail / Note_

### 8. RS3 happy path

**Prompt**: "Show me Zezima's hiscores in RS3."
**Expected tool**: `get_player_stats(username~"Zezima", game="rs3")`
**Expected response**: `**Zezima** (RS3 Hiscores)` header with the 30-skill table (RS3 includes Necromancy, Invention, Archaeology, etc. that OSRS doesn't have).
**Result**: _Pass / Fail / Note_

### 9. Unknown player

**Prompt**: "What are the stats of ghostplayer42 on OSRS?"
**Expected tool**: `get_player_stats(username~"ghostplayer42", game="osrs")`
**Expected response**: "Player 'ghostplayer42' not found on OSRS Hiscores."
**Result**: _Pass / Fail / Note_

---

## get_quest_info

### 10. OSRS happy path

**Prompt**: "Tell me about Cook's Assistant in OSRS."
**Expected tool**: `get_quest_info(quest_name~"Cook's Assistant", game="osrs")`
**Expected response**: `**Cook's Assistant** (OSRS Wiki)` header followed by `**Difficulty:**`, `**Length:**`, `**Members:**` field rows. Should be a Free-to-Play, Novice, Short quest.
**Result**: _Pass / Fail / Note_

### 11. Disambiguation

**Prompt**: "What's the quest Dragon Slayer in RS3?"
**Expected tool**: `get_quest_info(quest_name~"Dragon Slayer", game="rs3")`
**Expected response**: A "Did you mean..." disambiguation prompt, because the bare name "Dragon Slayer" on the RS3 wiki redirects to a quest series page rather than a single quest. The response should suggest a more specific name (e.g., "Dragon Slayer I").
**Result**: _Pass / Fail / Note_

### 12. Not found

**Prompt**: "What quest is zzzfakequestzzz?"
**Expected tool**: `get_quest_info(quest_name~"zzzfakequestzzz", ...)`
**Expected response**: "No quest found for 'zzzfakequestzzz' on the … wiki."
**Result**: _Pass / Fail / Note_

---

## Failures

For each row marked **Fail**, capture below and file a follow-up issue via `/todo`:

```
- **#N — <prompt>**
  - **Expected**: <expected behavior>
  - **Actual**: <what Claude Desktop returned, including any tool log lines>
  - **Follow-up**: <issue title to file>
```
