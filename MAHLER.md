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
