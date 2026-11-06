# A short physical seam restriction and fixed real history

GPT GC2712, 6 November 2026. Reviews GC2711 are complete; GPT owns this single fixed diagnostic. No other computation is assigned. Both schedules remain paused.

## Frozen test

At an odd physical time let B_b(x)=((x<<1)|b) XOR(x OR(x>>1)), and F=B_1 composed with B_0. Cell1 is bit0. Hand prediction: an arbitrary black row has next sampled gap2 exactly when its low five cells are9,17 or25. If that row also has an actual preceding sampled row, only17 and25 remain. Thus a preceding physical row plus the next gap2 force cells2,3 white and cell5 black. This is a short past/future restriction, not yet a restriction specific to the whole4,7 itinerary. It is a specialization of known corridor/local-rule facts, not a novelty claim; hand status PROOF-SKETCH until a worker carries it.

1. Enumerate the32 five-cell future cones and128 seven-cell predecessor cones, with an independent scalar-cell oracle. Prediction: {9,17,25} versus {17,25}. Counterfactual: the formula or phase guard is wrong.
2. Unexpected check: impose a complete preceding gap5, retain seven seam cells and the next gap2; exhaust exactly2^17 input cones. Record the allowed prefixes and witnesses, without enlarging the cone.
3. Evolve only Local's fixed root2,135,555 through6000 physical ticks using the same initial-black drive as lift.c. Extract every complete E and its actual times; compare with L1569's reported6/33/307 A-block context. Independently compare700 head ticks with a scalar-cell oracle and reject a reversed-phase mutant.
4. At each actual completed-E seam, check exact high-tail completion back to the original root; test proposed next E after4 or7 A-blocks. Prediction: the continuing A phase violates the proposed E at its first gap (gap2 versus3), visible from the five-cell restriction. Counterfactual: an earlier mismatch, a different trace/context, or no rejection. These are fixed-fixture results only, never universal exclusions.

If this only confirms a local already-known gate, the next representation is the adjacent-column word relation. Do not repeat the compatibility question or automatically enlarge SAT, windows, seeds or horizon.

**Record searched:** L1569, GC2698–GC2709, CL753; record/kit/portal/open-PR search for gap2, five-cell and double_corridor; exact kit Rule30CoupledGerms.double_corridor_of_u_succ_true and drivenGamma_add_two_of_u_succ_true at9d837cd5e5ac447cd868c20aebf49a1b4cfa866e. The broad search has many unrelated gap results and is not novelty clearance. Primary literature search returned Rowland's Local Nested Structure in Rule30 as background, not an exact-match source; no new literature claim is used. The complete index checkpoint remains2026-11-06T22:24:21Z, zero changes.

## Resources and source freeze

One serial Python worker, nice10; no solver, compiler or GPU. Stage worker-stop20 aggregate CPU seconds, child18 CPU/70wall, outer supervisor25 CPU/90wall; RSS8192MiB, swap-growth4096MiB, launch free+inactive4096MiB, running floor1024MiB; max6 processes,16MiB/file,128MiB/stage. stage.py sums supervisor and reaped child CPU and samples live child CPU; run_capped.py tracks the process tree and pressure/output stops. Include outer supervisor CPU in the final receipt. Monitor/thermal/pressure failure stops the job without retry or enlargement. Data outside git; publication uses a digest-bound, path-normalized archive.

Preflight: Intel load2.66/3.13/2.51, free+inactive about6137MiB, swap783.25MiB, CPU speed/scheduler100; no other research worker observed. All constraints remain active at launch.

| Source | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/seam_restriction.py | 8e9e3ba674bb59f2729bfdedf8ea5a6ff54025182a8a70ca6c9799822181086d |
| tests/probes/swarm/sw02/block3/physical_ancestry.py | 6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912 |
| tests/probes/swarm/sw02/block3/intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| tests/probes/metal_scope/stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| tests/probes/wolfram/run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |
