# RS-Agent-Planning

Planning, architecture, and session logs for the RuneScape Research Assistant — an AI agent that answers natural-language questions about RuneScape via Claude Desktop and Discord.

## Structure

- **`Planning/`** — Architecture docs, infrastructure decisions, diagrams, and task tracking
- **`Claude Sessions/`** — Per-session logs recorded by the `/record` skill, including terminal commands, files changed, and summaries
- **`Claude Sessions/Usage/`** — Token usage tracking across all sessions

## Project

The assistant routes RuneScape queries (items, quests, skills, Grand Exchange prices, lore) to specialized research tools backed by the RuneScape Wiki API, OSRS Wiki API, and Jagex Hiscores API. It supports both OSRS and RS3, with optional TTS responses for Discord voice channels.

See [`Planning/project-overview.md`](Planning/project-overview.md) for goals, data sources, and open decisions.
