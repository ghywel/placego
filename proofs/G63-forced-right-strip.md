# forced right strip

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT63. forced right strip
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

While the visible signal holds steady, each column on the right is forced into a fixed rhythm too.

**What it says.** In Rule 210 with the blinking wall, if column 1's visible signal is constant over a stretch, then
columns 1, 2, 3, ... on the right are each forced into a fixed repeating pattern over that stretch, shortened a
little at each end for each column further out.

**Why it matters.** It replaces G61 and G62's single-square restrictions with a whole forced strip of the right
half.

**An everyday picture.** A row of dominoes: once the first stands still, the next ones must stand still too, except
near the ends.

## The formal statement and proof

### G63. A constant effective run forces a right strip (2026-10-06)

Question from G037: can G61-G62's individual gate restrictions be replaced by a strip statement? The following local extension lemma does so. This is derived from Rule210's recorded truth table and the parity subsystem in G28; a targeted record search for period-six/constant Rule210 strip statements found no matching entry. It is not a literature novelty claim, a full-realization construction, or a finite-seed exclusion.

**Local extension lemma.** In a Rule210 orbit let neighboring columns L,C have constant two-phase temporal values on an integer time interval I=[A,B], inclusive. Write their (even,odd) pairs as L=(l_e,l_o), C=(c_e,c_o), each in{00,10,01}, with disjoint occupied phases: l_e*c_e=l_o*c_o=0. Then the next column R is forced on[A+2,B-2] to the pair

    R=(c_o XOR l_e, c_e XOR l_o).

No temporal periodicity assumption is imposed on R or any farther column. If C=00, its own update gives R(t)=L(t), using C(t+1)=0, and the formula follows. If C=10, its odd-time white update forces R(odd)=1 XOR l_o, while its even black update requires l_e=0. Put b=1 XOR l_o. If b=1, R is black at the preceding odd time; its own update then forces its next even value to C(odd)=0, independently of the farther column. If b=0 and an even R were1, its own update would force the next odd R to C(even)=1, contradicting the known odd0. Thus R(even)=0 in either case. The case C=01 is the parity-swapped argument, giving R(odd)=0 and R(even)=1 XOR l_e. Trimming two steps at each end ensures every preceding/following sample and C update used lies in I. These cases prove the lemma and show the output remains in{00,10,01}, with opposite occupied phase to C whenever nonzero.

**Strip corollary for0101.** Suppose s_n=x(1,2n)=a is constant for m<=n<=N. G61 forces d_n=x(1,2n+1)=0 for m<=n<N, since a constant transition is not0-to1. Thus columns0 and1 have pairs v_0=01, v_1=(a,0) on[2m,2N]. Iterating the lemma gives, for every k>=1 with a nonempty specified window,

    column k has pair v_k on
    [2m+2*(k-1), 2N-2*(k-1)],
    v_(k+1)=swap(v_k) XOR v_(k-1).

The vectors repeat spatially with period6. For a=0, v_0..v_5 are01,00,01,10,00,10; for a=1 they are01,10,00,10,01,00. In both cases direct recurrence gives v_6=v_0 and v_7=v_1, proving repetition. Neighboring forced columns have disjoint black phases, so every adjacent pair wholly inside their common forced time window has nonlinear product0. This is a growing, parity-linear right strip on the interior of a constant effective run, not just one gate's support. In G26 the effective dyadic runs grow without bound, so any full realization of that particular empty-left system has arbitrarily wide such strips.

**Unexpected boundary guard.** Dropping the temporal margin is unjustified. In the local layer system L=00,C=10 on[0,7], choose R=11 at times0,1 and thereafter R=01 (even0,odd1). C's updates and R's updates admit a farther-column stream, yet R(0)=1 disagrees with the predicted pair01. The preceding odd sample outside the interval is missing. This is a counterexample within the stated local layer equations, not an assertion that the farther stream itself has a full evolution. It shows why the lemma's proof must retain its time-window premises. The two-step margin is conservative; no optimality claim.

The corollary does not force the entire right half at one time or make every nonlinear event vanish eventually. Growing strips inside growing intervals can coexist with activity at their edges or farther right. G59 therefore still supplies no finite-seed contradiction. Full mixed-parity finite witnesses remain open.

**Next controls, preregistered NOT RUN.** ST1: enumerate all7 disjoint-phase pairs(L,C), all256 eight-bit R words on[0,7]; retain exactly those satisfying C's seven updates and admitting seven farther-column bits for R's own updates. Every accepted R must match the lemma on[2,5]. ST2: check both six-phase spatial cycles and their disjoint-phase property through60 columns. CF: the same forcing holds at every endpoint with no margin; must fail on the specified L=00,C=10,R boundary guard. These are local controls, not finite/full orbit searches. Independent Local reading requested; next run them before using the strip quantitatively.


### G63 controls outcome (2026-10-06)

ST1 passes all7 disjoint-phase pairs and1792 candidate eight-bit right words; exactly15 words admit both layers' specified updates, and all15 agree with the predicted trace at times2..5. ST2 passes both period-six patterns through120 column-phase values and118 neighboring phase pairs. The no-margin counterfactual is refuted by the accepted local boundary word with R(0)=1 instead of0. Probe: `tests/probes/lexicon/rule30_gpt_strip.py`, Python on GPT's Intel host, under1 s. No control failed.

These checks are local temporal layers, not full realizations of their farther streams; the full-orbit corollary uses the analytic lemma. G63 remains awaiting Local's independent reading. The bounded strip control block is complete. Next examine temporal block complexity for a fixed right column: the growing dyadic-run strips may leave only logarithmically many unconstrained windows. Any entropy claim needs a uniform bound over arbitrary starting times, not just a count of prefixes from time0; no such bound is claimed here yet.
