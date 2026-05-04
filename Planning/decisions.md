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

### Hosting: local / self-hosted VM throughout development
**Decision:** No cloud hosting provider will be chosen until the full stack (including Discord bot) is complete and working. Development and testing run locally or on a self-managed VM.

**Rationale:** Introducing a hosted environment before the stack is stable adds unnecessary ops overhead. The decision will be revisited once the full stack is working.

---

### Domain: deferred; "reldo" if a local reverse proxy is ever needed
**Decision:** No domain name will be registered during development. If a local reverse proxy is set up to expose the service on the home network, the hostname will reference **Reldo** — the Varrock Palace librarian and in-game authority on lore and knowledge.

**Rationale:** No public URL is needed until the service is production-ready.

---

### Caching: in-memory only; Redis deferred
**Decision:** All caching in the MCP server uses in-memory structures (dict / `cachetools`). Redis will only be introduced when there is an explicit need — multiple services sharing state, persistence requirements, or a measurable performance gap.

**Rationale:** The MCP server is a single process with no cross-service sharing. In-memory is sufficient and avoids infrastructure complexity during development. Caching should sit behind a thin interface so the backend can be swapped to Redis without touching tool logic.

---

### Game disambiguation: require explicit `game` on every MCP tool

**Decision:** Every MCP tool's `inputSchema` makes `game` a required parameter (no default). Each tool's description includes the sentence: *"If the user has not specified which game (RS3 or OSRS), ask them before calling this tool."*

**Rationale:** Prior behavior defaulted `game` to `"rs3"`, so ambiguous prompts like "What's the price of an abyssal whip?" silently returned RS3 results even when the user might have meant OSRS. Schema-required prevents silent omission; the description guides the LLM to clarify rather than guess when the prompt is ambiguous. Together they ensure the agent asks for game disambiguation rather than confidently producing a wrong-game answer. Surfaced during #17 QA testfest where multiple ambiguous prompts produced RS3-flavored answers without any clarification turn.

---

### Profanity handling: pass through verbatim

**Decision:** The MCP server passes through input and output verbatim across all three channels where profanity may appear: Jagex-censored usernames (honor whatever the hiscores API returns), wiki content (render canonical lore as-is), and freeform user queries (forward unmodified). No content scrubbing or refusal at the MCP layer.

**Rationale:** The MCP server is a data layer, not a content-moderation layer. Wiki redaction would distort canonical source material and break legitimate references. Selective per-channel filtering would create inconsistency where the same word renders one way in a wiki result and another way in a query echo. The MCP server also lacks the authorial context needed to filter correctly — it cannot distinguish strings the *user* typed (potentially filter-worthy) from strings the *data sources* returned (canonical, safe to echo); only the consuming agent has that context. Surfaced during #17 QA testfest as an undefined policy question.

**Consumer responsibilities:** Each agent that calls the MCP server is responsible for its own content policy at its own boundary, because only the consumer knows authorial origin.

- *Claude Desktop integration*: Anthropic's safety layer applies to model output, including refusing genuinely abusive freeform queries before they reach the MCP server. No additional filter is needed inside the integration.
- *Discord bot (future, Phase 2+)*: the bot will be a separate agent that doesn't go through Claude Desktop's safety layer, so it must implement its own filtering. Two filter points are required: an **input filter** at the Discord-message boundary (rejects user-typed slurs before they reach the LLM or the MCP server) and an **output filter** at the bot's reply boundary (last-line defense before posting back to chat). Specific filter implementation — community deny list, Anthropic's Moderation API, a discord.py library, or some combination — is deferred to the Discord-bot phase.

The MCP server stays uniform across consumers; the moderation surface lives at each consuming agent's I/O boundary, not in the data layer.

---

## Open

- Claude Desktop integration method: MCP server (recommended) vs. API proxy
- Discord library: discord.py vs. discord.js
- TTS provider: ElevenLabs, Google TTS, or AWS Polly
- Database: needed for v1?
