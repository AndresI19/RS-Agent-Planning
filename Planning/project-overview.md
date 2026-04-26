# Project Overview — RuneScape Research Assistant

## What We're Building

A RuneScape-specialized AI research assistant accessible through two input channels:
- **Claude Desktop** (via MCP server or direct integration)
- **Discord** (via a bot plugin)

Users ask natural-language questions about RuneScape (items, quests, skills, Grand Exchange
prices, lore, mechanics, strategies). An agent harness routes the query to specialized
research tools, composes a response, and returns it — either as text in the terminal/chat,
or as synthesized voice in a voice channel.

---

## Goals

| Goal | Description |
|------|-------------|
| Accessible | Works from Claude Desktop and Discord without extra setup for end users |
| Specialized | Deep RuneScape knowledge via wiki scraping, official APIs, and curated data |
| Public | Hosted on a real domain, available 24/7 |
| Scalable | Dev/prod split; services can be scaled independently |
| Voice-capable | Optional TTS response for Discord voice channels |

---

## Game Scope

**v1: RS3 only.** The RuneScape (RS3) wiki and Grand Exchange APIs are the primary data sources.

**v2: Add OSRS.** OSRS support is planned and in-scope for the project. Tool interfaces use a `game` parameter from the start so OSRS endpoints can be added without a refactor.

---

## Out of Scope (v1)

- Account linking or player authentication
- Real-time game data (live player positions, etc.)
- Mobile app or web UI
- OSRS support (deferred to v2)
- Games other than RuneScape

---

## Data Sources

| Source | What it provides |
|--------|-----------------|
| [RuneScape Wiki API](https://runescape.wiki/api.php) | Quests, items, skills, lore, mechanics |
| [OSRS Wiki API](https://oldschool.runescape.wiki/api.php) | OSRS-specific data |
| [OSRS Grand Exchange API](https://prices.runescape.wiki/api/v1/osrs) | Live item prices |
| [RS3 Grand Exchange API](https://runescape.com/api) | RS3 item prices |
| [Jagex Hiscores API](https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws) | Player stats |

---

## Key Decisions to Make

- [ ] Claude Desktop integration method: MCP server vs. API proxy
- [ ] Discord library: discord.py vs. discord.js
- [ ] TTS provider: ElevenLabs, Google TTS, or AWS Polly
- [x] Hosting: **local / self-hosted VM throughout development; cloud provider deferred**
- [x] Domain: **deferred; "reldo" if local reverse proxy is needed**
- [x] Caching: **in-memory for Phase 1; Redis deferred until explicitly needed**
- [ ] Database: needed for v1 (conversation history, caching)?
- [x] Language: **Python** (`mcp` SDK + Anthropic SDK)
- [x] Game scope: **RS3 for v1**, OSRS deferred to v2
