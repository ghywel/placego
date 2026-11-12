# The unconditional first check tends to 1/2: a Riesz product and a run lemma

Local, L1669, 12 November 2026. A sequel to
[the arc certificate](LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md), whose section 11 guessed at a Fourier reading.
This report tests that reading, finds it exact, and turns it into a proof.

**Status.** Theorem C is **PROOF-SKETCH, Local**: a hand proof, each step checked numerically, awaiting a
carrying read. The explicit constants are **COMPUTED**, by an exhaustive pruned search replayed in Wolfram up to
k = 64, and rest on steps 3 and 4 of the proof. Section 5 is a plan for the valid words with one unproved lemma;
it is **OPEN**, with first evidence. Nothing here proves Mahler's conjecture.

## 1. Summary

1. **Theorem C.** Among all n < 2^w, the share with T^w(n) odd tends to 1/2. GC2936 §2 called 1/2 "the observed
   limit" and proved 1/4 and 3/4.
2. **Explicitly.** The share is within 0.0187 of 1/2 for every w ≥ 64, within 0.0099 for w ≥ 72, and within 0.0054
   for w ≥ 80. The same holds after every prefix, for the 2^k continuations with k in place of w.
3. **How.** The Fourier transform of the set {n : T^w(n) odd} is a product of cosines along the orbit
   y → 3y/2, with one branch bit per step. Two small angles in a row force growth by exactly 3/2, and no angle
   is below 2^(−(u+2)), so no orbit stays small.
4. **The proved rate is poor** (a power of w below 1/4); the searched products carry the numbers. Their decay
   comes in drops and plateaus, not at a steady factor, and my prediction of a steady factor was refuted.
5. **The valid words.** The same route gives D_m/B_m → 1/2 if one lemma holds: a non-small angle shrinks the
   sum over valid words by a fixed factor. For all words that is the cosine itself. For valid words a first
   table agrees with it; the lemma is not proved.

## 2. Theorem C

T(n) = ceil(3n/2), O_w = #{n < 2^w : T^w(n) odd}, M = 2^(w+1). For an integer n put

    y_u(n) = n·3^u / 2^(u+2)  mod 1,     ρ_w(n) = Π_(u<w) |cos(π y_u(n))|,     ρ*_w = max over odd n of ρ_w(n).

‖y‖ is the distance from y to the nearest integer.

**Theorem C (Local; PROOF-SKETCH).** For every w ≥ 2 and every real H with 2 ≤ H,

    |O_w/2^w − 1/2|  ≤  ρ*_w (1 + ½ ln H) + 1/√(2(H − 1)),

ρ*_w does not increase with w, and ρ*_w ≤ cos(π/5)^N(w), where N(w) is the number of terms below w of the
sequence u_1 = 0, u_(r+1) = the largest integer below u_r + 2 + log_1.5(2^(u_r+3)/5): 0, 3, 11, 32, 89, …. So
N(w) ≥ log_2.71(w) − 2 and O_w/2^w → 1/2.

The same bound, with k for w, holds for the share of forced parity 1 among the 2^k continuations of any
prefix: by the arc statement that share is the number of points of θ·Y_k in a half circle, and the proof
below does not care which half circle or which odd θ.

*Proof.*

1. **The points.** Let Y_w = {n mod M : T^w(n) odd}. From 2^K T^K(n) = 3^K n + C, the residue with first w
   parities s and next parity 1 is y(s) ≡ −3^(−w) C(s) + 2^w (mod M), with C(s) = Σ_(i<w) s_i 2^i 3^(w−1−i).
   Every word s occurs once.
2. **The transform is a product.** Σ_s e(−h·y(s)/M) = ±Π_(i<w) (1 + e(h·3^(−w)·2^i·3^(w−1−i)/M)), because the
   sum runs over all 2^w words. Since |1 + e(φ)| = 2|cos(πφ)| and 2^i 3^(w−1−i)/M = 3^u/2^(u+2) at u = w − 1 − i,
   its modulus is 2^w ρ_w(n_h) with n_h = h·3^(−w) mod M.
3. **The count.** O_w is the number of points of Y_w in [0, 2^w). The indicator of that half circle has
   transform 0 at even h ≠ 0 and of modulus 1/|sin(πh/M)| at odd h. With |sin(πh/M)| ≥ 2|h|/M for |h| ≤ M/2,
   and ρ_w(−n) = ρ_w(n),

       |O_w/2^w − 1/2|  ≤  Σ over odd h with 0 < h < M/2 of ρ_w(n_h)/h.

4. **Split at H.** The terms with h ≤ H are at most ρ*_w Σ_(odd h ≤ H) 1/h ≤ ρ*_w (1 + ½ ln H). By Parseval the
   sum of ρ_w(n_h)² over all h modulo M is M·2^w/4^w = 2, so over odd h > 0 it is at most 1, and by
   Cauchy–Schwarz the terms with h > H are at most (Σ_(odd h > H) h^(−2))^(1/2) ≤ 1/√(2(H − 1)).
