# The black frontier of a Q01GapCore survivor recedes at the language's entropy

Local, L1673, 14 November 2026, at the owner's request ("Proceed on the rule 30 side, the branch counts of a
Q01GapCore survivor"). It follows [the 14 November portal update](LOCAL-PORTAL-KIT-UPDATE-20261114.md), section 2.1.

**Status.**
- The two logical remarks in section 2 are hand arguments of a few lines: PROOF-SKETCH, Local.
- Every table is COMPUTED by exhaustive enumeration with exact integers. The comparisons with the counting
  heuristic are MEASURED.
- Nothing here proves or refutes `Q01GapCore`.

## 1. Summary

1. **Quint's branch counts are the gap language's word counts.** The 5 and 11 branches of G.P.J.W. Quint and
   Gemini (kit `Rule30GateTrapLift`, R30-20261113-084253, and PR #348) are the admissible free-bit words of
   lengths 16 and 24 that start at a pulse. In general they grow like 2^(hk), with h = 0.127 bit per free step:
   the entropy of the gap language, which our record measured on the right side in L1610.
2. **Quint's black frontier does not persist.** At k = 16 and k = 24 every admissible row has a black cell within
   the last three or four depths it fixes. At k = 28 a row with six white cells at the end already appears. At
   k = 160 the longest white tail is 18.
3. **The deepest cells behave like fair coins.** Over the admissible words of length k, the length of the white
   tail is geometric with ratio 1/2: at k = 160, 50.1%, 25.0%, 12.5%, 6.3%, … of the 1,702,844 words have tails
   0, 1, 2, 3, …. The share with a black cell in the last three depths is 0.8751, against 7/8. The first check,
   the deepest cell, is white for 0.4992 of them; this is the language-conditioned twin of the kit's
   `first_check_balanced`.
4. **Survival therefore follows the counting heuristic.**
   - The longest-lived finite row of support at most W keeps admissible free bits for about W/(2 − h) steps:
     159 steps at W = 300, where 300/1.873 = 160.
   - Beyond its support a row survives each step with probability 0.2736, against λ/4 = 0.2730, where
     λ = 2^h. The factor 1/2 is the check; λ/2 is the language accepting the forced bit.
5. **Consequence.** The pulse-skeleton route cannot prove `Q01GapCore` by a bounded frontier law. A frontier of
   width at most 17 is refuted by explicit words, and the data say the width grows like hk. A survivor would be a
   single orbit beating a hazard of about 0.73 a step forever. That is the original single-orbit problem in a
   thinner language, just as Q01 itself has a hazard of 1/2 a check.

## 2. The objects and two remarks

All definitions are from kit main `268488d6`.
- **The dynamics.** `zrow L (t+1) d = zrow L t (d+1) xor (zrow L t d || zrow L t (d−1))`, with depth 0 white.
- **`InX`.** Depth 1 is black at every even step.
- **Free bits and gaps.** The free bits are f(s) = `zrow L (2s+1) 1`, and Theta f is the constrained row with
  those free bits. The gap sequence is g = ¬f.
- **`TwoWordsOK`.** Gaps are 3 or 5, with no 33 and no 3553.
- **`TwoCoreOK`.** The same, with 3535353 also forbidden. `Q01TwoCore ↔ Q01GapCore` (`Q01TwoCore_iff_Q01GapCore`).

**Anti-diagonals.** k free bits fix depths 1 to 2k+1 of Theta f. If D_n holds the cells z(τ, n−τ), then the
depth-1 value at tick n is the deepest cell xor the OR-terms of the two previous anti-diagonals. So

    row[n+1] = c(n) xor parity((D_n | D_(n−1)) on n bits),     D_(n+1) = prefix-xor(row[n+1], X << 1).

The odd depths 2k+2 carry the new free bit; the depth 2k+1 is determined, and it is the kit's first check
(`check n l = Theta (word l) (2n+1)`).

**Remark A (a bounded frontier would settle the question).** Suppose that for some c and every k, every
admissible word's (2k+1)-prefix has a black cell in its last c depths. A survivor of `Q01TwoCore` has a pulse b
after its threshold, and its row at tick 2b is Theta of its admissible future. That row would then have black
cells at unbounded depth. But `zrow_fin` bounds its support by W + 2b. So `Q01TwoCore` would hold.

**Remark B (but the frontier is the problem itself).** Let m(k) be the least last-black depth over admissible
k-words. Then m(k) ≤ W exactly when some row of support at most W keeps admissible free bits for k steps from a
pulse. The prefix is the row itself, and its first 2k+1 depth-1 values depend only on depths up to 2k+1. So
m(k) → ∞ is `Q01TwoCore` in its pulse-anchored form. Branch counts alone cannot decide it: it is a statement about
single orbits, and the counts can only say how unlikely a survivor is.

## 3. Results (COMPUTED; `TwoCoreOK` unless stated)

| k | B(k) | m(k) | T(k) = 2k + 1 − m(k) | share with a black cell in the last 3 depths | white first checks |
|---|---|---|---|---|---|
| 8 | 2 | 16 | 1 | 1 | 0.500 |
| 16 | 5 | 32 | 1 | 1 | 0.400 |
| 24 | 11 | 46 | 3 | 0.909 | 0.455 |
| 28 | 15 | 51 | **6** | 0.867 | 0.533 |
| 40 | 46 | 77 | 4 | 0.804 | 0.543 |
| 60 | 256 | 114 | 7 | 0.875 | 0.481 |
| 80 | 1,441 | 151 | 10 | 0.865 | 0.518 |
| 100 | 8,475 | 189 | 12 | 0.880 | 0.499 |
| 120 | 50,604 | 224 | 17 | 0.875 | 0.503 |
| 140 | 296,223 | 263 | 18 | 0.875 | 0.501 |
| 160 | 1,702,844 | 303 | 18 | 0.8751 | 0.4992 |

- **Growth.** The 30-step geometric mean of B(k+1)/B(k) at k = 160 is 1.09159, against 2^0.12707 = 1.09207.
  The one-step ratio oscillates between 1.04 and 1.16 with the gap structure.
- **The first k with T(k) ≥ c**, for c = 4, 6, 10, 14, 18, 22, is 22, 28, 48, 96, 114, 139.
- **`TwoWordsOK`.** The tables are the same to k = 24, and the frontier behaves the same way: T(140) = 18,
  B(140) = 465,919, and the white-check share is 0.5012.
- **The tail histogram at k = 160** (tail length: words):

  0: 852,771; 1: 425,072; 2: 212,247; 3: 106,647; 4: 53,169; 5: 26,622; 6: 13,377; 7: 6,498; 8: 3,138; 9: 1,785;
  10: 764; 11: 335; 12: 197; 13: 108; 14: 61; 15: 25; 16: 8; 17: 10; 18: 10.

  The successive ratios are 0.498, 0.499, 0.502, 0.499, 0.501, 0.502, 0.486, …. A longest tail of about
  log_2 B(k) ≈ hk is what B(k) fair coins would give.
- **The survival record S(W)**, the largest k with an admissible row of support at most W:

  | W | 20 | 40 | 60 | 100 | 140 | 200 | 260 | 300 |
  |---|---|---|---|---|---|---|---|---|
  | S(W) | 10 | 22 | 32 | 54 | 73 | 105 | 139 | 159 |

  W/S(W) tends to about 1.89, against 2 − h = 1.873.
- **The champion** at k = 160 has support 303. Its free bits are mostly gaps of 5 with isolated 3s, and it
  passes the forward check.

## 4. Controls and predictions

**Controls**, all PASS.
- **C1.** Forward evolution of every sampled prefix reproduces its free bits: ticks 0 to 2k, for k ≤ 30, in both
  languages and without a language.
- **C2.** Quint's 16-depth skeleton holds for every `TwoWordsOK` word with 8 ≤ k ≤ 25: L1..16 =
  1100011, ¬f3, 1011111, f3, of weight 11.
- **C3.** B(16) = 5 and B(24) = 11. Depths 20 and 21 are white, with depth 29 or 32 black and weight(1..32) ≥ 18
  (k = 16); one of depths 46, 47, 48 is black (k = 24). Known (Quint and Gemini, Lean), reproduced here
  computationally.
- **C4.** For Q01 without a language, m(k) for k = 1 to 19 is 2, 2, 5, 6, 7, 9, 9, 9, 11 (k = 9 to 14), 14,
  19, 19, 19, 22. This equals our own survival record: `sepgap/death_pairs.out` (L1595) to width 22, and this
  probe's own forward walk to width 16.

**Predictions** (L1673, pushed before the code existed).

| | Prediction | Outcome |
|---|---|---|
| P2 (0.85) | one-step ratio B(k+1)/B(k) within 0.002 of 1.0921 for k ≥ 80 | **REFUTED** as written: the one-step ratio oscillates (1.039 to 1.158). The 30-step mean is 1.0916 |
| P3 (0.65) | the frontier recedes: T(k) ≥ 6 by k = 120, T/k between 0.06 and 0.2 at the end | **HELD**: first at k = 28; T(160)/160 = 0.113 |
| P4 (0.6) | white first-check share within 0.06 of 1/2 for 60 ≤ k ≤ K | **HELD**: 0.454 to 0.547, and 0.4992 at k = 160 |
| P5 (0.5) | per-step decay beyond the support within 0.05 of λ/4 | **HELD**: median 0.2736, against 0.2730 |

P2 failed for a reason I should have seen: a language with gaps of 3 and 5 grows in steps. Its entropy is a limit
of geometric means, not of one-step ratios.

## 5. What this says about the period-2 gate

- **The route closes in its bounded form.** A frontier law "a black cell within c of the end, for every depth"
  would have proved `Q01GapCore`. It fails for every c ≤ 17, by explicit words found here. The fair-coin tail
  says the width grows like log_2 of the branch count, about 0.127 depth per free step, with no bound. A proof
  along these lines would need a frontier that grows with a strictly sublinear shortfall *and* an argument that a
  single orbit cannot keep up. That is the original problem.
- **What survives is a law.** The frontier bits of Theta over the admissible language are equidistributed: tails
  geometric(1/2) and the first check balanced. This is the Rule 30 counterpart of the equidistribution of valid
  starts proved for Mahler's map this week (L1670, carried by GPT in GC2940). A theorem of that kind here, for
  example that the white first-check share over admissible k-words tends to 1/2, is open. It would be the
  language-conditioned strengthening of `first_check_balanced`. It would give densities, not extinction.
- **Next, if wanted.**
  - (a) Read the kit's proof of `first_check_balanced` and see whether it survives conditioning on a sofic
    language.
  - (b) Ask the same question for `Rule30PeriodTwoWidth13`'s GE2 language (PR #349), whose mass ladder is the
    other side of the same gate.

## 6. Receipts

- **Probe:** [`local_q01core_frontier.py`](../tests/probes/sepgap/local_q01core_frontier.py), SHA256 `70857f28…`.
  It was frozen at `0f22cfb78` after L1673's predictions (`f3ef8bf13`); only the arithmetic kernel was timed
  beforehand, on random inputs.
- **Run 14:** COMPLETED in 60 s, peak RSS 19 MiB. Caps: CPU 900 s, wall 1500 s, RSS 4096 MiB; one Python
  process. The enumeration was complete to k = 140 (`TwoWordsOK`, 5.3·10^6 nodes) and k = 160 (`TwoCoreOK`,
  2.0·10^7 nodes).
- **Output:** [`local_q01core_frontier.out`](../tests/probes/sepgap/local_q01core_frontier.out), `f3e530f9…`.
- **Record searched:** as in L1673. Our record has the right-side trap language (L1608 to L1612, GC2794, GC2797)
  and the Q01 survival by width (`sepgap`, L1595). The kit and portal have Quint's skeleton to depth 48 and
  Cloud's `first_check_balanced`. None measures the left-side frontier beyond depth 48. No novelty is claimed
  for the heuristic, which is the standard first-moment count.
