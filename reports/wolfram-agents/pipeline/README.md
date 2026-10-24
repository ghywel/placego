# The Rule 30 Prize submission pipeline scripts (Local, committed 2026-10-24 for GPT's review, GC1760)

Copies of the scripts that run in the pipeline folder on the M5 (that folder, holding the kit copy, the essays and the
built notebooks, stays outside git). Every script takes its paths from the folder it runs in; none holds a credential
(the Wolfram kernel's own cloud connection authenticates the submission).

| file | purpose |
|---|---|
| `build_sub.wl NAME` | `MarkdownToNotebook` on `NAME/essay.md` with `RULE30PRIZE_KIT` set to the folder's kit copy; LeanLink builds and kernel-replays the module; prints the wall time and the result head |
| `read_nb_dexact60.wl` | prints the first 160 characters of every `Output` cell of `d-exact-60/essay.nb` |
| `submit_sub.wl NAME "H1 H2" [SUPERSEDES]` | posts the notebook with title, abstract (from the essay's front matter), authors, headlines; the raw reply goes to `NAME/submit-response.private.json` (outside git) |
| `status_all.wl` | the status line of every submitted id |
| `nb_build_capped.sh NAME CAP_S OUTLOG` | the bounded wrapper for a notebook build (below) |

## Bounded execution and cleanup (`nb_build_capped.sh`)

- The build runs in its **own process group**: a `python3 -c` launcher calls `os.setsid()` and execs `wolframscript`, so the
  kernel, LeanLink's `lake`/`lean` children and any temp-file `lean` belong to that group and to nothing else.
- The wrapper waits (up to 5 s) until the job's pgid equals its pid; if it does not, or equals the wrapper's own group, it
  **refuses** to signal any group, kills the one pid, writes `VERDICT not-clean (launcher)` and exits 3.
- Every 10 s it appends the group's `pid:rss_KiB:command` list to `OUTLOG.rss`.
- At `CAP_S` seconds of wall (checked each 10-s sample, so the cap is honoured within 10 s) it sends `TERM` to the whole
  group, waits 10 s, sends `KILL` to the group, and records both.
- After the job ends, it waits 2 s and records: exit code, wall, whether the cap was hit, the number of processes still
  in the group, the number of `lean`/`lake`/`WolframKernel` processes anywhere on the machine, and
  `VERDICT clean` only if exit 0, no cap hit and an empty group.
- It signals nothing outside the group it started. Stand-in tests of 2026-10-24 02:51 BST: cap hit on a parent-and-child
  `sleep` pair (both gone, `group_left 0`, verdict not-clean, exit 143 recorded); a clean 1-s job (verdict clean); an
  instant-exit job (refused at the launcher check, reported not-clean).
