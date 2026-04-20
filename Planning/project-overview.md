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

## Out of Scope (v1)

- Account linking or player authentication
- Real-time game data (live player positions, etc.)
- Mobile app or web UI
- Support for games other than RuneScape (OSRS + RS3 both in scope)

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
- [ ] Hosting: VPS (DigitalOcean/Linode) vs. cloud-native (AWS/GCP)
- [ ] Database: needed for v1 (conversation history, caching)?
- [ ] OSRS-only, RS3-only, or both?
