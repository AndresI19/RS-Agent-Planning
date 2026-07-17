# Claude Token Usage History

> Tracked from local session JSONL files in `~/.claude/`.
> Columns: **Input** = direct input tokens · **Output** = generated tokens · **Cache Read** = tokens served from prompt cache · **Cache Write** = tokens written to prompt cache.

---

## By Session

| Date | Session ID | Input | Output | Cache Read | Cache Write |
|------|-----------|------:|-------:|-----------:|------------:|
| 2026-06-19 | 538977fd | 2,768 | 2,541,139 | 741,054,694 | 4,757,963 |
| 2026-06-19 | 76cb686c | 67,660 | 694,831 | 93,190,094 | 2,075,552 |
| 2026-06-24 | 7321729e | 800,786 | 7,964,505 | 1,792,227,987 | 68,973,100 |
| 2026-06-27 | da133a81 | 7,929 | 37,668 | 867,558 | 57,697 |
| 2026-06-29 | 3cb99110 | 16,150 | 248,347 | 10,354,977 | 913,196 |
| 2026-06-30 | 23cef7d7 | 3,370 | 80 | 14,859 | 6,971 |
| 2026-06-30 | 37841b5f | 6,833 | 3,770 | 0 | 135,541 |
| 2026-06-30 | 86ff1eb1 | 20 | 1,632 | 0 | 53,368 |
| 2026-06-30 | e144726e | 40 | 2,020 | 55,584 | 55,764 |
| 2026-07-02 | ef210eaf | 46,907 | 1,481,724 | 186,380,112 | 12,888,002 |
| 2026-07-08 | ac2c9e25 | 46,020 | 2,140,624 | 144,720,526 | 9,383,624 |
| 2026-07-09 | 222e494e | 23,335 | 9,567 | 480,527 | 72,225 |
| 2026-07-09 | 7a167797 | 26,864 | 191,805 | 21,332,002 | 388,816 |
| 2026-07-09 | 88148252 | 67,639 | 1,459,485 | 197,381,742 | 1,587,270 |
| 2026-07-09 | df84edf7 | 9,167 | 7,024 | 437,096 | 38,583 |
| 2026-07-10 | 08cdc1c3 | 13,379 | 7,581 | 584,651 | 56,103 |
| 2026-07-10 | ab8c36b0 | 57,232 | 944,307 | 186,407,127 | 7,493,143 |
| 2026-07-12 | ebaf825b | 381,113 | 6,508,823 | 1,999,660,451 | 11,135,772 |
| 2026-07-12 | f827dce1 | 31,674 | 233,900 | 26,471,067 | 469,290 |
| 2026-07-13 | 98eec59c | 2,916 | 1,374,442 | 700,699,785 | 2,671,298 |
| 2026-07-14 | 501b8af5 | 7,346 | 6,075,657 | 1,899,374,411 | 14,763,999 |
| 2026-07-14 | e9739318 | 1,076 | 567,501 | 116,251,073 | 2,286,128 |
| 2026-07-15 | 84c51018 | 1,052 | 910,748 | 150,460,572 | 2,329,545 |
| 2026-07-15 | 9e5062d3 | 1,056 | 915,540 | 150,503,942 | 3,339,555 |
| 2026-07-15 | cb89924a | 2,032 | 2,317,289 | 481,713,465 | 9,379,849 |
| 2026-07-16 | 37c14509 | 1,356 | 753,348 | 173,868,294 | 2,572,652 |
| 2026-07-16 | 39899ccb | 1,384 | 593,216 | 169,864,530 | 2,341,101 |
| 2026-07-16 | 5b586922 | 2,066 | 1,400,223 | 419,772,965 | 13,356,616 |
| 2026-07-16 | 6839904f | 9,158 | 7,722,091 | 2,240,699,576 | 27,357,719 |
| 2026-07-16 | 6e884c19 | 1,754 | 1,138,616 | 273,381,945 | 2,887,276 |
| 2026-07-16 | a28f6a55 | 604 | 470,073 | 44,411,502 | 581,344 |
| 2026-07-16 | e420b9d8 | 934 | 461,303 | 71,312,615 | 861,773 |
| 2026-07-17 | 6ebc1211 | 3,138 | 1,903,441 | 705,592,844 | 9,676,794 |
| 2026-07-17 | a7abaebc | 1,318 | 795,537 | 147,622,616 | 2,392,130 |

## Totals

| Metric | Tokens |
|--------|-------:|
| **Input** | 1,646,076 |
| **Output** | 51,877,857 |
| **Cache Read** | 13,147,151,189 |
| **Cache Write** | 217,339,759 |
| **Grand Total** | 13,418,014,881 |

---

## Notes

- Cache read tokens are significantly cheaper than input tokens — high cache read ratios indicate good prompt caching efficiency.
- Updated by running the token extraction script against the workspace session JSONL files under `~/.claude/projects/`.
- The tracker is scoped to workspace project directories (`~/.claude/projects/*claude-workspace*/`). Earlier home-directory sessions (from before the launch cwd moved into the workspace) are out of scope and not included — the prior 2026-05-05 totals were that smaller home-era slice.
- This regeneration is the first since the tracker's session-path glob was fixed; the large jump versus the prior file reflects workspace sessions the broken glob had been silently missing, not a usage spike.
- Last updated: 2026-07-17
