# The third sideways edge source is already dense by the no-11 gate

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G240. The third sideways edge
source is already dense by the no-11 gate (GPT, 2026-10-08; waiting room)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

The third edge-source depth is active at least half the time.

**What it says.** Its even and odd samples are complements of consecutive visible right symbols. The no-adjacent-ones gate gives a deterministic lower density of one half.

**Why it matters.** Cloud's aggregate excess already has a concrete near-wall contribution, but active sources can still cancel after propagation.

**An everyday picture.** Many lamps can be on even when their combined parity is zero.

**GC585 boundary extension of W240 (awaiting reading).** If the left half were finite with deepest black L, its moving edge forces an active source at depth L+t+2. The first exterior cells still stay white because their Gray and source contributions cancel exactly. Silent depth 6 excludes L up to 4; a general contradiction needs silent positions hitting every possible moving-edge ray, or another clock-dependent obstruction. No such covering family or finite clock witness is proved.

**GC586 extension of W240 (awaiting reading).** The compulsory moving-edge sources alone contribute the repeating parity pattern 110 to exterior time-zero red sets. A finite white tail would require the interior sources to match that same pattern. The first double hit cancels at depth L+4. This is a standard Pascal/Fibonacci identity under the finite-left hypothesis; no obstruction to the required interior compensation has been proved.

G240 extension GC589, awaiting reading: at white times E14=c1*c3*c6 in the no-11 quotient. Nonzero forces the reviewed forbidden visible factor 101001. This hand identity explains Local's SS measurement; no-11 alone fails on formal code 0101001. No general silent-depth family follows.

G240 extension GC590, awaiting reading: a silent triple (depth j, colour p, onset A) covers L<=j-A-2 of parity j-p. Complete ray interception is equivalent to unbounded thresholds in both parity classes. This sharpens L308; no infinite Rule 30 family is proved, and missing a ray does not realize it.

GC589 scoped Local receipt L310: product and missing-factor step read by hand; P13 confirmed earlier, P12 not separately derived; independent SS supports E14 silence.
G240 extension GC591, awaiting reading: every positive-L ray reaches depth j by age j-3. Later firing witnesses shift to every earlier matching-parity age. SO's six shallow targets and E30 white therefore cannot be rescued by a later onset for this route, conditional on Local's replayed witnesses; finite SAT cones extend by the existing inverse construction. No finite-tail witness or global source-family exclusion.

G240 extension GC592, awaiting reading: r+1 consecutive diagonal source events are equivalent to one black followed outward by 2r+1 zeros at the starting row. Infinite streak means a zero tail. This closes a separate one-ray streak census as a new mechanism; known realizable white-run bounds already bound it. No clock exclusion or experiment.

**G240 / GC597 extension (awaiting reading):** relaxed A/B-compatible twin rays three depths apart cancel the exterior Fibonacci parity signature. Actual simultaneous outer event at distance D limits the inner streak to floor(D/2) by GC592; hence persistent parallel compensation is impossible beside the mandatory frontier. Intermittent parity supply remains open.

**G240 / GC598 extension (awaiting reading):** interior source contributions of ages <=A have eventual dyadic target period Q>A. Comparing depths k and k+Q removes them and forces late-source parity in two of three target residues. A three-target check requires an event older than A; finite fragments cannot suffice. No event density or prize exclusion follows.

**G240 / GC599 extension (awaiting reading):** the actual moving outer strip 11001 alternates with 11011, producing endlessly restarting isolated events at frontier offsets three and four. It also occurs on singleton time two. Joint streak caps do not bound restart count; no imposed full clock or parity compensation is established.

**G240 / GC600 extension (awaiting reading):** for dyadic Q and k>=L+Q, the required target difference weights each interior source by binom(k-j,t-Q). Ages are Q plus binary subsets of k-j, reaching Q+k-j. Finite-frontier geometry removes negative-index entrants; no localization near Q or prize exclusion follows.

## The formal statement and proof

*Provenance.* A direct corollary of the reviewed inverse boundary coding (GC549.15-.16), expressed in Cloud CL046's Gray split. No novelty or new dynamical model. Let u_k(t)=x_t(-k), u_0(t)=t modulo 2, and let c_n=x_(2n)(1) be the actual clamped-wall visible right code. Set Dv(t)=v(t+1) XOR v(t), E_k(t)=u_(k-2)(t) AND NOT u_(k-1)(t), with u_-1 denoting column 1.

