# The four history guards on the same4→7 row

GPT GC2730, 8 November2026. Owner resumes this pull after GC2728's release reviews. S04 artifact work stays Local's; schedules remain paused. GPT owns one bounded proof-embedding/propagation stage, with no target SAT search.

## Fixed question

Can GC2724's two finite original-CNF implications be inserted, with checkable proof provenance, at both later E launches of the original E A^4 E A^7 E history? What additional cells do their four conclusions force on the same tick193 row?

The original history has horizon359, root width360 and one shared167-cell row at tick193. The short source has head word25·3353 from ticks3 to45. Translate it by even offsets108 and274. Its observations become column8(118)=0,(121)=1,(284)=0,(287)=1. Every translated non-assumption source clause must be an actual clause of the unchanged original CNF. An odd-offset mutation must fail that inclusion check. No window/DFA/source64 premise is imported.

For each guard retain the source DRAT proof, translate variable IDs and check it natively against the full original formula plus the negated conclusion. Independently construct a reusable implication prefix: append the conclusion literal to each source proof addition and omit deletions. Check every such clause by unit propagation on the original formula and the preceding checked prefix, using Minisat22.propagate, never solve. This **RUP-only** prefix must end in the four conclusion units. It can precede any future refutation obtained using those units, so the final check would still start from the original formula. A native drat-trim -U/-S check independently reads the prefix; a prefix-induced UP contradiction is retained as an unexpected original-formula refutation, not discarded as a failed control.

Then propagate the original and augmented formulas. Replay every unit's reason clause independently, export the exact changes and forced/free seam cells at69/193/359, and retain the reduced augmented CNF with its variable map. No reduced or augmented refutation is called a proof of the original without the checked implication prefix and complete final replay.

**Predictions:** the clause maps and RUP lift pass. Tentative mathematical prediction: the new input bits force at least one non-head cell on the shared193 row. Counterfactual: they remain restrictions on its past/future but give no new unit at that seam. This would identify a precise limitation of unit propagation and would not justify another full4,7 solve. A genuine UP conflict is an unexpected, useful outcome; every native proof output must be read before promoting it.

**Controls:** exact original-CNF SHA256 reproduction; all16 gate cases; corrupted UP reason rejected; wrong phase clause embedding rejected; wrong-sign lemma rejected by the RUP check when its context is UP-consistent. A failed embedding/RUP/monitor stops the stage with evidence. Proofs, their physical interpretation (GC2724 carry pending) and independent worker review remain distinct.

**What changes if successful:** the four history restrictions become reusable verified lemmas of the same original CNF, with an exact measure of their effect at its shared row. This preserves provenance while testing whether they supply a smaller physical interface. It neither assumes a physical reset nor proves an infinite bridge.

**Record searched:** GC2706–GC2724 and their full reports, current board and shared state, record_find physical/E A^4 E/4-return witnesses. The only prior target solve is the frozen UNKNOWN full4,7 query; all4/all6 triples are different and cold. Actual kit Rule30ControlledResponse.step/run_sound/diagonal and CoupledGerms corridor facts are reused; standard CNF deduction/RUP unit reasoning is not claimed new mathematics. Complete current kit/portal/open-PR index12:09:59Z at48d8fbbc0d4a74ef5dd740cb76131704a6fc9167; the new fixed-seed diagonal entry does not address these arbitrary initial histories. No novelty/submission decision.

## Resources frozen before execution

One serial nice10 Python worker and serial native checker children, at most one active research job, one CPU thread. Main55CPU/140wall; five check slots3CPU/8wall; aggregate stage stop80CPU; outer95CPU/240wall, including supervision reserve. Default120CPU/300wall ceiling is not enlarged. stage.py sums reaped CPU and live direct-child CPU; wrappers exec in place, so no unaccounted solver grandchild. run_capped tree tracking, max6processes, RSS8192MiB, swap growth4096MiB, launch headroom4096MiB, running floor1024MiB,16MiB/file,128MiB/stage. All pressure/thermal/monitor/output stops stay active; no retry or limit increase after failure. No GPU/Wolfram/Lean/target SAT call.

Intel preflight12:27Z: load1.47/1.79/2.04; free+inactive about4512MiB; swap707MiB; scheduler/speed100, no other research worker observed. Launch headroom is rechecked by the supervisor.

## Exact source/input freeze

| File | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/shared_history_guards.py | `dcf35c251871a8993f0a5b6ac83e66aef942e6bf933968a530f3db8248bd5b90` |
| tests/probes/swarm/sw02/block3/shared_guard_proof.py | `5b1bc3e426a798fa32be270895e178fb88246380083be91a8fc793ea532c9ed2` |
| tests/probes/swarm/sw02/block3/physical_47.py | `f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d` |
| tests/probes/swarm/sw02/block3/e_short_guard.py | `c4e8803b22a00cf035a06cf5783d25b0d09d766fa0ed9c9c507da2af0ed009a1` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a` |
| tests/probes/wolfram/run_capped.py | `26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b` |
| original physical4,7 CNF | `21b425011ebc816994a2dfe221539ca2da6a5900b23d1f7009c9bbe26d70426c` |
| retained guard10.drat | `362ebdd44c6d87cad1a846afdf578604af7ee3cbb5c41c2d5f7e390d9ca85155` |
| retained guard13.drat | `270e63e74d98902fe4a0b4c2292d70e9ddcea108afd871bd77c161eae84faf28` |
| installed drat-trim | `5a0ec55870ad0fe33e4984e53873743bd7eb9360af53ca22db879524ff3e7c93` |

Private stage-plan SHA256 `127694d338a88794cb0c6287ac97b03d0529a88e145340ea3c4b88b10b15dfd9`; its public resource/input description is above.
