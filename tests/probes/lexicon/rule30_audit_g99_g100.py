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
print('ALL CHECKS PASS' if not fails else 'FAILED: ' + ', '.join(fails))
