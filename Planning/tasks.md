# Task List — RuneScape Research Assistant

## Phase 0 — Decisions & Setup
> Resolve open questions before writing any code.

- [x] Choose OSRS-only, RS3-only, or both for v1 → **RS3 for v1, OSRS in v2**
- [ ] Choose Discord library: discord.py vs. discord.js
- [ ] Choose TTS provider: Google TTS, ElevenLabs, or AWS Polly
- [ ] Choose Claude Desktop integration method: MCP Server or API Proxy
- [x] Choose hosting provider and server size → **local / self-hosted VM; cloud hosting deferred to post-full-stack**
- [x] Register domain name → **deferred; "reldo" if local reverse proxy is ever needed**
- [ ] Create Anthropic API account and confirm tier/rate limits
- [ ] Create Discord application and bot token (dev + prod)
- [ ] Set up GitHub org or user for project repos
- [ ] Define repo structure (monorepo vs. separate repos per service)

---

## Phase 1 — Dev Environment
> Local environment running all services via Docker Compose.

### Infrastructure
- [ ] Write `docker-compose.yml` base config
- [ ] Write `docker-compose.dev.yml` overrides
- [ ] Set up local PostgreSQL container + schema
- [ ] Set up local Redis container
- [ ] Configure `.env.example` with all required keys
- [ ] Add `.gitignore` covering `.env`, secrets, build artifacts
- [ ] Confirm secrets-check hook blocks `.env` commits

### Agent Harness
- [ ] Scaffold Agent Harness service (Python + Anthropic SDK)
- [ ] Implement basic query → Claude API → response flow
- [ ] Define tool schema for RuneScape Research Service calls
- [ ] Add conversation context management (per user/session)
- [ ] Write unit tests for tool dispatch logic

### RuneScape Research Service
- [ ] Scaffold service (Python)
- [ ] Implement `search_wiki(query)` — RS/OSRS wiki MediaWiki API
- [ ] Implement `get_item_price(item_name)` — GE price API
- [ ] Implement `get_player_stats(username)` — hiscores API
- [ ] Implement `get_quest_info(quest_name)` — wiki quest lookup
- [ ] Add Redis caching layer with appropriate TTLs
- [ ] Write integration tests against live APIs

### API Gateway
- [ ] Scaffold gateway (FastAPI or Express)
- [ ] Implement `/query` endpoint
- [ ] Add request validation and basic auth header check
- [ ] Add rate limiting middleware
- [ ] Wire to Agent Harness

### Discord Bot Service
- [ ] Create Discord application (dev bot)
- [ ] Scaffold bot service
- [ ] Implement `!rs <query>` text command
- [ ] Implement `/rs <query>` slash command
- [ ] Wire bot to API Gateway
- [ ] Test end-to-end: Discord → Gateway → Agent → Research → Discord
- [ ] Implement voice channel join + TTS audio streaming

### Claude Desktop Integration
- [ ] Set up MCP server scaffold
- [ ] Register `runescape_research` tool in MCP manifest
- [ ] Wire MCP tool call to Agent Harness
- [ ] Test end-to-end: Claude Desktop → MCP → Agent → Research → response

### TTS Service
- [ ] Choose and integrate TTS provider
- [ ] Implement text → audio stream endpoint
- [ ] Wire to Discord Bot voice output

---

## Phase 2 — Production Environment
> Deploy to VPS, configure domain, harden for public use.

### Server Setup
- [ ] Provision VPS (DigitalOcean or chosen provider)
- [ ] Configure SSH access and firewall rules
- [ ] Install Docker + Docker Compose on server
- [ ] Set up Caddy as reverse proxy with Let's Encrypt TLS
- [ ] Configure DNS: point domain to VPS IP
- [ ] Enable Cloudflare proxy (optional but recommended)

### Deployment
- [ ] Write `docker-compose.prod.yml` overrides
- [ ] Configure production environment variables (no `.env` files in prod)
- [ ] Set up container restart policies
- [ ] Deploy all services
- [ ] Smoke test all endpoints from public domain

### Hardening
- [ ] Add API key auth between services
- [ ] Set resource limits on containers (CPU/memory)
- [ ] Configure PostgreSQL backups
- [ ] Set up structured logging
- [ ] Add uptime monitoring (UptimeRobot or Better Uptime — free tier)
- [ ] Set up error alerting (Discord webhook or email)

---

## Phase 3 — Polish & Launch
> Quality, documentation, and public rollout.

- [ ] Write `README.md` for each service repo
- [ ] Document API endpoints
- [ ] Document MCP server setup for Claude Desktop users
- [ ] Write Discord bot setup guide (for server admins adding the bot)
- [ ] Create Discord server for support/feedback
- [ ] Invite beta testers
- [ ] Monitor API usage and costs post-launch
- [ ] Iterate on response quality based on feedback

---

## Backlog (Post-v1)

- [ ] Web UI (simple chat interface at the domain root)
- [ ] User accounts and saved preferences
- [ ] OSRS support (RS3 shipped in v1; add OSRS wiki + GE + hiscores endpoints)
- [ ] Price alert system ("notify me when Twisted Bow drops below X gp")
- [ ] Clan/group features
- [ ] Mobile app
