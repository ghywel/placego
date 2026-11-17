# Certificate inventory: source review and corrected proposer contracts

GPT, GC1868/MI800, 2026-10-25. **Review COMPLETE WITH CORRECTIONS.**
All 44 lines of CERTIFICATES.md at
`57d15812c4e0eaab95eadbc35aa303b4bd1d20a0` read. Useful taxonomy, but its
side-condition column is not yet a safe specification for a learned proposer.
This is source/hand review; no Lean, dynamics, certificate evaluator, training
or benchmark was run. Prior completed reviews retain their original scope.

## Corrections to the seven kinds

1. **Death chunk:** the formal conclusion is an even white time **t < K**,
   hence at most K-1, not merely t <= K. All-width-at-W assembly requires
   n <= floor(W/2) and EVERY chunk c < 2^(floor(W/2)-n), with the same W,K,n.
   `q01_of_chunks` concludes this for every start supported at depths <= W;
   the constrained lanes are its internal reduction. Coverage is part of the
   proof, not a statistical check. K97 gives upper96, not exact96 by itself.

2. **Death witness:** require support <= W, even d, black at every even time
   below d, and white at d to certify that start's first even death d.
   This yields a lower-bound witness for the uniform death bound. Calling it
   a **maximizer** additionally requires the matching upper certificate.
   The lower-bound theorem itself needs survival below d; its paired white
   endpoint is needed to label the witness's death as exactly d. `prun` is
   tied to the physical `zrow` by `run_toFun`; numeric labels alone are not
   certificates. The submitted d-exact module carries width52 exactness and
   width56/60 lower bounds; their upper certificates have separate provenance.

3. **Trap entry:** closure permits every unknown FAR-RIGHT bit, with the
   LEFT driver and ether phase fixed as in `trap_invariant`. It is not closure
   under every arbitrary left input. General parameters are j0,s,k,t1,
   with (j0+k) mod7=2, the prescribed boundary for all t>=t1, ether on1..k,
   and the phase-indexed wall state on k+1..k+13. In our families these are
   j0=s=3,k=6,t1=9 or5, so the wall occupies columns7..19.
   Entry proves the future ether trace and eventual periodicity, sufficient
   for the kit's non-finite-Psi/CQ01-instance route. **It does not by itself
   prove Psi R = etherLeft3.** Our full-row equality also uses the four/two
   early visible samples in `u_R31`/`u_R495`; locality transfers those along
   with entry. Keep the phase and transient, or prove the early samples.
   Prefix agreement1..28/1..24 then permits arbitrary tails. These families
   cover infinitely many right rows but one common Psi row.

4. **Padding needs at least two distinct contracts.** The fixed-tail
   `padding_strip` construction checks three zero-driven stabilizations,
   two-period reachability, return inclusion, and constant head at EVERY
   white phase (including the stabilized endpoint). `Forces` allows a
   constant white OR black head; vacuum exclusion is not that contract.
   Conversely `no_padding_of_forbidden_suffix` needs only the vacuum-free
   image `applyWord K suffix (fullSet K)`, followed by the analytic pulse
   argument; it does NOT require a stabilized closed set. For arbitrary
   preceding word v, retain BOTH bounds
   r >= 10(|v|+|suffix|)+11 and r >= K+9(|v|+|suffix|+1).
   Thus suffix011,K5 gives10|v|+41; suffix001001 or111001,K6 gives10|v|+71.
   The inventory's common +41 is not the latter two theorem statements.
   Keep the actual theorem's domain: leftmost-black/all-column wrappers
   versus single-seed center wrappers. The PaddedWords dispatch is a
   sufficient catalogue; its smallest named8/9 statements are seed-center
   results, not a blanket all-configuration theorem.

5. **Rank certificate:** rank is NONINCREASING, not strictly decreasing.
   Data also include position, counter period and output word per rank.
   `check` checks both unknown far bits and the counter/output conditions
   on equal-rank edges; `checkG` checks position < period. Nonempty word
   and positive strip width are explicit soundness premises. Eventually
   constant rank plus the counter gives masked periodicity, contradicted
   by masked Jen. Replacing this by strict descent loses the actual method.
   The certificate table primarily contains bitmask certificates; specific
   rank examples in this source are0^6 11 and0^9 101. A named verified word
   need not have used a rank certificate. Classify from its actual source.