5. **The run lemma.** For odd n, n·3^u is odd, so ‖y_u‖ ≥ 2^(−(u+2)). Also 2 y_(u+1) ≡ 3 y_u (mod 1). If
   ‖y_u‖ < 1/5 and ‖y_(u+1)‖ < 1/5, write them as signed distances η, η′; then 2η′ − 3η is an integer of
   absolute value below 1, so 2η′ = 3η and ‖y_(u+1)‖ = (3/2)‖y_u‖. Hence a run of consecutive indices a, …, b
   with ‖y_u‖ < 1/5 has (3/2)^(b−a) 2^(−(a+2)) < 1/5. Index 0 is not in a run, since ‖y_0‖ = 1/4. So if
   u_1 = 0 < u_2 < … are the indices with ‖y_u‖ ≥ 1/5, then u_(r+1) < u_r + 2 + log_1.5(2^(u_r+3)/5). Each
   such index contributes a factor at most cos(π/5).
6. **Monotone.** ρ_(w+1)(n) = ρ_w(n mod 2^(w+1))·|cos(π y_w(n))| ≤ ρ*_w. ∎

Taking H = w² + 1 gives |O_w/2^w − 1/2| ≤ ρ*_w (1 + ln(w + 1)) + 1/w. With ρ*_w ≤ (w/2)^(−0.21) this tends to 0,
and it first falls below 1/2 somewhere between w = 10^6 and w = 10^9. This is Kershner's kind of argument for the Bernoulli convolution of
ratio 2/3, with a branch bit added; I know his paper from surveys only and make no claim about what it contains.

## 3. Explicit bounds (COMPUTED)

ρ*_k is a maximum over 2^k residues. The factor at index u depends on n modulo 2^(u+2) only, and the partial
product bounds every extension, so a depth-first search over the bits of n, pruned by the best product found,
is exhaustive. Each row gives a bound for every w ≥ k by steps 3, 4 and 6, with H chosen to minimise it.

| k | ρ*_k | nodes searched | \|O_w/2^w − 1/2\| for every w ≥ k |
|---|---|---|---|
| 16 | 0.111298 | 97 | 0.4299 |
| 32 | 0.052264 | 481 | 0.2409 |
| 48 | 0.010441 | 11,807 | 0.0650 |
| 56 | 0.004070 | 77,881 | 0.0292 |
| 64 | 0.002425 | 220,133 | 0.0187 |
| 72 | 0.001174 | 939,940 | 0.0099 |
| 80 | 0.000593 | 3,684,586 | 0.0054 |

For k ≤ 15 the arc certificate is sharper: it gives 0.085 at k = 15, where this gives more than 0.4. The two
meet between k = 40 and k = 48. The average step of ρ*_k from k = 32 to 80 is 0.911. From k = 22 to 28 it does not move
(0.05497 to 0.05486): the best n is riding one long run of small angles.

## 4. Tests

Written before each run (L1669 and its addenda).

| | Claim | Outcome |
|---|---|---|
| R1 (0.9) | the modulus of the transform of Y_w is 2^w ρ_w(h·3^(−w)) at every h, w ≤ 12 | **held**, to 2·10^(−16); Parseval to 7·10^(−16) |
| R2 (0.9) | for 3 ≤ k ≤ 13: √2·max ρ/(M\|sin\|) ≤ certified half-width ≤ the sum of step 3, over every multiplier; the upper bound holds for the true O_w, w ≤ 20 | **held**; at k = 13: 0.0827 ≤ 0.1156 ≤ 0.1245 |
| R3a (0.7) | the certified half-width is 0.3 to 3 times ρ*_k for 8 ≤ k ≤ 15 | **held**: 0.629 to 0.755 |
| R3b (0.7) | ρ*_k falls by a factor between 0.80 and 0.92 a step for 11 ≤ k ≤ 22 | **refuted**: 0.797 to 1.000 |
| R4 (0.95) | the run lemma for every odd n modulo 2^21; ρ*_k ≤ cos(π/5)^N(k) for k ≤ 22 | **held**; least count 4 against a promised 3 |
| (0.6) | the searches at k = 72 and 80 finish under 2·10^7 nodes | **held** |

Run 4 printed all four tests and then stopped on an overflow in its last, informational line; run 5 is the
same file with that line repaired and the explicit bounds added, and it prints the same tables.

So the heuristic of the earlier report's section 11 stands corrected in one respect: the half-width is
governed by the largest product, but that product does not decay at a steady rate.

## 5. The valid words (OPEN; a plan and first evidence)

For the boundary words p of length m the points are y(p) = N_(m+1)(p1), and D_m is their number in [0, 2^m).
Put G(n) = Σ_p Π_(i : p_i = 1) e(y_(m−1−i)(n)), the same sum as in step 2 but over boundary words only, and
γ(n) = |G(n)|/B_m. Step 3 gives |D_m/B_m − 1/2| ≤ Σ over odd h > 0 of γ(n_h)/h, as before.

**The lemma that is missing.** There are C and λ < 1 with γ(n) ≤ C·λ^NS(n) for every m and every odd n, where
NS(n) is the number of u < m with ‖y_u(n)‖ ≥ 1/5.

