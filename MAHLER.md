# Mahler's 3/2 problem

*Room opened 2026-10-14 by the owner ("Switch to Mahler, full steam ahead. The fact it carries no prize at all means it
is the least interesting to anybody and it is less likely anybody has been mining it."). Claude (Local) leads the
mathematics and GPT reviews (AGENTS.md items 17 and 19). The earlier Mahler work, done as the third corner of the
Rule 30 / Collatz / Mahler triangle, is in RULE30-PRIZE.md 8.45, COLLATZ-PRIZE.md 9 and GPT's G49 .. G51 and
GC928 .. GC936. Their scopes in the Mahler setting were audited by GPT in GC1220. The literature survey is in
PRIOR-ART.md ("Mahler's 3/2 problem: survey at the room switch").*

## The honest summary

**No proof of Mahler's conjecture.**

**13 November 2026, GC2942. Fejer energy: a slope obstruction and an exact beta-transfer target.** [Proof block](reports/GPT-MAHLER-FEJER-ENERGY-20261113.md). PROVED two-party at its stated scopes since Local's [carrying read](reports/LOCAL-GC2940-GC2942-CARRY-20261114.md) (L1672, 14 November): ancestry suffix clusters rule out the energy bound uniformly over all odd multipliers above bandwidth exponent theta^2; the physical multiplier and intended shorter range remain open. Physical same-suffix pairs are controlled. Exact ternary transport, minimum-slack Gram weights and a phase conjugation reduce the remaining correlation to beta-transfer L2 norms at specific modular frequencies; finite-history weights and frequency-dependent constants must remain. Three bounded control stages pass; the “physical below random median” prediction was refuted (8/15). No power saving proved. Next: carry (C),(D),(T),(G'),(I), then bound (J)'s joint frequency/time boundary quantity; the endpoint identity requires no renewal approximation. Both schedules paused; no job running.

**13 November 2026, GC2940:** [GPT carries Local's corrected valid-start proof](reports/GPT-MAHLER-VALID-STARTS-REVIEW-20261113.md). Theorem V and V1–V3 are now PROVED hand/two-party. GPT's continuation, PROVED two-party since Local's [carrying read](reports/LOCAL-GC2940-GC2942-CARRY-20261114.md) (L1672): the exact affine phase survives any full prefix, giving a uniform (3/4)^j law for a growing logarithmic number of checks; a renewal sharpening improves the logarithmic exponent and constant, without changing the power of x. Exact controls pass, including a 257-letter history. The proposed pair test is corrected to Fejer energy; novelty remains uncleared pending Flatto's original paper.

**12 November 2026, L1670:** [the valid starts are equidistributed](reports/LOCAL-MAHLER-VALID-STARTS-20261112.md).
The integers below 2^w whose first w parities pass Mahler's test are equidistributed over intervals (Theorem V,
PROVED hand/two-party, Local and GPT GC2940: free bits, a renewal inequality, the run lemma and Erdős–Turán). Same
status: the first check on valid words tends to 1/2, which closes L1669's open limit; the share passing j more
checks tends to (3/4)^j; the number of Z-numbers below x is at most C x^θ/(log x)^c with c about 0.0007, against
Flatto's O(x^θ). The exponent is unchanged and the proved rate gives no usable number; measured, the discrepancy
is about 0.6/√A(w). Novelty not cleared.

**12 November 2026, L1669:** [the unconditional first check tends to 1/2](reports/LOCAL-MAHLER-FIRST-CHECK-LIMIT-20261112.md).
Among all n < 2^w the share with T^w(n) odd tends to 1/2 (PROOF-SKETCH, Local: a Riesz product and a run
lemma, each step checked numerically), and is within 0.0054 of it for every w >= 80 (COMPUTED search on that
sketch). For the valid words the limit was left open, reduced to one lemma about sums over the 3/2-shift;
L1670 proves that lemma (carried by GPT GC2940).

**12 November 2026, L1667–L1668:** [the first check is balanced on both sides](reports/LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md).
For every m ≥ 3 the valid words of length m that cannot take a 1 have forced parity 1 in a share between
1/27 and 26/27, and eventually between 0.2228 and 0.7772; GC2936's pairing lemma holds with |R_m| ≥ F(m − 6);
the unconditional check lies between 0.415 and 0.585 from w = 15. Hand steps are PROOF-SKETCH (Local) awaiting
a carrying read; the finite certificates are COMPUTED. This bounds a fixed number of checks. It is not a
route to extinction, and the report says why.

**11 November 2026, CL782 / GC2936:** [Kit-to-Mahler review](reports/GPT-MAHLER-TRANSFER-REVIEW-20261111.md).
Cloud's first-check identities, recognizable-ranking barrier and planted-survivor construction are
PROVED two-party at the corrected scopes. GPT's new unconditional 1/4–3/4 check bound, conditional
boundary pairing, odd-weight compactness formulation and explicit stripe recharge families are
PROOF-SKETCH pending Cloud; exact small controls pass. A fixed stripe ray can have unbounded extra
lifetime, so retain its returned odd state. The full survival-count formulation remains viable.
Cloud retains the three continuations; exact next: carry the new steps, then the joint real-slack
and modulo-three pairing lemma. Local owns Wolfram; both schedules remain paused.

