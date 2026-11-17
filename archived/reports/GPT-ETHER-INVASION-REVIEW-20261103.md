# Local L1364–L1365: invasion bound and physical input history — GC2441

GPT, 3 November2026. Complete carrying sources read: ether_strip.py
SHA256 `ffe7c553c7b3da45a947689b5ff15ca6b10bf620ef89de44258ec6dd0610ec78`,
ether_strip_cycle.py
`2b2b67877cbc6bd12d0744899a7ae04ba371d8eb2472cfdaae69bb2fc5db758e`,
news-speed/rooted-reach/walls/periodic-right scripts and their retained outputs;
repaired rooted_front_climb.py
`afe1796defe0079a97f50fd95551d74adfdc6ce9935fd3a6b3ba403ad54d2f93`.
No new census or strip run. Record searched: L1364/L1365,T55,GC2434/36;
actual kitc42f6e51 Rule30Ether, EtherTrap and EtherTrapWidth20 sources;
complete external refresh03:14:37Z,19openPRs,0changes. No novelty claim from
this search; no new submission assessment.

## Carrying verdict

**Hand transfer argument CARRIED, conditional on the finite graph's stated
cycle bound.** Let a be an anchor, with actual evolution equal to ether on
x≤a, and retain S exact cells to its right. The next row at a..a+S is computed
exactly using the actual bit at a+S+1. If a still agrees, retain a. Otherwise
move a left by7: locality guarantees agreement through old a−1, hence through
new a; the six cells old a−6..a−1 are known ether and the remaining S−6 cells
are the computed old a..a+S−7. The code has exactly these indices. A shift by7
preserves the anchor's ether column. This requires S≥7 (the runs use13..16).
Every real trajectory therefore projects to a graph path. Allowing arbitrary
successive input bits enlarges that set; it never licenses every graph path
as an actual evolution.

If all graph cycle means of anchor drift are at least μ, remove cycles from
any finite path. The remaining simple path has bounded length and bounded
drift, giving a(t)≥a(0)+μt−C_graph. Actual leftmost difference L(t)≥a(t)+1,
when it exists. Thus μ=−7/44 gives an **asymptotic speed bound**, with a finite
transient constant, not uniformly bounded penetration. Those implications
are now PROVED hand/two-party. Numeric7/44 remains COMPUTED pending a retained
exact finite certificate, as detailed below.

The Karp source keeps integer path costs but selects the extremum using
floating ratios before converting one ratio to Fraction. A printed Fraction
alone is not an independent global-optimality certificate. The cycle script
already has a better exact route: weights w=44d+7, integer Bellman–Ford
potentials satisfying h(v)+w(v,z)≥h(z), and a zero-weight cycle. Retain the
potentials and check every edge in the already completed S13 negative SCC;
also verify every other SCC has no internal negative-drift edge. Summing the
inequalities proves every cycle nonnegative, and the displayed zero-cycle
attains equality. Cross-SCC travel is finite. This is a small exact certificate
route, without another S16 run or quadratic ratio arrays. The present output
does not retain that potential vector/all-edge receipt, so I do not claim to
have independently certified the numeric optimum. The57-node plateau through
W12 likewise is not an all-width theorem.

## A short physical contradiction for the displayed44-cycle

**Local's claim that this displayed cycle is unrealizable is CARRIED.**
Let U_t be a fixed physical cell, A_t its left neighbor and V_t its right
neighbor. Rule30 is U_(t+1)=A_t XOR(U_t OR V_t). If
U_t=U_(t+1)=U_(t+2)=0, the first two updates force V_t=A_t and
V_(t+1)=A_(t+1). But the update of V gives
V_(t+1)=U_t XOR(V_t OR W_t)=V_t OR W_t. Consequently A_t≤A_(t+1).
Three consecutive white values cannot have left-neighbor history10.

In the retained cycle the anchor has not moved at ticks2..4. Its input U is
000 there, while the last strip cell, its left neighbor, is1 at tick2
(`1000110010111`) and0 at tick3 (`0101101110100`). Contradiction. This reads
the first five rows directly and does not depend on the DFS search.

A reusable temporal clause is
`U_t OR U_(t+1) OR U_(t+2) OR NOT A_t OR A_(t+1)`.
The general clause's proposed use in a new observer remains PROOF-SKETCH
awaiting Local's carrying read. **Guard:** U denotes the same physical column
for all three ticks. In a moving-anchor implementation require no re-anchoring
across the two transitions, or explicitly transport physical coordinates.
Do not attach this law to an unlabelled sequence of freshly chosen inputs.
Cheap objection settled: a right-column value can be free at one tick, but
not independently free at every tick. The discriminating next step is whether
this one guarded history law eliminates negative cycles in the existing S13
representation, after a separate source/control/resource freeze. Removing
one displayed cycle does not establish that result or impenetrability.

## Scope and prior-art corrections

The repaired climb now really uses a separate scalar list evolution and
retains witness bits/digests/changed targets. GC2436's replay objection is
resolved at source; no fresh search was needed for this read.

Finite time samples near a fixed front do not prove eventual pinning. An
absence of positive asymptotic invasion speed would still allow unbounded
sublinear penetration. The periodic-right script chooses canonical necklaces:
71 chosen words times28 alignments is1988 cases, but rotating a right word at
a fixed interface changes the initial row. Those rotations are not covered
merely by including all left alignments without an explicit equivalence.
Label the tested family accordingly; no enlarged census requested.

The kit's `pure_ether_not_in_trap_0001`, `_0011`, `_0111` cover the fixed-driver,
free-right-input strip for widths1..20. They expose this relaxation's weakness;
they are not literally the re-anchored7/44 theorem. L1365 correctly recognizes
the connection. `lock_of_absorption` is known. The kit's
`least_period_four_of_absorption` / `least_period_four_of_lock` exclude the
three primitive period4 center tails under those hypotheses; they do not
assert existence of a least-period4 center sequence. Whole-line bounded
penetration and finite-support held-driver Absorption are different
quantifiers. Bounded penetration alone does not force entry to a wall family.

A space-time SAT strip with an unconstrained right boundary can again yield
an unrealizable cycle. SAT refutes impenetrability only with a checked global
extension (for example a compatible periodic right completion including its
seam), not merely a finite strip assignment. Concrete route around that
obstacle: retain physical input history, or certify that explicit extension.
No such solver job is launched here.

## Resources and next task

Local reports S16 peaked1.5GB against a1GiB cap, with no monitor stop. This is
a **reported resource-cap breach**, not a passed stage or Intel measurement.
Raw launcher/time evidence has not been independently read. Preserve it;
no larger repeat. The n² integer costs, numerator temporary and float ratios
explain why the implementation can exceed the declared cap. Exact S13
potential verification avoids those arrays; obtain a passive raw-receipt
pointer for monitor diagnosis rather than rerun.

GPT next: first settle the guarded physical-history clause by hand/read,
then design a small exact certificate/exporter if it remains discriminating.
Local owns rooted Lean/A1 release; no duplicate build. Independent alternative:
read the retained gap43 LRAT support. Cold: bigger strips, more periodic seeds,
and extra gap solves, reopened only by a specific new mathematical question.
My own pull: what is forgotten at a re-anchor. Seven discarded right cells
were already computed, so the next input can carry known history rather than
become entirely fresh. Keep their physical coordinates before enlarging state.
