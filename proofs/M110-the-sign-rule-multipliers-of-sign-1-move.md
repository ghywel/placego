# The sign rule: multipliers of sign -1 move Mahler's and Erdős's sets off themselves

*Mahler and ternary digit obstructions. Derived from [PROOFS.md](../PROOFS.md), entry "Cloud 8.110 — The sign rule:
multipliers of sign -1 move Mahler's and Erdős's sets off themselves (Cloud, 2026-10-14; waiting room)"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** second-read; the head of PROOFS.md section M, quoted in the proofs index, gives each entry's current status.

## In plain words

In Mahler's and Erdős's problems, multiplying by (for Erdős, raising to the power of) the right kind of number
pushes points out of the set, all but one trivial point.

**What it says.** Mahler's set K holds the "2-adic" numbers (numbers written in binary with digits running on
forever to the left) whose odd-and-even pattern passes Mahler's test at every step. Write a nonzero whole-number
multiplier e, negative ones included, as a power of two, 2^a, times an odd number u; if 3^a times u leaves remainder
3 when divided by 4 (as for e = 2, 3, 7, 10, 11 or -1), then x and e times x can both be in K only when x = 0.
Erdős's set C holds the numbers written in base 3 with digits 0 and 1 only, again running on forever to the left. If
e is a power of three times a number u that leaves remainder 2 when divided by 3, and x ends in the digit 1, then x
and x raised to the power e can both be in C only when x = 1. So for whole numbers n ≥ 1 and e ≥ 2 of that kind (2,
5, 6, 8, 11, ...): if 2^n has no digit 2 in base 3, then 2^(en) has one.

**Why it matters.** It proves that any multiplier acting like a minus sign on the one digit that matters always
pushes these sets off themselves, which is the pattern a computer check of the multipliers from -15 to 40 found. It
does not say that the other multipliers keep a point: for Mahler's set, 13 pushes it off too. It also says nothing
about whether any single whole number belongs to the sets, and it solves no prize.

**An everyday picture.** A room where everyone must wear their watch on the left wrist: in a mirror, each of them
wears it on the right, so nobody in the room is also allowed in the mirror's room. Only someone with no watch at
all, the trivial point, can be in both.

## The formal statement and proof

*Status:* PROOF-SKETCH, single-party. A second reader is wanted. It is checked by computation for every multiplier
from -15 to 40, in both directions (Mahler at T = 16, Erdős at k = 12). The integer form is probably classical; the
literature was not checked.
*Where:* RULE30-PRIZE.md 8.110; `tests/probes/prizes/lifting_cloud_multipliers.py` (H1, and the `addendum` mode).

**Claim (Mahler).** For e = 2^a u with u odd and 3^a u = 3 mod 4, K ∩ eK = {0}. *Sketch:* the codes of x = 2^k m
and ex begin 0^k 1 c and 0^(k+a) 1 c'. Each needs its next parity to be 0, and the two conditions differ by the
factor 3^a u = -1 mod 4.

**Claim (Erdős).** Let C be the 3-adic integers with digits in {0, 1}. For e = 3^b u with u prime to 3 and
u = 2 mod 3, if x and x^e both lie in C and x = 1 mod 3, then x = 1. In particular, if n >= 1 and 2^n has no ternary
digit 2, then 2^(en) has one. *Sketch:* write x = 1 + 3^(m+1) w with w = 1 mod 3. Then
x^e = 1 + 3^(m+1+b) u w + O(3^(2m+2+b)), so digit m + 1 + b of x^e is u mod 3 = 2.

Not a prize claim. Both statements constrain pairs of points in the set, not a single integer.


**Independent carrying second read (GPT, GC1246, 2026-10-14). VERIFIED within the following explicit domain.**
The original waiting-room label is historical. Take e a NONZERO INTEGER; a=v2(e)>=0 and b=v3(e)>=0, with signed
integer units u. Both main sufficient exclusions hold, including negative e. The generalized-binomial remainder
bound holds for negative powers and converges on x=1 mod3. The ordinary positive-integer2^(en) corollary requires
e>=2 positive; negative powers use the 3-adic unit statement. The unit restriction is essential (3 and9 countercontrol).
The tested finite iff criteria are not an all-multiplier infinite-set converse. The two original False lines remain
failures, and the corrected valuation-shadow criterion is an honest post hoc repair, independently checked at the
registered finite bounds. See GC1246 and the independent probe; no full literature priority or prize claim.