**1 November 2026, GC2342:** the owner reopened cross-problem transfer from Rule30.
[The episode/recharge investigation below](#rule30-to-mahler-episodes-and-recharge-gc2342)
gives an explicit obstruction to a local countdown argument, using known coupling tools.
It is a solo PROOF-SKETCH application, not a new conjecture solution or novelty claim.

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
- *The parallel with Rule 30.* Every argument must use that n_0 is a positive ordinary integer, whose binary expansion
  ends in zeros, since S_strict also holds 2-adic non-integers such as -9/19; that every proof must use binary
  finiteness as its mechanism is not established (GC1233.1). This is the Mahler twin of Rule 30's "finite support"
  (the forced left half eventually white), and the record already met it there. (comb note, 2026-10-14, Local, SW-01:
  narrowed per GC1233.1, which the probe docstring already carried; the first wording said every argument must use
  the finite binary expansion of n_0.)

**Sufficient conditions in print.**
- *Andrieu, Eliahou and Vivion (2025, Conjecture 1.6):* every T-orbit is equidistributed modulo 2^k.
- *Weaker:* every T-orbit visits 3 mod 4. Two consecutive odd n_j give u_j >= 5/9, so a Z-number's orbit never visits
  3 mod 4. The implication runs one way. The formal code (1010)^infinity avoids 11, yet its fractional part is 3/5, so
  avoiding 11 is not sufficient for an arbitrary code. That code has no positive integer realization, so it does not
  decide an iff restricted to actual positive integer orbits (GC1221).

**The counting form** (CL092, MEASURED). The number of starts g < 2^w whose admissible window survives T steps falls
by a factor of about 3/4 a step once the free bits are spent. The record horizon below 2^20 is 47, against a coin
prediction of about 2.41 w. GC664 (PROVED, with Local's read L363): no positive Z-number is equivalent to every
bounded positive integer range dying out at some finite horizon. GC663's (3/4)^T density does not prove that.
(comb note, 2026-10-14, Local, SW-01: read pointer added; second read L363, CHAT-LEDGER.7.md, acknowledged at
RULE30-GPT.md's L363 checkpoint.)

*Note (Cloud, 2026-10-22, spring clean): NOW.md's joint halt of 14 October 13:45 BST put this room on a firm hold, not
abandoned, and the second halt of 15 October kept it there (both states are now in archive/NOW-HISTORY.md); nothing
below is changed. The proofs this room cites have pages in plain words:
[G50](proofs/G50-mahler-itinerary-coupling-and-alphabet-scope.md) and [G51](proofs/G51-exact-finite-mahler-coupling-window.md) (the coupling window), [G266](proofs/G266-mahler-s-map-with-one-place-carries-the.md) (one-place carries), [G293](proofs/G293-strict-mahler-codes-and-their-closed-2-adic.md)
(the strict codes' dimension), [G294](proofs/G294-the-mahler-window-ladder-is-equivalent-to-odd.md) (the window ladder); section M's [8.109](proofs/M109-mahler-s-admissible-set-meets-its-doubles-and.md), [8.110](proofs/M110-the-sign-rule-multipliers-of-sign-1-move.md),
[8.112](proofs/M112-odd-point-reduction-and-finite-certificates-k-13k.md) and [G295](proofs/G295-ternary-unit-power-intersections-the-opposite-sign-converse.md); and, still in the waiting room, [G296](proofs/W296-one-finite-mahler-joint-plateau-forces-zero-multiplier13.md).*

## Sections

1. **The record census** (2026-10-14; `tests/probes/mahler/mahler_census.{c,py}`, predictions committed first; GPT
   reviewing). The walk is exact: G51's windows as 128-bit dyadic numerators, and any start alive past step 124 replayed
   with exact fractions. Its controls equal CL092's exact-fraction histogram at 2^12 and 2^20; a first-run chunk
   overcount was caught by that control and is retained.
   - **No Z-number lies below 2^63 = 9.22e18** (COMPUTED; GPT adopted the receipt at the scope of a source audit plus
     fixed controls, not an independent full replay, GC1221.1). Every start in [1, 2^63) has a finite horizon. A
     Z-number in [n, n + 1) would make H(n) infinite, so this excludes Z-numbers below 2^63. The converse, from an
     infinite horizon to a Z-number in the same range, can need GC664's forward shift (GC1221).
     - *It extends a published bound* (corrected 2026-10-14). Dubickas and Mossinghoff, "Lower bounds for Z-numbers",
       Math. Comp. 78 (2009) 1837-1851, show by computation that any Z_{3/2}-number exceeds 2^57. My room-switch survey
       missed this and said no published large-scale check existed. The swarm's adelic lane found it, and Local
       confirmed the abstract. The census raises that 2009 bound by a factor of 64; later literature was not checked,
       so no current-record claim follows (GC1225; PRIOR-ART.md). (comb note, 2026-10-14, Local, SW-01: GC1225's
       qualifier restored; the first wording ended "The census raises the bound by a factor of 64.")
   - *Records.* H*(w) runs from 59 at w = 24 to 157 at w = 63 (n = 1541211973603965806), with H*/w in 2.18 .. 2.58,
     the coin law of about 2.4 w. No anomalous survivor appeared.
   - *The free bits pay exactly.* #{1 <= n < 2^w : H(n) > T} + 1 = 2^(w - T) A(T), with A(T) = 2, 3, 5, 8, 12, 18, 27, 40,
     60, 90, ... the same at every w, tending to a ratio of 3/2. A(T) is exactly the Renyi-Parry word count of the
     (3/2)-beta-shift (c_n = 1 + sum d_i c_(n-i), d = the greedy digits of 1 in base 3/2), for every T < 63. That is a
     computational confirmation, from a program that never used it, of the beta-shift identification in the summary
     (post hoc check).
   - *The tail.* Past the free bits, consecutive death-bin ratios N(h+1)/N(h) average 0.744 .. 0.752 (CL092's 3/4).
     Survivor-count ratios were not computed separately (GC1221.1; the first wording said "survivors").

2. **The swarm** (2026-10-14; the owner asked for one to "dig into these muddy clear waters and pull out some
   unexpected consequences"). Nine agents: four lanes of solver plus blind skeptic (two boundaries, adelic duality,
   computability, physics to mathematics), then a judge ranking by relevance to integer compatibility. GPT's lane
   changes (GC1222) were built in. Every item below is a single-party self-check under AGENTS item 16 until GPT's read.
   - **Verdict: nothing moves the critical path.** No candidate excludes a positive integer, and none uses eventually
     zero binary digits as a mechanism. The judge's words: "an honest null on the main question".
   - *The window ladder* (PROVED for positive ordinary integer codes: found independently by two lanes, re-derived by
     both skeptics, Local's carrying proof below, GPT's independent argument GC1228 = PROOFS.md G.GPT294; the
     emptiness R_g stays open). For g >= 3
     put alpha_g = 3^(g-1)/(3^g - 2^g), the value of the code (1 0^(g-1))^infinity, and
     beta_g = (1 + (2/3)^(g-1))/3. For every a in [alpha_g, beta_g], a real xi > 0 has every {xi (3/2)^j} in [0, a)
     iff xi = n + u_0(n), with n >= 1 whose T-code has every two 1s at distance >= g. Equivalently, every odd
     T-iterate of n is -1/3 mod 2^g, since the gap after an odd n_j is v_2((3 n_j + 1)/2) + 1.
     - g = 3: the windows [9/19, 13/27] and odd iterates 5 mod 8. g = 4: [27/65, 35/81] and 5 mod 16. g = 5:
       [81/211, 97/243] and 21 mod 32.
     - For these windows the fractional side is a shift of finite type, so the real number drops out. What is left
       is residue avoidance by positive integer orbits alone. (At a = alpha_g the strict fractional set omits the
       critical periodic tail, so "shift of finite type" holds there only for actual integer orbits, which never
       realize that tail: GC1227.1.)
     - The windows lie just above Flatto-Lagarias-Pollington's 1/3, and each has an uncountable hold set, so
       Stephan's certificate format cannot reach them. Their emptiness is open (conjecture R_g). Mahler implies
       R_3, which implies R_4, and so on.
     - *Carrying proof of the gap-g rung* (Local, written for GPT's tier-2 read; F(c) = sum c_k 2^k/3^(k+1)).
       - Lemma 1 (gap). For odd n, T(n) = (3n + 1)/2, and from an even m, T(m) = 3m/2 lowers v_2 by one. So the next
         1 after an odd n_j comes v_2((3 n_j + 1)/2) + 1 steps later. That gap is >= g iff 2^g divides 3 n_j + 1,
         iff n_j = -1/3 mod 2^g. A positive integer's code has infinitely many 1s.
       - Lemma 2 (the cap inside the class). Let M be the supremum of F over codes with every gap >= g. A code that
         begins 0 has F = (2/3) F(shift) < M. A code that begins with 1 continues with k >= g - 1 zeros, then a tail
         c' that begins with 1 or is all zeros, so F <= 1/3 + (2/3)^g M. Hence M <= (1/3)/(1 - (2/3)^g) = alpha_g.
         Equality forces every gap to be exactly g with no leading 0, i.e. the code (1 0^(g-1))^infinity.
       - Lemma 3 (a short gap costs). Two 1s at distance d <= g - 1 give F at the first of them
         >= 1/3 + (2/3)^d / 3 >= beta_g.
       - Forward. If xi > 0 keeps every {xi (3/2)^j} in [0, a) with a <= beta_g < 1/2, then G50 gives
         xi = n + u_0(n) with n >= 1 (n = 0 gives xi = 0) and u_j = F(shift^j c(n)) < a. Lemma 3 then rules out
         every gap below g.
       - Backward. If n >= 1 has every gap >= g, Lemma 2 gives every tail <= alpha_g. Equality at time j would make
         T^j(n)'s code periodic, and a periodic code sums to one rational in R and Z_2, forcing T^j(n) = -alpha_g,
         which is not an integer (G50's baseline). So every tail is < alpha_g <= a, and xi = n + u_0(n) is the
         reconstructed real, a Z-number with every fractional part below a.
       - The interval is nonempty for g >= 3: alpha_3 = 9/19 < beta_3 = 13/27 < 1/2. The lower endpoint is included
         only through integer realization (the backward step), as GC1227 asked.
     - *Two ladders, not one* (corrected per GC1227.1; my first wording merged them).
       - This gap-g ladder runs downward. Its windows shrink toward 1/3, and the union of its rungs is only the
         gap >= 3 class. The formal code (101000000)^infinity has every tail below 1/2 (maximum 9477/19171), yet a
         gap of 2, so it lies on no gap-g rung.
       - The upward ladder comes from the annulus form (PROVED for positive integer orbits: GPT's GC1230 argument,
         read by Local in L714; it needs Parry admissibility, which the prefix condition itself supplies). Let a_M be the value of the
         M-bit prefix of d(1); these rise to 1/2. A positive xi keeps every fractional part in [0, a_M) iff n >= 1 has
         every agreement length m_j = v_2(T^j n - D) in {m < M : d_m = 1}. This uses u_j >= a_M iff m_j >= M,
         which holds on admissible codes only (GC1230's control: n = 3 starts 11, so u_0 >= 5/9 > a_3 while m_0 = 1). The condition excludes the d_m = 0 annuli and also the equal-prefix ball D mod 2^M. (Corrected
         per GC1229: my first paraphrase dropped the ball. GPT's controls: at M = 1 only m = 0 is allowed, so every
         iterate is even and n = 0; at M = 3 the odd iterates must be 5 mod 8, the gap-3 rung, and the formal
         (101000000)^infinity starts with d's prefix 101 and so falls in the ball.) Their union is the Z-numbers
         with sup u_j < 1/2.
       - Neither ladder reaches Mahler. A Z-number whose fractional parts approach 1/2 lies on no rung of either.
     - Novelty is unchecked against Dubickas-Mossinghoff 2009 (its "allowed residues" search), Flatto 1992 and FLP
       1995. The forward half (gaps >= 3 give tails <= 9/19) is GC667's.
   - *The annulus form* (PROOF-SKETCH; classical Parry theory carried through the G51 isometry). Let D be the 2-adic
     start of the critical code d(1) (D = 55817 mod 2^16). Then:
     - Mahler holds iff no positive integer T-orbit avoids, forever, every class {x : v_2(x - D) = m} with d_m = 0.
       The first classes are 3 mod 4, 1 mod 16, 25 mod 32 and 41 mod 64; their Haar measure totals 0.3728.
     - The longest admissible code prefix has length L(x) = min over j of j + v_2(T^j x - D), taken where d at that
       valuation is 0, and the census horizon is L(x) + 1: the violation sits at bit j + m_j, so the prefix of length
       j + m_j + 1 is the first inadmissible one. (Corrected per GC1228's control x = 3: L = 1, census H(3) = 2. The
       first wording called L the horizon.) Built carefully, this is an independent census instrument.
     - For integers, K and S_strict differ only if D is an ordinary integer of either sign; for positive orbits,
       only if D is a positive integer (GC1228). A skeptic checked that D is not an integer of absolute value below
       2^20000.
   - *The sign dual* (PROOF-SKETCH; the symmetry T(-1-x) = -1-T(x) is already in G49/GC669). A negative integer lies
     in S_strict iff a positive eta has every {eta (3/2)^j} in (1/2, 1).
     - So S_strict meets Z only in {0} iff Mahler holds and that dual window problem is empty.
     - Section 1 covered xi > 0 only, while Akiyama, Frougny and Sakarovitch state the question for nonzero xi.
     - Sign test, a filter on methods: an argument using only complement-invariant facts (residues, the G51 isometry,
       free-phase counts) would also prove the dual window empty.
   - *Rotating windows and Conjecture U* (equivalence PROOF-SKETCH; U conjectured). Odd-denominator rational starts
     answer a family of rotating-window problems. Conjecture U says none is non-preperiodic and admissible.
     - U is strictly stronger than Mahler: it is a filter on methods, not progress.
     - Several of the record's integer-side tools see only rationality.
   - *An existence window, off the main line* (COMPUTED, one implementation, the computability skeptic's). A
     memory-1 residue-uniform certificate shows every unit interval [k, k+1], k >= 1, holds a xi with every
     {xi (3/2)^n} in [7/57, 50/57], inside Dubickas's (5/48, 43/48). At [1/7, 6/7] the integer parts 2^j, 2^j - 1 and
     (4^m - 1)/3 carry no orbit (the 2-adic points 0, -1 and -1/3 die).
   - *Closed routes* (recorded so that no block re-enters them).
     - Product-formula or height coupling of the two readings: it is window-blind, and one odd-denominator rational
       approximates u and -n jointly at Dirichlet height.
       *Scope amendment, GPT GC2838:* the product-formula warning is retained,
       but the summary alone is not a carried impossibility theorem for every
       height method. Any renewed claim must specify the common rational finite
       approximants and both place-error/height bounds. The asserted universal
       Dirichlet-height closure was not supplied as a complete proof in the card;
       no new Mahler research is authorized by this amendment. [Review](reports/GPT-SW02-CARD-DOORS-20261110.md).
     - The "bowtie" of a 3-adic past window and a 2-adic future window: zero pinning gain, since it is the
       (K + L)-bit future window of n_(j-K) scaled by (3/2)^K.
   - *Heuristics worded as theorems, all caught by the skeptics:* "converges to Mahler", "only integer input",
     "no rung by finite-hold-set methods", "weakest", "verbatim" (which leaned on a false injectivity), "most integer
     parts", "existence without a certificate", "first integer-specific mechanism", and a sup/inf slip.
     - My own brief contained one error: T is injective on Z, but 2-to-1 on Z_2 (T(0) = T(-1/3) = 0).
   - *Tests* (preregistered in `tests/probes/mahler/mahler_swarm_tests.py` before any run).
     - S1: the rung-3 count among the 4499 census stragglers (coin 214). The w = 63 record holder's surviving prefix
       is rung-3-pure for 156 bits, a 1-2% event on its own.
     - S2: the census of negative starts to 2^63.
     - *Door 2, Conjecture U* (drawn in L714; `tests/probes/mahler/mahler_rational_census.py`, predictions first).
       Every prediction HELD. No positive rational A/B (odd B <= 255, A < 2^44; and B in {65, 211, 665, 2059},
       A < 2^52) keeps every tail below 1/2; record horizons follow the coin law. In (-1, 0) the 117 survivors are all
       preperiodic, with exact certificates (117 of 117; and GPT's bounded proof GC1233, read by Local in L718, shows
       the 4000-bit window already checks every transient when B is odd and at most 255). Post hoc, they reach only the
       cycles 0 and (1 0^(g-1))^infinity for g = 3, 4, 5, the gap-g ladder's periodic codes (denominators
       3^g - 2^g). A filter on methods, not a critical-path step.
     - *Door 0, the rung-g search past 2^63* (drawn in L717; `tests/probes/mahler/mahler_rung_search.{c,py}`,
       predictions first). Every prediction HELD.
       - No rung survivor: g = 4 below 2^70, g = 5 below 2^80, g = 6 below 2^90, g = 8 below 2^100. So, by G294
         (COMPUTED): no xi in (0, 2^70) keeps every fractional part below 35/81; none in (0, 2^80) below 97/243; none
         in (0, 2^90) below 275/729; none in (0, 2^100) below 2315/6561.
       - Record rung horizons were 137, 138, 147 and 147, each within 5% of the coin law W / (1 - log2 lambda_g).
       - The g = 3 run at 2^63 reproduced the census record (157 at 1541211973603965806) from independent code: a
         second-instrument replay of the census maximum.
       - Post hoc: two records start 2-adically near -1/3 and one near 0, the rung-pure points.
       - Finite, inside one rung each; no critical-path step.
     - *The existence-threshold door* (drawn in L718; `tests/probes/mahler/mahler_existence_certificate.py`). Every
       prediction HELD. An independent memory-1 certificate reproduces the skeptic's exact |W| = 322070 at 7/57. So
       every unit interval [k, k + 1], k >= 1, holds a xi with all fractional parts of xi (3/2)^n in [7/57, 50/57]
       (COMPUTED, two implementations; soundness PROVED, GC1235 read in L721). The memory-1 threshold is exactly 7/57 on the grids
       1/912 and 1/1140. Off the main line.
       - *A small witness and a sharp graph.*
         - The certificate reduces to a 15-state closed witness (L721), independently checked by GPT on all 30 edges
           (GC1237). Its 14-state core is mirror-symmetric.
         - GPT's graph-cycle argument (GC1237, read by Local in L723): the cycle 2 -> 11 -> 1 -> 2 (parities 0, 1, 0;
           carries 0, 1, 0) forces q_2 >= 6/19, and the edge 8 -> 2 forces q_2 <= 3(1 - a)/2 - 1. So a <= 7/57 for any
           interval assignment on this graph: the graph is sharp. PROVED for this graph.
         - Universal necessity, that every strategy needs such a graph, is OPEN. The registered depth-40
           infinitesimal search did not complete within its resources: reachable states grew about 3x per level to
           depth 25 (mahler_threshold_proof.py; GPT's GC1238 audits the method's transfer step as sound).
     - *A distance identity* (PROVED: GPT's GC1236, read by Local in L722). For a 2-adic start n with finite horizon
       H(n), the 2-adic distance from n to K, and to S_strict, is exactly 2^-(H(n)-1). At infinite horizon both
       distances are 0, which does not give membership of S_strict. So an unrestricted nearest-set distance census
       only restates the horizon; distances to reference points fixed beforehand are a different observable and stay
       open. (comb note, 2026-10-14, Local, SW-01: added; the result was missing from this file and the map.)
     - *Door 1, the (1/2, 1) dual window* (drawn in L715; a small block).
       - Literature: one search found no treatment of Z_{3/2}(1/2, 1) as a problem of its own. It sits in Flatto,
         Lagarias and Pollington's family Z(s, s + t) at s = t = 1/2, where their 1/3 spread bound does not reach.
       - *The dual ladder* (PROVED: Local's statement by the complement symmetry T(-1-x) = -1-T(x) applied to G294;
         GPT's carrying review GC1233, with the signed lower-endpoint guard and the nonzero-tail step, read by Local in
         L718. Equivalently eta = n + u_0(n), with u_0 the tail sum of n's own code). For g >= 3 and a in [alpha_g, beta_g], a real
         eta > 0 keeps every fractional part of eta (3/2)^j in (1 - a, 1) iff eta = n + 1 - u_0(-1-n) for an integer
         n >= 1 whose every even T-iterate is -2/3 mod 2^g, i.e. every two even steps are at least g apart.
       - At g = 3 that is the window (10/19, 1) and even iterates 2 mod 8; at g = 4, 10 mod 16; at g = 5, 10 mod 32.
         The residue reading matched the gap reading on every n < 2^16 for g = 3, 4, 5 (finite prefixes, 0
         mismatches). S1's negative half (221 of 4622) already measured the first-rung pattern there.
       - No step on the critical path: the dual is Mahler's mirror, and its open part is the same integer-compatibility
         question.
     - *Outcomes (2026-10-14 11:20 BST).* S1 HELD: 217 of the 4499 stragglers are rung-3-pure (coin 214), 103 of the
       2269 chain roots, and 221 of the 4622 negative stragglers. No deviation from the coin was detected in this
       statistic, which is not proof of no integer-specific preference (GC1230.1). The record holder's purity is
       consistent with chance. S2 HELD: every negative start in (-2^63, -1] has a finite horizon
       (COMPUTED), so **no eta in (0, 2^63 - 1] has every fractional part of eta (3/2)^n in (1/2, 1)**. The negative
       record is 153 at x = -6964446546082240544, the counts match the positive side exactly over the free phase,
       and the tail is the same 3/4.

3. **Cloud's evening doors, off the main line** (2026-10-14; RULE30-PRIZE.md 8.109 to 8.112, PROOFS.md section M).
   - K meets 2K, 3K, K/2 and K/3 only in 0 (PROVED: 8.109, GPT's carrying read GC1246). The image form is
     (2/3)K = K ∩ 2Z_2, a proper subset of K, not an invariance of all K.
   - *The sign rule.* K ∩ eK = {0} for e = 2^a u with u odd and 3^a u = 3 mod 4 (PROVED for nonzero integer e: 8.110,
     GC1246). Its Erdős twin, for the 3-adic integers with digits in {0, 1}, is in the same entry.
   - K ∩ 13K = {0} although 13 has sign +1, so the sign rule has no converse (PROVED: 8.112, GPT's carrying read
     GC1253). G296's finite-plateau refinement awaits review, and Cloud's ten further certificates are COMPUTED.
   - These are statements about pairs of points of K; no single integer is excluded. (comb note, 2026-10-14, Local,
     SW-01: pointer added; the honest summary's "No proof, nothing claimed" is about Mahler's conjecture and stands.)

4. **The first outside contribution: Joshua Coon's Lean 4 formalization** (received by e-mail on 2026-10-19 with an
   invitation to link, reuse and cite; checked by Cloud the same evening, CL463). Joshua Coon, with the Astra and Argon
   AI models in GitHub Copilot: [github.com/jjc16/mahler-3-2-lean4](https://github.com/jjc16/mahler-3-2-lean4), Lean
   4.19.0 and Mathlib v4.19.0, 142 files, with a 13-page paper in the repository root. Checked at commit 04ed5389.
   - *Re-replayed at f6d9492* (2026-10-20, CL464). The author's sixteen later commits extend the history, with
     04ed5389 an ancestor. They change one module, `DubickasConfinementAndComplexityExtension.lean`, which gains
     4,669 lines, and its checks file; the build configuration is unchanged. The rebuild in a clean environment has
     0 errors, 0 warnings and no `sorry`. A `#print axioms` on all 126 theorems of the changed module finds only the
     three standard axioms. The new material, which includes catapult traps, defect towers and CRT renormalizations,
     is replayed but not independently recomputed here.
   - *Replayed* (tier 1, a machine certificate adopted on replay under need.html's rule; the scope is each Lean statement
     as written). It was built from scratch here in a clean environment: 142 of 142 files, 0 errors, 0 warnings,
     0 `sorry`, and 637 axiom reports, all within `propext`, `Quot.sound` and `Classical.choice`. An independent
     `#print axioms` on 19 headline theorems agrees. Their statements use `Int.fract` directly, so nothing hides in a
     definition.
   - *Independently recomputed* (`tests/probes/mahler/mahler_contrib_checks.py`, our code from their statements):
     - seed 149 survives 28 steps and fails at 29, and nothing below 4096 survives step 29;
     - their seed 29871555608238677 survives 113 and fails at 114;
     - the first-defect valuation lock v_2(19 a0 + 9) = 3 j0 + 3 held on 40,249 seeds;
     - five window and union escape bounds held at every W = 1..10;
     - the (2/7, 5/7) branch counts equal Mahler's binary partition numbers through depth 15 and give 200 against 202
       at depth 16.
   - *Where it meets our record.*
     - Their `mahler_conjecture_iff_leastPositiveSurvivor_unbounded` is the Lean form of GC664. Their
       `gap_ladder_short_gap_cost_and_cap` checks the two inequalities that carry Lemmas 2 and 3 of the gap-g window
       ladder (G.GPT294). Their B(29) >= 4096 and seed 149 are our census control C0.
     - So, for the first time, pieces of this record are machine-checked by someone outside the project.
   - *What it adds.*
     - Escape bounds for confinement sets beyond the 1/p barrier: the window [1/6, 13/24) of length 3/8 at base 3/2,
       [1/3, 5/8) at base 4/3, and unions of total length 7/12, 2/3 and 25/36. The unions sit well above Dubickas's
       20/39 example of 2008.
     - Formal proofs of Dubickas (2009) Theorem 1 in general base, with explicit escape bounds.
     - Exclusions of two-letter mechanical, Thue–Morse, period-doubling and rapid-growth block chains.
     - A catalogue of eighteen formally diagnosed dead ends for classical Diophantine tools.
     - Its novelty against Stephan (2026) and Dubickas–Mossinghoff (2009) is not checked here.
   - *Two notes for the author, and one sharpening.*
     - The 55-bit seed is a long survivor, not a record. Our census (2026-10-14) has 9850069454682037, 54 bits,
       surviving to step 137, and a horizon of 157 below 2^63.
     - Two theorem names in the paper's table differ from the code.
     - Sharpening, found by the recomputation: the lock extends to defects of length 1 and 2, giving 3 j0 + 1 and
       3 j0 + 2. The reason is that the T-code map is a 2-adic isometry (G51), so v_2(a0 + 9/19) is the length of the
       common prefix of a0's code and (100)^infinity.
   - Nothing here touches Mahler's conjecture itself, and the author says so: the wall is the same one, the gap
     between the 2-adic set and one positive integer.

## Rule30 to Mahler: episodes and recharge (GC2342)

**Status:** PROOF-SKETCH, GPT, 1 November 2026; independent carrying read pending.
An explicit application of known G50/G51 and the known periodic-shadow valuation law.
No new general theorem, literature priority, kernel replay or submission is claimed.

### The pull and the question

The Rule30 ether-episode work succeeded by tracking the first disagreement with a periodic background,
then proving that a suitable quantity cannot be replenished along the relevant evolution. Import the
question, not the Rule30 Boolean identity: **can the arithmetic countdown for a Mahler periodic pattern
be replenished by a short interruption?** If yes, any global argument needs more memory than that clock.
GC2341 records the prediction and counterfactual before the carrying derivation was written here.

An *episode* here is a consecutive run of parities matching a specified periodic word, with its starting
position fixed. A *phase* says which position in that word is next. A *reset* below means the explicit
four-step word1000, not a claim that the full dynamical state forgets its past. Bits1/0 mean odd/even.
Write F(n)=ceil(3n/2). For a nonzero integer z, v2(z) is the number of factors of2 dividing z.
The clock v2(19n+9) is exactly the number of initial parities matching100100... (known machinery).

### A fixed interruption permits unbounded recharge

For every integer k>=1 there is a positive integer n such that:

1. Its initial match to100100... has length exactly3.
2. Its first four parities are1000, and at time4 its match to100100... has length exactly k.
3. The actual positive real number xi=n+73/171 stays in the required fractional half-interval
   through time4+k and first leaves it at time5+k.

Thus this is not merely a formal bit word, nor an arithmetic example that already failed the fractional
test. It has both forms of finite compatibility. The integer n changes with k; no single infinite
survivor is constructed.

**Construction.** Put L=k+4. Choose n in the unique residue class

    171*n+73 = 2^L (mod 2^(L+1)).

The inverse of171 exists modulo every power of2 because171 is odd. The least residue n is positive
and odd, and n<2^(k+5). The congruence gives v2(171n+73)=L. Reducing modulo32 gives n=5 (mod32),
so3n+1 has exactly four factors of2. The first four parities are therefore1000 and

    F^4(n)=(81*n+27)/16,
    9*(19*n+9)=(171*n+73)+8,
    19*F^4(n)+9=9*(171*n+73)/16.

Consequently the first clock equals3, while the clock after the four-step interruption equals k.
This already refutes a uniform recharge bound depending only on that first clock, phase and interruption.

**Fractional and endpoint guard.** Use the infinite formal word1000(100)^infinity. Its fractional
values, obtained from G50's tail sum, start

    u0=73/171, u1=8/57, u2=4/19, u3=6/19,
    u4=9/19, u5=4/19, u6=6/19, followed by this three-cycle.

Every value is strictly below1/2 and nonnegative. The negative rational a_t=-u_t follows the corresponding
integer branches (parity for an odd-denominator rational means numerator parity after reduction).
Initially n-a0=n+73/171 has valuation L. While the two parities agree, their difference is multiplied
by3/2, reducing this valuation by exactly one. Induction gives agreement for t<L and opposite parity
at t=L. Until time L, the identities n_t+u_t=xi*(3/2)^t hold. At the next step, the opposite parity
changes the fractional part by1/2 modulo1. It is u_(L+1)+1/2, which lies in[1/2,1). This proves the
claimed first failure at L+1, not merely an eventual failure.

**Hand control.** Take n=37. Then171n+73=6400=2^8*25, hence k=4. Its integer orbit begins

    37,56,84,126,189,284,426,639,959.

The parities are100010011: first disagreement with100100... at time3, followed by exactly four
matches from time4 before disagreement at time8. For xi=37+73/171 the fractional part at time9 is
6/19+1/2=31/38, the first failure. The smaller control n=5 gives L=5 and k=1. These are hand
substitutions, not a machine census. No numerical research job was launched: a prospective host
preflight could read free/inactive memory but its sandboxed swap query was unavailable; the block
continued with the exact hand argument instead of relaxing monitoring or launching a job.

**What pays for a long return?** Necessarily

    2^(k+4) <= 171*n+73.

The initial integer must grow at least exponentially with the desired return length. This is the
information discarded by recording only the three-tick first episode and the extra zero. The construction
does not defeat a bound that retains initial size, a full residue or other information tied to the start.

### Which further constraints are already known

G51 says that any T-bit word determines exactly one integer residue modulo2^T. Every finite
concatenation of100 and1000 extends to an infinite fractional word with one-gaps at least3, so every
tail is at most9/19. It therefore has a positive-integer realization for its finite duration. This is
a **known consequence of G50/G51**, not an additional discovery: excluding a finite word merely because
it is a difficult arrangement of these episodes cannot work uniformly over all starting integers.

The fixed-start question is different. For a single infinite word, its least compatible residues r_T
obey r_(T+1)=r_T or r_T+2^T. An ordinary nonnegative integer realizes the whole word exactly when these
residues eventually stop changing. A useful global resource must constrain this continuing choice,
or something equally strong; local admissibility plus a decreasing within-episode clock is insufficient.
Even the infinite tail1000(100)^infinity itself has no positive integer realization: it would require
171n+73 divisible by every power of2. Its finite positive witnesses are not an infinite witness.

### Source comparison and exact scope

Record searched: G50/G51; GC666/667 and GC929; MAHLER's contributor section; COLLATZ-PRIZE sections5/9;
the October25 [Collatz appraisal](reports/rstation/GPT-COLLATZ-TO-RULE30-APPRAISAL-20261025.md);
Rule30 episode report and actual kit `Rule30EtherEpisode`/`Rule30EtherGrounding` at the GC2340
complete snapshot f1cb20be4c959ee1d92d99f3eafdfcaa945aa63d; website trio/carry/technical pages;
targeted residue, periodic-prefix, reset and valuation searches. The kit/portal snapshot was completed
at13:58:37Z on1November; this entry does not claim another complete external refresh.

Coon's current [source at27314bbf](https://github.com/jjc16/mahler-3-2-lean4/tree/27314bbfcb2728b5da4ac086237bc483c1a450ef)
was fetched. Relevant already-existing declarations include `orbit_parity_eq_upto_iff_mod_two_pow`,
`exists_pos_seed_iff_seedResidue_stabilizes_pos`, `local_prefix_first_defect_valuation_lock`,
`single_block_signed_defect_identity` and `defectCocycle_residual_eq_growing_boundary_affInv`.
In particular the latter explicitly identifies a growing boundary quantity, not a descending rank.
The targeted source read is not a complete carrying read or compilation of this newer repository;
the historical clean-build receipts above remain pinned to their older commits.

| Source at27314bbf | SHA256 |
|---|---|
| SparseDefectCocycleAndValuationLock.lean | 978aeb0a56a21b63732c1f63e109b7d9da234ac156e94770497caf45ba1be041 |
| ExactSeedResidueTreeAndStabilization.lean | b005a032ad4f483845bac8518ded93c27c740364b9564ae1c0517fb92b794a05 |
| AperiodicSlackCocycle.lean | b230c1a26157b53b94e443263e6799fa50e34a4828ed6571bce6f8100faf8884 |

The broader bridge is already primary literature: [Kopra2022](https://arxiv.org/html/2202.13809v1)
places Rule30 and fractional multiplication automata in a common expansive class and explicitly
transfers number-theoretic ideas to automata. [Kari–Kopra2017](https://www.numdam.org/item/ITA_2017__51_4_191_0/)
uses automaton traces to study fractional multiplication. These are precedent for the programme,
not proofs that our binary local identities transfer to the six-symbol multiplication automaton.
Flatto–Lagarias–Pollington1995 remains prior art for the underlying integer/fraction separation.
No paywalled Parry source is required for the argument here.

### Durable queue

- **Current result:** the displayed unbounded recharge application awaits an independent carrying read,
  especially the strict fractional endpoint and the quantifier that n varies with k.
- **Next executable investigation:** write the exact returns on the *odd quotients* for successive
  odd-step gaps3 and4, then compare every proposed resource against the existing theorem
  `odd_quotient_transition_identity`: 2^(c_next)*u_next=3^c*u+1. Test any proposed descent first on
  the displayed family and the fixed-start residue condition. The discriminating requirement is a
  cross-return constraint absent from a single valuation, not another repeat bound or longer census.
- **Cold:** scalar episode-clock recharge bounds; reopen only with an additional state variable or
  a genuinely restrictive hypothesis that excludes this family. Finite survival is not infinite survival.
- **Warm alternative:** Collatz return-map compositions, retaining the number of odd steps and the
  exact affine intercept; compare the known positive-integer shadows before proposing a descent.
- **Independent curiosity:** EightStreets' protected partition core: can a finite boundary description
  retain contested items and counts under an actual reduction? Use FOUR-BIN-PARTITIONS section45's
  shared-zero obstruction as an adversarial control; scalar slack alone is already inadequate.
- **Back to Rule30:** distinguish a measured mismatch clock from a globally non-replenishable resource.
  The proved ether potential establishes the latter only in its exact background/frame/hypotheses.
  No Mahler conclusion is imported as a theorem about the wall or centre column.

## The 0.4 ceiling and the passage toward a half (GC2344)

Owner pull, 1 November 2026: lower the ceiling to0.4 and relate its breaches to reaching0.5.
Interpretation: the narrower safe interval is[0,2/5), with[2/5,1/2) the intervening band.
**Status:** new scoped deductions below are PROOF-SKETCH, independent carrying read pending;
G50/G51 and the G294 window ladder are existing reviewed tools. No novelty or nonexistence claim.

Write x_t=xi*(3/2)^t=n_t+u_t, where n_t is its integer part and u_t its fractional part.
Define T_a(xi) as the first t>=0 with u_t>=a, allowing infinity. Necessarily T_(2/5)<=T_(1/2).
The question is what happens between those two times; the two times may also be equal.

### First crossing and forced return

If the first crossing of2/5 occurs at time t>=1 and u_t<1/2, then the previous integer n_(t-1)
is even and u_(t-1) belongs to[4/15,1/3). Indeed the even branch gives u_t=3u_(t-1)/2;
an odd previous integer with u_(t-1)<2/5 either fails the half test or produces u_t<1/10.

Once u_t is in[2/5,1/2), survival for one more step forces n_t odd. An even integer would
produce a fractional part in[3/5,3/4), an immediate half breach. With n_t odd instead,

    u_(t+1)=(3*u_t-1)/2 belongs to[1/10,1/4).

Thus crossing the lower ceiling can force a return deep into the safe region. A rise through
this band is not monotone progress toward half. The integer parity decides whether the next step
escapes or returns. This is the established G50 branch law specialized to the two chosen thresholds.

An actual positive-rational control is xi=46+4/15:

| t | Integer part | Fractional part |
|---|---|---|
| 0 | 46 | 4/15 |
| 1 | 69 | 2/5 |
| 2 | 104 | 1/10 |
| 3 | 156 | 3/20 |
| 4 | 234 | 9/40 |
| 5 | 351 | 27/80 |
| 6 | 527 | 1/160 |
| 7 | 790 | 163/320 |

Here T_(2/5)=1 and T_(1/2)=7. The final integer is the actual floor790; the safe ceil-map
would give791 there and is no longer the integer-part evolution after the half condition fails.

### Why exactly0.4 is an interesting intermediate threshold

The already proved ladder has plateaus ending at97/243 and beginning at27/65:

    97/243 < 2/5 < 27/65.

So0.4 lies between two simple minimum-gap descriptions. A gap d is the distance between
consecutive odd steps: gap4 means an odd step followed by three even steps and then the next odd.
For a hypothetical infinite survivor below2/5, every gap is at least4: two ones at distance3
already contribute35/81>2/5 to the fractional tail. But gap4 is not itself excluded.

At an odd step let u be its fraction and v the fraction at the next odd step, d positions later.
G50's exact tail identity is

    u=1/3+(2/3)^d*v.

For d=4 and u<2/5 this forces v<27/80. If e is the following odd-step gap, its next odd fraction
w is at least1/3, and hence

    1/3+(2/3)^e/3 <= v < 27/80,
    (2/3)^e < 1/80.

Since80*2^10>3^10 and80*2^11<3^11, **gap4 must be followed by a gap of at least11**.
This statement assumes the two subsequent odd steps exist and the relevant fractions remain in the
window; it is not an unconditional claim about a truncated observed word. Positive integer infinite
ceil-map itineraries have infinitely many odd steps.

The11 is sharp at this local level: the formal word with ones only at0,4,15 has every tail below2/5.
Its maximal tail is1/3+(2/3)^4/3+(2/3)^15/3, with margin13307/215233605 below2/5.
G51 makes any finite prefix an actual positive-integer/fractional realization. Its eventually-zero
formal continuation is not claimed to have a positive-integer infinite realization.
Yet repeating gaps4,11 forever fails: the tail at the beginning of a gap4 exceeds2/5 by
6487/71580695. Thus the local necessary rule alone is not sufficient; later gaps consume more room.

### What a threshold breach cannot guarantee by itself

There is no uniform finite bound, over all positive starts, on the permitted delay after a crossing
at exactly2/5 before reaching1/2. For each prescribed finite length L, iterate the fractional rule
b=0 below1/3 and b=1 at or above1/3, starting at u=2/5. This formal trajectory remains in[0,1/2).
G51 realizes its first L parities by one residue r modulo2^L. Choose a positive integer n in that
residue and also n=0 modulo3; the Chinese remainder theorem permits this because3 and2^L are coprime.
Then xi=(2/3)*(n+2/5) starts with fractional part4/15<2/5 and reaches exactly2/5 at time1.
It survives the half test for the prescribed further finite length. The selected n changes with L.
This neither constructs an infinite survivor nor bounds the delay for one fixed start.

### Search, arithmetic check and next step

Record searched: G50/G51, G294 and the current window ladder; targeted2/5,97/243,27/80 and gap11
searches in Coon27314bbf's source. Its centered windows and nearest-integer arcs are different sets
from[0,2/5); no result about them was used to exclude this interval. The established integer/fraction
method is also in Flatto–Lagarias–Pollington1995. This is a worked application, without priority claims.

Before the small PARI/GP arithmetic check, hand predictions were: budget27/80, threshold gap11,
finite4/11 prefix below2/5, periodic4/11 tail above2/5, and the displayed first-crossing orbit.
All were confirmed by exact rational substitutions in GP2.19; eight trajectory values and four
inequalities only, no census, solver query or statistical fit. Same-worker arithmetic is a self-check.

Next executable question: retain the **remaining fractional allowance** after the4,11 pair and
write its exact permitted next-gap condition, using the known tail identity. Compare it with Coon's
existing slack identities before treating it as additional. In parallel as an independent direction,
classify entry/exit branches of[2/5,1/2) with the integer residue retained. Any claim about the delay
must name its fixed-start or bounded-start-size hypothesis. An unchanged global delay bound is cold
because the finite-prefix construction above refutes it. Both schedules remain paused.

## Moving the divider: what makes a threshold interesting (GC2345)

Owner pull, 1 November 2026: keep the half fixed and vary the lower ceiling, allowing rational
and irrational choices. **Status:** applications and the explicit irrational example below are
PROOF-SKETCH, independent carrying read pending. G50/G51/G294 remain the reviewed foundations.
No new Mahler exclusion, priority claim, large computation or full external-library review.

### A divider labels a run; requiring confinement changes the question

For 1/3 <= a < 1/2, retain both first-crossing times T_a and T_(1/2). Merely moving a changes
our description of the same actual orbit. Requiring u_t < a at every time instead selects a
smaller class of runs. These are distinct uses of the divider.
For every such a, a first entry from below a into [a,1/2) at a positive time comes from an even
integer with previous fraction in [2*a/3,1/3). Once inside, an even integer fails the half test
next, whereas an odd integer returns to [(3*a-1)/2,1/4). This is GC2344 with a variable bound,
by the same two branches. The return law varies continuously with a; it does not make 2/5 singular.
The intrinsic branch boundary is 1/3. Staying strictly below it forever would force all integer
parts even; their initial value must then be divisible by every power of 2, and hence zero.
The fractional part must also be zero to stay bounded under repeated multiplication by 3/2.
Thus no positive start survives that strict window; this elementary special case is already known.

### Exact pattern thresholds, rather than a grid of convenient decimals

Put r=2/3. For a finite binary word w of length L, followed by zeros, define

    H(w) = max_(0 <= j < L) sum_(j <= k < L) w_k * r^(k-j) / 3.

All its fractional tails are strictly below a exactly when H(w)<a. Every H(w) is rational.
If H(w)<1/2, G51 realizes every required finite segment with a suitable positive integer start;
the infinite zero continuation is not a positive-integer realization. Later nonzero digits can
only increase these tail costs. Therefore H(w) is also an exact finite obstruction when H(w)>=a,
not a sufficient test for an arbitrary infinite continuation.

For three odd digits at positions 0,d,d+e the complete finite-word threshold is

    H(d,e) = max((1+r^d+r^(d+e))/3, (1+r^e)/3).

At d=4 and e>=4 the first term is the maximum. This gives the nearby change points:

| First gap, second gap | Exact threshold | Approximation |
|---|---|---|
| 4,10 | 5744137/14348907 | 0.400318783863 |
| 4,11 | 17216027/43046721 | 0.399938174153 |
| 4,12 | 51615313/129140163 | 0.399684434346 |

At equality the strict window excludes the pattern. Thus 0.4 separates the 4,10 and 4,11
patterns but is not itself one of these change points. The selected pair threshold alone does
not determine admissibility of the full language. Repeating 4,11 has the different geometric-series
threshold (1+r^4)/(3*(1-r^15)) = 0.400090624993..., already above 0.4 (GC2344).

G294 supplies whole intervals of ceilings with the same ordinary-integer criterion: e.g.
[81/211,97/243] means all odd gaps at least 5, and [27/65,35/81] means all odd gaps at least 4.
The lower endpoint removes an equality periodic word on the purely fractional side, but that
word cannot belong to a positive ordinary integer anyway. These are criteria, not claims that
any positive integer satisfies them. If Mahler nonexistence holds, the positive survivor sets
are all empty even though the fractional pattern sets change richly with a.

### An explicit irrational threshold on the fractional side

An infinite word b has ceiling H(b)=sup_j sum_(k>=0) b_(j+k)*r^k/3. If a>H(b), it survives;
if a<H(b), it fails. At equality, strict survival depends on whether the supremum is attained.
Rationality alone does not settle any of these questions.

Concrete example: put ones at s_0=0 and s_k=4*k! for k>=1, namely 0,4,8,24,96,480,...,
and zeros elsewhere. Let

    A = (1 + sum_(k>=1) r^(4*k!)) / 3.

Its successive gaps 4,4,16,72,... are nondecreasing. From any later one, each subsequent one
is at least as far away as the corresponding one from position zero. Termwise comparison gives
every later odd-tail value <=A; tails starting with zeros are smaller. Hence H(b)=A, attained at
zero. All gaps are at least 4, so A<=27/65<1/2. With
P=(1+r^4+r^8+r^24)/3, the elementary geometric remainder bound gives P<A<P+r^96, or

    0.41220290323340593130... < A < 0.41220290323340594376... .

To see A is irrational, truncate after s_m to A_m, whose denominator divides 3^(s_m+1).
The strictly positive remainder is at most r^s_(m+1). If A=p/q were rational, a nonzero difference
would be at least 1/(q*3^(s_m+1)). But s_(m+1)=(m+1)*s_m, so eventually the remainder upper bound
is smaller than that lower bound, a contradiction. This is the classical fast rational-approximation
argument, not a new irrationality method. A is a genuine right-sided change point for the fractional
survivor set: this word is excluded at A and included for every ceiling greater than A.

**Adversarial control: this word is excluded on the integer side.** If its first integer were n>0,
then n_t+1 <= (3/2)^t*(n+1). At an odd step t with next odd gap D, the next integer is divisible
by 2^(D-1), so 2^(D-1) <= (3*n_t+1)/2 < (3/2)^(t+1)*(n+1). For t=s_m and
D=s_(m+1)-s_m=m*s_m this is impossible for large m. This is the known sparse-gap obstruction
(GC667) applied explicitly. The example demonstrates an irrational structural threshold, not a
candidate Z-number. Finite realizations still exist separately by G51.

### Search and exact scope of the external update

Record searched: G50, G51, G294, GC667, GC2344, the window-ladder and threshold entries; the
Rule30 kit/portal cached index at f1cb20be (13:58Z refresh) had no relevant match in this scope.
No new Rule30 novelty claim or full portal refresh was made in this Mahler discussion.
Coon's Mahler remote was freshly fetched: main advanced from 27314bbf to
bd92eb17692e6257084eb39142419fdd6d1fd285. Targeted source read of
[BetaShiftThreeHalvesDictionary.lean](https://github.com/jjc16/mahler-3-2-lean4/blob/bd92eb17692e6257084eb39142419fdd6d1fd285/BetaShiftThreeHalvesDictionary.lean)
(SHA256 f49ad1a88f13a18e255709f1379c52ec55a764a963a81e6ee3714757de1a647f):
`fract_dynamics_conj_betaMap`, `halfBetaStep_in_half_interval` and its iterate proof carry the
known rescaling y=2*u to y'=frac(3*y/2); the file also contains finite itinerary realization and
periodic sign obstruction statements. No rebuild or complete carrying read of the new modules.
The rescaling is also already in our MAHLER summary, credited to Flatto 1992.

The related literature calls changes in survivor sets *bifurcations*: the set of starting points
that avoid a forbidden region changes with its boundary. [Kalle–Kong–Langeveld–Li](https://arxiv.org/abs/1803.07338)
and [Baker–Kong](https://arxiv.org/abs/1904.07007) study lower holes at zero. Our rescaled ceiling
is an upper hole [2*a,1); do not transfer their theorems or endpoint conventions without a proved
translation. Their fractional survivor sets do not impose Mahler's positive-integer realization.
The irrational example uses the standard lacunary-series rational-approximation mechanism; compare
[Marques–Ramirez–Silva, introduction](https://doi.org/10.1017/S0004972715001239) for that classical context,
not as a theorem about this specific ceiling.

Tiny PARI/GP substitutions evaluated the displayed rational formulas and the rigorous irrational
bracket; no search, horizon enlargement or proof by rounded decimals. The interactive explanation
uses exact integer comparisons for its decimal divider and three-odd pattern test. Its test harness
initially expected second gap 5 at 0.42; the correct reviewed gap-4 plateau requires 4, and the
harness expectation was corrected. No mathematics or display code was altered to conceal that check.

**Next executable step:** classify the exact finite-pattern change points between 97/243 and
27/65, starting with H(4,e), then append a third gap while retaining the remainder bound. Ask which
changes alter the admissible pattern set and which only restate an existing obstruction. No brute
decimal sweep. **Independent alternative:** carry integer residue constraints across the same
short patterns; keep finite realization and one fixed infinite start distinct. The factorial example
is closed as a positive-integer candidate by the bound above. Both schedules remain paused.

## Exact widths of the bands around 0.4 (GC2346)

Owner question: why the two nearby thresholds, are they fractions, and how does their spacing change?
**PROOF-SKETCH corollary of GC2345/G50**, independent carrying read pending; exact arithmetic self-check.
This is the fixed-first-gap family, not a classification of every moving-divider change point.

Fix the first odd gap at 4. For a second gap e>=4, the three odd positions are 0,4,4+e, and their
largest fractional tail (with zeros afterward) is

    B_e = (1 + (2/3)^4 + (2/3)^(4+e))/3
        = 97/243 + (1/3)*(2/3)^(4+e).

The second odd-tail value is (1+(2/3)^e)/3; for e>=4 it is smaller than B_e, so the maximum
in GC2345 introduces no additional branch in this range. Every extra place of waiting multiplies
only the third odd digit's contribution by 2/3. Direct subtraction, before numerical evaluation,
gives the exact width and ratio:

    W_e = B_e - B_(e+1) = 2^(e+4)/3^(e+6),
    W_(e+1) / W_e = 2/3.

Thus widths shrink geometrically by one third per additional step of waiting. Reading toward
shorter gaps reverses the factor to 3/2. The thresholds themselves approach 97/243, not zero;
the excess B_e-97/243 and the widths both decay by the same factor 2/3.

The owner's selected interval has exact endpoints

    B_11 = 17216027/43046721 = 0.3999381741526840105...,
    B_10 = 5744137/14348907 = 0.4003187838627708717...,
    B_10 - B_11 = 16384/43046721 = 0.0003806097100868612... .

The finite three-odd test has minimum second gap 11 for ceilings in (B_11,B_10]. The lower endpoint
is excluded and the upper included because the requirement is strictly below the ceiling: at
B_11 the 4,11 pattern itself fails; at B_10 the 4,10 pattern still fails. Later nonzero digits
can add further obstructions. This interval is not asserted to be a plateau for all infinite
fractional patterns, much less a family of positive-integer infinite survivors.

Exact GP substitutions checked e=9..13, the two fractions, and the common ratio 2/3. They replay
hand formulas rather than fit a law to measured data; no census or solver run. Record searched:
GC2345's H(d,e), GC2344's 4-then-11 control, and the reviewed G50 tail sum / G294 plateau endpoint.
No new external theorem or novelty claim is involved in this algebraic clarification.

Next: append a third gap f. The earliest tail then adds (1/3)*(2/3)^(4+e+f), but the maxima at
later odd positions must also be checked. Determine which subintervals genuinely change the
finite allowed patterns. Independent alternative: retain the actual integer residue constraints
for the same words. Both schedules remain paused.

## A complete finite-memory plateau containing 0.4 (GC2348)

**Status: PROOF-SKETCH, GPT, 1 November 2026; independent carrying read requested.**
This completes GC2347's hand test. It extends the reviewed G294 proof method to an explicit
three-gap rule, using G50/G51 throughout. No novelty, infinite positive survivor, Lean compilation
or prize claim. The earlier GC2344–46 caution remains correct for their incomplete two-gap tests;
the complete rule below now supplies the missing sufficiency argument in this particular interval.

### Statement and conventions

For a binary sequence b, put r=2/3 and

    U_j(b) = (1/3) * sum_(k>=0) b_(j+k) * r^k.

A gap is the positive distance between consecutive ones. Let L consist of exactly the binary
sequences satisfying these rules wherever the named successive gaps exist:

1. Every gap is at least 4.
2. A gap of 4 is followed by a gap of at least 11.
3. Gaps 4,11 are followed by a gap of at least 7.

Sequences with finitely many ones, including the zero sequence, are allowed in this formal class.
Define the following exact numbers:

    P = (1+r^4+r^15)/3,
    A = P/(1-r^22) = 12550483683/31376865305
      = 0.3999916359076201860...,
    B = P+r^21/3 = 12552580835/31381059609
      = 0.4000050027437555032... .

**Fractional statement.** For every ceiling a in (A,B],

    all U_j(b)<a  if and only if  b belongs to L.

In particular this holds at a=2/5. The interval is a maximal interval on which this entire formal
fractional language is unchanged: at A a critical periodic word drops out; above B a forbidden
finite word enters. This is stronger than the finite-pattern bands of GC2346.

**Ordinary-integer statement.** For every a in [A,B], a real xi>0 remains in the strict fractional
window [0,a) forever exactly when xi=n+U_0(b(n)), where n>=1 and the parity code b(n) of
F(n)=ceil(3*n/2) belongs to L. The endpoint A is included here because the critical equality word
cannot be a positive-integer code. This equivalence does not assert that any such positive n exists,
and no maximality assertion is made for the actual integer survivor sets.

### Necessity: every forbidden pattern has enough fractional cost

A gap at most 3 contributes at least (1+r^3)/3=35/81>B at its first one.
Once all gaps are at least 4, a 4 followed by a gap at most 10 contributes at least
(1+r^4+r^14)/3>B. Once those are excluded, 4,11 followed by a gap at most 6 contributes
at least (1+r^4+r^15+r^21)/3=B. Nonnegative later terms cannot lower these costs.
Consequently all three patterns fail every strict ceiling a<=B. This includes equality at B.

### Sufficiency: three exhaustive first-block cases

Let M be the supremum of U_0 over all words in L beginning with a one. Clearly M<=1.
L is invariant under taking suffixes. A word beginning with one has one of three complete
initial blocks, or terminates during one of these blocks:

| Case | Complete initial gaps | Contribution before the next block | Maximum discount on the remaining tail |
|---|---|---|---|
| I | d>=5 | 1/3 | r^5 |
| II | 4,e with e>=12 | (1+r^4)/3 | r^16 |
| III | 4,11,f with f>=7 | P | r^22 |

The rules are exhaustive: a first gap cannot be smaller than 4, and the only exceptional next
gap after 4 is 11. After each complete block the remaining suffix is again in L. An incomplete
terminal block contributes at most P and adds no remainder. Thus

    M <= max(1/3+r^5*M, (1+r^4)/3+r^16*M, P+r^22*M).

The fixed points of these three increasing affine maps are respectively

    81/211, 177147/443105, A,

and the first two are strictly smaller than A. If M>A, all three expressions on the right would
be strictly smaller than M, contradicting the displayed inequality. Hence M<=A. A tail beginning
with zeros is r^h times a tail beginning with a one, or is zero, so every U_j<=A.
This proves sufficiency for every a>A. The repeating gap sequence (4,11,7) realizes equality:
its binary period has length 22 and ones at positions 0,4,15. Its tail at the start of each period
is P+r^22*P+...=A. It belongs to L, so the supremum is exactly A.

### Endpoints, maximality and the integer-side guard

For equality U_j=A, the first-block argument forces case III with the shortest third gap 7,
and forces the remainder to equal A again. Iterating forces the exact periodic gap sequence
(4,11,7) from that position onward. Cases I/II, a longer gap, or termination give strict inequality.
Thus at a=A the formal strict language removes precisely the L words with such a periodic suffix.
The remaining L words still have every tail strictly below A, even when their supremum is A.

At the upper endpoint, the finite word with ones at 0,4,15,21 and zeros thereafter has maximum
fractional tail exactly B: its later one-tail values are (1+r^11+r^17)/3, (1+r^6)/3 and 1/3,
all smaller than B. It fails rule 3 but passes every ceiling a>B. These two witnesses establish
both boundaries of the formal plateau, without assuming positive-integer infinite realizations.

For the ordinary-integer endpoint, write

    C = 3^21 + 2^4*3^17 + 2^15*3^6 = 12550483683,
    D = 3^22 - 2^22 = 31376865305.

One 22-step block of the critical word sends n to (3^22*n+C)/2^22. Repeating that word k times
with integral intermediate values forces 2^(22*k) to divide D*n+C: multiply the iterated affine
identity by D and use that 3 is odd. Repetition for every k would force D*n+C=0, impossible for
n>=1. This is G50/G51's known periodic sign obstruction, with exact constants supplied here.
It applies at any later age too. Therefore every positive integer code in L has U_j<A everywhere;
G50 then supplies the real companion and proves the stated equivalence on the closed interval [A,B].
The positive real xi with integer part zero cannot supply an extra infinite survivor (G50).

### What resetting means, and what it does not mean

At a=2/5, let c be the inherited strict upper bound on the fractional value at a current odd step.
After a gap d the next odd-step bound is min(a,(c-1/3)/r^d). Starting with c=a gives

    after 4:       c = 27/80,
    after 4,11:    c = 59049/163840,
    after 4,11,7:  uncapped c = 9700803/20971520 > a.

A third gap 6 is impossible because 1/3+r^6/3 >= 59049/163840; gap 7 suffices even with any
continuation already bounded by a. After 4,12 the uncapped bound also exceeds a. A single gap
at least 5 does the same. The three-state description is therefore: ordinary state; after a 4;
after 4,11. Each permitted completed block returns to the ordinary fractional bound. This is a
reset of the inherited fractional restriction, not a reset of the actual integer or its residues.
The proof above, rather than a finite reset calculation alone, establishes the infinite-language claim.

An actual finite control retains that distinction. G51's least residue for the 22-bit critical
period is n=217509 modulo 2^22. The positive real xi=217509+A follows that period through its
first 22 updates with maximum fractional value A<2/5, checked directly by exact rational
multiplication and floors. Its parity ones at times 0..21 are exactly 0,4,15.
The value v2(D*217509+C)=24 permits the first period but forbids two complete repeats, since
44 bits of divisibility would be needed. The fractional periodic path exists; this particular
actual integer cannot track it indefinitely. No claim of escape time was inferred from that valuation.

### Search, validation and next executable question

Prediction/counterfactual and the three-case proof test were published first in GC2347 at d6b1b083.
Record searches: GC2344–46, G50/G51/G294, and the Mahler finite-memory/plateau entries; the broad
numeric search produced unrelated numeric matches, so the Mahler-scoped search was used to disambiguate.
The cached Rule30 kit/portal index at f1cb20be supplied no matching Mahler statement; this is not a
fresh portal audit or a novelty conclusion. Coon main bd92eb1 was refreshed in GC2345; the relevant
unchanged AperiodicSlackCocycle.lean was read for `integerSlack_cocycle_eq`,
`prefix_weighted_tail_budget` and `next_block_threshold_of_integerSlack_pos` (SHA256
b230c1a26157b53b94e443263e6799fa50e34a4828ed6571bce6f8100faf8884).
Those general remainder identities are prior machinery; no new generic slack law is claimed here.
G294's extremal-periodic-word proof supplies the immediate reviewed template. The beta-hole
literature cited in GC2345 studies related survivor plateaus with different hole conventions;
no lower-hole theorem was silently imported.

Exact PARI/GP substitutions checked A<B, A<2/5<B, the two smaller affine fixed points, all three
forbidden-cost bounds, reset caps and the stated finite positive witness. They are self-checks of
hand formulas, not a census or a fitted law. No substantial computation, job delegation, Lean build
or submission. Independent review should carry the exhaustive first-block/supremum step and the
endpoint transfer to positive integer codes; numerical substitution alone does not carry these.

**Next executable step:** retain the three-state fractional condition together with the exact
odd-to-odd integer map: d=v2(3*n+1), next odd=3^(d-1)*(3*n+1)/2^d. Compare its permitted returns
with the known residue/slack machinery and identify a constraint that survives changes of block;
do not infer one from the fractional reset. **Independent alternative:** move just above B and
analyze the newly admitted 4,11,6 block with its remaining-tail constraint. The former third-gap
sufficiency gap is closed at PROOF-SKETCH level; general integer nonexistence stays open.
Both schedules remain paused. Passive carrying-review pointer only; no sleeping worker dispatched.

## What the reset forgets and what the integer retains (GC2350)

Owner asks to continue GC2348 and compare Rule30 remembering/forgetting. **PROOF-SKETCH applications
of reviewed G50/G51**, independent carrying read pending; the referenced Rule30 observer correction
was carried by Local in L1143. Prediction and counterfactual were published as GC2349 at 6cd9f3bc.
No new generic conjugacy, novelty or nonexistence claim. This section separates a sufficient
summary of *fractional admissibility* from a sufficient state for *actual future prediction*.

### Full integer evolution does not merge distinct pasts

While the half condition holds, the whole numbers evolve by F(n)=ceil(3*n/2). Directly,

    F(2k)=3k,       F(2k+1)=3k+2.

Its image contains residues 0 and 2 modulo 3, never 1. On that image its unique inverse is

    n = 2m/3       when m=0 modulo 3,
    n = (2m-1)/3   when m=2 modulo 3.

Thus F is injective on nonnegative integers. A valid current integer has only one predecessor,
and at a specified elapsed time determines its whole earlier integer history. The full real
update xi -> 3*xi/2 is also injective. No claim that Rule30's full map is injective is being made.
The fractional map, or a summary of its remaining upper bound, is a different observation.

### Exact transport from an input binary residue to an output ternary residue

For an L-bit parity word w, let C_0=0 and C_(t+1)=3*C_t+w_t*2^t. G51 gives

    2^L*n_L = 3^L*n_0 + C_L.

Let R be its least compatible input residue modulo 2^L, and let
M=(3^L*R+C_L)/2^L. Then all nonnegative integer realizations of that word obey exactly

    n_0 = R + 2^L*k  <=>  n_L = M + 3^L*k,     k>=0.

Here 0<=M<3^L: use 0<=R<2^L and 0<=C_L<=3^L-2^L. In particular,

    M = 2^(-L)*C_L modulo 3^L.

Different L-bit words have different M. To recover the word from M modulo 3^L, its residue
modulo 3 determines the last parity (0 for output residue 0, 1 for residue 2). The inverse formula
above then determines the preceding integer modulo 3^(L-1); repeat. Changing the representative
M by a multiple of 3^L changes that predecessor by a multiple of 3^(L-1), so this reconstruction
is well-defined. Thus a fractional reset does not erase the preceding word from the actual
integer: it is encoded in a ternary residue. This is an elementary consequence of the known affine
coupling, not a claim that the history is stored as independent ternary digits without carries.

The quotient k remains important as well. Since 3^L is odd, the next integer parity is

    b_L = (M+k) modulo 2.

Keeping the residue M while forgetting the quotient can therefore change the next branch.
Two different admissible reset blocks of the same length illustrate history retention:

| 22-step gap block | C_L | R modulo 2^22 | M modulo 3^22 |
|---|---|---|---|
| 4,11,7 | 12550483683 | 217509 | 1627367841 |
| 5,5,5,7 | 12043134675 | 2907189 | 21751089894 |

Both finish in the ordinary fractional state of GC2348; their output history residues differ.
The first word is its critical 22-bit word; the second has all gaps at least 5 and is covered by
G294's stronger ceiling. The table's residues were checked by exact GP modular arithmetic.

### An exact same-observation, different-future witness

For any L, two real starts differing by 2^L have differences

    x'_t-x_t = 3^t*2^(L-t)    for 0<=t<=L.

These are integers throughout, so their fractional histories are exactly identical through L.
For t<L the difference is even, so the integer parities also agree. At t=L it is odd, so the
parities are opposite. If the shared fraction u_L is in [0,1/2), exactly one of the two next
steps passes the half condition: the even integer requires u_L<1/3, and the odd integer requires
u_L>=1/3. This is a fixed family of exact pairs, not an assumed random missing bit.

Specialize to the actual reset in GC2348. With

    A = 12550483683/31376865305,
    x_0 = 217509+A,
    x'_0 = 4411813+A = x_0+2^22,

both fractional histories stay below 2/5 through time 22, with identical values and identical
parity word at times 0..21. At time 22 the whole numbers are 1627367841 and 33008427450,
respectively odd and even, and their common fraction is A. At time 23:

    frac(x_23)  = 3137292872/31376865305 = 0.099987453861430...,
    frac(x'_23) = 37651451049/62753730610 = 0.599987453861430... .

One survives this next step and the other breaches the half. No infinite survival is asserted.
Direct exact-rational multiplication and floor extraction independently replayed these finite
histories. The difference at time 22 is 3^22=31381059609, as predicted before the check.
This refutes predictive closure from even the complete finite fractional history, and therefore
also from the three-state fractional summary, over this class of varying positive starts.
It is not an ambiguity for a specified exact starting number.

### The connection to Rule30: information omitted by the observer

In the reviewed [GC2028/L1143 Rule30 analysis](reports/rule30-exact-strip-knowledge.md#locals-carrying-read-l1143-29-october-2026),
initial cells a10 give F^2(x)_2=a despite arbitrary exterior bits. The relevant intermediate
expressions include NOT r and r OR s. Each can be unknown individually, yet their OR is always 1.
Replacing them by independent unknowns loses their shared dependence and misses the returned bit.
That was a representation error, not evidence that the true system destroyed the relation.
The result is about all specified completions of a patch; it is not a randomness theorem for
the one fixed single-seed orbit.

The analogous Mahler omission is the coupling between fractional branch, integer residue and
quotient. The three-state grammar correctly says which fractional continuations are allowed;
it does not say which one the actual integer will select. Both systems warn us to retain the
relation that carries a future constraint. The two mechanisms are not claimed identical: the
Mahler whole-number map is injective, whereas the cited Rule30 theorem concerns a local observer.

### What this changes in the research question

G51 already makes every finite admissible prefix realizable by some positive integer. Searching
for a new finite fractional word forbidden solely by ordinary-integer existence, while allowing
arbitrarily large starts, cannot close the gap. The obstruction must retain a single fixed start
(or an explicitly bounded set of starts) across arbitrarily long prefixes.

For a chosen fractional word, let R_L be its least input residue. Successive extensions give
R_(L+1)=R_L+epsilon_L*2^L with epsilon_L in {0,1}. A fixed positive integer realizes the word
exactly when these residues eventually stabilize at that integer (G51). More explicitly,

    n_0 = R_L + 2^L*k_L,
    epsilon_L = (b_L-M_L) modulo 2,
    k_(L+1) = (k_L-epsilon_L)/2.

For a fixed n_0 this is its actual binary quotient, which eventually becomes zero. That does not
force a fractional failure: the subsequent branches are determined by M_L and still have to be
analyzed. It forbids treating new seed bits as an independent, inexhaustible supply of choices.
The three-state plateau makes the fractional part finite-memory; it does not by itself prove
that every nonzero compatible residue path must keep lifting. This is the remaining inference.

Search/controls: G50/G51/G294, GC2348, the full GC2028/L1143 carrying source, record searches for
Mahler injectivity/forgetting/residue history, and current Coon source matches for residue and
orbit identities. Relevant literature is the classical integer/beta decomposition (Flatto 1992;
Flatto–Lagarias–Pollington 1995), already credited in this record. No new source theorem is
needed for the elementary affine corollaries here. No full portal refresh, build or novelty claim.
Only the frozen pair and the two named block residues were evaluated in GP; no random samples,
horizon enlargement, solver job or worker delegation. Exact computations are self-checks.

**Next executable step:** retain (fractional state,R_L,M_L) under one of the three permitted
blocks and ask for a provable obstruction to eventual zero lifts, comparing existing stabilization
and two-sided residue constraints first. Do not call state merging or fractional reset a decrease
of arithmetic memory. **Independent alternative:** the exact four-odd continuation constraints
above GC2348's upper endpoint B. If the next block merely restates unbounded-residue necessity
without a new bound, park the stabilization route and take that alternative. Both schedules paused.

## Just above B: first feasibility versus full continuation reset (GC2471)

The independent4,11,6 continuation lead now has a [complete hand application](reports/GPT-MAHLER-POST-B-BOUNDARY-20261103.md), PROVED hand/two-party L1383. Put r=2/3 and B=12552580835/31381059609. For B<a≤T4, define

`T_f=B+r^(21+f)/3`, `S_f=B/(1−r^(21+f))`, f≥5.

The finite five-one word at gaps4,11,6,f enters iff a>T_f. The same prefix accepts every already-a-admissible continuation beginning with a one iff a≥S_f. The necessity proof constructs a finite-repeat counterexample instead of assuming tail values approach a. Strict periodic equality at S_f remains excluded. The first possible next gap grows without bound as a↓B; release of the inherited fractional restriction requires at most one additional waiting step. No ordinary-integer survivor or loss of arithmetic history is asserted.

The feasibility widths have ratio2/3 exactly. The full-reset widths have ratio `(2/3)(1−q_f)/(1−(4/9)q_f)<2/3`, tending to2/3. Exact GP substitutions and a concrete two-block counterexample are self-checks, not a carrying read.

**Current source refresh:** Coon main is b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe,93files changed sincebd92eb1. Targeted statement/proof comparison finds `subCeiling_survival_rung_unique_and_trichotomy` already supplies the generic geometric recovery principle; it is credited as known. AperiodicSlackCocycle is unchanged at hashb230c1a2. The full new library and kernel builds have not been reviewed here. The particular variable-ceiling prefix/strict-endpoint dictionary stays separate from that generic prior art.

Next executable step: carry the constructive full-reset necessity and endpoint treatment, then test the CONJECTURE that each `(S_f,T_(f−1)]`, f≥5, is a complete finite-memory plateau with gap rules≥4,4→≥11,4,11→≥6,4,11,6→≥f. Use the four exhaustive first-block cases and forbidden costs; overlap/equality cases are the cheap objection. The prefix theorem alone does not establish this. Compare the exact integer-slack hypotheses before treating a general principle as additional. Do not rerun integer-residue stabilization without a new bound or start a threshold grid/census. Independent alternative: a genuinely new Rule30 relational lemma from Local. The current overnight programme/schedules are ACTIVE by the2November owner restart; older paused checkpoints above are historical.

## An infinite family of complete plateaus accumulating at B (GC2473)

The conjecture above now has a [full hand proof](reports/GPT-MAHLER-PLATEAU-CASCADE-20261103.md#completed-argument--gc2473), PROVED hand/two-party L1384. For every f≥5, the formal language is exactly the four gap rules of L_f throughout `(S_f,T_(f−1)]`. Four forbidden costs give necessity; four first-block affine bounds give supremum S_f. Periodic lower/finite upper witnesses establish maximality and strict endpoints. Ordinary-integer criteria include the lower endpoint by G51's periodic obstruction, with no existence or integer-maximality assertion.

The gap reader has four states, while a binary reader needs a bounded waiting counter; an explicit nonminimal list has f+17 forbidden binaryblocks, all lengths≤21+f. No uniform memory bound independent of f, and no finite-state predictor of an actual integer's next gap, is claimed.

The fixed-code right limit is exact: intersection of all L_f equals the old three-rule language plus words with a unique terminal4,11,6 and no further ones. It is exactly the closed-ceiling condition allU_j≤B. Strict ceilingB removes those terminal extras; positive-integer parity codes cannot have finitely many ones. This does not exchange “one fixed integer for all f” with “a possibly different integer for each f.”

Next executable step: read the carrying response, then examine the transition interval at the exact midpoint a=(T5+S5)/2. Before proposing a count-only reset model, compare finite words with gaps4,11,6,5,5 and4,11,6,5,7 via the exact inherited cap; they have the same number of short critical blocks. This is a specified hand control, not a threshold grid. Independent alternative: an actual new relational lemma from Local's Rule30 work.


## Complete plateaus inside the transition intervals (GC2475)

[Five-case hand proof and exact midpoint control](reports/GPT-MAHLER-NESTED-PLATEAUS-20261103.md),
PROVED hand/two-party L1385. The two finite gap words (4,11,6,5,5) and (4,11,6,5,7) have one
critical block each, yet respectively fail and pass at (T_5+S_5)/2. The continuation's value matters;
this does not prove that a finite observer is impossible.

For every f≥5 and h≥5, add to L_f the rule “after 4,11,6,f, next gap≥h.” Its complete formal language
is unchanged on `(R_(f,h), V_(f,h−1)]`, where R=T_f/(1−r^(21+f+h)) and V=T_f+r^(21+f+h)/3.
Five exhaustive first blocks and explicit finite/periodic witnesses prove the assertion by hand.
For each f, infinitely many such intervals lie inside (T_f,S_f) and accumulate at T_f. The h=5
edge works; h=4 is a failed control because the proposed repeated word joins two forbidden gaps 4.
The fixed-code right limit is L_(f+1) plus specified terminal words; positive-integer codes exclude
those. No integer survivor, whole-transition classification, novelty or Lean check is asserted.
GC2473 is independently carried by L1384, whose full proof/source/output were read.

Next executable step: carry the new five-case step and test a guarded general refinement lemma,
including competitor bounds and overlap conditions. Retain the separate curiosity lead in INSTINCT:
can reflection into the endpoint-correct lazy beta map make the lower-hole literature applicable?
No theorem transfers before that dictionary and its endpoint exceptions are proved.


## An exact upper-ceiling to lower-map dictionary, with an applicability guard (GC2476)

[Hand dictionary and primary-source scope](reports/GPT-MAHLER-LAZY-DICTIONARY-20261103.md), mathematical dictionary/arithmetic PROVED hand/two-party L1386; source-range reading attributed to GPT,
specializes known beta reflection: x=2U follows the greedy map G at beta=3/2; y=1−x follows the lower
map L=T^-_(3/2,1/2) on (0,1]. The branch at y=1/3 maps to 1, and L(1)=1. All U_j<a is exactly
all L^j(y)>1−2a. It is a strict lower threshold, not a closed-survivor condition. Integer compatibility
is still separate; complemented parity histories of positive n correspond to negative −1−n.

Langeveld–Samuel v1's exact definitions and printed Corollary 2.7 were inspected. At this lazy endpoint,
the lower itinerary of 1 is 1 forever, so the named greedy-base conversion requires beta'=2 rather
than a value in its printed (1,2). This blocks an unqualified invocation, not every possible theorem
transfer. The final journal treatment and later construction remain to be audited. The nested GC2475
family is separately carried by L1385, whose complete proof/source/output were read.


## Direct strict-hole doubling code, without dropping endpoint words (GC2479)

[Complete hand construction](reports/GPT-MAHLER-DOUBLING-CODE-20261103.md), PROVED hand/two-party L1388.
For every 0<a<1/2, let kappa(a) be the greedy beta=3/2 word of X=2a and theta(a) its complemented
binary value. The formal all-tail ceiling language is exactly the shifted lexicographic bound
sigma^j(b)<kappa(a). A first-difference supremum proof establishes this even for initially arbitrary
binary words, so no unproved greedy-code assumption is used.

Complemented binary evaluation gives an exact time-preserving conjugacy to the LOWER doubling map
on (0,1], with every iterate strictly greater than theta. For the usual doubling map on [0,1), it
is exactly the infinite-one part of the original language. The lost lower-map points are precisely
surviving dyadics, corresponding to finite-one words. Positive integer parity codes have infinitely
many ones, so their endpoint discrepancy disappears, while their integer-residue compatibility
condition remains fully in force. Quantitative first-difference separation proves continuity both
ways; no distance, measure, dimension or integer-existence equality is asserted.

GC2476's map/sign/arithmetic claims are carried L1386; the version-specific source-range reading
remains GPT's lookup. The direct construction bypasses that corollary, without claiming a corrected
journal theorem. Next match one precise doubling-hole result to this strict convention. The specific
Lyndon-word interval candidate and its parameter-map caveat are retained in INSTINCT.


## A guarded word constructor for complete bands (GC2481)

[Strict word-interval proof and general constructor](reports/GPT-MAHLER-LYNDON-CONSTRUCTOR-20261103.md),
mathematics PROVED hand/two-party L1389; primary-source comparison attributed to GPT, known Lyndon-interval mechanism specialized here. For any cyclic gap
list (d,g2,...,gm) with m≥2,d≥3, and all other gaps≥d+1, root at the uniquely shortest gap and
form its period word w of length L. Set A=(1/3)sum of r^p at its one positions, r=2/3;
S=A/(1−r^L), T=A+r^(L−1)/3. Then (S,T] is an exact maximal formal ceiling plateau.
The language is every shifted word≤w forever repeated. For each zero position j of w, forbidding
its prefix through j−1 followed by1 compiles it into L−m local blocks of length≤L.

The complemented word satisfies the actual finite-suffix Lyndon test. Its finite/periodic binary
interval is exactly Baker–Kong Definition1.2 at beta2. A direct strict-hole proof supplies the
needed endpoints/maximality; no non-strict or beta<2 lemma is silently imported. The map theta's
inverse image gives (S,T] without any image-surjectivity assumption. Both prior families are cases.
The same w has the exact G51 finite coupling window [A,T), with S inside it. The sample (3,4)
has S=945/2059,T=1009/2187; the latter is already in G296's finite table, not a new rational.
No ordinary-integer survivor or coverage of all ceilings follows.

GC2479 is now independently carried L1388; its finite truncation-decision guards were checked
without repeating the random test. Next carry the general constructor, then test one explicit
repeated-shortest-gap word using the suffix predicate rather than an automatic parameter scan.


## Repeated minimum gaps, two extra constraints and a uniform width law (GC2483)

[Complete hand argument](reports/GPT-MAHLER-REPEATED-GAPS-20261103.md), PROOF-SKETCH awaiting carry.
The constructor needs the actual complemented-word strict suffix predicate, not a unique minimum.
All cyclic gaps≥3 suffice for the boundary guard: the upper finite word can have one terminal gap2,
whose tail is at most13/27<1/2. Suffix order puts that finite root at its maximum. The same (S,T]
language/finite compiler and G51 window [A,T) follow, including G294's cases with a single 1 per period.

For the queued gaps (4,11,6,5,4,11,7,5), L=53 and one positions0,4,15,21,26,30,41,48. The second4's
suffix is decided by6 versus7 at relative index21. Its band lies strictly between V_(5,4) and S_5.
The exact language is L_5 plus exclusions of gap words (4,11,6,5,4,11,6) and (4,11,6,5,4,11,7,4).
No single next-gap threshold after (4,11,6,5) describes it: allowing4 admits the old inadmissible
critical repeat; forbidding4 excludes the new admissible period. Finite earlier context must persist.

The exact ratio (T−S)/(T−A)=1−2S lies in [1/19,1/3), giving uniform geometric width bounds over
this constructor class. This is a same-word window comparison, not spacing or frequency information.
GC2481 mathematics independently carried L1389. Next consider the set of ceilings where the
language actually changes, with an explicit discontinuity-safe criterion and a word-cover bound;
no further band enumeration is authorized by this observation alone.

## Where threshold changes live, and finite certificates of a flat interval (GC2485)

[Complete hand proof](reports/GPT-MAHLER-THRESHOLD-SET-20261103.md), PROVED hand/two-party L1392, including GC2487's correction.
For C_a the strict formal all-tail language, E consists of a for which every increase changes C_a.
For every0<a<1/2, the exact criterion is every greedy G^j(2a)≤2a. A first upward violation cannot
have passed through the cut2/3, which maps to0 forever. Its finite affine itinerary consequently
certifies a two-sided flat neighborhood. Thus E is relatively closed and is exactly the failure
set of local constancy. The weak inequality and the map's cut are both retained.

Below beta_g=(1+(2/3)^(g−1))/3, g≥3, threshold codes in E have all one-gaps≥g. Their prefix counts
satisfy N_n=N_(n−1)+N_(n−g). If lambda_g^g=lambda_g^(g−1)+1, then1<lambda_g<3/2, and a direct
cover of the REAL parameter gives dim_H E≤log(lambda_g)/log(3/2)<1 in this range, hence zero
ordinary length. In particular local constancy holds on an open dense set of full length below13/27.
No measure is transported through theta; G293's 2-adic dimension concerns a different object.

The supremum of all tails of any nonzero formal history, when below1/2, lies in E, even when it
is never attained. Every E value conversely occurs as such a supremum. GC2487 corrects an initial
scope error: compactness and positive tail weights EXCLUDE terminating maxima for infinite-one
histories below1/2. Periodic maximizing limits remain possible for nonperiodic formal histories.
No integer survivor, orbit frequency or new residue bound follows. Exact cut/flat/outer-endpoint
controls are in the report. Known bifurcation/covering methods reproved with these conventions.
Next classify terminating threshold codes via the last-bit suffix guard, rather than enumerate bands.

## One-sided endpoints and exactly which formal maxima remain (GC2490)

[Complete hand argument](reports/GPT-MAHLER-ONE-SIDED-ENDPOINTS-20261103.md), mathematics carried L1394; global nowhere-density corollary carried L1395.
For ALL0<a<1/2, a point of E is isolated from the LEFT exactly when its threshold code terminates.
A finite cut hit gives a one-sided escape shell and a left flat interval. For a nonterminating code,
the maximum m_n over all tails of its n-digit truncation is terminating/inE, strictly belowa, and
increases toa. Terminating points are countable/dense inE and also approached from the right;
E has no isolated points. No arbitrary prefix is assumed rooted at its maximum.
Density of terminating points and their left isolation also make E nowhere dense throughout
(0,1/2), so flat neighborhoods are dense in that full range. Zero ordinary length is still only
established below13/27; topology is not substituted for a measure proof.

Below13/27, lowering the terminal1 gives the actual strict suffix predicate, even when the old
suffix equals its prefix. Wrap gap≥4 and T_w=a recover an exact(S_w,a] plateau; u=1 is separate.
More generally prefix blocks separated by K_n zeros, with r^(K_n+1)<a−m_n and K_n≥n, construct
a non-eventually-periodic word with every tail STRICTLY<a and unattained supremuma. Consequently
possible sub-half maxima of non-eventually-periodic FORMAL histories are exactly the nonterminating
threshold points of E, equivalently its left-accumulation points. This is not G51 integer realization.
GC2485/2487 mathematics now independently carried L1392, full proof/source/output read.
Next right-side isolation versus pure periodicity, with a counterexample or exact proof before scans.

## Complete formal plateau classification and right-isolated thresholds (GC2494)

[Full hand proof](reports/GPT-MAHLER-COMPLETE-PLATEAUS-20261103.md), mathematics PROVED hand/two-party L1397; primary-source comparisons attributed to GPT.
A self-maximal binary word with sub-half root is proper greedy by an exact first-difference
supremum contradiction. Thus the full word class needs only the strict suffix predicate and
S_w<1/2, with no gap3 assumption. Its exact band is(S_w,T_w], languageH_w, and G51 finite window
[A_w,T_w). Terminating threshold maxima approach1/2 via the known critical expansion; every flat
component therefore has a terminating right endpoint, whose last-bit reduction supplies its
periodic left endpoint. This classifies ALL nondegenerate formal plateaus on(0,1/2), with the
zero-language interval separate. Right isolation inE is exactly PURE periodicity, not eventual
periodicity. The earlier word families are sufficient subfamilies of this full class.

For non-eventually-periodic FORMAL histories the maximal bands are[S_w,T_w], since equality at
the lower boundary would force an eventual periodic tail. Actual positive-integer codes inherit
the same finite criterion there, but formal witnesses do not prove integer maximality/existence.
The same-word width ratio1−2S has infimum0 over the full class, not the gap3-class bound1/19.
The gap2 example9477/19171 is already known in the two-ladder discussion, recovered as a control.
Pointwise Mahler survival can still have supremum1/2 and is outside uniform sub-half ceilings.
Next audit a primary ergodicity/positive invariant-density theorem for G_(3/2) before extending
zero ordinary length to the full parameter range; no measure transfer through theta or scan.

## Global zero length and an exact total-width identity (GC2496)

[Primary-source audit and invariant-set proof](reports/GPT-MAHLER-GLOBAL-NULLITY-20261103.md), mathematics PROVED hand/two-party L1398; primary-source reading GPT-only.
Brown–Yin1999's actual greedy map/domain, ergodic invariant probability and Parry density match
G_(3/2). The density bounds1/3≤rho≤3 check equivalence to ordinary length in the needed direction.
For each rationalq<1, eventual confinement belowq is an exactly invariant union of nested
preimages, with measure<1; ergodicity makes it null. Every doubled E threshold belongs to one
of these countably many sets. Thus E has zero ordinary length on ALL(0,1/2), not just below13/27.
No nonlinear theta measure transport or orbit sampling is used.

Combining the carried complete plateau classification gives the exact sum over the full word
classW: sum(T_w−S_w)=1/6, since the bottom zero-language interval contributes1/3 of the total1/2.
This is parameter width, not integer-orbit frequency. No global dimension bound<1, integer
exclusion, or conclusion for pointwise Mahler histories with sup=1/2 follows. Next explicit
compact-range dimension cover via a periodic dominating word/Parry base, with direct metric
and prefix-count checks; existing G50 moving-age height applied to padding is the alternative.

## Compact-range dimension from direct word counts (GC2498)

[Complete direct count and parameter cover](reports/GPT-MAHLER-COMPACT-DIMENSION-20261103.md), mathematics PROVED hand/two-party L1401; primary reading GPT-only.
For every full-class word w, let gamma solve sum_(j>=1)(w∞)_j gamma^-j=1; then1<gamma<3/2.
First difference gives actual prefix counts gamma^n≤N_n≤gamma^(n+L), with the lower count
separately using the root1 critical-tail guard. The ORIGINAL r^n cover yields
dim_H(E∩(0,T_w])≤log(gamma)/log(3/2)<1, adding the finite upper endpoint as one singleton.
Cofinal S_w supply such a bound below every fixed A<1/2; no dimension transport or global
dimension1 claim. The gap comparison (gamma−1)^2(1−2S)≤3/2−gamma≤(9/4)(1−2S) connects the
known width ratio to these upper exponents. Exact rate of H_w is not a lower bound for E.
GC2496 nullity/total width1/6 adopted PROVED hand/two-party L1398; source audit GPT-only.
Next the EXISTING G50 moving-age height filter on NEW separated blocks, distinguishing oversized
from near-minimal safe padding; no duplicate of Local's record-law test or A1 maintainer wait.

## Band words, escape time and compact finite means (GC2500/2501)

Local L1400's infinite waiting-time mean is CARRIED with the backward-record monotonicity
repair; forward suffix counts agree in LAW and expectation, not pathwise monotonicity. New
PROOF-SKETCH: tau(2a)=|w| on OPEN(S,T), infinity at BOTH endpoints. Hence exact tail widths
Leb_X{tau>n}=2sum_(|w|>n)(T−S) and divergent weighted length sum, pending identitycarry.
Zero-extending finite survivors' firstn digits puts them inH_w, giving ACTUAL
Leb_X{X≤2S,tau>n}≤gamma^L*(gamma/beta)^n. Every fixed compact range has finite mean;
global infinite mean is concentrated near1. Moving cutoffs1−60/n need new constant control.
No c/n constant, fixed-L derivative asymptotic, integer consequence or duplicate experiment.

GC2503 adoption: L1403 complete carrying argument read; GC2500/2501 mathematics PROVED hand/two-party, including endpoint exceptions, exact tail identity, infinite weighted length and finite compact means. L1404 full scan source/output read as M5 measurements; no Intel rerun or cap-receipt audit. Its log-periodic prediction is refuted on the sampled range, c/n remains conjectural. New near-minimal G50 padding control is retained in INSTINCT, still a sketch.

## Padded histories test the arithmetic filters without realizing an integer (GC2505)

[Complete hand control and exact source comparison](reports/GPT-MAHLER-PADDING-ARITHMETIC-20261103.md), mathematics PROVED hand/two-party L1407; source comparison GPT-only.
B=concat(100)^k0^(3k+1) is least-safe only for the genericfuture≤1 bound. SharperD=concat(100)^k0
already has everytail<9/19, unattainedsup9/19, and isaperiodic. Bothpass the knownzero-run
heighttest withfixed budget6. Exact firstrepeat SECONDorigins in gapcoordinates arequadratic:
R_L(B)=(L+1)(L+2)/2; R_L(D)=h(h+1)/2+1,h=ceil(L/2). Thuscurrent Coon linear-origin
complexity theorem's premise fails, althoughmean gaps exist6/3. CappednormalizedminSlack
isidentically1 for ALLgaps≥3, so hasno distinctionbetween thesehistories orpure100. Specific
ratio/squeeze andrapidgrowth hypothesesfail; not a whole-library no-exclusion claim.
ForD a hypotheticalfullinteger realization obeys2^(3k+4)v_(k+1)=3^(3k+1)v_k−1, k≥2, with
positiveoddv_k coprime3. Known clock/coupling specialization, not an infinite solution or
newexclusion. Nextmatchfullpacketquotient to existingarithmetic identities; no newcensus.

GC2506 [anchored packet reformulation](reports/GPT-MAHLER-PADDING-ARITHMETIC-20261103.md#7a-gc2506-match-the-existing-quotient-and-retain-the-initial-anchor), mathematics PROVED hand/two-party L1407.
The packetvariable is an affine rescaling ofcurrentCoon's ordinary oddquotient, not new
stateinformation. Retain v_2=49+342t and n_1=293+2048t,t≥0. Anchored positiveodd recurrence
isexactly Drealization byG51/clock induction, notexistence/exclusion. Seed293matches11digits
andfailsnext; ξ293+U0(D) firstbreacheshalfattime12. Summaryroutesparked pendinganewrelation.

## Explicit bounds for the earlier sampling-window omissions (GC2507)

[Six-case hand argument](reports/GPT-MAHLER-WINDOW-OMISSION-20261103.md), PROVED hand/two-party L1409.
GC2501 extends to2T_w forn≥L becauseeveryopenbandstateescapesatL. Fiveselectedknownbands
and rationalgamma bounds yield actual n-scaledomission ceilings0.004,0.001,0.008,0.00005,
2e−12,0.005 atthe sixoldR1times100…3200. Same-workerGP sixrationalcomparisonsallpass,
notindependentreview. Theseboundnominalcontinuouspopulation omissions, notsamplingerror.
No general movingcutoff/c/n/constant theorem or newalgorithm.

## From the kit back to Mahler: the first check, a barrier and a planted survivor (Cloud, CL781 and CL782, 11 November)

**Status:** hand statements PROOF-SKETCH (Cloud, awaiting GPT's read), each replayed exhaustively on its range;
shares MEASURED to w = 26. [Report](reports/CLOUD-KIT-TO-MAHLER-20261111.md). The owner reopened this room on 11 November to carry the kit's
newer Rule 30 methods back.

Since 31 October the kit writes Rule 30's period 2 as an integer iteration, F(Y) = (Y >> 1) xor (Y or 2Y)
(`Q01_iff_integer`), the same shape as T(n) = n + ceil(n/2), and has many theorems about it. Three now have
Mahler twins.

- *The first parity past the free bits* (twin of `Rule30FirstChecks`). With chi_w(n) = T^w(n) mod 2 for
  n < 2^w: chi_w(2^w - 1 - n) = chi_w(n); chi_w(n) = chi_(w-1)(r) xor (q mod 2) for T(n) = q 2^(w-1) + r,
  so the check differs from the shifted word's exactly when T(n) is in the middle third; T^w(n) is the least
  residue of C 2^(-w) modulo 3^w; at least A(w+1) - A(w) of the valid n pass; and the two extensions of a
  word p differ in their checks by chi_(w-1)(p) xor [w even]. Measured: the share of valid n < 2^w that pass
  is 0.742 to 0.759 for 16 <= w <= 26, and the next check the same. A proved two-sided bound is open.
- *No descent through a finite-state statistic* (twin of `Rule30RecognizableBarrier`). No function of the bit
  length, a finite-monoid image of the binary digits and bounded windows at both ends, into a well-founded
  order, falls at every valid step. Witnesses: the truncations (4^L - 1)/3 of the stripe -1/3, whose orbits
  are 3^j 2^(2L-1-j). With GC2342's recharge family for valuation clocks, both known kinds of local clock are
  now defeated by explicit families.
- *A planted survivor* (twin of `Rule30PlantedSurvivor`). A conjugate of T by a tree automorphism that moves
  one residue class modulo 4^L has an immortal positive integer and T's survival counts, plus one beyond an
  explicit threshold.

Nothing here touches Mahler's conjecture. Open next: the two-sided bound; a sharp linear law between horizon
and size (the twin of the kit's Conjecture S); whether long survivors lie on rays from -1/3 and -9/19.

## The first check is balanced on both sides (Local, L1667 and L1668, 12 November)

**Status:** hand arguments PROOF-SKETCH (Local, awaiting a carrying read); finite tables COMPUTED, exact, and
replayed in Wolfram at the smaller sizes. [Report](reports/LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md).

- *The arc statement.* Write a word as p″s, with the prefix of length l. The starts r″ + 2^l t, t < 2^k, have
  continuations equal to the parity words of x″ + 3^l t, x″ = T^l(r″). So the number of them whose continuation
  lies in a set W of words of length K is the number of points of 3^(-l) N_K(W) in an arc of 2^k consecutive
  residues of Z/2^K. The prefix is a rotation and a multiplier.
- *Theorem A.* With B_m the valid words of length m that cannot take a 1, D_m those with forced parity 1, and
  F the count of full words: F(m - 7) <= D_m <= B_m - F(m - 7) for m >= 7, and 1/27 <= D_m/B_m <= 26/27 for
  every m >= 3. The certificate is 14 points in Z/256 with every cyclic gap at most 121, for the 64 powers of 3.
- *Theorem B, GC2936's lemma.* |R_m| >= F(m - 6) for m >= 6: four points in Z/16, by hand.
- *Larger tables.* D_m/B_m is eventually in [0.2228, 0.7772]; the share of valid starts passing the first
  check is eventually in [0.611, 0.889] (measured 0.75); at most 0.823 pass two checks and 0.701 pass three.
  Over all n < 2^w the check has share in [0.415, 0.585] for every w >= 15.
- *Limits.* Some arc always holds a survivor, so the method gives no extinction and no exponent below
  Flatto's. The certified constants converge slowly; four predictions that assumed random-like worst
  rotations were refuted. The limit 1/2 is open.

## The unconditional first check tends to 1/2 (Local, L1669, 12 November)

**Status:** Theorem C PROOF-SKETCH (Local, awaiting a carrying read; each step checked numerically); explicit
constants COMPUTED; the valid-word limit OPEN. [Report](reports/LOCAL-MAHLER-FIRST-CHECK-LIMIT-20261112.md).

- *The product.* With M = 2^(w+1) and Y_w = {n mod M : T^w(n) odd}, the transform of Y_w at h has modulus
  2^w rho_w(h 3^(-w)), where rho_w(n) is the product over u < w of |cos(pi n 3^u / 2^(u+2))|.
- *Theorem C.* |O_w/2^w - 1/2| <= rho*_w (1 + ln(H)/2) + 1/sqrt(2(H - 1)) for every H >= 2, with rho*_w the
  largest rho_w over odd n. Two consecutive angles below 1/5 grow by exactly 3/2, and no angle is below
  2^-(u+2), so rho*_w <= cos(pi/5)^N(w) with N(w) >= log_2.71(w) - 2. Hence O_w/2^w -> 1/2, and the same for
  the continuations of every prefix.
- *Explicit.* rho*_64 = 0.002425, rho*_72 = 0.001174, rho*_80 = 0.000593 by exhaustive pruned search, so the
  share is within 0.0187, 0.0099 and 0.0054 of 1/2 from w = 64, 72 and 80.
- *Valid words.* D_m/B_m -> 1/2 would follow from one lemma: the sum over boundary words, with a phase on
  each 1, is at most C B_m lambda^NS, NS the number of non-small angles. For all words that is the product
  itself. A table at m = 12 to 18 agrees with the shape; no proof.

## The valid starts are equidistributed (Local, L1670, 12 November)

**Status, updated GC2940:** Theorem V, Propositions G and M and corollaries V1 to V3 PROVED hand/two-party
(Local and GPT); tables retain their COMPUTED or MEASURED scope.
[Report](reports/LOCAL-MAHLER-VALID-STARTS-20261112.md).

- *Free bits (Lemma T).* A bit that follows a full prefix and is followed by 00 can be flipped: z000 and z100 are
  both full. With sites restricted to a 3-separated set U, the flips act freely and keep the sites, so the sum
  over valid words of e(sum q_i alpha_i) is at most the sum over words of the product of |cos(pi alpha_i)| over
  their sites.
- *Renewal inequality (Lemma R).* The sum over full words z of length t of lambda^(sites of z in U) is at most
  mu^|U| F(t), with lambda = cos(pi/5), mu = 1 - 2(1 - lambda)/K and K < 72.8. The sharp series constant is
  13.37 (COMPUTED for r <= 400); the weakest contraction seen is 0.958 a site (t = 7), near 0.95 for t >= 10.
- *One frequency (Proposition G).* With the run lemma of L1669 (more than log_2.71((w - a)/0.85) non-small
  angles at valuation a): gamma_w(h) <= 6.23 (0.85/(w - a))^delta, delta = 0.00176.
- *Theorem V.* By the Erdős–Turán inequality the discrepancy over intervals of V_w = {n < 2^w : valid word of
  length w} is at most 6/(w + 1) + 8(1 + ln w)(0.85/(w - log_2 w))^delta. It tends to 0.
- *Corollaries.* V1: D_m/B_m -> 1/2. V2: the share of valid starts below 2^m that pass j more checks tends to
  (3/4)^j. V3: at most 450 x^theta/(log_2 x)^c Z-numbers below x, theta = log_2(3/2), c = 0.0007.
- *Proposition M and the wall.* #{n < 2^m valid for m + j steps} <= (pi^2/4) A(m+j) 2^-j (1 + sum over
  0 < |h| < 2^j of gamma). A bounded sum for j = eps m would lower the exponent by 0.415 eps. Measured, the sum
  is about 0.5 * 2^j/sqrt(A); proved, each term is only a power of log. This is the 2-against-3 wall with a
  number on it.
- *Measured.* Discrepancy 0.046, 0.019, 0.011, 0.0046, 0.00074, 0.00008 at w = 12, 16, 20, 24, 32, 40, about
  0.6/sqrt(A(w)); D_m/B_m = 0.49996 at m = 36; pass shares within 0.0007 of (3/4)^j at m = 32.
- *Refuted (S1).* The low spectrum is not flat: the mean of A gamma^2 over odd low frequencies is about 0.3.
  The valid starts are more even than random points at coarse scales.
