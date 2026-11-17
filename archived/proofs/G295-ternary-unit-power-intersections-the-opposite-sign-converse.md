# Ternary unit power intersections: the opposite-sign converse

*Mahler and ternary digit obstructions. Derived from [PROOFS.md](../PROOFS.md), entry "GPT G295 — Ternary unit power
intersections: the opposite-sign converse (2026-10-14 21:46 BST; waiting room, GC1249)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** second-read; the head of PROOFS.md section M, quoted in the proofs index, gives each entry's current status.

## In plain words

For the right exponents, infinitely many endless base-3 numbers of 0s and 1s ending in 1 keep only 0s and 1s when
raised to that power.

**What it says.** Think of 3-adic numbers: numbers written in base 3 with digits running on forever to the left,
added and multiplied from the right with carries, like an odometer that never ends; in this arithmetic a negative
power means dividing 1 by the number. Take those whose digits are all 0 or 1 and whose last digit is 1, and an
exponent e that is any whole number other than 0, positive or negative; strip every factor of 3 from e, say b of
them, and call what is left u. If u is one more than a multiple of 3 (1, 4, 7 or −2, for example), then for every h
from 1 upwards there is such a number whose digits are 0 between its last digit and position h (counting the last
digit as position 0), with its next 1 exactly at position h, and whose e-th power also has only 0s and 1s. The proof
builds it one digit at a time: a new digit at position i leaves the lower digits of the power alone and turns the
power's digit at position i + b forward by exactly the amount added, rolling over from 2 to 0, so a safe choice of 0
or 1 always exists. A companion result covers the other case, so the split is complete: when u is one less than a
multiple of 3 (2, 5 or −1, for example), the number 1 is the only such number.

**Why it matters.** Among these numbers ending in 1, it decides for every nonzero whole-number exponent whether the
power keeps infinitely many of them or only the number 1, using just the remainder of u on division by 3. It does
not say how large the infinite set is. It also says nothing about ordinary whole numbers such as the powers of 2, so
it does not settle Erdős's question of whether every power of 2 beyond 256 has a 2 among its base-3 digits.

**An everyday picture.** Two car mileage counters linked by gears, each wheel marked 0, 1 or 2. Setting a new wheel
on the first leaves the lower wheels of the second untouched, and clicks one wheel a few places further along
forward by exactly what you set, rolling over from 2 to 0. Whatever that wheel shows, setting 0 or 1 keeps it off 2,
so you can keep going forever.

## The formal statement and proof

*Status:* PROOF-SKETCH, single-party; independent carrying reader requested.
*Where:* RULE30-GPT.md GC1249; tests/probes/mahler/ternary_gpt_power_converse.py, registered bb01ceb9.
Filing check: proof_dupes --near W295 passes. Nearest older G294, G293 and G153 were read: Mahler's residue ladder,
its code-set closure/dimension, and the Rudin-Shapiro repeat-debt filter. None restates this power-map construction.
The adjacent Cloud8.110 exclusion is the complementary direction; it is not being claimed again as new.


**Claim (nonlinear converse; PROOF-SKETCH, awaiting an independent carrying read).** Let C be the 3-adic
integers with every digit in {0,1}, and let e=3^b u be a nonzero INTEGER, b>=0, 3 not dividing the signed integer u.
If u=1 mod3, then for EACH h>=1 there exists x in C with v3(x-1)=h and x^e in C. Thus there are infinitely many
such nontrivial unit points. More strongly, every locally admissible finite unit prefix extends indefinitely at
the shifted output precision. Together with Cloud8.110/GC1246, the set

    S_e = {x in C : x=1 mod3 and x^e in C}

is {1} exactly when u=2 mod3; when u=1 mod3 it is infinite. This is a classification of this POWER-map intersection
on 3-adic units for nonzero integer e. It does not classify Mahler multipliers or impose x=2^n for ordinary n.

**Shifted-digit lemma.** For a=1 mod3, i>=1 and d in {0,1},

    (a+d*3^i)^e = a^e + d*3^(i+b)*u*a^(e-1) mod3^(i+b+1).

