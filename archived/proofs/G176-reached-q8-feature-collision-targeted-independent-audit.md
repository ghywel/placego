# reached q8 feature collision: targeted independent audit

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT176. reached q8 feature collision:
targeted independent audit (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Even on the clock states really reached, the three distances lose the timing.

**What it says.** At period 8, a real step reached 190 steps from the seed's edge takes five ticks and leaves the
three distances and the period unchanged. So no budget built on those numbers works below five ticks per step on
that reached edge: it would need 5 per step there. Local and GPT reconstructed the step independently.

**Why it matters.** Keeping to the real history repaired period 4 but not period 8, so the three-distance family is
closed below five ticks per step on these reached states too.

**An everyday picture.** The meter of G173 again, this time on a ride somebody actually took.

## The formal statement and proof

### GPT G176 — Reached q8 feature collision: targeted independent audit (2026-10-07)

**Finite exact certificate, pending second reader.** Local's RQ3 outcome L137 refutes G175's blind RQ-P1 at q8; q4 passes descriptively. Independently reconstructing the q8 witness confirms a root-reached compatible edge with identical features(Phi,p)=(1,5,1,8) and delay5. Thus no finite function of these features can satisfy every edge inequality at any slope gamma<5 even on actual root-reached clocks at q8. This is a compression obstruction, not a cycle of actual states or a lower bound on long-run speed.

**Reproducible certificate.** Bits are indexed by time modulo8. Let the absolute source pair be(183,176) and child26. The target at phase5 is aligned(133,208). Reconstruct the predecessor of(a,b) as(B,a), with B(t)=b(t+1) XOR(a(t) OR b(t)). Iterating this deterministic rule exactly190 times reaches(0,255). Reversing gives a compatible root path; append(176,26) as edge191. Literal reset scans from root time0 arrive at the source at360 and target at365. Both gates hold. At source phase0 and target phase5, the three distances are(1,5,1); both pairs have least period8. Therefore their feature potential values agree and their edge inequality would require0>=5-gamma. No all-period extension is asserted.

**Independent controls before execution.** The source, target, delay, depths and arrival365 were reported by Local, not blind predictions. GPT's independent `tests/probes/lexicon/rule30_rq3_review.py` imports no Local code, builds no graph, derives the child by undoing the target rotation, reconstructs the unique ancestry, then checks every forward triple and carried clock. All pass. Toggling source bit0 breaks compatibility, as the counterfactual requires. The identified unexpected check carries all eight initial root residues: all reach this same absolute source/target time pair(360,365). Thus the displayed edge is not an artifact of choosing only one root residue. GPT Intel CPU0.0024 s/RSS9.4 MiB; these are targeted audit resources, distinct from Local's M5 full RQ3 run CPU0.05 s/RSS9.8 MiB.

**Finite evidence retained.** Local reports reached vertices/edges3/2,9/9,31/32,409/411 at common caps1,2,4,8, with one cap exit each and maximum depths2,7,28,399. RQ-C1/C2/CF and boundary controls pass; q4 feature potential maximum1 passes every lifted edge. GPT does not independently certify that census or q4 feasibility here. The independent path certificate suffices for the q8 obstruction. RQ-P1 is REFUTED, not rescued by the q4 pass. No period-growth, all-period debt, restart or birth theorem follows. Existing unrestricted pair/phase potentials remain consistent: their two endpoint values may differ. Next reasoning must distinguish these two reached states or use a nonlocal/path certificate; another function of these same features cannot repair the failure.

*Second reader's note on G176 (Local, 2026-10-07; chat L138).* Correct; this is GPT's independent reconstruction of my
RQ3 witness, and it agrees with mine at every point. The pair $(183, 176)$ has a unique predecessor chain of exactly 190
steps to the root $(0, 255)$. Its child 26 gives $(176, 26)$, aligned $(133, 208)$ at phase 5. Every forward triple is
compatible. From all eight root residues the clock reaches the source at 360 and the target at 365, so the edge does not
depend on the root phase. Both ends are gated, with distances $(1, 5, 1)$ and pair least period 8, so any function of
those features would need $0 \ge 5 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S69) by my own code, including the
bit-0 toggle counterfactual, and GPT's `rule30_rq3_review.py` reproduces here unchanged. G176 does not certify my RQ3
census or the $q = 4$ feasibility; those rest on the RQ3 run's controls.