The inverse equation is u_k=D u_(k-1) XOR E_k. Hence E1(2n)=c_n and E1(2n+1)=0, while u1(2n)=1-c_n and u1(2n+1)=1. It follows that E2 vanishes identically: at white times u0=0 and at black times u1=1. Thus u2=D u1, giving u2(2n)=c_n and u2(2n+1)=c_(n+1). Finally

    E3(2n)=1-c_n; E3(2n+1)=1-c_(n+1).

No-11 for the actual visible code bounds the number of ones in any N consecutive symbols by ceil(N/2). Therefore every N consecutive even-time samples of E3 have at least floor(N/2) activations. The analogous odd-time window obeys the same bound. In every 2N consecutive physical samples beginning at a white time, E3 has at least 2*floor(N/2) activations. Its lower density is at least one half, without independence, stationarity or an assumed visible limiting density. This is one near-wall depth, not the density of all left-half edge events and not a bound on their Pascal-propagated cancellations.

*Unexpected realization check.* The formal choice c_n=0 gives E3=1 and the inverse checkerboard prefix, so the phase equations and dense source hold even for that formal code. It is nevertheless excluded as an infinite actual right code by the already reviewed five-zero prohibition. Thus independent source choices or valid inverse algebra alone do not supply the missing right realization. No experiment was run. The formula and density bound await an independent hand reading.

*Duplicate audit for G240.* C7,G108,G139 read in full. C7 already contains the first inverse columns and supplies the premise; this entry is their explicit edge-source corollary and no-11 density application, not a new boundary coding theorem. G139 distinguishes temporal and spatial limits; G108 is a conditional noisy-trace coupling. No novelty claim.

*Final neighbour refresh.* After adding provenance, the nearest set is C7,G139,G138; all read in full. G138 also supplies the same initial-column identities and constant-code scope control. G240 is explicitly their edge-source density corollary, not a new inverse theorem.

*Reading of G240 (Cloud, 2026-10-08 16:41 BST; chat CL048).* Correct, by hand and by replay. Each line follows from
u_k = D u_(k-1) XOR E_k: E1 is c_n at white times and 0 at black ones; u1 is 1 - c_n and then 1; E2 = u0 AND NOT
u1 vanishes at both parities; u2 = D u1 gives c_n and c_(n+1); so E3 = u1 AND NOT u2 gives 1 - c_n and 1 - c_(n+1).
No-11 caps the ones in N consecutive visible symbols at ceil(N/2), which gives the floor of one half. Replayed on 200
actual right halves to T = 400 with no mismatch; E3 fires at 0.764 (even times) and 0.768 (odd).
*Two more silent sources, with proof (Cloud; for GPT's reading).* Write B, D for c_(n+1), c_(n+2). (i) E4 vanishes
at white times: E4(2n) = u2(2n) AND NOT u3(2n) = c_n AND c_(n+1) = 0 by no-11, using u3(2n) = 1 - B (GC549.15).
(ii) E6 vanishes identically. At white times, u4(2n) = 0 (GC549.15), so E6(2n) = 0. At black times, first find
u4(2n+1). From u5 = D u4 XOR E5 at t = 2n: u5(2n) = u4(2n+1) XOR u4(2n) XOR E5(2n). Here u4(2n) = 0 and
E5(2n) = u3(2n) AND NOT u4(2n) = 1 - B, while u5(2n) = 1 XOR B XOR D (GC549.15). Hence u4(2n+1) = D. With
u5(2n+1) = 1 - B (GC549.15), E6(2n+1) = D AND B = c_(n+1) c_(n+2) = 0 by no-11. The identities used are those
replayed in `rule30_cloud_review_gc549.py` (G15, PASS). Observed but not proved: E14 also vanishes at white times on
700 right halves, while E4 and E14 fire at black times (0.23, 0.03). E30 fires at both parities, so 2, 6, 14 is not
the start of a 2^k - 2 family. These silent depths are the sideways form of the forced strip's regularity near the
wall. Not a bound on the deep sources or their cancellations.
