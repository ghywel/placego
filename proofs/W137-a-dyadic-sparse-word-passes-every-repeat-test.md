# A dyadic sparse word passes every repeat test; faster powers fail

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G137. A dyadic sparse word
passes every repeat test; faster powers fail (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Sparse powers of two pass the entire repetition test, while faster integer powers fail it.

**What it says.** The word with ones exactly at powers of two satisfies every necessary repetition inequality and has only linearly many different words of each length. Replacing two by any integer at least three creates zero runs that violate the inequality.

**Why it matters.** The repetition condition excludes some geometric defect schedules, but cannot by itself prove positive entropy or exclude every sparse one. Passing the condition is not a Rule 30 realization.

**An everyday picture.** A useful filter can reject some candidates while admitting a sparse one that still needs every other physical constraint checked.

## The formal statement and proof

**Status and target.** Symbolic obstruction audit, independent review pending; no experiment. G134/G135 are verified by Local L088 and G136 awaits review. Counterfactual: using every period and every starting position in Theorem E Step 0, rather than only the derived kick recursion, might rule out all geometrically sparse corrections or force positive word-count entropy. The explicit dyadic word refutes that inference. This strengthens the scope guard rather than claiming a Rule 30 realization. The existing Thue-Morse guard in section 8.57 already shows that the repeat inequality alone is not an entropy theorem; the new point is its exact compatibility with sparse geometric defects. G26/G64 concern a different Rule210 dyadic-run construction and do not supply a Rule30 realization here.

Let d_s=1 precisely when s=2^j for some integer j>=0, and d_s=0 otherwise, including d_0=0.

**Every repetition obeys the strongest nonnegative-margin test.** If d_s=d_(s+q) for every a<=s<=b, where a>=0 and q>=1, then

    b <= 2a+q-1.

For a>=1, choose the smallest power of two p>=a, so p<=2a. If p+q is not a power of two, there is a mismatch at s=p. If p+q=P is a power of two, then P>=2p and p+2q=2P-p lies strictly between P and 2P. Thus there is a mismatch at s=P=p+q. In both cases a mismatch lies in [a,2a+q], proving the bound.

For a=0, if q is a power of two, s=0 is already a mismatch. Otherwise q>=3. If q+1 is not a power of two, s=1 is a mismatch; if q+1 is a power of two, s=2 is a mismatch since q+2 lies strictly between q+1 and its double. In either case the first mismatch is at most q, giving b<=q-1 as required. The reasoning covers every q, not only a selected sequence of convergent periods.

Consequently d satisfies the necessary finite-left repeat bound b<=2a+q+C for every C>=0, all periods and all starting positions. Passing this necessary condition does not establish a compatible forced left row, a full right evolution or a finite global seed.

**Sparse, aperiodic and zero word-count entropy.** The ones have zero density because their count up to N is at most 1+floor(log_2 N). They are infinite but have unbounded gaps, so d is not eventually periodic. For a factor length m>=1, starts a<m contribute at most m different words. For a>=m, two powers of two cannot both lie in [a,a+m-1]: their separation is at least a>=m. Such factors have at most one one, giving at most m+1 possibilities. Therefore the number P(m) of distinct length-m factors obeys

    P(m) <= 2m+1,
    limsup log_2(P(m))/m = 0.

This is word-count entropy of this one word, not the dynamical entropy of Rule 30. Complementing d preserves all repetition tests and its factor complexity.

**Unexpected rate control.** For an integer B>=3 let d^(B) have ones at B^j and zero elsewhere. For sufficiently large p=B^j, between p and Bp the period-one equality stretch has a=p+1 and b=Bp-2. The repeat bound would require

    (B-2)*p <= C+5.

It fails for arbitrarily large p, for every fixed C. Thus these faster geometric isolated-one schedules are excluded for a finite-left alternating-wall companion by Theorem E Step 0 alone. Powers of two are the exact surviving integer-base case for this necessary test. This is the identified independent check: geometric spacing is not a single undifferentiated regime. No experiment or claim about irrational-base flips is used in this control.

**Closed bridge and next obligation.** Do not try to deduce positive entropy, positive defect density or exclusion of every geometric schedule solely from the repeat inequality, even when all q and a are imposed. The explicit sparse word passes the full family. Adding it to a Sturmian base need not preserve that property, so this does not prove that a dyadically flipped Sturmian word passes the tests or is realizable. A useful next proof must use a further Rule30 wall constraint, a relation across the corrections, or the coupled-tail condition of G130. The finite-left sufficiency question for d itself is not answered here.
