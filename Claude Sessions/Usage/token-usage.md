# Claude Token Usage History

> Tracked from local session JSONL files in `~/.claude/`.
> Columns: **Input** = direct input tokens · **Output** = generated tokens · **Cache Read** = tokens served from prompt cache · **Cache Write** = tokens written to prompt cache.

---

## By Session

| Date | Session ID | Input | Output | Cache Read | Cache Write |
|------|-----------|------:|-------:|-----------:|------------:|
| 2026-04-19 | 69a10a02 | 280 | 54,098 | 4,793,887 | 67,846 |
| 2026-04-19 | daa09029 | 18 | 1,611 | 126,490 | 11,226 |
| 2026-04-19 | f091be47 | 50 | 3,570 | 316,841 | 9,061 |
| 2026-04-19 | f744d41c | 429 | 80,652 | 11,288,740 | 170,598 |
| 2026-04-21 | b4788b84 | 284 | 54,025 | 11,175,405 | 213,404 |
| 2026-04-25 | cf328501 | 188 | 39,762 | 6,523,358 | 199,875 |

---

## Totals

| Metric | Tokens |
|--------|-------:|
| **Input** | 1,249 |
| **Output** | 233,718 |
| **Cache Read** | 34,224,721 |
| **Cache Write** | 672,010 |
| **Grand Total** | 35,131,698 |

---

## Notes

- Cache read tokens are significantly cheaper than input tokens — high cache read ratios indicate good prompt caching efficiency.
- Updated by running the token extraction script against `~/.claude/projects/` and `~/.claude/sessions/` JSONL files.
- Last updated: 2026-04-25
