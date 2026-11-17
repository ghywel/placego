# From the kit back to Mahler: the dictionary, a transfer table and the first three transfers

Cloud, CL781 and CL782, 11 November 2026. The owner pinned the wall work of CL780 and asked to go back to
Mahler with the methods the Rule 30 kit has gained: "Further working on mahler with these new methods might
yield new information on mahler, which could bear on wolfram in turn." This report is the map and the first
results. It claims nothing about Mahler's conjecture itself.

**GPT carrying review, GC2936 (11 November):** H1–H5 and the two constructions are carried,
with the domain/scope corrections below. [Full read and proposed strengthenings](GPT-MAHLER-TRANSFER-REVIEW-20261111.md).
The new unconditional bound, conditional pairing, odd-weight formulation and stripe recharge
families are GPT sketches awaiting Cloud; the old measurements are not promoted to theorems.

## 1. Summary

1. **The two problems now have the same written shape.** Since 31 October the kit states Rule 30's period 2 as
   an integer iteration (`Q01_iff_integer`): no natural number keeps every iterate of G = F∘F odd, with
   F(Y) = (Y >> 1) xor (Y or 2Y). Mahler's conjecture is: no positive integer keeps the parity word of
   T(n) = n + ceil(n/2) inside the 3/2 beta-shift. Both maps are the Gray code plus a correction
   (COLLATZ-PRIZE.md §8, in the record since 8 October).
2. **Two weeks of kit theorems about F had not been tried on T.** Section 4 lists them against Mahler.
3. **Three transfers are done here.** The first parity past the free bits (five exact identities, and the
   measured share that passes: three quarters). A barrier: no descent by a finite-state statistic of the
   binary digits. A planted survivor: a conjugate of T with an immortal positive integer and the same
   survival table below an explicit threshold, and exactly one extra survivor above it. Predictions were pushed before each run and held, with one indexing slip of mine caught
   by its own check.
4. **The two problems share their witness.** The stripe …010101, which is −1/3 as a 2-adic integer, is the
   immortal point behind the kit's barriers for Rule 30 and behind the same barriers for Mahler.
5. **Differences that matter.** Mahler's first check looks fair; Rule 30's is provably unbalanced at odd
   lengths. T is injective on the integers, so Mahler has no twins. Mahler's inverse chart has an explicit weighted-sum formula, but it is not affine
   for either ordinary binary addition or the pointwise XOR used by the kit's `LinearCharts`.

## 2. Record searched

MAHLER.md whole: its honest summary, sections 1 to 4, GC2342 ("Rule 30 to Mahler: episodes and recharge",
1 November) with its durable queue, and the plateau series to GC2507 by title. COLLATZ-PRIZE.md §4 (the
least-residue lemma), §8 (the Gray-code identity), §9 (the carry dial) and proofs/G266. PRIZE-PROBLEMS.md's
summary. The kit's catalogue at its main of 12 November (17fcf59, 266 modules), read from a clone, with the
rows named in section 4. record_find for "Gray code" and "first check". Not searched: open kit pull requests
(my index refresh fails on them, HTTP 403) and the wider literature on the first determined parity, so no
novelty is claimed for sections 5 to 7.

What the search changed: the linear relatives are already done (G266 and the carry dial), so they are not
repeated; the least-residue form of the state after the free bits is the record's own lemma for Collatz and
is only restated for Mahler's map; GC2342 is a first barrier of the valuation-clock kind and section 6 is the
finite-state kind beside it.

## 3. The dictionary

| | Rule 30, period 2 | Mahler |
|---|---|---|
| Map on natural numbers | F(Y) = (Y >> 1) xor (Y or 2Y); G = F∘F | T(n) = n + ceil(n/2) = (3n + b)/2, b = n mod 2 |
| Shared linear part | the Gray code Y xor (Y >> 1) | the Gray code n xor (n >> 1) |
| Correction | local, one cell | a carry, of any length |
| Observed bit | bit 0 of each G-iterate | bit 0 of each T-iterate |
| Immortal | every G-iterate odd | every tail of the parity word below 1/2 |
| Open statement | no natural number is immortal (`Q01`) | no positive integer is immortal |
| Chart to a shift | free bits (`Theta`, `fb`); not linear from depth 7 | the code map; start = −Σ b_k 2^k/3^(k+1) |
| Free range | `count_constrained` | A(T) = 2, 3, 5, 8, 12, 18, 27, 40, 60, 90, … |
| Bounded ranges | `Q01_iff_bounded`, `mortality_iff_Q01` | GC664 |
| Immortal 2-adic points off the natural numbers | the stripe −1/3, fixed by F; three eventually periodic rows (`UnrestrictedClosing`) | −1/3 (word 1000…), −9/19 (word (100)^∞), the rung points |
| Growth of a row | one cell a step | a factor 3/2 a step |
| Injective on finite rows | no (`LateTwins`) | yes |

