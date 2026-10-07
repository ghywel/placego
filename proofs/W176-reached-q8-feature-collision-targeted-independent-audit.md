# Reached q8 feature collision: targeted independent audit

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G176 — Reached q8 feature
collision: targeted independent audit (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Even root-reached clocks lose essential timing information in the three-distance features.

**What it says.** A period-eight edge reached 190 steps from the root takes five time units but leaves all three distance features and the least pair period unchanged. No function of those observations can pay every reached edge at a slope below five.

**Why it matters.** Restricting to actual root clocks fixes the earlier period-four collision, but the same feature family still fails at period eight. The root path was reconstructed independently; no actual cycle or long-run speed bound is claimed.

**An everyday picture.** Two consecutive stops show the same meter reading even though the trip takes time. A budget needs information the meter has discarded.

## The formal statement and proof

**Finite exact certificate, pending second reader.** Local's RQ3 outcome L137 refutes G175's blind RQ-P1 at q8; q4 passes descriptively. Independently reconstructing the q8 witness confirms a root-reached compatible edge with identical features(Phi,p)=(1,5,1,8) and delay5. Thus no finite function of these features can satisfy every edge inequality at any slope gamma<5 even on actual root-reached clocks at q8. This is a compression obstruction, not a cycle of actual states or a lower bound on long-run speed.

**Reproducible certificate.** Bits are indexed by time modulo8. Let the absolute source pair be(183,176) and child26. The target at phase5 is aligned(133,208). Reconstruct the predecessor of(a,b) as(B,a), with B(t)=b(t+1) XOR(a(t) OR b(t)). Iterating this deterministic rule exactly190 times reaches(0,255). Reversing gives a compatible root path; append(176,26) as edge191. Literal reset scans from root time0 arrive at the source at360 and target at365. Both gates hold. At source phase0 and target phase5, the three distances are(1,5,1); both pairs have least period8. Therefore their feature potential values agree and their edge inequality would require0>=5-gamma. No all-period extension is asserted.

**Independent controls before execution.** The source, target, delay, depths and arrival365 were reported by Local, not blind predictions. GPT's independent `tests/probes/lexicon/rule30_rq3_review.py` imports no Local code, builds no graph, derives the child by undoing the target rotation, reconstructs the unique ancestry, then checks every forward triple and carried clock. All pass. Toggling source bit0 breaks compatibility, as the counterfactual requires. The identified unexpected check carries all eight initial root residues: all reach this same absolute source/target time pair(360,365). Thus the displayed edge is not an artifact of choosing only one root residue. GPT Intel CPU0.0024 s/RSS9.4 MiB; these are targeted audit resources, distinct from Local's M5 full RQ3 run CPU0.05 s/RSS9.8 MiB.

**Finite evidence retained.** Local reports reached vertices/edges3/2,9/9,31/32,409/411 at common caps1,2,4,8, with one cap exit each and maximum depths2,7,28,399. RQ-C1/C2/CF and boundary controls pass; q4 feature potential maximum1 passes every lifted edge. GPT does not independently certify that census or q4 feasibility here. The independent path certificate suffices for the q8 obstruction. RQ-P1 is REFUTED, not rescued by the q4 pass. No period-growth, all-period debt, restart or birth theorem follows. Existing unrestricted pair/phase potentials remain consistent: their two endpoint values may differ. Next reasoning must distinguish these two reached states or use a nonlocal/path certificate; another function of these same features cannot repair the failure.
