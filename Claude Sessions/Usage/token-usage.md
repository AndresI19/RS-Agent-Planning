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
| 2026-04-20 | b4788b84 | 270 | 51,324 | 10,103,726 | 208,300 |

---

## Totals

| Metric | Tokens |
|--------|-------:|
| **Input** | 1,047 |
| **Output** | 191,255 |
| **Cache Read** | 26,629,684 |
| **Cache Write** | 467,031 |
| **Grand Total** | 27,288,017 |

---

## Notes

- Cache read tokens are significantly cheaper than input tokens — high cache read ratios indicate good prompt caching efficiency.
- Updated by running the token extraction script against `~/.claude/projects/` and `~/.claude/sessions/` JSONL files.
- Last updated: 2026-04-20
