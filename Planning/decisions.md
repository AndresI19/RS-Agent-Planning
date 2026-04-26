# Decisions — RuneScape Research Assistant

Resolved decisions are recorded here with rationale. Open decisions remain in `project-overview.md`.

---

## Resolved

### Language: Python
**Decision:** Implement the MCP server, Agent Harness, and RuneScape Research Service in Python using the `mcp` SDK and Anthropic Python SDK.

**Rationale:** Architecture already specified Python for the Agent Harness and Research Service. Using Python throughout keeps the stack consistent and avoids split toolchains.

---

### Game Scope: RS3 first, OSRS in v2
**Decision:** v1 targets RS3 exclusively. OSRS support is planned for v2 and considered in-scope for the project overall — API abstractions should make adding OSRS endpoints straightforward.

**Rationale:** Focusing on one game reduces v1 surface area. RS3 was chosen as the starting point. OSRS is explicitly deferred, not dropped — tool interfaces (e.g. `search_wiki`, `get_item_price`) should accept a `game` parameter from the start so OSRS can be added without a refactor.

---

## Open

- Claude Desktop integration method: MCP server (recommended) vs. API proxy
- Discord library: discord.py vs. discord.js
- TTS provider: ElevenLabs, Google TTS, or AWS Polly
- Hosting provider and server size
- Database: needed for v1?
