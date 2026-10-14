# Mahler's 3/2 problem

*Room opened 2026-10-14 by the owner ("Switch to Mahler, full steam ahead. The fact it carries no prize at all means it
is the least interesting to anybody and it is less likely anybody has been mining it."). Claude (Local) leads the
mathematics and GPT reviews (AGENTS.md items 17 and 19). The earlier Mahler work, done as the third corner of the
Rule 30 / Collatz / Mahler triangle, is in RULE30-PRIZE.md 8.45, COLLATZ-PRIZE.md 9 and GPT's G49 .. G51 and
GC928 .. GC936. Their scopes in the Mahler setting were audited by GPT in GC1220. The literature survey is in
PRIOR-ART.md ("Mahler's 3/2 problem: survey at the room switch").*

## The honest summary

**No proof, nothing claimed.**

**The problem (Mahler 1968).** Is there a real xi > 0 with every fractional part {xi (3/2)^n} in [0, 1/2), a
*Z-number*? Mahler conjectured there is none. It carries no cash prize.

**The exact form used here** (GPT's G50, PROVED with Local's read L022, and G51's finite windows, a reviewed tool; both
listed in GC1220). Write
xi (3/2)^j = n_j + u_j, with n_j a nonnegative integer and u_j in [0, 1/2), and b_j = n_j mod 2. Then:
- n_(j+1) = ceil(3 n_j / 2) = (3 n_j + b_j) / 2. The integer parts follow the map T(x) = ceil(3x/2) from n_0.
- u_j = sum_(k >= 0) b_(j+k) 2^k / 3^(k+1). The fractional part is fixed by the future parity itinerary.

So a Z-number is exactly a positive integer n_0 whose T-orbit parity itinerary b satisfies u_j < 1/2 for every j. Then
xi = n_0 + u_0. (The first wording also allowed n_0 = 0 with u_0 > 0. That case is empty: n_0 = 0 gives b = 0 and so
u_0 = 0, xi = 0. Local, L710.)

**What this record adds at the room switch** (Local; read by GPT in GC1221 and GC1222, corrected in L710).
- *The fractional side is completely free.* For u in [0, 1/2), b = 0 if u < 1/3 and b = 1 otherwise keeps
  u' = (3u - b)/2 in [0, 1/2). So every point of Mahler's window has an infinite admissible orbit; in Stephan's terms
  the window's hold set is the whole window.
  - The admissible itineraries are exactly the greedy digit sequences of this map. Up to scaling they are greedy
    expansions in base 3/2, a beta-shift of entropy log2(3/2) per digit. This is the content of Flatto's 1992
    "Z-numbers and beta-transformations"; his O(x^0.585) count has this exponent.
  - It is not sofic, since 3/2 is not an algebraic integer.
- *The integer side is the whole problem.* The same series S(b) = sum b_k (2/3)^k / 3 converges both in R (giving u_0)
  and in the 2-adic integers, where it gives -n_0. That is G51's nested residues r_T = -C_T 3^(-T) mod 2^T.
- *The question restated* (corrected per GC1221).
  - Let S_strict be the 2-adic integers whose T-itinerary keeps every tail u_j strictly below 1/2. Let K be those whose
    every finite G51 window is nonempty.
  - K is closed and is the closure of S_strict, but the two differ. The critical code d(1) (u_0 = 1/2) and the code
    0 d(1) (u_1 = 1/2) lie in K and not in S_strict.
  - The first wording called S closed. That was wrong: the strict inequality is not a closed condition.
  - Both sets are uncountable, of Hausdorff dimension log2(3/2). This is GC1221's argument: prefix covers give the upper
    bound, and Lebesgue measure pushed through the code map gives the lower one. PROVED, with Local's read in L710.
  - They have the same finite-prefix language (GC1222). Every valid prefix's window is a nonempty half-open interval,
    whose points have strict codes, so the census counts cannot tell them apart.
  - S_strict contains 2-adic non-integers, such as -9/19 with itinerary (100)^infinity (G50).
  - **Mahler's conjecture says S_strict contains no positive ordinary integer.** A nonnegative ordinary integer is a
    2-adic integer whose binary expansion ends in zeros; a negative one's ends in ones (GC1224). Using K instead needs GC664's half-boundary repair, a forward shift that can
    raise the integer part.
- *Consequence for one certificate format* (narrowed per GC1221; the first wording said "fractional-side methods cannot
  settle it", which is too broad). Stephan's block certificates are complete on the
  finite-hold-set class and obstructed on infinite ones (2026, paper 2, Theorem D). His record window,
  Z_{3/2}(2/7, 5/7) empty with length 3/7, is the method's exact ceiling.
- *The parallel with Rule 30.* Every argument must use the finite binary expansion of n_0. This is the Mahler twin of
  Rule 30's "finite support" (the forced left half eventually white), and the record already met it there.

**Sufficient conditions in print.**
- *Andrieu, Eliahou and Vivion (2025, Conjecture 1.6):* every T-orbit is equidistributed modulo 2^k.
- *Weaker:* every T-orbit visits 3 mod 4. Two consecutive odd n_j give u_j >= 5/9, so a Z-number's orbit never visits
  3 mod 4. The implication runs one way. The formal code (1010)^infinity avoids 11, yet its fractional part is 3/5, so
  avoiding 11 is not sufficient for an arbitrary code. That code has no positive integer realization, so it does not
  decide an iff restricted to actual positive integer orbits (GC1221).

**The counting form** (CL092, MEASURED). The number of starts g < 2^w whose admissible window survives T steps falls
by a factor of about 3/4 a step once the free bits are spent. The record horizon below 2^20 is 47, against a coin
prediction of about 2.41 w. GC664 (PROVED): no positive Z-number is equivalent to every bounded positive integer range
dying out at some finite horizon. GC663's (3/4)^T density does not prove that.

## Sections

1. **The record census** (2026-10-14; `tests/probes/mahler/mahler_census.{c,py}`, predictions committed first; GPT
   reviewing). The walk is exact: G51's windows as 128-bit dyadic numerators, and any start alive past step 124 replayed
   with exact fractions. Its controls equal CL092's exact-fraction histogram at 2^12 and 2^20; a first-run chunk
   overcount was caught by that control and is retained.
   - **No Z-number lies below 2^63 = 9.22e18** (COMPUTED; GPT adopted the receipt at the scope of a source audit plus
     fixed controls, not an independent full replay, GC1221.1). Every start in [1, 2^63) has a finite horizon. A
     Z-number in [n, n + 1) would make H(n) infinite, so this excludes Z-numbers below 2^63. The converse, from an
     infinite horizon to a Z-number in the same range, can need GC664's forward shift (GC1221). The survey found no
     published large-scale check.
   - *Records.* H*(w) runs from 59 at w = 24 to 157 at w = 63 (n = 1541211973603965806), with H*/w in 2.18 .. 2.58,
     the coin law of about 2.4 w. No anomalous survivor appeared.
   - *The free bits pay exactly.* #{1 <= n < 2^w : H(n) > T} + 1 = 2^(w - T) A(T), with A(T) = 2, 3, 5, 8, 12, 18, 27, 40,
     60, 90, ... the same at every w, tending to a ratio of 3/2. A(T) is exactly the Renyi-Parry word count of the
     (3/2)-beta-shift (c_n = 1 + sum d_i c_(n-i), d = the greedy digits of 1 in base 3/2), for every T < 63. That is a
     computational confirmation, from a program that never used it, of the beta-shift identification in the summary
     (post hoc check).
   - *The tail.* Past the free bits, consecutive death-bin ratios N(h+1)/N(h) average 0.744 .. 0.752 (CL092's 3/4).
     Survivor-count ratios were not computed separately (GC1221.1; the first wording said "survivors").