## 4. The transfer table

| Kit module | What it proves for F | Mahler counterpart | State |
|---|---|---|---|
| `Rule30FirstChecks`, `Rule30FirstCheckDegree` | the first check past the free range: exact pair counts, share between 1/40 and 39/40 for two of any three lengths, exact degree, `ones n ≡ n` | the first parity past the free bits | **done here, section 5** |
| `Rule30ZeroBoundaryBarriers`, `Rule30RecognizableBarrier` | no ranking through a finite abstraction, a local window, an edge automaton, a recognizable statistic | the same for T | **done here, section 6** |
| `Rule30PlantedSurvivor` | a conjugate map with an immortal finite row, identical finite tables below a threshold and one extra survivor above | the same for T | **done here, section 7** |
| `Rule30HybridWall`, `Rule30WallDeadlines` | linear relatives solved exactly | the carry dial at 0 and 1 | in the record (G266) |
| `Rule30FrontierChart`, `Q01_iff_bounded` | mortality, budgets and Q01 are one statement | GC664 | in the record |
| `Rule30LinearCharts` | every linear chart is the free-bit chart | explicit weighted-sum inverse; not affine for binary XOR | analogous rigidity is not disposed of by the formula (GC2936) |
| `Rule30LateTwins` | every late row has a twin; reset words of the backward transducer | none: T is injective on the integers | differs |
| `Rule30PeriodTwoMass` | Conjecture S, 7·A ≥ H + 4, with A the seed population, sharp on truncations of 2538/127 | a horizon-versus-weight question for odd starts | open; the census coin law concerns bit length, not population (GC2936) |
| `Rule30ZeroBoundaryStripe*` | long survivors lie on rays from the stripe | long survivors near −1/3 and −9/19 | partly in the record (rung-pure records); open |
| `Rule30DrivenLeftWindows`, `jen_clock` | window bounds for periodic agreement | the valuation clocks, W1 to W3 | in the record |
| `Rule30FreeMiddle`, `Rule30PeriodTwoNoFloor`, `Rule30UnrestrictedClosing` | three further negative results on ranks, floors and closing | not yet stated for T | open, low priority |
| `Rule30SeparatorQ01` | hard-core endpoint: free bits with no two adjacent whites | "every orbit visits 3 mod 4" (no 11 in the word) | in the record as the weaker conjecture |

## 5. Transfer 1: the first parity past the free bits

For 0 ≤ n < 2^w the first w parities of n are free: each word of length w belongs to one n (G51). Write
χ_w(n) = T^w(n) mod 2, the first parity that n itself decides. Take w ≥ 1 and set χ_0(0) = 0. A word is valid while every tail of its
zero-padded code is below 1/2; A(w) counts the valid words of length w.

**Five identities (Cloud; PROVED, two-party with GPT GC2936, at the displayed scopes; each replayed exhaustively).**

- *H1, complement.* χ_w(2^w − 1 − n) = χ_w(n).
  Proof. T(−1 − x) = −1 − T(x) for every integer x, by cases on the parity of x. And
  T^w(x + 2^w m) = T^w(x) + 3^w m, since adding 2^w leaves the first w parities alone. So
  T^w(2^w − 1 − n) = 3^w − 1 − T^w(n), and 3^w − 1 is even. Hence the number of n < 2^w with χ = 1 is even.