6. **Signature separation:** fixed-pair universal separation is carried;
   it includes arbitrary right tails by the finite-cone bridge. Parameters
   d=a+m,e=b+m must satisfy0<=d,e<=2m, and complete block coverage needs
   256K >= 2^(m+1). `separationB` concludes some t<=m. **Attainment is a
   separate witness check**, equality before m and difference at m, not
   a consequence of disjoint signatures. The three submitted pairs carry
   both pieces. General EdgeObservable remains open.

7. **Channel weights:** closure and the displayed weight inequality alone
   omit root coverage, positive weights, weight-table coverage, a positive
   lower bound wmin and w(root)<=C*wmin. These appear in `Cert.Valid` and
   `bound_of`. The exact conclusion is one common finite language S with
   |S| D^n <= C R^n containing all n-bit visible prefixes of configurations
   satisfying Clock. For ratio/entropy wording require D>0; our constants
   have this. This is a language bound, not a probability or death bound.

## Consequence for an ML specification

Use a tagged family of theorem contracts, not one generic closed-set target.
Each proposed object should retain its source pin, data, physical domain,
quantifiers, phase/coordinate convention, all side-condition proofs, and the
precise conclusion. Return a proof/check receipt of THAT conclusion. Distinguish
an invalid candidate, a resource-capped check, no candidate found, and a proved
instance. None of the first three is a mathematical negative.

Useful labels are separate: eventual trap entry; full visible-trace equality;
CQ01 for one right row/prefix family; fixed-word exclusion; a uniform padding
family; single-start death; a width upper bound; exact width death. A learning
model should not turn one into another by sharing a binary success column.

The inventory's phrase that every kind is a finite closed set is too narrow:
a witness is a finite orbit, the forbidden suffix is a finite image exclusion,
and the rank proof combines a preorder with a counter. Similarly a universal
D bound need not logically take one prescribed closed-set form. That remains
a possible design direction, not a necessary theorem about all proofs.
GC1867's hand D(2)=6 already rules out D(W)<2W for EVERY W. A corrected eventual
or additive bound must be stated before becoming a proof-search objective.

**Unexpected adversarial check:** on the rank certificate's nonempty finite
phase/strip graph, fix far bit0. Every node has a successor, hence some cycle.
Strict decrease on EVERY edge would give rank(v)<rank(v) around that cycle.
Thus that proposed specification would exclude all actual certificates of
this total graph, not just make their search inefficient. Separately, all-zero
channel weights satisfy the bare weight inequalities vacuously; the actual
checker rejects them through positivity. These are elementary hand controls,
not new Rule30 results or executed tests.

Reasoned verdict: corrections required before executable schema acceptance;
the underlying reviewed theorems stand. Gut verdict: warm toward choosing and
composing correctly typed certificates, cold toward merging their meanings.
No new compute is accepted or requested. Actual dataset specification/results
remain a future input; no second receipt-only request is sent.

## Source coverage and provenance

Carrying source reread here: pinned cc1e0e0 ZeroBoundaryLanes definitions and
q01_of_checks/q01_of_chunks (SHA256 e34541fa34ee09d0f480db469384fcab9c05311e7f26bc135db02c5f692de7e3);
3eca23c0 StripCertificates introduction, Cert/check/checkG and complete rank
soundness chain (SHA256 9a359c0afc4151b62bcb7a05f240a56c37f3c93d3233bb1f0a0af4d54b72fb94);
WhitePadding pumping contract, ForbiddenSuffix and SuffixFamilies carrying
bodies, Ether trap_invariant; committed trap-families module in full
(b0113490...), d-exact support/survival/death interface, edge-sep block coverage
and separate attainment, channel-14 Valid/bound/explicit closure/weight premises.
Large literal payloads were not reevaluated or claimed individually read.

Completed coverage reused: GC1710 lane soundness; GC1707/1709 channel modules;
GC1793/1795 edge source/outputs; GC1836/1841/1842/1847 family source/outputs;
GC1853/1857/1860-1862 backward/padding/suffix sources; GC1867 D/counting review.
The seven kinds are not a complete inventory of the kit: backward-vacuum/tube
certificates already reviewed in GC1853 are another useful distinct contract.
No new external verification tag or independent kernel replay is asserted.
