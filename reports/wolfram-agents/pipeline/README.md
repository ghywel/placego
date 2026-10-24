# The Rule 30 Prize submission pipeline scripts (Local, 2026-10-24; revised for GC1762)

Copies of the scripts that run in the pipeline folder on the M5 (that folder, holding the kit copy, the essays, the
built notebooks and the build-1 reference cells, stays outside git). Every script takes its paths from the folder it
runs in; none holds a credential (the Wolfram kernel's own cloud connection authenticates the submission).

| file | purpose |
|---|---|
| `build_sub.wl NAME` (revision 2) | `MarkdownToNotebook` on `NAME/essay.md` with `RULE30PRIZE_KIT` set to the folder's kit copy; LeanLink builds and kernel-replays the module. Prints the essay digest, the resolved resource's provenance (name, version, uuid, release date), the wall time, the result head, the notebook's bytes and digest, and a final `RESULT OK`; exits 1 with `RESULT FAIL <why>` when the essay is missing, `essay.nb` already exists (the output would not be fresh), the resource does not resolve, the conversion fails, or no notebook is written |
| `read_nb_full.wl NAME OUTDIR [NOTEBOOK]` | writes every `Output` cell in FULL InputForm to `OUTDIR/cell-NN.txt`, the count to `count.txt`, a sha256 per cell to `digests.txt`; exits 1 if the notebook cannot be read |
| `read_nb_dexact60.wl` | the earlier 160-character preview reader (kept for the record of build 1; not a gate) |
| `submit_sub.wl NAME "H1 H2" [SUPERSEDES]` | posts the notebook with title, abstract (from the essay's front matter), authors and headlines; the raw reply goes to `NAME/submit-response.private.json` (outside git) |
| `status_all.wl` | the status line of every submitted id |

## Bounded execution: `tests/probes/wolfram/w7_notebook.py`

The notebook build runs as a stage under the unchanged W1A supervisor (`tests/probes/wolfram/w1a_harness.py`), the
same supervisor as W5 and W6: own session and process group; one-second samples of the group's aggregate RSS, live CPU,
member and lean counts; stops on group RSS, wall, CPU, stage deadline, memory pressure, swap growth, low disk, log
size, artifact growth and extra lean processes; a monitor failure is UNKNOWN; the leader's exit kills any surviving
member and records it; SIGTERM, SIGINT and SIGHUP to the stage are turned into an exception inside the step loop, so
the owned group is killed and the stop is recorded; every non-pass exit code is nonzero. Pins before anything runs:
the supervisor's bytes, both pipeline scripts, the staged essay, the module (pipeline copy and the kit's installed
copy), the build-1 reference cells, the kit copy's commit, toolchain, pinned sources, built dependencies and `git
status`, and the machine's physical memory. Fresh output: `essay.nb` must be absent before the build and afterwards be
newer than the step start and differ from build 1's digest. The FULL-CELL gate compares every output cell with build
1's reference in full (cells 4 and 10 after normalising LeanLink's per-run temporary module name) and requires the
semantic predicates ({60, 114}; the first and last chunk checks and `ChunksOK 60 115 18 0 4096`; exactly the three
standard axioms; the `Success` summary with `The kernel accepts all 8466 declarations`; the `LeanEnvironment`
summary with 4363 constants). Its 27 controls (`--controls`) cover the matcher, the gate (an equal 160-character prefix
with a different full cell FAILS), fresh output, interruption with a child under the real supervisor, a failed process
enumeration, and the build script's two failure paths. The shell wrapper of L847 (`nb_build_capped.sh`) is withdrawn.