For all 2^m words it holds with C = 1 and λ = cos(π/5). For valid words the sum is not a product. The natural
proof groups words into fibres: a bit that follows a full prefix and is followed by 00 can be toggled without
changing anything later, and each toggled bit at a non-small angle gives a cosine. That needs a count of how
many words have a toggle at a given place, uniformly, and I have not done it.

**If the lemma holds, D_m/B_m → 1/2** (sketch, not checked line by line):
- above H = (4/3)^m m², Parseval gives Σ_h |G|² = M·B_m, and the terms with h > H are at most about 1/m;
- inside a run the branch bit is forced, so at most 2(4m + 4)^L odd n have NS(n) ≤ L. Each has γ ≤ C λ^N(m), and
  the sum of 1/h over that few frequencies is at most about L ln(4m + 4);
- the remaining frequencies have γ ≤ C λ^L, against a harmonic sum of about 0.15 m;
- take L a large multiple of ln m.

**First evidence** ([`local_conditional_sums.out`](../tests/probes/mahler/local_conditional_sums.out); two
predictions, both held). At m = 18, with B = 1144:

| NS | odd frequencies | largest γ | root mean square γ |
|---|---|---|---|
| 4 | 14 | 0.314 | 0.182 |
| 5 | 156 | 0.372 | 0.155 |
| 7 | 5,184 | 0.266 | 0.071 |
| 9 | 31,610 | 0.217 | 0.037 |
| 12 | 48,642 | 0.128 | 0.020 |
| 15 | 5,940 | 0.121 | 0.015 |
| 18 | 14 | 0.018 | 0.013 |

- K1 (0.6): the largest γ over NS ≥ 9 is at most 0.35. **Held:** 0.217.
- K2 (0.6): the largest γ of all sits within 3 of the least NS. **Held:** at NS = 5, the least being 4.
- The sum of step 3 for the true count falls with m: 0.239, 0.163, 0.128, 0.091 at m = 12, 14, 16, 18.
- At m = 16 the largest γ is at h = 39033, the multiplier at which the arc certificate's least count sat for
  k = 16. The two reports see the same object.

A random set of B points would have γ about 1/√B = 0.030 everywhere; the table's floor is half that. This is a
table at four lengths. It supports the shape of the lemma and proves nothing.

## 6. What carries the proof, for the second read

1. Step 1's formula for y(s), and step 2's passage from a sum over all words to a product.
2. Step 3's constants: the transform of the half circle and the bound 1/(M|sin(πh/M)|) ≤ 1/(2|h|).
3. Step 4's use of Parseval for the odd frequencies only.
4. Step 5: that two consecutive small values force 2η′ = 3η, with the threshold 1/5, and the recursion for
   the non-small indices.
5. Section 3's search: that pruning by the partial product is exhaustive.

## 7. Receipts

Local's M5, `run_capped.py`, one Python process, CPU 600 s, wall 900 s, RSS 4096 MiB. Nothing above 2^23 is
walked.

| Run | Source (SHA256) | Output (SHA256) | Result |
|---|---|---|---|
| 4 | [`local_first_check_riesz.py`](../tests/probes/mahler/local_first_check_riesz.py) at `4e7f0712…` | [`…_run4.out`](../tests/probes/mahler/local_first_check_riesz_run4.out) `b28120c6…` | CHILD_FAILED after the four tests, 3 s |
| 5 | the same file at `d3f4e190…` | [`local_first_check_riesz.out`](../tests/probes/mahler/local_first_check_riesz.out) `d9739544…` | COMPLETED, 5 s |
| 6 | [`local_conditional_sums.py`](../tests/probes/mahler/local_conditional_sums.py) `b92f8abb…` | [`local_conditional_sums.out`](../tests/probes/mahler/local_conditional_sums.out) `aa016054…` | COMPLETED, 1 s |

**Wolfram replay**, own code, same kernel session as the earlier replay: R1 for w ≤ 8 (largest difference
1.5·10^(−14)); ρ*_k by brute force at k = 6, 8, 10, 12, 13; ρ*_k by a pruned search in a different order at
k = 16, 22, 32, 48, 64 (684,073 nodes at 64). Every value equals Python's to the printed digits.
**Python only:** ρ*_72 and ρ*_80, R2, R4 and run 6.

Record searched: as in L1669. record_find for "Riesz product", "Kershner", "Bernoulli convolution",
"Erdős–Turán": Local's own pull of 14 October on the Bernoulli convolution at 2/3, and nothing that states
this limit. Kit and portal: none. No novelty claimed.

## 8. Next

- The carrying read of Theorem C.
- The missing lemma of section 5. It is a statement about the 3/2-shift with phases on the ones, and it is
  where a second mind would help most.
- The same argument with j forced bits should give equidistribution of T^w(n) modulo 2^j over n < 2^w for
  each fixed j: the angles become n·3^u/2^(u+j+1) and Parseval gives 2^j. Not written out and not tested.
