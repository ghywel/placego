#!/usr/bin/env python3
"""rule30_audit_g99_g100.py: Local's second reading of GPT's G99 (versioned dependency evaluation preserves logical
time) and G100 (fair rows do not make rightward flips independent in time), independent of GPT's VP1 and RF1. Exact
enumeration. (Local, 2026-10-06; PROOFS.md notes; chat.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g99_g100.py      (seconds)

CHECKS (GPT's claims at 827e006):
  S1 (G99): for N = 1..5 and every initial word on [-N, N], evaluating the triangle's nodes in three different ready
     orders (by generation, by largest site first, and a seeded random ready order) gives every node its synchronous
     value; the mixed-generation projection after only node (0, 1) from a seed at 1 is {0, 1}, not {0, 1, 2}.
  S2 (G100): at the observer p_t = t, the flip words B_0 B_1 B_2 over all 128 seven-bit initial words have counts
     [1, 3, 5, 7, 3, 9, 7, 29] x 2 both from the moving-frame map H and from literal spacetime; marginals 3/4, adjacent
     covariance 0, lag-two covariance 1/32, count variance 5/8 (iid would be 9/16).
  S3 (G101, added 2026-10-06 at 7773c41): the observer p_t = floor(3t/4) over all 512 initial words on sites -1..7,
     literal spacetime: the four-flip histogram is 4 x [1, 3, 5, 7, 3, 9, 7, 29] for each first-flip value; means
     (1/2, 3/4, 3/4, 3/4); covariance 1/32 between the second and fourth flips and 0 for the other five pairs; count
     mean 11/4 and variance 7/8 (independent flips: 13/16).
  S4 (G092's scope point on L054, exact): from sites 0..3 = 0, 0, 0, 1 (zeros elsewhere), right races at site 1 then
     site 0 make site 0 differ from the synchronous value, while site 0's isolated right-race injection is 0.
  S5 (G102, added 2026-10-06 at 84d09c9): a forced race at site 0 of a fair row, neighbour race flags at sites 1..D
     (right) or -1..-D (left) with weights eps^k (1 - eps)^(D - k), the next site synchronous; by exact enumeration of
     every old word and flag word for D = 0..5 and eps = 0, 1/100, 1/4, 1/2, 1: right injection = Q_D / 4 with
     Q_0 = 1/2, Q_D = 1/2 + (eps/2) Q_(D-1), remainder (eps/2)^(D+1) / (4 (2 - eps)) to 1/(8 - 4 eps); left = 1/2.
  S6 (G103, added 2026-10-06 at 43095bf): on rings of 3 to 5 cells, T = 1, 2 steps, every initial row and every flag
     history, both race directions with races.c's conventions: every site whose dependency cone holds no flag agrees
     with the ideal history; with exact flag weights at eps = 1/4, 1/2, 1, every site's disagreement probability is at
     most 1 - (1 - eps)^M (M the deduplicated cone size) and at most eps t^2; the final-tick guard (ring of 5, black
     cell at 2, one right race at site 0 on step 1) makes site 1 differ on step 2.
  S7 (G104, added 2026-10-06 at 8753ab0): right-reading races: for block widths 1..5, every flag pattern and every
     three-bit tail, the old bits x_0..x_(w-1) map bijectively onto y_1..y_w. Left-reading races on a fair first row:
     density 1/2 and adjacent disagreement 1/2 (right cell unflagged) or 3/4 (flagged), so 1/2 + eps/4 with exact
     weights at eps = 0, 1/4, 1/2, 1 (chains anchored at depth <= 3).
  S8 (G105, added 2026-10-06 at f0f3a1b): on rings of 3 to 7 cells, every flag word in both scan directions (races.c's
     conventions, race_step above): the all-zero new row has exactly 2 old preimages under right races, and under left
     races 1 or 2 according to whether an effective flag is present; the exact masses 2^(1-W) and
     [1 + (1 - eps)^(W-1)] 2^(-W) at eps = 0, 1/4, 1/2, 1; the all-zero row stays zero under every flag word.
  S9 (G106, added 2026-10-06 at d05bb6b): right-reading races, old words on sites -2..D+2, flags on -1..D, site D+1
     synchronous, D = 0..4, exact weights at eps = 0, 1/4, 1/2, 1: the observer's flip x_0 XOR y_delta has mean 1/2
     for delta = -1, 0 and U_D for delta = +1, with U_0 = 3/4, U_D = 3/4 - eps/4 + (eps/2) U_(D-1), and the remainder
     to (3 - eps)/(4 - 2 eps) is [eps/(8 - 4 eps)] (eps/2)^D.
  S10 (G107, added 2026-10-06 at e779bd0): for T = 1..3, every nonincreasing path (increments -1 or 0) and every
     schedule switching whole rows between synchronous and right-reading-everywhere (a synchronous right terminal),
     over all initial words on sites -2T..T+1: the sampled vector (s_0..s_T) is uniform for every path and schedule,
     so the trace is iid fair conditional on the schedule, with fully correlated rows included.
  S11 (G108, added 2026-10-06 at 85f0972): for T = 1..3, every nonincreasing path and whole-row schedule, and every
     assignment of the non-pivot initial bits: the ideal and noisy traces are each bijective images of the T + 1 pivots,
     and the mask I_t XOR J_t is a function of the ideal prefix I_0..I_(t-1) alone (causal); the guard (old 1, 2 = 0, 1,
     only the target racing) gives E_1 = 1 - I_0 for all four pivot values.
  S12 (G109, added 2026-10-06 at f9aa008): (a) every background on sites -3..3 with site 0 flipped: the source error
     over ticks 0, 1, 2 is 1, 1 - z(1), z(1) OR z(2), and delta_1(-1) = 1 - z(-1), delta_1(1) = 1, computed by an
     XOR-difference propagation (the difference of the OR term), not the truth table; (b) every old word on sites
     -3..3 with one isolated right race at site 0 on tick 1: 16 injections, each with source signature 1, 0, 1 over
     ticks 1..3, the other 112 giving 0, 0, 0; second-tick damage sets {1} and {-1, 1}, 8 each.
  S13 (G110, added 2026-10-06 at f922142): the isolated pulse over all 128 words on -3..3: in each bin K_2 = (b, 0),
     8 words with E_1 = 1 and 56 with E_1 = 0; E_3 = E_1 always; both four-sample traces uniform (16 words, 8 each).
  S14 (G112, added 2026-10-06 at 38eda50): (a) white agreement after one right-reading step, at every site of every
     ring of 3 to 6 cells, every initial row and flag word: z_1(j+1) = y_1(j+1) = 0 implies z_1(j) = y_1(j); (b) the two
     nine-node cylinders on the line (initial words 0110000 and 0000010 on -3..3, flags as stated): ideal / raced source
     traces 1100..., B occurs with E_3 = 0, and 0011 / 0110 with I_2 = 1, E_2 = 0, E_3 = 1; (c) the left-scan guard on
     a ring of 5 (initial 00001, only site 1 flagged): site 2 white in both, site 1 different.
  S15 (G113, added 2026-10-06 at 832c0d3): the isolated pulse over all 8,192 words on sites -6..6, seven samples at
     site 0: A = {K_4 = K_5 = (0, 0)} has 1,872 words with 40 giving E_6 = 1; B = A and {K_3 = (0, 0)} has 896 with 0;
     the child K_3 = (0, 1) has 40 with 20; both seven-sample traces uniform (128 words, 64 each).
  S16 (G114, added 2026-10-06 at 9e09890): the expanded difference identity delta = p XOR (1-c) q XOR (1-b) r XOR q r
     against the truth table on all 64 triples; the cylinder 0011110010000 on -6..6 with the pulse gives ideal / noisy
     rows 1010101 / 1111011 (tick 3), 01010 / 00001 (tick 4), 101 / 001 (tick 5), incoming source errors (1, 1) at
     tick 4 and (1, 0) at tick 5; the black-centre guard (p = q = 0, r = 1) gives 0, not Rule 90's 1.
  S17 (G115, G116, added 2026-10-06 at 241fb49): over the 8,192 pulse words, the candidate X_5 = (F, K_4, K_5) with
     F = E_1: parent (1, (0,0), (0,0)) has 80 words with 40 next errors, its full-history child
     ((0,0),(0,1),(0,0),(0,1),(0,0),(0,0)) has 20 with none; 24 full-history children of 112 differ from their parent's
     rate (18 parents); adding only K_3 to X_5 splits nothing. And E_4 = F (I_1 XOR I_2 XOR I_3) on every word; on these
     8,192 words (16 times G116's 512) 1,024 injections, 512 fourth errors, each (I_2, I_3) bin 256 histories with 128
     errors (the first run compared with G116's unscaled 64, 32 and 16/8 and failed for that reason only).
  S18 (G117, added 2026-10-06 at 6c4792e): over the 2,048 pulse words on sites -5..5: the fifth error equals G117's
     formula in (I_1, I_2, I_3, I_4, D), D = x(3) (x(4) OR x(5)), on every injected word and is 0 otherwise; 256
     injections, 152 fifth errors; each injected ideal quadruple occurs 16 times, D = 1 in 6; the per-quadruple error
     counts have histogram {0: 2, 16: 6, 6: 6, 10: 2}; the all-zero quadruple has E_5 = D.
  S19 (G118, added 2026-10-06 at 8ced884): over the 2,048 pulse words, six samples each: both marginal traces 64 x 32;
     the joint histogram {32: 32, 24: 32, 8: 16, 5: 16, 3: 16}, 112 distinct pairs; each ideal trace beginning 0 has 8
     injections among 32, beginning 1 none; H(A, B) and MI(A; B) from the counts equal 6 + h2(1/4)/2 + h2(3/8)/16 and
     6 - h2(1/4)/2 - h2(3/8)/16 to 1e-12.
  S20 (G119, added 2026-10-06 at 439744b): on the 2,048 pulse words, for t = 0..5, the prefix mutual information M_t
     equals (t + 1) - sum_(s <= t) H(E_s | paired past), every quantity computed from exact counts; and the two toys:
     the positive control gives M = 1, 2 - h2(1/4), 3 - h2(1/4), the cross-copy reuse guard gives M = 1, 1, 3 while
     its last error is known from the paired past (so the identity would wrongly give 2 there).
  S21 (G120, added 2026-10-06 at 9f37d68): on the real pulse traces, H(E_t | paired past) <= 1/8 for t = 2..5 (the
     values are 0, 0, 0 and h2(3/8)/16); the positive toy's final error entropy is 1/8 (the bound tight), and the hidden
     event guard's is h2(1/8)/2 > 1/8 while its prefix information still obeys G119's identity.
  S22 (G121, G122, added 2026-10-06 at 65e0261): every finite word of span w grows to span w + 2 (w <= 14); images of
     distinct words are distinct; for w = 4..16 exactly 2^(w-4) of the 2^(w-2) normalized span-w words have a finite
     predecessor (three quarters are roots), and 101 is a root at w = 3; the canonical right-quiescent predecessor of
     the single black cell has an all-black left tail, and its own predecessor a left tail of period 3 with bits 001
     up to phase; applying Rule 30 to each returns the row it came from.
  S23 (G123, G124, added 2026-10-06 at 9da67fb): (a) on every ring of N = 1..16 cells, every state that reaches zero
     has least spatial period 1 or 3 * 2^k, and periods 3, 6 and 12 all occur (N = 12); (b) the single cell's canonical
     ancestors x_1..x_12, computed on a long window, have far-left tails whose least periods p_n are 1, 3, then 3 * 2^k,
     with p_(n-1) dividing p_n, p_n >= ceil(log2(n + 1)), and Rule 30 mapping each tail to the previous one; (c) the
     cyclic trajectory 001010 -> 011011 -> 010010 -> 111111 -> 000000.
  S24 (G125, added 2026-10-06 at 0c1c83f): for m = 1..10, the recurrent states of the m-cell ring map to track pairs
     (sites 0, 1) that H^m returns exactly, distinct states giving distinct pairs; for m = 1..4, a brute-force count of
     H^m-fixed pairs among all temporally periodic track pairs of period L (L the lcm of the ring's cycle lengths),
     made without the ring correspondence, equals the number of recurrent states; H(1, 1) = (0, 1).
  S25 (G126, added 2026-10-06 at 1a5a291): the ternary map T (decode a code to its pair in H's image, apply H, encode),
     built from G22's definitions: (a) no ternary predecessor window of length k + 2 maps onto any of the six forbidden
     words (length k), a local check with no periodicity; (b) for every period p = 1..8, the periodic targets with a
     p-periodic predecessor are exactly the periodic words avoiding the six words cyclically; (c) the local section R
     gives T(R(z)) = z for every such word; (d) 0220 has predecessor 2210 and 112 has none. (The first run failed
     only at p = 2 because the cyclic-avoidance test unrolled the word too few times to see 0202 inside 2020; fixed.)
  S26 (G127, G128, added 2026-10-06 at 81fb4fd): T on the period-two points 00, 11, 22, 12, 21 gives 00, 22, 11, 22, 22;
     0102 lies in Y and maps to 1212; the full-shift precursor blocks of the target prefix 022000 are exactly the six
     listed, all beginning 22100, and those of 022001 also all begin 22100; (022000) repeated lies in Y. For G128:
     every binary word of length N <= 11 is the trace of site 0 over times 0..N-1 for some finite initial row (solved
     leftwards); the spatial checkerboard is fixed by Rule 30; the pair (alternating, all ones) is not in H's image.
  S27 (G129, added 2026-10-06 at 0f3b3ec): next to the alternating wall (both phases), every left seed of radius
     L = 0..10 evolved forward with the wall as its right boundary violates the wall equation at a black time within
     18 ticks, so B(L, alternating) is empty for L <= 10 by finite boxes (death times 1,7,7,7,7,9,9,9,17,17,17 for
     phase 0 and 0,2,6,6,6,8,10,12,12,18,18 for phase 1); a seed determines at most one visible itinerary.
  S28 (G130, added 2026-10-06 at 40af176): for 200 random finite right tails and random wall prefixes of length
     N <= 12, successive solving gives exactly one left word, whose forward evolution realizes the prefix; the row
     ...111|000... becomes the single black cell in one tick; truncating its left seed to ones at -N..-1 (N = 1..14)
     keeps the wall through time N and first breaks it at N + 1.
  S29 (G131, added 2026-10-06 at 85e3257): for 40 random step functions on the circle whose jump endpoints lie on one
     rotation orbit (alpha = sqrt 2 - 1 and the golden angle; even numbers of endpoints), f(beta + y) XOR h(y) is
     constant along 20,000 orbit points, with h the XOR of rotated interval codes from Q(z) = (1 + z) P(z) over GF(2);
     for alpha < 1/2 the Sturmian word has no adjacent ones (AND factor constantly 0); and a repetition of g of length
     e - a + 1 gives a repetition of the width-(w+1) block code of length e - a + 1 - w on random words.
  S30 (G132, added 2026-10-06 at d318ac4): the circle-covering example f(x) = psi(2x mod 1), psi the Sturmian interval
     for beta = 2 alpha mod 1: its jumps on a fine grid sit at {0, 1/2, -alpha, 1/2 - alpha} mod 1 for two irrational
     alpha (both 2 alpha < 1 and 2 alpha > 1), and its orbit code equals the beta-Sturmian code from 2 theta for 20,000
     steps; the two-torus box [0, 1/2)^2 is not a function of h_(a,b) for any nonzero (a, b) with |a|, |b| <= 4 (two
     points with equal character value and different box values are found).
  S31 (G133, added 2026-10-06 at 407e7d6): for 30 random phases and C = 0, 2, 5, every golden-angle Sturmian prefix of
     length N = 84 (C + 4) contains a repetition g_s = g_(s+q) on a <= s <= b with b + q <= N and b > 2a + q + C; the
     first prefix length at which a violation appears is recorded (descriptive); the Fibonacci horizon check
     4 * 55 + 8 = 228 < 336 at C = 0; the kick-gap recursion excludes k_j = 2^(2^j) and admits k_j = 2^j.
  S32 (G134, G135, added 2026-10-06 at 748ce79): for awkward angles (golden, sqrt 2 - 1, e - 2, pi - 3, a tiny alpha
     1/(50 + golden) with a huge first denominator, and 1 minus it), 10 random phases each and C = 0, 2: every
     Sturmian prefix of length 251 (C + 4) contains a violating repetition (the first violation length is recorded);
     K_A = 8 (A + 1)^4 + 3 gives 131 at A = 1; 4 * 31 T + 3C + 8 = 251 C + 1000 for T = 2C + 8.
  S33 (G136, added 2026-10-06 at f8c09fd): exact rational mechanical codes (alpha = 0, 1, 1/2, 2/5, 3/7, random
     rational phases) and random width-(w+1) block codes (w <= 3) of irrational and rational mechanical words all
     contain a violating repetition within H(C, w) = 251 (C + 4) + 250 w (C = 0, 1); the width guard: a recoding of a
     golden Sturmian word fitting the first 120 Thue-Morse bits exists at the width where the 121 blocks become
     distinct (at least 119, since a Sturmian word has n + 1 blocks of length n), and that Thue-Morse prefix
     (overlap-free) has no repetition violating the bound with C = 0. (The first run capped the width search at 119.)
  S34 (G137, added 2026-10-06 at 9b7a799): the dyadic word (ones at powers of two) on indices 0..3000 has no
     repetition with b >= 2a + q (the bound b <= 2a + q - 1 holds for every period and start); its factor counts obey
     P(m) <= 2m + 1 for m <= 40; the base-3 and base-4 words violate the bound with C = 5 within 3000 indices.
  S35 (G138, G139, added 2026-10-06 at 2105418): forced columns v_0..v_6 computed directly from the wall and random
     visible words (100 words, 60 visible bits) match G138's five even/odd pairs; for the dyadic word v_1(0)..v_5(0) =
     1, 0, 0, 0, 1; the defect field against the checkerboard background obeys G139's two recurrences and its
     locality (e_j(t) = 0 whenever e_1 vanishes on [t, t + j - 1]) for j <= 12; dyadic defects at depth j <= 30 lie in
     the stated backward neighbourhoods of the pulse times; temporal factor counts of the dyadic columns obey
     P(m) <= 4(m + j) + 2 for j <= 10, m <= 30.
  S36 (G140, added 2026-10-06 at 3ab755c): for 50 random visible words, the forced row Phi(c) evolved two steps
     forward against the wall (an independent half-line evolution) equals Phi(shift c) at every depth not touched by
     the truncation; every Phi(c) has a black wall neighbour at odd times; and Phi(shift^(t_n) d) for t_n = 3 * 2^(n-1)
     agrees with the left checkerboard (ones at odd depths) on a prefix that grows with n.
  S37 (G140's sharpenings, Local's second reading, 2026-10-06): an independent forward evolution of Phi(c) against the
     wall reads back x_t(-1) = 1 - c_s at t = 2s and 1 at odd t; for every prefix length k <= 10 the 2^k prefixes give
     2^k distinct patterns on depths 1..2k, already distinct on depths 1..2k-1, and 2^(k-1) on depths 1..2k-2 (odd
     depths free, even depths forced), with depth 2 = NOT depth 1; and a left row of radius L >= 1 has radius exactly
     L + 2 after one F iterate.
  S38 (G141, added 2026-10-06 at 54956f6): rows by depth from the wall, backward step q_(j+1) = y_j XOR (q_j OR q_(j-1)).
     For 400 random finite white-phase rows u (radius 1..15): the black-phase predecessor (q_0 = q_1 = 1) evolves
     forward to u, has radius exactly L - 1 when finite, and its tail (zero or black) is the one the M0 graph predicts
     from the last pair; both white-phase predecessors (q_0 = 0, q_1 = a) evolve to it, are finite exactly when the
     M0 test says so (with radius exactly L - 2), and have a period-three tail containing ones after a black tail;
     the guard rows 011 and 101 both give 1011 and then 10011; and for 30 random visible words c the white-phase
     predecessors of Phi(c) are Phi((1 - a) c), the phase convention of G140.
  S39 (G143, added 2026-10-07 at 54a9d03; all within GC159's 4,096-symbol prefix, 60-digit decimals): for
     c_s = floor(s beta) mod 2, beta = 2 - sqrt 2: the mismatch rule (c_s != c_(s+q) exactly when x_s = {s beta} lies in
     [1 - eps, 1) or [0, -eps), eps the error to the nearest even integer) for q <= 200 and s + q <= 4,095; the
     same-sign error records for q <= 2,048 are exactly 1, 2, Q_n = q_n + q_(n-1) and 2 q_n; for n = 2..9 the q_(n+1)
     orbit points have exactly two gaps, d = |delta_n| (q_(n+1) - q_n times) and E = (1 + r) d (q_n times); the first
     positive mismatch is at q_n for period Q_n and in [q_n, Q_n] for period 2 q_n; and every maximal repeat interval
     of those periods inside the prefix has debt at most -3 (Q_n) and q_(n-1) - q_n - 1 (2 q_n), with -3 attained.
  S40 (G144, added 2026-10-07 at f824c71; G144's own arithmetic controls, 60-digit decimals, prefixes under 2,100): for
     beta = sqrt 2 - 1 and the even numerators p_n = 2, 12, 70 the first positive mismatch of period q_n is q_(n+1) and
     the initial interval has debt q_(n+1) - q_n - 1 or - 3 by the sign of delta_n (6 at period 5, [0, 11]); for
     beta = [0; 1, 1, 4, 4, ...] the numerators are odd and, for period 2 q_n, the first positive mismatch is
     (a - 1) q_n + q_(n-1) and the initial debt (a - 3) q_n + q_(n-1) - 1 or - 3; for beta = 2 - sqrt 2 the even
     mediants satisfy B_n |D_n| = 1 / (B_(n+1) / B_n + r) < 1/2 and are alpha's convergents, consecutive and unimodular.
  S41 (G145, added 2026-10-07 at e760928; within GC159's 4,096 symbols, exact integers cross-checked by 60-digit
     decimals): for the half-phase code c_s = floor(s beta + 1/2) mod 2, beta = 2 - sqrt 2, and n = 3, 5, 7, 9, the
     period Q_n = q_n + q_(n-1) has its first mismatch at h_n = 2 q_n + q_(n-1)/2 (none at time 0, none before), so the
     prefix interval [0, h_n - 1] has debt q_n - q_(n-1)/2 - 1 = 3, 22, 133, 780; and the mismatch times agree with
     G145's arc {k beta} in [1/2 - E, 1/2), E = (1 + r) |delta_n|.
  S42 (G146, added 2026-10-07 at 960ddfa; only GC159's 4,096 symbols of c^(0)): sigma^t c^(0) = c^(t beta mod 2) on
     the prefix; along the shifts t < 2,048 whose phase t beta mod 2 sets a new closest approach to 1/2, the shifted
     prefix contains G145's witness whenever its agreement with c^(1/2) covers it, its maximal debt (all periods within
     the shifted prefix) never exceeds t, and the agreement reaches beyond the n = 7 witness. A first draft also asked
     the agreement and the debt to rise monotonically along the records; G146 claims neither, and that draft failed
     (the approach alternates sides of 1/2 and the shrinking prefix truncates the debt); it was narrowed to the above.
  S43 (G148, added 2026-10-07 at eeb3e01): on GC159's silver prefix and on 20 random words of length 600, for
     k = 1..5 and n = 1..12, P_(D^k x)(n) <= P_x(n+k) <= 2^k P_(D^k x)(n), and the jet (x, Dx, ..., D^k x) has exactly
     P_x(n+k) length-n factors; D^(2^m) = 1 + S^(2^m) for m <= 4; a p-periodic Dy forces y to be 2p-periodic (all
     y up to p = 6); the ordinary second difference of 0101... alternates -2, 2 while its XOR D^2 vanishes; and the
     left checkerboard is fixed by every single wall step, so every positive-order temporal difference at every
     depth vanishes on a row of infinite support.
  S44 (G149, added 2026-10-07 at 1df0f13): (a) on every cyclic ring of size up to 24 (numpy), each row reaching zero
     has least period 1 or 3 * 2^a with a <= T - 2, T its first-hit time (G124 with G149's bound); (b) from 200 random
     finite rows, k = 1..4 wall-phase backward pairs (black step q_0 = q_1 = 1, white step q_0 = 0 with a random q_1)
     give rows whose far tails are eventually periodic, with least period 1 or 3 * 2^a, a <= 2k - 2, and whose tail
     pattern reaches zero within 2k ordinary steps; each evolves forward 2k wall steps back to its finite row; and
     (c) the controls 001 -> 111 -> 000 and the stationary 01. The first run of (b) failed through my orientation slip
     (depth-indexed tails fed to a left-to-right ring); reversed, every case passes.
  S45 (G150, added 2026-10-07 at 70db53c): for every nonconstant cyclic output of least period p <= 14, the number of
     Rule 30 predecessors on rings of size m p (m = 1..6), counted independently by the left-to-right transfer matrix
     (trace of the product over a period, raised to m), is 1 for every m when a cyclic run of ones has length 1 mod 3,
     else 2 for every m when the number N of runs of length 2 mod 3 is even, else 2 for even m and 0 for odd m; and the
     three literal controls (001 <- 101; 011 <- 001010 and its translate by 3; 000111 <- 000010 and 111001).
  S46 (G151, added 2026-10-07 at 8ecebee): for every nonconstant cyclic output of least period p <= 12 whose
     predecessors double (G150's odd case), both period-2p predecessors (found by the descending recursion on a ring of
     size 2p and confirmed by forward steps) contain the cyclic factor 010 and have exactly one predecessor on rings of
     size 2p and 4p; on every ring up to size 24, each row reaching zero first at time T >= 2 has least period 1 or
     3 * 2^a with a <= floor((T - 2) / 2); and the literal six-site trajectory 101011 -> ... -> 000000.
  S47 (G152, added 2026-10-07 at aba4501): the primitive-necklace counts L(3) = 2, L(6) = 9, L(12) = 335 by brute
     force; on rings of size 3, 6, 12 and 24 every zero-reaching row's first-hit trajectory visits pairwise distinct
     rotation classes, every class on it has least period 1 or 3 * 2^b, and T + 1 <= C_a for its least period
     3 * 2^a; the trajectory 011 -> 010 -> 111 -> 000 attains C_0 - 1 = 3; and the largest first-hit time at each
     ring size is reported.
  Instrument fault found 2026-10-07 while checking S47: the ring censuses of S44, S46 and S47 ran the forward map for
     only 3n + 3 steps, and on the 24-ring 2,592 rows reach zero later (up to step 147), so those checks were not
     exhaustive although S46's note said so. All three now use the exact basin from a backward search (zero_basin),
     cross-checked on the 24-ring against 1,500 forward steps; the verdicts are re-run on the complete sets.
  S48 (G154, added 2026-10-07 at 5759564): r(n) = parity of overlapping 11s satisfies r(2n) = r(n) and
     r(2n+1) = r(n) XOR (n mod 2) for n < 2^14; (r(n), n mod 2) is the fixed word of a -> ab, b -> ad, c -> cd, d -> cb
     on its first 2^14 letters; the sixth power of that substitution's letter matrix is positive; and the separated-block
     identities r(2^k + m) = r(m), r(3 * 2^k + m) = 1 XOR r(m) hold for k <= 12 and m < 2^(k-1).
  S49 (G155, added 2026-10-07 at bec27d5): for 60 random visible words, changing any letter c_i with i >= ceil(L/2)
     leaves the initial row through depth L unchanged (L = 1..40), while changing c_(ceil(L/2) - 1) changes depth L
     when L is odd (the free odd depth); depth 3 is 1 - c_1 and depth 4 is c_0 c_1; and on the first 2^18 letters of
     r the factor counts satisfy P(k) <= 16 h < 32 k for k <= 64 (h the least power of two >= k). Descriptive: the
     counts observed for 8 <= k <= 64 (the record's comparison with the known complexity is in the chat, not here).
  S50 (G156, added 2026-10-07 at 9fcc564): for every period P <= 7, exhaustively over all 4^P pairs of P-periodic
     temporal words, B(a, b) = (S b XOR (a OR b), a) commutes with rotation; the rooted tree (all pairs that reach the
     root (0, 1^P)) has longest prefix K with K + 1 <= N_4(P), the all-necklace count; its pairs at different depths lie
     in different rotation classes; K = 3 at P = 1 and K = 8 at P = 2 with G156's literal path; and the largest K by P
     is reported.
  S51 (G157, added 2026-10-07 at 70a3fad): for every P <= 15, the rooted edge tree built by children (c(t+1) =
     a(t) XOR (b(t) OR c(t)), closed cyclically) has every profile of least period a power of two dividing
     Q = 2^v2(P), its longest prefix K equals that of the Q-tree, and restriction to the first Q letters maps its nodes
     bijectively onto the Q-tree's; the period-three pair (0, 100) is not dyadic. K for Q = 1, 2, 4, 8 is reported as a
     by-product. (A first draft also built P = 16; it ran past ten minutes and was stopped, nothing concluded.)
  S52 (G158, added 2026-10-07 at 6592bf3): on the rooted trees of S51 (P <= 15), every node's number of child
     rotation classes follows G158's rule (driver nonzero: 1; zero driver, block parity 0: 2; parity 1: 1 if 2q | P,
     else 0); the quotient is a tree with leaves = even-parity branch nodes + 1; P = 1 and 2 quotients are chains; and
     the local guards a = 0110 -> {0010, 1101}, a = 0101 -> {0011, 1100} (written in time order).
  S53 (G159, added 2026-10-07 at 60d0ce8): on the same trees, every descendant within six depths of an even-parity
     zero-driver node has a nonzero driver, and the number of rotation classes at depth n is at most 2^ceil(n/7).
  Found while writing S52/S53: for every P <= 15 the rooted trees contain no even-parity branch node at all (each
     quotient is one chain), so on them the spacing claim is vacuous and the two-class case of G158 untested. Both
     lemmas are local, so S52 and S53 also run them ambiently, over every pair (a, b) of P-periodic words, P <= 8:
     G158's child-class count at every pair, and G159's six nonzero drivers below every nonzero even-parity a with
     driver zero, along every continuation.
  S54 (G160, added 2026-10-07 at b1cc1a2): on G8's full-line front graph for every P <= 7 (states (a, b, r), the zero
     pair excluded; children c with c(t+1) = a(t) XOR (b(t) OR c(t)); arrival r' one past the first black b cell at or
     after r, or r' = r when b = 0), the gate is forward invariant, every state enters it within two edges, every
     state on a cycle (Tarjan components) is gated, each pair's gated phases number the black cells of a (or the
     transitions of b when a = 0), and the period-four control a = 0101, b = 0, r = 1 needs both edges.
  S55 (G161, added 2026-10-07 at 17b7292): the single representative path, run for Q = 1, 2, 4, 8 only, reports no
     genuine branch and visits exactly K(Q) nodes of S51's complete trees, its pair period stays exact, and the
     labeled node counts obey N(Q) = N(Q/2) + Q (K(Q) - K(Q/2)) = 3, 13, 97, 3065.
  S56 (G162, added 2026-10-07 at 2756706): by literal reset arithmetic (each driver's cost = steps to one past its
     first black cell at or after arrival), at every even-parity zero-driver pair (a, 0) of every period P <= 10 and
     every gated phase r, the three post-split costs of the two children are {l + 2, l + m + 2} for the adjacent runs of
     c at r; the rooted control a = 0000110001010011 gives the six cost pairs of G162; the single-black-cell family
     attains q + 2 at q = 4..16; and the pulse-difference family has orders q - 2 -> q - 1 and cost q + 2 at q = 8..16.
  S57 (G163, added 2026-10-07 at 7869162): for 400 random strips (m = 1..12 drivers, period P = 1..8, zero drivers
     allowed), the block map F is nondecreasing with F(t + P) = F(t) + P; every phase cycle gives the same rate rho;
     |F^n(t) - t - n rho| <= P - 1 for all t and n <= 60; and when rho <= 5m/2 the truncated supremum H is at most
     2(P - 1) and satisfies the block inequality; the pulse strip attains the error P - 1, and the G8 witness's
     F(0) = 27, F(3) = 31 at P = 4 give F^n(0) = 28 n - 1.
  S58 (G164, added 2026-10-07 at 1c93907): for 300 random driver lists (M <= 40, P <= 8, zero drivers allowed) at
     gamma = 1 and 5/2, every interval map from every start u and every global phase shift obeys
     G(u) - u <= gamma (b - a) + D + P - 1, with D the reference path's all-interval debt; the birth-clamped front,
     computed by its own recursion f_j = max(beta_j, F(f_(j-1))) for random barriers beta_j <= j, obeys
     f_k <= gamma k + D + P - 1; and the single pulse attains the overhead P - 1.
  S59 (G165, added 2026-10-07 at 3d9dbda): along the known Q = 16 representative path (S55's rep_path, replayed to its
     first genuine branch at depth 53,207), the pair period never decreases, changes only at odd-parity zero-driver
     nodes and only by doubling, every node's driver has least period dividing its stage period, the stage entries are
     N_1..N_4 = 3, 8, 29, 400 with no period-32 node, and the branch node keeps period 16.
  S60 (G166 addenda, added 2026-10-07 at 818c533): on HG4's gated aligned graph (rule30_hg4.py) at q = 4, 6, 8 the
     least potential h is reached, and the largest shortest tight-edge distance to the zero-potential set equals the
     first stable Bellman horizon (4, 21, 85), computed separately; the abstract chain (-1, +1)^L, +1 has max h = 2 and
     horizon 2L + 1 for L = 1..12; and for q = 4, 8, 16 the driver-only edge (S b XOR b, b) -> (b, b) exists with reset
     cost q and gated ends, and (b, b) has the single child 0.
  S61 (G166 scope table, added 2026-10-07 at a0cb85d): G8's cyclic period-4 list [9, 8, 14, 12, 4, 7, 6, 2, 11, 3, 1,
     13] is compatible; for each row of the table (driver b, preceding a, arrival r) the gate bit a(r - 1) is 1 and the
     reset delay of b from r is the listed delta; the delays sum to 36, so a phase-free g(a, b) needs gamma >= 3.
  S62 (G167, added 2026-10-07 at bb39671): at every gated even-parity zero-driver case of every P <= 10, the literal
     delays of the four-edge branch block are 0, 1, 1, l (fast sibling) and 0, l + 1, 1, m (slow sibling); the
     doubled prefix rewards are G167's, the block rewards are at most 2q - 16 and the anchored prefix maximum at most
     max(0, 2q - 10); the q = 16 rooted control gives block maximum -4 and prefix maximum 2; and the q = 8 pulse
     case gives slow block 0, two-edge prefix 6 and the after-free-edge reset reward 11.
  S63 (G168, added 2026-10-07 at 25521dd): on 500 random finite paths with disjoint four-edge blocks, the least
     contracted potential K lifted by h = K + A at retained vertices and backward fill inside blocks satisfies every
     original edge inequality with max h <= max K + A + B; over every gated block of every P <= 10, the largest
     anchored prefix reward is at most max(0, 2q - 10) and the largest subinterval reward at most max(0, 2q - 5); and
     the q = 8 slow pulse block lifts to (6, 11, 0, 3, 6).
  S64 (G169, added 2026-10-07 at 8d75ab4): the three witness edges are valid gated compatible edges with the stated
     costs and distance triples ((3, 4, 3) -> (4, 4, 0); (1, 0, 1) -> (0, 2, 2); (q, q, 0) -> (q, 0, q) for q = 4, 8, 16),
     and the resulting linear inequalities force beta - chi <= 1 and beta - chi >= 11/8 at q = 8, an empty system.
  S65 (G170, added 2026-10-07 at 6b2cd29): at q = 8 and 16 the period-4 words (12, 8), (8, 8), (9, 0), (0, 14)
     repeated q/4 times keep both edges compatible and gated with the same phase-0 delays and distance triples; with
     the pulse edge, the dual combination (q/2, q/2, 1) leaves 0 >= 6q - 2 gamma (q + 1), so gamma >= 3q/(q + 1),
     which is 8/3 > 5/2 at q = 8 and gives no contradiction at q = 4.
  S66 (G171, added 2026-10-07 at 3ff10fb): at q = 16, 32, 64 the three exact-period edges (b with black bits 3, 7,
     q - 1 to (b, b, 4); (S c XOR c, 0) to (0, c) for c with bits 1, q - 1; the pulse) are compatible and gated, keep
     the triples (3, 4, 3) -> (4, 4, 0), (1, 0, 1) -> (0, 2, 2), (q, q, 0) -> (q, 0, q), and every endpoint word
     has least period exactly q; at q = 16 the words are 32904, 49356, 32770, 49155 and 32768.
  S67 (G173, added 2026-10-07 at 3c91458): at q = 4 (DQ3's (15, 12) -> child 2) and at q = 8, 16, 32, 64 (b with bits
     2, 3, q - 1; c with bits 1, 5, q - 1; a = S c XOR (b OR c)) the edge is compatible and gated, costs 3, has source
     and target triples both (1, 3, 1) and pair least period q at both ends; at q = 8 the words are a = 255, b = 140,
     c = 162 and the aligned target (145, 84).
  S68 (G174, added 2026-10-07 at 9588885): the period-4 chain (0,15), (15,15), (15,0), (0,5), (5,15), (15,5), (5,5),
     (5,0), (0,9), (9,15), (15,12) is compatible and is the unique predecessor chain from (15, 12) to the root; carrying
     the full-line clock from root times 0, 1, 2, 3 reaches (15, 12) at times 9, 13, 13, 13 (phase 1 every time);
     there its triple is (1, 2, 1) and the next edge lands at phase 3 with (1, 3, 1), while phase 0 is gated but unreached.
  S69 (G176, added 2026-10-07 at 0f15531): at q = 8 the pair (183, 176) has a unique predecessor chain of exactly 190
     steps to the root (0, 255); its child 26 reaches (176, 26), aligned (133, 208) at phase 5; every forward triple
     is compatible; from all eight root residues the clock reaches the source at 360 and the target at 365; both ends
     are gated with distances (1, 5, 1) and pair least period 8; toggling the source's bit 0 breaks compatibility.
  S70 (G178, added 2026-10-07 at 5c2f424): the seven RQO representative edges are reached edges of RQ3's q = 8 domain
     (depths 270-275 and 318-320) with the stated costs summing to 21 and the stated refined labels, which close in
     feature space; both splices are false joins ((138, 140) != (182, 84), (137, 206) != (143, 26)), so the summed
     inequalities give 0 >= 21 - 7 gamma, i.e. gamma >= 3, for every function of the refined features.
  S71 (G179, added 2026-10-07 at 07195dc): on 300 random weighted DAGs, the least line-graph potential K lifted by
     h(s) = max(0, max over (s, t) of w + K) satisfies every original edge inequality with h <= W + max K, and K(s, t)
     = h(t) satisfies every consecutive-pair inequality; the one-edge terminal control gives h = (r, 0) with K = 0; and
     G178's seven feature edges, line-graphed after compression, still form a cycle of total doubled reward 7.
  S72 (G182, added 2026-10-07 at 7407ea9): the RC2 certificate rebuilt in memory as rule30_rc2_export.py writes it is
     byte-identical to the shared artifact (56,232 bytes, the recorded SHA-256); GPT's checker (any int.bit_count
     replaced on Python < 3.10, nothing else; GPT made it portable at 25a64b5) accepts all four caps, still accepts a reordered copy, and rejects eight real
     corruptions, each at the intended assertion (zero K, a lowered tight K, the known tree edge removed, a non-tree
     edge removed, a changed delay, a dropped terminal label, a false summary, an unreached vertex); the exact least
     potential on the certified edges has maxima 0, 0, 1, 14, so the finite budget 14 is attained, once, by the actual
     reached path (143, 200) -> (132, 215), depths 273 -> 281, rewards 3, 3, 1, -3, 5, -3, 3, 5; the K lift dominates
     it, looser at 14 of 409 vertices by at most 5.
  S73 (G183, added 2026-10-07 at fcedaa4): on 400 random small weighted graphs with random label maps (seed 183), a
     nonnegative label potential exists (longest-path relaxation) exactly when no subset of actual edges, found by
     brute force, balances at every label with positive reward (111 feasible, 260 not); the least potential equals
     the best simple label walk and lies below every other feasible potential found; the +1, -1 merged-endpoint
     control is feasible with F = (1, 0); G176's reached q = 8 edge (cost 5) is a balanced singleton in RQ3's labels
     but not in RQO's; DQ3's literal q = 4 edge (15, 12) -> (9, 4) (cost 3) is one in the three distances; G178's
     seven reached edges balance at every RQO label but not at four actual states, with elapsed 21.
  S74 (G184, added 2026-10-07 at 7aed12f): the stage entries N_1..N_4 = 3, 8, 29, 400 recomputed from RQ3's reached
     graphs (first node of least period q at q = 2, 4, 8; the single q = 8 cap exit after depth 399), every depth's
     states being temporal rotations of one another (unbranched), and each reached graph at q <= 8 acyclic with one
     sink, its cap exit (no history stays at period <= 8); R_j and lambda_j exact and the recurrence and closed
     form on them; on 200 random nonnegative schedules (seed 184) the closed form and the window bound
     R_j >= 2^-m (lambda_(j-m) + ... + lambda_(j-1)); the constant schedule lambda = 3 from R = 100 gives exactly
     3 + 97/2^j; the alternating schedule (1 at even j, j at odd j) meets both of G184's bounds and passes 99 by
     j = 400; on each recorded stage the period-to-depth ratio peaks at entry, at 1/R_j.
  S75 (G185, added 2026-10-07 at 3901bff): at q = 4, 8, 16, 32, 64 the words a, c, e built as stated and f, the single
     periodic child of (1, e) by the two-seed recursion, give a prefix a, 0, c, 1, e, f whose four triples satisfy
     S z = x XOR (y OR z); orders (cyclic differences on the 2q-cycle) q, 0, q + 1, 1, q + 1, 2q; least periods q for a
     and 2q for c, e, f; f of weight q/2 + 1; pair maxima q + 1, q + 1, q + 1, 2q; the three later pairs of least period
     2q with nonzero drivers; G160's gate at all five pairs from arrival phase q - 2 with the reset-clock updates; the
     q = 4 masks 238, 180, 255, 150, 82 with f confirmed by brute force. At q = 2 the run count fails (f has weight 1)
     and the gate fails at (a, 0) from phase 0, although f still has order 4. Rooted at q = 4: RQ3's reached q = 8
     graph passes through the prefix at depths 28 -> 32 by consecutive edges (arrival phases G185's plus 5), so the
     jump of 3 happens on the actual history at 31 -> 32; the rooted q = 8 cap exit is not G185's q = 8 entry.
  S76 (G186, added 2026-10-07 at d7b103e): at gamma = 5/2, theta = 11/5 (time margin 1/2, endpoint margin 1/5), on 300
     random good depths (seed 186) the largest k with ceil(theta 2^k) <= n gives n < ceil(2 theta 2^k), and once P/2^k
     is small against A, B, L (134 cases) G2.4's three requirements and its A'''' sandwich hold with the settling bound
     taken at its worst; a slope with gamma theta = 6 fails the time requirement. On G186's spike schedule (N_1 = 2,
     lambda = 2^(2^(k-1)) at j = 2^k, else 1) the recurrence holds exactly, p/M = 1/R_j at every entry, every depth
     n in stage j has R_(j+1) > n/(2 p(n)), R_(2^k + 1) >= 2^(2^(k-1))/2, and R_(2^(k+1)) <= 1 + k 2^-(2^(k-1)) for
     k = 1..4 (R_17 > 128, R_32 - 1 < 1/100); on 200 random schedules lambda_j/2 <= R_(j+1) <= max(R_j, lambda_j),
     so limsup R_j is infinite exactly when lambda is unbounded.
  S77 (G186's paperfolding continuation, added 2026-10-07 at f366f6b): A'''' at (-1, 0) with a = 2i, a' = 2i',
     n = 2l on the recorded repeats (RULE30-PRIZE 8.59, BF4; at k = 14 the pairs (0, 49152, 32768) and (16384, 49152,
     32767)); for s = 2^3 .. 2^20, L in {1, 7, 100}, P in {0, 1, 3} the paperfolding contradiction holds exactly from
     M = L + 2s + 2P + 2 and fails one below and at M = 4s, and Thue-Morse's from M = L + 2s + 2P; GPT's offset control
     (L = 1, s = 8, P = 1: M = 21 gives 29 < 30, the Thue-Morse threshold M = 19 gives 31, no contradiction); theta in
     (2, min(4, 6/gamma)) nonempty below slope 3, and theta = 11/5 at gamma = 5/2 reaches the contradiction for
     s = 2^20 .. 2^39 once the constants are small against s.
  S78 (G187, added 2026-10-07 at e7829c1): delta = (3 - gamma)/(2 gamma + 2A + 8); r < delta exactly when
     4r/(1 - 2r) < (6 - 2 gamma)/(2 gamma + A + 1) on a rational grid (gamma 1 .. 29/10, A 0 .. 10), delta <= 1/5, and
     delta <= 1/7 once A >= 2 (delta = 1/42 at gamma 5/2, A 4); GPT's integer control (s = 256, M = 547, 1447.5 < 1536,
     1021 against 1022); on 400 random depths (seed 187) with q <= r n, r < delta, the endpoint 2s + 2q + D <= n
     reaches both contradictions (800 of 800), while at r = 3 delta its time margin fails (200 of 200); the strict
     threshold cannot be relaxed; within each stage p/M is least at N_(j+1) - 1, equal to 1/(2 R_(j+1) - 2^-j); the
     schedule 25 2^j (400 above 1/42, 799 below); the recorded stage ends 8/399 and 16/53207 are below 1/42.
  S79 (G187's dyadic refinement, added 2026-10-07 at 9992b94): K, the least power of two above
     (2 gamma + A + 1)/(6 - 2 gamma), has a positive coefficient gap and K/2 has none, and K >= 2 once A >= 2 (the
     fraction is at least 5/4); GPT's control (fraction 10, K = 16, threshold 17, s = 256, M = 547, margin 88.5, K = 8
     gap -2); for q = 2^8 .. 2^40 the endpoint s = Kq, M = 2s + 2q + D reaches both contradictions once q is large
     against D and B; the schedule 18 2^j passes 17 but its stage ends tend to 1/36 > 1/42; the record's R_4 = 25 > 17.
  S80 (G188 with its continuation, added 2026-10-07 at 46e23c5 and ea8fd3f): after every odd doubling at q = 4, 8, 16
     (every odd q/2-source, both children, T c = 1 + c) no profile at positions 1 to 10 is zero (the first returns are
     21 at q = 4 and 88 at q = 8); for every nonzero c at caps 2 to 12, every branch has the profile 1 at position 2
     and no zero at positions 9 or 10; GPT's E table, the position-9 transitions (one cycle, 010 <-> 101) and the
     position-10 edges (five, acyclic), and position 8's allowed triples 001, 010, 011, 100, 101, all by brute force;
     the even-source seven-step control at cap 4 and the q = 2 five-step return; the rooted q = 16 stage from the
     q = 8 cap exit (161, 0) first returns 52,808 steps later (depth 53,207) with an even driver, G2.3's split.
     The ambient first returns at q = 16 are in rule30_g188_returns.py (exploratory, not preregistered).
  S81 (G188's return-11 continuation, added 2026-10-07 at bdfc1f6): H and F as stated; the successor rule's table
     equals GPT's sixteen entries, every state feeds one 11-cycle, and the cycle word 00001111001 has exactly those
     windows; backward reconstruction from it gives a compatible return at position 11 at cap 11, nonzero throughout,
     with an even-parity source, and the forward walk from its (0, c) reproduces it; among caps 2 to 13, a first zero
     at position 11 occurs only at cap 11; after every odd doubling at q = 4, 8, 16 nothing through position 11 is zero.
  S82 (G189, added 2026-10-07 at 43ca004): G189's backward functions computed directly on all words of length 9: for
     n <= 12, U_2j(0) is a function of w(0..j) with coefficient 1 in w(j), and U_(2j+1)(0) of w(0..j); U_2 = Delta w,
     U_3 = w Delta w (which ignores w(1) when w(0) = 0), U_4 = Delta^2 w; the r = 5 and r = 7 maps; at caps 2 to 11
     every nonzero c whose first zero is at an odd position r = 2k + 3 has least period at most 2^k (exactly 2 at r = 5,
     4 at r = 7; 11 at r = 11); at cap 12 an even first return at r = 8 has an entry of least period 12.
  S83 (GC244's control, added 2026-10-07 at fe0e7bd): w = 10100100 at cap 8 reconstructs, through G189's backward
     functions, a compatible first return at position 8 from c = 10010011 (weight 4, least period 8, no complementary
     halves; source 10110100, least period 8, even); over all 357 cyclic words at caps 4 to 16 giving a return at 8,
     the gaps between ones have one or two zeros, the length is 2A + 3B and the entry weight 2A + B, so a balanced
     entry needs B = 2A and q = 8A (found only at caps 8 and 16).
  S84 (G190, added 2026-10-07 at de10ef7): the paired-window graph built from its definition (F = U_(2m-1) and A from
     U_2m on m-bit windows, vertices 1, 1, 25, 25, 225, 1089 for m = 1..6) has no length-q/2 path from a vertex to its
     swap for q = 2, 4, 8, 16, and exactly then no doubling-entered return at r = 2m + 2 exists; the two actual even
     first returns after odd doublings, q = 8 at r = 88 and the rooted q = 16 at r = 52,808, equal G189's backward
     reconstruction at every position, with U_(r-3) = 1, complementary halves, least period q and a source of least
     period q/2 and odd half-parity; the q = 8 one traces a length-4 path from v to its swap in the graph so defined
     (m = 43); the r = 4 graph has one vertex and no edge; GC244's control fails c(1) + c(5) = 1; c = 010101 on cap 6.
  S85 (G191, added 2026-10-07 at 0b4a947): on 400 random graphs of up to 8 vertices with an involutive automorphism
     (seed 191; 266 with and 134 without the component), G191's test (a sigma-invariant strongly connected component
     with a cycle, period g a power of two, class shift 0) predicts the dichotomy: with it every dyadic q from 2^8 to
     2^12 is admitted, without it every admitted q is at most n; the 4-cycle with a half shift admits q = 4 only,
     K_{2,2} with the in-part swap every q >= 4, the 6-cycle with a half shift nothing, two exchanged loops nothing.
  S86 (G191's cutoff continuation, added 2026-10-07 at 2b8a267): on 300 random graphs of up to 7 vertices (seed 1912;
     183 with the persistent component, 117 without) admission at each of the first two dyadic Q >= 8 n^2 agrees with
     the component test; 3 and 5 represent every integer from 10 (residues 0, 2, 1 mod 3 first at 0, 5, 10) but not 7;
     an isolated fixed vertex admits nothing; at Q = 128 the half-turn 4-cycle is absent and K_{2,2} present.
  S87 (G191's Rule 30 continuation, added 2026-10-07 at 96ecd4d): in G190's actual graphs for m = 1 to 6 no edge
     joins two sigma-fixed vertices; on 600 random involutive graphs with that property (seed 1913), every invariant
     component in which each vertex has exactly one internal successor (106 found) fails the persistence test; a
     sigma-fixed self-loop, which breaks the property, admits every dyadic q.
  S88 (G192, added 2026-10-07 at 1a7f5e4): U5 = F3 accepts exactly the triples 001, 010, 011, 100, 101; at every cap
     from 1 to 16 the 362 single words with U5 = 1 (10100100 among them) all have c = 1 + S Delta^2 w and only
     accepted triples, yet no two of them, shifted or not, have complementary entries c_u + c_v = 1; the solutions of
     Delta^2 beta = 1 at caps 4, 8, 12, 16 are the four rotations of 0011, each containing 11001.
  S89 (G193, added 2026-10-07 at d689b08): in G190's graphs for m = 1 to 6, every edge ends in H_m (V(X) + V(Y) = 1,
     V = U_(2m-2)), every discarded vertex, diagonal ones included, has indegree 0, |H_m| = 2 N0 N1 with (N0, N1) =
     (0, 1), (0, 1), (2, 3), (2, 3), (5, 10), (16, 17), and for every source vertex and appended pair the edge equation
     holds exactly when V(X') + V(Y') = 1; orientation plus edge label equals the target's orientation on every edge;
     the longest r = 8 path has 5 edges (G193 bounds it by 6); V_3 = x + z on G192's triples; the labelled quotients
     of the half-turn 4-cycle (q = 4 yes, q = 8 no) and K_{2,2} (every even length, not 1).
  S90 (G194, added 2026-10-07 at 87fd466): on 500 random strongly connected labelled quotients (seed 194; up to 6
     vertices, parallel edges allowed; 105 with A soluble, 100 with only B, 295 with neither), G194's two GF(2)
     potentials predict the explicit two-sheet lift exactly: A soluble gives no swap path; only B gives admissions at
     q = 2g alone, and none unless g is a power of two; neither gives persistence exactly at power-of-two g (checked to
     q = 4096, beyond G191's cutoff); the half-turn 4-cycle's quotient (A fails, B holds), K_{2,2}'s (both fail), the
     1-1 two-cycle (A holds), and adding 1 to every edge, which wrongly rejects the locked case.
  S91 (G195, added 2026-10-07 at b4c160a): in G190's graphs for m = 1 to 6 (pruned to H_m, canonical sources) each
     source has at most one edge per label, parallel quotient edges always carry opposite labels, and they are exactly
     the four-window pairs over (m - 1)-bit T (one each at m = 3 and m = 6, none elsewhere, all in acyclic graphs);
     at m = 3, T = 01 gives source (101, 001) with targets (010, 011) and its swap; on 300 random strongly connected
     labelled graphs with an opposite parallel pair added, neither of G194's potentials is soluble.
  S92 (G195's overlap continuation, added 2026-10-07 at e6c9aad): on the actual q = 8 (r = 88, m = 43, h = 4) and
     rooted q = 16 (r = 52,808, m = 26,403, h = 8) returns, beta = w + S^h w is h-periodic and nonzero, no source window
     pair on the walk has equal tails, and the walk's h quotient vertices are distinct; the guard 00001000 (h = 4)
     has three zeros in a row in beta but not four.
  S93 (G196, added 2026-10-07 at eba0105): for every (m - 1)-bit tail T and m = 1 to 10, the last-bit difference
     D_m(T) = F_m(T0) + F_m(T1) equals (m mod 2) plus the suffix sum of F_k, and the one-step recurrence
     D_m(T) = D_(m-1)(suffix(T)) + 1 + F_(m-1)(T) holds; D_1 = 1, D_2(x) = x, and at m = 3 only tails 01 and 10 have
     B_3 = 1; in G190's graphs for m = 1 to 6 a source of H_m has two out-edges exactly when B_m holds on both tails
     (4 such sources at m = 3, 2 with unequal tails; 70 at m = 6, 68 unequal; none at m = 1, 2, 4, 5); the source
     (010, 001) branches to (100, 010) and (101, 011).
  S94 (G197, added 2026-10-07 at 0b7eaae): every primitive binary word of length q <= 12 is phase-identified by q - 1
     bits (0001 needs exactly 3); by brute force over every continuation after a flipped append (five small primitive
     words, m = q to q + 3, every exit phase) no first window returns to an original window before m - L + 1 edges,
     and on three complementary dyadic words no paired continuation reaches equal tails before m - h; GPT's w = 01,
     m = 3 path returns in exactly 3 edges; the PR196-D1 word's sixteen 8-bit blocks are GPT's table, all distinct,
     with phases 7 and 13 sharing 0011000, so L = 8 and the bounds are 26,396 and 26,395.
  S95 (G198, added 2026-10-07 at 75156e9): on 600 random graphs built around a dyadic cycle (q = 2, 4, 8) with the
     half-turn swap and random swap-closed extra edges and vertex pairs (seed 198; 321 persistent, 279 not), the
     component of the cycle is persistent (period a proper divisor of q) exactly when some excursion from a cycle vertex
     back to the cycle has l + s - u != 0 mod q, and G191's component test agrees; GPT's locked detour has G = 4 and
     no mismatched excursion, the chords give G = 1; three edges from phase 0 end aligned at ordered phase 3, while
     phase 1 would read as residue 2; D1's hypothetical rejoin from 0 after 26,396 edges is aligned at phase 12.
  S96 (G199, added 2026-10-07 at 6fa98c5): with B(a, b) = (S b + (a OR b), a), six and seven steps back from
     (w, w) = (10100100, 10100100) reach (0, c) and (a, 0), c = 10010011, a = Delta c = 10110100 (weight 4, least
     period 8); at caps 1 to 8 the only nonzero pair mapped to zero is (0, all ones); no rotation of (a, 0) lies in
     RQ3's rooted cap-8 graph, whose zero drivers (depths 2, 7, 28, 399) all have odd parity over their own least-period
     block while a's is even; iterating B from (w, w) enters a cycle of length 4,064 after 389 steps without reaching
     zero; (01, 10) at cap 2 cycles without reaching zero too. A first draft of the check took parity over all 8 bits
     and failed on the rooted doublings from periods 1, 2, 4; the block parity is the right notion.
  S97 (G199's odd-domain continuation, added 2026-10-07 at 3e651f6): the D0 witness (source block 1000, odd) first
     returns at 88 and its repeated endpoint never reaches zero under B; the rooted q = 4 cap exit has block 1011, and
     doubled, with either integration child and every rotation, it first returns at 371; in RQ3's rooted cap-8 graph the
     only entries (0, c) with c of least period 8 sit at depth 29, and the next zero driver is 371 steps after depth 28.
  S98 (G200, RULE30-GPT.md, added 2026-10-07 at 0e12c2f): the rooted zero-driver sources at cap 8 sit at depths 2, 7,
     28, 399 (entries 3, 8, 29, 400), each an odd integration over its own least-period block, so the stages to periods
     2, 4, 8 are single excursions of 5, 21, 371; from source 399 the period-16 stage first returns 52,808 later, at
     depth 53,207, whose driver has least period 16 and even parity, an internal branch rather than the exit;
     telescoping and M <= lambda <= k M hold on 200 random schedules; GPT's two multiplicity controls.
  S99 (G201, added 2026-10-07 at ab7f4f2): after every even-parity zero driver at caps 4 and 8, and 400 sampled at 16
     (534 in all, seed 201), the two continuations give c and 1 + c, then 1, then e and 1 + e, and the next profiles
     f, f' are disjoint with no cyclic 00 in their union, so their weights sum to at least q/2; GPT's rooted control
     a = 0000110001010011 (Delta c with c = 0000010000110001, weight 6, least period 16, a rotation of D1's driver)
     gives e = 1, 0, 1, 1 at phases 15, 0, 1, 2, f = 0, 1, 0 and f' = 0, 1 as stated, and the following profiles share
     phase 3 (g(3) = g'(3) = 1).
  S100 (G202 and its unsigned addendum, added 2026-10-07 at 3176844): on every q-periodic compatible triple at q = 1
     to 8 (exhaustive), pi(a) = pi(b) + pi(b AND c) and |a| - |b| = 2 E(b, c) - |b AND c| with E = |S c AND NOT (b OR
     c)|, every counted rise having a = 1; pi(c) cancels (from q = 3 each parity class of (a, b) admits both parities
     of c); both identities fail on some incompatible q = 4 triples. On every edge of the rooted reached graphs at
     caps 1, 2, 4, 8 both hold, no state (0, 0) is reached, and along the root path to the single cap exit the
     excursion syndromes are pi_q of the returning sources: 1 / 0, 1 / 0, 0, 1 / 0, 0, 0, 1 with zeros at 2, 7, 28,
     399, overlap totals |a_next| + 2 sum E; each exit source is odd with no q-periodic child and a doubled child of
     least period 2q. The two known first returns: S97's q = 8 witness (r = 88) ends at the odd driver 00111101, an
     exit (syndrome 1), and S98's rooted q = 16 return (r = 52,808) at an even driver with two q-periodic children
     (syndrome 0). G202's S75 control: masks 238, 180, 255, 150, 82, weights 4, 8, 4, 3, S f = 1 + (e OR f); the pairs
     sit at depths 28 to 32 on consecutive reached edges, delays consistent with one absolute rotation; summaries (0,
     0, 0) at depths 30 and 31 with next parities 0 and 1; |e AND f| = 2, E(e, f) = 3, 8 - 4 = 2*3 - 2, and -4 without
     E.
  S101 (G203, added 2026-10-07 at 730de91): on every first-zero-return excursion from an even zero driver, both
     children, at q = 2, 4, 6, 8, 10 (exhaustive) with c and w nonconstant: r >= 5, u_(r-2) = u_(r-1) = w, the prefix
     0, c, 1, e with e = 1 + S^-1 c and startup overlaps summing to q, T = |w| + 2 E_total, T >= q + |w| and E_total
     >= q/2; when r >= 6, u_(r-3) = w + S w, its overlap is V(w)/2, T >= q + |w| + V(w)/2 and E_total >= q/2 + 1; r =
     5 occurs exactly twice at each q, always with the alternating w (least period 2), so never with a primitive w at
     q >= 4; no excursion ends at w = 1. The rooted cap-2 path's excursion from depth 2 to 7 is 0, 01, 11, 01, 01, 0
     up to rotation, with overlaps 1, 1, 1, 0, T = 3 = q + |w| and E_total = 1 = q/2; GPT's retained sketch 0, 01, 11,
     10, 10, 0 is incompatible. S97's q = 8 (r = 88) and S98's rooted q = 16 (r = 52,808) returns satisfy every bound
     with r >= 6; a single-one word has V = 2 at q = 2 .. 32.
  S102 (G204, added 2026-10-07 at a06776c): the interval lemma min B - max A <= min(B - A) <= min B - min A and G204's
     rival separation (h* attains min B; if the least rival B minus the largest rival A exceeds D*, h* is the unique
     minimizer of D) on 3,000 random finite families (seed 204; the separation decides 1,084 of them); GPT's
     counterfactual (10, 100), (80, 110) gives 90, 30, 20. From the committed outcomes (rule30_tm5b.py's 16 N_5, max
     894,235, with 667,052 among them; rule30_tm6.c's N_6 = 65,821,413 on the history entering 32 at 667,052, no other
     32-bit zero below 67,108,864 = 4 * 2^24, a completed round's end containing the exit): D* = 65,154,361, rivals >=
     66,214,630, margin 1,060,269, min lambda_5 = 2,036,073 + 25/32, and the wrong subtraction 65,733,546. A model of
     the round convention: a zero exactly at the frontier F gives entry F + 1, so F + 1 is the safe bound.
  S103 (GPT's repair of C.4, R3/GC295, added 2026-10-07 at cab0942): Rule 30 on finite windows with constant tails.
     The diagonal recursion D_k(t + 1) = D_(k-2)(t) + (D_(k-1)(t) OR D_k(t)) on 40 random rows for 11 steps; GPT's
     coalescing pair (black through site 0 then white; black except site 0) differs at site 0 and both become one
     black cell at site 1; on 300 random finite nonempty perturbations (seed 295, 20 steps) the difference set never
     empties, k_min never decreases, rises only when D_(k_min - 1) = 1, and its total rise is the sum of the rises;
     the barrier recursion keeps a difference on w + 1 with agreement below and heals it at once when the copies
     differ on w - 1.
  S104 (GPT's R4 of C.7, GC299, added 2026-10-07 at dca7307): columns beside the wall (0 at even times, 1 at odd) by
     the inverse rule from column 1. On all 55 visible words of length 8 with no 11 (Lemma 3's consequence for actual
     right halves), with random hidden odd bits, R4's seven even/odd pairs hold at every s with room and the hidden
     bits are invisible; on all 256 words C.7's formal column -4 is c_s c_(s+1) at even times and c_(s+2) at odd
     times, nonzero for some word. GPT's four seeds, driven with column 0 held at the wall, are admissible, have A = D
     = 0 and (B, E) = 00, 01, 10, 11, and give depth-7 odd outputs 1, 0, 1, 1 (as 1 + E + BE gives, and as GPT's probe
     prints), mixed XOR 1; R4's text and the probe's outcome note print 1, 1, 0, 1, a transcription slip that leaves
     the conclusion intact.
  S105 (GC306, added 2026-10-07 at f314a7d): R_(j+1) = (R_j + lambda_j)/2 exactly (Fractions) on the single cell's
     entries 3, 8, 29, 400, 87,867 and on TM6's minimizing history to 65,821,413, with lambda_1..3 = 5/2, 21/4, 371/8;
     on 2,000 random runs bounded lambda <= K keeps R <= max(R_start, K), and bounded R <= M gives lambda <= 2M;
     lambda alternating 1, 3 drives R onto the 2-cycle 7/3, 5/3 (limsups 3 and 7/3 differ); on 500 random sequences an
     eventual bound K is a bound from the root at max(K, the earlier values).
  S106 (GPT's odd-run refinement of Theorem B, entry 06, GC307, added 2026-10-07 at 1eba144): the forced left half
     from every pair of P-periodic columns 0 and 1 (column 0 nonzero), P = 2 .. 7, 40 columns deep. Every maximal
     white run in row 0 bounded by black cells has n <= 2P - 2, every odd n = 2m + 1 >= 3 has n <= 2P - 5, and its
     centre column is white at times 0 .. m + 1. Longest bounded runs seen: odd 3, 5, 5, 9 at P = 4, 5, 6, 7 (so 2P -
     5 is attained at P = 4, 5, 7) and even 4, 6, 4, 6, 6 at P = 3 .. 7 (2P - 2 attained at P = 3, 4). The stripes
     0101... are stationary; a maximal odd run with black ends shrinks with black ends and its apex, with parents 101,
     stays white one more step.
  S107 (GC310, added 2026-10-07 at 1c26430): exact arithmetic for the variable-debt refinement of G186. On random
     schedules E_j = sum_(i<=j) (d_i + 2^i - 1) obeys E_j <= 2(C + 1) 2^j for d_i = C 2^i and E_j <= 2(j^2 + 1) 2^j
     for d_i <= i^2 2^i; d_j = N_j forces N_j/(2^j + E_j) <= 1; the period-1 overhead is 0. On 3,000 random cases (1
     <= gamma < 3, theta in (2, min(4, 6/gamma))) the largest dyadic s with ceil(theta s) <= N satisfies N < ceil(2
     theta s) <= 2 theta s + 1 and s > (N - 1)/(2 theta). On the synthetic schedule N_j = 4^j with d_i = i^2 2^i,
     gamma = 5/2, theta = 11/5, (2^j + E_j)/s falls to below 10^-9 and (gamma M + E_j + B + P)/s tends to gamma theta
     = 11/2 < 6.
  S108 (GC313, added 2026-10-07 at a28e0eb): GPT's width-n strip graph for a right continuation of P-periodic columns
     0 and 1 (states: phase and the n cells right of column 1; column 1's equation constrains the first; the far-right
     input is free), pruned to its cycle core. GPT's 01/11 boundary at P = 2 dies at width 1; every pair violating
     column 1's one-step condition (P = 2, 3, 4) has no successor at all; all 49 pairs with a periodic continuation
     (AW's survivors at P = 2, 3, 4, recomputed) keep cycles at every width 1 .. 5 and the survivors cover every
     phase; sample cycles have length a multiple of P.
  S109 (GC314, added 2026-10-07 at 6284c27): column 0 alternating (0 at even times) has no 2-periodic column 1 with
     any right continuation: for each of the four sigma, no column 2 and no exterior column 3 satisfy the column-1 and
     column-2 equations on t = 0 .. 5 (exhaustive over both columns' bits), and S108's strip graph dies at width 1
     (and widths 2 .. 6); the sidedness control, constant black column 0 beside constant white column 1 (the
     stationary striped row), survives at widths 1 .. 6.
  S110 (GC312 and GC315, added 2026-10-07 at a57901b): the block merge D = max(D1, D2, A1 + H2 - m1) agrees with the
     joined block's largest forward rise on 3,000 random joins (and GPT's 2, 2 -> 3); the reference debts of
     increments 1, 1, 0, 1 and 1, 1, 0, 2 at slope 1 are 0 and 1, so the P - 1 guard is attained at P = 2 (the
     increments themselves are GPT's, not re-derived); with P <= 2^j and |D' - D| <= P - 1 the joint denominators
     differ by at most a factor 2 (3,000 random cases); the backward map B commutes with rotation at q = 8, 16, 32
     over 50 steps, so rotating a terminal pair rotates the whole recovered prefix.
  S111 (GC316, added 2026-10-07 at 5b1b58d): GPT's re-anchoring argument for all-depth maxima. The forced left half is
     translation invariant: re-anchoring at column -r (300 random pairs, P = 3 .. 7, r <= 30) reproduces the original
     columns to its left exactly; Theorem B's 2P - 2 <= 12 puts any bounded run plus its left boundary within 13
     columns at P <= 7, inside AW2's 40-column excess census; and every pair with a periodic right continuation
     (S108's _per108) keeps its bounded row-0 runs within AW's actual maxima to depth 200.
  S112 (GC323, added 2026-10-07 at e3c2c40): on 2,000 random clocks and rational slopes 1 <= a/b < 3, D^(b) = max
     b(T_v - T_u) - a(v - u) equals b D and the integer gate b N > K(b q + D^(b)) agrees with N > K(q + D); a passing
     upper debt U >= D certifies D, while a lower bound only bounds the ratio from above; |D_phi - D| <= q - 1 makes N
     > K(2q - 1 + D) pass every phase; GPT's two abstract schedules (q_j = 2^j, N_j = 2^(j^2), debt jumps on alternate
     parities) have nondecreasing debts, both ratios unbounded, and the smaller current ratio below 1 at every stage j
     = 2 .. 25.
  S113 (GC326, added 2026-10-07 at 12e3536): GPT's sparse episode. At every rotation s for q = 4 .. 32, the source e_s
     + e_(s+2) with driver e_s has the unique children 1 + e_(s+1) + e_(s+2), then 1 + e_(s+1) + e_(s+2) + e_(s+3),
     then e_(s+4), and from phase s + 1 the reset delays are q, 3, 1, q (cost 2q + 4); at q = 3 the first edge still
     holds but the four-step pattern fails at every rotation. At q = 16 the cost is 36 and the slope-5/2 debt 26. A
     separately written absolute-time walk of every rooted history at q = 16 finds the state (320, 64), clock phase 7,
     at depth 725,146, the rooted occurrence GPT reports.
  S114 (GC327, added 2026-10-07 at a9a4541): the four-edge block (costs q, 3, 1, q) has adjusted prefixes 0, q - 5/2,
     q - 2, q - 7/2, 2q - 6 at slope 5/2, debt 2q - 6 for q = 4 .. 64 (a tie with q - 2 at q = 4) and transferred
     allowance 3q - 7 (5, 17, 41, 89 at q = 4, 8, 16, 32); sum_(i=2..j) (3 2^i - 7) = 6Q - 7j - 5 <= 6Q to j = 39; the
     debt is subadditive over consecutive blocks (3,000 random splits). On the actual rooted period-16 tree, walked in
     absolute time, the start class (rotations of (e_0 + e_2, e_0)) occurs on each of the 16 histories at most once,
     exactly once on the two sharing the start at depth 725,146 and nowhere else; the pulse 1024 at depth 725,149 has
     predecessor 64639.
  S115 (GC334, added 2026-10-07 at d396289): for every q = 4 .. 32 (not only dyadic) and 1 <= r <= q - 2, 464 cases,
     the pair (e_0 + e_r, e_0) has the unique children 1 + e_1 + .. + e_r, then 1 + e_1 + .. + e_(r+1), then e_(r+2);
     from phase 1 the delays are q, r + 1, 1, q; the doubled adjusted prefixes are 0, 2q - 5, 2q + 2r - 8, 2q + 2r -
     11, 4q + 2r - 16, and for q >= 8 the debt is 2q + r - 8. At q = 4, r = 2 has debt 2 and r = 1 has debt 3/2, not
     its endpoint 1. At q = 4, r = 1 the pair after three transitions is a rotation of the start (GPT's rooted
     exclusion by G156); for q >= 8, r = q - 3 ends at the start of the r = 1 class; r = q - 1 gives the child e_0,
     then 0, then an odd exit.
  S116 (GC335, added 2026-10-07 at e7cdf43): inside every r-window (q = 4 .. 32), of the three later pairs only (C, E)
     at r = q - 2 (the terminal separation q - 1) and (E, F) at r = q - 3 (separation 1, pulse at q - 1) are named
     starts (a two-black predecessor over a singleton driver). For q = 8 .. 32 the actual child map from (e_0 +
     e_(q-3), e_0) gives seven drivers with delays q, q - 2, 1, q, 2, 1, q from phase 1, reference debt 4q - 31/2 (the
     final prefix, all prefixes nonnegative), one-transfer allowance 5q - 33/2, a saving of 2q - 7/2 against the
     separate 7q - 20, and still above 3q - 8. The terminal window alone has delays q, q, debt 2q - 5, allowance 3q -
     6, below the containing 4q - 11 for q >= 8; at q = 4 the group needs 6.
"""
import random
from fractions import Fraction as F
from itertools import product

fails = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
    if not ok:
        fails.append(name)


R30 = lambda l, c, r: l ^ (c | r)
rng = random.Random(99)
ok = True
for N in range(1, 6):
    nodes = [(i, k) for k in range(1, N + 1) for i in range(-(N - k), N - k + 1)]
    for s in range(2 ** (2 * N + 1)):
        x0 = {i: (s >> (i + N)) & 1 for i in range(-N, N + 1)}
        sync = {(i, 0): x0[i] for i in x0}
        for k in range(1, N + 1):
            for i in range(-(N - k), N - k + 1):
                sync[(i, k)] = R30(sync[(i - 1, k - 1)], sync[(i, k - 1)], sync[(i + 1, k - 1)])
        for order in ('generation', 'largest-site', 'random'):
            store = {(i, 0): x0[i] for i in x0}
            todo = set(nodes)
            while todo:
                ready = [n for n in todo if all((n[0] + d, n[1] - 1) in store for d in (-1, 0, 1))]
                if order == 'generation':
                    n = min(ready, key=lambda q: (q[1], q[0]))
                elif order == 'largest-site':
                    n = max(ready, key=lambda q: (q[0], -q[1]))
                else:
                    n = rng.choice(ready)
                i, k = n
                store[n] = R30(store[(i - 1, k - 1)], store[(i, k - 1)], store[(i + 1, k - 1)])
                todo.remove(n)
            ok &= all(store[n] == sync[n] for n in nodes)
seed = {1}
latest = {i: int(i in seed) for i in range(-3, 4)}
latest[0] = R30(0, 0, 1)
proj = {i for i, v in latest.items() if v}
full = {i for i in range(-3, 4) if R30(int(i - 1 in seed), int(i in seed), int(i + 1 in seed))}
check('S1 three ready orders give the synchronous triangle (N <= 5, every word); mixed projection {0,1} vs {0,1,2}',
      ok and proj == {0, 1} and full == {0, 1, 2}, '%s %s' % (sorted(proj), sorted(full)))
cH, cL = [0] * 8, [0] * 8
for s in range(128):
    x = [(s >> i) & 1 for i in range(7)]
    z, B = x[:], []
    for t in range(3):
        B.append(z[1] | z[2])
        z = [z[j] ^ (z[j + 1] | z[j + 2]) for j in range(len(z) - 2)]
    cH[B[0] * 4 + B[1] * 2 + B[2]] += 1
    rows = [{i: x[i] for i in range(7)}]
    for t in range(3):
        p = rows[-1]
        rows.append({i: R30(p[i - 1], p[i], p[i + 1]) for i in p if i - 1 in p and i + 1 in p})
    Bl = [rows[t + 1][t + 1] ^ rows[t][t] for t in range(3)]
    cL[Bl[0] * 4 + Bl[1] * 2 + Bl[2]] += 1
P = lambda w: F(cH[w], 128)
m = [sum(P(w) for w in range(8) if (w >> (2 - k)) & 1) for k in range(3)]
c01 = sum(P(w) for w in range(8) if (w >> 2) & 1 and (w >> 1) & 1) - m[0] * m[1]
c02 = sum(P(w) for w in range(8) if (w >> 2) & 1 and w & 1) - m[0] * m[2]
var = sum(P(w) * bin(w).count('1') ** 2 for w in range(8)) - sum(P(w) * bin(w).count('1') for w in range(8)) ** 2
check('S2 counts, marginals 3/4, cov 0 and 1/32, variance 5/8 (not 9/16); H agrees with literal spacetime',
      [c // 2 for c in cH] == [1, 3, 5, 7, 3, 9, 7, 29] and cH == cL and m == [F(3, 4)] * 3 and c01 == 0
      and c02 == F(1, 32) and var == F(5, 8) and var != F(9, 16), str([c // 2 for c in cH]))
hist = {}
for s_ in range(512):
    x = {i - 1: (s_ >> i) & 1 for i in range(9)}
    rows = [x]
    for t in range(4):
        q = rows[-1]
        rows.append({i: R30(q[i - 1], q[i], q[i + 1]) for i in q if i - 1 in q and i + 1 in q})
    pos = [(3 * t) // 4 for t in range(5)]
    B = tuple(rows[t + 1][pos[t + 1]] ^ rows[t][pos[t]] for t in range(4))
    hist[B] = hist.get(B, 0) + 1
Pw = lambda w: F(hist.get(w, 0), 512)
words = [tuple((v >> (3 - k)) & 1 for k in range(4)) for v in range(16)]
mean = [sum(Pw(w) * w[k] for w in words) for k in range(4)]
cov = {(a, b): sum(Pw(w) * w[a] * w[b] for w in words) - mean[a] * mean[b] for a in range(4) for b in range(a + 1, 4)}
cm = sum(Pw(w) * sum(w) for w in words)
cv = sum(Pw(w) * sum(w) ** 2 for w in words) - cm ** 2
tri = [1, 3, 5, 7, 3, 9, 7, 29]
ok3 = all(hist.get((b0,) + tuple((v >> (2 - k)) & 1 for k in range(3)), 0) == 4 * tri[v] for b0 in (0, 1) for v in range(8))
check('S3 G101: histogram 4 x G100 triple for each first flip; means; covariances; count mean 11/4, variance 7/8',
      ok3 and mean == [F(1, 2)] + [F(3, 4)] * 3 and cov[(1, 3)] == F(1, 32)
      and all(v == 0 for k, v in cov.items() if k != (1, 3)) and cm == F(11, 4) and cv == F(7, 8) and cv != F(13, 16),
      'variance %s' % cv)
row = {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, -1: 0}
sync = {i: R30(row.get(i - 1, 0), row[i], row.get(i + 1, 0)) for i in range(0, 4)}
new = {}
for i in (3, 2):
    new[i] = R30(row.get(i - 1, 0), row[i], row.get(i + 1, 0))
new[1] = R30(row[0], row[1], new[2])          # right race at site 1 reads the new site 2
new[0] = R30(row[-1], row[0], new[1])         # right race at site 0 reads the raced site 1
iso0 = (1 - row[0]) & (sync[1] ^ row[1])      # isolated injection at site 0: NOT x_0 AND (synchronous change of site 1)
check('S4 G092: chained right races make site 0 differ though its isolated injection is 0',
      new[0] != sync[0] and iso0 == 0, 'sync %d raced %d' % (sync[0], new[0]))
def chain(D, eps, side):
    """Exact injection probability at site 0 under a forced race, D neighbour flags, as a Fraction."""
    tot = F(0)
    n = D + 4                                     # old sites -(D+2) .. (D+2) suffice for both sides
    sites = list(range(-(D + 2), D + 3))
    for w in range(2 ** len(sites)):
        old = {sites[k]: (w >> k) & 1 for k in range(len(sites))}
        for fl in range(2 ** D):
            flags = [(fl >> k) & 1 for k in range(D)]
            weight = F(1)
            for f_ in flags:
                weight *= eps if f_ else 1 - eps
            new = {}
            if side == 'R':
                # site D+1 synchronous; sites D..1 race if flagged (read the new right neighbour); site 0 forced race
                new[D + 1] = R30(old[D], old[D + 1], old[D + 2])
                for i in range(D, 0, -1):
                    rr = new[i + 1] if flags[i - 1] else old[i + 1]
                    new[i] = R30(old[i - 1], old[i], rr)
                raced = R30(old[-1], old[0], new[1])
            else:
                new[-(D + 1)] = R30(old[-(D + 2)], old[-(D + 1)], old[-D])
                for i in range(-D, 0):
                    ll = new[i - 1] if flags[-i - 1] else old[i - 1]
                    new[i] = R30(ll, old[i], old[i + 1])
                raced = R30(new[-1], old[0], old[1])
            sync = R30(old[-1], old[0], old[1])
            tot += weight * (raced != sync)
    return tot / 2 ** len(sites)


ok5 = True
for eps in (F(0), F(1, 100), F(1, 4), F(1, 2), F(1)):
    Q = F(1, 2)
    for D in range(0, 6):
        if D > 0:
            Q = F(1, 2) + eps / 2 * Q
        r_, l_ = chain(D, eps, 'R'), chain(D, eps, 'L')
        lim = 1 / (8 - 4 * eps)
        ok5 &= r_ == Q / 4 and lim - r_ == (eps / 2) ** (D + 1) / (4 * (2 - eps)) and l_ == F(1, 2)
check('S5 G102: right chain Q_D/4 with the stated remainder; left 1/2 (D <= 5; eps = 0, 1/100, 1/4, 1/2, 1)', ok5,
      'q at eps = 1/100: %.5f' % float(1 / (8 - 4 * F(1, 100))))
def race_step(row, flags, mode):
    W_ = len(row)
    new = [0] * W_
    order = range(W_) if mode == 'L' else range(W_ - 1, -1, -1)
    for i in order:
        l = row[(i - 1) % W_]
        r = row[(i + 1) % W_]
        if flags[i] and mode == 'L' and i > 0:
            l = new[i - 1]
        if flags[i] and mode == 'R' and i < W_ - 1:
            r = new[i + 1]
        new[i] = R30(l, row[i], r)
    return new


def ideal_step(row):
    W_ = len(row)
    return [R30(row[(i - 1) % W_], row[i], row[(i + 1) % W_]) for i in range(W_)]


ok6 = True
for W_ in range(3, 6):
    for T_ in (1, 2):
        cones = {}
        for i in range(W_):
            cone = set()
            for s_ in range(1, T_ + 1):
                for d in range(-(T_ - s_), T_ - s_ + 1):
                    cone.add(((i + d) % W_, s_))
            cones[i] = cone
        for mode in 'LR':
            prob = {e: [F(0)] * W_ for e in (F(1, 4), F(1, 2), F(1))}
            for r0 in range(2 ** W_):
                row0 = [(r0 >> k) & 1 for k in range(W_)]
                ideal = row0
                for _ in range(T_):
                    ideal = ideal_step(ideal)
                for fh in range(2 ** (W_ * T_)):
                    flags = [[(fh >> (s_ * W_ + k)) & 1 for k in range(W_)] for s_ in range(T_)]
                    row = row0
                    for s_ in range(T_):
                        row = race_step(row, flags[s_], mode)
                    nf = bin(fh).count('1')
                    for i in range(W_):
                        clean = all(not flags[s_ - 1][j] for (j, s_) in cones[i])
                        if clean and row[i] != ideal[i]:
                            ok6 = False
                        if row[i] != ideal[i]:
                            for e in prob:
                                prob[e][i] += e ** nf * (1 - e) ** (W_ * T_ - nf) / 2 ** W_
            for e in prob:
                for i in range(W_):
                    M = len(cones[i])
                    ok6 &= prob[e][i] <= 1 - (1 - e) ** M and prob[e][i] <= min(1, e * T_ ** 2)
row = [0, 0, 1, 0, 0]
r1 = race_step(row, [1, 0, 0, 0, 0], 'R')
r2 = race_step(r1, [0] * 5, 'R')
i2 = ideal_step(ideal_step(row))
check('S6 G103: clean cones agree; disagreement within both bounds (rings 3..5, T <= 2, both directions); final-tick '
      'guard', ok6 and r1 == [1, 1, 1, 1, 0] and r2[1] != i2[1], 'raced step 1 %s' % r1)
ok7 = True
for w in range(1, 6):
    for fl in range(2 ** w):
        r = {i: (fl >> (i - 1)) & 1 for i in range(1, w + 1)}
        for tail in range(8):
            tx = {w: tail & 1, w + 1: (tail >> 1) & 1, w + 2: (tail >> 2) & 1}
            outs = set()
            for ob in range(2 ** w):
                x = dict(tx)
                for i in range(w):
                    x[i] = (ob >> i) & 1
                y = {w + 1: R30(x[w], x[w + 1], x[w + 2])}
                for i in range(w, 0, -1):
                    y[i] = R30(x[i - 1], x[i], y[i + 1] if r[i] else x[i + 1])
                outs.add(tuple(y[i] for i in range(1, w + 1)))
            ok7 &= len(outs) == 2 ** w
lefts = {}
for D in range(0, 4):
    # sites -(D+1) .. 3 old; target pair (1, 2); flags at sites 1-D .. 2 (site 2 is the pair's right cell)
    sites = list(range(-(D + 1), 4))
    flag_sites = list(range(1 - D, 3))
    for e in (F(0), F(1, 4), F(1, 2), F(1)):
        dens = F(0)
        dis = F(0)
        for xw in range(2 ** len(sites)):
            x = {sites[k]: (xw >> k) & 1 for k in range(len(sites))}
            for fw in range(2 ** len(flag_sites)):
                r = {flag_sites[k]: (fw >> k) & 1 for k in range(len(flag_sites))}
                r[1 - D] = 0                         # anchor: the chain's leftmost site reads an old bit
                nf = sum(r[k] for k in flag_sites)
                wt = e ** nf * (1 - e) ** (len(flag_sites) - 1 - nf) if True else 0
                if (fw & 1):                          # anchored site forced unflagged: skip the flagged half
                    continue
                y = {}
                for i in range(1 - D, 3):
                    y[i] = R30(y[i - 1] if r[i] and (i - 1) in y else x[i - 1], x[i], x[i + 1])
                dens += wt * y[1]
                dis += wt * (y[1] ^ y[2])
        tot = 2 ** len(sites)
        lefts[(D, e)] = (dens / tot, dis / tot)
ok7 &= all(v[0] == F(1, 2) and v[1] == F(1, 2) + e / 4 for (D, e), v in lefts.items() if D >= 1)
check('S7 G104: right-reading block bijection (widths <= 5); left first-row density 1/2, pairs 1/2 + eps/4', ok7,
      'depth 3: %s' % {str(e): str(lefts[(3, e)][1]) for e in (F(0), F(1, 4), F(1, 2), F(1))})
ok8 = True
for W_ in range(3, 8):
    for mode in 'LR':
        mass = {e: F(0) for e in (F(0), F(1, 4), F(1, 2), F(1))}
        for fw in range(2 ** W_):
            flags = [(fw >> k) & 1 for k in range(W_)]
            eff = any(flags[1:]) if mode == 'L' else any(flags[:W_ - 1])
            pre = sum(1 for r0 in range(2 ** W_) if not any(race_step([(r0 >> k) & 1 for k in range(W_)], flags, mode)))
            want = 2 if mode == 'R' else (1 if eff else 2)
            ok8 &= pre == want and not any(race_step([0] * W_, flags, mode))
            nf = sum(flags)
            for e in mass:
                mass[e] += e ** nf * (1 - e) ** (W_ - nf) * F(pre, 2 ** W_)
        for e in mass:
            ok8 &= mass[e] == (F(2, 2 ** W_) if mode == 'R' else (1 + (1 - e) ** (W_ - 1)) / 2 ** W_)
check('S8 G105: zero-row preimages 2 (right), 1 or 2 (left); exact masses; the zero row stays zero (rings 3..7)', ok8)
ok9 = True
for D in range(0, 5):
    sites = list(range(-2, D + 3))
    fsites = list(range(-1, D + 1))
    for e in (F(0), F(1, 4), F(1, 2), F(1)):
        mean = {-1: F(0), 0: F(0), 1: F(0)}
        for xw in range(2 ** len(sites)):
            x = {sites[k]: (xw >> k) & 1 for k in range(len(sites))}
            for fw in range(2 ** len(fsites)):
                r = {fsites[k]: (fw >> k) & 1 for k in range(len(fsites))}
                nf = sum(r.values())
                wt = e ** nf * (1 - e) ** (len(fsites) - nf)
                y = {D + 1: R30(x[D], x[D + 1], x[D + 2])}
                for i in range(D, -2, -1):
                    y[i] = R30(x[i - 1], x[i], y[i + 1] if r[i] else x[i + 1])
                for d in (-1, 0, 1):
                    mean[d] += wt * (x[0] ^ y[d])
        tot = 2 ** len(sites)
        U = F(3, 4)
        for _ in range(D):
            U = F(3, 4) - e / 4 + e / 2 * U
        lim = (3 - e) / (4 - 2 * e)
        ok9 &= mean[-1] / tot == F(1, 2) and mean[0] / tot == F(1, 2) and mean[1] / tot == U
        ok9 &= lim - U == e / (8 - 4 * e) * (e / 2) ** D
check('S9 G106: flip means 1/2, 1/2 and U_D with the stated remainder (D <= 4; eps = 0, 1/4, 1/2, 1)', ok9,
      'eps = 1/2 limit %s' % ((3 - F(1, 2)) / (4 - 2 * F(1, 2))))
ok10 = True
for T_ in range(1, 4):
    lo0, hi0 = -2 * T_, T_ + 1
    nb = hi0 - lo0 + 1
    for path in product((-1, 0), repeat=T_):
        pos = [0]
        for d in path:
            pos.append(pos[-1] + d)
        for sched in product((0, 1), repeat=T_):
            cnt = {}
            for w in range(2 ** nb):
                row = {lo0 + k: (w >> k) & 1 for k in range(nb)}
                lo, hi = lo0, hi0
                samp = [row[0]]
                for t in range(T_):
                    new = {}
                    new[hi - 1] = R30(row[hi - 2], row[hi - 1], row[hi])
                    for i in range(hi - 2, lo, -1):
                        rr = new[i + 1] if sched[t] else row[i + 1]
                        new[i] = R30(row[i - 1], row[i], rr)
                    row, lo, hi = new, lo + 1, hi - 1
                    samp.append(row[pos[t + 1]])
                cnt[tuple(samp)] = cnt.get(tuple(samp), 0) + 1
            ok10 &= len(cnt) == 2 ** (T_ + 1) and len(set(cnt.values())) == 1
check('S10 G107: nonincreasing traces uniform under every whole-row race schedule (T <= 3)', ok10)
def trace(row0, lo0, hi0, pos, sched):
    row, lo, hi = dict(row0), lo0, hi0
    out = [row[pos[0]]]
    for t in range(len(sched)):
        new = {hi - 1: R30(row[hi - 2], row[hi - 1], row[hi])}
        for i in range(hi - 2, lo, -1):
            new[i] = R30(row[i - 1], row[i], new[i + 1] if sched[t] else row[i + 1])
        row, lo, hi = new, lo + 1, hi - 1
        out.append(row[pos[t + 1]])
    return out


ok11 = True
for T_ in range(1, 4):
    lo0, hi0 = -2 * T_, T_ + 1
    for path in product((-1, 0), repeat=T_):
        pos = [0]
        for d in path:
            pos.append(pos[-1] + d)
        piv = [pos[t] - t for t in range(T_ + 1)]
        others = [i for i in range(lo0, hi0 + 1) if i not in piv]
        for sched in product((0, 1), repeat=T_):
            for rw in range(2 ** len(others)):
                base = {others[k]: (rw >> k) & 1 for k in range(len(others))}
                Is, Js, mask = set(), set(), {}
                for pw in range(2 ** (T_ + 1)):
                    row = dict(base)
                    for k in range(T_ + 1):
                        row[piv[k]] = (pw >> k) & 1
                    I = trace(row, lo0, hi0, pos, (0,) * T_)
                    J = trace(row, lo0, hi0, pos, sched)
                    Is.add(tuple(I))
                    Js.add(tuple(J))
                    for t in range(T_ + 1):
                        key = (t, tuple(I[:t]))
                        e = I[t] ^ J[t]
                        if mask.setdefault(key, e) != e:
                            ok11 = False
                ok11 &= len(Is) == 2 ** (T_ + 1) and len(Js) == 2 ** (T_ + 1)
g_ok = True
for xm1 in (0, 1):
    for x0 in (0, 1):
        x = {-1: xm1, 0: x0, 1: 0, 2: 1, -2: 0, 3: 0}
        I1 = R30(x[-1], x[0], x[1])
        y1 = R30(x[0], x[1], x[2])
        J1 = R30(x[-1], x[0], y1)
        g_ok &= (I1 ^ J1) == 1 - x0
check('S11 G108: both traces bijective in the pivots, the mask causal in the ideal prefix (T <= 3); E_1 = 1 - I_0',
      ok11 and g_ok)
def diff_step(z, d, lo, hi):
    """Synchronous step of a background z and its difference d, by the difference of the OR term."""
    nz, nd = {}, {}
    for i in range(lo + 1, hi):
        nz[i] = R30(z[i - 1], z[i], z[i + 1])
        orz = z[i] | z[i + 1]
        orw = (z[i] ^ d[i]) | (z[i + 1] ^ d[i + 1])
        nd[i] = d[i - 1] ^ orz ^ orw
    return nz, nd


ok12 = True
for w in range(2 ** 7):
    z = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    d = {i: int(i == 0) for i in range(-3, 4)}
    z1, d1 = diff_step(z, d, -3, 3)
    z2, d2 = diff_step(z1, d1, -2, 2)
    ok12 &= (d[0], d1[0], d2[0]) == (1, 1 - z[1], z[1] | z[2])
    ok12 &= d1[-1] == 1 - z[-1] and d1[1] == 1
inj = 0
sets = {}
for w in range(2 ** 7):
    x = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    ideal1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    raced1 = dict(ideal1)
    raced1[0] = R30(x[-1], x[0], ideal1[1])        # site 1 synchronous, already computed; only site 0 races
    def sync(r, lo, hi):
        return {i: R30(r[i - 1], r[i], r[i + 1]) for i in range(lo, hi + 1)}
    i2, r2 = sync(ideal1, -1, 1), sync(raced1, -1, 1)
    i3, r3 = sync(i2, 0, 0), sync(r2, 0, 0)
    sig = (ideal1[0] ^ raced1[0], i2[0] ^ r2[0], i3[0] ^ r3[0])
    if sig[0]:
        inj += 1
        ok12 &= sig == (1, 0, 1)
        dset = tuple(i for i in (-1, 0, 1) if i2[i] != r2[i])
        sets[dset] = sets.get(dset, 0) + 1
    else:
        ok12 &= sig == (0, 0, 0)
check('S12 G109: single-flip kernel by XOR-difference propagation; 16 injections, all 1, 0, 1; damage sets',
      ok12 and inj == 16 and sets == {(1,): 8, (-1, 1): 8}, 'injections %d, sets %s' % (inj, sets))
bins = {}
hI, hJ = {}, {}
ok13 = True
for w in range(2 ** 7):
    x = {i: (w >> (i + 3)) & 1 for i in range(-3, 4)}
    ideal1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    raced1 = dict(ideal1)
    raced1[0] = R30(x[-1], x[0], ideal1[1])
    def sync(r, lo, hi):
        return {i: R30(r[i - 1], r[i], r[i + 1]) for i in range(lo, hi + 1)}
    i2, r2 = sync(ideal1, -1, 1), sync(raced1, -1, 1)
    i3, r3 = sync(i2, 0, 0), sync(r2, 0, 0)
    I = (x[0], ideal1[0], i2[0], i3[0])
    J = (x[0], raced1[0], r2[0], r3[0])
    E = tuple(a ^ b for a, b in zip(I, J))
    ok13 &= E[2] == 0 and E[3] == E[1]
    key = (I[2], E[2], E[1])
    bins[key] = bins.get(key, 0) + 1
    hI[I] = hI.get(I, 0) + 1
    hJ[J] = hJ.get(J, 0) + 1
ok13 &= all(bins.get((b, 0, 1), 0) == 8 and bins.get((b, 0, 0), 0) == 56 for b in (0, 1))
ok13 &= len(hI) == 16 and set(hI.values()) == {8} and len(hJ) == 16 and set(hJ.values()) == {8}
check('S13 G110: bins 8 and 56 per ideal bit, E_3 = E_1, both traces uniform', ok13, str(sorted(bins.items())))
ok14 = True
for W_ in range(3, 7):
    for r0 in range(2 ** W_):
        x = [(r0 >> k) & 1 for k in range(W_)]
        z = ideal_step(x)
        for fw in range(2 ** W_):
            fl = [(fw >> k) & 1 for k in range(W_)]
            y = race_step(x, fl, 'R')
            for j in range(W_):
                j1 = (j + 1) % W_
                if z[j1] == 0 and y[j1] == 0 and z[j] != y[j]:
                    ok14 = False


def line_cyl(word, flag_t1_site0):
    x = {i - 3: int(word[i]) for i in range(7)}
    z1 = {i: R30(x[i - 1], x[i], x[i + 1]) for i in range(-2, 3)}
    y1 = {}
    for i in range(2, -3, -1):                     # right-to-left scan on the cone's tick-1 nodes
        rr = y1[i + 1] if (i == 0 and flag_t1_site0) else x[i + 1]
        y1[i] = R30(x[i - 1], x[i], rr)
    z2 = {i: R30(z1[i - 1], z1[i], z1[i + 1]) for i in range(-1, 2)}
    y2 = {i: R30(y1[i - 1], y1[i], y1[i + 1]) for i in range(-1, 2)}
    z3 = R30(z2[-1], z2[0], z2[1])
    y3 = R30(y2[-1], y2[0], y2[1])
    return (x[0], z1[0], z2[0], z3), (x[0], y1[0], y2[0], y3)


I_, J_ = line_cyl('0110000', False)
E_ = [a ^ b for a, b in zip(I_, J_)]
ok14 &= I_[1] == 1 and I_[2] == 1 and E_[1] == 0 and E_[2] == 0 and E_[3] == 0
I_, J_ = line_cyl('0000010', True)
E_ = [a ^ b for a, b in zip(I_, J_)]
ok14 &= I_ == (0, 0, 1, 1) and J_ == (0, 1, 1, 0) and I_[2] == 1 and E_[2] == 0 and E_[3] == 1
x5 = [0, 0, 0, 0, 1]
z5 = ideal_step(x5)
y5 = race_step(x5, [0, 1, 0, 0, 0], 'L')
ok14 &= z5[2] == 0 and y5[2] == 0 and z5[1] != y5[1]
check('S14 G112: white agreement (rings 3..6, right scan); both cylinders; the left-scan guard', ok14)
cntA = sA = cntB = sB = cntC = sC = 0
hI7, hJ7 = {}, {}
for w in range(2 ** 13):
    x = {i: (w >> (i + 6)) & 1 for i in range(-6, 7)}
    zr = dict(x)
    yr = dict(x)
    I7, J7 = [x[0]], [x[0]]
    for t in range(1, 7):
        lo, hi = -6 + t, 6 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
            ny[0] = R30(yr[-1], yr[0], ny[1])           # the pulse: site 0 reads its updated right neighbour
        else:
            ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        zr, yr = nz, ny
        I7.append(zr[0])
        J7.append(yr[0])
    E7 = [a ^ b for a, b in zip(I7, J7)]
    K = [(I7[t], E7[t]) for t in range(7)]
    hI7[tuple(I7)] = hI7.get(tuple(I7), 0) + 1
    hJ7[tuple(J7)] = hJ7.get(tuple(J7), 0) + 1
    if K[4] == (0, 0) and K[5] == (0, 0):
        cntA += 1
        sA += E7[6]
        if K[3] == (0, 0):
            cntB += 1
            sB += E7[6]
        if K[3] == (0, 1):
            cntC += 1
            sC += E7[6]
check('S15 G113: A 1872 with 40, B 896 with 0, child (0,1) 40 with 20; traces uniform',
      (cntA, sA, cntB, sB, cntC, sC) == (1872, 40, 896, 0, 40, 20) and len(hI7) == 128 and set(hI7.values()) == {64}
      and len(hJ7) == 128 and set(hJ7.values()) == {64}, str((cntA, sA, cntB, sB, cntC, sC)))
ok16 = True
for a_, b_, c_, p_, q_, r_ in product((0, 1), repeat=6):
    lit = R30(a_, b_, c_) ^ R30(a_ ^ p_, b_ ^ q_, c_ ^ r_)
    ok16 &= lit == p_ ^ ((1 - c_) & q_) ^ ((1 - b_) & r_) ^ (q_ & r_)
word = '0011110010000'
x = {i - 6: int(word[i]) for i in range(13)}
zr, yr = dict(x), dict(x)
rows = {}
for t in range(1, 6):
    lo, hi = -6 + t, 6 - t
    nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
    ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
    if t == 1:
        ny[0] = R30(yr[-1], yr[0], ny[1])
    zr, yr = nz, ny
    rows[t] = (zr, yr)
sl = lambda r_, lo, hi: ''.join(str(r_[i]) for i in range(lo, hi + 1))
ok16 &= (sl(rows[3][0], -3, 3), sl(rows[3][1], -3, 3)) == ('1010101', '1111011')
ok16 &= (sl(rows[4][0], -2, 2), sl(rows[4][1], -2, 2)) == ('01010', '00001')
ok16 &= (sl(rows[5][0], -1, 1), sl(rows[5][1], -1, 1)) == ('101', '001')
e4 = (rows[4][0][-1] ^ rows[4][1][-1], rows[4][0][1] ^ rows[4][1][1])
e5 = (rows[5][0][-1] ^ rows[5][1][-1], rows[5][0][1] ^ rows[5][1][1])
ok16 &= e4 == (1, 1) and e5 == (1, 0)
ok16 &= (0 ^ ((1 - 0) & 0) ^ ((1 - 1) & 1) ^ (0 & 1)) == 0 and (0 ^ 1) == 1
check('S16 G114: expanded identity on 64 triples; the cylinder rows; incoming errors (1,1), (1,0); black guard', ok16)
par, full, k3 = {}, {}, {}
ok17 = True
inj = e4s = 0
bins23 = {}
for w in range(2 ** 13):
    x = {i: (w >> (i + 6)) & 1 for i in range(-6, 7)}
    zr, yr = dict(x), dict(x)
    I7, J7 = [x[0]], [x[0]]
    for t in range(1, 7):
        lo, hi = -6 + t, 6 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        I7.append(zr[0])
        J7.append(yr[0])
    E7 = [a ^ b for a, b in zip(I7, J7)]
    K = tuple((I7[t], E7[t]) for t in range(7))
    Fi = E7[1]
    ok17 &= E7[4] == Fi * (I7[1] ^ I7[2] ^ I7[3])
    if Fi:
        inj += 1
        e4s += E7[4]
        b = bins23.setdefault((I7[2], I7[3]), [0, 0])
        b[0] += 1
        b[1] += E7[4]
    X = (Fi, K[4], K[5])
    for d, key in ((par, X), (full, (X, K[:6])), (k3, (X, K[3]))):
        v = d.setdefault(key, [0, 0])
        v[0] += 1
        v[1] += E7[6]
ok17 &= par[(1, (0, 0), (0, 0))] == [80, 40]
Hz = ((0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 0))
ok17 &= full[((1, (0, 0), (0, 0)), Hz)] == [20, 0]
uneq = sum(1 for (X, H), (n, e) in full.items() if e * par[X][0] != par[X][1] * n)
uneq3 = sum(1 for (X, k), (n, e) in k3.items() if e * par[X][0] != par[X][1] * n)
ok17 &= uneq == 24 and len(full) == 112 and len(par) == 18 and uneq3 == 0
ok17 &= inj == 64 * 16 and e4s == 32 * 16 and all(v == [256, 128] for v in bins23.values()) and len(bins23) == 4   # 8,192 words = 16 x G116's 512
check('S17 G115, G116: candidate witness 80/40 vs 20/0; 24 of 112 full-history splits, none from K_3; E_4 parity law',
      ok17, 'full splits %d of %d (parents %d), K_3 splits %d; injections %d, fourth errors %d' % (
          uneq, len(full), len(par), uneq3, inj, e4s))
ok18 = True
inj18 = e5s = 0
quad = {}
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    I6, J6 = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        I6.append(zr[0])
        J6.append(yr[0])
    E6 = [u ^ v for u, v in zip(I6, J6)]
    Fi = E6[1]
    if not Fi:
        ok18 &= E6[5] == 0
        continue
    inj18 += 1
    e5s += E6[5]
    a_, b_, c_, d_ = I6[1], I6[2], I6[3], I6[4]
    Dh = x[3] & (x[4] | x[5])
    H_ = a_ ^ b_ ^ c_
    L_ = 1 ^ ((1 - b_) & (d_ ^ (c_ | (1 ^ a_ ^ b_))))
    R_ = b_ ^ Dh
    C_ = c_ ^ ((1 ^ a_ ^ b_) | (1 ^ a_ ^ Dh))
    form = L_ ^ ((1 - C_) & H_) ^ ((1 - d_) & R_) ^ (H_ & R_)
    ok18 &= E6[5] == form
    q = quad.setdefault((a_, b_, c_, d_), [0, 0, 0])
    q[0] += 1
    q[1] += Dh
    q[2] += E6[5]
    if (a_, b_, c_, d_) == (0, 0, 0, 0):
        ok18 &= E6[5] == Dh
hist = {}
for v in quad.values():
    hist[v[2]] = hist.get(v[2], 0) + 1
ok18 &= inj18 == 256 and e5s == 152 and len(quad) == 16 and all(v[0] == 16 and v[1] == 6 for v in quad.values())
ok18 &= hist == {0: 2, 16: 6, 6: 6, 10: 2}
check('S18 G117: fifth-error formula on every injected word; 256 injections, 152 errors; D-split; histogram', ok18,
      'injections %d, errors %d, histogram %s' % (inj18, e5s, dict(sorted(hist.items()))))
import math
joint, mA, mB, injA = {}, {}, {}, {}
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    A_, B_ = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        A_.append(zr[0])
        B_.append(yr[0])
    A_, B_ = tuple(A_), tuple(B_)
    joint[(A_, B_)] = joint.get((A_, B_), 0) + 1
    mA[A_] = mA.get(A_, 0) + 1
    mB[B_] = mB.get(B_, 0) + 1
    ia = injA.setdefault(A_, [0, 0])
    ia[0] += 1
    ia[1] += A_[1] ^ B_[1]
jh = {}
for v in joint.values():
    jh[v] = jh.get(v, 0) + 1
Hn = lambda counts: -sum(c / 2048 * math.log2(c / 2048) for c in counts)
HAB = Hn(joint.values())
HA, HB = Hn(mA.values()), Hn(mB.values())
h2 = lambda q: -q * math.log2(q) - (1 - q) * math.log2(1 - q)
ok19 = len(mA) == 64 and set(mA.values()) == {32} and len(mB) == 64 and set(mB.values()) == {32}
ok19 &= jh == {32: 32, 24: 32, 8: 16, 5: 16, 3: 16} and len(joint) == 112
ok19 &= all(v[1] == (8 if a[0] == 0 else 0) for a, v in injA.items())
ok19 &= abs(HAB - (6 + h2(0.25) / 2 + h2(0.375) / 16)) < 1e-12 and abs((HA + HB - HAB) - (6 - h2(0.25) / 2 - h2(0.375) / 16)) < 1e-12
check('S19 G118: marginals, joint histogram, injections by I_0, H(A,B) and MI', ok19,
      'MI = %.6f bits' % (HA + HB - HAB))
def H_counts(counter, total):
    return -sum(c / total * math.log2(c / total) for c in counter.values() if c)


def prefix_MI(samples, t):
    """samples: list of (I tuple, J tuple), equally weighted. MI between prefixes of length t + 1."""
    n = len(samples)
    from collections import Counter
    cA = Counter(I[:t + 1] for I, J in samples)
    cB = Counter(J[:t + 1] for I, J in samples)
    cAB = Counter((I[:t + 1], J[:t + 1]) for I, J in samples)
    return H_counts(cA, n) + H_counts(cB, n) - H_counts(cAB, n)


def cond_err_entropy(samples, t):
    """H(E_t | K_0..K_(t-1)) from counts."""
    from collections import Counter
    n = len(samples)
    past = Counter((tuple(zip(I[:t], J[:t]))) for I, J in samples)
    joint = Counter((tuple(zip(I[:t], J[:t])), I[t] ^ J[t]) for I, J in samples)
    return H_counts(joint, n) - H_counts(past, n)


pulse = []
for w in range(2 ** 11):
    x = {i: (w >> (i + 5)) & 1 for i in range(-5, 6)}
    zr, yr = dict(x), dict(x)
    A_, B_ = [x[0]], [x[0]]
    for t in range(1, 6):
        lo, hi = -5 + t, 5 - t
        nz = {i: R30(zr[i - 1], zr[i], zr[i + 1]) for i in range(lo, hi + 1)}
        ny = {i: R30(yr[i - 1], yr[i], yr[i + 1]) for i in range(lo, hi + 1)}
        if t == 1:
            ny[0] = R30(yr[-1], yr[0], ny[1])
        zr, yr = nz, ny
        A_.append(zr[0])
        B_.append(yr[0])
    pulse.append((tuple(A_), tuple(B_)))
ok20 = True
acc = 0.0
for t in range(6):
    acc += cond_err_entropy(pulse, t)
    ok20 &= abs(prefix_MI(pulse, t) - ((t + 1) - acc)) < 1e-12
toy = []
for b in range(32):
    X0, X1, X2, U, V = [(b >> k) & 1 for k in range(5)]
    Rr = U & V
    toy.append(((X0, X1, X2), (X0, X1 ^ Rr, X2 ^ (Rr & X0))))
ok20 &= abs(prefix_MI(toy, 0) - 1) < 1e-12 and abs(prefix_MI(toy, 1) - (2 - h2(0.25))) < 1e-12
ok20 &= abs(prefix_MI(toy, 2) - (3 - h2(0.25))) < 1e-12
reuse = [((X, Y, Z), (X, Z, Y)) for X in (0, 1) for Y in (0, 1) for Z in (0, 1)]
Ms = [prefix_MI(reuse, t) for t in range(3)]
ok20 &= all(abs(a - b) < 1e-12 for a, b in zip(Ms, (1, 1, 3))) and abs(cond_err_entropy(reuse, 2)) < 1e-12
check('S20 G119: the increment identity on the pulse traces (t <= 5); positive toy; the cross-copy reuse guard', ok20,
      'pulse M_5 = %.6f' % prefix_MI(pulse, 5))
ok21 = True
vals = [cond_err_entropy(pulse, t) for t in range(2, 6)]
ok21 &= all(v <= 0.125 + 1e-12 for v in vals) and abs(vals[3] - h2(0.375) / 16) < 1e-12 and all(abs(v) < 1e-12 for v in vals[:3])
posit = []
for b in range(64):
    X0, X1, X2, U, V, Q = [(b >> k) & 1 for k in range(6)]
    Fv = (1 - X0) & (1 - U) & V
    posit.append(((X0, X1, X2), (X0, X1 ^ Fv, X2 ^ (Fv & Q))))
ok21 &= abs(cond_err_entropy(posit, 2) - 0.125) < 1e-12 and abs((prefix_MI(posit, 2) - prefix_MI(posit, 1)) - 0.875) < 1e-12
hidden = []
for b in range(32):
    X0, X1, U, V, Q = [(b >> k) & 1 for k in range(5)]
    Fv = (1 - X0) & (1 - U) & V
    hidden.append(((X0, X1), (X0, X1 ^ (Fv & Q))))
he = cond_err_entropy(hidden, 1)
ok21 &= abs(he - h2(0.125) / 2) < 1e-12 and he > 0.125
ok21 &= abs((prefix_MI(hidden, 1) - prefix_MI(hidden, 0)) - (1 - he)) < 1e-12
check('S21 G120: pulse error entropies <= 1/8 after t = 1; tight toy 1/8; hidden-event guard h2(1/8)/2', ok21,
      'pulse t = 2..5: %s; hidden %.6f' % (['%.4f' % v for v in vals], he))
def fwd_finite(bits):
    """bits: tuple with bits[0] = bits[-1] = 1 (normalized); image on positions -1..len, normalized."""
    w = len(bits)
    x = lambda i: bits[i] if 0 <= i < w else 0
    out = tuple(R30(x(i - 1), x(i), x(i + 1)) for i in range(-1, w + 1))
    return out


ok22 = True
for w in range(1, 15):
    seen = set()
    for m in range(2 ** max(0, w - 2)):
        mid = tuple((m >> k) & 1 for k in range(w - 2)) if w >= 2 else ()
        word = (1,) + mid + ((1,) if w >= 2 else ())
        img = fwd_finite(word)
        ok22 &= img[0] == 1 and img[-1] == 1 and len(img) == w + 2
        ok22 &= img not in seen
        seen.add(img)
for w in range(4, 17):
    imgs = set()
    for m in range(2 ** (w - 4)):
        mid = tuple((m >> k) & 1 for k in range(w - 4))
        imgs.add(fwd_finite((1,) + mid + (1,)))
    ok22 &= len(imgs) == 2 ** (w - 4)
ok22 &= fwd_finite((1,)) == (1, 1, 1)


def canon_pred(y, lo, hi, depth):
    """Right-quiescent predecessor of y (dict on lo..hi, zero outside), computed down to site lo - depth."""
    x = {hi + 1: 0, hi + 2: 0}
    for i in range(hi + 1, lo - depth, -1):
        x[i - 1] = y.get(i, 0) ^ (x[i] | x[i + 1])
    return x


y0 = {0: 1}
p1 = canon_pred(y0, 0, 0, 40)
tail1 = [p1[i] for i in range(-30, -10)]
ok22 &= all(b == 1 for b in tail1)
ok22 &= all(R30(p1.get(i - 1, 0), p1.get(i, 0), p1.get(i + 1, 0)) == y0.get(i, 0) for i in range(-25, 3))
p2 = {hi: 0 for hi in ()}
x = {3: 0, 4: 0}
for i in range(3, -60, -1):
    yi = p1.get(i, 1 if i < -39 else 0)
    x[i - 1] = yi ^ (x[i] | x[i + 1])
tail2 = [x[i] for i in range(-50, -20)]
per3 = all(tail2[k] == tail2[k + 3] for k in range(len(tail2) - 3)) and sorted(tail2[:3]) == [0, 0, 1]
ok22 &= per3
ok22 &= all(R30(x[i - 1], x[i], x[i + 1]) == p1.get(i, 0) for i in range(-30, 2))
check('S22 G121, G122: span growth and injectivity; root fraction 3/4; canonical tails black then period 3 (001)',
      ok22, 'second tail sample %s' % ''.join(map(str, tail2[:9])))
def least_period(seq):
    n = len(seq)
    for q in range(1, n + 1):
        if n % q == 0 and all(seq[i] == seq[(i + q) % n] for i in range(n)):
            return q
    return n


ok23 = True
allowed = lambda q: q == 1 or (q % 3 == 0 and (q // 3) & ((q // 3) - 1) == 0)
seen_periods = set()
for N in range(1, 17):
    mask = (1 << N) - 1
    nxt = []
    for st in range(1 << N):
        if N == 1:
            nxt.append(R30(st, st, st))
            continue
        l = ((st << 1) | (st >> (N - 1))) & mask
        r = ((st >> 1) | (st << (N - 1))) & mask
        nxt.append((l ^ (st | r)) & mask)
    preds = {}
    for st, t in enumerate(nxt):
        preds.setdefault(t, []).append(st)
    basin, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for v in preds.get(u, []):
            if v not in basin:
                basin.add(v)
                stack.append(v)
    for st in basin:
        q = least_period([(st >> i) & 1 for i in range(N)])
        ok23 &= allowed(q)
        if N == 12:
            seen_periods.add(q)
ok23 &= {3, 6, 12} <= seen_periods
# canonical ancestors of the single cell on a long window
Wn = 6000
lo_w, hi_w = -Wn, 2
cur = {i: 0 for i in range(lo_w, hi_w + 1)}
cur[0] = 1
tails = []
for n in range(1, 13):
    x = {hi_w + 1: 0, hi_w + 2: 0}
    for i in range(hi_w + 1, lo_w, -1):
        x[i - 1] = cur.get(i, 0) ^ (x[i] | x[i + 1])
    seg = [x[i] for i in range(lo_w + 50, lo_w + 50 + 1536)]
    q = None
    for cand in range(1, 769):
        if all(seg[i] == seg[i + cand] for i in range(len(seg) - cand)):
            q = cand
            break
    tails.append(q)
    ok23 &= all(R30(x[i - 1], x[i], x[i + 1]) == cur.get(i, 0) for i in range(lo_w + 2, hi_w))
    cur = {i: x[i] for i in range(lo_w, hi_w + 1)}
import math as _m
ok23 &= tails[0] == 1 and tails[1] == 3 and all(q is not None and allowed(q) for q in tails)
ok23 &= all(tails[k] % tails[k - 1] == 0 for k in range(1, len(tails)))
ok23 &= all(tails[n - 1] >= _m.ceil(_m.log2(n + 1)) for n in range(1, 13))
traj = ['001010', '011011', '010010', '111111', '000000']
for a_, b_ in zip(traj, traj[1:]):
    v = [int(c) for c in a_]
    ok23 &= ''.join(str(R30(v[i - 1], v[i], v[(i + 1) % 6])) for i in range(6)) == b_
ok23 &= [least_period([int(c) for c in t]) for t in traj] == [6, 3, 3, 1, 1]
check('S23 G123, G124: zero-basin periods on rings to 16; canonical tail periods; the period-6 trajectory', ok23,
      'tail periods %s; periods at N = 12 %s' % (tails, sorted(seen_periods)))
def Hmap(a, b):
    """Sideways map on periodic tracks (tuples of equal length L, time index mod L)."""
    L_ = len(a)
    return tuple(a[(t + 1) % L_] ^ (a[t] | b[t]) for t in range(L_)), a


ok24 = True
from math import gcd
for m in range(1, 11):
    mask = (1 << m) - 1
    def ring_step(st):
        if m == 1:
            return R30(st, st, st)
        l = ((st << 1) | (st >> (m - 1))) & mask
        r = ((st >> 1) | (st << (m - 1))) & mask
        return (l ^ (st | r)) & mask
    nxt = [ring_step(st) for st in range(1 << m)]
    # recurrent states: on cycles
    rec = set()
    for st in range(1 << m):
        x = st
        for _ in range(1 << m):
            x = nxt[x]
        rec.add(x)
    # close: collect full cycles
    recurrent = set()
    for st in rec:
        y = nxt[st]
        while y != st:
            recurrent.add(y)
            y = nxt[y]
        recurrent.add(st)
    cyc_len = {}
    for st in recurrent:
        y, k = nxt[st], 1
        while y != st:
            y, k = nxt[y], k + 1
        cyc_len[st] = k
    Lc = 1
    for k in set(cyc_len.values()):
        Lc = Lc * k // gcd(Lc, k)
    pairs = set()
    for st in recurrent:
        rows = [st]
        for _ in range(Lc - 1):
            rows.append(nxt[rows[-1]])
        bit = lambda r_, i: (r_ >> (i % m)) & 1
        a = tuple(bit(r_, 0) for r_ in rows)
        b = tuple(bit(r_, 1) for r_ in rows)
        u, v = a, b
        for _ in range(m):
            u, v = Hmap(u, v)
        ok24 &= (u, v) == (a, b)
        pairs.add((a, b))
    ok24 &= len(pairs) == len(recurrent)
    if m <= 4 and 2 * Lc <= 20:
        cnt = 0
        for wa in range(1 << Lc):
            for wb in range(1 << Lc):
                a = tuple((wa >> t) & 1 for t in range(Lc))
                b = tuple((wb >> t) & 1 for t in range(Lc))
                u, v = a, b
                for _ in range(m):
                    u, v = Hmap(u, v)
                cnt += (u, v) == (a, b)
        ok24 &= cnt == len(recurrent)
ok24 &= Hmap((1,), (1,)) == ((0,), (1,))
check('S24 G125: recurrent ring states give exact H^m fixed pairs (m <= 10); brute-force fixed-point counts (m <= 4)', ok24)
def decode_cyc(code):
    """Ternary code (cyclic tuple) -> pair (X, Y) of H's image: Y = [code = 2], X = code where Y = 0, else 1 - Y(t+1)."""
    L_ = len(code)
    Y = tuple(1 if c == 2 else 0 for c in code)
    X = tuple(code[t] if Y[t] == 0 else 1 - Y[(t + 1) % L_] for t in range(L_))
    return X, Y


def encode(X, Y):
    return tuple(2 if Y[t] else X[t] for t in range(len(X)))


def T_cyc(code):
    X, Y = decode_cyc(code)
    L_ = len(code)
    X2 = tuple(X[(t + 1) % L_] ^ (X[t] | Y[t]) for t in range(L_))
    return encode(X2, X)


FORB = [(1, 0, 0), (1, 0, 1), (1, 1, 2), (0, 2, 1, 0), (0, 2, 1, 1), (0, 2, 0, 2)]
ok25 = True
for w in FORB:
    k = len(w)
    for pre in product((0, 1, 2), repeat=k + 2):
        Y = [1 if c == 2 else 0 for c in pre]
        X = [pre[t] if Y[t] == 0 else (1 - Y[t + 1] if t + 1 < len(pre) else None) for t in range(len(pre))]
        # target code at t: the new second track X(t) marks 2, the new first track is X(t+1) XOR (X(t) OR Y(t))
        tgt = tuple(2 if X[t] == 1 else (X[t + 1] ^ (X[t] | Y[t])) for t in range(k))
        ok25 &= tgt != w
def avoids_cyc(word):
    L_ = len(word)
    ext = word * 8            # long enough that every 4-letter window starting in the middle copy is complete
    return not any(tuple(ext[i:i + len(f)]) == f for f in FORB for i in range(L_, 2 * L_))


def section(z):
    L_ = len(z)
    C = tuple(1 if c == 2 else 0 for c in z)
    D = tuple(z[t] if C[t] == 0 else 1 - C[(t + 1) % L_] for t in range(L_))
    A = tuple((D[t] ^ C[(t + 1) % L_]) if C[t] == 0 else int(z[(t - 1) % L_] == 0) for t in range(L_))
    return tuple(2 if A[t] else C[t] for t in range(L_))


for p_ in range(1, 9):
    images = set(T_cyc(c) for c in product((0, 1, 2), repeat=p_))
    Yset = set(w for w in product((0, 1, 2), repeat=p_) if avoids_cyc(w))
    ok25 &= images == Yset
    ok25 &= all(T_cyc(section(z)) == z for z in Yset)
ok25 &= T_cyc((2, 2, 1, 0)) == (0, 2, 2, 0) and (1, 1, 2) not in set(T_cyc(c) for c in product((0, 1, 2), repeat=3))
check('S25 G126: forbidden windows have no predecessor; periodic images = Y for p <= 8; the local section inverts T', ok25)
def T_window(pre):
    """Precursor code block of length k + 2 -> target block of length k."""
    Yp = [1 if c == 2 else 0 for c in pre]
    Xp = [pre[t] if Yp[t] == 0 else (1 - Yp[t + 1] if t + 1 < len(pre) else None) for t in range(len(pre))]
    return tuple(2 if Xp[t] == 1 else (Xp[t + 1] ^ (Xp[t] | Yp[t])) for t in range(len(pre) - 2))


ok26 = True
per2 = {w: T_cyc(w) for w in [(0, 0), (1, 1), (2, 2), (1, 2), (2, 1)]}
ok26 &= per2 == {(0, 0): (0, 0), (1, 1): (2, 2), (2, 2): (1, 1), (1, 2): (2, 2), (2, 1): (2, 2)}
ok26 &= avoids_cyc((0, 1, 0, 2)) and T_cyc((0, 1, 0, 2)) == (1, 2, 1, 2) and avoids_cyc((1, 2))
pre6 = sorted(''.join(map(str, pre)) for pre in product((0, 1, 2), repeat=8) if T_window(pre) == (0, 2, 2, 0, 0, 0))
ok26 &= pre6 == ['22100000', '22100001', '22100002', '22100022', '22100220', '22100221']
pre6b = [pre for pre in product((0, 1, 2), repeat=8) if T_window(pre) == (0, 2, 2, 0, 0, 1)]
ok26 &= len(pre6b) > 0 and all(pre[:5] == (2, 2, 1, 0, 0) for pre in pre6b)
ok26 &= avoids_cyc((0, 2, 2, 0, 0, 0))
# G128: finite-window realization of every binary trace (left-permutive solving)
for Nw in range(1, 12):
    for wv in range(2 ** Nw):
        target = [(wv >> t) & 1 for t in range(Nw)]
        # unknown initial bits at sites 0, -1, ..., -(Nw-1); all other initial bits zero
        init = {}
        for k in range(Nw):
            # choose x_0(-k) so that the site-0 sample at time k matches
            for guess in (0, 1):
                init[-k] = guess
                row = {i: init.get(i, 0) for i in range(-Nw - 1, Nw + 2)}
                for t in range(k):
                    row = {i: R30(row[i - 1], row[i], row[i + 1]) for i in range(-Nw - 1 + t + 1, Nw + 1 - t)}
                if row[0] == target[k]:
                    break
            else:
                ok26 = False
        row = {i: init.get(i, 0) for i in range(-Nw - 1, Nw + 2)}
        tr = [row[0]]
        for t in range(Nw - 1):
            row = {i: R30(row[i - 1], row[i], row[i + 1]) for i in range(-Nw - 1 + t + 1, Nw + 1 - t)}
            tr.append(row[0])
        ok26 &= tr == target
chk = [0, 1] * 4
ok26 &= [R30(chk[i - 1], chk[i], chk[(i + 1) % 8]) for i in range(8)] == chk
# (a, b) = ((01)^inf, 1^inf) has no H-preimage: H's second output is the first input, which must then be all ones,
# and the first output is then S(ones) XOR (ones OR b') = 0 everywhere. Brute force over period-2 (and period-4) inputs:
for Lq in (2, 4):
    tgt_a = tuple(t % 2 for t in range(Lq))
    tgt_b = tuple(1 for _ in range(Lq))
    for wa in range(2 ** Lq):
        for wb in range(2 ** Lq):
            ap = tuple((wa >> t) & 1 for t in range(Lq))
            bp = tuple((wb >> t) & 1 for t in range(Lq))
            ok26 &= Hmap(ap, bp) != (tgt_a, tgt_b)
ok26 &= Hmap(tuple([1] * 4), tuple([0, 1, 0, 1]))[0] == (0, 0, 0, 0)
check('S26 G127, G128: period-two table; 0102 lift; the six precursors of 022000 (all 22100...); finite-window traces', ok26)
ok27 = True
deaths = {0: [], 1: []}
for phase in (0, 1):
    tau = lambda t: (t + phase) % 2
    for Ls in range(0, 11):
        last = 0
        for seed in range(2 ** Ls):
            Tm = 60
            Wd = Ls + Tm + 3
            row = {i: ((seed >> (-i - 1)) & 1) if -Ls <= i <= -1 else 0 for i in range(-Wd, 0)}
            died = None
            for t in range(Tm):
                ell = row[-1]
                if tau(t) == 1 and ell != 1 - tau(t + 1):
                    died = t
                    break
                new = {i: R30(row[i - 1], row[i], row[i + 1] if i + 1 < 0 else tau(t)) for i in range(-Wd + 1, 0)}
                new[-Wd] = 0
                row = new
            ok27 &= died is not None
            last = max(last, died if died is not None else 999)
        deaths[phase].append(last)
ok27 &= deaths[0] == [1, 7, 7, 7, 7, 9, 9, 9, 17, 17, 17] and deaths[1] == [0, 2, 6, 6, 6, 8, 10, 12, 12, 18, 18]
check('S27 G129: every left seed (L <= 10) dies against the alternating wall within 18 ticks, both phases', ok27,
      str(deaths))
def wall_trace(init, T_):
    """init: dict site -> bit (finite support, zero elsewhere); trace of site 0 for t = 0..T_."""
    lo_, hi_ = min(init) - T_ - 2, max(init) + T_ + 2
    row = {i: init.get(i, 0) for i in range(lo_, hi_ + 1)}
    out = [row[0]]
    for t in range(T_):
        row = {i: R30(row.get(i - 1, 0), row[i], row.get(i + 1, 0)) for i in range(lo_ + t + 1, hi_ - t)}
        out.append(row[0])
    return out


rng28 = random.Random(130)
ok28 = True
for trial in range(200):
    Nn = rng28.randint(1, 12)
    rtail = {i: rng28.randint(0, 1) for i in range(0, rng28.randint(1, 6))}
    tau = [rtail[0]] + [rng28.randint(0, 1) for _ in range(Nn)]
    left = {}
    for n in range(1, Nn + 1):
        sols = []
        for g_ in (0, 1):
            left[-n] = g_
            init = dict(rtail)
            init.update(left)
            if wall_trace(init, n)[n] == tau[n]:
                sols.append(g_)
        ok28 &= len(sols) == 1
        left[-n] = sols[0] if sols else 0
    init = dict(rtail)
    init.update(left)
    ok28 &= wall_trace(init, Nn) == tau
one = {i: (1 if i < 0 else 0) for i in range(-40, 41)}
step = {i: R30(one.get(i - 1, 1 if i - 1 < 0 else 0), one[i], one.get(i + 1, 0)) for i in range(-39, 40)}
ok28 &= all(step[i] == (1 if i == 0 else 0) for i in range(-39, 40))
single = wall_trace({0: 1}, 16)
tau_g = [0] + single
for Nt in range(1, 15):
    seed = {i: 1 for i in range(-Nt, 0)}
    seed[0] = 0
    tr = wall_trace(seed, Nt + 1)
    ok28 &= tr[:Nt + 1] == tau_g[:Nt + 1] and tr[Nt + 1] != tau_g[Nt + 1]
check('S28 G130: unique successive left solving realizes every prefix; the one-tick guard; truncations break at N + 1', ok28)
import math as _mm
ok29 = True
rng29 = random.Random(131)
for alpha in (_mm.sqrt(2) - 1, (_mm.sqrt(5) - 1) / 2):
    g = lambda y: 1 if (y % 1.0) >= 1 - alpha else 0
    for trial in range(20):
        ks = sorted(rng29.sample(range(-6, 7), 2 * rng29.randint(1, 3)))
        beta = rng29.random()
        ends = sorted(((beta + k * alpha) % 1.0) for k in ks)
        f0 = rng29.randint(0, 1)
        f = lambda x: (sum(1 for e in ends if e <= (x % 1.0)) + f0) % 2
        # Q(z) = sum z^(k - kmin); P = Q / (1 + z) over GF(2)
        kmin = ks[0]
        Q = [0] * (ks[-1] - kmin + 1)
        for k in ks:
            Q[k - kmin] ^= 1
        P = [0] * (len(Q) - 1)
        rem = Q[:]
        for i in range(len(Q) - 1, 0, -1):          # divide from the top: z^i term -> P_(i-1)
            if rem[i]:
                P[i - 1] ^= 1
                rem[i] ^= 1
                rem[i - 1] ^= 1
        ok29 &= not any(rem)
        def h(y):
            v = 0
            for j, pj in enumerate(P):
                if pj:
                    k = j + kmin
                    v ^= g(y - (k + 1) * alpha)
            return v
        theta = rng29.random()
        vals = set()
        for sidx in range(20000):
            y = (theta - beta + sidx * alpha) % 1.0
            x = (beta + y) % 1.0
            if min(abs(x - e) for e in ends) < 1e-9:
                continue
            vals.add(f(beta + y) ^ h(y))
        ok29 &= len(vals) == 1
a2 = _mm.sqrt(2) - 1
gs = [1 if ((0.3 + s_ * a2) % 1.0) >= 1 - a2 else 0 for s_ in range(5000)]
ok29 &= all(not (gs[i] and gs[i + 1]) for i in range(4999))
for trial in range(200):
    wv = rng29.randint(0, 3)
    base = [rng29.randint(0, 1) for _ in range(30)]
    q = rng29.randint(1, 5)
    word = base + [0] * 40
    for i_ in range(len(base), len(word)):
        word[i_] = word[i_ - q]
    a_ = rng29.randint(0, 10)
    e_ = len(word) - 1 - q
    Fb = lambda blk: (sum(blk) % 2) ^ (blk[0] & blk[-1])
    cw = [Fb(word[i_:i_ + wv + 1]) for i_ in range(len(word) - wv)]
    ok29 &= all(cw[s_] == cw[s_ + q] for s_ in range(len(base), e_ - wv + 1))
check('S29 G131: one-orbit arc codes = XOR of rotated interval codes + constant; no adjacent ones for alpha < 1/2; '
      'repeats inherited by block codes', ok29)
ok30 = True
for alpha in ((_mm.sqrt(2) - 1) / 1.7, (_mm.sqrt(5) - 1) / 2):
    beta = (2 * alpha) % 1.0
    psi = lambda u: 1 if (u % 1.0) >= 1 - beta else 0
    fcov = lambda x: psi((2 * x) % 1.0)
    Ngrid = 200000
    jumps = []
    prev = fcov(0.0)
    for i in range(1, Ngrid + 1):
        x = i / Ngrid
        cur = fcov(x % 1.0)
        if cur != prev:
            jumps.append(x)
        prev = cur
    expect = sorted(v % 1.0 for v in (0.0, 0.5, -alpha, 0.5 - alpha))
    got = sorted(j % 1.0 for j in jumps)
    ok30 &= len(got) == 4 and all(min(abs(gv - e), 1 - abs(gv - e)) < 2.0 / Ngrid for gv, e in zip(got, expect))
    th = 0.123
    ok30 &= all(fcov((th + s_ * alpha) % 1.0) == psi(2 * th + s_ * beta) for s_ in range(20000)
                if min(abs(((2 * th + s_ * beta) % 1.0) - (1 - beta)), ((2 * th + s_ * beta) % 1.0)) > 1e-9)
box = lambda x, y: 1 if (x % 1.0) < 0.5 and (y % 1.0) < 0.5 else 0
for a_ in range(-4, 5):
    for b_ in range(-4, 5):
        if a_ == 0 and b_ == 0:
            continue
        found = False
        for trial in range(2000):
            x, y = rng29.random(), rng29.random()
            tstep = rng29.random()
            x2, y2 = (x + b_ * tstep) % 1.0, (y - a_ * tstep) % 1.0      # same character value a x + b y
            if box(x, y) != box(x2, y2):
                found = True
                break
        ok30 &= found
check('S30 G132: covering endpoints and Sturmian code; the box is not a function of any small character', ok30)
ok31 = True
alpha_g = (_mm.sqrt(5) - 1) / 2
first_viol = {}
for Cc in (0, 2, 5):
    Nn = 84 * (Cc + 4)
    worst = 0
    for trial in range(30):
        th = rng29.random()
        gseq = [1 if ((th + s_ * alpha_g) % 1.0) >= 1 - alpha_g else 0 for s_ in range(Nn + 1)]
        first = None
        for q in range(1, Nn):
            run_start = None
            for s_ in range(0, Nn - q + 1):
                if gseq[s_] == gseq[s_ + q]:
                    if run_start is None:
                        run_start = s_
                    b_ = s_
                    if b_ > 2 * run_start + q + Cc:
                        pos = b_ + q
                        first = pos if first is None else min(first, pos)
                        break
                else:
                    run_start = None
        ok31 &= first is not None and first <= Nn
        worst = max(worst, first if first is not None else 10 ** 9)
    first_viol[Cc] = worst
ok31 &= 4 * 55 + 8 == 228 and 228 < 336
kk = [2 ** (2 ** j) for j in range(1, 6)]
ok31 &= any(kk[j + 1] > 169 * kk[j] + 84 * 1 + 505 for j in range(len(kk) - 1))
kd = [2 ** j for j in range(1, 40)]
ok31 &= all(kd[j + 1] <= 169 * kd[j] + 84 * 1 + 505 for j in range(len(kd) - 1))
check('S31 G133: every golden prefix of length 84(C+4) violates the repeat bound (C = 0, 2, 5); horizon and kick checks',
      ok31, 'latest first violation over 30 phases: %s (horizons %s)' % (first_viol, {c: 84 * (c + 4) for c in (0, 2, 5)}))
def first_violation(alpha, th, Cc, Nn):
    gseq = [1 if ((th + s_ * alpha) % 1.0) >= 1 - alpha else 0 for s_ in range(Nn + 1)]
    first = None
    for q in range(1, Nn):
        run_start = None
        for s_ in range(0, Nn - q + 1):
            if gseq[s_] == gseq[s_ + q]:
                if run_start is None:
                    run_start = s_
                if s_ > 2 * run_start + q + Cc:
                    pos = s_ + q
                    first = pos if first is None else min(first, pos)
                    break
            else:
                run_start = None
        if first is not None and q > first:
            break
    return first


ok32 = True
tiny = 1 / (50 + (1 + _mm.sqrt(5)) / 2)
angles = {'golden': (_mm.sqrt(5) - 1) / 2, 'sqrt2-1': _mm.sqrt(2) - 1, 'e-2': _mm.e - 2, 'pi-3': _mm.pi - 3,
          'tiny': tiny, '1-tiny': 1 - tiny}
worst32 = {}
for name, alpha in angles.items():
    for Cc in (0, 2):
        Nn = 251 * (Cc + 4)
        w = 0
        for trial in range(10):
            fv = first_violation(alpha, rng29.random(), Cc, Nn)
            ok32 &= fv is not None and fv <= Nn
            w = max(w, fv if fv is not None else 10 ** 9)
        worst32[(name, Cc)] = w
ok32 &= 8 * 2 ** 4 + 3 == 131
ok32 &= all(4 * 31 * (2 * Cc + 8) + 3 * Cc + 8 == 251 * Cc + 1000 for Cc in range(20))
check('S32 G134, G135: every awkward-angle prefix of length 251(C+4) violates the repeat bound; constants', ok32,
      'latest first violations: %s' % {k: v for k, v in worst32.items()})
def first_violation_seq(seq, Cc):
    Nn = len(seq) - 1
    first = None
    for q in range(1, Nn):
        run_start = None
        for s_ in range(0, Nn - q + 1):
            if seq[s_] == seq[s_ + q]:
                if run_start is None:
                    run_start = s_
                if s_ > 2 * run_start + q + Cc:
                    pos = s_ + q
                    first = pos if first is None else min(first, pos)
                    break
            else:
                run_start = None
        if first is not None and q > first:
            break
    return first


def mech_exact(alpha, theta, n):
    return [1 if ((theta + s_ * alpha) % 1) >= 1 - alpha else 0 for s_ in range(n)]


ok33 = True
for alpha in (F(0), F(1), F(1, 2), F(2, 5), F(3, 7)):
    for trial in range(5):
        th = F(rng29.randint(0, 999), 1000)
        for Cc in (0, 1):
            Mm = 251 * (Cc + 4)
            fv = first_violation_seq(mech_exact(alpha, th, Mm + 1), Cc)
            ok33 &= fv is not None and fv <= Mm
for alpha in ((_mm.sqrt(5) - 1) / 2, _mm.pi - 3, F(2, 5)):
    for trial in range(5):
        wv = rng29.randint(0, 3)
        table = {blk: rng29.randint(0, 1) for blk in product((0, 1), repeat=wv + 1)}
        for Cc in (0, 1):
            Mm = 251 * (Cc + 4) + 250 * wv
            th = rng29.random() if not isinstance(alpha, F) else F(rng29.randint(0, 999), 1000)
            g_ = mech_exact(alpha, th, Mm + wv + 1)
            cseq = [table[tuple(g_[i:i + wv + 1])] for i in range(Mm + 1)]
            fv = first_violation_seq(cseq, Cc)
            ok33 &= fv is not None and fv <= Mm
tm = [bin(i).count('1') % 2 for i in range(400)]
ok33 &= first_violation_seq(tm[:400], 0) is None
gg = mech_exact((_mm.sqrt(5) - 1) / 2, 0.3, 1200)
for wv in range(1, 900):       # a Sturmian word has n + 1 blocks of length n: 121 distinct need w >= 119
    blocks = [tuple(gg[i:i + wv + 1]) for i in range(121)]
    if len(set(blocks)) == 121:
        break
table = {blocks[i]: tm[i] for i in range(121)}
ok33 &= [table[tuple(gg[i:i + wv + 1])] for i in range(121)] == tm[:121]
check('S33 G136: rational and recoded mechanical prefixes violate within H(C, w); the Thue-Morse width guard', ok33,
      'width needed for 121 distinct golden blocks: %d' % wv)
ok34 = True
dy = [1 if s_ >= 1 and (s_ & (s_ - 1)) == 0 else 0 for s_ in range(3001)]
ok34 &= first_violation_seq(dy, -1) is None
for m in range(1, 41):
    facts = set(tuple(dy[i:i + m]) for i in range(0, 3001 - m))
    ok34 &= len(facts) <= 2 * m + 1
for B in (3, 4):
    pw = set()
    v = 1
    while v <= 3000:
        pw.add(v)
        v *= B
    dB = [1 if s_ in pw else 0 for s_ in range(3001)]
    fv = first_violation_seq(dB, 5)
    ok34 &= fv is not None and fv <= 3000
check('S34 G137: dyadic word passes b <= 2a + q - 1 everywhere; factor counts <= 2m + 1; bases 3, 4 fail', ok34)
def forced_columns(vis, J, T):
    """v_j(t) for j = 0..J, t = 0..T-1 (lists), from column 0 = t mod 2 and visible bits vis[s] at time 2s."""
    Tt = T + J + 2
    v0 = [t % 2 for t in range(Tt)]
    c1 = [(vis[t // 2] if t // 2 < len(vis) else 0) if t % 2 == 0 else 0 for t in range(Tt)]
    cols = [v0]
    right, far = v0, c1
    for j in range(1, J + 1):
        col = [right[t + 1] ^ (right[t] | far[t]) for t in range(len(right) - 1)]
        cols.append(col)
        far, right = right, col
    return cols


ok35 = True
for trial in range(100):
    vis = [rng29.randint(0, 1) for _ in range(60)]
    cols = forced_columns(vis, 6, 80)
    for s_ in range(0, 25):
        A, B, D = vis[s_], vis[s_ + 1], vis[s_ + 2]
        pairs = [(1 - A, 1), (A, B), (1 - B, 1 - B), (A & B, D), (D ^ (A | (1 - B)), 1 - B)]
        for j in range(1, 6):
            ok35 &= (cols[j][2 * s_], cols[j][2 * s_ + 1]) == pairs[j - 1]
dyv = [1 if s_ >= 1 and (s_ & (s_ - 1)) == 0 else 0 for s_ in range(400)]
dcols = forced_columns(dyv, 30, 300)
ok35 &= [dcols[j][0] for j in range(1, 6)] == [1, 0, 0, 0, 1]
# defect field
for trial in range(50):
    vis = [rng29.randint(0, 1) if rng29.random() < 0.2 else 0 for _ in range(60)]
    cols = forced_columns(vis, 13, 70)
    e = [None] + [[cols[j][t] ^ (j % 2) for t in range(len(cols[j]))] for j in range(1, 14)]
    for j in range(2, 13):
        for t in range(0, 60):
            if j % 2 == 1:
                pred = e[j][t + 1] ^ (e[j][t] & (1 - e[j - 1][t]))
            else:
                pred = e[j][t + 1] ^ ((1 - e[j][t]) & e[j - 1][t])
            ok35 &= e[j + 1][t] == pred
    for j in range(1, 13):
        for t in range(0, 55):
            if not any(e[1][u] for u in range(t, t + j)):
                ok35 &= e[j][t] == 0
ed = [None] + [[dcols[j][t] ^ (j % 2) for t in range(len(dcols[j]))] for j in range(1, 31)]
pulses = [2 * (2 ** k) for k in range(0, 9)]
for j in range(1, 31):
    for t in range(0, 250):
        if ed[j][t]:
            ok35 &= any(P_ - j + 1 <= t <= P_ for P_ in pulses)
for j in range(1, 11):
    col = dcols[j]
    for m in range(1, 31):
        facts = set(tuple(col[u:u + m]) for u in range(0, 240 - m))
        ok35 &= len(facts) <= 4 * (m + j) + 2
check('S35 G138, G139: low-depth pairs; dyadic initial cells 10001; defect recurrences and locality; '
      'dyadic defect support; temporal factor bound', ok35)
def phi_row(vis, K):
    cols = forced_columns(vis, K, 2)
    return [cols[j][0] for j in range(1, K + 1)]


def wall_two_steps(row, K):
    """Half-line x <= -1 (row[j-1] = x(-j)), wall x_t(0) = t mod 2, two forward steps from t = 0."""
    cur = {-j: row[j - 1] for j in range(1, K + 1)}
    for t in range(2):
        wall = t % 2
        nxt = {}
        for j in range(1, K + 1 - (t + 1)):
            i = -j
            right = wall if i + 1 == 0 else cur[i + 1]
            nxt[i] = R30(cur[i - 1], cur[i], right)
        cur = nxt
    return [cur[-j] for j in range(1, K - 1)]


ok36 = True
Kp = 80
for trial in range(50):
    vis = [rng29.randint(0, 1) for _ in range(Kp)]
    r0 = phi_row(vis, Kp)
    after = wall_two_steps(r0, Kp)
    r_shift = phi_row(vis[1:] + [0], Kp)
    ok36 &= after[:Kp - 6] == r_shift[:Kp - 6]
    cols = forced_columns(vis, 2, 2 * Kp)
    ok36 &= all(cols[1][t] == 1 for t in range(1, 2 * Kp - 4, 2))
dyw = [1 if s_ >= 1 and (s_ & (s_ - 1)) == 0 else 0 for s_ in range(4000)]
agree = []
for n in range(2, 9):
    tn = 3 * 2 ** (n - 1)
    row = phi_row(dyw[tn:tn + 300], 200)
    checker = [1 if j % 2 == 1 else 0 for j in range(1, 201)]
    k = 0
    while k < 200 and row[k] == checker[k]:
        k += 1
    agree.append(k)
ok36 &= all(agree[i + 1] >= agree[i] for i in range(len(agree) - 1)) and agree[-1] > agree[0]
check('S36 G140: the conjugacy F Phi = Phi shift; black wall neighbour at odd times; the checkerboard limit', ok36,
      'checkerboard agreement prefixes for n = 2..8: %s' % agree)
ok37 = True
for trial in range(30):
    vis = [rng29.randint(0, 1) for _ in range(40)]
    cur = phi_row(vis, 120)
    trace = []
    for t in range(60):
        trace.append(cur[0])
        cur = [R30(cur[i + 1], cur[i], (t % 2) if i == 0 else cur[i - 1]) for i in range(len(cur) - 1)]
    ok37 &= all(trace[2 * s_] == 1 - vis[s_] and trace[2 * s_ + 1] == 1 for s_ in range(30))
for k in range(1, 11):
    pats = [tuple(phi_row(list(p_) + [0] * 4, 2 * k)) for p_ in product((0, 1), repeat=k)]
    ok37 &= len(set(pats)) == 2 ** k and len({q[:2 * k - 1] for q in pats}) == 2 ** k
    ok37 &= k == 1 or len({q[:2 * k - 2] for q in pats}) == 2 ** (k - 1)
    ok37 &= all(q[1] == 1 - q[0] for q in pats)
for trial in range(200):
    L = rng29.randint(1, 40)
    row = [rng29.randint(0, 1) for _ in range(L - 1)] + [1] + [0] * 10
    after = wall_two_steps(row, L + 10)
    ok37 &= max(j + 1 for j in range(len(after)) if after[j]) == L + 2
check('S37 G140 sharpened: forward read-back of the coding; odd depths free, even depths forced; radius grows by exactly 2',
      ok37)
def back_step(y, wall, q1):
    q = [wall, q1]
    for j in range(1, len(y)):
        q.append(y[j - 1] ^ (q[j] | q[j - 1]))
    return q[1:]


def fwd_step(row, wall):
    q = [wall] + row
    return [q[j + 1] ^ (q[j] | q[j - 1]) for j in range(1, len(row))]


def radius(row):
    return max([j + 1 for j in range(len(row)) if row[j]] or [0])


def tail_kind(row, start):
    t = row[start:]
    if not any(t):
        return 'zero'
    if all(t):
        return 'black'
    if all(t[i] == t[i + 3] for i in range(len(t) - 3)) and any(t):
        return 'period3'
    return 'other'


ok38 = True
kinds = {}
for trial in range(400):
    L = rng29.randint(1, 15)
    K = L + 60
    u = [rng29.randint(0, 1) for _ in range(L - 1)] + [1] + [0] * (K - L)
    z = back_step(u, 1, 1)
    ok38 &= fwd_step(z, 1)[:K - 2] == u[:K - 2]
    pair = (z[L], z[L - 1])          # (q_(L+1), q_L): the outward recursion is M0 from here
    zk = tail_kind(z, L + 3)
    ok38 &= zk == ('zero' if pair == (0, 0) else 'black')
    if zk == 'zero':
        ok38 &= radius(z) == L - 1 if L >= 2 else radius(z) <= 1
    for a in (0, 1):
        w = back_step(z[:K - 4], 0, a)
        ok38 &= fwd_step(w, 0)[:K - 7] == z[:K - 7]
        if zk == 'black':
            wk = tail_kind(w[:K - 6], L + 12)
            ok38 &= wk == 'period3'
        else:
            m = radius(z)
            wp = (w[m], w[m - 1]) if m >= 1 else (w[0], 0)
            wk = tail_kind(w[:K - 6], m + 3)
            ok38 &= wk == ('zero' if wp == (0, 0) else 'black')
            if wk == 'zero':
                ok38 &= radius(w) == L - 2
        kinds[(zk, wk)] = kinds.get((zk, wk), 0) + 1
g1 = fwd_step([0, 1, 1] + [0] * 8, 0)
g2 = fwd_step([1, 0, 1] + [0] * 8, 0)
ok38 &= g1 == g2 and g1[:6] == [1, 0, 1, 1, 0, 0] and fwd_step(g1, 1)[:7] == [1, 0, 0, 1, 1, 0, 0]
for trial in range(30):
    vis = [rng29.randint(0, 1) for _ in range(60)]
    u = phi_row(vis, 110)
    z = back_step(u, 1, 1)
    for a in (0, 1):
        w = back_step(z[:105], 0, a)
        ok38 &= w[:90] == phi_row([1 - a] + vis, 110)[:90]
check('S38 G141: the black and white backward steps, their tail tests and radii; the merging guard; the phase convention',
      ok38, 'tail kinds (black-phase predecessor, white-phase predecessor): %s' % sorted(kinds.items()))
import decimal
decimal.getcontext().prec = 60
DB = 2 - decimal.Decimal(2).sqrt()
NP = 4096
xs = [(s_ * DB) % 1 for s_ in range(NP)]
cb = [int((s_ * DB).to_integral_value(rounding=decimal.ROUND_FLOOR)) % 2 for s_ in range(NP)]


def eps_even(q):
    v = q * DB
    P = 2 * int((v / 2).to_integral_value(rounding=decimal.ROUND_HALF_EVEN))
    return v - P


def in_mis(x, e):
    return x >= 1 - e if e > 0 else x < -e


ok39 = True
for q in range(1, 201):
    e = eps_even(q)
    ok39 &= all((cb[s_] != cb[s_ + q]) == in_mis(xs[s_], e) for s_ in range(NP - q))
recs, best = [], {1: None, -1: None}
for q in range(1, 2049):
    e = eps_even(q)
    sg = 1 if e > 0 else -1
    if best[sg] is None or abs(e) < best[sg]:
        best[sg] = abs(e)
        recs.append(q)
qs = [1, 2]
while qs[-1] < 5000:
    qs.append(2 * qs[-1] + qs[-2])
want = sorted({1, 2} | {qs[n] + qs[n - 1] for n in range(1, len(qs))} | {2 * qs[n] for n in range(1, len(qs))})
ok39 &= recs == [q for q in want if q <= 2048]
for n in range(1, 9):
    qn, qn1 = qs[n], qs[n + 1]
    d = min(abs(qn * DB - k) for k in range(qn + 1))
    E = (decimal.Decimal(2).sqrt()) * d
    pts = sorted(xs[:qn1])
    gaps = [pts[i + 1] - pts[i] for i in range(len(pts) - 1)] + [1 - pts[-1] + pts[0]]
    nd = sum(1 for g_ in gaps if abs(g_ - d) < decimal.Decimal(10) ** -40)
    nE = sum(1 for g_ in gaps if abs(g_ - E) < decimal.Decimal(10) ** -40)
    ok39 &= nd == qn1 - qn and nE == qn
worst = {}
for n in range(1, 9):
    for kind, q in (('Q', qs[n] + qs[n - 1]), ('2q', 2 * qs[n])):
        if q > 2048:
            continue
        mis = [s_ for s_ in range(1, NP - q) if cb[s_] != cb[s_ + q]]
        first = mis[0]
        ok39 &= first == qs[n] if kind == 'Q' else qs[n] <= first <= qs[n] + qs[n - 1]
        dmax, s_ = None, 0
        while s_ + q <= NP - 1:
            if cb[s_] == cb[s_ + q]:
                a_ = s_
                while s_ + q <= NP - 1 and cb[s_] == cb[s_ + q]:
                    s_ += 1
                if s_ + q <= NP - 1:            # only intervals closed by a mismatch inside the prefix
                    dd = (s_ - 1) - 2 * a_ - q
                    dmax = dd if dmax is None else max(dmax, dd)
            s_ += 1
        bound = -3 if kind == 'Q' else qs[n - 1] - qs[n] - 1
        ok39 &= dmax is not None and dmax <= bound
        worst[q] = dmax
ok39 &= all(worst[qs[n] + qs[n - 1]] == -3 for n in range(2, 8))
check('S39 G143: the mismatch rule, the record list, the two-gap mesh, the first hits and the debt bounds at the records',
      ok39, 'records to 2,048: %s; worst debts: %s' % (recs, sorted(worst.items())))
from fractions import Fraction as _Fr


def cf_conv(a0, cf):
    p0, q0, p1, q1 = 1, 0, a0, 1
    out = []
    for a in cf:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
        out.append((p1, q1))
    return out


def cf_value(cf):
    x = _Fr(0)
    for a in reversed(cf):
        x = 1 / (a + x)
    return decimal.Decimal(x.numerator) / decimal.Decimal(x.denominator)


def initial_debt(beta, q, M):
    c_ = [int((s_ * beta).to_integral_value(rounding=decimal.ROUND_FLOOR)) % 2 for s_ in range(M + q + 2)]
    mis = [s_ for s_ in range(M) if c_[s_] != c_[s_ + q]]
    h = [s_ for s_ in mis if s_ > 0][0]
    a_ = 1 if c_[0] != c_[q] else 0
    return h, (h - 1) - 2 * a_ - q


ok40 = True
b1 = decimal.Decimal(2).sqrt() - 1
cv1 = cf_conv(0, [2] * 12)
for i in range(1, 6):
    (pn, qn), (pn1, qn1) = cv1[i], cv1[i + 1]
    if pn % 2 == 0:
        dn = qn * b1 - pn
        h, dbt = initial_debt(b1, qn, qn1 + 5)
        ok40 &= h == qn1 and dbt == (qn1 - qn - 1 if dn > 0 else qn1 - qn - 3)
ok40 &= initial_debt(b1, 5, 20) == (12, 6)
cf2 = [1, 1] + [4] * 120
b2 = cf_value(cf2)
cv2 = cf_conv(0, cf2[:8])
ok40 &= all(pn % 2 == 1 for pn, _ in cv2)
for i in range(1, 5):
    (pm, qm), (pn, qn) = cv2[i - 1], cv2[i]
    a = cf2[i + 1]
    dn = qn * b2 - pn
    h, dbt = initial_debt(b2, 2 * qn, (a - 1) * qn + qm + 5)
    ok40 &= h == (a - 1) * qn + qm and dbt == ((a - 3) * qn + qm - 1 if dn > 0 else (a - 3) * qn + qm - 3)
b3 = 2 - decimal.Decimal(2).sqrt()
al = b3 / 2
r_ = decimal.Decimal(2).sqrt() - 1
cv3 = cf_conv(0, [1, 1] + [2] * 14)
AB = [((cv3[i][0] + cv3[i - 1][0]) // 2, cv3[i][1] + cv3[i - 1][1]) for i in range(2, 13)]
cva = cf_conv(0, [3] + [2] * 16)
for i in range(len(AB) - 1):
    (A, B), (A1, B1) = AB[i], AB[i + 1]
    D, D1 = B * al - A, B1 * al - A1
    ok40 &= abs(A * B1 - A1 * B) == 1 and D * D1 < 0 and B * abs(D) < decimal.Decimal(1) / 2
    ok40 &= abs(B * abs(D) - 1 / (decimal.Decimal(B1) / B + abs(D1) / abs(D))) < decimal.Decimal(10) ** -40
    ok40 &= abs(abs(D1) / abs(D) - r_) < decimal.Decimal(10) ** -40
    ok40 &= (A, B) in cva
check('S40 G144: the even-numerator and large-coefficient obstructions on its controls; the converse mediants are alpha convergents',
      ok40)
def flh_int(s_):
    return 0 if s_ == 0 else 2 * s_ - ((math.isqrt(8 * s_ * s_) - 1) // 2 + 1)


ok41 = True
NH = 4096
hc = [flh_int(s_) % 2 for s_ in range(NH)]
ok41 &= all(flh_int(s_) == int((s_ * DB + decimal.Decimal(1) / 2).to_integral_value(rounding=decimal.ROUND_FLOOR))
            for s_ in range(NH))
qsb = [1, 2]
while len(qsb) < 12:
    qsb.append(2 * qsb[-1] + qsb[-2])
debts41 = []
for n in (3, 5, 7, 9):
    qn, qm = qsb[n - 1], qsb[n - 2]
    Q, h = qn + qm, 2 * qn + qm // 2
    mis = [k for k in range(NH - Q) if hc[k] != hc[k + Q]]
    d_ = min(abs(qn * DB - j) for j in range(qn + 1))
    E_ = (1 + (decimal.Decimal(2).sqrt() - 1)) * d_
    arc = [k for k in range(NH - Q) if decimal.Decimal(1) / 2 - E_ <= xs[k] < decimal.Decimal(1) / 2]
    ok41 &= qn % 2 == 1 and qm % 2 == 0 and mis[0] == h and mis == arc
    debts41.append((h - 1) - Q)
    ok41 &= (h - 1) - Q == qn - qm // 2 - 1
ok41 &= debts41 == [3, 22, 133, 780]
check('S41 G145: the half-phase first hits h_n = 2 q_n + q_(n-1)/2 and the unbounded prefix debts', ok41,
      'debts at n = 3, 5, 7, 9: %s' % debts41)
ok42 = True
half = decimal.Decimal(1) / 2
c0 = cb
ok42 &= all(c0[t_ + s_] == int(((s_ + t_) * DB).to_integral_value(rounding=decimal.ROUND_FLOOR)) % 2 and
            c0[t_ + s_] == int((s_ * DB + ((t_ * DB) % 2)).to_integral_value(rounding=decimal.ROUND_FLOOR)) % 2
            for t_ in (1, 7, 41, 239) for s_ in range(200))


def max_debt(w):
    best_ = None
    for q in range(1, len(w) // 2 + 1):
        s_ = 0
        while s_ + q <= len(w) - 1:
            if w[s_] == w[s_ + q]:
                a_ = s_
                while s_ + q <= len(w) - 1 and w[s_] == w[s_ + q]:
                    s_ += 1
                dd = (s_ - 1) - 2 * a_ - q
                best_ = dd if best_ is None else max(best_, dd)
            s_ += 1
    return best_


recs42, bestd = [], None
for t_ in range(1, 2048):
    dist = abs((t_ * DB) % 2 - half)
    if bestd is None or dist < bestd:
        bestd = dist
        recs42.append(t_)
wit = [(3, 7, 11), (5, 41, 64), (7, 239, 373)]           # (n, Q_n, h_n) from S41
rows42 = []
for t_ in recs42:
    w = c0[t_:]
    agree = 0
    while agree < len(w) and w[agree] == hc[agree]:
        agree += 1
    md = max_debt(w)
    for n_, Q, h in wit:
        if agree >= h + Q:
            ok42 &= all(w[k] == w[k + Q] for k in range(h)) and (h - 1) - Q <= md
    ok42 &= md <= t_
    rows42.append((t_, agree, md))
ok42 &= max(a_ for _, a_, _ in rows42) >= 373 + 239
check('S42 G146: shifted passing codes approach the half-phase code, carry its witnesses, and obey the shift allowance',
      ok42, '(t, agreement with c^(1/2), max debt): %s' % rows42)
def xdiff(x, k):
    for _ in range(k):
        x = [x[i] ^ x[i + 1] for i in range(len(x) - 1)]
    return x


def nfac(x, n):
    return len({tuple(x[i:i + n]) for i in range(len(x) - n + 1)})


ok43 = True
words = [c0[:4096]] + [[rng29.randint(0, 1) for _ in range(600)] for _ in range(20)]
for x in words:
    for k in range(1, 6):
        dk = xdiff(x, k)
        jets = [xdiff(x, j)[:len(x) - k] for j in range(k + 1)]
        jet = list(zip(*jets))
        for n in range(1, 13):
            pd, px = nfac(dk, n), nfac(x, n + k)
            ok43 &= pd <= px <= 2 ** k * pd and nfac(jet, n) == px
for m in range(5):
    x = [rng29.randint(0, 1) for _ in range(200)]
    ok43 &= xdiff(x, 2 ** m) == [x[i] ^ x[i + 2 ** m] for i in range(200 - 2 ** m)]
for p_ in range(1, 7):
    for bits in product((0, 1), repeat=p_):
        for y0 in (0, 1):
            y = [y0]
            for i in range(60):
                y.append(y[-1] ^ bits[i % p_])
            ok43 &= all(y[i] == y[i + 2 * p_] for i in range(len(y) - 2 * p_))
alt = [i % 2 for i in range(40)]
ok43 &= xdiff(alt, 2) == [0] * 38 and [alt[i + 2] - 2 * alt[i + 1] + alt[i] for i in range(38)] == [-2, 2] * 19
row = [1 if j % 2 == 1 else 0 for j in range(1, 121)]
cur = row[:]
for t in range(40):
    nxt = [R30(cur[i + 1], cur[i], (t % 2) if i == 0 else cur[i - 1]) for i in range(len(cur) - 1)]
    ok43 &= nxt == row[:len(nxt)]
    cur = nxt
check('S43 G148: factor counts of fixed-order differences and jets; dyadic orders; integration periods; the controls', ok43)
import numpy as _np


def ring_step(x):
    return [x[(i - 1) % len(x)] ^ (x[i] | x[(i + 1) % len(x)]) for i in range(len(x))]


def least_period(w):
    for P in range(1, len(w) + 1):
        if len(w) % P == 0 and w == w[P:] + w[:P]:
            return P


def first_hit(x, cap):
    for T in range(cap + 1):
        if not any(x):
            return T
        x = ring_step(x)
    return None


def allowed(P, T):
    if P == 1:
        return True
    a, q = 0, P
    if q % 3:
        return False
    q //= 3
    while q % 2 == 0:
        q //= 2
        a += 1
    return q == 1 and a <= T - 2



def basin_preds(Y):
    """All predecessors of the ring row Y (cells left to right, Rule 30)."""
    n = len(Y)
    if n <= 2:
        cands = [[(v >> i) & 1 for i in range(n)] for v in range(1 << n)]
        return [x for x in cands if ring_step(x) == Y]
    out = []
    for a in (0, 1):
        for b in (0, 1):
            x = [None] * n
            x[0], x[1] = a, b
            for i in range(0, -(n - 2), -1):          # x_(i-1) = Y_i XOR (x_i OR x_(i+1)), indices mod n
                x[(i - 1) % n] = Y[i % n] ^ (x[i % n] | x[(i + 1) % n])
            if ring_step(x) == Y:
                out.append(x)
    return out


def zero_basin(n):
    """Exact first-hit times of every row of the n-ring that reaches zero: breadth-first search backward from zero.
    The forward map is deterministic, so the backward distance is the first-hit time. No step cap is involved."""
    hit, frontier, T = {0: 0}, [0], 0
    while frontier:
        T += 1
        nxt = []
        for v in frontier:
            for x in basin_preds([(v >> i) & 1 for i in range(n)]):
                u = sum(b << i for i, b in enumerate(x))
                if u not in hit:
                    hit[u] = T
                    nxt.append(u)
        frontier = nxt
    return hit


BASIN = {n: zero_basin(n) for n in range(1, 25)}
m24 = (1 << 24) - 1                                   # forward cross-check of the 24-ring basin, 1,500 steps
cur24 = _np.arange(1 << 24, dtype=_np.uint32)
hit24 = _np.full(1 << 24, -1, dtype=_np.int32)
for T in range(1500):
    hit24[(cur24 == 0) & (hit24 < 0)] = T
    cur24 = ((((cur24 << 1) | (cur24 >> 23)) & m24) ^ (cur24 | (((cur24 >> 1) | (cur24 << 23)) & m24))) & m24
fw24 = {int(v): int(hit24[v]) for v in _np.nonzero(hit24 >= 0)[0]}
BASIN_FORWARD_AGREES = fw24 == BASIN[24]
del cur24, hit24

ok44 = BASIN_FORWARD_AGREES
for n in range(1, 25):
    for v, T in BASIN[n].items():
        w = [(v >> i) & 1 for i in range(n)]
        ok44 &= allowed(least_period(w), T) and first_hit(w, T + 1) == T
for trial in range(200):
    k = 1 + trial % 4
    L = rng29.randint(1, 12)
    K = 1600
    y = [rng29.randint(0, 1) for _ in range(L - 1)] + [1] + [0] * (K - L)
    rows = [y]
    for _ in range(k):
        z = back_step(rows[-1], 1, 1)
        w_ = back_step(z, 0, rng29.randint(0, 1))
        rows += [z, w_]
    u = rows[-1]
    win = u[700:1300]
    P = next(P for P in range(1, 300) if all(win[i] == win[i + P] for i in range(len(win) - P)))
    pat = list(reversed(win[:P]))                       # depth runs leftward; the ring reads left to right
    T = first_hit(pat, 2 * k)
    ok44 &= T is not None and T <= 2 * k and allowed(least_period(pat), 2 * k)
    fw = u
    for t in range(2 * k):
        fw = fwd_step(fw, t % 2)
    ok44 &= fw[:200] == y[:200]
ok44 &= ring_step([0, 0, 1]) == [1, 1, 1] and ring_step([1, 1, 1]) == [0, 0, 0] and ring_step([0, 1, 0, 1]) == [0, 1, 0, 1]
check('S44 G149: zero-reaching periodic tails, their periods and first hits; backward wall pairs give such tails', ok44)
def _mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def ltr_matrix(y):
    M = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    for yi in y:
        T = [[0] * 4 for _ in range(4)]
        for a in (0, 1):
            for b in (0, 1):
                for c_ in (0, 1):
                    if yi == a ^ (b | c_):
                        T[2 * a + b][2 * b + c_] = 1
        M = _mm(M, T)
    return M


def g150_predict(y):
    i0 = y.index(0)
    rot = y[i0:] + y[:i0]
    runs, cur = [], 0
    for v in rot[1:] + [0]:
        if v == 1:
            cur += 1
        else:
            runs.append(cur)
            cur = 0
    if any(L % 3 == 1 for L in runs):
        return 'reset'
    return 'even' if sum(1 for L in runs if L % 3 == 2) % 2 == 0 else 'odd'


ok45 = True
kinds45 = {'reset': 0, 'even': 0, 'odd': 0}
for p_ in range(2, 15):
    for v in range(1, (1 << p_) - 1):
        y = [(v >> i) & 1 for i in range(p_)]
        if least_period(y) != p_:
            continue
        kind = g150_predict(y)
        kinds45[kind] += 1
        H = ltr_matrix(y)
        P_ = H
        for m in range(1, 7):
            tr = sum(P_[i][i] for i in range(4))
            want = 1 if kind == 'reset' else (2 if kind == 'even' or m % 2 == 0 else 0)
            ok45 &= tr == want
            P_ = _mm(P_, H)
ok45 &= ring_step([1, 0, 1]) == [0, 0, 1]
ok45 &= ring_step([0, 0, 1, 0, 1, 0]) == [0, 1, 1] * 2 and ring_step([0, 1, 0, 0, 0, 1]) == [0, 1, 1] * 2
ok45 &= ring_step([0, 0, 0, 0, 1, 0]) == [0, 0, 0, 1, 1, 1] and ring_step([1, 1, 1, 0, 0, 1]) == [0, 0, 0, 1, 1, 1]
check('S45 G150: periodic predecessor counts on rings of size m p follow the zero-gap parity rule exactly', ok45,
      'outputs by kind (p <= 14): %s' % kinds45)
def ring_preds(Y):
    n = len(Y)
    out = []
    for a in (0, 1):
        for b in (0, 1):
            x = [None] * n
            x[0], x[1] = a, b
            for i in range(0, -(n - 2), -1):          # x_(i-1) = Y_i XOR (x_i OR x_(i+1)), indices mod n
                x[(i - 1) % n] = Y[i % n] ^ (x[i % n] | x[(i + 1) % n])
            if ring_step(x) == Y:
                out.append(x)
    return out


def has_010(x):
    n = len(x)
    return any(x[i] == 0 and x[(i + 1) % n] == 1 and x[(i + 2) % n] == 0 for i in range(n))


ok46 = True
n_odd = 0
for p_ in range(2, 13):
    for v in range(1, (1 << p_) - 1):
        y = [(v >> i) & 1 for i in range(p_)]
        if least_period(y) != p_ or g150_predict(y) != 'odd':
            continue
        n_odd += 1
        xs_ = ring_preds(y * 2)
        ok46 &= len(xs_) == 2 and all(least_period(x) == 2 * p_ for x in xs_)
        for x in xs_:
            H = ltr_matrix(x)
            ok46 &= has_010(x) and sum(H[i][i] for i in range(4)) == 1 and sum(_mm(H, H)[i][i] for i in range(4)) == 1
n_basin46 = 0
for n in range(1, 25):
    for v, T in BASIN[n].items():
        if T < 2:
            continue
        n_basin46 += 1
        w = [(v >> i) & 1 for i in range(n)]
        P = least_period(w)
        a = 0
        q = P // 3
        while q > 1 and q % 2 == 0:
            q //= 2
            a += 1
        ok46 &= P % 3 == 0 and q == 1 and a <= (T - 2) // 2
traj = [[1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 1, 0, 0, 1, 0], [1] * 6, [0] * 6]
ok46 &= all(ring_step(traj[i]) == traj[i + 1] for i in range(5)) and has_010(traj[0])
check('S46 G151: doubled predecessors carry 010 and have one predecessor; the floor((T-2)/2) bound on rings to 24',
      ok46, '%d doubling outputs checked; %d basin rows with T >= 2 on rings to 24' % (n_odd, n_basin46))
def canon(w):
    return min(tuple(w[i:] + w[:i]) for i in range(len(w)))


def L_neck(q):
    return len({canon([(v >> i) & 1 for i in range(q)]) for v in range(1 << q)
                if least_period([(v >> i) & 1 for i in range(q)]) == q})


ok47 = True
Ls = {3: L_neck(3), 6: L_neck(6), 12: L_neck(12)}
ok47 &= Ls == {3: 2, 6: 9, 12: 335}
Cbound = {3: 2 + 2, 6: 2 + 2 + 9, 12: 2 + 2 + 9 + 335, 24: 2 + 2 + 9 + 335 + (2 ** 24 - 2 ** 12 - 2 ** 8 + 2 ** 4) // 24}
tmax47 = {}
for n in (3, 6, 12, 24):
    for v, T in BASIN[n].items():
        if T < 1:
            continue
        w = [(v >> i) & 1 for i in range(n)]
        P = least_period(w)
        if P == 1:
            continue
        traj, x = [], w
        for _ in range(T + 1):
            traj.append(canon(x))
            x = ring_step(x)
        ok47 &= len(set(traj)) == len(traj)
        ok47 &= all(least_period(list(c_)) in (1, 3, 6, 12, 24) for c_ in traj)
        ok47 &= T + 1 <= Cbound[P]
        tmax47[n] = max(tmax47.get(n, 0), T)
ok47 &= ring_step([0, 1, 1]) == [0, 1, 0] and ring_step([0, 1, 0]) == [1, 1, 1] and ring_step([1, 1, 1]) == [0, 0, 0]
check('S47 G152: necklace counts, distinct rotation classes along first-hit trajectories, and T + 1 <= C_a', ok47,
      'largest first-hit time by ring size: %s; bounds C_a: %s' % (tmax47, Cbound))
def r_rs(n):
    return bin(n & (n >> 1)).count('1') % 2


ok48 = all(r_rs(2 * n) == r_rs(n) and r_rs(2 * n + 1) == r_rs(n) ^ (n % 2) for n in range(1 << 14))
SUB = {'a': 'ab', 'b': 'ad', 'c': 'cd', 'd': 'cb'}
LET = {(0, 0): 'a', (0, 1): 'b', (1, 0): 'c', (1, 1): 'd'}
wfix = 'a'
while len(wfix) < (1 << 14):
    wfix = ''.join(SUB[ch] for ch in wfix)
ok48 &= wfix[:1 << 14] == ''.join(LET[(r_rs(n), n % 2)] for n in range(1 << 14))
Mx = [[SUB[x].count(y) for y in 'abcd'] for x in 'abcd']
M6 = Mx
for _ in range(5):
    M6 = [[sum(M6[i][k] * Mx[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
ok48 &= all(v > 0 for row in M6 for v in row)
ok48 &= all(r_rs(2 ** k + m) == r_rs(m) and r_rs(3 * 2 ** k + m) == 1 ^ r_rs(m)
            for k in range(1, 13) for m in range(2 ** (k - 1)))
check('S48 G154: the Rudin-Shapiro substitution, its primitivity and the separated-block identities', ok48)
ok49 = True
for trial in range(60):
    vis = [rng29.randint(0, 1) for _ in range(40)]
    base = phi_row(vis, 40)
    for L in range(1, 41):
        k = (L + 1) // 2
        for i in range(k, 22):
            alt = vis[:]
            alt[i] ^= 1
            ok49 &= phi_row(alt, 40)[:L] == base[:L]
        if L % 2 == 1:
            alt = vis[:]
            alt[k - 1] ^= 1
            ok49 &= phi_row(alt, 40)[L - 1] != base[L - 1]
    ok49 &= base[2] == 1 - vis[1] and base[3] == vis[0] & vis[1]
rw = ''.join(str(r_rs(n)) for n in range(1 << 18))
pk49 = {}
for k in range(1, 65):
    h = 1
    while h < k:
        h *= 2
    pk = len({rw[i:i + k] for i in range(len(rw) - k + 1)})
    pk49[k] = pk
    ok49 &= pk <= 16 * h < 32 * k
check('S49 G155: the growing determining window, its endpoints, and the coarse factor bound for Rudin-Shapiro', ok49,
      'P(k) for k = 8..16 and 64: %s' % ([pk49[k] for k in range(8, 17)] + [pk49[64]]))
from math import gcd as _gcd


def edge_B(a, b, P):
    m = (1 << P) - 1
    Sb = ((b >> 1) | (b << (P - 1))) & m             # value at time t moves to time t - 1
    return (Sb ^ (a | b)) & m, a


def rot_class(a, b, P):
    m = (1 << P) - 1
    best = None
    for h in range(P):
        ra = ((a >> h) | (a << (P - h))) & m
        rb = ((b >> h) | (b << (P - h))) & m
        best = (ra, rb) if best is None or (ra, rb) < best else best
    return best


ok50 = True
K50 = {}
for P in range(1, 8):
    m = (1 << P) - 1
    pairs = [(a, b) for a in range(1 << P) for b in range(1 << P)]
    img = {x: edge_B(x[0], x[1], P) for x in pairs}
    ok50 &= all(rot_class(*img[x], P) == rot_class(*img[rot_class(*x, P)], P) for x in pairs)
    root = (0, m)
    ok50 &= img[root] == (0, 0) and img[(0, 0)] == (0, 0)
    pre = {}
    for x, y in img.items():
        pre.setdefault(y, []).append(x)
    depth, frontier, d = {root: 0}, [root], 0
    while frontier:
        d += 1
        nxt = [x for y in frontier for x in pre.get(y, []) if x not in depth and x[0] == y[1]]
        for x in nxt:
            depth[x] = d
        frontier = nxt
    K = max(depth.values()) + 1
    N4 = sum(phi_ * 4 ** (P // dd) for dd in range(1, P + 1) if P % dd == 0
             for phi_ in [sum(1 for t in range(1, dd + 1) if _gcd(t, dd) == 1)]) // P
    classes = {}
    for x, dx in depth.items():
        classes.setdefault(rot_class(*x, P), set()).add(dx)
    ok50 &= K + 1 <= N4 and all(len(v) == 1 for v in classes.values())
    K50[P] = (K, N4)
ok50 &= K50[1][0] == 3 and K50[2][0] == 8
path = [(0, 3), (3, 3), (3, 0), (0, 1), (1, 3), (3, 1), (1, 1), (1, 0)]
ok50 &= edge_B(*path[0], 2) == (0, 0) and all(edge_B(*path[i + 1], 2) == path[i] for i in range(7))
check('S50 G156: rotation commutes with B; rooted edge depths sit in distinct classes; K + 1 <= N_4(P) for P <= 7', ok50,
      'longest K and N_4 by period: %s' % K50)
def edge_children(a, b, P):
    out = []
    for c0 in (0, 1):
        c = [c0]
        for t in range(P - 1):
            c.append(((a >> t) & 1) ^ (((b >> t) & 1) | c[t]))
        if ((a >> (P - 1)) & 1) ^ (((b >> (P - 1)) & 1) | c[P - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def lp_bits(w, P):
    for d in range(1, P + 1):
        if P % d == 0 and all(((w >> t) & 1) == ((w >> ((t + d) % P)) & 1) for t in range(P)):
            return d


def edge_tree(P):
    root = (0, (1 << P) - 1)
    nodes, frontier, depth = {root: 0}, [root], 0
    while frontier:
        depth += 1
        nxt = []
        for (a, b) in frontier:
            for c_ in edge_children(a, b, P):
                if (b, c_) not in nodes:
                    nodes[(b, c_)] = depth
                    nxt.append((b, c_))
        frontier = nxt
    return nodes


ok51 = True
trees = {P: edge_tree(P) for P in range(1, 16)}
K51 = {P: max(t_.values()) + 1 for P, t_ in trees.items()}
for P in range(1, 16):
    Q = P & -P
    ok51 &= all((lp_bits(x, P) & (lp_bits(x, P) - 1)) == 0 and Q % lp_bits(x, P) == 0 for nd in trees[P] for x in nd)
    ok51 &= K51[P] == K51[Q]
    restr = {(a & ((1 << Q) - 1), b & ((1 << Q) - 1)): dpt for (a, b), dpt in trees[P].items()}
    ok51 &= len(restr) == len(trees[P]) and restr == trees[Q]
ok51 &= lp_bits(0b001, 3) == 3 and K51[1] == 3 and K51[2] == 8 and K51[4] == 29
check('S51 G157: rooted edge trees reduce to the dyadic part of the period, node for node, for P <= 15', ok51,
      'longest K for Q = 1, 2, 4, 8: %s; nodes at Q = 8: %d' % ([K51[q] for q in (1, 2, 4, 8)], len(trees[8])))
def bits_str(w, P):
    return ''.join(str((w >> t) & 1) for t in range(P))


ok52 = ok53 = True
E52 = {}
for P in range(1, 16):
    T = trees[P]
    kids = {}
    for (b, c_) in T:
        if T[(b, c_)] == 0:
            continue
        par = edge_B(b, c_, P)
        kids.setdefault(par, []).append((b, c_))
    qkids = {}
    for nd in T:
        cls = rot_class(*nd, P)
        qkids.setdefault(cls, set()).update(rot_class(*k, P) for k in kids.get(nd, []))
    nE = nL = 0
    for nd in T:
        a, b = nd
        nc = len(qkids[rot_class(*nd, P)])
        if b != 0:
            want = 1
        else:
            q = lp_bits(a, P)
            sig = bin(a & ((1 << q) - 1)).count('1') % 2
            want = 2 if sig == 0 else (1 if P % (2 * q) == 0 else 0)
        ok52 &= nc == want
    for cls, ch in qkids.items():
        a, b = cls
        if b == 0 and len(ch) == 2:
            nE += 1
        if len(ch) == 0:
            nL += 1
    ok52 &= nL == nE + 1
    E52[P] = nE
    if P in (1, 2):
        ok52 &= nE == 0
    for nd, dpt in T.items():
        a, b = nd
        if b == 0 and bin(a & ((1 << lp_bits(a, P)) - 1)).count('1') % 2 == 0:
            front = [nd]
            for step in range(6):
                front = [k for x in front for k in kids.get(x, [])]
                ok53 &= all(k[1] != 0 for k in front)
    byd = {}
    for nd, dpt in T.items():
        byd.setdefault(dpt, set()).add(rot_class(*nd, P))
    ok53 &= all(len(v) <= 2 ** (-(-dpt // 7)) for dpt, v in byd.items())


def integ(a_str):
    P = len(a_str)
    out = []
    for c0 in (0, 1):
        c = [c0]
        for t in range(P - 1):
            c.append(int(a_str[t]) ^ c[t])
        if int(a_str[P - 1]) ^ c[P - 1] == c0:
            out.append(''.join(map(str, c)))
    return sorted(out)


ok52 &= integ('0110') == ['0010', '1101'] and integ('0101') == ['0011', '1100']
amb52 = amb53 = 0
for P in range(1, 9):
    m = (1 << P) - 1
    for a in range(1 << P):
        for b in range(1 << P):
            ch = edge_children(a, b, P)
            ncls = len({rot_class(b, c_, P) for c_ in ch})
            if b != 0:
                want = 1
            else:
                q = lp_bits(a, P)
                sig = bin(a & ((1 << q) - 1)).count('1') % 2
                want = 2 if sig == 0 else (1 if P % (2 * q) == 0 else 0)
                amb52 += want == 2
            ok52 &= ncls == want
        q = lp_bits(a, P)
        if a != 0 and bin(a & ((1 << q) - 1)).count('1') % 2 == 0:
            front = [(0, c_) for c_ in edge_children(a, 0, P)]
            for step in range(6):
                ok53 &= all(x[1] != 0 for x in front)
                front = [(x[1], c_) for x in front for c_ in edge_children(x[0], x[1], P)]
                amb53 += len(front)
check('S52 G158: child rotation classes follow the parity rule; leaves = branches + 1; P = 1, 2 are chains', ok52,
      'rooted even-parity branch classes for P <= 15: %d; ambient two-class pairs, P <= 8: %d' % (sum(E52.values()), amb52))
check('S53 G159: six nonzero drivers after every even-parity branch; at most 2^ceil(n/7) classes at depth n', ok53,
      'ambient continuations checked: %d' % amb53)
def front_succ(a, b, r, P):
    if b == 0:
        r2, cost = r, 0
    else:
        t = r
        while not (b >> (t % P)) & 1:
            t += 1
        r2, cost = (t + 1) % P, t - r + 1
    return [((b, c_, r2), cost) for c_ in edge_children(a, b, P)]


def gated(a, b, r, P):
    if a != 0:
        return (a >> ((r - 1) % P)) & 1 == 1
    return ((b >> (r % P)) & 1) ^ ((b >> ((r - 1) % P)) & 1) == 1


def tarjan_cyclic(nodes, succ):
    index, low, onst, st, cyc, idx = {}, {}, set(), [], set(), [0]
    for v0 in nodes:
        if v0 in index:
            continue
        work = [(v0, iter(succ[v0]))]
        index[v0] = low[v0] = idx[0]; idx[0] += 1; st.append(v0); onst.add(v0)
        while work:
            v, it = work[-1]
            w = next(it, None)
            if w is None:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        x = st.pop(); onst.discard(x); comp.append(x)
                        if x == v:
                            break
                    if len(comp) > 1 or v in succ[v]:
                        cyc.update(comp)
            elif w not in index:
                index[w] = low[w] = idx[0]; idx[0] += 1; st.append(w); onst.add(w)
                work.append((w, iter(succ[w])))
            elif w in onst:
                low[v] = min(low[v], index[w])
    return cyc


ok54 = True
ncyc54 = {}
for P in range(1, 8):
    states = [(a, b, r) for a in range(1 << P) for b in range(1 << P) for r in range(P) if (a, b) != (0, 0)]
    succ = {}
    for (a, b, r) in states:
        sc = front_succ(a, b, r, P)
        ok54 &= all((x[0], x[1]) != (0, 0) for x, _ in sc)
        succ[(a, b, r)] = [x for x, _ in sc]
        if gated(a, b, r, P):
            ok54 &= all(gated(*x, P) for x in succ[(a, b, r)])
    for v in states:
        ok54 &= all(gated(*y, P) for x in succ[v] for y in succ[x])
    cyc = tarjan_cyclic(states, succ)
    ok54 &= all(gated(*v, P) for v in cyc)
    ncyc54[P] = len(cyc)
    for a in range(1 << P):
        for b in range(1 << P):
            if (a, b) == (0, 0):
                continue
            ng = sum(gated(a, b, r, P) for r in range(P))
            want = bin(a).count('1') if a else sum(((b >> t) & 1) != ((b >> ((t + 1) % P)) & 1) for t in range(P))
            ok54 &= ng == want
a0 = 0b1010                                            # a = 0101 in time order (bit t is time t)
ok54 &= not gated(a0, 0, 1, 4)
kids0 = sorted(x for x, _ in front_succ(a0, 0, 1, 4))
ok54 &= kids0 == sorted([(0, 0b1100, 1), (0, 0b0011, 1)])         # c = 0011 and its complement, time order
ok54 &= all(not gated(*x, 4) for x in kids0)
ok54 &= all(gated(*y, 4) for x in kids0 for y, _ in front_succ(*x, 4))
check('S54 G160: the arrival gate is invariant, entered within two edges, and contains every cycle (P <= 7)', ok54,
      'cyclic states by P: %s' % ncyc54)
def rep_path(Q):
    """G161's procedure on Q-periodic words (bit t = time t): returns ('branch' or 'none', nodes visited, periods)."""
    a, b, q = 0, (1 << Q) - 1, 1                # root (0, 1) with least common period 1, written on Q letters
    visited, periods = 0, []
    while True:
        visited += 1
        periods.append(q)
        if b != 0:
            ch = edge_children(a, b, Q)
            assert len(ch) == 1
            a, b = b, ch[0]
        else:
            sig = bin(a & ((1 << q) - 1)).count('1') % 2
            if sig == 0:
                return 'branch', visited, periods
            if q == Q:
                return 'none', visited, periods
            c, cs = 0, []
            for t in range(Q):
                cs.append(c)
                c ^= (a >> t) & 1
            a, b, q = b, sum(v << t for t, v in enumerate(cs)), 2 * q


ok55 = True
N55 = {}
for Q in (1, 2, 4, 8):
    verdict, vis, per = rep_path(Q)
    ok55 &= verdict == 'none' and vis == K51[Q]
    ok55 &= all(per[i] <= per[i + 1] for i in range(len(per) - 1))
    N55[Q] = len(trees[Q])
ok55 &= N55[1] == 3 and all(N55[Q] == N55[Q // 2] + Q * (K51[Q] - K51[Q // 2]) for Q in (2, 4, 8))
check('S55 G161: the single representative path agrees with the complete rooted trees for Q <= 8', ok55,
      'labeled nodes N(Q): %s' % N55)
def reset_cost(w, r, P):
    t = r
    while not (w >> (t % P)) & 1:
        t += 1
    return t - r + 1, (t + 1) % P


def three_costs(a, c, r, P):
    """Elapsed cost of the next three nonzero drivers below (a, 0) along child c: c, then d, then e."""
    d = [x for x in edge_children(0, c, P)]
    assert d == [(1 << P) - 1]
    e = edge_children(c, d[0], P)
    assert len(e) == 1
    k1, r1 = reset_cost(c, r, P)
    k2, r2 = reset_cost(d[0], r1, P)
    k3, r3 = reset_cost(e[0], r2, P)
    return k1 + k2 + k3


def run_pair(c, r, P):
    """(l, m): lengths of the constant run of c starting at r and of the next run."""
    v = (c >> r) & 1
    l = 0
    while ((c >> ((r + l) % P)) & 1) == v and l < P:
        l += 1
    m = 0
    while ((c >> ((r + l + m) % P)) & 1) != v and m < P:
        m += 1
    return l, m


ok56 = True
n56 = 0
for P in range(2, 11):
    for a in range(1, 1 << P):
        q = lp_bits(a, P)
        if bin(a & ((1 << q) - 1)).count('1') % 2:
            continue
        kids = edge_children(a, 0, P)
        if len(kids) != 2:
            continue
        for r in range(P):
            if not (a >> ((r - 1) % P)) & 1:
                continue
            c = kids[0]
            l, m = run_pair(c, r, P)
            costs = sorted(three_costs(a, k, r, P) for k in kids)
            ok56 &= costs == sorted([l + 2, l + m + 2]) and l + m <= q
            n56 += 1
aW = int('0000110001010011'[::-1], 2)                  # time order -> bit t
cW = int('0000010000110001'[::-1], 2)
ok56 &= sorted(edge_children(aW, 0, 16)) == sorted([cW, cW ^ 0xFFFF])
want = {0: (7, 8), 5: (3, 7), 6: (6, 8), 10: (4, 7), 12: (5, 6), 15: (3, 8)}
gates = [r for r in range(16) if (aW >> ((r - 1) % 16)) & 1]
ok56 &= gates == [0, 5, 6, 10, 12, 15]
ok56 &= all(tuple(sorted(three_costs(aW, k, r, 16) for k in (cW, cW ^ 0xFFFF))) == want[r] for r in gates)
for q in (4, 8, 16):
    c1 = 1 << (q - 1)
    a1 = c1 ^ (((c1 >> 1) | (c1 << (q - 1))) & ((1 << q) - 1))
    ok56 &= lp_bits(a1, q) == q and max(three_costs(a1, k, 0, q) for k in edge_children(a1, 0, q)) == q + 2
for q in (8, 16):
    mq = (1 << q) - 1
    dlt = lambda w: (w ^ (((w >> 1) | (w << (q - 1))) & mq)) & mq      # (Delta w)(t) = w(t) XOR w(t+1)
    g = 1 << (q - 1)
    cD, aD = dlt(g), dlt(dlt(g))

    def nu(w):
        k = 0
        while w:
            w = dlt(w)
            k += 1
        return k
    ok56 &= nu(aD) == q - 2 and nu(cD) == q - 1 and bool((aD >> (q - 1)) & 1)
    ok56 &= max(three_costs(aD, k, 0, q) for k in edge_children(aD, 0, q)) == q + 2
check('S56 G162: three post-split costs are {l + 2, l + m + 2}; the rooted control; the q + 2 families', ok56,
      '%d gated even-parity cases checked' % n56)
from fractions import Fraction as _F57


def block_map(drivers, P):
    def F(t):
        for w in drivers:
            if w:
                u = t
                while not (w >> (u % P)) & 1:
                    u += 1
                t = u + 1
        return t
    return F


def strip_rate(F, P):
    rates = set()
    for t0 in range(P):
        seen, t, n = {}, t0, 0
        while t % P not in seen:
            seen[t % P] = (n, t)
            t, n = F(t), n + 1
        n0, t1 = seen[t % P]
        rates.add(_F57(t - t1, n - n0))
    return rates


ok57 = True
for trial in range(400):
    P = rng29.randint(1, 8)
    m = rng29.randint(1, 12)
    drivers = [0 if rng29.random() < 0.2 else rng29.randint(0, (1 << P) - 1) for _ in range(m)]
    F = block_map(drivers, P)
    ok57 &= all(F(t + P) == F(t) + P and F(t) <= F(t + 1) for t in range(-P, 2 * P))
    rates = strip_rate(F, P)
    ok57 &= len(rates) == 1
    rho = rates.pop()
    for t in range(P):
        x = t
        for n in range(1, 61):
            x = F(x)
            ok57 &= abs(x - t - n * rho) <= P - 1
    if rho <= _F57(5 * m, 2):
        def H(t, N=60):
            best, x = 0, t
            for n in range(1, N + 1):
                x = F(x)
                best = max(best, 2 * (x - t) - 5 * m * n)
            return best
        Hs = [H(t) for t in range(P)]
        ok57 &= max(Hs) <= 2 * (P - 1)
        ok57 &= all(H(t) >= 2 * (F(t) - t) - 5 * m + H(F(t) % P) for t in range(P))
for P in (2, 5, 8):
    Fp = block_map([1], P)
    x = 0
    for n in range(1, 30):
        x = Fp(x)
    ok57 &= strip_rate(Fp, P) == {P} and abs(x - 29 * P) == P - 1
F0 = lambda t: {0: 27, 3: 31}[t % 4] + 4 * (t // 4) if t % 4 in (0, 3) else None
x = 0
for n in range(1, 8):
    x = F0(x)
    ok57 &= x == 28 * n - 1
check('S57 G163: one winding rate per strip, the P - 1 error band, and the whole-block potential below 2(P - 1)', ok57)
def reset1(w, t, P):
    if not w:
        return t
    u = t
    while not (w >> (u % P)) & 1:
        u += 1
    return u + 1


ok58 = True
for trial in range(300):
    P = rng29.randint(1, 8)
    M = rng29.randint(1, 40)
    dr = [0 if rng29.random() < 0.15 else rng29.randint(1, (1 << P) - 1) for _ in range(M)]
    T = [0]
    for w in dr:
        T.append(reset1(w, T[-1], P))
    for gam in (_F57(1), _F57(5, 2)):
        D = max(T[b] - T[a] - gam * (b - a) for a in range(M + 1) for b in range(a, M + 1))
        for phi in range(P):
            sh = [((w >> phi) | (w << (P - phi))) & ((1 << P) - 1) for w in dr]
            for a in range(M + 1):
                for u in range(P):
                    x = u
                    for b in range(a, M + 1):
                        if b > a:
                            x = reset1(sh[b - 1], x, P)
                        ok58 &= x - u <= gam * (b - a) + D + P - 1
        beta = [0] + [rng29.randint(0, j) for j in range(1, M + 1)]
        f = 0
        for j in range(1, M + 1):
            f = max(beta[j], reset1(dr[j - 1], f, P))
            ok58 &= f <= gam * j + D + P - 1
for P in (2, 5, 8):
    ok58 &= reset1(1, 0, P) - 0 == 1 and reset1(1, 1, P) - 1 == P
check('S58 G164: one reference path bounds every interval, start, phase shift and birth-clamped front (+P - 1)', ok58)
def rep_path_nodes(Q):
    a, b, q = 0, (1 << Q) - 1, 1
    nodes = []
    while True:
        nodes.append((a, b, q))
        if b != 0:
            ch = edge_children(a, b, Q)
            a, b = b, ch[0]
            continue
        sig = bin(a & ((1 << q) - 1)).count('1') % 2
        if sig == 0 or q == Q:
            return nodes
        c, cs = 0, []
        for t in range(Q):
            cs.append(c)
            c ^= (a >> t) & 1
        a, b, q = b, sum(v << t for t, v in enumerate(cs)), 2 * q


ok59 = True
nodes59 = rep_path_nodes(16)
ok59 &= len(nodes59) == 53208
entries = {}
for k in range(1, len(nodes59)):
    q0, q1 = nodes59[k - 1][2], nodes59[k][2]
    if q1 != q0:
        a0, b0, _ = nodes59[k - 1]
        ok59 &= q1 == 2 * q0 and b0 == 0 and bin(a0 & ((1 << q0) - 1)).count('1') % 2 == 1
        entries[q1] = k
for a_, b_, q_ in nodes59:
    ok59 &= lp_bits(b_, 16) <= q_ and q_ % lp_bits(b_, 16) == 0 and lp_bits(a_, 16) <= q_
ok59 &= entries == {2: 3, 4: 8, 8: 29, 16: 400} and nodes59[-1][2] == 16 and nodes59[-1][1] == 0
check('S59 G165: the stage structure along the known Q = 16 path; entries 3, 8, 29, 400; the branch keeps period 16', ok59)
import os as _os60
import sys as _sys60
_sys60.path.insert(0, _os60.path.dirname(_os60.path.abspath(__file__)))
import rule30_hg4 as _hg4
from array import array as _arr60

ok60 = True
hz60 = {}
for q in (4, 6, 8):
    cnt = 1 << (2 * q)
    isv = bytearray(cnt)
    for v in range(cnt):
        isv[v] = 1 if (v == 0 or _hg4.gated(v, q)) else 0
    E60 = [(s_, t, 2 * d - 5) for s_, t, d in _hg4.aligned_edges(q) if isv[s_] and isv[t]]
    prev = _arr60('i', [0]) * cnt
    n = 0
    while True:
        n += 1
        cur = _arr60('i', [0]) * cnt
        for s_, t, w in E60:
            if w + prev[t] > cur[s_]:
                cur[s_] = w + prev[t]
        if cur == prev:
            break
        prev = cur
    first_stable = n - 1
    h = cur
    radj = {}
    for s_, t, w in E60:
        if h[s_] == w + h[t]:
            radj.setdefault(t, []).append(s_)
    dist = {v: 0 for v in range(cnt) if isv[v] and h[v] == 0}
    frontier = list(dist)
    while frontier:
        nxt = []
        for t in frontier:
            for s_ in radj.get(t, []):
                if s_ not in dist:
                    dist[s_] = dist[t] + 1
                    nxt.append(s_)
        frontier = nxt
    ok60 &= all(isv[v] == 0 or v in dist for v in range(cnt))
    hz60[q] = (first_stable, max(dist.values()))
    ok60 &= first_stable == max(dist.values())
ok60 &= hz60[4][0] == 4 and hz60[6][0] == 21 and hz60[8][0] == 85
for L in range(1, 13):
    wts = [-1, 1] * L + [1]
    hh = [0] * (len(wts) + 1)
    for i in range(len(wts) - 1, -1, -1):
        hh[i] = max(0, wts[i] + hh[i + 1])
    Hn = [0] * (len(wts) + 1)
    horizon = 0
    while Hn[0] != hh[0] or any(Hn[i] != hh[i] for i in range(len(wts) + 1)):
        Hn = [max(0, wts[i] + Hn[i + 1]) if i < len(wts) else 0 for i in range(len(wts) + 1)]
        horizon += 1
    ok60 &= max(hh) == 2 and horizon == 2 * L + 1
for q in (4, 8, 16):
    mq = (1 << q) - 1
    b = 1 << (q - 1)
    a = (((b >> 1) | (b << (q - 1))) & mq) ^ b
    ok60 &= b in edge_children(a, b, q) and reset_cost(b, 0, q) == (q, 0)
    ok60 &= (a >> (q - 1)) & 1 == 1 and (b >> (q - 1)) & 1 == 1
    ok60 &= edge_children(b, b, q) == [0]
check('S60 G166 addenda: tight-edge distance equals the stable horizon (4, 21, 85); the chain; the driver-only edge', ok60,
      'first stable horizon and max tight distance by q: %s' % hz60)
cyc61 = [9, 8, 14, 12, 4, 7, 6, 2, 11, 3, 1, 13]
tab61 = [(9, 13, 1, 3), (8, 9, 0, 4), (14, 8, 0, 2), (12, 14, 0, 3), (4, 12, 3, 4), (7, 4, 3, 2), (6, 7, 3, 3),
         (2, 6, 2, 4), (11, 2, 2, 2), (3, 11, 2, 3), (1, 3, 1, 4), (13, 1, 1, 2)]
ok61 = all(cyc61[(j + 1) % 12] in edge_children(cyc61[j - 1], cyc61[j], 4) for j in range(12))
ok61 &= [b for b, _, _, _ in tab61] == cyc61 and all(a == cyc61[j - 1] for j, (_, a, _, _) in enumerate(tab61))
ok61 &= all((a >> ((r - 1) % 4)) & 1 == 1 and reset_cost(b, r, 4)[0] == dl for b, a, r, dl in tab61)
ok61 &= sum(dl for _, _, _, dl in tab61) == 36
check('S61 G166 scope table: twelve gated maximum-delay phases on G8 cycle sum to 36, forcing gamma >= 3', ok61)
def block_delays(a, c, r, P):
    d = edge_children(0, c, P)[0]
    e = edge_children(c, d, P)[0]
    k1, r1 = reset_cost(c, r, P)
    k2, r2 = reset_cost(d, r1, P)
    k3, r3 = reset_cost(e, r2, P)
    return [0, k1, k2, k3]


def prefix_rewards(dl):
    out, tot = [0], 0
    for i, x in enumerate(dl):
        tot += x
        out.append(2 * tot - 5 * (i + 1))
    return out


ok62 = True
n62 = 0
for P in range(2, 11):
    for a in range(1, 1 << P):
        q = lp_bits(a, P)
        if bin(a & ((1 << q) - 1)).count('1') % 2:
            continue
        kids = edge_children(a, 0, P)
        if len(kids) != 2:
            continue
        for r in range(P):
            if not (a >> ((r - 1) % P)) & 1:
                continue
            for c in kids:
                l, m = run_pair(c, r, P)
                dl = block_delays(a, c, r, P)
                fast = (c >> r) & 1
                ok62 &= dl == ([0, 1, 1, l] if fast else [0, l + 1, 1, m])
                pr = prefix_rewards(dl)
                ok62 &= pr == ([0, -5, -8, -11, 2 * l - 16] if fast else [0, -5, 2 * l - 8, 2 * l - 11, 2 * (l + m) - 16])
                ok62 &= pr[-1] <= 2 * q - 16 and max(pr) <= max(0, 2 * q - 10)
                n62 += 1
lm = [(5, 1), (1, 4), (4, 2), (2, 3), (3, 1), (1, 5)]
ok62 &= max(max(2 * l - 16, 2 * (l + m) - 16) for l, m in lm) == -4
ok62 &= max(max(0, 2 * l - 8, 2 * (l + m) - 16) for l, m in lm) == 2
c8 = 1 << 7
a8 = c8 ^ (((c8 >> 1) | (c8 << 7)) & 0xFF)
slow8 = [k for k in edge_children(a8, 0, 8) if not (k >> 0) & 1][0]
pr8 = prefix_rewards(block_delays(a8, slow8, 0, 8))
ok62 &= pr8[-1] == 0 and pr8[2] == 6 and 2 * reset_cost(slow8, 0, 8)[0] - 5 == 11
check('S62 G167: branch-block delays and prefix rewards; block <= 2q - 16; the rooted control; the q = 8 counterexample',
      ok62, '%d gated sibling cases' % n62)
def lift_check(rewards, blocks):
    """rewards[i] is the reward of edge i (vertex i -> i + 1); blocks are disjoint start indices of 4-edge blocks."""
    n = len(rewards)
    bset = {}
    for b0 in blocks:
        bset[b0] = b0 + 4
    ret = [v for v in range(n + 1) if not any(b0 < v < b0 + 4 for b0 in blocks)]
    K = {ret[-1]: 0}
    for i in range(len(ret) - 2, -1, -1):
        v, u = ret[i], ret[i + 1]
        w = sum(rewards[v:u])
        K[v] = max(0, w + K[u])
    A = max([0] + [sum(rewards[b0:b0 + j]) for b0 in blocks for j in range(1, 5)])
    B = max([0] + [sum(rewards[i:j]) for b0 in blocks for i in range(b0, b0 + 4) for j in range(i + 1, b0 + 5)])
    h = {}
    for v in ret:
        h[v] = K[v] + A
    for b0 in blocks:
        for v in range(b0 + 3, b0, -1):
            h[v] = max(0, rewards[v] + h[v + 1])
    ok = all(h[v] >= rewards[v] + h[v + 1] for v in range(n)) and min(h.values()) >= 0
    return ok and max(h.values()) <= max(K.values()) + A + B, h


ok63 = True
for trial in range(500):
    nb = rng29.randint(0, 4)
    rewards, blocks = [], []
    for k in range(nb + 1):
        rewards += [rng29.randint(-6, 4) for _ in range(rng29.randint(0, 5))]
        if k < nb:
            blocks.append(len(rewards))
            rewards += [rng29.randint(-6, 12) for _ in range(4)]
    if not rewards:
        continue
    ok63 &= lift_check(rewards, blocks)[0]
for P in range(2, 11):
    for a in range(1, 1 << P):
        q = lp_bits(a, P)
        if bin(a & ((1 << q) - 1)).count('1') % 2:
            continue
        kids = edge_children(a, 0, P)
        if len(kids) != 2:
            continue
        for r in range(P):
            if not (a >> ((r - 1) % P)) & 1:
                continue
            for c in kids:
                rw = [2 * x - 5 for x in block_delays(a, c, r, P)]
                ok63 &= max([0] + [sum(rw[:j]) for j in range(1, 5)]) <= max(0, 2 * q - 10)
                ok63 &= max([0] + [sum(rw[i:j]) for i in range(4) for j in range(i + 1, 5)]) <= max(0, 2 * q - 5)
okl, h63 = lift_check([-5, 11, -3, -3], [0])
ok63 &= okl and [h63[v] for v in range(5)] == [6, 11, 0, 3, 6]
check('S63 G168: one shared reserve lifts contracted block certificates; the G167 reserves A and B; the q = 8 lift', ok63)
def Dd(w, r, P):
    return reset_cost(w, r, P)[0] if w else 0


def gated3(a, b, r, P):
    if a:
        return (a >> ((r - 1) % P)) & 1 == 1
    return ((b >> (r % P)) & 1) ^ ((b >> ((r - 1) % P)) & 1) == 1


def tri(a, b, r, P):
    return (Dd(a, r, P), Dd(b, r, P), Dd(a ^ b, r, P))


ok64 = True
ok64 &= 8 in edge_children(12, 8, 4) and edge_children(8, 8, 4) == [0]
ok64 &= gated3(12, 8, 0, 4) and gated3(8, 8, 0, 4) and reset_cost(8, 0, 4) == (4, 0)
ok64 &= tri(12, 8, 0, 4) == (3, 4, 3) and tri(8, 8, 0, 4) == (4, 4, 0)
ok64 &= 14 in edge_children(9, 0, 4) and gated3(9, 0, 0, 4) and gated3(0, 14, 0, 4)
ok64 &= tri(9, 0, 0, 4) == (1, 0, 1) and tri(0, 14, 0, 4) == (0, 2, 2)
for q in (4, 8, 16):
    b = 1 << (q - 1)
    ok64 &= edge_children(b, b, q) == [0] and gated3(b, b, 0, q) and gated3(b, 0, 0, q)
    ok64 &= reset_cost(b, 0, q) == (q, 0) and tri(b, b, 0, q) == (q, q, 0) and tri(b, 0, 0, q) == (q, 0, q)
# inequalities h(src) >= reward + h(tgt) with h = alpha D(a) + beta D(b) + chi D(a^b):
#   edge 1: (3,4,3) - (4,4,0) >= 3  ->  -alpha + 3 chi >= 3
#   edge 2: (1,0,1) - (0,2,2) >= -5 ->  alpha - 2 beta - chi >= -5
#   pulse:  (q,q,0) - (q,0,q) >= 2q - 5 -> q (beta - chi) >= 2q - 5
lhs1 = tuple(x - y for x, y in zip((3, 4, 3), (4, 4, 0)))
lhs2 = tuple(x - y for x, y in zip((1, 0, 1), (0, 2, 2)))
ok64 &= lhs1 == (-1, 0, 3) and lhs2 == (1, -2, -1)
sumv = tuple(x + y for x, y in zip(lhs1, lhs2))
ok64 &= sumv == (0, -2, 2) and 3 + (-5) == -2                     # 2 (chi - beta) >= -2, i.e. beta - chi <= 1
ok64 &= _F57(2 * 8 - 5, 8) > 1                                     # q = 8 needs beta - chi >= 11/8 > 1
check('S64 G169: three explicit gated edges make the shared three-distance potential infeasible at q = 4 and 8', ok64)
def rep4(w4, q):
    return sum(w4 << (4 * k) for k in range(q // 4))


ok65 = True
for q in (8, 16):
    A1, B1, C1 = rep4(12, q), rep4(8, q), rep4(0, q)
    A2, B2, C2 = rep4(9, q), rep4(0, q), rep4(14, q)
    ok65 &= B1 in edge_children(A1, B1, q) and C2 in edge_children(A2, B2, q)
    ok65 &= edge_children(B1, B1, q) == [C1] and gated3(A1, B1, 0, q) and gated3(B1, B1, 0, q)
    ok65 &= gated3(A2, B2, 0, q) and gated3(B2, C2, 0, q)
    ok65 &= reset_cost(B1, 0, q)[0] == 4 and tri(A1, B1, 0, q) == (3, 4, 3) and tri(B1, B1, 0, q) == (4, 4, 0)
    ok65 &= tri(A2, B2, 0, q) == (1, 0, 1) and tri(B2, C2, 0, q) == (0, 2, 2)
    for gam in (_F57(5, 2), _F57(3 * q, q + 1) - _F57(1, 1000), _F57(3 * q, q + 1)):
        rhs = _F57(q, 2) * (8 - 2 * gam) + _F57(q, 2) * (-2 * gam) + (2 * q - 2 * gam)
        ok65 &= rhs == 6 * q - 2 * gam * (q + 1)
        ok65 &= (rhs > 0) == (gam < _F57(3 * q, q + 1))
ok65 &= _F57(3 * 8, 9) == _F57(8, 3) > _F57(5, 2) and _F57(12, 5) < _F57(5, 2)
check('S65 G170: embedded period-4 edges plus the pulse force gamma >= 3q/(q + 1) on the shared three-distance family', ok65)
def Sw(w, q):
    return ((w >> 1) | (w << (q - 1))) & ((1 << q) - 1)


ok66 = True
for q in (16, 32, 64):
    b = (1 << 3) | (1 << 7) | (1 << (q - 1))
    a = Sw(b, q) ^ b
    ok66 &= b in edge_children(a, b, q) and gated3(a, b, 0, q) and reset_cost(b, 0, q) == (4, 4)
    ok66 &= gated3(b, b, 4, q) and tri(a, b, 0, q) == (3, 4, 3) and tri(b, b, 4, q) == (4, 4, 0)
    c = (1 << 1) | (1 << (q - 1))
    a2 = Sw(c, q) ^ c
    ok66 &= c in edge_children(a2, 0, q) and gated3(a2, 0, 0, q) and gated3(0, c, 0, q)
    ok66 &= tri(a2, 0, 0, q) == (1, 0, 1) and tri(0, c, 0, q) == (0, 2, 2)
    pb = 1 << (q - 1)
    ok66 &= edge_children(pb, pb, q) == [0] and tri(pb, pb, 0, q) == (q, q, 0) and tri(pb, 0, 0, q) == (q, 0, q)
    ok66 &= all(lp_bits(w, q) == q for w in (a, b, a2, c, pb))
    if q == 16:
        ok66 &= (b, a, c, a2, pb) == (32904, 49356, 32770, 49155, 32768)
check('S66 G171: exact-period witnesses keep the three constraints, so least-period coefficients cannot escape', ok66)
def pair_lp(a, b, q):
    for d in range(1, q + 1):
        if q % d == 0 and hg_rot(a, d, q) == a and hg_rot(b, d, q) == b:
            return d


def hg_rot(w, d, q):
    d %= q
    return ((w >> d) | (w << (q - d))) & ((1 << q) - 1)


ok67 = True
cases = [(4, 15, 12, 2)]
for q in (8, 16, 32, 64):
    b = (1 << 2) | (1 << 3) | (1 << (q - 1))
    c = (1 << 1) | (1 << 5) | (1 << (q - 1))
    a = Sw(c, q) ^ (b | c)
    cases.append((q, a, b, c))
for q, a, b, c in cases:
    ok67 &= c in edge_children(a, b, q) and gated3(a, b, 0, q)
    k, r2 = reset_cost(b, 0, q)
    ok67 &= k == 3 and r2 == 3 and gated3(b, c, 3, q)
    ok67 &= tri(a, b, 0, q) == (1, 3, 1) and tri(b, c, 3, q) == (1, 3, 1)
    ok67 &= pair_lp(a, b, q) == q and pair_lp(b, c, q) == q
    if q == 8:
        ok67 &= (a, b, c) == (255, 140, 162) and (hg_rot(b, 3, 8), hg_rot(c, 3, 8)) == (145, 84)
    if q == 4:
        ok67 &= (hg_rot(b, 3, 4), hg_rot(c, 3, 4)) == (9, 4)
check('S67 G173: a gated edge with identical (1, 3, 1) features, cost 3 and pair period q at every q = 4..64', ok67)
from rule30_gpt_local_front import predecessor as predecessor_gpt
chain68 = [(0, 15), (15, 15), (15, 0), (0, 5), (5, 15), (15, 5), (5, 5), (5, 0), (0, 9), (9, 15), (15, 12)]
ok68 = all(chain68[i + 1][1] in edge_children(chain68[i][0], chain68[i][1], 4) and chain68[i + 1][0] == chain68[i][1]
           for i in range(len(chain68) - 1))
x = (15 << 4) | 12
back = []
while x != (0 << 4) | 15:
    back.append(x)
    x = predecessor_gpt(x, 4)
back.append(x)
ok68 &= [(v >> 4, v & 15) for v in reversed(back)] == chain68
arr = []
for t0 in range(4):
    t = t0
    for a_, b_ in chain68[:-1]:
        if b_:
            while not (b_ >> (t % 4)) & 1:
                t += 1
            t += 1
    arr.append(t)
ok68 &= arr == [9, 13, 13, 13] and all(t % 4 == 1 for t in arr)
ok68 &= tri(15, 12, 1, 4) == (1, 2, 1) and reset_cost(12, 1, 4) == (2, 3) and tri(12, 2, 3, 4) == (1, 3, 1)
ok68 &= gated3(15, 12, 0, 4) and tri(15, 12, 0, 4) == (1, 3, 1)
check('S68 G174: the root chain to (15, 12) reaches it only at phase 1, where the (1, 3, 1) self-loop is absent', ok68,
      'root-clock arrivals %s' % arr)
ok69 = True
chain69 = [((183 << 8) | 176)]
while chain69[-1] != 255:
    chain69.append(predecessor_gpt(chain69[-1], 8))
    if len(chain69) > 1000:
        break
ok69 &= len(chain69) - 1 == 190 and chain69[-1] == 255
pairs69 = [(v >> 8, v & 255) for v in reversed(chain69)] + [(176, 26)]
ok69 &= all(pairs69[i + 1][1] in edge_children(pairs69[i][0], pairs69[i][1], 8) and pairs69[i + 1][0] == pairs69[i][1]
            for i in range(len(pairs69) - 1))
ok69 &= (hg_rot(176, 5, 8), hg_rot(26, 5, 8)) == (133, 208)
for t0 in range(8):
    t = t0
    arrive = []
    for a_, b_ in pairs69[:-1]:
        if b_:
            while not (b_ >> (t % 8)) & 1:
                t += 1
            t += 1
        arrive.append(t)
    ok69 &= arrive[-2] == 360 and arrive[-1] == 365
ok69 &= gated3(183, 176, 0, 8) and gated3(176, 26, 5, 8)
ok69 &= tri(183, 176, 0, 8) == (1, 5, 1) and tri(176, 26, 5, 8) == (1, 5, 1)
ok69 &= pair_lp(183, 176, 8) == 8 and pair_lp(176, 26, 8) == 8
ok69 &= 26 not in edge_children(183 ^ 1, 176, 8)
check('S69 G176: the reached q = 8 collision edge, its 190-step root chain, and arrivals 360, 365 from every root residue', ok69)
import rule30_rq3 as _rq3
import rule30_rqo as _rqo
_root70, _depth70, _par70, _edges70, _ = _rq3.reached(8)
_eset70 = {(s_, t_): d_ for s_, t_, d_ in _edges70}
seg70 = [((143, 26), (134, 186), 2), ((134, 186), (174, 62), 2), ((174, 62), (143, 200), 2), ((143, 200), (140, 168), 4),
         ((140, 168), (138, 140), 4), ((182, 84), (138, 152), 3), ((138, 152), (137, 206), 4)]
labels70 = [(1, 2, 1, 8, 8, 8, 7), (2, 2, 3, 8, 8, 8, 5), (2, 2, 5, 8, 8, 8, 7), (1, 4, 1, 8, 8, 8, 7), (3, 4, 3, 8, 8, 8, 7),
            (2, 3, 2, 8, 8, 8, 7), (2, 4, 2, 8, 8, 8, 7), (1, 2, 1, 8, 8, 8, 7)]
ok70 = all(_eset70.get((s_, t_)) == d_ for s_, t_, d_ in seg70)
ok70 &= [_depth70[seg70[0][0]], _depth70[seg70[5][0]]] == [270, 318]
ok70 &= sum(d_ for _, _, d_ in seg70) == 21 and 2 * 21 - 5 * 7 == 7
ok70 &= all(_rqo.feat(seg70[i][0], 8) == labels70[i] for i in range(7)) and _rqo.feat(seg70[6][1], 8) == labels70[7]
ok70 &= all(_rqo.feat(seg70[i][1], 8) == labels70[i + 1] for i in range(7))
ok70 &= seg70[4][1] != seg70[5][0] and seg70[6][1] != seg70[0][0] and labels70[0] == labels70[7]
check('S70 G178: seven reached edges close in refined feature space with cost 21, through two false joins (gamma >= 3)', ok70)
def lift71(n, E):
    """E: list of (s, t, w) on vertices 0..n-1 forming a DAG with edges s < t."""
    out = {}
    for i, (s_, t_, w_) in enumerate(E):
        out.setdefault(s_, []).append(i)
    K = {}
    for i in sorted(range(len(E)), key=lambda i: -E[i][1]):
        t_ = E[i][1]
        K[i] = max([0] + [E[f][2] + K[f] for f in out.get(t_, [])])
    W = max([0] + [w_ for _, _, w_ in E])
    h = {v: max([0] + [E[i][2] + K[i] for i in out.get(v, [])]) for v in range(n)}
    ok = all(K[i] >= E[f][2] + K[f] for i in range(len(E)) for f in out.get(E[i][1], []))
    ok &= all(h[s_] >= w_ + h[t_] for s_, t_, w_ in E) and all(0 <= h[v] <= W + max([0] + list(K.values())) for v in h)
    ok &= all(h[E[i][1]] >= E[f][2] + h[E[f][1]] for i in range(len(E)) for f in out.get(E[i][1], []))
    return ok, h


ok71 = True
for trial in range(300):
    n = rng29.randint(2, 9)
    E = [(a_, b_, rng29.randint(-6, 6)) for a_ in range(n) for b_ in range(a_ + 1, n) if rng29.random() < 0.35]
    if E:
        ok71 &= lift71(n, E)[0]
okt, ht = lift71(2, [(0, 1, 5)])
ok71 &= okt and (ht[0], ht[1]) == (5, 0)
fe = [(labels70[i], labels70[i + 1], 2 * seg70[i][2] - 5) for i in range(7)]
ok71 &= all(fe[i][1] == fe[(i + 1) % 7][0] for i in range(7)) and sum(w_ for _, _, w_ in fe) == 7
ok71 &= sum(fe[(i + 1) % 7][2] for i in range(7)) == 7
check('S71 G179: the line-graph lift and its converse on random DAGs; the terminal control; post-compression cycle kept', ok71)
import copy as _cp72
import hashlib as _hl72
import json as _js72
import sys as _sys72
import traceback as _tb72
import rule30_rc2 as _rc72

_SHA72 = 'f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7'


def cert72():
    """The RC2 certificate rebuilt in memory exactly as rule30_rc2_export.py writes it (c5d24a0)."""
    out = {'producer': 'tests/probes/lexicon/rule30_rc2_export.py', 'note': 'regenerated (RC2 kept no arrays)'}
    for q in (1, 2, 4, 8):
        root, depth, parent, edges, exits = _rq3.reached(q)
        verts = sorted(depth, key=lambda s: (depth[s], s))
        vid = {s: i for i, s in enumerate(verts)}
        eidx = {(s, t, d): i for i, (s, t, d) in enumerate(edges)}
        lab = {s: _rqo.feat(s, q) for s in depth}
        feas, K, quot, cyc, n_arcs, L = _rc72.context_test(edges, lambda v: lab[v], lambda e: 2 * e[2] - 5)
        ok, h = _rc72.lift(edges, L, K, lambda e: 2 * e[2] - 5, list(depth))
        vrows = [{'state': list(s), 'parent_edge': None if parent[s] is None else
                  eidx[(parent[s][0], s, parent[s][1])]} for s in verts]
        out[str(q)] = {'root': vid[root], 'vertices': vrows,
                       'edges': [{'source': vid[s], 'target': vid[t], 'delay': d} for s, t, d in edges],
                       'K': [{'label': [list(x[0]), list(x[1])], 'K': K[x]} for x in sorted(K)],
                       'summary': {'vertices': len(verts), 'edges': len(edges), 'labels': len(K), 'cap_exits': exits,
                                   'K_max': max(K.values()), 'h_max': max(h.values())}}
    return out


_raw72 = _js72.dumps(cert72(), sort_keys=True, separators=(',', ':')).encode()
ok72 = _hl72.sha256(_raw72).hexdigest() == _SHA72 and len(_raw72) == 56232
# GPT's checker, unmodified except int.bit_count (Python 3.10) where this interpreter lacks it.
_src72 = open(_os60.path.join(_os60.path.dirname(_os60.path.abspath(__file__)),
                              'rule30_rc2_certificate_check.py')).read()
if _sys72.version_info < (3, 10):                      # GPT's checker dropped it at 25a64b5; kept for older copies
    ok72 &= _src72.count('a.bit_count()') <= 1
    _src72 = _src72.replace('a.bit_count()', "bin(a).count('1')")
_ns72 = {'__name__': 'rc2_certificate_check'}
exec(compile(_src72, 'rule30_rc2_certificate_check.py', 'exec'), _ns72)
_data72 = _js72.loads(_raw72)


def verdict72(d, q):
    """None if GPT's verify accepts; else the checker line that rejected (an AssertionError only)."""
    try:
        _ns72['verify'](d, q)
        return None
    except AssertionError:
        return _src72.splitlines()[_tb72.extract_tb(_sys72.exc_info()[2])[-1].lineno - 1].strip()
    except Exception as ex_:
        return 'non-assert %s' % type(ex_).__name__


import contextlib as _cl72
import io as _io72
with _cl72.redirect_stdout(_io72.StringIO()):
    ok72 &= all(verdict72(_data72[str(q)], q) is None for q in (1, 2, 4, 8))


def mutate72(fn):
    d = _cp72.deepcopy(_data72['8'])
    fn(d)
    with _cl72.redirect_stdout(_io72.StringIO()):
        return verdict72(d, 8)


_st72 = [tuple(v['state']) for v in _data72['8']['vertices']]
_e143 = next(i for i, e in enumerate(_data72['8']['edges'])
             if (_st72[e['source']], _st72[e['target']]) == ((143, 26), (134, 186)))


def drop_edge72(d):
    del d['edges'][_e143]
    for v in d['vertices']:
        if v['parent_edge'] is not None and v['parent_edge'] > _e143:
            v['parent_edge'] -= 1
        elif v['parent_edge'] == _e143:
            v['parent_edge'] = None


def zero_k72(d):
    for r in d['K']:
        r['K'] = 0


def tight_k72(d):
    next(r for r in d['K'] if r['K'] == 14)['K'] = 13


def delay72(d):
    next(e for e in d['edges'] if e['delay'] == 2)['delay'] = 3


def drop_terminal72(d):
    st = [tuple(v['state']) for v in d['vertices']]
    outs = {e['source'] for e in d['edges']}
    lab = {}
    e = next(e for e in d['edges'] if e['target'] not in outs)
    tl = [list(_ns72_phi(st[e['source']])), list(_ns72_phi(st[e['target']]))]
    d['K'] = [r for r in d['K'] if r['label'] != tl]


def _ns72_phi(s):
    return _rqo.feat(s, 8)


def summary72(d):
    d['summary']['h_max'] = 13


def orphan72(d):
    have = {tuple(v['state']) for v in d['vertices']}
    s = next((a, b) for a in range(256) for b in range(256) if (a, b) not in have and a & 128)
    d['vertices'].append({'state': list(s), 'parent_edge': None})


def permute72(d):
    """Positive control: reversing the edge list and the K rows (parent indices remapped) must still pass."""
    n = len(d['edges'])
    d['edges'].reverse()
    d['K'].reverse()
    for v in d['vertices']:
        if v['parent_edge'] is not None:
            v['parent_edge'] = n - 1 - v['parent_edge']


def drop_nontree72(d):
    tree = {v['parent_edge'] for v in d['vertices']}
    i = next(i for i in range(len(d['edges'])) if i not in tree)
    del d['edges'][i]
    for v in d['vertices']:
        if v['parent_edge'] is not None and v['parent_edge'] > i:
            v['parent_edge'] -= 1


_mut72 = [('zero K', zero_k72, 'K[L[i]]>=w+K[L[j]]'), ('the known edge removed', drop_edge72, 'edges[pe][1]==i'),
          ('a non-tree edge removed', drop_nontree72, 'actual==expected'),
          ('one tight K lowered', tight_k72, 'K[L[i]]>=w+K[L[j]]'), ('one delay changed', delay72, 'd==D(b)'),
          ('terminal label dropped', drop_terminal72, 'set(K)==set(L)'),
          ('summary h max', summary72, 'summary[key]==value'), ('unreached vertex added', orphan72, 'type(pe)==int')]
_rej72 = {name: mutate72(fn) for name, fn, _ in _mut72}
ok72 &= all(isinstance(_rej72[name], str) and frag in _rej72[name] for name, _, frag in _mut72)
ok72 &= mutate72(permute72) is None


def least72(cert, q):
    """Exact least nonnegative potential on the certified edge list itself (longest path, Bellman-Ford)."""
    E = [(e['source'], e['target'], 2 * e['delay'] - 5) for e in cert['edges']]
    h = [0] * len(cert['vertices'])
    for r in range(len(h) + 2):
        ch = False
        for s, t, w in E:
            if w + h[t] > h[s]:
                h[s], ch = w + h[t], True
        if not ch:
            return h
    return None


_least72 = {q: least72(_data72[str(q)], q) for q in (1, 2, 4, 8)}
ok72 &= all(_least72[q] is not None for q in _least72)
ok72 &= [max(_least72[q]) for q in (1, 2, 4, 8)] == [0, 0, 1, 14]
# the K lift dominates the least potential; the q = 8 maximum is attained once, by an actual 8-edge reached path
_c72 = _data72['8']
_s72 = [tuple(v['state']) for v in _c72['vertices']]
_l72 = _least72[8]
_hk72 = [0] * len(_s72)
_k72 = {(tuple(r['label'][0]), tuple(r['label'][1])): r['K'] for r in _c72['K']}
for e in _c72['edges']:
    _hk72[e['source']] = max(_hk72[e['source']], 2 * e['delay'] - 5 +
                             _k72[(_rqo.feat(_s72[e['source']], 8), _rqo.feat(_s72[e['target']], 8))])
ok72 &= all(_hk72[i] >= _l72[i] for i in range(len(_s72))) and max(_hk72) == 14
ok72 &= sum(x > y for x, y in zip(_hk72, _l72)) == 14 and max(x - y for x, y in zip(_hk72, _l72)) == 5
_i72 = [i for i in range(len(_l72)) if _l72[i] == 14]
ok72 &= len(_i72) == 1 and _s72[_i72[0]] == (143, 200)
_p72, _w72 = [_i72[0]], []
while _l72[_p72[-1]] > 0:
    e = next(e for e in _c72['edges'] if e['source'] == _p72[-1] and 2 * e['delay'] - 5 + _l72[e['target']]
             == _l72[_p72[-1]])
    _w72.append(2 * e['delay'] - 5)
    _p72.append(e['target'])
ok72 &= _w72 == [3, 3, 1, -3, 5, -3, 3, 5] and _s72[_p72[-1]] == (132, 215)
ok72 &= [_depth70[_s72[_p72[0]]], _depth70[_s72[_p72[-1]]]] == [273, 281]
check('S72 G182: the certificate rebuilt byte-identical; GPT checker accepts it and rejects eight real corruptions at '
      'the intended assertion; the finite budget 14 is exact', ok72)
_rng73 = random.Random(183)


def bf73(m, arcs, init=None):
    """Least nonnegative label potential above init by longest-path relaxation; None on a positive cycle."""
    F = list(init) if init else [0] * m
    for _ in range(m + 2):
        ch = False
        for x, y, w in arcs:
            if w + F[y] > F[x]:
                F[x], ch = w + F[y], True
        if not ch:
            return F
    return None


def walkmax73(m, arcs, x):
    """Maximum reward over simple label paths from x (the empty path included), by exhaustive search."""
    out = {}
    for a, b, w in arcs:
        out.setdefault(a, []).append((b, w))
    best = 0

    def go(v, seen, tot):
        nonlocal best
        best = max(best, tot)
        for b, w in out.get(v, []):
            if b not in seen:
                go(b, seen | {b}, tot + w)
    go(x, {x}, 0)
    return best


ok73, _n73 = True, [0, 0]
for trial in range(400):
    n = _rng73.randint(2, 6)
    E = [(a_, b_, _rng73.randint(-4, 3)) for a_ in range(n) for b_ in range(n) if _rng73.random() < 0.3][:11]
    if not E:
        continue
    m = _rng73.randint(1, n)
    lab = [_rng73.randrange(m) for _ in range(n)]
    arcs = [(lab[a_], lab[b_], w_) for a_, b_, w_ in E]
    Fl = bf73(m, arcs)
    # independent side: some subset of actual edges is balanced at every label and has positive total reward
    pos = False
    for mask in range(1, 1 << len(E)):
        sub = [arcs[i] for i in range(len(E)) if mask >> i & 1]
        bal = [0] * m
        for x, y, _ in sub:
            bal[x] += 1
            bal[y] -= 1
        if not any(bal) and sum(w_ for _, _, w_ in sub) > 0:
            pos = True
            break
    ok73 &= (Fl is None) == pos
    _n73[pos] += 1
    if Fl is not None:
        H = [walkmax73(m, arcs, x) for x in range(m)]
        ok73 &= Fl == H and all(H[x] >= w_ + H[y] for x, y, w_ in arcs)
        G = bf73(m, arcs, [_rng73.randint(0, 5) for _ in range(m)])
        ok73 &= G is not None and all(G[x] >= H[x] for x in range(m)) and all(G[x] >= w_ + G[y] for x, y, w_ in arcs)
ok73 &= min(_n73) >= 50
# G183's control: s -> t -> u with rewards +1, -1 and phi(s) = phi(u) = A, phi(t) = B is feasible with F = (1, 0)
ok73 &= bf73(2, [(0, 1, 1), (1, 0, -1)]) == [1, 0]
# the Rule 30 collections: G176's reached q = 8 edge is balanced alone in RQ3's labels (cost 5), not in RQO's
_e76 = ((183, 176), (133, 208), 5)
ok73 &= _rq3.feat(_e76[0], 8) == _rq3.feat(_e76[1], 8) and _rqo.feat(_e76[0], 8) != _rqo.feat(_e76[1], 8)
ok73 &= _e76 in set(_edges70)
# DQ3's q = 4 edge (15, 12) -> (9, 4), delay 3: literal, equal three-distance labels, so slope >= 3 at q = 4
_c73 = _rq3.rot(4, -3, 4)
ok73 &= _c73 in _rq3.children_brute(15, 12, 4) and (_rq3.rot(12, 3, 4), _rq3.rot(_c73, 3, 4)) == (9, 4)
ok73 &= _rq3.feat((15, 12), 4)[:3] == _rq3.feat((9, 4), 4)[:3] == (1, 3, 1) and _rq3.D(12, 4) == 3
# G178's seven reached edges: balanced at every RQO label, unbalanced at exactly four actual states, elapsed 21
_lb73, _sb73 = {}, {}
for s_, t_, d_ in seg70:
    for key, v in ((_rqo.feat(s_, 8), 1), (_rqo.feat(t_, 8), -1)):
        _lb73[key] = _lb73.get(key, 0) + v
    _sb73[s_] = _sb73.get(s_, 0) + 1
    _sb73[t_] = _sb73.get(t_, 0) - 1
ok73 &= not any(_lb73.values()) and sorted(k for k, v in _sb73.items() if v) == [(137, 206), (138, 140), (143, 26),
                                                                                  (182, 84)]
ok73 &= sum(d_ for _, _, d_ in seg70) == 21
ok73 &= all(sum(d_ - g for _, _, d_ in seg70) > 0 for g in (_Fr(5, 2), _Fr(29, 10)))   # slopes below 3 fail
check('S73 G183: feasibility iff no positive label-balanced edge set (400 random graphs, brute force); least potential '
      '= best walk; the merged-endpoint control; G176, DQ3 and G178 collections balanced at labels only', ok73)
_rng74 = random.Random(184)
# the recorded entries N_j (first node of least pair period 2^j), read off RQ3's reached graphs independently
_N74, ok74 = {}, True
for q in (2, 4, 8):
    _rt, _dp, _pa, _ed, _ex = _rq3.reached(q)
    _N74[q.bit_length() - 1] = min(_dp[s] for s in _dp if _rq3.pair_lp(s[0], s[1], q) == q)
    _by74 = {}
    for s in _dp:
        _by74.setdefault(_dp[s], []).append(s)
    # unbranched: states sharing a depth are temporal rotations of one another (non-genuine copies)
    ok74 &= all(any((_rq3.rot(s[0], k, q), _rq3.rot(s[1], k, q)) == v[0] for k in range(q)) for v in _by74.values()
                for s in v)
    if q == 8:
        ok74 &= _ex == 1
        _N74[4] = max(_dp.values()) + 1                  # the single cap exit: the next node doubles to 16
ok74 &= [_N74[j] for j in (1, 2, 3, 4)] == [3, 8, 29, 400]
# no history stays at period <= 8: each reached graph is acyclic (Kahn's order covers it) with one sink, its cap exit
for q in (1, 2, 4, 8):
    _rt, _dp, _pa, _ed, _ex = _rq3.reached(q)
    _ind74, _out74 = {s: 0 for s in _dp}, {}
    for s_, t_, _ in _ed:
        _ind74[t_] += 1
        _out74.setdefault(s_, []).append(t_)
    _st74, _k74 = [s for s in _dp if not _ind74[s]], 0
    while _st74:
        s_ = _st74.pop()
        _k74 += 1
        for t_ in _out74.get(s_, []):
            _ind74[t_] -= 1
            if not _ind74[t_]:
                _st74.append(t_)
    ok74 &= _k74 == len(_dp) and [_dp[s] for s in _dp if s not in _out74] == [max(_dp.values())]
_R74 = {j: _Fr(_N74[j], 2 ** j) for j in _N74}
_l74 = {j: _Fr(_N74[j + 1] - _N74[j], 2 ** j) for j in (1, 2, 3)}
ok74 &= [_R74[j] for j in (1, 2, 3, 4)] == [_Fr(3, 2), 2, _Fr(29, 8), 25]
ok74 &= [_l74[j] for j in (1, 2, 3)] == [_Fr(5, 2), _Fr(21, 4), _Fr(371, 8)]
ok74 &= all(_R74[j + 1] == (_R74[j] + _l74[j]) / 2 for j in (1, 2, 3))
ok74 &= _R74[4] == _Fr(1, 8) * _R74[1] + sum(_Fr(1, 2 ** (4 - i)) * _l74[i] for i in (1, 2, 3))


def sched74(R0, lam, n):
    R = [_Fr(R0)]
    for j in range(n):
        R.append((R[-1] + lam(j)) / 2)
    return R


# the recurrence's closed form and the window bound on random nonnegative schedules
for trial in range(200):
    lam = [_Fr(_rng74.randint(0, 40), 2 ** _rng74.randint(0, 3)) for _ in range(30)]
    R = sched74(_rng74.randint(0, 9), lambda j: lam[j], 30)
    ok74 &= all(R[j] == _Fr(R[0], 2 ** j) + sum(_Fr(1, 2 ** (j - i)) * lam[i] for i in range(j)) for j in range(31))
    m = _rng74.randint(1, 6)
    ok74 &= all(R[j] >= _Fr(sum(lam[j - m:j]), 2 ** m) for j in range(m, 31))
# counterfactual: constant normalized stage length C = 3 from R = 100 tends to C, not to infinity
R = sched74(100, lambda j: 3, 60)
ok74 &= all(R[j] == 3 + _Fr(97, 2 ** j) for j in range(61)) and R[60] - 3 < _Fr(1, 10 ** 15)
# the unexpected check: lambda = 1 at even j, j at odd j still diverges, with G184's two bounds
R = sched74(0, lambda j: 1 if j % 2 == 0 else j, 400)
ok74 &= all(R[j] >= (_Fr(j - 1, 2) if (j - 1) % 2 else _Fr(j - 2, 4)) for j in range(3, 401))
ok74 &= R[400] > 99 and all(R[j] >= _Fr(sum(1 if i % 2 == 0 else i for i in (j - 2, j - 1)), 4) for j in range(2, 401))
# the period-to-depth ratio on a stage peaks at its entry: max over k in [N_j, N_j+1) of 2^j / k = 1 / R_j
ok74 &= all(max(_Fr(2 ** j, k) for k in range(_N74[j], _N74[j + 1])) == 1 / _R74[j] for j in (1, 2, 3))
check('S74 G184: entries 3, 8, 29, 400 recomputed from the reached graphs (unbranched); R and lambda exact; the '
      'recurrence, window bound and both synthetic schedules', ok74)
def nu75(w, n):
    k = 0
    while w:
        w = w ^ _rq3.rot(w, 1, n)                       # Delta = I + S, S w(t) = w(t + 1), on the n-cycle
        k += 1
        if k > n:
            return None
    return k


def lp75(w, n):
    return next(d for d in range(1, n + 1) if n % d == 0 and _rq3.rot(w, d, n) == w)


def g185(q):
    """G185's prefix a, 0, c, 1, e, f on the 2q-cycle, words as integers (bit t = time t)."""
    n = 2 * q
    bits = [0] * (q - 2) + [1, 0] + [1] * (q - 2) + [0, 1]
    c = sum(b << t for t, b in enumerate(bits))
    one = (1 << n) - 1
    a = c ^ _rq3.rot(c, 1, n)
    e = one ^ _rq3.rot(c, -1, n)
    kids = _rq3.children(one, e, n)
    return n, a, c, one, e, kids


def compat75(x, y, z, n):
    return _rq3.rot(z, 1, n) == x ^ (y | z)


ok75 = True
for q in (4, 8, 16, 32, 64):
    n, a, c, one, e, kids = g185(q)
    ok75 &= len(kids) == 1
    f = kids[0]
    seq = [a, 0, c, one, e, f]
    ok75 &= all(compat75(seq[i], seq[i + 1], seq[i + 2], n) for i in range(4))
    ok75 &= [nu75(w, n) for w in seq] == [q, 0, q + 1, 1, q + 1, 2 * q]
    ok75 &= lp75(a, n) == q and all(lp75(w, n) == n for w in (c, e, f))
    ok75 &= [(a >> t) & 1 for t in range(q)] == [0] * (q - 3) + [1, 1, 1]
    ok75 &= bin(f & ((1 << n) - 1)).count('1') == q // 2 + 1
    pairs = list(zip(seq, seq[1:]))[1:]                  # (0, c), (c, 1), (1, e), (e, f)
    ok75 &= [max(nu75(x, n), nu75(y, n)) for x, y in pairs] == [q + 1, q + 1, q + 1, 2 * q]
    ok75 &= all(_rq3.pair_lp(x, y, n) == n for x, y in pairs[1:]) and all(y for x, y in pairs[:3])
    # G160's gate along the prefix from arrival phase r = q - 2 at (a, 0), with the reset-clock updates
    r = q - 2
    gates = []
    for i in range(5):
        x, y = seq[i], seq[i + 1]
        gates.append(_rq3.gated(_rq3.rot(x, r, n), _rq3.rot(y, r, n), n))
        if y:
            while not (y >> (r % n)) & 1:
                r += 1
            r += 1
    ok75 &= all(gates)
    if q == 4:
        ok75 &= seq[:1] + seq[2:] == [238, 180, 255, 150, 82] and f in _rq3.children_brute(one, e, n)
# the excluded q = 2: the run count fails (f has weight 1, not q/2 + 1 = 2) and the gate fails at (a, 0) from phase 0,
# although f still reaches order 2q = 4
n, a, c, one, e, kids = g185(2)
ok75 &= len(kids) == 1 and bin(kids[0]).count('1') == 1 and nu75(kids[0], n) == 4
ok75 &= not _rq3.gated(a, 0, n) and not _rq3.gated(0, c, n)
# rooted at q = 4: RQ3's reached q = 8 graph runs through G185's prefix at depths 28 -> 32 by consecutive edges, each
# aligned state being G185's pair at its own arrival phase (2, 2, 3, 4, 5) plus one offset, 5; the rooted q = 8 cap
# exit at depth 399 is not G185's q = 8 entry
_n4, _a4, _c4, _o4, _e4, _k4 = g185(4)
_s4 = [_a4, 0, _c4, _o4, _e4, _k4[0]]
_rt, _dp8, _pa, _ed8, _ex = _rq3.reached(8)
_E8 = {(s_, t_) for s_, t_, _ in _ed8}
_al4 = [(_rq3.rot(_s4[i], k, 8), _rq3.rot(_s4[i + 1], k, 8)) for i, k in zip(range(5), (7, 7, 0, 1, 2))]
ok75 &= [_dp8.get(s_) for s_ in _al4] == [28, 29, 30, 31, 32] and all((_al4[i], _al4[i + 1]) in _E8 for i in range(4))
_snk = [s_ for s_ in _dp8 if s_ not in {x for x, _, _ in _ed8}]
ok75 &= len(_snk) == 1 and _dp8[_snk[0]] == 399
ok75 &= [(_snk[0][0] >> t) & 1 for t in range(8)] == [1, 0, 0, 0, 0, 1, 0, 1]
_mx75 = {s_: max(_rqo.nu(s_[0], 8), _rqo.nu(s_[1], 8)) for s_ in _dp8}
_jp75 = [_mx75[t_] - _mx75[s_] for s_, t_, _ in _ed8]
ok75 &= max(_jp75) == 3 and _jp75.count(3) == 7      # the q = 4 jump is the largest on the rooted q = 8 graph
ok75 &= not any(_rq3.rot(_snk[0][0] | (_snk[0][0] << 8), k, 16) == g185(8)[1] for k in range(16))
check('S75 G185: at q = 4 .. 64 the prefix a, 0, c, 1, e, f is compatible and gated from phase q - 2, with orders '
      'q, 0, q + 1, 1, q + 1, 2q, the jump q - 1 on the last edge; rooted at q = 4 (depths 28-32); q = 2 fails the '
      'gate', ok75)
_rng76 = random.Random(186)


def g24_76(M, tau, P, L, k):
    """G2.4's three requirements, then its A'''' sandwich 2l <= L - 1 + 6 2^k - M + 2P <= 2l - 1 (l = 2^(k+1))."""
    req = M < 6 * 2 ** k and tau + P <= 6 * 2 ** k and M >= L + 2 ** (k + 1) + 2 * P
    upper = L - 1 + 6 * 2 ** k - M + 2 * P <= 2 * 2 ** (k + 1) - 1
    return req, upper


def endpoint76(n, theta):
    """The largest k >= 0 with M = ceil(theta 2^k) <= n, and that M (None if even k = 0 fails)."""
    k = None
    while math.ceil(theta * 2 ** (0 if k is None else k + 1)) <= n:
        k = 0 if k is None else k + 1
    return (k, math.ceil(theta * 2 ** k)) if k is not None else (None, None)


ok76, _hits76 = True, 0
gam, th = _Fr(5, 2), _Fr(11, 5)
ok76 &= 2 < th < 6 / gam and gam * th == _Fr(11, 2) and th - 2 == _Fr(1, 5)
# endpoint selection on random good depths: maximality, the factor-two window, and G2.4 once P / 2^k is small enough
for trial in range(300):
    n = _rng76.randint(3, 10 ** 7)
    k, M = endpoint76(n, th)
    ok76 &= k is not None and M <= n < math.ceil(2 * th * 2 ** k) <= 2 * th * 2 ** k + 1
    A, B, L = _rng76.randint(0, 40), _rng76.randint(0, 500), _rng76.randint(1, 300)
    P = _rng76.randint(0, max(0, (2 ** k - 10 * (B + L + 4)) // (10 * (A + 3))))   # small relative period
    tau = gam * M + A * P + B                             # the assumed settling bound, at its worst
    req, upper = g24_76(M, tau, P, L, k)
    if 2 ** k >= 20 * (A + 3) * max(P, 1) + 40 * (B + L + 4):
        ok76 &= req and upper                             # the one-cell contradiction is reached
        _hits76 += 1
ok76 &= _hits76 >= 100
_tr76 = [g24_76(*args) for args in [(math.ceil(th * 2 ** 20), gam * math.ceil(th * 2 ** 20), 0, 1, 20)]]
ok76 &= _tr76[0] == (True, True)
# a slope at the limit fails: gamma theta = 6 leaves no time margin
ok76 &= not g24_76(math.ceil(th * 2 ** 20), _Fr(6) / th * math.ceil(th * 2 ** 20) + 1, 0, 1, 20)[0]


def sched76(lam, J):
    N = {1: 2}
    for j in range(1, J):
        N[j + 1] = N[j] + lam(j) * 2 ** j
    return N


# the equivalence on a schedule: at entries p/M = 1/R_j; inside stage j every depth n has R_(j+1) > n / (2 p(n))
_lam76 = (lambda j: 2 ** (2 ** (j.bit_length() - 2)) if j >= 2 and j & (j - 1) == 0 else 1)
_N76 = sched76(_lam76, 33)
_R76 = {j: _Fr(_N76[j], 2 ** j) for j in _N76}
ok76 &= all(_lam76(2 ** k) == 2 ** (2 ** (k - 1)) for k in range(1, 6)) and _lam76(3) == 1 and _lam76(1) == 1
ok76 &= all(_R76[j + 1] == (_R76[j] + _lam76(j)) / 2 for j in range(1, 32))
ok76 &= all(_Fr(2 ** j, _N76[j]) == 1 / _R76[j] for j in _N76)
for j in range(1, 20):
    for n in (_N76[j], (_N76[j] + _N76[j + 1]) // 2, _N76[j + 1] - 1):
        ok76 &= _R76[j + 1] > _Fr(n, 2 * 2 ** j)
# the strictness control: R spikes after each spike, falls back to 1 + (at most k 2^-(2^(k-1))) before the next
for k in range(1, 5):
    jk, jk1 = 2 ** k, 2 ** (k + 1)
    ok76 &= _R76[jk + 1] >= _Fr(2 ** (2 ** (k - 1)), 2)
    ok76 &= 1 <= _R76[jk1] <= 1 + k * _Fr(1, 2 ** (2 ** (k - 1)))
    ok76 &= all(_Fr(2 ** (3 * 2 ** h // 2), 2 ** jk1) <= _Fr(1, 2 ** (jk // 2)) for h in range(1, k + 1))
ok76 &= _R76[17] >= 128 and _R76[32] - 1 < _Fr(1, 10 ** 2)   # limsup infinite; p/M at entries near 1
# limsup R = infinity exactly when lambda is unbounded: R_(j+1) >= lambda_j / 2 and R_(j+1) <= max(R_j, lambda_j)
for trial in range(200):
    lam = [_Fr(_rng76.randint(0, 60), 2 ** _rng76.randint(0, 4)) for _ in range(40)]
    R = [_Fr(_rng76.randint(1, 30), 2)]
    for j in range(40):
        R.append((R[-1] + lam[j]) / 2)
    ok76 &= all(lam[j] / 2 <= R[j + 1] <= max(R[j], lam[j]) for j in range(40))
    ok76 &= max(R) <= max(R[0], max(lam))
check('S76 G186: endpoint selection and both G2.4 margins at gamma 5/2, theta 11/5 (300 random depths); the '
      'entry equivalence; limsup R infinite iff lambda unbounded; the spike schedule returns near 1', ok76)
def a4_77(L, i, ip, ell, M, tau, P):
    """A'''' at the pair (-1, 0), distance L - 1, a = 2i, a' = 2i', n = 2 ell: (requirements met, contradiction)."""
    a, ap, n = 2 * i, 2 * ip, 2 * ell
    req = M < ap - a and tau + P <= ap
    return req, req and not (n <= L - 1 + ap - M + 2 * P)


ok77 = True
# the recorded repeats (RULE30-PRIZE 8.59, BF4): Thue-Morse i = 0, i' = 3 2^k, l = 2^(k+1); paperfolding i = s,
# i' = 3s, l = 2s - 1; at k = 14 they are the recorded pairs (0, 49152, 32768) and (16384, 49152, 32767)
ok77 &= (0, 3 * 2 ** 14, 2 ** 15) == (0, 49152, 32768) and (2 ** 14, 3 * 2 ** 14, 2 ** 15 - 1) == (16384, 49152, 32767)
for s in (2 ** e for e in range(3, 21)):
    for L in (1, 7, 100):
        for P in (0, 1, 3):
            # paperfolding: the contradiction holds exactly from M = L + 2s + 2P + 2 up to M < 4s (with tau slack)
            lo = L + 2 * s + 2 * P + 2
            if lo + 1 < 4 * s:
                ok77 &= a4_77(L, s, 3 * s, 2 * s - 1, lo, 6 * s - P, P) == (True, True)
                ok77 &= a4_77(L, s, 3 * s, 2 * s - 1, lo - 1, 6 * s - P, P)[1] is False
                ok77 &= a4_77(L, s, 3 * s, 2 * s - 1, 4 * s, 6 * s - P, P)[0] is False
            # Thue-Morse with 2^k = s: threshold L + 2s + 2P, upper 6s
            lo_t = L + 2 * s + 2 * P
            if lo_t < 6 * s:
                ok77 &= a4_77(L, 0, 3 * s, 2 * s, lo_t, 6 * s - P, P) == (True, True)
                ok77 &= a4_77(L, 0, 3 * s, 2 * s, lo_t - 1, 6 * s - P, P)[1] is False
# GPT's offset control: L = 1, s = 8, P = 1, M = 21, tau = 47; right side 29 < n = 30; at the TM threshold M = 19, 31
ok77 &= a4_77(1, 8, 24, 15, 21, 47, 1) == (True, True) and 1 - 1 + 48 - 21 + 2 == 29
ok77 &= a4_77(1, 8, 24, 15, 19, 47, 1) == (True, False) and 1 - 1 + 48 - 19 + 2 == 31
# the asymptotic choice: theta in (2, min(4, 6/gamma)) is nonempty below slope 3; at gamma 5/2, theta 11/5 serves both
ok77 &= all(2 < min(4, _Fr(6) / g) for g in (_Fr(1), _Fr(2), _Fr(5, 2), _Fr(299, 100)))
_g77, _t77 = _Fr(5, 2), _Fr(11, 5)
for e in range(20, 40):
    s = 2 ** e
    for L, A, B, P in ((1, 2, 0, 0), (300, 22, 500, 2 ** (e // 3)), (50, 40, 50, 2 ** (e // 2 - 4))):
        M = math.ceil(_t77 * s)
        if 40 * (A + 3) * max(P, 1) + 80 * (B + L + 4) <= s:
            ok77 &= a4_77(L, s, 3 * s, 2 * s - 1, M, _g77 * M + A * P + B, P) == (True, True)
check('S77 G186 continuation: paperfolding (i = s, i\' = 3s, l = 2s - 1) needs M < 4s and M >= L + 2s + 2P + 2, '
      'exact at the thresholds for s = 2^3 .. 2^20; the offset control; theta 11/5 serves both families at slope 5/2',
      ok77)
_rng78 = random.Random(187)


def delta78(g, A):
    return (3 - g) / (2 * g + 2 * A + 8)


ok78 = True
# the threshold algebra: r < delta iff 4r/(1 - 2r) < (6 - 2 gamma)/(2 gamma + A + 1), on a rational grid
for g in (_Fr(1), _Fr(3, 2), _Fr(2), _Fr(5, 2), _Fr(29, 10)):
    for A in range(0, 11):
        d = delta78(g, A)
        ok78 &= d <= _Fr(1, 5) and (A < 2 or d <= _Fr(1, 7))
        for r in [_Fr(a, 997) for a in range(1, 498, 7)] + [d, d - _Fr(1, 10 ** 6), d + _Fr(1, 10 ** 6)]:
            if 0 < r < _Fr(1, 2):
                ok78 &= (r < d) == (4 * r / (1 - 2 * r) < (6 - 2 * g) / (2 * g + A + 1))
ok78 &= delta78(_Fr(5, 2), 4) == _Fr(1, 42)


def endpoint78(n, q, D):
    s = 1
    while 4 * s <= n - 2 * q - D:
        s *= 2
    return (s, 2 * s + 2 * q + D) if 2 * s <= n - 2 * q - D else (None, None)


# GPT's integer control: L = 1, B = 0, gamma 5/2, A = 4, n = 1000, q = 16
s, M = endpoint78(1000, 16, 3)
ok78 &= (s, M) == (256, 547) and _Fr(5, 2) * M + 4 * 16 + 0 + 16 == _Fr(2895, 2) < 6 * s and M < 4 * s
ok78 &= 1 - 1 + 6 * s - M + 2 * 16 == 1021 and 4 * s - 2 == 1022
ok78 &= a4_77(1, s, 3 * s, 2 * s - 1, M, _Fr(5, 2) * M + 4 * 16, 16) == (True, True)
ok78 &= a4_77(1, 0, 3 * s, 2 * s, M, _Fr(5, 2) * M + 4 * 16, 16) == (True, True)
# the construction on random good depths with q <= r n, r < delta: M <= n, s > (n - 2q - D)/4, and both contradictions
_hit78 = 0
for trial in range(400):
    g, A = _rng78.choice([_Fr(1), _Fr(2), _Fr(5, 2)]), _rng78.randint(2, 8)
    d = delta78(g, A)
    r = d * _Fr(_rng78.randint(1, 95), 100)
    L, B = _rng78.randint(1, 50), _rng78.randint(0, 200)
    n = _rng78.randint(10 ** 6, 10 ** 9)
    q = int(r * n)
    for code, D in (('TM', L), ('PF', L + 2)):
        s, M = endpoint78(n, q, D)
        ok78 &= s is not None and M <= n and 4 * s > n - 2 * q - D
        tau = g * M + A * q + B                          # P <= q by monotone periods, at its worst P = q
        margin = (6 - 2 * g) * s - (2 * g + A + 1) * q - g * D - B
        if margin > 0:
            _hit78 += 1
            want = (True, True)
            got = a4_77(L, 0, 3 * s, 2 * s, M, tau, q) if code == 'TM' else a4_77(L, s, 3 * s, 2 * s - 1, M, tau, q)
            ok78 &= got == want
ok78 &= _hit78 >= 600
# the threshold is not vacuous: at r = 3 delta the same construction's time margin goes negative
_neg78 = 0
for trial in range(200):
    g, A = _rng78.choice([_Fr(1), _Fr(2), _Fr(5, 2)]), _rng78.randint(2, 8)
    n = _rng78.randint(10 ** 6, 10 ** 9)
    q = int(3 * delta78(g, A) * n)
    s, M = endpoint78(n, q, 1)
    _neg78 += (6 - 2 * g) * s - (2 * g + A + 1) * q - g - 0 <= 0
ok78 &= _neg78 >= 100
# strictness: at q/s exactly (6 - 2 gamma)/(2 gamma + A + 1) the time requirement needs gamma D + B <= 0
g, A, s = _Fr(5, 2), 4, 2 ** 20
q = (6 - 2 * g) / (2 * g + A + 1) * s
ok78 &= 2 * g * s + (2 * g + A + 1) * q == 6 * s and 2 * g * s + (2 * g + A + 1) * q + g * 1 + 0 > 6 * s
# the stage identity: within stage j, p/M is least at m_j = N_(j+1) - 1, where it is 1/(2 R_(j+1) - 2^-j)
for trial in range(100):
    N = [None, _rng78.randint(2, 9)]
    for j in range(1, 25):
        N.append(N[j] + _rng78.randint(1, 3000) * 2 ** j // _rng78.randint(1, 8) + 1)
    for j in range(1, 24):
        ends = [N[j], (N[j] + N[j + 1]) // 2, N[j + 1] - 1]
        R1 = _Fr(N[j + 1], 2 ** (j + 1))
        ok78 &= min(_Fr(2 ** j, m) for m in ends) == _Fr(2 ** j, N[j + 1] - 1) == 1 / (2 * R1 - _Fr(1, 2 ** j))
# the synthetic schedule N_j = 25 2^j: R = 25 > 21 at every entry, stage ends fall to 1/50; at period 16, 400 and 799
ok78 &= all(_Fr(25 * 2 ** j, 2 ** j) == 25 for j in range(1, 30)) and 1 / (2 * _Fr(25) - _Fr(1, 2 ** 30)) < _Fr(1, 49)
ok78 &= _Fr(16, 400) > _Fr(1, 42) > _Fr(16, 799)
# the recorded Rule 30 stages against delta = 1/42: stage 3 ends at 399 (8/399), stage 4 at N_5 - 1 >= 53,207
ok78 &= _Fr(8, 399) < _Fr(1, 42) and _Fr(16, 53207) < _Fr(1, 42) and _R74[4] == 25 > 21
check('S78 G187: r < delta iff the q/s margin (rational grid); delta <= 1/7 for A >= 2; endpoint construction on 400 '
      'random depths, both codes; the integer control; strictness; the stage-end identity; the 25 2^j schedule', ok78)
def kdy79(g, A):
    """The smallest power of two K strictly above (2 gamma + A + 1)/(6 - 2 gamma)."""
    f, K = (2 * g + A + 1) / (6 - 2 * g), 1
    while K <= f:
        K *= 2
    return f, K


ok79 = True
# the coefficient fraction is at least 5/4 once A >= 2 and gamma >= 1, so K >= 2 > 1 (paperfolding's extra need)
for g in (_Fr(1), _Fr(3, 2), _Fr(2), _Fr(5, 2), _Fr(29, 10)):
    for A in range(2, 12):
        f, K = kdy79(g, A)
        ok79 &= f >= _Fr(5, 4) and K >= 2 and (6 - 2 * g) * K - (2 * g + A + 1) > 0
        ok79 &= (6 - 2 * g) * (K // 2) - (2 * g + A + 1) <= 0       # the next smaller power is not licensed
# GPT's coefficient control at gamma 5/2, C = 1 (A = 4): fraction 10, K = 16, threshold 17; q = 16, L = 1, B = 0
f, K = kdy79(_Fr(5, 2), 4)
ok79 &= (f, K) == (10, 16) and (6 - 5) * 8 - 10 == -2
q, D = 16, 3
s, M = K * q, 2 * (K + 1) * q + D
ok79 &= (s, M) == (256, 547) and 6 * s - ((2 * _Fr(5, 2) * (K + 1) + 4 + 1) * q + _Fr(5, 2) * D) == _Fr(177, 2)
# the construction: whenever N_(j+1) > 2(K + 1) q + D, s = K q and M = 2s + 2q + D reach both contradictions once q is
# large against D and B (P <= q because M < N_(j+1))
for g, A in ((_Fr(5, 2), 4), (_Fr(2), 6), (_Fr(1), 2)):
    f, K = kdy79(g, A)
    gap = (6 - 2 * g) * K - (2 * g + A + 1)
    for j in range(8, 41):
        q = 2 ** j
        for L, B in ((1, 0), (40, 300)):
            for code, D in (('TM', L), ('PF', L + 2)):
                s, M = K * q, 2 * (K + 1) * q + D
                if gap * q > g * D + B and (2 * K - 2) * q > D:
                    tau = g * M + A * q + B
                    got = a4_77(L, 0, 3 * s, 2 * s, M, tau, q) if code == 'TM' else \
                        a4_77(L, s, 3 * s, 2 * s - 1, M, tau, q)
                    ok79 &= got == (True, True)
# the schedule 18 2^j passes the dyadic threshold 17 but not G187's general 1/42 (its stage ends tend to 1/36)
ok79 &= 18 > 17 and 1 / (2 * _Fr(18)) == _Fr(1, 36) > _Fr(1, 42)
ok79 &= 1 / (2 * _Fr(18) - _Fr(1, 2 ** 30)) > _Fr(1, 42)
# the record against the dyadic threshold at C = 1: R_4 = 25 > 17, so N_4 = 400 > 2 (17)(8) + D for D < 128
ok79 &= _R74[4] > 17 and 400 > 2 * 17 * 8 + 127
check('S79 G187 dyadic refinement: K the least power of two above (2 gamma + A + 1)/(6 - 2 gamma), K >= 2, the next '
      'smaller not licensed; s = Kq reaches both contradictions; threshold 17 at C = 1; the 18 2^j schedule', ok79)
def walk80(q, a, cap):
    """After the zero driver (a, 0): positions 1, 2, ... starting at a child c; deterministic until a zero.
    Returns, per child c, the first zero position (None if none by cap) and the parity of the driver before it."""
    out = []
    for c in _rq3.children(a, 0, q):
        x, y, pos = 0, c, 1
        while y and pos < cap:
            ch = _rq3.children(x, y, q)
            x, y, pos = y, ch[0], pos + 1
        out.append((pos, bin(x).count('1') % 2) if y == 0 else (None, None))
    return out


def branches80(q, x, y, depth):
    """Every compatible continuation of the pair (x, y) for depth more profiles, as lists of profiles."""
    if depth == 0:
        return [[]]
    res = []
    for z in _rq3.children(x, y, q):
        for rest in branches80(q, y, z, depth - 1):
            res.append([z] + rest)
    return res


ok80 = True
# G188 and its continuation on every odd doubling entry: q = 4, 8, 16, every odd q/2-source, both children
_min80 = {}
for q in (4, 8, 16):
    h = q // 2
    for blk in range(1, 1 << h):
        if bin(blk).count('1') % 2 == 0:
            continue
        a = blk | (blk << h)
        kids = _rq3.children(a, 0, q)
        ok80 &= len(kids) == 2 and all(_rq3.rot(c, h, q) == c ^ ((1 << q) - 1) for c in kids)     # T c = 1 + c
        if q <= 8:
            for pos, par in walk80(q, a, 10 ** 4):
                _min80[q] = min(_min80.get(q, 10 ** 9), pos)
        else:
            ok80 &= all(pos is None for pos, par in walk80(q, a, 11))           # no zero at positions 1..10
ok80 &= _min80 == {4: 21, 8: 88}
# positions 9 and 10 need only a nonzero c: every nonzero c at caps 2 .. 12, every branch, no zero at 9 or 10
for q in range(2, 13):
    for c in range(1, 1 << q):
        for br in branches80(q, 0, c, 9):
            seq = [c] + br                                  # positions 1 .. 10
            ok80 &= seq[1] == (1 << q) - 1 and seq[8] != 0 and seq[9] != 0
# GPT's E table and the two return tables, by brute force over bits
E80 = lambda x, y, z: x ^ y ^ (z & (1 - x) & (1 - y))
ok80 &= [E80(*map(int, '{:03b}'.format(t))) for t in range(8)] == [0, 1, 1, 1, 1, 1, 0, 0]
t9 = {}
for x, y, z in product((0, 1), repeat=3):
    for v in (0, 1):
        d2 = x ^ z                                          # (Delta^2 w)(t) = w(t) + w(t + 2)
        if (y ^ v) == 1 ^ (E80(x, y, z) | d2):              # S(Delta^2 w)(t) = 1 + (E(w) OR Delta^2 w)(t)
            t9.setdefault((x, y, z), []).append(v)
ok80 &= all(len(v) == 1 for v in t9.values()) and len(t9) == 8
_nx9 = {k: (k[1], k[2], v[0]) for k, v in t9.items()}
ok80 &= _nx9[(0, 1, 0)] == (1, 0, 1) and _nx9[(1, 0, 1)] == (0, 1, 0) and _nx9[(1, 0, 0)] == (0, 0, 0)
ok80 &= _nx9[(0, 0, 0)] == (0, 0, 1) and _nx9[(1, 1, 1)] == (1, 1, 0)
_cyc9 = set()
for k in _nx9:
    s_ = _nx9[k]
    for _ in range(8):
        if s_ == k:
            _cyc9.add(k)
            break
        s_ = _nx9[s_]
ok80 &= _cyc9 == {(0, 1, 0), (1, 0, 1)}
e10 = set()
for x, y, z, v in product((0, 1), repeat=4):
    Ea, Eb = E80(x, y, z), E80(y, z, v)
    if (Ea == 1 and Eb == 0) or (Ea == 0 and Eb == 1 ^ x ^ y ^ z ^ v):
        e10.add(((x, y, z), (y, z, v)))
ok80 &= e10 == {((0, 1, 1), (1, 1, 0)), ((0, 1, 1), (1, 1, 1)), ((1, 1, 1), (1, 1, 0)), ((1, 1, 0), (1, 0, 0)),
                ((1, 0, 0), (0, 0, 0))}
# position 8's f-equation: y(1 + z) = 1 + [(x + z) OR x(1 + y)] allows exactly 001, 010, 011, 100, 101
_al8 = {(x, y, z) for x, y, z in product((0, 1), repeat=3) if (y & (1 - z)) == 1 ^ ((x ^ z) | (x & (1 - y)))}
ok80 &= _al8 == {(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}
# the literal controls: the even-source seven-step return at cap 4, and the q = 2 five-step return
w4 = lambda s: sum(int(b) << t for t, b in enumerate(s))
_ctl = [w4(s) for s in ('0110', '0000', '1101', '1111', '0001', '0101', '0011', '0011', '0000')]
ok80 &= all(_rq3.rot(_ctl[i + 2], 1, 4) == _ctl[i] ^ (_ctl[i + 1] | _ctl[i + 2]) for i in range(7))
ok80 &= _ctl[0] == _ctl[2] ^ _rq3.rot(_ctl[2], 1, 4) and _rq3.rot(_ctl[2], 2, 4) != _ctl[2] ^ 15
_q2 = [w4(s) for s in ('00', '01', '11', '01', '01', '00')]
ok80 &= all(_rq3.rot(_q2[i + 2], 1, 2) == _q2[i] ^ (_q2[i + 1] | _q2[i + 2]) for i in range(4))
# the rooted q = 16 stage: from the q = 8 cap exit (161, 0), doubled, the first zero is 52,808 steps later
# (depth 399 + 52,808 = 53,207, G2.3's white driver), with an even-parity driver (a genuine split, not a doubling)
_rt16 = walk80(16, 161 | (161 << 8), 60000)
ok80 &= _rt16 == [(52808, 0), (52808, 0)]
check('S80 G188 with its continuation: no zero at positions 1 to 10 after any odd doubling at q = 4, 8, 16 (first '
      'returns 21 and 88 at q = 4, 8); 9 and 10 for every nonzero c at caps 2-12; E and the return tables; the '
      'controls; the rooted q = 16 return at 53,207', ok80)
ok81 = True
H81 = lambda x, y, z: (x ^ y) | (y ^ z)
F81 = lambda x, y, z, v: y ^ v ^ H81(x, y, z)
ok81 &= [H81(*map(int, '{:03b}'.format(t))) for t in range(8)] == [0, 1, 1, 1, 1, 1, 1, 0]
# the return-11 successor rule u = z + H(y, z, v) + 1 + [F(x, y, z, v) OR (E(x, y, z) + E(y, z, v))]
_succ81 = []
for t in range(16):
    x, y, z, v = map(int, '{:04b}'.format(t))
    u = z ^ H81(y, z, v) ^ 1 ^ (F81(x, y, z, v) | (E80(x, y, z) ^ E80(y, z, v)))
    _succ81.append('{}{}{}{}'.format(y, z, v, u))
ok81 &= _succ81 == ['0001', '0011', '0100', '0111', '1000', '1011', '1100', '1111',
                    '0000', '0010', '0100', '0111', '1001', '1011', '1100', '1110']
_nx81 = {'{:04b}'.format(t): _succ81[t] for t in range(16)}
_cy81, s_ = ['0000'], _nx81['0000']
while s_ != '0000':
    _cy81.append(s_)
    s_ = _nx81[s_]
ok81 &= _cy81 == ['0000', '0001', '0011', '0111', '1111', '1110', '1100', '1001', '0010', '0100', '1000']
for t in _nx81:                                           # every state feeds that one cycle
    s_ = t
    for _ in range(16):
        s_ = _nx81[s_]
    ok81 &= s_ in _cy81
# the cycle word w = 00001111001 and the ambient return at position 11 it reconstructs, at cap 11
_w81 = [int(b) for b in '00001111001']
ok81 &= ['{}{}{}{}'.format(*[_w81[(i + k) % 11] for k in range(4)]) for i in range(11)] == _cy81
W = lambda bits: sum(b << t for t, b in enumerate(bits))
w = W(_w81)
S = lambda u: _rq3.rot(u, 1, 11)
dw = w ^ S(w)
Ew = W([E80(_w81[t], _w81[(t + 1) % 11], _w81[(t + 2) % 11]) for t in range(11)])
Fw = W([F81(*[_w81[(t + k) % 11] for k in range(4)]) for t in range(11)])
e = S(Ew) ^ (Fw | Ew)
c = 2047 ^ S(e)
seq = [0, c, 2047, e, Fw, Ew, dw ^ S(dw), w & dw, dw, w, w, 0]  # 0, c, 1, e, f, g, h, i, j, k, l, 0
ok81 &= all(S(seq[i + 2]) == seq[i] ^ (seq[i + 1] | seq[i + 2]) for i in range(10))
ok81 &= c not in (0, 2047) and bin(c ^ S(c)).count('1') % 2 == 0 and all(seq[k] for k in range(1, 11))
# forwards from (0, c) at cap 11 the walk is that sequence, returning to zero at position 11
x, y, path = 0, c, [c]
while y and len(path) < 12:
    x, y = y, _rq3.children(x, y, 11)[0]
    path.append(y)
ok81 &= path == seq[1:] and len(path) == 11
# without an earlier zero, a position-11 return occurs only at cap 11 among caps 2 to 13
_caps81 = set()
for q in range(2, 14):
    for c0 in range(1, 1 << q):
        x, y, pos = 0, c0, 1
        while y and pos < 11:
            x, y, pos = y, _rq3.children(x, y, q)[0], pos + 1
        if pos == 11 and y == 0:
            _caps81.add(q)
ok81 &= _caps81 == {11}
# and after an odd doubling at q = 4, 8, 16 no profile through position 11 is zero
for q in (4, 8, 16):
    h = q // 2
    for blk in range(1, 1 << h):
        if bin(blk).count('1') % 2:
            ok81 &= all(pos is None for pos, par in walk80(q, blk | (blk << h), 12))
check('S81 G188 return 11: the successor table, one 11-cycle fed by every state, the cycle word 00001111001 and its '
      'ambient return at cap 11 (even-parity source); returns at 11 only at cap 11 (caps 2-13); none after doubling',
      ok81)
def U82(n, w):
    """G189's backward functions on a finite word (list of bits), at t = 0: U_0 = U_1 = w,
    U_(n+2) = S U_n + (U_(n+1) OR U_n); U_n is defined on len(w) - n // 2 positions."""
    U = [w, w]
    for i in range(2, n + 1):
        a, b = U[i - 2], U[i - 1]
        U.append([a[t + 1] ^ (b[t] | a[t]) for t in range(min(len(a) - 1, len(b)))])
    return U[n][0]


ok82 = True
# support and affine structure, exhaustively on words of length 9: U_2j(0) depends only on w(0..j) with coefficient 1
# in w(j); U_(2j+1)(0) depends only on w(0..j)
for n in range(0, 13):
    j = n // 2
    table = {}
    for bits in range(1 << 9):
        w = [(bits >> i) & 1 for i in range(9)]
        key = tuple(w[:j + 1])
        val = U82(n, w)
        ok82 &= table.setdefault(key, val) == val
    if n % 2 == 0:
        ok82 &= all(table[k] ^ table[k[:j] + (1 - k[j],)] == 1 for k in table)
# the first functions: U_2 = Delta w, U_3 = w (Delta w), U_4 = Delta^2 w
for x, y, z in product((0, 1), repeat=3):
    w = [x, y, z] + [0] * 6
    ok82 &= U82(2, w) == x ^ y and U82(3, w) == x & (x ^ y) and U82(4, w) == x ^ z
# the even functions really can lose the newest bit at odd index: U_3 = x(1 + y) ignores y when x = 0
ok82 &= U82(3, [0, 0] + [0] * 7) == U82(3, [0, 1] + [0] * 7) == 0
# the r = 5 and r = 7 maps: U_2 = 1 alternates, U_4 = 1 gives the 0011 cycle
ok82 &= all(U82(2, [x, 1 - x] + [0] * 7) == 1 for x in (0, 1))
ok82 &= all(U82(4, [x, y, 1 - x] + [0] * 6) == 1 for x in (0, 1) for y in (0, 1))
# the bound on actual walks: at caps 2 to 11, every nonzero c whose first zero is at an odd position r = 2k + 3 has
# least period at most 2^k; exact at r = 5 (period 2) and r = 7 (period 4); the r = 11 return has period 11
_lp82 = lambda u, q: next(d for d in range(1, q + 1) if q % d == 0 and _rq3.rot(u, d, q) == u)
_odd82 = {}
for q in range(2, 12):
    for c0 in range(1, 1 << q):
        x, y, pos = 0, c0, 1
        while y and pos < 400:
            x, y, pos = y, _rq3.children(x, y, q)[0], pos + 1
        if y == 0 and pos % 2:
            L = _lp82(c0, q)
            ok82 &= L <= 2 ** ((pos - 3) // 2)
            _odd82[pos] = max(_odd82.get(pos, 0), L)
ok82 &= _odd82[5] == 2 and _odd82[7] == 4 and _odd82[11] == 11
# even returns have no such bound: at cap 12 a first zero at position 8 has an entry of least period 12
_ev82 = []
for c0 in range(1, 1 << 12):
    x, y, pos = 0, c0, 1
    while y and pos < 9:
        x, y, pos = y, _rq3.children(x, y, 12)[0], pos + 1
    if y == 0 and pos == 8:
        _ev82.append(_lp82(c0, 12))
ok82 &= 12 in _ev82
check('S82 G189: U_2j affine in its newest bit with support w(t..t+j), U_(2j+1) on the same support (n <= 12, '
      'exhaustive); U_2, U_3, U_4; odd first returns at caps 2-11 obey q <= 2^k, exact at r = 5, 7; even r = 8 reaches '
      'period 12', ok82)
def Ucyc83(n, w, q):
    """G189's backward functions on a cyclic q-bit word."""
    U = [w, w]
    for i in range(2, n + 1):
        U.append(_rq3.rot(U[i - 2], 1, q) ^ (U[i - 1] | U[i - 2]))
    return U[n]


ok83 = True
# GC244's literal control: w = 10100100 at cap 8 reconstructs a first return at position 8 from c = 10010011
_W83 = lambda s: sum(int(b) << t for t, b in enumerate(s))
q, full = 8, 255
w, c = _W83('10100100'), Ucyc83(6, _W83('10100100'), 8)
src = c ^ _rq3.rot(c, 1, q)
ok83 &= Ucyc83(5, w, q) == full and c == _W83('10010011') and bin(c).count('1') == 4 and _lp82(c, q) == 8
ok83 &= _rq3.rot(c, 4, q) != c ^ full and src == _W83('10110100') and _lp82(src, q) == 8
ok83 &= bin(src).count('1') % 2 == 0
seq = [src, 0, c] + [Ucyc83(n, w, q) for n in range(5, -1, -1)] + [0]
ok83 &= all(_rq3.rot(seq[i + 2], 1, q) == seq[i] ^ (seq[i + 1] | seq[i + 2]) for i in range(len(seq) - 2))
x, y, pos = 0, c, 1
while y and pos < 20:
    x, y, pos = y, _rq3.children(x, y, q)[0], pos + 1
ok83 &= pos == 8
# the gap count over every cyclic w at caps 4 to 16 with U_5 = 1 (a return at 8): gaps of one or two zeros only,
# length 2A + 3B and entry weight 2A + B; balance (weight q/2) then needs B = 2A, so q = 8A
_n83, _bal83 = 0, set()
for q in range(4, 17):
    full = (1 << q) - 1
    for w in range(1, full):
        if Ucyc83(5, w, q) != full:
            continue
        _n83 += 1
        ones = [t for t in range(q) if (w >> t) & 1]
        gaps = [(ones[(i + 1) % len(ones)] - ones[i] - 1) % q for i in range(len(ones))]
        A, B = gaps.count(1), gaps.count(2)
        cw = bin(Ucyc83(6, w, q)).count('1')
        ok83 &= set(gaps) <= {1, 2} and 2 * A + 3 * B == q and cw == 2 * A + B
        if 2 * cw == q:
            _bal83.add(q)
            ok83 &= B == 2 * A and q == 8 * A
ok83 &= _n83 == 357 and _bal83 == {8, 16}
check('S83 GC244: the cap-8 return from w = 10100100 (c = 10010011, weight 4, no complementary halves, even source); '
      'gap count length 2A + 3B and weight 2A + B over all 357 return-8 words at caps 4-16; balance only at q = 8A',
      ok83)
def graph84(m):
    """G190's paired-window graph for return r = 2m + 2: F = U_(2m-1), U_2m(t) = w(t + m) + A(w(t..t+m-1))."""
    F, A = {}, {}
    for X in product((0, 1), repeat=m):
        F[X] = U82(2 * m - 1, list(X) + [0])
        A[X] = U82(2 * m, list(X) + [0])                   # w(t + m) = 0 here, so U_2m(0) = A(X)
        ok = U82(2 * m, list(X) + [1]) == 1 ^ A[X]         # the newest bit enters with coefficient 1
        assert ok
    V = [(X, Y) for X in F for Y in F if F[X] == 1 and F[Y] == 1]
    Vs = set(V)
    E = {}
    for X, Y in V:
        for b, b2 in product((0, 1), repeat=2):
            if b ^ b2 == 1 ^ A[X] ^ A[Y]:
                n = (X[1:] + (b,), Y[1:] + (b2,))
                if n in Vs:
                    E.setdefault((X, Y), []).append(n)
    return V, E


def rhs84(m, h):
    V, E = graph84(m)
    for v in V:
        layer = {v}
        for _ in range(h):
            layer = {n for u in layer for n in E.get(u, [])}
        if (v[1], v[0]) in layer:
            return True
    return False


def lhs84(m, q):
    """Some q-periodic w with U_(2m-1)(w) = 1 and c = U_2m(w) of complementary halves (odd doubling from q/2)."""
    full, h = (1 << q) - 1, q // 2
    for w in range(1 << q):
        if Ucyc83(2 * m - 1, w, q) == full:
            c = Ucyc83(2 * m, w, q)
            if _rq3.rot(c, h, q) == c ^ full:
                return True
    return False


ok84 = True
# both sides on small cases, the graph built from its definition: no path and no return for q = 2 to 16, m = 1 to 6
for q in (2, 4, 8, 16):
    for m in range(1, 7):
        ok84 &= lhs84(m, q) == rhs84(m, q // 2) == False
_V1, _E1 = graph84(1)
ok84 &= _V1 == [((1,), (1,))] and not _E1                    # the r = 4 boundary: one vertex, no edge


def walk84(q, a):
    c = _rq3.children(a, 0, q)[0]
    prof, x, y = [0, c], 0, c
    while y and len(prof) < 60000:
        x, y = y, _rq3.children(x, y, q)[0]
        prof.append(y)
    return prof


# the two actual even first returns after odd doublings: q = 8 at r = 88, and the rooted q = 16 at r = 52,808
_s8 = next(b | (b << 4) for b in range(16) if bin(b).count('1') % 2 and len(walk84(8, b | (b << 4))) - 1 == 88)
for q, a, rr in ((8, _s8, 88), (16, 161 | (161 << 8), 52808)):
    pr = walk84(q, a)
    r, full, h = len(pr) - 1, (1 << q) - 1, q // 2
    w, c = pr[r - 1], pr[1]
    U = [w, w]
    for n in range(2, r + 1):
        U.append(_rq3.rot(U[n - 2], 1, q) ^ (U[n - 1] | U[n - 2]))
    src = c ^ _rq3.rot(c, 1, q)
    ok84 &= r == rr and pr[r - 2] == w and all(U[n] == pr[r - 1 - n] for n in range(r)) and U[r - 3] == full
    ok84 &= _rq3.rot(c, h, q) == c ^ full and _lp82(c, q) == q and _lp82(src, q) == h
    ok84 &= bin(src & ((1 << h) - 1)).count('1') % 2 == 1
    if q == 8:
        # its paired windows trace a length-4 path from v to its swap, with F and A taken from their definitions
        m = (r - 2) // 2
        bit = lambda t: (w >> (t % q)) & 1
        X = [tuple(bit(t + k) for k in range(m)) for t in range(q + 1)]
        Fv = lambda Z: U82(2 * m - 1, list(Z) + [0])
        Av = lambda Z: U82(2 * m, list(Z) + [0])
        ok84 &= all(Fv(X[t]) == 1 for t in range(q))
        ok84 &= all(bit(t + m) ^ bit(t + h + m) == 1 ^ Av(X[t]) ^ Av(X[t + h]) for t in range(h))
        ok84 &= (X[h], X[2 * h]) == (X[h], X[0])           # after h steps the pair (X(0), X(h)) is swapped
# GC244's balanced cap-8 return fails c(1) + c(5) = 1; the nondyadic guard c = 010101 on cap 6
_c244 = sum(int(b) << t for t, b in enumerate('10010011'))
ok84 &= ((_c244 >> 1) & 1) ^ ((_c244 >> 5) & 1) == 0
_c6 = sum(int(b) << t for t, b in enumerate('010101'))
ok84 &= _rq3.rot(_c6, 3, 6) == _c6 ^ 63 and _lp82(_c6, 6) == 2 and (_c6 ^ _rq3.rot(_c6, 1, 6)) == 63
check('S84 G190: no path and no return for q = 2-16, m = 1-6 (graph from its definition); the actual even returns at '
      'q = 8 (r = 88) and the rooted q = 16 (r = 52,808) reconstruct backwards with complementary halves and odd '
      'sources, the first tracing a length-4 swap path; r = 4; GC244; cap 6', ok84)
from math import gcd as _gcd85


def mul85(A, B, n):
    out = []
    for row in A:
        r, k = 0, 0
        while row:
            if row & 1:
                r |= B[k]
            row >>= 1
            k += 1
        out.append(r)
    return out


def admitted85(adj, sig, n, J):
    """Dyadic q = 2^j (j = 1..J) for which some v has a path of length q/2 to sig(v)."""
    P, res = adj[:], []                                    # P = M^(2^(j-1)), starting at j = 1 (h = 1)
    for j in range(1, J + 1):
        if any((P[v] >> sig[v]) & 1 for v in range(n)):
            res.append(j)
        P = mul85(P, P, n)
    return res


def criterion85(adj, sig, n):
    """G191's test: a sigma-invariant strongly connected component with a cycle, period g a power of two, shift 0."""
    reach = [adj[v] for v in range(n)]
    for _ in range(n):
        reach = [reach[v] | mul85([reach[v]], adj, n)[0] for v in range(n)]
    comps, seen = [], set()
    for v in range(n):
        if v in seen:
            continue
        C = {u for u in range(n) if ((reach[v] >> u) & 1 and (reach[u] >> v) & 1) or u == v}
        seen |= C
        comps.append(C)
    for C in comps:
        if not any((adj[u] >> w) & 1 for u in C for w in C):
            continue                                       # no positive cycle
        if {sig[u] for u in C} != C:
            continue
        root = min(C)
        lev, todo = {root: 0}, [root]
        while todo:
            u = todo.pop()
            for w in C:
                if (adj[u] >> w) & 1 and w not in lev:
                    lev[w] = lev[u] + 1
                    todo.append(w)
        g = 0
        for u in C:
            for w in C:
                if (adj[u] >> w) & 1:
                    g = _gcd85(g, abs(lev[u] + 1 - lev[w]))
        d = (lev[sig[root]] - lev[root]) % g
        if g & (g - 1) == 0 and d == 0:
            return True
    return False


_rng85 = random.Random(191)
ok85, _cnt85 = True, [0, 0]
for trial in range(400):
    n = _rng85.randint(1, 8)
    perm = list(range(n))
    _rng85.shuffle(perm)
    sig = list(range(n))
    for i in range(0, n - 1, 2):
        if _rng85.random() < 0.7:
            a, b = perm[i], perm[i + 1]
            sig[a], sig[b] = b, a
    adj = [0] * n
    for u in range(n):
        for w in range(n):
            if _rng85.random() < 0.25:
                adj[u] |= 1 << w
                adj[sig[u]] |= 1 << sig[w]                 # sigma is an automorphism
    adm = admitted85(adj, sig, n, 12)
    ev = criterion85(adj, sig, n)
    _cnt85[ev] += 1
    if ev:
        ok85 &= all(j in adm for j in range(8, 13))      # every large dyadic q (h >= 128 > n^2) is admitted
    else:
        ok85 &= all(2 ** j <= n for j in adm)            # every admitted q is at most n
ok85 &= min(_cnt85) >= 40
# GPT's controls: 4-cycle with a half-shift admits q = 4 only; K_{2,2} both ways with the in-part swap admits every
# q >= 4; the 6-cycle with a half-shift admits nothing dyadic; two exchanged self-loops admit nothing
cyc = lambda n: [1 << ((v + 1) % n) for v in range(n)]
ok85 &= admitted85(cyc(4), [2, 3, 0, 1], 4, 10) == [2] and not criterion85(cyc(4), [2, 3, 0, 1], 4)
_k22 = [0b1100, 0b1100, 0b0011, 0b0011]                    # a, a' -> b, b'; b, b' -> a, a'
ok85 &= admitted85(_k22, [1, 0, 3, 2], 4, 10) == list(range(2, 11)) and criterion85(_k22, [1, 0, 3, 2], 4)
ok85 &= admitted85(cyc(6), [3, 4, 5, 0, 1, 2], 6, 10) == [] and not criterion85(cyc(6), [3, 4, 5, 0, 1, 2], 6)
ok85 &= admitted85([0b01, 0b10], [1, 0], 2, 10) == [] and not criterion85([0b01, 0b10], [1, 0], 2)
check('S85 G191: on 400 random graphs with an involutive automorphism the component test predicts the dichotomy '
      '(all large dyadic q, or none above n); the four controls (C4, K22, C6, two loops)', ok85)
ok86, _cnt86 = True, [0, 0]
_rng86 = random.Random(1912)
for trial in range(300):
    n = _rng86.randint(1, 7)
    perm = list(range(n))
    _rng86.shuffle(perm)
    sig = list(range(n))
    for i in range(0, n - 1, 2):
        if _rng86.random() < 0.7:
            a, b = perm[i], perm[i + 1]
            sig[a], sig[b] = b, a
    adj = [0] * n
    for u in range(n):
        for w in range(n):
            if _rng86.random() < 0.22:
                adj[u] |= 1 << w
                adj[sig[u]] |= 1 << sig[w]
    J = (8 * n * n - 1).bit_length() + 1                  # 2^(J-1) >= 8 n^2: check that dyadic Q and the next one
    adm = admitted85(adj, sig, n, J)
    ev = criterion85(adj, sig, n)
    _cnt86[ev] += 1
    cut = [j for j in range(1, J + 1) if 2 ** j >= 8 * n * n]
    ok86 &= all((j in adm) == ev for j in cut)           # admission at any Q >= 8 n^2 is equivalent to persistence
# the arithmetic control: 3 and 5 represent every integer from 10 (residues 0, 2, 1 mod 3 by 0, 5, 10), but not 7
_rep86 = {a * 3 + b * 5 for a in range(10) for b in range(10)}
ok86 &= 7 not in _rep86 and all(N in _rep86 for N in range(10, 40)) and {0, 5, 10} <= _rep86
ok86 &= [min(x for x in _rep86 if x % 3 == res) for res in (0, 2, 1)] == [0, 5, 10]
# an isolated vertex fixed by sigma: an empty swap path, no positive cycle, no admitted q
ok86 &= admitted85([0], [0], 1, 8) == [] and not criterion85([0], [0], 1)
# the base controls at Q = 128 = 8 n^2 for n = 4: absent for the half-turn 4-cycle, present for K_{2,2}
ok86 &= 7 not in admitted85(cyc(4), [2, 3, 0, 1], 4, 8) and 7 in admitted85(_k22, [1, 0, 3, 2], 4, 8)
ok86 &= min(_cnt86) >= 40
check('S86 G191 cutoff: on 300 random graphs admission at every dyadic Q >= 8 n^2 (and the next) agrees with the '
      'persistent component; the 3-and-5 control; the isolated fixed vertex; C4 absent and K22 present at Q = 128',
      ok86)
ok87 = True
# in G190's actual graphs (m = 1 to 6) no edge joins two sigma-fixed vertices (X = Y on both ends)
for m in range(1, 7):
    V, E = graph84(m)
    ok87 &= all(not (u[0] == u[1] and w[0] == w[1]) for u in E for w in E[u])
# on random involutive graphs with that property, an invariant component in which every vertex has exactly one
# internal successor (a single cycle) is never persistent; with the property dropped, a fixed self-loop persists
_rng87, _single87 = random.Random(1913), 0
for trial in range(600):
    n = _rng87.randint(1, 8)
    perm = list(range(n))
    _rng87.shuffle(perm)
    sig = list(range(n))
    for i in range(0, n - 1, 2):
        if _rng87.random() < 0.8:
            a, b = perm[i], perm[i + 1]
            sig[a], sig[b] = b, a
    adj = [0] * n
    for u in range(n):
        for w in range(n):
            if _rng87.random() < 0.2 and not (sig[u] == u and sig[w] == w):
                adj[u] |= 1 << w
                adj[sig[u]] |= 1 << sig[w]
    # strongly connected components, as in S85
    reach = [adj[v] for v in range(n)]
    for _ in range(n):
        reach = [reach[v] | mul85([reach[v]], adj, n)[0] for v in range(n)]
    seen = set()
    for v in range(n):
        if v in seen:
            continue
        C = {u for u in range(n) if ((reach[v] >> u) & 1 and (reach[u] >> v) & 1) or u == v}
        seen |= C
        if {sig[u] for u in C} != C or not any((adj[u] >> w) & 1 for u in C for w in C):
            continue
        if all(sum((adj[u] >> w) & 1 for w in C) == 1 for u in C):
            _single87 += 1
            sub = [sum(((adj[u] >> w) & 1) << j for j, w in enumerate(sorted(C))) for u in sorted(C)]
            idx = {u: i for i, u in enumerate(sorted(C))}
            ok87 &= not criterion85(sub, [idx[sig[u]] for u in sorted(C)], len(C))
ok87 &= _single87 >= 30
ok87 &= admitted85([1], [0], 1, 8) == list(range(1, 9)) and criterion85([1], [0], 1)
check('S87 G191 Rule 30 continuation: no edge joins two sigma-fixed vertices in G190\'s graphs (m <= 6); invariant '
      'single-cycle components are never persistent when fixed vertices are not joined; a fixed self-loop is', ok87)
ok88 = True
# U5 = F3 on a triple (x, y, z) accepts exactly 001, 010, 011, 100, 101, and c = U6 = 1 + S Delta^2 w when U5 = 1
_acc88 = {(x, y, z) for x, y, z in product((0, 1), repeat=3) if U82(5, [x, y, z] + [0] * 6) == 1}
ok88 &= _acc88 == {(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)}
# G192 for arbitrary paired words: at caps 1 to 16 no two periodic words u, v (not only shifts of one another) have
# U5 = 1 on both and complementary reconstructed entries; single words with U5 = 1 do exist (10100100 among them)
_single88 = 0
for q in range(1, 17):
    full = (1 << q) - 1
    S5 = [w for w in range(1 << q) if Ucyc83(5, w, q) == full]
    _single88 += len(S5)
    c6 = {w: Ucyc83(6, w, q) for w in S5}
    for w in S5:
        ok88 &= c6[w] == full ^ _rq3.rot(w ^ _rq3.rot(w, 2, q), 1, q)      # c = 1 + S Delta^2 w
        bits = [(w >> t) & 1 for t in range(q)]
        ok88 &= all((bits[t], bits[(t + 1) % q], bits[(t + 2) % q]) in _acc88 for t in range(q))
    cset = set(c6.values())
    ok88 &= not any((c ^ full) in cset for c in cset)                     # no pair with c_u + c_v = 1
ok88 &= _single88 > 0 and Ucyc83(5, sum(int(b) << t for t, b in enumerate('10100100')), 8) == 255
# Delta^2 beta = 1 forces beta(t + 2) = 1 + beta(t): a rotation of 0011, which contains 11001
for q in (4, 8, 12, 16):
    sols = [b for b in range(1 << q) if (b ^ _rq3.rot(b, 2, q)) == (1 << q) - 1]
    ok88 &= len(sols) == 4 and all(any(all(((b >> ((s + k) % q)) & 1) == int('11001'[k]) for k in range(5))
                                       for s in range(q)) for b in sols)
check('S88 G192: F3 accepts 001, 010, 011, 100, 101; at caps 1-16 no two words with U5 = 1 have complementary entries '
      '(single words exist); Delta^2 beta = 1 forces 0011 and the block 11001', ok88)
ok89 = True
_long89 = {}
for m in range(1, 7):
    V, E = graph84(m)
    Vf = lambda X: U82(2 * m - 2, list(X) + [0])          # V_m = U_(2m-2) on the m-bit window
    Ff = lambda X: U82(2 * m - 1, list(X) + [0])
    Af = lambda X: U82(2 * m, list(X) + [0])
    Vs = set(V)
    H = {(X, Y) for X, Y in V if Vf(X) ^ Vf(Y) == 1}
    wins = {X for X, Y in V}
    N0, N1 = sum(1 for X in wins if Vf(X) == 0), sum(1 for X in wins if Vf(X) == 1)
    ok89 &= len(H) == 2 * N0 * N1 and all((Y, X) in H for X, Y in H) and all(X != Y for X, Y in H)
    indeg = {v: 0 for v in V}
    for u in E:
        for w in E[u]:
            indeg[w] += 1
            ok89 &= w in H                                   # every edge ends in H_m
    ok89 &= all(indeg[v] == 0 for v in V if v not in H)     # discarded vertices (diagonals too) have no in-edge
    # the target-only identity: for a source vertex and appended bits with the new pair a vertex, G190's edge equation
    # b + b' = 1 + A(X) + A(Y) holds exactly when V(X') + V(Y') = 1
    for X, Y in V:
        for b, b2 in product((0, 1), repeat=2):
            X2, Y2 = X[1:] + (b,), Y[1:] + (b2,)
            if (X2, Y2) in Vs:
                ok89 &= ((b ^ b2) == 1 ^ Af(X) ^ Af(Y)) == ((Vf(X2) ^ Vf(Y2)) == 1)
    # orientation labels on the quotient: canonical representative has V(X) = 0; every edge's label carries the
    # orientation exactly (orientation of source + label = orientation of target)
    orient = lambda v: 0 if Vf(v[0]) == 0 else 1
    for u in E:
        if u in H:
            for w in E[u]:
                canon_u = u if orient(u) == 0 else (u[1], u[0])
                w_from_canon = w if canon_u == u else (w[1], w[0])
                label = orient(w_from_canon)
                ok89 &= orient(u) ^ label == orient(w)
    # longest path in the (acyclic) original graph
    memo = {}

    def lp(v):
        if v not in memo:
            memo[v] = max([0] + [1 + lp(w) for w in E.get(v, [])])
        return memo[v]
    _long89[m] = (max(lp(v) for v in V), N0, N1)
ok89 &= _long89[1][1:] == (0, 1) and _long89[3][1:] == (2, 3) and _long89[3][0] <= 6
# V_3 = U_4 = x + z on G192's five triples: 010, 101 have 0; 001, 011, 100 have 1
ok89 &= {t: U82(4, list(t) + [0] * 6) for t in _acc88} == {(0, 1, 0): 0, (1, 0, 1): 0, (0, 0, 1): 1, (0, 1, 1): 1,
                                                            (1, 0, 0): 1}


def quotient_admits89(adj, sig, canon, h):
    """Labelled quotient: a closed walk of length h whose labels XOR to 1 exists."""
    n = len(adj)
    orient = [0 if v in canon else 1 for v in range(n)]
    rep = {v: (v if v in canon else sig[v]) for v in range(n)}
    Q = {}
    for c in canon:
        for w in adj[c]:
            Q.setdefault(c, []).append((rep[w], orient[w]))
    for c in canon:
        layer = {(c, 0)}
        for _ in range(h):
            layer = {(t, s ^ e) for (x, s) in layer for t, e in Q.get(x, [])}
        if (c, 1) in layer:
            return True
    return False


_c4adj, _c4sig = [[1], [2], [3], [0]], [2, 3, 0, 1]
ok89 &= quotient_admits89(_c4adj, _c4sig, {0, 1}, 2) and not quotient_admits89(_c4adj, _c4sig, {0, 1}, 4)
_k22adj, _k22sig = [[2, 3], [2, 3], [0, 1], [0, 1]], [1, 0, 3, 2]
ok89 &= all(quotient_admits89(_k22adj, _k22sig, {0, 2}, h) for h in (2, 4, 8, 16))
ok89 &= not quotient_admits89(_k22adj, _k22sig, {0, 2}, 1)
check('S89 G193: in G190\'s graphs (m = 1-6) every edge ends in H_m, discarded vertices have no in-edge, '
      '|H_m| = 2 N0 N1, the edge equation is target-only, labels carry orientation; r = 8 paths <= 6 edges; C4 and K22 '
      'quotients', ok89)
def potential90(k, edges, rhs):
    """Solve p(s) + p(t) = rhs(e) over GF(2) on a connected edge list; True if soluble."""
    adj = {}
    for idx, (s, t, _) in enumerate(edges):
        adj.setdefault(s, []).append((t, rhs[idx]))
        adj.setdefault(t, []).append((s, rhs[idx]))
    p = {0: 0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v, r in adj.get(u, []):
            if v not in p:
                p[v] = p[u] ^ r
                todo.append(v)
    return all(p[s] ^ p[t] == rhs[i] for i, (s, t, _) in enumerate(edges))


def classes90(k, edges):
    """Cycle gcd g of a strongly connected labelled graph and breadth-first classes mod g."""
    out = {}
    for s, t, _ in edges:
        out.setdefault(s, []).append(t)
    dist, fr = {0: 0}, [0]
    while fr:
        nx = []
        for u in fr:
            for v in out.get(u, []):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    nx.append(v)
        fr = nx
    g = 0
    for s, t, _ in edges:
        g = gcd(g, abs(dist[s] + 1 - dist[t]))
    return g, {v: dist[v] % g for v in range(k)}


def lift90(k, edges):
    """The two-sheet lift as an adjacency bitmask list over (v, s) -> 2v + s, with the sheet swap."""
    n = 2 * k
    adj = [0] * n
    for s, t, e in edges:
        for sh in (0, 1):
            adj[2 * s + sh] |= 1 << (2 * t + (sh ^ e))
    return adj, [x ^ 1 for x in range(n)]


ok90, _case90 = True, {'A': 0, 'B': 0, 'none': 0}
_rng90 = random.Random(194)
for trial in range(500):
    k = _rng90.randint(1, 6)
    # a random strongly connected labelled multigraph: a Hamiltonian cycle plus random extra edges (parallels allowed)
    perm = list(range(k))
    _rng90.shuffle(perm)
    edges = [(perm[i], perm[(i + 1) % k], _rng90.randint(0, 1)) for i in range(k)]
    edges += [(_rng90.randrange(k), _rng90.randrange(k), _rng90.randint(0, 1)) for _ in range(_rng90.randint(0, 4))]
    if k == 1 and _rng90.random() < 0.5:
        edges = [(0, 0, _rng90.randint(0, 1))]
    g, cls = classes90(k, edges)
    wrap = [1 if (g == 1 or (cls[s] == g - 1 and cls[t] == 0)) else 0 for s, t, _ in edges]
    A = potential90(k, edges, [e for _, _, e in edges])
    B = potential90(k, edges, [e ^ w for (_, _, e), w in zip(edges, wrap)])
    adj, sig = lift90(k, edges)
    adm = admitted85(adj, sig, 2 * k, 12)            # up to q = 4096 >= 8 (2k)^2, G191's cutoff
    pers = criterion85(adj, sig, 2 * k)
    pow2 = g & (g - 1) == 0
    if A:
        _case90['A'] += 1
        ok90 &= adm == [] and not pers
    elif B:
        _case90['B'] += 1
        ok90 &= not pers and all(2 ** j == 2 * g for j in adm) and (pow2 or adm == [])
    else:
        _case90['none'] += 1
        ok90 &= pers == pow2
        ok90 &= (all(j in adm for j in (11, 12)) if pow2 else adm == [])
ok90 &= min(_case90.values()) >= 50
# GPT's controls: the half-turn 4-cycle's quotient (two-cycle, labels 0, 1): A fails, B holds; K22's quotient (parallel
# labels 0 and 1 both ways): both fail; a two-cycle labelled 1, 1: A holds; the constant-1 test misses the locked case
_q4 = [(0, 1, 0), (1, 0, 1)]
g4, c4 = classes90(2, _q4)
w4 = [1 if (c4[s] == g4 - 1 and c4[t] == 0) else 0 for s, t, _ in _q4]
ok90 &= g4 == 2 and not potential90(2, _q4, [0, 1]) and potential90(2, _q4, [e ^ w for (_, _, e), w in zip(_q4, w4)])
ok90 &= not potential90(2, _q4, [e ^ 1 for _, _, e in _q4])          # adding 1 everywhere would wrongly reject B
_qk = [(0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)]
gk, ck = classes90(2, _qk)
wk = [1 if (ck[s] == gk - 1 and ck[t] == 0) else 0 for s, t, _ in _qk]
ok90 &= not potential90(2, _qk, [0, 1, 0, 1]) and not potential90(2, _qk, [e ^ w for (_, _, e), w in zip(_qk, wk)])
ok90 &= potential90(2, [(0, 1, 1), (1, 0, 1)], [1, 1])
check('S90 G194: on 500 random strongly connected labelled quotients the A/B potentials predict the explicit two-sheet '
      'lift (no swap path; only q = 2g; persistence exactly at power-of-two g); C4, K22, the 1-1 cycle, constant-1',
      ok90)
ok91, _par91 = True, {}
for m in range(1, 7):
    V, E = graph84(m)
    Vf = lambda X: U82(2 * m - 2, list(X) + [0])
    Ff = lambda X: U82(2 * m - 1, list(X) + [0])
    H = {(X, Y) for X, Y in V if Vf(X) ^ Vf(Y) == 1}
    canon = lambda v: v if Vf(v[0]) == 0 else (v[1], v[0])
    # quotient edges from canonical sources, with labels (target swapped from canonical = 1)
    par, outdeg = set(), {}
    for u in H:
        if canon(u) != u:
            continue
        tg = [(canon(w), 0 if canon(w) == w else 1) for w in E.get(u, [])]
        outdeg[u] = len(tg)
        for i in range(len(tg)):
            for j in range(i + 1, len(tg)):
                if tg[i][0] == tg[j][0]:
                    ok91 &= tg[i][1] != tg[j][1]                 # parallel orbits carry opposite labels
                    par.add((u, tg[i][0]))
    ok91 &= all(d <= 2 for d in outdeg.values())                 # at most one edge per label from each source
    # the four-window criterion over (m - 1)-bit words T
    four = set()
    for T in product((0, 1), repeat=m - 1):
        a, b, c, d = (0,) + T, (1,) + T, T + (0,), T + (1,)
        if Ff(a) == Ff(b) == Ff(c) == Ff(d) == 1 and Vf(a) ^ Vf(b) == 1:
            four.add((canon((a, b)), canon((c, d))))
    ok91 &= par == four
    _par91[m] = len(par)
ok91 &= _par91[1] == 0
# the m = 3 instance with T = 01: canonical source (101, 001), targets (010, 011) labelled 0 and (011, 010) labelled 1
_s91, _t91 = ((1, 0, 1), (0, 0, 1)), ((0, 1, 0), (0, 1, 1))
_V3, _E3 = graph84(3)
ok91 &= set(_E3.get(_s91, [])) == {_t91, (_t91[1], _t91[0])}
# opposite parallel edges inside a strongly connected labelled graph make both of G194's potentials insoluble
_rng91 = random.Random(195)
for trial in range(300):
    k = _rng91.randint(1, 6)
    perm = list(range(k))
    _rng91.shuffle(perm)
    edges = [(perm[i], perm[(i + 1) % k], _rng91.randint(0, 1)) for i in range(k)]
    edges += [(_rng91.randrange(k), _rng91.randrange(k), _rng91.randint(0, 1)) for _ in range(_rng91.randint(0, 3))]
    s, t, e = edges[_rng91.randrange(len(edges))]
    edges.append((s, t, 1 - e))
    g, cls = classes90(k, edges)
    wrap = [1 if (g == 1 or (cls[a] == g - 1 and cls[b] == 0)) else 0 for a, b, _ in edges]
    ok91 &= not potential90(k, edges, [x for _, _, x in edges])
    ok91 &= not potential90(k, edges, [x ^ w for (_, _, x), w in zip(edges, wrap)])
check('S91 G195: in G190\'s graphs (m = 1-6) parallel quotient edges are exactly the four-window pairs, with opposite '
      'labels; T = 01 at m = 3; an opposite parallel pair in a strongly connected graph defeats both potentials', ok91)
ok92 = True
# G195's overlap continuation on the two actual even returns: beta = w + S^h w is h-periodic and nonzero, so no window
# pair on the walk has equal tails (m - 1 >= h), and with m >= q the h quotient vertices of the walk are distinct
for q, a in ((8, _s8), (16, 161 | (161 << 8))):
    pr = walk84(q, a)
    r, h = len(pr) - 1, q // 2
    m = (r - 2) // 2
    w = pr[r - 1]
    beta = w ^ _rq3.rot(w, h, q)
    ok92 &= m - 1 >= h and m >= q and beta != 0 and _rq3.rot(beta, h, q) == beta and _lp82(w, q) == q
    bit = lambda t: (w >> (t % q)) & 1
    win = lambda t: tuple(bit(t + i) for i in range(min(m, 3 * q)))   # windows longer than 2q repeat; 3q bits decide
    for t in range(h):
        X, Y = win(t), win(t + h)
        ok92 &= X[1:] != Y[1:]                               # tails differ at every source on the walk
    verts = [frozenset((win(t), win(t + h))) for t in range(h)]
    ok92 &= len(set(verts)) == h                             # the walk's quotient vertices are distinct
# the sharp-length guard: an h-periodic nonzero difference can hold h - 1 zeros in a row (w = 00001000, h = 4)
_w92 = sum(int(b) << t for t, b in enumerate('00001000'))
_b92 = _w92 ^ _rq3.rot(_w92, 4, 8)
ok92 &= _b92 == sum(int(b) << t for t, b in enumerate('10001000'))
ok92 &= any(all(not (_b92 >> ((s + k) % 8)) & 1 for k in range(3)) for s in range(8))
ok92 &= not any(all(not (_b92 >> ((s + k) % 8)) & 1 for k in range(4)) for s in range(8))
check('S92 G195 overlap continuation: on the actual q = 8 (r = 88) and rooted q = 16 (r = 52,808) returns no source '
      'has equal tails and the walk\'s quotient vertices are distinct; the h - 1 zero guard (00001000)', ok92)
ok93 = True
Fm93 = lambda m, Z: U82(2 * m - 1, list(Z) + [0])          # F_m on an m-bit window
# the suffix formula D_m(T) = (m mod 2) + sum_k F_k(suffix_k(T)), and the one-step recurrence, for m = 1 to 10
for m in range(1, 11):
    for T in product((0, 1), repeat=m - 1):
        D = Fm93(m, T + (0,)) ^ Fm93(m, T + (1,))
        S = m % 2
        for k in range(1, m):
            S ^= Fm93(k, T[len(T) - k:])
        ok93 &= D == S
        if m >= 2:
            Tp = T[1:]                                       # suffix_(m-2)(T)
            Dp = Fm93(m - 1, Tp + (0,)) ^ Fm93(m - 1, Tp + (1,))
            ok93 &= D == Dp ^ 1 ^ Fm93(m - 1, T)
# the controls: D_1 = 1, B_1 = 0; D_2(x) = x, B_2 = 0; at m = 3 only tails 01 and 10 have B_3 = 1 (11 has D = 0, B = 0)
B93 = lambda m, T: Fm93(m, T + (0,)) & Fm93(m, T + (1,))
ok93 &= Fm93(1, (0,)) ^ Fm93(1, (1,)) == 1 and B93(1, ()) == 0
ok93 &= all((Fm93(2, (x, 0)) ^ Fm93(2, (x, 1))) == x and B93(2, (x,)) == 0 for x in (0, 1))
ok93 &= [T for T in product((0, 1), repeat=2) if B93(3, T)] == [(0, 1), (1, 0)]
ok93 &= (Fm93(3, (1, 1, 0)) ^ Fm93(3, (1, 1, 1))) == 0 and B93(3, (1, 1)) == 0
# branching in the actual graphs: a source of H_m has two out-edges exactly when B_m(tail X) = B_m(tail Y) = 1
_br93 = {}
for m in range(1, 7):
    V, E = graph84(m)
    Vf = lambda X: U82(2 * m - 2, list(X) + [0])
    H = [(X, Y) for X, Y in V if Vf(X) ^ Vf(Y) == 1]
    two, uneq = 0, 0
    for X, Y in H:
        pred = B93(m, X[1:]) == 1 and B93(m, Y[1:]) == 1
        ok93 &= (len(E.get((X, Y), [])) == 2) == pred
        if pred:
            two += 1
            uneq += X[1:] != Y[1:]
    _br93[m] = (two, uneq)
# the unexpected unequal-tail source (010, 001) at m = 3: targets (100, 010) and (101, 011)
_V93, _E93 = graph84(3)
ok93 &= set(_E93.get(((0, 1, 0), (0, 0, 1)), [])) == {((1, 0, 0), (0, 1, 0)), ((1, 0, 1), (0, 1, 1))}
ok93 &= _br93[1] == (0, 0) and _br93[2] == (0, 0) and _br93[3][1] > 0
check('S93 G196: D_m equals its suffix formula and recurrence for all tails, m = 1-10; B_m predicts two-successor '
      'sources exactly in G190\'s graphs (m = 1-6); the m = 1, 2, 3 controls; the unequal-tail source (010, 001)', ok93)
def phase_id94(bits):
    """The least L such that the q cyclic length-L blocks of the word are distinct."""
    q = len(bits)
    for L in range(1, q + 1):
        if len({tuple(bits[(t + i) % q] for i in range(L)) for t in range(q)}) == q:
            return L


def primitive94(bits):
    q = len(bits)
    return all(bits[d:] + bits[:d] != bits for d in range(1, q))


ok94 = True
# the q - 1 anchor: every primitive binary word of length q <= 12 is phase-identified by q - 1 bits; 0001 needs all 3
for q in range(2, 13):
    for v in range(1 << q):
        bits = [(v >> i) & 1 for i in range(q)]
        if primitive94(bits):
            ok94 &= phase_id94(bits) <= q - 1
ok94 &= phase_id94([0, 0, 0, 1]) == 3
# the return bound: after an exit that flips the first appended bit, no continuation's first window equals any original
# window before ell = m - L + 1 edges (brute force over every continuation, small primitive words, m >= q)
for bits in ([0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1]):
    q = len(bits)
    L = phase_id94(bits)
    for m in range(q, q + 4):
        orig = {tuple(bits[(t + i) % q] for i in range(m)) for t in range(q)}
        for t0 in range(q):
            prefix = [bits[(t0 + i) % q] for i in range(m)] + [1 - bits[(t0 + m) % q]]
            first = None
            for ell in range(1, m - L + 2):
                for tail in range(1 << max(0, ell - 1)):
                    extra = [(tail >> i) & 1 for i in range(ell - 1)]
                    win = tuple((prefix + extra)[ell:ell + m])
                    if win in orig:
                        first = ell if first is None else min(first, ell)
            ok94 &= first is None or first >= m - L + 1
# GPT's word-only controls: w = 01, m = 3: (010, 101) -> (100, 011) -> (001, 110) -> (010, 101), returning in 3 edges
_seq94 = [((0, 1, 0), (1, 0, 1)), ((1, 0, 0), (0, 1, 1)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1))]
ok94 &= all(_seq94[i + 1][0][:2] == _seq94[i][0][1:] and _seq94[i + 1][1][:2] == _seq94[i][1][1:] for i in range(3))
ok94 &= _seq94[1][0][2] == 1 - 1 and phase_id94([0, 1]) == 1 and 3 - 1 + 1 == 3       # flipped append, L = 1, bound 3
# the equal-tail bound: on a dyadic circuit, the paired tails cannot agree before ell = m - h (brute force, q = 4, 8)
for bits in ([0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]):
    q, h = len(bits), len(bits) // 2
    if all(bits[t] == bits[(t + h) % q] for t in range(q)):
        continue                                             # beta = 0: not a complementary circuit word
    for m in range(q, q + 3):
        for t0 in range(q):
            X = [bits[(t0 + i) % q] for i in range(m)]
            Y = [bits[(t0 + h + i) % q] for i in range(m)]
            for ell in range(0, m - h):
                for ext in range(1 << (2 * ell)):
                    ex = [(ext >> i) & 1 for i in range(ell)]
                    ey = [(ext >> (ell + i)) & 1 for i in range(ell)]
                    Xw, Yw = (X + ex)[ell:ell + m], (Y + ey)[ell:ell + m]
                    ok94 &= Xw[1:] != Yw[1:]
# the PR196-D1 rooted word: its sixteen 8-bit blocks are GPT's table, all distinct; L = 8 (phases 7, 13 share 0011000)
_w94 = [int(b) for b in '1000101001100001']
_blk94 = [''.join(str(_w94[(t + i) % 16]) for i in range(8)) for t in range(16)]
ok94 &= _blk94 == ['10001010', '00010100', '00101001', '01010011', '10100110', '01001100', '10011000', '00110000',
                   '01100001', '11000011', '10000110', '00001100', '00011000', '00110001', '01100010', '11000101']
ok94 &= len(set(_blk94)) == 16 and phase_id94(_w94) == 8 and _blk94[7][:7] == _blk94[13][:7] == '0011000'
ok94 &= 26403 - 8 + 1 == 26396 and 26403 - 8 == 26395
check('S94 G197: q - 1 bits identify the phase of every primitive word (q <= 12; 0001 needs 3); no continuation '
      'returns before m - L + 1 edges or reaches equal tails before m - h (brute force); the D1 word\'s 8-block table, '
      'L = 8', ok94)
def comp95(n, adj, v):
    """Vertices mutually reachable with v (adjacency as lists)."""
    def reach(src, nbrs):
        seen, todo = {src}, [src]
        while todo:
            u = todo.pop()
            for w in nbrs[u]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        return seen
    radj = [[] for _ in range(n)]
    for u in range(n):
        for w in adj[u]:
            radj[w].append(u)
    return reach(v, adj) & reach(v, radj)


def gcd95(adj, C):
    root = min(C)
    pot, todo = {root: 0}, [root]
    while todo:
        u = todo.pop()
        for w in adj[u]:
            if w in C and w not in pot:
                pot[w] = pot[u] + 1
                todo.append(w)
    g = 0
    for u in C:
        for w in adj[u]:
            if w in C:
                g = gcd(g, abs(pot[u] + 1 - pot[w]))
    return g


def mismatched95(n, adj, q):
    """Is there an excursion v_s -> v_u (interior off the cycle 0..q-1) of length l with l + s - u != 0 mod q?"""
    for s in range(q):
        # states (vertex, length mod q); interior vertices must be off the cycle
        start = [(w, 1 % q) for w in adj[s]]
        seen, todo = set(start), list(start)
        while todo:
            v, l = todo.pop()
            if v < q:
                if (l + s - v) % q:
                    return True
                continue                                     # an excursion ends at its first cycle vertex
            for w in adj[v]:
                st = (w, (l + 1) % q)
                if st not in seen:
                    seen.add(st)
                    todo.append(st)
    return False


ok95, _cnt95 = True, [0, 0]
_rng95 = random.Random(198)
for trial in range(600):
    q = _rng95.choice([2, 4, 8])
    h = q // 2
    extra = _rng95.randint(0, 3)                            # extra vertex pairs (x, x') exchanged by sigma
    n = q + 2 * extra
    sig = [(t + h) % q for t in range(q)] + [q + (i ^ 1) for i in range(2 * extra)]
    adj = [set() for _ in range(n)]
    for t in range(q):
        adj[t].add((t + 1) % q)
    for _ in range(_rng95.randint(0, 5)):
        u, w = _rng95.randrange(n), _rng95.randrange(n)
        if u < q and w < q and w == (u + 1) % q:
            continue
        adj[u].add(w)
        adj[sig[u]].add(sig[w])
    adj = [sorted(a) for a in adj]
    C = comp95(n, adj, 0)
    G = gcd95(adj, C)
    pers = G < q and q % G == 0
    mis = mismatched95(n, adj, q)
    _cnt95[pers] += 1
    ok95 &= q % G == 0 and pers == mis
    # and G191's criterion on the component itself agrees
    idx = {v: i for i, v in enumerate(sorted(C))}
    sub = [sum(1 << idx[w] for w in adj[v] if w in C) for v in sorted(C)]
    ok95 &= criterion85(sub, [idx[sig[v]] for v in sorted(C)], len(C)) == pers
ok95 &= min(_cnt95) >= 100
# GPT's controls: the locked detour (0 -> a -> 2, 2 -> a' -> 0 on the half-turn 4-cycle) has G = 4; the chords 0 -> 2,
# 2 -> 0 make G = 1; three cycle edges from 0 end at ordered phase 3, aligned, while phase 1 would read as residue 2
_lock = [[1, 4], [2], [3, 5], [0], [2], [0]]                # vertices 0..3, a = 4, a' = 5
ok95 &= gcd95(_lock, comp95(6, _lock, 0)) == 4 and not mismatched95(6, _lock, 4)
_chord = [[1, 2], [2], [3, 0], [0]]
ok95 &= gcd95(_chord, comp95(4, _chord, 0)) == 1 and mismatched95(4, _chord, 4)
ok95 &= (3 + 0 - 3) % 4 == 0 and (3 + 0 - 1) % 4 == 2
ok95 &= (26396 + 0 - 12) % 16 == 0                          # D1's hypothetical aligned rejoin from s = 0 at u = 12
check('S95 G198: on 600 random graphs around a dyadic cycle (q = 2, 4, 8) the component is persistent exactly when a '
      'mismatched excursion exists, and G191 agrees; the locked detour, the chords, the ordered-phase trap, D1', ok95)
def B96(pair, q):
    """The backward pair map B(a, b) = (S b XOR (a OR b), a) on q-bit cyclic words."""
    a, b = pair
    return (_rq3.rot(b, 1, q) ^ (a | b), a)


ok96 = True
_W96 = lambda s: sum(int(ch) << t for t, ch in enumerate(s))
w, c, a = _W96('10100100'), _W96('10010011'), _W96('10110100')
x = (w, w)
seq = [x]
for k in range(7):
    x = B96(x, 8)
    seq.append(x)
ok96 &= seq[6] == (0, c) and seq[7] == (a, 0)               # six and seven backward steps from (w, w)
ok96 &= (c ^ _rq3.rot(c, 1, 8)) == a and bin(a).count('1') == 4 and _lp82(a, 8) == 8
# the absorption identity: a nonzero pair maps to (0, 0) under B only from (0, all ones), at caps 1 to 8
for q in range(1, 9):
    full = (1 << q) - 1
    pre = [(u, v) for u in range(1 << q) for v in range(1 << q) if (u, v) != (0, 0) and B96((u, v), q) == (0, 0)]
    ok96 &= pre == [(0, full)]
# (a, 0) in any rotation is absent from the rooted cap-8 graph (RQ3's reached set holds no even-parity zero driver)
_rt96, _dp96, _pa96, _ed96, _ex96 = _rq3.reached(8)
ok96 &= all((_rq3.rot(a, k, 8), 0) not in _dp96 for k in range(8))
# parity is taken over the driver's own least-period block: the rooted zero drivers (255, 0), (170, 0), (221, 0) at
# depths 2, 7, 28 are the odd doublings from periods 1, 2, 4 (even weight over all 8 bits, odd over their period)
_zd96 = [s for s in _dp96 if s[1] == 0]
_blockpar96 = lambda u: bin(u & ((1 << _lp82(u, 8)) - 1)).count('1') % 2
ok96 &= all(_blockpar96(s[0]) == 1 for s in _zd96) and _blockpar96(a) == 0
ok96 &= sorted(_dp96[s] for s in _zd96) == [2, 7, 28, 399]
# and (w, w) never reaches zero: iterate B until the trajectory repeats
seen, x, steps = {}, (w, w), 0
while x not in seen:
    seen[x] = steps
    ok96 &= x != (0, 0)
    x = B96(x, 8)
    steps += 1
_cyc96 = steps - seen[x]
ok96 &= (0, 0) not in seen and (0, 255) not in seen
# the cap-2 example (01, 10) also never reaches zero
seen2, y = set(), (_W96('01'), _W96('10'))
while y not in seen2:
    seen2.add(y)
    y = B96(y, 2)
ok96 &= (0, 0) not in seen2 and (0, 3) not in seen2
check('S96 G199: B^6 (w, w) = (0, c), B^7 (w, w) = (a, 0) with a = Delta c of weight 4 and period 8; only (0, 1) maps '
      'to zero (caps 1-8); no rotation of (a, 0) is rooted at cap 8; (w, w) and (01, 10) never reach zero', ok96)
ok97 = True


def first_return97(q, a, child=0):
    c = _rq3.children(a, 0, q)[child]
    x, y, pos, prof = 0, c, 1, [0, c]
    while y and pos < 5000:
        x, y, pos = y, _rq3.children(x, y, q)[0], pos + 1
        prof.append(y)
    return pos if y == 0 else None, prof


# the D0 witness: source block 1000 (odd parity), first return 88; its repeated endpoint never reaches zero under B
_r97, _pr97 = first_return97(8, 17)
ok97 &= _r97 == 88 and bin(17 & 15).count('1') % 2 == 1
_ww97 = (_pr97[-2], _pr97[-2])
seen, x = set(), _ww97
while x not in seen:
    seen.add(x)
    x = B96(x, 8)
ok97 &= (0, 0) not in seen and (0, 255) not in seen
# the rooted period-8 entry: the q = 4 cap exit (block 1011) doubled; both children and every rotation first return
# at 371; in RQ3's rooted cap-8 graph the only states (0, c) with c of least period 8 sit at depth 29
_rt97, _dp97, _pa97, _ed97, _ex97 = _rq3.reached(4)
_sink97 = [s for s in _dp97 if s[1] == 0 and _dp97[s] == max(_dp97.values())][0]
_blk97 = _sink97[0]
ok97 &= [(_blk97 >> t) & 1 for t in range(4)] == [1, 0, 1, 1]
for k in range(4):
    b = _rq3.rot(_blk97, k, 4)
    a8 = b | (b << 4)
    ok97 &= all(first_return97(8, a8, ch)[0] == 371 for ch in (0, 1))
_r8, _d8, _p8, _e8, _x8 = _rq3.reached(8)
ok97 &= sorted({_d8[s] for s in _d8 if s[0] == 0 and s[1] and _lp82(s[1], 8) == 8}) == [29]
ok97 &= max(_d8.values()) - 28 == 371                        # zero at depth 28, next zero driver at 399
check('S97 G199 continuation: the D0 witness (block 1000, return 88) has a non-absorbing endpoint, while every rooted '
      'entry to period 8 (block 1011, both children, all rotations) first returns at 371, its only entry depth 29',
      ok97)
ok98 = True
# G200's event classification on the rooted history: the zero-driver sources sit at depths 2, 7, 28, 399 (cap 8), so
# the stages to periods 2, 4, 8 have one excursion each, of lengths 5, 21, 371 (entries 3, 8, 29, 400 = source + 1)
_r98, _d98, _p98, _e98, _x98 = _rq3.reached(8)
_z98 = sorted(_d98[s] for s in _d98 if s[1] == 0)
ok98 &= _z98 == [2, 7, 28, 399] and [b - a for a, b in zip(_z98, _z98[1:])] == [5, 21, 371]
ok98 &= [z + 1 for z in _z98] == [3, 8, 29, 400]                                      # N_1 .. N_4
# every one of those sources is an odd integration over its own least-period block (each ends a stage)
ok98 &= all(bin(s[0] & ((1 << _lp82(s[0], 8)) - 1)).count('1') % 2 == 1 for s in _d98 if s[1] == 0)
# the period-16 stage: from source 399 the first zero comes 52,808 later (depth 53,207), and that driver has even parity
# over its own least period, which is 16, so it is an internal genuine branch, not the exit to period 32
_pr98 = walk84(16, 161 | (161 << 8))
_drv98 = _pr98[-2]
ok98 &= len(_pr98) - 1 == 52808 and 399 + 52808 == 53207 and _lp82(_drv98, 16) == 16
ok98 &= bin(_drv98).count('1') % 2 == 0
# telescoping and the bounds M <= lambda <= k M on random schedules; GPT's two multiplicity controls
_rng98 = random.Random(200)
for trial in range(200):
    j = _rng98.randint(1, 8)
    q = 2 ** j
    r = [_rng98.randint(1, 500) for _ in range(_rng98.randint(1, 6))]
    z = [_rng98.randint(1, 50)]
    for x in r:
        z.append(z[-1] + x)
    ell, lam, M = z[-1] - z[0], _Fr(sum(r), q), _Fr(max(r), q)
    ok98 &= ell == sum(r) and M <= lam <= len(r) * M
for j in range(1, 12):
    q = 2 ** j
    ok98 &= _Fr(q * q * 12, q) == 12 * q and _Fr(12, q) == _Fr(12, q)                  # k = q^2: lambda 12q, M 12/q
    ok98 &= _Fr(q * 12, q) == 12                                                        # k = q: lambda stays 12
check('S98 G200: rooted zero sources at 2, 7, 28, 399 give single excursions 5, 21, 371 with odd sources; the '
      'period-16 '
      'stage\'s first return (52,808, depth 53,207) is an even branch; telescoping and M <= lambda <= k M', ok98)
def sib99(a, q, depth):
    """Both continuations after an even zero driver (a, 0): profiles 0, c, 1, ... and 0, 1 + c, 1, ... ."""
    out = []
    for c in sorted(_rq3.children(a, 0, q)):
        x, y, prof = 0, c, [0, c]
        for _ in range(depth):
            kids = _rq3.children(x, y, q)
            if len(kids) != 1:
                break
            x, y = y, kids[0]
            prof.append(y)
        out.append(prof)
    return out


ok99, _n99 = True, 0
full99 = lambda q: (1 << q) - 1
# on every even-parity source at caps 4, 8 (and a sample at 16), the next profiles f, f' are disjoint and their union
# has no cyclic 00, so weight(f) + weight(f') >= q/2
_rng99 = random.Random(201)
for q in (4, 8, 16):
    srcs = [a for a in range(1, 1 << q) if bin(a).count('1') % 2 == 0]
    if q == 16:
        srcs = _rng99.sample(srcs, 400)
    for a in srcs:
        s = sib99(a, q, 4)
        if len(s) != 2 or min(len(p) for p in s) < 6:
            continue
        P, Pp = s
        c, cp = P[1], Pp[1]
        if cp != c ^ full99(q):
            P, Pp = Pp, P
            c, cp = P[1], Pp[1]
        ok99 &= cp == c ^ full99(q) and P[2] == Pp[2] == full99(q) and Pp[3] == P[3] ^ full99(q)
        f, fp = P[4], Pp[4]
        D = f ^ fp
        ok99 &= (f & fp) == 0
        ok99 &= all(((D >> t) & 1) or ((D >> ((t + 1) % q)) & 1) for t in range(q))
        ok99 &= bin(f).count('1') + bin(fp).count('1') >= q // 2
        _n99 += 1
ok99 &= _n99 >= 300
# GPT's rooted control: a = 0000110001010011 (a rotation of D1's driver), c = 0000010000110001
_W99 = lambda s_: sum(int(ch) << t for t, ch in enumerate(s_))
a, c = _W99('0000110001010011'), _W99('0000010000110001')
ok99 &= (c ^ _rq3.rot(c, 1, 16)) == a and bin(a).count('1') == 6 and _lp82(a, 16) == 16
ok99 &= any(_rq3.rot(a, k, 16) == _W99('1000101001100001') for k in range(16))
s = sib99(a, 16, 4)
P = [p for p in s if p[1] == c][0]
Pp = [p for p in s if p[1] == c ^ 0xFFFF][0]
e, f, g = P[3], P[4], P[5]
fp, gp = Pp[4], Pp[5]
bit = lambda u, t: (u >> (t % 16)) & 1
ok99 &= [bit(e, t) for t in (15, 0, 1, 2)] == [1, 0, 1, 1]
ok99 &= [bit(f, t) for t in (0, 1, 2)] == [0, 1, 0] and [bit(fp, t) for t in (1, 2)] == [0, 1]
ok99 &= bit(g, 2) == 0 and bit(g, 3) == 1 and bit(gp, 3) == 1 and (g & gp) != 0
check('S99 G201: after every even zero driver at caps 4, 8 (and 400 at 16) the next sibling profiles are disjoint with '
      'no cyclic 00 in their union; on the rooted q = 16 source the following profiles share phase 3', ok99)
ok100 = True
_pi100 = lambda u: bin(u).count('1') & 1
_wt100 = lambda u: bin(u).count('1')


def _E100(b, c, q):
    """G202 addendum: rises of c outside resets, |S c AND NOT (b OR c)| within the q-bit block."""
    return _wt100(_rq3.rot(c, 1, q) & ~(b | c) & ((1 << q) - 1))


# every q-periodic compatible triple S c = a XOR (b OR c), q = 1 .. 8 exhaustively: the mod-2 identity
# pi(a) = pi(b) XOR pi(b AND c), the integer identity |a| - |b| = 2 E(b, c) - |b AND c|, and a = 1 at every counted rise
for q in range(1, 9):
    cls = {}
    for a in range(1 << q):
        for b in range(1 << q):
            for c in _rq3.children(a, b, q):
                ok100 &= _pi100(a) == _pi100(b) ^ _pi100(b & c)
                ok100 &= _wt100(a) - _wt100(b) == 2 * _E100(b, c, q) - _wt100(b & c)
                ok100 &= (_rq3.rot(c, 1, q) & ~(b | c) & ~a & ((1 << q) - 1)) == 0
                cls.setdefault((_pi100(a), _pi100(b)), set()).add(_pi100(c))
    # pi(c) cancels: from q = 3 every class (pi(a), pi(b)) admits both parities of c (at q = 2 class (1, 0) forces 1)
    if q >= 3:
        ok100 &= len(cls) == 4 and all(v == {0, 1} for v in cls.values())
# not vacuous: at q = 4 both identities fail on some incompatible triples
ok100 &= any(_pi100(a) != _pi100(b) ^ _pi100(b & c) for a, b, c in product(range(16), repeat=3))
ok100 &= any(_wt100(a) - _wt100(b) != 2 * _E100(b, c, 4) - _wt100(b & c) and _pi100(a) == _pi100(b) ^ _pi100(b & c)
             for a, b, c in product(range(16), repeat=3))


def _bal100(prof, q):
    """One excursion prof = [0, w_(z+1), ..., a_next, 0]: XOR and integer sums of overlaps over n = z+1 .. z_next-1."""
    I = [prof[n] & prof[n + 1] for n in range(1, len(prof) - 1)]
    E = [_E100(prof[n], prof[n + 1], q) for n in range(1, len(prof) - 1)]
    x = 0
    for v in I:
        x ^= _pi100(v)
    return x, sum(_wt100(v) for v in I), sum(E)


# the rooted reached graphs at caps 1, 2, 4, 8: every edge obeys both identities; no state (0, 0) is reached (so every
# returning source is nonzero); along the root path to the single cap exit, each excursion's syndrome is pi_q of its
# returning source and its overlap total is |a_next| + 2 sum E. The doubled period-q/2 exits are even over q bits
# (syndrome 0); only the cap exit is odd, and it has no q-periodic child while its doubled child has least period 2q
for q, zexp, synexp in ((1, [2], [1]), (2, [2, 7], [0, 1]), (4, [2, 7, 28], [0, 0, 1]),
                        (8, [2, 7, 28, 399], [0, 0, 0, 1])):
    _rt100, _dp100, _pa100, _ed100, _ex100 = _rq3.reached(q)
    ok100 &= (0, 0) not in _dp100 and _ex100 == 1
    for (a, b), tgt, d in _ed100:
        c = _rq3.rot(tgt[1], -d, q)
        ok100 &= _rq3.rot(tgt[0], -d, q) == b and _pi100(b & c) == _pi100(a) ^ _pi100(b)
        ok100 &= _wt100(b & c) == _wt100(b) - _wt100(a) + 2 * _E100(b, c, q)
    _snk100 = [s_ for s_ in _dp100 if not _rq3.children(s_[0], s_[1], q)]
    ok100 &= len(_snk100) == 1
    chain, s_ = [], _snk100[0]
    while _pa100[s_] is not None:                   # literal triples (in each source state's frame) back to the root
        par, d, c = _pa100[s_]
        chain.append((par, c))
        s_ = par
    chain.reverse()
    w = {-1: 0}                                     # the root (0, 1...1) is (w_-1, w_0)
    for n, (st, c) in enumerate(chain):
        w[n], w[n + 1] = st[1], c
    zeros = [n for n in range(len(chain) + 1) if w[n] == 0]
    ok100 &= zeros == zexp
    syn = []
    for zp, zn in zip([-1] + zeros, zeros):
        x, tot = 0, 0
        for n in range(zp + 1, zn):
            x ^= _pi100(chain[n][0][1] & chain[n][1])
            tot += _wt100(chain[n][0][1] & chain[n][1]) - 2 * _E100(chain[n][0][1], chain[n][1], q)
        syn.append(x)
        ok100 &= x == _pi100(w[zn - 1]) and tot == _wt100(w[zn - 1]) and w[zn - 1] != 0
    ok100 &= syn == synexp
    a_ex = w[zexp[-1] - 1]
    ok100 &= _pi100(a_ex) == 1 and not _rq3.children(a_ex, 0, q)
    _k2 = _rq3.children(a_ex | (a_ex << q), 0, 2 * q)
    ok100 &= len(_k2) == 2 and all(_rq3.pair_lp(k, 0, 2 * q) == 2 * q for k in _k2)
    if q == 8:                                      # the period-8 stage: one excursion, l = 371, k = 1
        tot = 0
        for n in range(29, 399):
            tot += _wt100(chain[n][0][1] & chain[n][1])
        ok100 &= 399 - 28 == 371 and 8 * (371 - 1) >= tot >= 2 * 1 - 1 and tot >= _wt100(a_ex)
# the two known first returns after odd doublings: S97's q = 8 witness (r = 88) ends at the odd driver 00111101, an
# exit with no q-periodic child (syndrome 1); S98's rooted q = 16 (r = 52,808) ends at an even driver, an internal
# branch (syndrome 0), where extending one index to the zero's q-periodic child keeps the identity. Both balances exact
for prof, q, rr, par in ((_pr97, 8, 88, 1), (_pr98, 16, 52808, 0)):
    x, tot, Es = _bal100(prof, q)
    drv = prof[-2]
    ok100 &= len(prof) - 1 == rr and drv != 0 and _pi100(drv) == par == x
    ok100 &= tot == _wt100(drv) + 2 * Es and tot >= _wt100(drv)
    _kd100 = _rq3.children(drv, 0, q)
    ok100 &= (not _kd100) if par else (len(_kd100) == 2 and all(_pi100(drv) == _pi100(0 & k) for k in _kd100))
ok100 &= _pr97[-2] == sum(int(ch) << t for t, ch in enumerate('00111101'))
# G202's literal rooted control (G185 / S75, q = 4 on cap 8), time 0 in the low bit: masks, weights, the equation for f
_W100 = lambda s_: sum(int(ch) << t for t, ch in enumerate(s_))
a, c, one, e, f = (_W100(s_) for s_ in ('01110111', '00101101', '11111111', '01101001', '01001010'))
ok100 &= [a, c, one, e, f] == [238, 180, 255, 150, 82] and [_wt100(u) for u in (c, one, e, f)] == [4, 8, 4, 3]
ok100 &= (e | f) == _W100('01101011') and _rq3.rot(f, 1, 8) == _W100('10010100') == one ^ (e | f)
_sq100 = [a, 0, c, one, e, f]
ok100 &= all(_sq100[i + 2] in _rq3.children(_sq100[i], _sq100[i + 1], 8) for i in range(4))
# rooted: some choice of per-state rotations puts the five pairs at depths 28 .. 32 on consecutive reached edges, with
# k_(i+1) = k_i + delay_i, so in absolute time the suffix is the literal words under one common rotation
_rt100, _dp100, _pa100, _ed100, _ex100 = _rq3.reached(8)
_Ed100 = {(s_, t_): d for s_, t_, d in _ed100}
_pr100 = lambda i, k: (_rq3.rot(_sq100[i], k, 8), _rq3.rot(_sq100[i + 1], k, 8))
_ch100 = [ks for ks in product(range(8), repeat=5)
          if all(_dp100.get(_pr100(i, ks[i])) == 28 + i for i in range(5))
          and all((_pr100(i, ks[i]), _pr100(i + 1, ks[i + 1])) in _Ed100 for i in range(4))]
# each k_i is fixed only modulo its pair's least period (the state at depth 28 has pair period 4), so delays agree
# modulo the gcd of source and target pair periods on every chain, and exactly (mod 8) on at least one
_dl100 = lambda ks, i: (ks[i] + _Ed100[(_pr100(i, ks[i]), _pr100(i + 1, ks[i + 1]))] - ks[i + 1])
_pp100 = lambda i: _rq3.pair_lp(_sq100[i], _sq100[i + 1], 8)
ok100 &= bool(_ch100) and all(_dl100(ks, i) % math.gcd(_pp100(i), _pp100(i + 1)) == 0
                              for ks in _ch100 for i in range(4))
ok100 &= any(all(_dl100(ks, i) % 8 == 0 for i in range(4)) for ks in _ch100)
_sm100 = lambda x, y: (_pi100(x), _pi100(y), _pi100(x & y))
for ks in _ch100:
    s30, s31 = _pr100(2, ks[2]), _pr100(3, ks[3])
    ok100 &= _sm100(*s30) == _sm100(*s31) == (0, 0, 0)
    ok100 &= {_pi100(k) for k in _rq3.children(*s30, 8)} == {0}
    ok100 &= {_pi100(k) for k in _rq3.children(*s31, 8)} == {1}
# the addendum's hand control on (one, e, f): |e AND f| = 2, E(e, f) = 3, 8 - 4 = 2*3 - 2; without E, overlap -4
ok100 &= _wt100(e & f) == 2 and _E100(e, f, 8) == 3 and 8 - 4 == 2 * _E100(e, f, 8) - _wt100(e & f)
ok100 &= _wt100(e) - _wt100(one) == -4
check('S100 G202: pi(a) = pi(b) + pi(b AND c) and |a| - |b| = 2E - |b AND c| on every compatible triple '
      '(q <= 8) and rooted edge; syndrome 1 only at exits; overlap = |a_next| + 2 sum E; S75 transfer at 28-32', ok100)
ok101 = True
_wt101 = lambda u: bin(u).count('1')


def _exc101(prof, q):
    """G203's quantities on one excursion u_0 = 0, ..., u_r = 0: r, T, E_total, w, V(w)."""
    r, full = len(prof) - 1, (1 << q) - 1
    T = sum(_wt101(prof[n] & prof[n + 1]) for n in range(1, r))
    E = sum(_wt101(_rq3.rot(prof[n + 1], 1, q) & ~(prof[n] | prof[n + 1]) & full) for n in range(1, r))
    w = prof[r - 1]
    return r, T, E, w, _wt101(w ^ _rq3.rot(w, 1, q))


def _check101(prof, q):
    """Every G203 statement on one first-return excursion with c and w nonconstant."""
    full = (1 << q) - 1
    r, T, E, w, V = _exc101(prof, q)
    c = prof[1]
    good = r >= 5 and prof[r - 2] == w and T == _wt101(w) + 2 * E
    good &= prof[2] == full and prof[3] == full ^ _rq3.rot(c, -1, q)                    # 0, c, 1, e = 1 + S^-1 c
    good &= _wt101(prof[1] & prof[2]) + _wt101(prof[2] & prof[3]) == q                  # startup charge q
    good &= T >= q + _wt101(w) and 2 * E >= q
    if r >= 6:
        good &= prof[r - 3] == w ^ _rq3.rot(w, 1, q)                                   # u_(r-3) = w + S w
        good &= _wt101(prof[r - 3] & w) * 2 == V and T >= q + _wt101(w) + V // 2 and 4 * E >= 2 * q + V
        good &= E >= q // 2 + 1
    else:                                                                               # r = 5: w alternating
        good &= (w ^ _rq3.rot(w, 1, q)) == full
    return good, r


# ambient: every first-return excursion from an even zero driver (a, 0), both children, at even q = 2 .. 10, when c
# and w are nonconstant; r = 5 only where w alternates, and w = 1 never ends an excursion
_cnt101 = {}
for q in (2, 4, 6, 8, 10):
    full = (1 << q) - 1
    for a in range(1, 1 << q):
        if _wt101(a) % 2:
            continue
        for c in _rq3.children(a, 0, q):
            if c in (0, full):
                continue
            prof, x, y = [0, c], 0, c
            while y:
                x, y = y, _rq3.children(x, y, q)[0]
                prof.append(y)
            w = prof[-2]
            ok101 &= w != full
            if w == 0 or w == full:
                continue
            g, r = _check101(prof, q)
            ok101 &= g
            prim = _lp82(w, q) == q
            _cnt101[(q, r == 5, prim)] = _cnt101.get((q, r == 5, prim), 0) + 1
            if r == 5:
                ok101 &= (w ^ _rq3.rot(w, 1, q)) == full and _lp82(w, q) == 2              # alternating
            if q >= 4 and prim:
                ok101 &= r >= 6                                                         # primitive w: never r = 5
# r = 5 occurs at every q (from the alternating w, least period 2), but at q >= 4 never with a primitive w
ok101 &= all(_cnt101.get((q, True, q == 2), 0) == 2 for q in (2, 4, 6, 8, 10))
ok101 &= not any(k[1] and k[2] for k in _cnt101 if k[0] >= 4)
# the rooted q = 2 control: cap 2's root path, zeros at 2 and 7, equals 0, 01, 11, 01, 01, 0 up to rotation;
# T = 3 = q + |w|,
# E_total = 1 = q/2 (equality: no strict surplus)
_W101 = lambda s_: sum(int(ch) << t for t, ch in enumerate(s_))
_rt, _dp, _pa, _ed, _ex = _rq3.reached(2)
_sk = [s_ for s_ in _dp if not _rq3.children(s_[0], s_[1], 2)][0]
_ch, s_ = [], _sk
while _pa[s_] is not None:
    par, d, c = _pa[s_]
    _ch.append((par, c, d))
    s_ = par
_ch.reverse()
# literal profiles in absolute time: undo the per-edge delays
_prof, shift = [], 0
for n, (st, c, d) in enumerate(_ch):
    if n == 0:
        _prof += [_rq3.rot(st[0], -shift, 2), _rq3.rot(st[1], -shift, 2)]
    _prof.append(_rq3.rot(c, -shift, 2))
    shift += d
_z = [n for n, u in enumerate(_prof) if u == 0]                      # index n is depth n - 1 (the root's w_-1 first)
_seg = _prof[_z[1]:_z[2] + 1]
ok101 &= [z - 1 for z in _z[1:3]] == [2, 7]
_tgt = [_W101(s_) for s_ in ('00', '01', '11', '01', '01', '00')]
ok101 &= any([_rq3.rot(u, k, 2) for u in _seg] == _tgt for k in range(2))
ok101 &= _exc101(_tgt, 2)[:3] == (5, 3, 1) and _check101(_tgt, 2) == (True, 5)
ok101 &= [_wt101(_tgt[n] & _tgt[n + 1]) for n in range(1, 5)] == [1, 1, 1, 0]
# GPT's retained failure: the mixed-phase sketch 0, 01, 11, 10, 10, 0 breaks compatibility
_bad = [_W101(s_) for s_ in ('00', '01', '11', '10', '10', '00')]
ok101 &= not all(_bad[i + 2] in _rq3.children(_bad[i], _bad[i + 1], 2) for i in range(4))
# the two recorded first returns (S97's q = 8, r = 88; S98's rooted q = 16, r = 52,808): r >= 6 and every bound
for prof, q in ((_pr97, 8), (_pr98, 16)):
    g, r = _check101(prof, q)
    ok101 &= g and r >= 6
# units control: a primitive word with a single one has V = 2 at every q >= 2
ok101 &= all(_wt101(1 ^ _rq3.rot(1, 1, q)) == 2 for q in range(2, 33))
check('S101 G203: on every first return from an even zero (q = 2 .. 10, c and w nonconstant) and the rooted returns, '
      'T >= q + |w| (+ V(w)/2 when r >= 6), r >= 5, r = 5 only with w alternating; rooted q = 2 equality', ok101)
import pathlib as _pl102
import re as _re102
ok102 = True
_rng102 = random.Random(204)
# the interval lemma, min B - max A <= min(B - A) <= min B - min A, and G204's separation rule: with h* attaining min B,
# L = the least rival B and U = the largest rival A, L - U > D* forces h* to be the unique minimizer of D = B - A
_sep102 = 0
for trial in range(3000):
    n = _rng102.randint(2, 7)
    A = [_rng102.randint(1, 300) for _ in range(n)]
    B = [a + _rng102.randint(1, 400) for a in A]
    D = [b - a for a, b in zip(A, B)]
    ok102 &= min(B) - max(A) <= min(D) <= min(B) - min(A)
    s = B.index(min(B))
    if B.count(min(B)) == 1:
        L = min(B[i] for i in range(n) if i != s)
        U = max(A[i] for i in range(n) if i != s)
        if L - U > D[s]:
            _sep102 += 1
            ok102 &= D.index(min(D)) == s and D.count(min(D)) == 1
ok102 &= _sep102 >= 50
# GPT's abstract counterfactual: entries (10, 100) and (80, 110)
ok102 &= (100 - 10, min(100 - 10, 110 - 80), 100 - 80) == (90, 30, 20)
# the recorded integers, read from the committed outcomes (rule30_tm5b.py's docstring, rule30_tm6.c's header)
_d102 = _pl102.Path(__file__).parent
_t5b = _d102.joinpath('rule30_tm5b.py').read_text()
_m102 = _re102.search(r'N_5 over the histories: ([\d,\s]+?)\. So', _t5b).group(1)
_n5 = [int(x.replace(',', '')) for x in _m102.replace('\n', ' ').split(', ')]
_t6 = _d102.joinpath('rule30_tm6.c').read_text()
ok102 &= len(_n5) == 16 and max(_n5) == 894235 and min(_n5) == 87867 and 667052 in _n5
ok102 &= 'N_6 = 65,821,413' in _t6 and 'entered period 32 at 667,052' in _t6 and 'below depth 67,108,864' in _t6
# the frontier is a completed round's end: rounds of 2^24, and the winning exit lies inside round 4
_F102 = 4 * 2 ** 24
ok102 &= _F102 == 67108864 and 3 * 2 ** 24 < 65821412 < _F102
_Ds, _Dr = 65821413 - 667052, _F102 + 1 - max(_n5)
ok102 &= (_Ds, _Dr, _Dr - _Ds) == (65154361, 66214630, 1060269) and 65821412 - 667051 == _Ds
ok102 &= _Fr(_Ds, 32) == 2036073 + _Fr(25, 32) and 65821413 - min(_n5) == 65733546
# the round convention modelled: a walk advanced while d < round_end may hold an unprocessed odd zero at depth F
# exactly; its entry is then F + 1, so F + 1 (not F + 2) is the safe bound, and it can be attained
for zf in (_F102 - 1, _F102, _F102 + 1):
    d, re_, ent = 0, 0, None
    while ent is None:
        re_ += 2 ** 24
        while d < re_:
            if d == zf:
                ent = d + 1
                break
            d += 2 ** 20                      # coarse steps that land on the round ends and on F +- 1 below
            if d > zf:
                d = zf
    ok102 &= (ent >= _F102 + 1) == (zf >= _F102) and (zf != _F102 or ent == _F102 + 1)
check('S102 G204: min B - max A <= min(B - A) <= min B - min A and the rival separation on 3,000 random families; '
      'recorded entries give D* = 65,154,361 against rivals >= 66,214,630; min lambda_5 = 2,036,073 + 25/32', ok102)
ok103 = True


def _step103(row, L, R, lo):
    """One Rule 30 step on a row given on [lo, lo + len) with constant tails L (left) and R (right)."""
    n = len(row)
    get = lambda i: L if i < lo else (R if i >= lo + n else row[i - lo])
    new = [get(i - 1) ^ (get(i) | get(i + 1)) for i in range(lo - 1, lo + n + 1)]
    return new, L ^ (L | L), R ^ (R | R), lo - 1


def _run103(row, L, R, lo, T):
    rows = [(row, L, R, lo)]
    for _ in range(T):
        rows.append(_step103(*rows[-1]))
    return rows


def _cell103(state, i):
    row, L, R, lo = state
    return L if i < lo else (R if i >= lo + len(row) else row[i - lo])


_rng103 = random.Random(295)
# (a) the diagonal recursion D_k(t + 1) = D_(k-2)(t) + (D_(k-1)(t) OR D_k(t)), D_k(t) = x(k - t, t), on random rows
for trial in range(40):
    n = _rng103.randint(5, 30)
    rows = _run103([_rng103.randint(0, 1) for _ in range(n)], _rng103.randint(0, 1), _rng103.randint(0, 1), 0, 12)
    D = lambda k, t: _cell103(rows[t], k - t)
    ok103 &= all(D(k, t + 1) == D(k - 2, t) ^ (D(k - 1, t) | D(k, t)) for t in range(11) for k in range(-15, 45))
# (b) GPT's coalescing pair: black through site 0 then white, and black except site 0, both give one black cell at 1
_A103 = _step103([1, 0, 0, 0], 1, 0, 0)
_B103 = _step103([0, 1, 1, 1], 1, 1, 0)
ok103 &= all(_cell103(_A103, i) == _cell103(_B103, i) == (1 if i == 1 else 0) for i in range(-6, 10))
ok103 &= _cell103((([1, 0, 0, 0]), 1, 0, 0), 0) != _cell103(([0, 1, 1, 1], 1, 1, 0), 0)   # they differed at 0
# (c) random finite nonempty perturbations: the difference set stays nonempty and finite, k_min never decreases and
# rises only when the diagonal below it is black, and k_min's total rise is the sum of the rises (the speed identity)
for trial in range(300):
    n = _rng103.randint(8, 24)
    base = [_rng103.randint(0, 1) for _ in range(n)]
    L, R = _rng103.randint(0, 1), _rng103.randint(0, 1)
    pert = base[:]
    for i in _rng103.sample(range(n), _rng103.randint(1, 3)):
        pert[i] ^= 1
    T = 20
    X, Y = _run103(base, L, R, 0, T), _run103(pert, L, R, 0, T)
    kmin = []
    for t in range(T + 1):
        lo, hi = -t - 2, n + t + 2
        diff = [i for i in range(lo, hi) if _cell103(X[t], i) != _cell103(Y[t], i)]
        ok103 &= bool(diff)
        kmin.append(min(diff) + t)
    D = lambda k, t: _cell103(X[t], k - t)
    rises = 0
    for t in range(T):
        ok103 &= kmin[t + 1] >= kmin[t]
        if kmin[t + 1] > kmin[t]:
            ok103 &= D(kmin[t] - 1, t) == 1
            rises += kmin[t + 1] - kmin[t]
    ok103 &= kmin[T] - kmin[0] == rises
# (d) the barrier lock by the recursion: with agreement on diagonals <= w and D_w = 0 from t0, a difference on w + 1
# is permanent; with a difference on w - 1 at one time it heals (the corollary's hypothesis is needed)
for trial in range(200):
    T = 15
    low = [[_rng103.randint(0, 1) for _ in range(T + 1)] for _ in range(2)]        # common D_(w-1), D_w = 0
    up = _rng103.randint(0, 1)
    d1, d2 = [up], [up ^ 1]
    for t in range(T):
        d1.append(low[0][t] ^ d1[-1])
        d2.append(low[0][t] ^ d2[-1])
    ok103 &= all(a != b for a, b in zip(d1, d2))
    lowB = low[0][:]
    tb = _rng103.randint(0, T - 1)
    lowB[tb] ^= 1                                                                    # copy B differs on w - 1 at tb
    e1, e2 = [up], [up ^ 1]
    for t in range(T):
        e1.append(low[0][t] ^ e1[-1])
        e2.append(lowB[t] ^ e2[-1])
    ok103 &= e1[tb + 1] == e2[tb + 1]                                                # healed at tb + 1
check('S103 C4 repair (GPT R3): the diagonal recursion on random rows; GPT\'s coalescing pair; on 300 finite '
      'perturbations the damage persists, k_min rises only over a black diagonal and telescopes; the barrier lock '
      'holds with agreement below and fails without it', ok103)
ok104 = True
_rng104 = random.Random(299)


def _cols104(vis, hid, depth=7):
    """Columns 0, -1, ..., -depth beside the wall (column 0 is 0 at even times, 1 at odd), from column 1 with visible
    bits vis[s] at time 2s and hidden bits hid[s] at time 2s + 1, by the inverse rule
    x(-j, t) = x(-j + 1, t + 1) XOR (x(-j + 1, t) OR x(-j + 2, t))."""
    T = 2 * len(vis)
    col1 = [vis[t // 2] if t % 2 == 0 else hid[t // 2] for t in range(T)]
    wall = [t % 2 for t in range(T)]
    cols = [col1, wall]                                    # cols[k] is column 1 - k
    for j in range(1, depth + 1):
        right, right2 = cols[-1], cols[-2]
        cols.append([right[t + 1] ^ (right[t] | right2[t]) for t in range(len(right) - 1)])
    return cols


def _r4_104(j, A, B, D, E):
    """R4's even/odd pair at depth j on the admissible domain."""
    return {1: (1 ^ A, 1), 2: (A, B), 3: (1 ^ B, 1 ^ B), 4: (0, D), 5: ((1 ^ B) ^ D, 1 ^ B), 6: (D, B ^ D ^ E),
            7: (1 ^ D ^ E, 1 ^ E ^ (B & E))}[j]


# every visible word of length 8 with no 11 (Lemma 3's admissibility consequence), random hidden bits: R4's table holds
# at every s with room, and the columns ignore the hidden bits
_nw104 = 0
for v in range(1 << 8):
    vis = [(v >> i) & 1 for i in range(8)]
    if any(vis[i] & vis[i + 1] for i in range(7)):
        continue
    _nw104 += 1
    cA = _cols104(vis, [_rng104.randint(0, 1) for _ in range(8)])
    cB = _cols104(vis, [_rng104.randint(0, 1) for _ in range(8)])
    for j in range(1, 8):
        colA, colB = cA[1 + j], cB[1 + j]
        ok104 &= colA == colB                                                       # hidden bits invisible
        for s in range(4):
            if 2 * s + 1 < len(colA):
                A, B, D, E = vis[s], vis[s + 1], vis[s + 2], vis[s + 3]
                ok104 &= (colA[2 * s], colA[2 * s + 1]) == _r4_104(j, A, B, D, E)
ok104 &= _nw104 == 55                                                               # Fibonacci F(10)
# C7's formal table on arbitrary visible words: column -4 at time 2s is c_s c_(s+1), and nonzero for some word
_f104 = False
for v in range(1 << 8):
    vis = [(v >> i) & 1 for i in range(8)]
    c = _cols104(vis, [0] * 8)
    for s in range(3):
        ok104 &= c[5][2 * s] == vis[s] & vis[s + 1] and c[5][2 * s + 1] == vis[s + 2]
        _f104 |= c[5][2 * s] == 1
ok104 &= _f104
# realizability by the actual driven right side: GPT's four seeds (width 8, zero padding), column 0 held at the wall
def _drive104(seed, T, pad=24):
    row = seed + [0] * pad                                                          # columns 1, 2, ...
    vis, hid = [], []
    for t in range(T):
        (vis if t % 2 == 0 else hid).append(row[0])
        wall = t % 2
        row = [(wall if i == 0 else row[i - 1]) ^ (row[i] | (row[i + 1] if i + 1 < len(row) else 0))
               for i in range(len(row))]
    return vis, hid
_out104 = []
for sd in ('01101000', '00100000', '00000000', '00000010'):
    vis, hid = _drive104([int(ch) for ch in sd], 16)
    ok104 &= not any(vis[i] & vis[i + 1] for i in range(len(vis) - 1))              # admissible: no 11
    cols = _cols104(vis, hid)
    _out104.append((vis[0], vis[1], vis[2], vis[3], cols[8][1]))
ok104 &= [o[0] for o in _out104] == [0] * 4 and [o[2] for o in _out104] == [0] * 4
ok104 &= [(o[1], o[3]) for o in _out104] == [(0, 0), (0, 1), (1, 0), (1, 1)]
ok104 &= [o[4] for o in _out104] == [1, 0, 1, 1]                                  # R4 printed 1, 1, 0, 1: a slip
ok104 &= _out104[0][4] ^ _out104[1][4] ^ _out104[2][4] ^ _out104[3][4] == 1        # mixed XOR 1: not affine
check('S104 GPT\'s R4 of C.7: on all 55 no-11 visible words R4\'s seven depth pairs hold and hidden bits are '
      'invisible; C.7\'s formal product holds on all words; GPT\'s four driven seeds give (B, E) = 00, 01, 10, 11, '
      'depth-7 odd outputs 1, 0, 1, 1 (mixed XOR 1)', ok104)
ok105 = True
_rng105 = random.Random(306)
# GC306: R_(j+1) = (R_j + lambda_j)/2 with R_j = N_j/2^j and lambda_j = (N_(j+1) - N_j)/2^j, exactly, on the rooted
# record: the single cell's entries 3, 8, 29, 400, 87,867 and TM6's minimizing history to 65,821,413
for N in ([3, 8, 29, 400, 87867], [3, 8, 29, 400, 667052, 65821413]):
    R = [_Fr(n, 2 ** (j + 1)) for j, n in enumerate(N)]
    lam = [_Fr(N[j + 1] - N[j], 2 ** (j + 1)) for j in range(len(N) - 1)]
    ok105 &= all(R[j + 1] == (R[j] + lam[j]) / 2 for j in range(len(N) - 1))
ok105 &= [_Fr(3, 2), _Fr(5, 2), _Fr(21, 4), _Fr(371, 8)] == [_Fr(3, 2)] + [_Fr(b - a, 2 ** (j + 1)) for j, (a, b) in
                                                                         enumerate(zip([3, 8, 29], [8, 29, 400]))]
# bounded lambda <= K gives R <= max(R_start, K); bounded R <= M gives lambda <= 2M (exact, random sequences)
for trial in range(2000):
    K = _Fr(_rng105.randint(1, 50), _rng105.randint(1, 5))
    R0 = _Fr(_rng105.randint(1, 200), _rng105.randint(1, 5))
    R = R0
    for _ in range(40):
        lam = K * _Fr(_rng105.randint(0, 100), 100)
        R = (R + lam) / 2
        ok105 &= R <= max(R0, K)
    Rs = [_Fr(_rng105.randint(1, 100), 7) for _ in range(30)]
    M = max(Rs)
    ok105 &= all(2 * Rs[j + 1] - Rs[j] <= 2 * M for j in range(29))
# the limsups need not agree: lambda alternating 1, 3 drives R onto the 2-cycle 7/3 (after a 3), 5/3 (after a 1)
R = _Fr(10)
for j in range(200):
    R = (R + (1 if j % 2 == 0 else 3)) / 2
ok105 &= abs(R - _Fr(7, 3)) < _Fr(1, 10 ** 30) and abs((R + 1) / 2 - _Fr(5, 3)) < _Fr(1, 10 ** 30)
# fixed-root pruning: a sequence whose lambda is eventually <= K is bounded from the root by max(K, its earlier values)
for trial in range(500):
    j0 = _rng105.randint(0, 10)
    lam = [_rng105.randint(0, 1000) for _ in range(j0)] + [_rng105.randint(0, 20) for _ in range(30)]
    ok105 &= max(lam) <= max([20] + lam[:j0])
check('S105 GC306: R_(j+1) = (R_j + lambda_j)/2 exactly on the rooted record; bounded lambda <=> bounded R with '
      'R <= max(R_start, K) and lambda <= 2M; alternating 1, 3 gives the cycle 5/3, 7/3; fixed-root pruning suffices',
      ok105)
ok106 = True
# GC307's odd-run refinement of Theorem B (entry 06): build the forced left half from every pair of P-periodic columns
# 0 and 1 (column 0 nonzero) by the inverse rule x(-j, t) = x(-j + 1, t + 1) + (x(-j + 1, t) OR x(-j + 2, t)), P = 2 .. 7,
# 40 columns deep; in row 0, every maximal white run bounded by black cells inside the left half has length <= 2P - 2
# (Theorem B), and an odd run n = 2m + 1 >= 3 has n <= 2P - 5, its centre column white at times 0 .. m + 1
_max106 = {}
for P in range(2, 8):
    for w0 in range(1, 1 << P):
        for w1 in range(1 << P):
            cols = [[(w1 >> t) & 1 for t in range(P)], [(w0 >> t) & 1 for t in range(P)]]   # columns 1, 0
            for j in range(1, 41):
                r, r2 = cols[-1], cols[-2]
                cols.append([r[(t + 1) % P] ^ (r[t] | r2[t]) for t in range(P)])
            row = [cols[1 + k][0] for k in range(0, 41)]                                  # columns 0, -1, ..., -40
            k = 1
            while k <= 40:
                if row[k] == 0 and row[k - 1] == 1:
                    e = k
                    while e <= 40 and row[e] == 0:
                        e += 1
                    if e <= 40:                                                           # bounded by a black cell
                        n = e - k
                        ok106 &= n <= 2 * P - 2
                        if n % 2 and n >= 3:
                            m = (n - 1) // 2
                            ok106 &= n <= 2 * P - 5
                            centre = cols[1 + k + m]
                            ok106 &= all(centre[t % P] == 0 for t in range(m + 2))
                            _max106[(P, 'odd')] = max(_max106.get((P, 'odd'), 0), n)
                        elif n % 2 == 0:
                            _max106[(P, 'even')] = max(_max106.get((P, 'even'), 0), n)
                    k = e
                k += 1
# the singleton exception: spatial stripes 0101... are stationary, columns constant (P = 1), singleton white gaps
_row106 = [i % 2 for i in range(12)]
ok106 &= [_row106[i - 1] ^ (_row106[i] | _row106[i + 1]) for i in range(1, 11)] == _row106[1:11]
# the apex mechanism alone: a maximal white run of odd length n >= 3 with black ends shrinks with black ends, and its
# centre is white at time m + 1 (parents 101)
for n in (3, 5, 7, 9):
    m = (n - 1) // 2
    row = [1] * 4 + [0] * n + [1] * 4
    hist = [row]
    for t in range(m + 1):
        r = hist[-1]
        hist.append([r[i - 1] ^ (r[i] | r[i + 1]) if 0 < i < len(r) - 1 else 1 for i in range(len(r))])
    c = 4 + m
    ok106 &= all(hist[t][c] == 0 for t in range(m + 2)) and hist[m][c - 1] == hist[m][c + 1] == 1
check('S106 GC307 (entry 06 refinement): over all P-periodic column pairs, P = 2..7, every bounded row-0 white run has '
      'n <= 2P - 2 and every odd n >= 3 has n <= 2P - 5 with its centre white for m + 2 steps; stripes keep singletons',
      ok106)
ok107 = True
_rng107 = random.Random(310)
_E107 = lambda d: [sum(d[i] + 2 ** i - 1 for i in range(j + 1)) for j in range(len(d))]
# GC310's controls: d_i = C 2^i gives E_j <= 2(C + 1) 2^j; d_i <= i^2 2^i gives E_j <= 2(j^2 + 1) 2^j; period 1 adds
# overhead 2^0 - 1 = 0; assigning d_j = N_j makes N_j/(2^j + E_j) <= 1
for trial in range(200):
    C = _rng107.randint(0, 20)
    J = _rng107.randint(1, 60)
    E = _E107([C * 2 ** i for i in range(J)])
    ok107 &= all(E[j] <= 2 * (C + 1) * 2 ** j for j in range(J))
    E2 = _E107([_rng107.randint(0, i * i) * 2 ** i for i in range(J)])
    ok107 &= all(E2[j] <= 2 * (j * j + 1) * 2 ** j for j in range(J))
    N = sorted(_rng107.randint(1, 10 ** 12) for _ in range(J))
    E3 = _E107(N)
    ok107 &= all(_Fr(N[j], 2 ** j + E3[j]) <= 1 for j in range(J))
ok107 &= 2 ** 0 - 1 == 0
# the endpoint selection: for theta in (2, min(4, 6/gamma)) and s the largest power of 2 with ceil(theta s) <= N,
# N < ceil(2 theta s) <= 2 theta s + 1, so s > (N - 1)/(2 theta)
for trial in range(3000):
    gamma = _Fr(_rng107.randint(10, 29), 10)                                        # 1 <= gamma < 3
    hi = min(_Fr(4), _Fr(6) / gamma)
    theta = 2 + (hi - 2) * _Fr(_rng107.randint(1, 99), 100)
    N = _rng107.randint(10, 10 ** 15)
    s = 1
    while -((-theta * 2 * s) // 1) <= N:
        s *= 2
    c2 = -((-2 * theta * s) // 1)
    ok107 &= -((-theta * s) // 1) <= N < c2 <= 2 * theta * s + 1 and s > _Fr(N - 1) / (2 * theta)
# the joint test on a synthetic schedule (N_j = 4^j with polynomial allowances d_i = i^2 2^i, gamma = 5/2,
# theta = 11/5): (2^j + E_j)/s and P/s tend to 0 and (gamma M + E_j + B + P)/s tends to gamma theta < 6
gamma, theta, B = _Fr(5, 2), _Fr(11, 5), 100
E = _E107([i * i * 2 ** i for i in range(80)])
vals = []
for j in range(20, 80, 10):
    Nj = 4 ** j
    s = 1
    while -((-theta * 2 * s) // 1) <= Nj:
        s *= 2
    M = -((-theta * s) // 1)
    vals.append((_Fr(2 ** j + E[j], s), _Fr(gamma * M + E[j] + B + 2 ** j, s)))
ok107 &= all(a > b for (a, _), (b, _) in zip(vals, vals[1:])) and vals[-1][0] < _Fr(1, 10 ** 9)
ok107 &= gamma * theta < 6 and abs(vals[-1][1] - gamma * theta) < _Fr(1, 10 ** 6)
check('S107 GC310: E_j bounds for d_i = C 2^i and i^2 2^i, zero overhead at period 1, d_j = N_j fails the joint test; '
      'the dyadic endpoint selection N < ceil(2 theta s) <= 2 theta s + 1; the synthetic schedule meets the joint test',
      ok107)
ok108 = True


def _strip108(c0, c1, P, n):
    """GC313's width-n graph: state (phase, cells 2 .. n + 1 at that time); column 1's equation constrains cell 2;
    the far-right input (cell n + 2) is free. Returns the set of states left after pruning states with no successor
    (nonempty exactly when the graph has a cycle) and the successor map."""
    nxt = {}
    for p in range(P):
        a0, a1, b1 = (c0 >> p) & 1, (c1 >> p) & 1, (c1 >> ((p + 1) % P)) & 1
        for s in range(1 << n):
            succ = []
            if b1 == a0 ^ (a1 | (s & 1)):                       # x(1, t+1) = x(0, t) + (x(1, t) OR x(2, t))
                for b in (0, 1):
                    cell = lambda i: a1 if i == 1 else ((s >> (i - 2)) & 1 if i <= n + 1 else b)
                    s2 = sum((cell(i - 1) ^ (cell(i) | cell(i + 1))) << (i - 2) for i in range(2, n + 2))
                    succ.append(((p + 1) % P, s2))
            nxt[(p, s)] = succ
    alive = set(nxt)
    changed = True
    while changed:
        changed = False
        for v in list(alive):
            if not any(w in alive for w in nxt[v]):
                alive.discard(v)
                changed = True
    return alive, nxt


_W108 = lambda b: sum(v << t for t, v in enumerate(b))
# GPT's 01/11 boundary at P = 2 dies at width 1, whatever the exterior
ok108 &= not _strip108(_W108([0, 1]), _W108([1, 1]), 2, 1)[0]
# pairs failing column 1's one-step condition (a black cell must be followed by x(0, t) + 1) have no successor at all
for P in (2, 3, 4):
    for c0 in range(1 << P):
        for c1 in range(1 << P):
            bad = any(((c1 >> t) & 1) and ((c1 >> ((t + 1) % P)) & 1) != (((c0 >> t) & 1) ^ 1) for t in range(P))
            if bad:
                alive, nxt = _strip108(c0, c1, P, 2)
                ok108 &= not alive
# a periodic right continuation (AW's survivors, recomputed here for P = 2, 3, 4) gives cycles at every width 1 .. 5,
# and every surviving set covers all P phases
def _per108(P):
    def succ(u, v):
        out = [0]
        for t in range(P):
            need = ((v >> ((t + 1) % P)) & 1) ^ ((u >> t) & 1)
            if (v >> t) & 1:
                if need != 1:
                    return []
                out = [o | (b << t) for o in out for b in (0, 1)]
            else:
                out = [o | (need << t) for o in out]
        return out
    nodes = {(a, b): {(b, w) for w in succ(a, b)} for a in range(1 << P) for b in range(1 << P)}
    alive = set(nodes)
    changed = True
    while changed:
        changed = False
        for v in list(alive):
            if not (nodes[v] & alive):
                alive.discard(v)
                changed = True
    return alive
_npairs108 = 0
for P in (2, 3, 4):
    for c0, c1 in _per108(P):
        _npairs108 += 1
        for n in range(1, 6):
            alive, nxt = _strip108(c0, c1, P, n)
            ok108 &= bool(alive) and {p for p, _ in alive} == set(range(P))
ok108 &= _npairs108 == 3 + 15 + 31
# cycle lengths are multiples of P (phase advances by 1 each step): follow surviving successors from one state
for P, c0, c1 in ((2, _W108([0, 1]), _W108([0, 0])), (3, 5, 0), (4, 5, 0)):
    alive, nxt = _strip108(c0, c1, P, 4)
    if alive:
        v = min(alive)
        seen = {}
        k = 0
        while v not in seen:
            seen[v] = k
            v = min(w for w in nxt[v] if w in alive)
            k += 1
        ok108 &= (k - seen[v]) % P == 0
check('S108 GC313: the width-n strip graph (P 2^n states, column 1 constraint, free far input): 01/11 dies at width 1; '
      'one-step violations have no successor; surviving sets cover every phase; cycle lengths are multiples of P',
      ok108)
ok109 = True
# GC314: column 0 alternating (01 = 0 at even times) has no 2-periodic right companion. Literally: sigma_even = 1 breaks
# column 1's own update; sigma = 00 forces column 2 = column 0, whose odd update gives 1 at the next even time; sigma =
# 01 forces column 2 = 1 at even times, then 1 at odd, then 0 at even. Checked over every exterior bit x(3, t).
_tau109 = lambda t: t % 2
for se, so in ((0, 0), (0, 1), (1, 0), (1, 1)):
    sig = lambda t: se if t % 2 == 0 else so
    ok_any = False
    for x2 in range(1 << 6):                                          # column 2 on t = 0 .. 5
        for x3 in range(1 << 6):                                      # column 3 on t = 0 .. 5 (the exterior)
            c2 = lambda t: (x2 >> t) & 1
            c3 = lambda t: (x3 >> t) & 1
            if all(sig(t + 1) == _tau109(t) ^ (sig(t) | c2(t)) for t in range(5)) and \
               all(c2(t + 1) == sig(t) ^ (c2(t) | c3(t)) for t in range(5)):
                ok_any = True
                break
        if ok_any:
            break
    ok109 &= not ok_any                                               # no column 2, no exterior, already by t = 5
# the strip graph agrees: all four companions die at width 1 (and at widths 2 .. 6)
ok109 &= all(not _strip108(0b10, s_, 2, n)[0] for s_ in range(4) for n in range(1, 7))
# sidedness: constant black column 0 beside constant white column 1 is the stationary striped row, and survives
ok109 &= all(bool(_strip108(0b11, 0b00, 2, n)[0]) for n in range(1, 7))
_row109 = [1, 0] * 6
ok109 &= [_row109[i - 1] ^ (_row109[i] | _row109[i + 1]) for i in range(1, 11)] == _row109[1:11]
check('S109 GC314: an alternating column 0 has no period-two right companion: each of the four sigma fails by t = 5 for '
      'every column 2 and exterior, and dies at strip width 1; constant black beside constant white survives', ok109)
ok110 = True
_rng110 = random.Random(315)


def _debt110(inc, gamma):
    """GC312's reference debt: the largest forward rise of the prefix sums of the adjusted increments (inc - gamma)."""
    z, lo, best = 0, 0, 0
    for v in inc:
        z += v - gamma
        best = max(best, z - lo)
        lo = min(lo, z)
    return best


def _summary110(adj):
    """Block summary (A, m, H, D): total, least prefix (with 0), greatest prefix (with 0), largest forward rise."""
    z, lo, hi, best = 0, 0, 0, 0
    for v in adj:
        z += v
        best = max(best, z - lo)
        lo, hi = min(lo, z), max(hi, z)
    return z, lo, hi, best


# GC312's merge rule D = max(D1, D2, A1 + H2 - m1) against the direct rise of the joined block, on random blocks
for trial in range(3000):
    b1 = [_rng110.randint(-3, 3) for _ in range(_rng110.randint(0, 8))]
    b2 = [_rng110.randint(-3, 3) for _ in range(_rng110.randint(0, 8))]
    A1, m1, H1, D1 = _summary110(b1)
    A2, m2, H2, D2 = _summary110(b2)
    ok110 &= max(D1, D2, A1 + H2 - m1) == _summary110(b1 + b2)[3]
ok110 &= _summary110([2, -1])[3] == 2 and _summary110([2, -1, 2, -1])[3] == 3          # GPT's example: 2, 2, joined 3
# GC315's sharpness control: increments 1, 1, 0, 1 and 1, 1, 0, 2 at slope 1 have exact debts 0 and 1 (= P - 1 at P = 2)
ok110 &= _debt110([1, 1, 0, 1], 1) == 0 and _debt110([1, 1, 0, 2], 1) == 1
# the factor-2 invariance: with P <= 2^j and |D' - D| <= P - 1, (2^j + D')/(2^j + D) lies in [1/2, 2]
for trial in range(3000):
    j = _rng110.randint(1, 40)
    P = 2 ** _rng110.randint(0, j)
    D = _rng110.randint(0, 10 ** 12)
    D2 = max(0, D + _rng110.randint(-(P - 1), P - 1))
    r = _Fr(2 ** j + D2, 2 ** j + D)
    ok110 &= _Fr(1, 2) <= r <= 2
# the backward map B(y, z) = (S z + (y OR z), y) commutes with rotation, so rotating a terminal pair rotates the whole
# recovered prefix (q = 8, 16, 32, random pairs, 50 steps)
for q in (8, 16, 32):
    for trial in range(100):
        y, z = _rng110.getrandbits(q), _rng110.getrandbits(q)
        k = _rng110.randint(1, q - 1)
        a, b = y, z
        ra, rb = _rq3.rot(y, k, q), _rq3.rot(z, k, q)
        for _ in range(50):
            a, b = _rq3.rot(b, 1, q) ^ (a | b), a
            ra, rb = _rq3.rot(rb, 1, q) ^ (ra | rb), ra
            ok110 &= (ra, rb) == (_rq3.rot(a, k, q), _rq3.rot(b, k, q))
check('S110 GC312/GC315: the block merge D = max(D1, D2, A1 + H2 - m1) on 3,000 random joins (and 2, 2 -> 3); debts 0 '
      'and 1 for increments 1,1,0,1 and 1,1,0,2 at slope 1; global rotation moves the joint ratio by at most a factor '
      '2; B commutes with rotation', ok110)
ok111 = True
_rng111 = random.Random(316)


def _left111(c0, c1, P, depth):
    cols = [[(c1 >> t) & 1 for t in range(P)], [(c0 >> t) & 1 for t in range(P)]]      # columns 1, 0
    for j in range(1, depth + 1):
        r, r2 = cols[-1], cols[-2]
        cols.append([r[(t + 1) % P] ^ (r[t] | r2[t]) for t in range(P)])
    return cols                                                                           # cols[1 + k] is column -k


# GC316's re-anchoring: the forced left half is translation invariant. Re-anchor at column -r: the pair (column -r,
# column -r + 1) forces exactly the original columns to its left (random pairs, P = 3 .. 7, r up to 30)
for trial in range(300):
    P = _rng111.randint(3, 7)
    c0, c1 = _rng111.randint(1, (1 << P) - 1), _rng111.randint(0, (1 << P) - 1)
    cols = _left111(c0, c1, P, 60)
    r = _rng111.randint(1, 30)
    w = lambda col: sum(v << t for t, v in enumerate(col))
    sub = _left111(w(cols[1 + r]), w(cols[r]), P, 30)
    ok111 &= all(sub[1 + k] == cols[1 + r + k] for k in range(31))
# Theorem B puts any bounded run within 2P - 2 <= 12 columns, so a re-anchored run lies within 13 columns of its wall
ok111 &= all(2 * P - 2 + 1 <= 13 for P in range(3, 8))
# finite consistency at depth 200: on every pair with a periodic right continuation (P = 3 .. 7), no bounded row-0 run
# beats AW's actual maxima (odd 1, 1, 5, 5, 5; even 4, 6, 2, 4, 6)
_awmax111 = {3: (1, 4), 4: (1, 6), 5: (5, 2), 6: (5, 4), 7: (5, 6)}
for P in range(3, 8):
    for c0, c1 in _per108(P):
        if not c0:
            continue
        cols = _left111(c0, c1, P, 200)
        row = [cols[1 + k][0] for k in range(201)]
        k = 1
        while k <= 200:
            if row[k] == 0 and row[k - 1] == 1:
                e = k
                while e <= 200 and row[e] == 0:
                    e += 1
                if e <= 200:
                    n = e - k
                    ok111 &= n <= _awmax111[P][0 if n % 2 else 1]
                k = e
            k += 1
check('S111 GC316: the forced left half is translation invariant (re-anchoring at any black column reproduces the '
      'columns to its left); bounded runs fit in 13 columns at P <= 7; periodic-admissible pairs stay within AW\'s '
      'maxima to depth 200', ok111)
ok112 = True
_rng112 = random.Random(323)
# GC323's exact integer gate: with gamma = a/b and D^(b) = max over u <= v of b(T_v - T_u) - a(v - u) = b D, the test
# b N > K (b q + D^(b)) is N > K (q + D); an upper debt U >= D that passes also certifies D; a lower bound L <= D only
# bounds the ratio from above (random clocks)
for trial in range(2000):
    a, b = _rng112.randint(1, 29), _rng112.randint(1, 10)
    if _Fr(a, b) >= 3 or _Fr(a, b) < 1:
        continue
    T = [0]
    for _ in range(_rng112.randint(1, 30)):
        T.append(T[-1] + _rng112.randint(0, 6))
    Db = max(b * (T[v] - T[u]) - a * (v - u) for u in range(len(T)) for v in range(u, len(T)))
    D = max(_Fr(T[v] - T[u]) - _Fr(a, b) * (v - u) for u in range(len(T)) for v in range(u, len(T)))
    ok112 &= Db == b * D
    N, q, K = _rng112.randint(1, 10 ** 6), 2 ** _rng112.randint(0, 6), _rng112.randint(1, 50)
    ok112 &= (b * N > K * (b * q + Db)) == (N > K * (q + D))
    U = D + _rng112.randint(0, 20)
    if N > K * (q + U):
        ok112 &= N > K * (q + D)
    L = D - _rng112.randint(0, 20)
    ok112 &= _Fr(N, q + max(L, 0)) >= _Fr(N, q + D) if L >= 0 else True
# the all-phase gate: |D_phi - D| <= q - 1 gives q + D_phi <= 2q - 1 + D, so N > K(2q - 1 + D) passes every phase
for trial in range(2000):
    q = 2 ** _rng112.randint(0, 10)
    D = _rng112.randint(0, 10 ** 5)
    Dphi = max(0, D + _rng112.randint(-(q - 1), q - 1))
    N, K = _rng112.randint(1, 10 ** 8), _rng112.randint(1, 100)
    if N > K * (2 * q - 1 + D):
        ok112 &= N > K * (q + Dphi)
# GPT's asynchronous control: q_j = 2^j, N_j = 2^(j^2); history A has D_j = N_j at odd j (carried to the next even j),
# B the reverse; each debt sequence is nondecreasing, each history's ratio is unbounded along alternate stages, and
# the smaller of the two current ratios is below 1 at every stage
def _hist112(odd, J):
    D, out = 0, []
    for j in range(2, J):
        if j % 2 == odd:
            D = 2 ** (j * j)
        out.append((j, D))
    return out
_A112, _B112 = _hist112(1, 26), _hist112(0, 26)
ok112 &= all(x[1] <= y[1] for h in (_A112, _B112) for x, y in zip(h, h[1:]))
_QA = [_Fr(2 ** (j * j), 2 ** j + D) for j, D in _A112]
_QB = [_Fr(2 ** (j * j), 2 ** j + D) for j, D in _B112]
ok112 &= all(min(x, y) < 1 for x, y in zip(_QA, _QB))
ok112 &= max(_QA) > 2 ** 40 and max(_QB) > 2 ** 40
check('S112 GC323: the exact integer gate equals N > K(q + D); upper debt certifies, lower debt only bounds above; the '
      'all-phase gate N > K(2q - 1 + D); the asynchronous two-path control (both unbounded, minimum current ratio < 1)',
      ok112)
ok113 = True


def _rd113(w, T, q):
    if w == 0:
        return 0
    return next(i + 1 for i in range(q) if (w >> ((T + i) % q)) & 1)


# GC326's sparse episode: source a = e_s + e_(s+2), driver b = e_s; children 1 + e_(s+1) + e_(s+2), then
# 1 + e_(s+1) + e_(s+2) + e_(s+3), then e_(s+4); from phase s + 1 the reset delays are q, 3, 1, q. Every rotation, q = 4 .. 32
_n113 = 0
for q in range(4, 33):
    full = (1 << q) - 1
    e = lambda i: 1 << (i % q)
    for s in range(q):
        a, b = e(s) | e(s + 2), e(s)
        c1 = full ^ e(s + 1) ^ e(s + 2)
        c2 = c1 ^ e(s + 3)
        c3 = e(s + 4)
        ok113 &= _rq3.children(a, b, q) == [c1] and _rq3.children(b, c1, q) == [c2] and _rq3.children(c1, c2, q) == [c3]
        T, ds = s + 1, []
        for w in (b, c1, c2, c3):
            dl = _rd113(w, T, q)
            ds.append(dl)
            T += dl
        ok113 &= ds == [q, 3, 1, q] and 2 * sum(ds) - 5 * 4 == 2 * (2 * q + 4) - 20
        _n113 += 1
ok113 &= _n113 == sum(range(4, 33))
# at q = 3 the whole four-step pattern fails at every rotation (it needs phases s .. s + 4 distinct enough); the first
# step alone still holds there, so the rejection is of the chain, not of its first edge
for s in range(3):
    e3 = lambda i: 1 << (i % 3)
    a, b = e3(s) | e3(s + 2), e3(s)
    c1 = 7 ^ e3(s + 1) ^ e3(s + 2)
    c2 = c1 ^ e3(s + 3)
    c3 = e3(s + 4)
    steps = (_rq3.children(a, b, 3) == [c1], _rq3.children(b, c1, 3) == [c2], _rq3.children(c1, c2, 3) == [c3])
    T, ds = s + 1, []
    for w in (b, c1, c2, c3):
        dl = _rd113(w, T, 3)
        ds.append(dl)
        T += dl
    ok113 &= not (all(steps) and ds == [3, 3, 1, 3]) and steps[0]
# at q = 16: cost 36 and slope-5/2 debt 26 over the four edges
ok113 &= 2 * 16 + 4 == 36 and 2 * 36 - 5 * 4 == 52
# the rooted occurrence: walk every rooted history at q = 16 in absolute time from the root and read the state and
# clock phase at depth 725,146 on the histories that exit period 16 at 770,531 and 894,234
_hits113 = []
_st113 = [(0, (1 << 16) - 1, 0, 0)]
while _st113:
    x, y, d, T = _st113.pop()
    while True:
        if d == 725146:
            _hits113.append((x, y, T % 16))
        if y == 0:
            kids = _rq3.children(x, 0, 16)
            if not kids:
                break
            c1, c2 = kids
            if not any(_rq3.rot(c1, k, 16) == c2 for k in range(16)):
                _st113.append((0, c2, d + 1, T))
            x, y, d = 0, c1, d + 1
            continue
        T += _rd113(y, T, 16)
        x, y, d = y, _rq3.children(x, y, 16)[0], d + 1
ok113 &= (320, 64, 7) in _hits113
check('S113 GC326: the sparse episode e_s + e_(s+2), e_s -> 1 + e_(s+1) + e_(s+2) -> ... -> e_(s+4) with delays q, 3, 1, q '
      'at every rotation for q = 4..32 (the chain fails at q = 3); cost 36, debt 26 at q = 16; the rooted state (320, 64) at '
      'phase 7 at depth 725,146', ok113)
ok114 = True
_rng114 = random.Random(327)
# GC327: the four-edge block's adjusted prefixes at slope 5/2 are 0, q - 5/2, q - 2, q - 7/2, 2q - 6 (doubled: 0, 2q - 5,
# 2q - 4, 2q - 7, 4q - 12), its debt is 2q - 6 for q >= 4 (a tie with q - 2 at q = 4), the transferred allowance 3q - 7
for q in range(4, 65):
    z = [0]
    for c in (q, 3, 1, q):
        z.append(z[-1] + 2 * c - 5)
    lo, D = z[0], 0
    for v in z:
        D = max(D, v - lo)
        lo = min(lo, v)
    ok114 &= z == [0, 2 * q - 5, 2 * q - 4, 2 * q - 7, 4 * q - 12] and min(z) == 0 and D == 4 * q - 12
    ok114 &= (2 * q - 6) + (q - 1) == 3 * q - 7
ok114 &= [(2 * q - 6, 3 * q - 7) for q in (4, 8, 16, 32)] == [(2, 5), (10, 17), (26, 41), (58, 89)]
ok114 &= all(sum(3 * 2 ** i - 7 for i in range(2, j + 1)) == 6 * 2 ** j - 7 * j - 5 <= 6 * 2 ** j for j in range(2, 40))
# the debt (largest forward rise) is subadditive over consecutive blocks: D(joined) <= D1 + D2 (random blocks)
def _rise114(adj):
    z, lo, best = 0, 0, 0
    for v in adj:
        z += v
        best = max(best, z - lo)
        lo = min(lo, z)
    return best
for trial in range(3000):
    b1 = [_rng114.randint(-5, 5) for _ in range(_rng114.randint(0, 9))]
    b2 = [_rng114.randint(-5, 5) for _ in range(_rng114.randint(0, 9))]
    ok114 &= _rise114(b1 + b2) <= _rise114(b1) + _rise114(b2)
# ancestry on the actual rooted period-16 tree (every history, absolute time): each history meets the start class
# (rotations of (e_0 + e_2, e_0)) at most once; the one rooted start is at depth 725,146 (shared by the two histories
# through it), and the pulses 64 and 1024 occur three columns apart there with different predecessors (320, 64639)
_start114 = {(_rq3.rot(1 | 4, k, 16), _rq3.rot(1, k, 16)) for k in range(16)}
_per114 = []
_st114 = [(0, (1 << 16) - 1, 0, ())]
while _st114:
    x, y, d, hits = _st114.pop()
    hits = list(hits)
    while True:
        if (x, y) in _start114:
            hits.append(d)
        if d == 725149 and y == 1024:
            ok114 &= x == 64639
        if d == 725146 and (x, y) == (320, 64):
            hits.append(-1)                                 # marker: the GC326 occurrence on this history
        if y == 0:
            kids = _rq3.children(x, 0, 16)
            if not kids:
                _per114.append(hits)
                break
            c1, c2 = kids
            if not any(_rq3.rot(c1, k, 16) == c2 for k in range(16)):
                _st114.append((0, c2, d + 1, tuple(hits)))
            x, y, d = 0, c1, d + 1
            continue
        x, y, d = y, _rq3.children(x, y, 16)[0], d + 1
ok114 &= len(_per114) == 16
ok114 &= all(len([h for h in hs if h >= 0]) <= 1 for hs in _per114)
ok114 &= sum(1 for hs in _per114 if 725146 in hs) == 2
check('S114 GC327: the four-edge block debt 2q - 6 (tie at q = 4) and allowance 3q - 7, sum 6Q - 7j - 5 <= 6Q, debt '
      'subadditive over blocks; on the actual period-16 tree each history starts the burst at most once (two share the '
      'start at 725,146), the second pulse having predecessor 64639', ok114)
ok115 = True


def _rd115(w, T, q):
    return 0 if w == 0 else next(i + 1 for i in range(q) if (w >> ((T + i) % q)) & 1)


def _debt115(costs):
    z, lo, best = [0], 0, 0
    for c in costs:
        z.append(z[-1] + 2 * c - 5)
    for v in z:
        best = max(best, v - lo)
        lo = min(lo, v)
    return z, best


# GC334: for every q = 4 .. 32 and 1 <= r <= q - 2, from (A, B) = (e_0 + e_r, e_0) the children are
# C = 1 + e_1 + .. + e_r, E = 1 + e_1 + .. + e_(r+1), F = e_(r+2); from phase 1 the delays are q, r + 1, 1, q; the doubled
# adjusted prefixes are 0, 2q - 5, 2q + 2r - 8, 2q + 2r - 11, 4q + 2r - 16, and for q >= 8 the debt is 2q + r - 8
_n115 = 0
for q in range(4, 33):
    full = (1 << q) - 1
    e = lambda i: 1 << (i % q)
    for r in range(1, q - 1):
        A, B = e(0) | e(r), e(0)
        C = full ^ sum(e(i) for i in range(1, r + 1))
        E = full ^ sum(e(i) for i in range(1, r + 2))
        F = e(r + 2)
        ok115 &= _rq3.children(A, B, q) == [C] and _rq3.children(B, C, q) == [E] and _rq3.children(C, E, q) == [F]
        T, ds = 1, []
        for w in (B, C, E, F):
            dl = _rd115(w, T, q)
            ds.append(dl)
            T += dl
        ok115 &= ds == [q, r + 1, 1, q]
        z, D = _debt115(ds)
        ok115 &= z == [0, 2 * q - 5, 2 * q + 2 * r - 8, 2 * q + 2 * r - 11, 4 * q + 2 * r - 16]
        if q >= 8:
            ok115 &= D == 4 * q + 2 * r - 16
        _n115 += 1
ok115 &= _n115 == sum(q - 2 for q in range(4, 33))
# q = 4: r = 2 has debt 2 (allowance 5); r = 1 has prefixes 0, 3/2, 1, -1/2, 1, debt 3/2 (not the endpoint 1), allowance 9/2
ok115 &= _debt115([4, 3, 1, 4]) == ([0, 3, 4, 1, 4], 4) and 4 + 2 * 3 == 10
ok115 &= _debt115([4, 2, 1, 4]) == ([0, 3, 2, -1, 2], 3) and 3 + 2 * 3 == 9
# the q = 4, r = 1 exclusion: after three transitions (E, F) = (e_0 + e_3, e_3), a rotation of (A, B) = (e_0 + e_1, e_0)
ok115 &= any((_rq3.rot(0b0011, k, 4), _rq3.rot(0b0001, k, 4)) == (0b1001, 0b1000) for k in range(4))
# q >= 8, r = q - 3: the ending pair (E, F) = (e_0 + e_(q-1), e_(q-1)) starts the r = 1 class (rotated by q - 1)
for q in range(8, 33):
    full = (1 << q) - 1
    E = full ^ sum(1 << i for i in range(1, q - 1))
    F = 1 << (q - 1)
    ok115 &= (E, F) == ((1 << (q - 1)) | 1, 1 << (q - 1))
    ok115 &= (E, F) == (_rq3.rot(0b11, 1, q), _rq3.rot(0b1, 1, q))
# r = q - 1: C = e_0, then the child is 0, then the odd source e_0 has no q-periodic child
for q in range(4, 33):
    full = (1 << q) - 1
    C = full ^ sum(1 << i for i in range(1, q))
    ok115 &= C == 1 and _rq3.children(1 | (1 << (q - 1)), 1, q) == [C]
    ok115 &= _rq3.children(1, C, q) == [0] and _rq3.children(C, 0, q) == []
check('S115 GC334: for every q = 4..32 and 1 <= r <= q - 2 the children C, E, F and delays q, r + 1, 1, q hold, prefixes '
      'and debt 2q + r - 8 (q >= 8); q = 4 controls (debt 2; r = 1 debt 3/2 not 1); the q = 4, r = 1 rotation exclusion; '
      'r = q - 3 ends at an r = 1 start; r = q - 1 exits', ok115)
ok116 = True


def _start116(x, y, q):
    """A named start (e_s + e_(s+r), e_s), 1 <= r <= q - 1: a two-black predecessor whose bit at the singleton driver
    is set."""
    return bin(y).count('1') == 1 and bin(x).count('1') == 2 and (x & y) == y


# GC335's internal-start classification: inside the r-window (A, B, C, E, F), the pairs (B, C), (C, E), (E, F) are named
# starts exactly for (C, E) at r = q - 2 (the terminal separation q - 1) and (E, F) at r = q - 3 (separation 1)
for q in range(4, 33):
    full = (1 << q) - 1
    e = lambda i: 1 << (i % q)
    for r in range(1, q - 1):
        A, B = e(0) | e(r), e(0)
        C = full ^ sum(e(i) for i in range(1, r + 1))
        E = full ^ sum(e(i) for i in range(1, r + 2))
        F = e(r + 2)
        ok116 &= not _start116(B, C, q)
        ok116 &= _start116(C, E, q) == (r == q - 2)
        ok116 &= _start116(E, F, q) == (r == q - 3)
        if r == q - 2:
            ok116 &= (C, E) == (e(0) | e(q - 1), e(0))                   # separation q - 1, the terminal start
        if r == q - 3:
            ok116 &= (E, F) == (e(q - 1) | e(0), e(q - 1))               # separation 1, pulse at q - 1
# the joined r = q - 3 window, q = 8 .. 32, from the actual child map: seven drivers with delays q, q-2, 1, q, 2, 1, q from
# phase 1, doubled prefixes ending at 8q - 31, debt 4q - 31/2, one-transfer allowance 5q - 33/2, saving 2q - 7/2 against
# the separate 7q - 20
for q in range(8, 33):
    full = (1 << q) - 1
    x, y = (1 | (1 << (q - 3))), 1
    drivers = []
    for _ in range(7):
        drivers.append(y)
        c = _rq3.children(x, y, q)
        ok116 &= len(c) == 1
        x, y = y, c[0]
    T, ds = 1, []
    for w in drivers:
        dl = _rd115(w, T, q)
        ds.append(dl)
        T += dl
    ok116 &= ds == [q, q - 2, 1, q, 2, 1, q]
    z, D = _debt115(ds)
    ok116 &= z[-1] == 8 * q - 31 and D == 8 * q - 31 and min(z) == 0
    ok116 &= 2 * (4 * q - 12 + 3 * q - 8) - (D + 2 * (q - 1)) == 4 * q - 7          # saving 2q - 7/2, doubled
    ok116 &= D + 2 * (q - 1) > 2 * (3 * q - 8)                                       # 5q - 33/2 > 3q - 8
# containment: the terminal window alone has delays q, q from phase 1, debt 2q - 5, allowance 3q - 6, below the
# containing r = q - 2 window's 4q - 11 for q >= 8; at q = 4 the group needs 6 (r = 2 has 5, terminal alone 6)
for q in range(4, 33):
    x, y = (1 | (1 << (q - 1))), 1
    c1 = _rq3.children(x, y, q)
    ok116 &= c1 == [1] and _rq3.children(y, 1, q) == [0]
    T, ds = 1, []
    for w in (1, 1):
        dl = _rd115(w, T, q)
        ds.append(dl)
        T += dl
    z, D = _debt115(ds)
    ok116 &= ds == [q, q] and D == 4 * q - 10
    if q >= 8:
        ok116 &= 3 * q - 6 < 4 * q - 11
ok116 &= max(5, 3 * 4 - 6) == 6
check('S116 GC335: internal named starts occur only at r = q - 2 (terminal) and r = q - 3 (separation 1); the joined '
      'r = q - 3 window has delays q, q-2, 1, q, 2, 1, q, debt 4q - 31/2, allowance 5q - 33/2 (saving 2q - 7/2); the '
      'terminal window (debt 2q - 5) is covered; q = 4 group 6', ok116)
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
