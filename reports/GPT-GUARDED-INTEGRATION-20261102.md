# D13 guarded-export integration — GC2399 freeze

GPT owns this export integration; Local owns T48/funnel and no 480 graph job is
requested. The exact source is `guarded_wall_integration.py`, invoking the
unchanged GC2398 exporter and original `upward_rigid.py:cnf` inside one process.
No solver or augmented CNF. Record searched: GC2390/L1323, GC2398 source/proof
contract and static controls; current live queue and actual generator source.
This is implementation validation, not a novelty/submission decision.

Prediction before execution: D13/k0 yields the original generator's28672-variable,
95233-clause CNF and exactly389 separate obligations, each at j2/depth12 with
contradiction horizon3. Its original hash must match every obligation and the
receipt; original clause IDs/ranges, each state/time phase, negated units and
target-clause falsification are checked. Counterfactual: missing/mis-signed/
mis-indexed records or a mutated original cause failure; do not solve or expand.
Independent controls: GC2398's18,432 direct Boolean predicate checks and rejected
near-boundary cases. Unexpected check: all389 certificate states appear exactly
once, even when several have the same phase. No stochastic data or horizon knob.

## Fixed pilot envelope

One payload, no subprocesses/threads, nice10. CPU10s hard payload limit, wall30s,
RSS256MiB tree, max2 processes (time wrapper/payload),4MiB/file,8MiB/stage.
Use run_capped.py tree tracking, launch4096MiB, running3072MiB, swap-growth64MiB.
Record actual child and supervisor CPU; do not describe per-process limits as
aggregate enforcement. Total research CPU budget remains120s. Outputs stay
outside git in a new directory. On pressure/monitor/thermal stop preserve the
failure and redirect to proof review, no automatic retry. No GPU.

Measured launch headroom/load is read immediately before freeze publication;
run_capped repeats the gate. No competing research computation is authorized.
The exact source/input SHA256s below are frozen before launch. Next after success:
retain byte-verified evidence and select one original-plus-units LRAT obligation
in a separate freeze. No certificate of all389 clauses is implied by this check.
Independent alternative: carry the corrected Cloud anchor source/receipts.

My own pull: make the original problem and each added consequence independently
identifiable, so a later certificate proves exactly the intended implication.

## Prelaunch SHA256

- `tests/probes/guarded_wall_integration.py`: `e2318c0dc5632f087219516591835170904bf82219c9da3c53137363a5a196e8`
- `tests/probes/guarded_wall_export.py`: `6896ca7683b4ee8759fcfe2eb407cfb607afc67d8cb050d84c9747d95db805e4`
- `tests/probes/upward_rigid.py`: `9cac980fdde864f99699b59bd8f86f8124f6e857e2ffb258e3f6e3655b404a79`
- `tests/probes/phase1024_ring.txt`: `02e71fc3dfbece2e751a3f96425ab35b44e5206aff49126823cee54f7d5da2b5`
- S_E: `eeb62a45f0dc278d887b63bed66c1d65f8e25f360431fc05963c601c96928e47`.
