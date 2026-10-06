# injection memory plus one lag still misses deeper history

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT115. injection memory plus
one lag still misses deeper history (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Remembering the race and the last two steps still misses older information.

**What it says.** A description that includes whether the race happened and the last two observations leaves the
next error a coin toss, while the full history pins it down exactly.

**Why it matters.** A shallow check can wrongly suggest a model is complete.

**An everyday picture.** A doctor who asks only about the last two days misses the cause from last week.

## The formal statement and proof

### G115. Injection memory plus one lag still misses deeper observed pulse history (2026-10-06)

**Status:** exact finite-cone candidate-state counterexample; independent review pending. IS0-IS2 predictions and instrument published through114a83c before execution. This tests Local L070's injection-history repair in the isolated-pulse ensemble, not repeated random races.

Use the same8192 fair initial cone words as G113. Define F=E1, the actual injection indicator, and candidate X5=(F,K4,K5). Every positive injection happens at the fixed pulse time1, so adding its time or age at tick5 adds no further information. Refine each candidate bin by the full observed history H=(K0,...,K5). The instrument uses two independently checked update formulations and exact integer cross products.

The parent A={F=1,K4=(0,0),K5=(0,0)} has80 compatible words and40 next errors, so P(E6=1|A)=1/2. Its full-history child

    H=((0,0),(0,1),(0,0),(0,1),(0,0),(0,0))

has20 compatible words and no next error, so P(E6=1|H)=0. Both bins have positive probability in the infinite fair ensemble because only13 initial bits are needed. Thus the next-error law retains observed-past information not supplied by injection occurrence/time and one lag. The specified state is not sufficient at tick5, even allowing the known pulse phase.

A concrete word in the zero child is0101100010000 on-6..6. G113's independently checked positive cylinder0011110010000 lies in the same candidate parent and produces next error1. The zero conditional rate for the entire full-history child is certified by exhaustive enumeration, not inferred from the single zero word. Independent review remains required; no repeated-race or all-finite-orders conclusion follows.

**IS0-IS2 outcomes (2026-10-06 21:19 BST).** IS0 PASS:all8192 words, F=E3=001 indicator, bin totals and unaugmented0/896 versus40/1872 witness. IS1's blind split prediction HELD:24 unequal full-prefix refinements among18 candidate parents and112 full histories. A second witness has parent(F,K4,K5)=(1,(0,0),(0,1)), next-error24/48, while its zero-success full-history child has0/12. IS2's unexpected shallow-equality prediction HELD:zero unequal refinements when only K3 is added to X5. This is a controlled false reassurance: the K3-only diagnostic holds at this horizon while the complete observed past splits. No held finite diagnostic is promoted to closure. The unaugmented one-lag closure counterfactual remains refuted.