- *H2, the shift rule.* Write T(n) = q·2^(w−1) + r with r < 2^(w−1). Then q ≤ 2 and
  χ_w(n) = χ_(w−1)(r) xor (q mod 2).
  Proof. T(n) ≤ 3·2^(w−1) − 1, and T^(w−1)(q·2^(w−1) + r) = 3^(w−1) q + T^(w−1)(r).
  So the check differs from the check of the shifted word exactly when T(n) lies in [2^(w−1), 2^w), the
  middle third. That happens for exactly floor((2^(w+1) − 2)/3) − floor((2^w − 2)/3) of the n < 2^w.
- *H3, the state after the free bits.* T^w(n) is the least nonnegative residue of C·2^(−w) modulo 3^w, with
  C = Σ_(k<w) b_k 2^k 3^(w−1−k).
  Proof. 2^w T^w(n) = 3^w n + C by induction on 2T(x) = 3x + b, and 0 ≤ T^w(n) ≤ 3^w − 1 because T is
  increasing and T^w(2^w − 1) = 3^w − 1 by H1. This is COLLATZ-PRIZE.md §4's lemma for a map whose every step
  multiplies by 3. So χ is the parity of a least residue modulo a power of 3.
- *H4, a floor.* Among the valid n < 2^w, at least A(w+1) − A(w) pass the first check.
  Proof. A word that may take a 1 may take a 0, so its n passes whatever χ is, and there are
  A(w+1) − A(w) such words. The share is at least A(w+1)/A(w) − 1, which tends to one half.
- *H5, the last-bit rule.* If p has length w − 1 and e = χ_(w−1)(p), the two extensions of p satisfy
  χ_w(p0) xor χ_w(p1) = e xor [w even]. Here p0 and p1 are parity-word extensions, not ordinary binary concatenations; their representatives can occur in either order.
  Proof. The extensions are r and r + 2^(w−1). Their (w−1)-th iterates are m and m + 3^(w−1), of parities
  e and 1 − e, so their w-th iterates differ by (3^w + 1 − 2e)/2, and (3^w + 1)/2 is odd exactly at even w.

**Measured (`tests/probes/mahler/cloud_mahler_first_check.py`, every n < 2^w, w ≤ 26, 92 s).** "Boundary"
means a valid word that cannot take a 1; only those can die at the first check.

| w | valid A(w) | χ = 1, all n | boundary words | of them χ = 1 | pass share | floor of H4 | second check pass share |
|---|---|---|---|---|---|---|---|
| 10 | 90 | 0.5098 | 46 | 0.5652 | 0.7111 | 0.4889 | 0.7500 |
| 14 | 452 | 0.4911 | 226 | 0.4956 | 0.7522 | 0.5000 | 0.7500 |
| 18 | 2,291 | 0.4996 | 1,144 | 0.4904 | 0.7551 | 0.5007 | 0.7491 |
| 22 | 11,606 | 0.5000 | 5,804 | 0.5038 | 0.7481 | 0.4999 | 0.7512 |
| 26 | 58,750 | 0.5000 | 29,377 | 0.5023 | 0.7488 | not computed | 0.7502 |

Predictions (CL781, pushed first) and outcomes:

- MF1, the control: A(1..10) equals the census's table. Held.
- MF2 (0.95): H1 and H2 at every n for w ≤ 22, H3 for w ≤ 18, H4 at every w. Held.
- MF3 (0.8): over all n the share with χ = 1 is within 0.02 of one half from w = 12. Held. The exact excess
  over one half is 0, −2, −2, −6, −2, −2, −2, 14, 10, 2, −2, −30, −146, −94, −174, −74, −102, −94, −78 for
  w = 2 to 20, far below the square root of 2^w.
- MF4 (0.7): boundary share within 0.05 of one half and pass share within 0.03 of 3/4 from w = 16. Held
  (0.481 to 0.516, and 0.742 to 0.759).
- MF5 (0.6): the second check's pass share within 0.03 of 3/4. Held (0.746 to 0.759).
- No parity law appears on the valid words: the parities of their χ-count and of the deaths are irregular.

**Reading.** Rule 30's first check has exact pair counts, degree exactly n or n − 1, the parity law
`ones n ≡ n`, proved non-balance at odd n, and only the proved bounds 1/40 and 39/40. Mahler's has H1 to H5 by
one-line arithmetic, is complement-invariant, and is fair as far as measured: approximately three quarters pass in the measured range, a lower bound tending to
one half is proved, and over all n the check is balanced to within a hundred in a million at w = 20. What is missing
on the Mahler side is the twin of `first_check_balanced`, a proved two-sided bound on the boundary share.
H2 and H5 are the tools for it: the middle-third rule says how the check moves when the word is shifted, the
last-bit rule how it moves when the last bit is flipped.

