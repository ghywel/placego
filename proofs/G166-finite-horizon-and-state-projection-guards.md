# finite-horizon and state-projection guards

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT166. finite-horizon and
state-projection guards (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

How long a timing budget takes to find says nothing about how large it is, and forgetting part of the state can
invent a loop.

**What it says.** GPT predicted that looking 4q steps ahead would find a timing budget for period q. Local's run
(HG4) refuted that at period 8, where 85 steps were needed, although the budget itself stayed small. G166 explains
why: the number of steps needed is the largest shortest route through steps that use up the allowance exactly,
ending where the remaining allowance is zero; it can be long while the budget is small. It also shows that a budget
remembering only the current stripe and the clock fails, since one real step costs q yet seems to return to where it
began; forgetting the clock fails as well.

**Why it matters.** It rejects two specific ways of forgetting state. Other compressions may work if they preserve
the distinctions those projections lose.

**An everyday picture.** A map that shows junctions but not which road you came in on can draw a roundabout where
there is only a dead end.

## The formal statement and proof

**Exact horizon diagnostic: tight-edge distance, not potential size (2026-10-07; symbolic, review requested).** Consider any finite directed graph with real edge rewards w, no positive-reward cycle, and stopping permitted at every vertex. Let h(v) be its least nonnegative feasible potential, equivalently the maximum reward of any finite walk from v, including the empty walk. G8 already proves finiteness by deleting nonpositive cycles. For an edge v->u set its slack s(v,u)=h(v)-w(v,u)-h(u)>=0. For any at-most-n-edge walk p ending at z, telescoping gives

    h(v)-reward(p)=h(z)+sum of the edge slacks on p.

Therefore h(v)-H_n(v) is exactly the minimum of this terminal potential plus accumulated slack over all such walks. In particular H_n(v)=h(v) if and only if some at-most-n-edge walk consists entirely of tight edges (slack0) and ends at h=0. All summands are nonnegative, so neither implication loses a condition. This also covers h(v)=0 by the empty walk and vertices with no successors.

Such a tight walk always exists: choose a minimum-length walk attaining h(v). An optimum exists among simple paths by cycle deletion. Its endpoint must have h=0, since otherwise a positive optimal continuation increases the reward; then the telescoping identity forces every traversed edge to be tight. Let d(v) be the shortest tight-edge distance to the zero-potential set. The first globally stable Bellman horizon is exactly max_v d(v): equality H_n=h is equivalent to n>=max d; and any equality H_(n+1)=H_n makes H_n a feasible potential, hence the least potential because H_n<=h. The shortest tight path is simple, so d(v)<=|V|-1. This is a finite graph bound, exponential rather than linear in q for the aligned pair domain; it supplies no all-period Rule30 budget.

**Identified unexpected check: allowed numerical weights do not control horizon.** On a directed chain take2L+1 edges with rewards(-1,+1) repeated L times, followed by+1, for L>=1. These weights have the exact numerical reset form2*delta-5 with delta2 or3. Every even-index vertex before the final leaf has h=1, every odd-index vertex has h=2, and the leaf has h=0. Every edge is tight. Thus max h=2 while the initial vertex has d=2L+1: all earlier even prefixes have reward0 and odd prefixes reward-1. No positive cycle exists. This refutes a generic inference from bounded potential size to bounded horizon, even with bounded positive reset delays and odd integer rewards. It is an abstract chain, not a claimed compatible or rooted Rule30 history. The zero leaf and empty-stop conventions are essential controls, and no computation was run.

**Application and next question.** HG4 failure concerns the tight-route length in the full gated graph. It does not by itself refute a potential magnitude O(q). Local's descriptive85, if its fixed-point computation is correct, means max d=85 in that finite q8 domain; this is an interpretation, not an independent global audit. A future horizon proof needs a compatibility theorem on tight paths, while the actual stage goal can instead bound h directly without a short-horizon theorem. This isolates two obligations that should not be conflated. No new universal bound, rooted counterexample or prize result follows. The reweighting/telescoping mechanism is standard shortest-path potential theory; see PRIOR-ART.md, not a novelty claim.


**Direct-potential restriction: the current driver and phase are insufficient (2026-10-07; symbolic, review requested).** At any dyadic q>=4, let b have its sole black bit at time q-1, let a=S b XOR b, and take arrival phase0. Then c=b is a valid child of(a,b), because S b=a XOR(b OR b). Both source(a,b,0) and target(b,b,0) satisfy G160's gate: a(q-1)=1 and b(q-1)=1. The source reset costs q, so the clock returns to phase0 and the edge reward at slope gamma is q-gamma.

Suppose a proposed finite potential has the form f(b,r), depending on the whole current driver b and relative phase r but forgetting the preceding word a. Its edge inequality here becomes

    f(b,0) >= q-gamma+f(b,0).

This is impossible when gamma<q. In particular no such potential can certify slope5/2 on the full gated q-domain for any dyadic q>=4. More generally a fixed finite gamma cannot be certified on all dyadic periods by this restricted family. The argument permits arbitrary dependence on q and arbitrary finite potential magnitude: changing constants, density, run lengths, difference orders or even retaining the whole b cannot rescue the family if a is discarded. This is a restriction on the potential's information, not a refutation of G8's two-word-and-phase potentials or G165's desired bound. Root reachability of these sources is not asserted.

**Identified unexpected check: the projected loop is not an actual repeatable cycle.** The target(b,b) has unique period-q child0: a black b resets c to0 and all intervening white times preserve c. Thus the actual next target is(b,0), not another copy of(b,b). The second reset also costs q, and the next zero-driver reset costs0. Forgetting a creates a positive self-loop in the projected driver graph from a valid edge, while the actual pair graph has no such self-loop here. Repeating that projected loop is invalid. The actual two-edge cost2q is a finite period-scale charge, consistent with an O(q) pair potential. At q4 the source is(12,8), its target(8,8), and then(8,0): both delays4 and rewards3, agreeing with HG4's known H0 rejection and G10's maximum6. At q2 the edge reward at slope5/2 is negative, so this specific obstruction does not apply; the dyadic q>=4 condition matters. No numerical run or new cycle census was used.

**Prior record and next intention.** G7's scalar compatibility/reset rule and G160's gate supply the calculation; G8 already keeps both words. This sharpens the earlier phase-loss guard by showing that preserving phase while discarding the preceding word also fails on the ambient gated domain. It is elementary state-projection reasoning, with no novelty claim. Next candidate charges must retain preceding-word information or explicitly exploit a proved rooted restriction. No claim is made that the rooted domain contains this family, and no additional Local computation is requested.


**G8 phase-free obstruction survives the arrival gate (2026-10-07; symbolic scope audit, review requested).** G8.2 already rejects a phase-free two-word potential on the full compatible domain at every slope gamma<3. It is not a new cycle discovery. The remaining scope question is whether G160's gate removes the individually maximizing phases used in that proof. It does not. For G8's cyclic list of period4 words the following exact table supplies a gated maximum-delay phase on each edge; a is the preceding cyclic word and b the listed driver. Time bits are least-significant first.

| b | a | arrival r | a(r-1) | delta(b,r) |
|---|---|---|---|---|
|9|13|1|1|3|
|8|9|0|1|4|
|14|8|0|1|2|
|12|14|0|1|3|
|4|12|3|1|4|
|7|4|3|1|2|
|6|7|3|1|3|
|2|6|2|1|4|
|11|2|2|1|2|
|3|11|2|1|3|
|1|3|1|1|4|
|13|1|1|1|2|

Each source is gated, each triple is the existing compatible G8 triple, and each target is gated by G160 closure. A finite phase-free g(a,b) that satisfies the edge inequalities for all gated states must satisfy each independently chosen row. Summing cancels the cyclic pair potentials and gives36<=12*gamma. Hence gamma>=3 remains necessary even on the gated domain, at dyadic q4. The existing phase-sensitive q4 certificate at gamma5/2 is consistent with this distinction.

**Identified unexpected check and counterfactual.** The selected phases need not concatenate into one physical front. Their use is valid precisely because g forgets phase and must satisfy all gated instances separately. Claiming a real36-step compatible clock cycle would be false: G8's coherent recurrent circuit has elapsed28. If even one of the displayed maximizing phases were excluded by the gate, the old unrestricted proof could not simply be imported; all twelve gate bits have instead been checked explicitly. No new computation was run. This is an exact scope extension of G8, using G160, not a new general potential theorem.

**Working restriction after the two projection guards.** On the full gated domain, neither discarding a while retaining(b,r), nor discarding r while retaining(a,b), can support the desired below3 certificate. These facts do not prove that every successful statistic must store the full pair and phase; other compressions or a rooted-only restriction remain possible. The next direct-charge argument must preserve the distinction each proposed compression erases, rather than transfer an unrestricted graph result without checking its gate. No rooted debt lower bound or prize conclusion is claimed.



*Second reader's note on G166 (Local L127, 2026-10-07).* The tight-edge distance identity and both projection obstructions are correct. S60 checks equality of tight distance and stabilization at horizons4,21,85 for q4,6,8 and the abstract chain controls. S61 checks all twelve gated phases and the compatible q4 cycle. The audit initially imported HG4's module-level CPU limit and lost later output; Local moved the limit to main() and repeated the audit. The corrected complete audit passes; the earlier incomplete run is not a pass.
