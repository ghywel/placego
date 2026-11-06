# Returned bridge read and class-amplifier carry

GPT, GC2711, 6 November 2026. The owner asks for Cloud CL753 and Local L1578 first, then continuation of the physical bridge pull. No new simulation or build was needed for these reviews.

## Cloud CL753: accepted, with follow-on guards

I read the complete [Cloud report](CLOUD-BRIDGE-RETURN-REVIEW-20261106.md), its two replay programs and their outputs. Cloud supplies the independent worker read requested in GC2706/GC2709. The following are now **PROVED hand/two-party**, with their original hypotheses:

1. The induced complete-E return machine, exact unary labels and full-future quotient.
2. The sharp conditional mean clock 145/2 sampled steps and its finite endpoint corrections.
3. Post-image inclusion and the existence of an abstract cycle in a stable nonempty fibre, with free exteriors.
4. The physical seam equivalence, retaining phase, width and both past/future head guards.
5. The known diagonal identity and unique high-tail completion, including zero and width endpoints.

Cloud's own-code replay corroborates the finite table calculations. It does not rebuild Local's original window graphs, so their 128-bit subset-hash/completeness caveat remains. The physical SAT result is still UNKNOWN. No physical 4→7 witness, infinite realization or capture theorem follows.

Cloud's proposed one-cycle lift needs two corrections. The path 6,4 is not repeatable at widths 39–41: it ends in S, which rejects the next 6. The primitive 6 self-loop costs 76 sampled steps; 4,8 is a closed two-return path of total 152. Also, requiring the entire spacetime strip to have the head's period could miss a periodic head supported by longer-period or aperiodic farther columns. An exact phase-augmented finite graph must allow all such supporting temporal cycles. Compatible lifts at every width can give an infinite right-half history by compactness; they do not give an eventually white tail. Finite persistence gives neither conclusion. The proposal remains an alternative, with no established cost advantage over SAT and no automatic run.

## Local L1578: carrying verdicts

I read the complete [report](SW02-CLASS-AMPLIFIER.md), preregistration, all its Python/C sources and the digest-verified raw packet. Two GPT assistants checked the counting and sector arguments as self-checks; the verdict below is GPT's read of Local's proof. The report has been amended in place, preserving the original predictions and failed approaches.

**Theorem C — PASS.** Width grows by two under G. An asynchronous G-class therefore occupies exactly one parity of widths, starting at its minimum v_C; a minimum representative supplies every larger width of that parity. For fixed W there are finitely many initial rows. Choose a common time after every mortal row has failed and every coalescing equal-width immortal pair has merged. Late distinct rows correspond exactly to pairs (class, initial width). Hence

q(W) = Σ_C max(0, floor((W − v_C)/2) + 1),

q(W) − q(W − 2) = o(W),

where o(W) counts classes with v_C ≤ W and q(V)=0 for V<0. No uniform bound on the stabilization time is asserted. Unbounded class count is equivalent to q(W)/W tending to infinity; a finite total o gives q(W)=(o/2)W+O(1).

A new class increases the slope; superlinear amplification requires unboundedly many classes. Finite edits of a temporal trace preserve its eventual tail, by `Rule30PrefixMerger.trace_tail_iff_row`. Finite spatial edits need not preserve a class. The corresponding trace characterization of G-classes uses every pair of **even** time shifts. Guarded predecessors can lower a class's minimum width without creating a new class.

**Theorem S — PASS with explicit witnesses.** Set K=87,867 and read the highest K cells of a row Y inward as V_K(Y). For width(Y)≥K, direct substitution in F(Y)=(Y>>1) XOR(Y OR(Y<<1)) gives

V_K(FY) = L(V_K(Y)) mod 2^K, with L(v)=4v XOR(2v OR v).

New depth j reads only old depths j−2,j−1,j; the moving white boundary is outside this strip. For each kit word v in {A0,A1,B0,B1}, take X_v=reverse_K(v). The kit's boundedness and oddness give width(X_v)=K. The row 2^m X_v has the same strip and shift zero, with width K+m. Taking m=0,…,15 realizes all sixteen phases of all four primitive, pairwise distinct strip orbits. This avoids the unjustified claim that padding an arbitrary short row preserves its strip.

The invariant (strip, shift−width mod 16) is constant under F and hence on G-classes. At most k immortal classes occupy at most k of the 64 positive-natural sectors. **One** class leaves at least **63** sectors without immortals; two classes leave at least 62. Zero is outside this sector partition. None of the constructed witnesses is asserted immortal.

Primary source checked at kit `9d837cd5e5ac447cd868c20aebf49a1b4cfa866e`: `Rule30FourLeftSides.rows_finite`, the four return/primitive/distinctness facts, `odd_reaches_one_of_four`, `least_period_16`; the bit recurrence in `Rule30UniversalLeftSide`; and the complete `trace_tail_iff_row` statement/proof in `Rule30PrefixMerger`.

**Lemma R — PASS under the stated AM-5 premises.** If P=Per_d(x)≥Q, both are powers of two, so Q divides P. In the periodic intertwining identity Ψ(T^k x)=T^k b_(r+k), compare k and k+P. The 1-Lipschitz property and matching b-phase give T^(k+P)b=T^k b modulo 2^d. Cancel T^k, a permutation, to obtain Per_d(b) dividing P. Choosing k in each Q-phase covers every b. No transitivity is used. This carries the lemma conditional on the periodic-intertwining hypotheses, not every structural claim of AM-5. Lemma G is also valid as a restatement of the finite-radius and width-cost assumptions; an empty output interval is vacuous.

The all-row counting analogue in §3 is valid for the true limits M(W). The displayed finite-time differences ΔN_4096 are not certified class births. A plateau is an upper bound on the limiting count, not a proof of permanent nonmerging.

## Evidence corrections and limits

- Reading the raw rate rows reproduces 469 exclusions among 512 odd values in the sharp test. The e_36=9 example is **817**, not 13. Seed 13 has e_36=13, as does seed 1.
- This refutes pointwise minimality of seed 1. A finite table does not refute the registered asymptotic bounded-gap version of P5; that remains unresolved.
- Period 8 through tested depth 400 means wheels 0–399. The kit's wheel 400 already has primitive period 16, and appears at depth 401.
- The finite phase comparison does not establish independence. The damage median 0.2535 is within the cited 0.246±0.01 interval.
- Candidate H remains open at all radii. A proposed memory-flush identity would need further uniform-radius and extension arguments before a whole-line centralizer result applies.

The computations remain Local/M5 measurements. GPT inspected their data and recomputed summaries, without rerunning the simulations. Evidence: `cited/local/class-amplifier-20261106.tar.gz`, 78,594 bytes, SHA256 `ab8e6f4d3f3eb04f6cc78970156c017ac624e4ab2b8e176ae31f184c02a987ed`.

**Record searched:** GC2698–GC2709, CL753, L1578, AM-1/2/5, the exact kit sources above and the retained source index. The complete `known_find.py --new` refresh finished at 2026-11-06T22:24:21Z, kit hash above, 33 open PRs, zero added/changed/removed entries. No novelty or submission decision is made here; no clean keyword search is being treated as clearance.

**Continuation:** GPT now takes the fixed L1569 real-history fixture R=2,135,555, retaining its actual phase and both excursion anchors. Locate the first head guard that rejects a shortened return, then ask whether it reduces to a short jointly forced tail restriction. No census, larger window, blind SAT retry or schedule restart.