## 6. Transfer 2: no descent through a finite-state statistic

**Statement (Cloud; PROVED, two-party with GPT GC2936; twin of `Rule30RecognizableBarrier.no_recognizable_ranking`).** Fix a
finite monoid, a morphism μ from binary words into it, and a window size K. There is no function ρ of
(bit length of n, μ of the binary digits of n read from the top, the top K digits, the bottom K digits) into
a well-founded order that falls at every step n ↦ T(n) taken while the parity word of the start is valid.
Reading the digits from the bottom gives the same statement for the opposite monoid.

**Proof.** Let t_L = (4^L − 1)/3, the first 2L bits of the stripe. T(t_L) = 2^(2L−1), and then each step
turns a factor 2 into a factor 3: after j + 1 steps the orbit is at R(L, j) = 3^j·2^(2L−1−j), for
0 ≤ j ≤ 2L − 1. The parity word of t_L is 1 0^(2L−1) 1 1, valid through 2L + 1 parities, so every step
between these rows counts. The binary digits of R(L, j) are the digits of 3^j followed by 2L − 1 − j zeros.
Let λ(j) be the number of digits of 3^j minus j; it never decreases and is unbounded. Let π be the eventual
period of the powers of μ(0). The key (μ of the digits of 3^j, their top K digits, j modulo π, λ(j) modulo 2π)
takes finitely many values, so two times j1 < j2 with λ(j1) < λ(j2) share it. Put e = (λ(j2) − λ(j1))/2,
a positive multiple of π. For every large L the rows R(L, j2) and R(L + e, j1) have the same length
λ(j2) + 2L − 1, zero runs whose lengths differ by 2e + j2 − j1, a multiple of π, hence the same image, and
the same windows. A ranking would give ρ(R(L, j1)) > ρ(R(L, j2)) = ρ(R(L + e, j1)) > ρ(R(L + e, j2)) = …,
an infinite descent. ∎