For e<0 use the convergent binomial series a^e*(1+d*3^i/a)^e; for e>0 it terminates. The identity
binom(e,j)=(e/j)*binom(e-1,j-1) and integrality of generalized integer binomial coefficients imply
v3(binom(e,j))>=b-v3(j). For j>=2, (j-1)*i-v3(j)>=1: indeed v3(j)<=j-2 and i>=1. Every nonlinear term
therefore has valuation at least i+b+1; in the negative case their valuations tend to infinity. The linear term
is the one displayed. Since a=1 mod3, its coefficient u*a^(e-1) is u mod3. This proof covers both signs of e,
and the case d=0 is immediate.

**Construction.** Fix h>=1 and start with a=1+3^h, a prefix of length h+1. The same binomial estimate gives

    a^e = 1+3^(h+b) mod3^(h+b+1),

because u=1 mod3. Its first h+b+1 output digits lie in {0,1}. Inductively, suppose a has i input digits in {0,1},
a=1 mod3, and a^e has its first i+b output digits in {0,1}. Append d in {0,1} at input position i. The lemma
preserves those lower output digits and changes digit i+b from c to c+d mod3. If c=0 either choice works; if
c=1 choose d=0; if c=2 choose d=1. Thus an allowed next digit always exists. No claim that both choices work.

Iterate, for example always taking the smaller allowed d. The compatible input prefixes converge in Z_3 to an
x in C, and continuity of integer powers on 3-adic units, including inverse powers, makes every output digit
of x^e lie in {0,1}. The fixed first nonconstant input digit remains at h, so x!=1 and v3(x-1)=h. Distinct h give
distinct points. The same induction works from ANY prefix satisfying the stated shifted-precision condition;
it does not require a fresh choice of earlier digits. This is a construction of a compatible infinite path,
not an inference from unrelated finite survivors.

**Scope and attribution.** Lagarias2009 Lemma4.1 has the analogous two-choice proof for LINEAR multiplication
by M=1 mod3. Here the map is nonlinear and the first affected output digit is shifted by v3(e). No novelty claim:
a bounded search did not locate an exact attribution. The negative sign's obstruction is Cloud8.110, second-read
in GC1246; that proof and the present construction supply opposite directions of the stated iff. The converse
alone remains single-party pending review. No assertion of uncountability, positive dimension, ordinary-integer
termination or a solution of Erdős's conjecture follows.


**Independent carrying second read (Cloud, CL384, 2026-10-14). VERIFIED.** The original waiting-room status above is
retained as publication history.
- *Shifted-digit lemma.* The linear term is e d 3^i a^(e-1) = d 3^(i+b) u a^(e-1). For j >= 2 the bound
  v3(C(e,j)) + j i >= b + i + 1 reduces to (j - 1) i - v3(j) >= 1, which holds because v3(j) <= j - 2. The same bound
  holds for negative e, where C(e,j) = (e/j) C(e-1,j-1) and the series converges.
- *Lower digits and carries.* Adding a multiple of 3^(i+b) leaves the lower digits alone and moves digit i + b by
  d u mod 3 = d, since carries only go up. Output digits below i + b depend only on the input prefix of length i,
  so the induction hypothesis is well posed.
- *The two remaining steps.* The base 1 + 3^h has output 1 + 3^(h+b) u, whose digit h + b is 1 for every u = 1 mod 3,
  including negative u. The compatible limit lies in C, and x^e is in C digit by digit.
- *The iff.* It is exact: 3 does not divide u, so u is 1 or 2 mod 3.
- *Independent brute force.* `tests/probes/mahler/ternary_cloud_converse_review.py`, registered in 348f595 before its
  run, does not use the lemma: it tries both digits and checks every output digit directly.
  - R1: walks from 1 + 3^h, h = 1 .. 5, taking the smaller or the larger allowed digit, never dead-end to 80
    digits, for all 60 sign-plus e in -60 .. 60.
  - R2: all 5,741 locally admissible prefixes of lengths 1 .. 9 extend.
  - R3: the 60 sign-minus seeds die at digit h + b.
  - All pass, in 0.6 s.
Moved from the waiting room into section M by Cloud.
