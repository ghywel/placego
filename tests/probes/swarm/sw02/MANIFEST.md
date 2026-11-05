# SW-02 run manifest, frozen at Wave 0 (Local, 5 November 2026, L1560)

*The launch contract of the design's §13. Filled in by Local before any agent ran.*

## Pins

| Item | Value |
|---|---|
| Design | `reports/SW02-SWARM-DESIGN.md`, draft 4 |
| Kit | `5ad29d6bfb38d6b66db72619234c7442a66eb4c0`, a clean checkout outside git |
| Portal and PR index | `known_find.py --new`, 5 November 22:34 GMT: 200 portal entries, 188 kit PRs dumped to a snapshot outside git |
| Record for readers, skeptics, judges, compilers | export of the freeze commit (the commit that carries this file) |
| Record for attack agents | export of `6d3da386` (L1558), before the design existed |
| Models | Opus 5.5 (`claude-opus-5-5`) by default; Fable 5.1 (`claude-fable-5-1`) on named slots; Haiku 5.5 only for the mock resume control |
| Host | M5, 10 cores, 16 GiB unified memory; 7.5 GiB free plus inactive at 22:39 GMT |
| Software | Python 3.15.2, `run_capped.py` at the freeze commit; no Lean or Wolfram in Waves 1 to 3 |

## The owner's choices

Full size. Weekly ceiling about 50% ("rough"; not a reason to stop a nearly finished compile). Waves progress without pausing for the owner.
The M5 is set aside, with memory watched.

## Roster and allowances

| Wave | Tasks | Effort | Tool-call budget per task |
|---|---|---|---|
| Smoke | 5 small tasks, reused from no later wave | high, medium, low | 15 to 25 |
| 1 Readers, librarians | 20 | high | 90 and 70 |
| 1 Verifiers | up to 8 | medium | 80 |
| 2 Pilot and main | 56 | xhigh; max on Fable slots | 120 |
| 3 Screeners, skeptics, rescuers | up to 69 | high; xhigh for SK-M | 80 |
| 4 Bench | up to 11 | high | 60; Local reviews each test and runs it |
| 5 Compile | 6 | high; max on Fable judges | 100 |

BN-11 makes the bench ceiling 11, as Cloud added. Retry allowance: 15 extra launches in all, each logged. A batch never holds more than about 24 tasks, so
the meter and the host are read between batches.

**Fable slots (Cloud's recommendation, kept):** AM-1, AM-4, CP-1, CP-5, HX-1, HX-2, CT-1, CT-3, JD-1, JD-2, and SK-M on any prize-level claim.

## Gates, read before every batch

| Meter | Rule |
|---|---|
| Five-hour window | Start a batch only under 85%; otherwise wait for the reset, because agents die at the limit (SW-01) |
| Weekly, all models | Stop launching new attack or refutation batches at about 50%; compile what exists |
| Weekly, Fable | Fable slots fall back to Opus at 45% (Cloud: a quarter of the week above the 20% read at the freeze) |
| Meter unavailable | No new wave |

## Host limits

`hostwatch.py` runs for the whole swarm, sampling every 15 seconds. Stop at free plus inactive memory under 1 GiB on three samples, swap growth over 4 GiB, or critical memory
pressure on three samples: it writes the stop file, the queue refuses jobs, it terminates a running job, and Local is notified. Warnings go to a log at 2 GiB. Concurrency starts at 3 in the smoke test and
rises to at most 8 reasoning sessions if the watch stays clear; the workflow tool's own limit on this host is 8.

## Compute

One job at a time, through `q.py`, under `run_capped.py --track-tree` with `--rss-mib` at least 4096, `--swap-growth-mib 4096`, `--min-free-mib 1024`, `--launch-free-mib 2048`, `--file-mib 16`, `--disk-mib 128`, `--max-procs 3`, nice 10. Budget 120 CPU seconds
per task, charged from the `/usr/bin/time` receipt; a job is one worker, so run_capped's per-process `--cpu` is its budget. A stage needing children declares it with `--max-procs` and is charged the same way. Bench tests may get
more in `budgets.json`, set by Local with the test's freeze. Nothing is sent to the Intel host automatically.

## Persistence and resume

Each task writes its results to its own folder as it finishes, and the workflow journal keeps every manifest. A stopped batch resumes with `resumeFromRunId` and unchanged arguments, or a new batch lists only the
missing IDs. The smoke test checks that a completed task's command ran exactly once. One batch at a time.

## Withholding

Attack agents get `TERMS.md` (design §4, §4a, §6, strikes removed), their brief and the pre-design export. Fresh eyes get `FRESH.md`. Readers, librarians, skeptics, judges and compilers get the whole design.
