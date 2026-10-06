# Mahler itinerary coupling and alphabet scope

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT50. Mahler itinerary
coupling and alphabet scope"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Mahler's 3/2 problem needs two conditions at once, and its known cellular-automaton form works differently from Rule 30.

**What it says.** Mahler asked whether some number, multiplied by 3/2 again and again, always has a fractional part
below a half. GPT showed this needs both an integer step pattern and a fractional-part condition. For example, two
odd steps in a row are forbidden, and a repeating pattern can satisfy the fractional part while matching no whole
number. The known cellular automaton for the problem is not of Rule 30's "left-invertible" kind.

**Why it matters.** It sets out honestly what transfers from the record's methods to Mahler's problem, and warns
where it does not.

**An everyday picture.** A lock with two dials: getting one right is not enough.

## The formal statement and proof

**Where:** RULE30-GPT.md G50; proof copied verbatim. **Status:** second-read by Local, 2026-10-06 (note below G51); corrected MA controls pass, initial phase-order failure retained in G50 outcome. Established decoupling specialized; no novelty or Z-number nonexistence claim.

### G50 theorem and proof: Mahler needs both itineraries, and a different alphabet

Write xi*(3/2)^j=n_j+u_j, with integer n_j>=0 and0<=u_j<1/2 at every j. If b_j=n_j modulo2, direct separation of integer and fractional parts gives

    n_(j+1)=(3*n_j+b_j)/2=ceil(3*n_j/2),
    u_(j+1)=(3*u_j-b_j)/2.

For even n_j, the half-interval condition forces u_j<1/3; for odd n_j it forces u_j>=1/3, wrapping the fractional part once. Iterating the second recurrence backwards and using the bounded tail yields

    u_j=sum_(k>=0) b_(j+k)*2^k/3^(k+1).

Conversely, start from a nonnegative integer n_0 and its ceil-map parity itinerary. Define u_j by this convergent series. If every u_j<1/2, the series gives3*u_j= b_j+2*u_(j+1). Combining this with the integer recurrence shows n_j+u_j=xi*(3/2)^j, xi=n_0+u_0. Provided xi>0, this is a Z-number. Thus the fractional-tail restriction and ordinary-integer itinerary realization are both required. No lower coefficient-deficit ceiling arises, since the integer coefficient is(3/2)^t at every prefix. This is the established decoupling mechanism, specialized here; no novelty claim.

Two consecutive ones are forbidden: their contribution to u_j is at least1/3+2/9=5/9>1/2. This finite forbidden word does not establish emptiness. Unexpected scope control: the purely periodic formal word(100)^infinity has tail values9/19,4/19,6/19, all below1/2, and satisfies the fractional recurrence exactly. It nevertheless cannot be the itinerary of any nonnegative integer start. A period100 has the integer branch map n -> (27*n+9)/8. After k periods integrality implies

    19*n_0+9 = 0 modulo8^k.

Indeed8^k*n_(3k)=27^k*n_0+9*(27^k-8^k)/19, and27 is invertible modulo8^k. Divisibility for every k forces19*n_0+9=0, impossible for a nonnegative integer. The compatible 2-adic value-9/19 is not an ordinary integer start. Formal fractional admissibility alone is therefore insufficient, even when every tail obeys the strict half-interval bound.

For the actual base-six CA, Kari–Kopra define g(x,y)=3*(x modulo2)+floor(y/2) and f(x,y,z)=g(g(x,y),g(y,z)). Fix y,z and vary x in{0,...,5}. The output depends only on x modulo2, so this six-letter local rule is not left-permutive in the usual full-alphabet sense. Both parity choices give distinct outputs: the inner value changes by3, its parity flips, and the outer value changes by3. There are exactly two outputs, not six. Membership in a broader expansive class must not be substituted for the binary left-invertibility used in our wall proofs. Canonical base-six expansions encode the strict fractional half-interval by a first fractional digit in{0,1,2}; the selected real configurations also require an eventually-zero integer-side tail. Arbitrary bi-infinite traces discard that realization requirement.
