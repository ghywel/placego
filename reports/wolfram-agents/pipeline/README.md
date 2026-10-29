# The Rule 30 Prize submission pipeline scripts (Local, 2026-10-24; revised for GC1762)

Copies of the scripts that run in the pipeline folder on the M5 (that folder, holding the kit copy, the essays, the
built notebooks and the build-1 reference cells, stays outside git). Every script takes its paths from the folder it
runs in; none holds a credential (the Wolfram kernel's own cloud connection authenticates the submission).

| file | purpose |
|---|---|
| `build_sub.wl NAME [OUTPUT-NOTEBOOK]` (revision 3) | `MarkdownToNotebook` on `NAME/essay.md` with `RULE30PRIZE_KIT` set to the folder's kit copy; LeanLink builds and kernel-replays the module. The optional OUTPUT-NOTEBOOK is the absolute path the notebook is written to (the supervised stage passes a path inside its monitored output folder). Prints the essay digest, the notebook path, the resolved resource's provenance (recorded, not pinned: name, version, uuid, release date), the wall time, the result head, the notebook's bytes and digest, and a final `RESULT OK`; exits 1 with `RESULT FAIL <why>` when the essay is missing, the output notebook already exists (the output would not be fresh), the resource does not resolve, the conversion fails, or no notebook is written |
| `read_nb_full.wl NAME OUTDIR [NOTEBOOK]` | writes every `Output` cell in FULL InputForm to `OUTDIR/cell-NN.txt`, the count to `count.txt`, a sha256 per cell to `digests.txt`; exits 1 if the notebook cannot be read |
| `read_nb_dexact60.wl` | the earlier 160-character preview reader (kept for the record of build 1; not a gate) |
| `submit_sub.wl NAME "H1 H2" [SUPERSEDES]` | posts the notebook with title, abstract (from the essay's front matter), authors and headlines; the raw reply goes to `NAME/submit-response.private.json` (outside git) |
| `status_all.wl` | the status line of every submitted id |

## Bounded execution: `tests/probes/wolfram/w7_notebook.py` (revision 2)

The notebook build runs as a stage under the unchanged W1A supervisor (`tests/probes/wolfram/w1a_harness.py`), the
same supervisor as W5 and W6: own session and process group per step; one-second samples of the group's aggregate RSS,
live CPU, member and lean counts; stops on group RSS, wall, CPU, stage deadline, memory pressure, swap growth, low
disk, log size, artifact growth and extra lean processes; a monitor failure is UNKNOWN; the leader's exit kills any
surviving member and records it. Revision 2 adds, for GC1764: (1) the ten build-1 reference cells are pinned by their
byte digests inside the stage's source and re-verified at the moment the gate reads them, so a changed reference with
an unchanged manifest fails; (2) the notebook is written inside the stage's output folder (covered by the supervisor's
artifact sampling, cap 64 MiB) and a watcher thread samples its size every second during the build (8 MiB cap, fail
closed on an unreadable file), killing the owned groups on a breach; on a pass the notebook is copied to `NAME/essay.nb`
for the submit script, which must not exist beforehand, and the copy's digest is verified; (3) ownership over the whole
child lifetime: the watcher discovers this process's session-leading children every second and records them; every
kill decision re-discovers first; the signal handler (TERM, INT, HUP) kills the owned groups itself before raising, so
a signal between the supervisor's spawn and its try/finally still terminates the child; a repeated or nested signal is
recorded and deferred; a finalization on every exit path re-checks the owned groups and persists the receipt; a watcher
that cannot enumerate processes three times running kills the owned groups and stops the stage; supervisor
construction and the memory read are inside the guarded receipt path; the group RSS stop must be strictly below half
of physical memory. Exit codes: pass 0, STOP 1, REFUSED 3, interrupted 130. Its 39 controls (`--controls`) cover the
matcher, the full-cell gate (an equal 160-character prefix with a different full cell FAILS; a changed reference payload
with an unchanged manifest FAILS), fresh output, interruption with a child inside and outside a supervised step, two
signals in quick succession, the notebook growing past its cap during a step, a failed process enumeration inside the
supervisor and in the watcher, and the build script's two failure paths. The shell wrapper of L847 is withdrawn.

## 29 October2026: persistent MCP kernels are a separate resource allocation (L1092, GC2058)

The supervision described above applies to processes actually inside the owned stage. It does not automatically
bound a pre-existing Wolfram MCP kernel used through a connector. Local reported repeated LeanLink notebook
builds accumulating environments in that kernel (75GB footprint/39GB host swap before stopping its session's
kernel). Treat that as a retained resource failure, not a successful bounded notebook pipeline outcome.

For connector-based validation, use a fresh session-owned kernel for one notebook build and stop that same
kernel after retaining outputs. Before running, freeze kernel-inclusive wall/CPU/memory/output bounds and
pressure stops, identify how its PID/allocation is monitored, account for concurrent host allocations, and retain
baseline and teardown receipts. An isolated lean/compiler or calling-helper RSS limit alone is insufficient.
If the required kernel resource observation cannot be enforced, record that limitation and use the supervised
fresh-process pipeline instead; do not describe MCP work as protected by W7 merely because W7 exists. Do not
stop kernels owned by other sessions, and do not rerun a failed stage automatically.

## 29 October2026: output controls and diagnostic retention (L1100, GC2068)

The right-profile failed and repaired notebooks both had6 outputs, no Message cells and no $Failed. Only the
actual illustration output distinguished them: the failure retained a header-only table, while the repaired
artifact contained both expected rows. Counting Message cells is therefore insufficient as a success gate.
Assert the expected output content and formal-check outcome as well.

Retain a bounded full internal-handler packet and its digest before stopping a session-owned kernel; a
truncated top-N list loses unknown event names. Define any expected off-by-default framework events and the
unknown-event disposition before a build. If retained evidence is incomplete, label the manual review and its
limits explicitly; do not claim an unchanged 'any message' counterfactual passed, reconstruct lost evidence,
or rerun only to obtain a cleaner record. This does not weaken the separate proof/source/kernel checks.