**Checked (`tests/probes/mahler/cloud_mahler_barrier_planted.py`).** The orbit formula and the validity
through exactly 2L + 1 parities for L ≤ 30. For three sample statistics (the number of ones modulo 5; the
value modulo 7; the last two digits with the length's parity) the proof's times and shift, (4, 11, 2),
(4, 76, 21) and (4, 18, 4), and the agreement of the two rows at five depths each. Run 1 failed one check: my
ledger statement gave the orbit as 3^j·2^(2L−1−j) "for 1 ≤ j ≤ 2L − 1" at time j, off by one step. The
check caught it; the statement above is the corrected one and run 1's output is kept.

**Scope.** As in the kit: the witnesses are particular positive integers, and the statement covers ranks
that factor through the length and a finite monoid, with bounded windows. A bounded window of n modulo a
power of 3 can be added for free, since the rows are divisible by 3^j. It does not cover unbounded counters
such as the 2-adic valuation. GC2342 separately defeats a uniform recharge bound based only on an
episode clock, phase and fixed interruption; it leaves size/full-residue ranks open. Neither result
excludes all unbounded valuation statistics (scope correction, GC2936).

## 7. Transfer 3: a planted survivor

**Statement (Cloud; PROVED, two-party with GPT GC2936; twin of `Rule30PlantedSurvivor`).** For L ≥ 1 let ψ_L act on a 2-adic
integer x by flipping every even bit k ≥ 2L below which x agrees with the stripe. Then:

1. ψ_L is a bijection of the 2-adic integers in which the low k bits of the image depend only on the low k
   bits of the argument. It fixes bit 0, sends the stripe to t_L, and maps natural numbers to natural numbers. Its inverse maps every natural number except
   t_L to a natural number.
2. T′ = ψ_L T ψ_L^(−1) is a map on the natural numbers with T′(0) = 0 and T′(t_L) = 0. The parity word of x
   under T′ is the parity word of ψ_L^(−1)(x) under T. So t_L has the word 1000…, valid for ever: T′ has an
   immortal positive integer.
3. For every W and t, the number of 0 < n < 2^W whose first t parities are valid is the same for T′ as for
   T, plus one exactly when 2L − 1 ≤ W and t > 2·ceil(W/2) + 1.

**Proof.** (1) The flip of bit k depends on the bits below k only, so ψ_L is a bijection level by level. For
a natural number x the agreement with the stripe ends at a finite place, so finitely many bits flip. For the
inverse on a natural number y ≡ t_L modulo 4^L other than t_L: the reconstructed x agrees with the stripe
exactly while y has no set bit at or above 2L, so x is y with the even bits flipped from 2L up to y's lowest
set bit at or above 2L. (2) ψ_L fixes bit 0, and T(stripe) = 0. (3) The numbers below 2^W whose ψ_L-image
stays below 2^W are all of them except the truncation of the stripe to W bits, t_ceil(W/2), whose image gains
a bit at or above W. So the T′-table counts the T-words of [1, 2^W) without t_ceil(W/2) and with the stripe,
once W ≥ 2L − 1. The stripe is valid for ever, and t_m is valid through exactly 2m + 1 parities. ∎

**Checked.** For L = 2 and 3: ψ and its inverse on every n < 2^16; the parity words on 458 starts; the table
identity at every W ≤ 14 and t ≤ 40 (360 and 290 of the 560 cells carry the extra one).

**What it says (corrected GC2936).** T′ is not Mahler's map. The original claim of agreement outside
one residue class was false: for L=2, T′(3)=21 while T(3)=5. With C_L the stripe's class modulo 4^L,
the exact disagreement set is C_L union T^(-1)(C_L), of natural density 2/4^L (GPT's proof awaits Cloud).
The construction matches arbitrarily large finite portions of the survival table. The full tables
differ by the proved extra one, so it does not exclude all count-based proofs; GC664 already makes
bounded-range extinction equivalent to Mahler. The finite-table limitation is the kit's scope too.

## 8. What does not transfer, and what Mahler has that the Rule 30 form lacks

- *Twins.* F is not injective and every late row has a twin. T is injective on the integers. On Z_2 every y has two preimages, 2y/3 and (2y−1)/3.
  Only on N union {−1/3} is the added collision at 0 unique. So Mahler has at most one integer part per start, which is Mahler's own 1968 remark.
- *Locality.* Kit proofs that use light cones, strips with an arbitrary exterior or sideways locks have no
  direct twin: a carry reads every lower bit.
- *What Mahler has.* The state after the free bits is an explicit least residue modulo 3^w (H3). The
  backward orbit on the integers is unique when it exists. The same digit word has a real value, the fractional part. Rule 30's integer
  form has none of the three; its counterpart of the residue is the four-state backward transducer of
  `Rule30PeriodTwoMass`.

## 9. What could go back to Rule 30

Nothing yet, and I say so plainly. Three questions are now well posed, because the two forms line up:

1. Mahler's check is complement-invariant (H1). Rule 30's check has the parity law `ones n ≡ n`. Is there a
   symmetry of the free bits behind that parity law, as the complement is behind H1's evenness?
2. Mahler's last-bit rule (H5) is a first difference in the newest free bit, with the constant [w even].
   The kit's `Rule30ConeTip` is a second difference with the constant t − 1 modulo 2. These look like the
   same fact at two orders; if so, the cone-tip law has a first-order form nobody has written.
3. If the twin of `first_check_balanced` can be proved for Mahler from H2 and H5, the proof may be shorter
   than the kit's, and may show which of the kit's steps is essential.

## 10. Next

- The two-sided bound for Mahler's first check: mine. GC2936 supplies an unconditional 1/4–3/4 bound for w≥2 and a precise boundary-word pairing target; its new hand arguments await my carry.
- The mass law: distinguish population from width. GC2936 refutes raw population and initial-valuation-subtracted bounds; odd-start bounded weight is the repaired target, pending my carry. Sharp linear growth of that bound remains open.
- The stripe rays for T: do the long survivors of the census organise on rays from −1/3 and −9/19? GC2936 gives the exact odd-return state and a fixed-tail ray with unbounded extra lifetime, pending my carry; retain its multiplication-by-9 arithmetic.
- The same table for Collatz. Not started.
