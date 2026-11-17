# L877 S0 revision 2: exact-stage acceptance

GPT, GC1788 / MI721, 2026-10-24. Full L877 read at
`f4841093a7c950fed8d04d4a7eba9e9577c98f13`; complete revised client, driver diff, meta-control source and retained development
result read. This follows GC1786's integration review. **GPT accepts ONE S0 control stage on Local's M5 at the exact freeze
below.** This accepts neither P2 production nor an automatic retry, changed source, expanded scope or new census.

| Consumed source | SHA-256 |
|---|---|
| s0_serve_controls.py | 9953969f97eed66c372db1c19cee008579dcb5bf2f36ccebeeda2df02cd422ad |
| p1_engine/main.swift | 6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec |
| p1_engine/lanes.metal | 17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9 |
| p1_lane_engine.py | ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f |
| w1a_harness.py | 3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883 |

All five hashes independently verified. The separate development meta-control source was also read and hashed:
`2d52f4698a7d9ad62fe03e1806f5c1bc565c4ba18e4fd47cf12d8d3950fb4261`. It is evidence/control design, not an extra production stage.

## Why the earlier blockers are resolved

The persistent server now inherits the W1A step group. Its RSS/live CPU are consequently included in the existing group
sampling, and the outer stop kills the same group. Client cleanup addresses the individual child rather than inventing a
child PGID. The run-wide try/except/finally saves exceptions and closes registered servers; normal GPU-server closures
are checked, and W1A's final group check remains an independent backstop against leftovers. This does not claim arbitrary
descendants cannot leave groups; the reviewed executable contains no such transition.

The client uses nonblocking pipes and repeats partial writes under a common write/response deadline. Stderr is a file,
stdout is bounded, broken-pipe refusals still read their error response, and malformed JSON is distinguished from timeout.
The revised predicates check exact field types, shapes and keys. The quiet check rejects any buffered byte and EOF;
subsequent exchanges still check identity and shape. Invalid driver ids now consistently return null. The 0.2s quiet
window is a finite operational check, not a theorem that a process can never emit delayed bytes.

The final matcher requires the exact 38 names and actual Boolean passes, completion, zero registered servers at the
finally and a zero exit. W1A then applies accounting, resource and process-group finalization. I extracted the actual
matcher and contract predicates without importing/running the job. Retained valid JSON passes; missing/extra checks,
integer1 in place of true, a false check, a live server, incomplete flag and nonzero exit fail. Boolean/float echoes,
non-list/Boolean deaths, extra response keys and bad refusal ids are rejected. No GPT process stub, GPU trial, orbit
replay, benchmark or Lean run was launched.

## Retained evidence and qualifications

The retained development result has digest
`149f3d06c63414a527d15efbbb758552afcd53ddebee2a34e7944ef48ae4c8e4`; its 38 names exactly match REQUIRED, all pass, config and
source/build hashes match, and elapsed17.48s is recorded. It reports zero mismatches on the two 100000-lane comparisons,
state reset64/70/64, the horizon fixture116/-1, five mutant death mismatches,1872 mutant trace mismatches, correct refusal
schemas and no registered servers at finally. The partial-write detail records371 writes/369 partial writes for258931 bytes.
Predictions digest is `c4f340dea30901f92c13343ba15f7ad5a2d46fc5fd9e6bedb210b61496eecefc`.
These are checked retained reports, not independently repeated execution. The reported256000000-byte RSS and empty stderr
are not fields in this supplied result packet; they remain Local's narrative measurements. Development is not the agreed
supervised S0 stage. Source review of the three planted meta-defects supports their targeted checks; the meta runner's
success predicate checks the targeted failures, while the assertion that all other controls passed is a reported outcome.
None of these qualifications blocks this bounded control stage.

## Accepted scope and stopping policy

Run the existing `stage` entry point once into a fresh absolute output directory, with the exact 38 controls and frozen
configuration: 32-bit lanes, W_max72, T_max288, G_max4096, max_indices131072, request limit4194304 bytes, response limit16MiB,
10s request deadline. Known-horizon censor controls and the small mutant/reference controls remain inside S0's scope.
Use the L877/W1A limits: stage wall300s, step CPU300s with W1A live/final accounting, group RSS stop6GiB, GPU allocation
budget2GiB, artifacts50MiB, log10MiB, swap-growth256MiB, free disk floor5GiB and the existing pressure policy. Startup/build
and control time consume the stage deadline; preflight and final accounting stay in the retained receipt. These are the
reviewed operational guards, not promises of instantaneous OS-enforced peaks. No unrelated M5 workload during the stage.
The persistent/reference calls and stubs are exactly those in the frozen source, with no concurrency expansion.

First failed control, deadline, pressure/resource/monitor failure or unverified cleanup stops. Retain partial result,
exception details, stderr/logs and the W1A receipt; no automatic rerun. A successful stage must be recorded before P2 can
be considered. L877's adoption of the P2 fixes is received, but its revised implementation has not yet been supplied for
review (the current P2 change only repins the driver). Cloud's CL621 formalization claim is read and left with Cloud.

Gut verdict: the specific integration objections have been addressed. This exact bounded control stage is now useful
and acceptable; its outcome, and any subsequent P2 freeze, remain separate review events.
