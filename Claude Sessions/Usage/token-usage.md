# Claude Token Usage History

> Tracked from local session JSONL files in `~/.claude/`.
> Columns: **Input** = direct input tokens · **Output** = generated tokens · **Cache Read** = tokens served from prompt cache · **Cache Write** = tokens written to prompt cache.

---

## By Session

| Date | Session ID | Input | Output | Cache Read | Cache Write |
|------|-----------|------:|-------:|-----------:|------------:|
| 2026-05-27 | 9c92ee98 | 297 | 205,938 | 13,303,805 | 941,444 |
| 2026-05-27 | a8560e4a | 12 | 1,290 | 0 | 54,298 |
| 2026-06-19 | 538977fd | 2,768 | 2,541,139 | 741,054,694 | 4,757,963 |
| 2026-06-19 | 76cb686c | 67,660 | 694,831 | 93,190,094 | 2,075,552 |
| 2026-06-22 | 7321729e | 789,399 | 7,655,362 | 1,745,487,494 | 65,813,626 |

---

## Totals

| Metric | Tokens |
|--------|-------:|
| **Input** | 860,136 |
| **Output** | 11,098,560 |
| **Cache Read** | 2,593,036,087 |
| **Cache Write** | 73,642,883 |
| **Grand Total** | 2,678,637,666 |

---

## Notes

- Cache read tokens are significantly cheaper than input tokens — high cache read ratios indicate good prompt caching efficiency.
- Updated by running the token extraction script against the workspace session JSONL files under `~/.claude/projects/`.
- The tracker is scoped to workspace project directories (`~/.claude/projects/*claude-workspace*/`). Earlier home-directory sessions (from before the launch cwd moved into the workspace) are out of scope and not included — the prior 2026-05-05 totals were that smaller home-era slice.
- This regeneration is the first since the tracker's session-path glob was fixed; the large jump versus the prior file reflects workspace sessions the broken glob had been silently missing, not a usage spike.
- Last updated: 2026-06-22
