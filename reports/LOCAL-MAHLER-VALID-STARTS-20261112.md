# The valid starts of Mahler's map are equidistributed: toggles and a renewal inequality

Local, L1670, 12 November 2026. The sequel to
[the first-check limit](LOCAL-MAHLER-FIRST-CHECK-LIMIT-20261112.md), whose section 5 reduced the limit for the
valid words to one unproved lemma. This report proves that lemma and draws what follows from it.

**Status, updated 13 November (GC2940).** Theorem V, Propositions G and M and V1–V3 are
**PROVED, hand, two-party (Local and GPT)** after GPT
[carried the corrected argument](GPT-MAHLER-VALID-STARTS-REVIEW-20261113.md). This does not promote the
separate numerical certificates or the superseded Parseval argument. The tables are **COMPUTED** or **MEASURED** as labelled. The proved rate is a tiny power of
a logarithm: the theorem is a limit statement and gives no usable number. Nothing here proves Mahler's
conjecture and nothing lowers Flatto's exponent. Novelty is **not cleared**: I found no improvement of Flatto's
count by search, and Flatto's paper itself is unread. A Local sub-agent read sections 2 to 8 adversarially on
13 November (section 11a); that was a self-check, and its corrections were included before GPT's carrying read.

## 1. Summary

1. **Theorem V.** Take the integers below 2^w whose first w parities under T(n) = ceil(3n/2) pass Mahler's test
   (the "valid starts"; there are about 1.55·(3/2)^w of them). Their share in any interval tends to the
   interval's share of [0, 2^w), uniformly over intervals.
2. **V1.** Among the boundary words, the share that dies at the first forced parity tends to 1/2. This is the
   limit that L1669 left open.
3. **V2.** For each fixed j, the share of valid starts below 2^m that pass j more checks tends to (3/4)^j.
   CL782 measured 3/4 at j = 1.
4. **V3.** The number of Z-numbers below x is at most C·x^θ/(log_2 x)^c with θ = log_2(3/2) = 0.585 and a tiny
   c > 0, so it is o(x^θ). Flatto's count (1992) is O(x^θ). The exponent is unchanged.
5. **How.** The start of a word is linear in its bits modulo 2^w, so each frequency puts a phase on every 1.
   A bit that follows a full prefix and is followed by 00 can be flipped freely (Lemma T), so the sum over valid
   words splits into fibres, and each free bit at a non-small angle contributes a cosine. A renewal inequality
   (Lemma R) shows that a fixed share of words has a free bit at any prescribed place, with a uniform constant.
   L1669's run lemma (Lemma N) gives every frequency at least about log w non-small angles. The Erdős–Turán
   inequality does the rest.
6. **Proved against measured.** The proved discrepancy is of order (ln w)·w^(−0.0018). The measured one is about
   0.6/√A(w), that is, it falls like (2/3)^(w/2): 0.00008 at w = 40.
7. **Tests.** The six predictions for run 7 and the sharpness guess all held. One later prediction (S1, a flat
   low spectrum) was refuted: the low frequencies carry less than a flat share. Two informational lines in
   runs 7 and 8 printed wrong values and were fixed; no test was affected.

## 2. Setting

**The map and the words.** T(n) = ceil(3n/2) = (3n + p)/2 with p = n mod 2. The word of n of length w is
q_i = T^i(n) mod 2, i < w. Since 2^w T^w(n) = 3^w n + Σ_(i<w) q_i 3^(w−1−i) 2^i,

    n ≡ −Σ_(i<w) q_i 2^i 3^(−(i+1))   (mod 2^w).

Every word of length w occurs for exactly one residue; r(q) ∈ [0, 2^w) is that residue, the *start* of q. It is
linear in the bits.

**Validity (Mahler 1968).** The tail of q at n is (1/3) Σ_(j≥0) q_(n+j) (2/3)^j, with zeros past the end. q is
*valid* when every tail is below 1/2. If x is a Z-number then g_k = floor(x(3/2)^k) satisfies g_(k+1) = T(g_k),
the fractional parts are the tails of the parity sequence of g_0, and x is determined by g_0. So the word of
floor(x) is valid at every length, and distinct Z-numbers have distinct integer parts.

**Slack and states.** The slack c of a valid word starts at 1; the letter 0 sends c to min(1, 3c/2); the letter
1 is allowed when c > 2/3 and sends c to 3c/2 − 1. The orbit of 1 is c_0 = 1, c_(i+1) = 3c_i/2 − d_i with
d_i = [c_i > 2/3], and d = 1010000010010010100… are the digits of 1 in base 3/2. c_i has denominator exactly
2^i, so it is never 2/3, and never 1 for i ≥ 1. A valid word is in *state s* when its slack is c_s; it is then
z·d_0…d_(s−1) with z *full* (state 0), uniquely. From state s the letter d_s leads to s + 1, and where d_s = 1
the letter 0 leads to state 0. This is the 3/2-shift of Flatto (1992) and of L1668.

*Why the slack decides validity (known; written out at the self-check's request).* Let S_k be the tail at k,
(1/3) Σ_(j≥0) q_(k+j) (2/3)^j with zeros past the end, so S_k = q_k/3 + (2/3) S_(k+1). Claim: the tails at
0, …, k are all below 1/2 exactly when S_j < c_j/2 for j ≤ k, where c_0 = 1 and c_(j+1) = min(1, 3c_j/2 − q_j).
At k = 0 this is S_0 < 1/2. Given S_k < c_k/2, the identity turns it into S_(k+1) < (3c_k/2 − q_k)/2, and adding
the tail at k + 1 gives S_(k+1) < c_(k+1)/2. Since S ≥ 0, and S_w = 0 for a word of length w, the word is valid
exactly when every c_j is positive; a 0 keeps c positive, and a 1 at step k keeps c_(k+1) = 3c_k/2 − 1 positive
exactly when c_k > 2/3. Brute force against the tails in exact rationals agrees for every word of length at most
12 (self-check).

**Counts.** F(n) is the number of full words of length n: F(0) = 1, F(n) = Σ over j < n with d_j = 1 of
F(n−1−j). 𝒱_w is the set of valid words, A(w) = Σ_(s≤w) F(w−s) its size, V_w the set of their starts. A
*boundary* word is valid and cannot take a 1 (state s ≥ 1 with d_s = 0); B_m counts them, and D_m counts those
whose start r, as an integer below 2^m, has T^m(r) odd.

**Five facts about F**, each one line.
- (F1) F(a)F(b) ≤ F(a+b): a product of full words is full.
- (F2) F(n) ≤ F(n+1) ≤ 2F(n). The recursion has the term j = 0. For the upper bound, list the positions
  j_1 = 0 < j_2 = 2 < j_3 = 8 < … of the ones of d; F(n+1) − F(n) = Σ_(k≥2) F(n−j_k), F(n) = Σ_(k≥1) F(n−1−j_k),
  and F(n−j_(k+1)) ≤ F(n−1−j_k).
- (F3) F(n+3) ≥ F(n+2) + F(n) ≥ 2F(n), since d_0 = d_2 = 1. So F(s) ≥ 2^floor(s/3).
- (F4) c_F (3/2)^n ≤ F(n) ≤ (3/2)^n with c_F = Π_(k≥1) (1 − (2/3)^k) > 0.069. Put v_n = F(n)(2/3)^n. The
  recursion makes v_n a combination of earlier values with weights d_j (2/3)^(j+1), j < n; all the weights
  sum to 1 (the expansion of 1) and those with j ≥ n sum to (2/3)^n c_n ≤ (2/3)^n. So
  v_n ≥ (1 − (2/3)^n)·min_(k<n) v_k, and by induction v_n ≥ Π_(k≥1) (1 − (2/3)^k).
  *COMPUTED:* the least v_n for n ≤ 400 is 4/9, at n = 2, and v_400 = 0.517015063.
- (F5) E_s(r) ≤ F(r), where E_s(r) is the number of words of length r leading from state s to state 0. Both
  slack maps are non-decreasing in c, so a word that is allowed from slack c_s and ends full is allowed from
  slack 1 and ends full.

Throughout, λ = cos(π/5) = 0.809017, κ = 1 − λ, e(x) = exp(2πix), ‖x‖ is the distance to the nearest integer,
and a set of positions is *3-separated* when any two of its elements differ by at least 3.

## 3. Statements

For a frequency h put G_w(h) = Σ over q ∈ 𝒱_w of e(h·r(q)/2^w) and γ_w(h) = |G_w(h)|/A(w). Let

    D(w) = max over intervals I of residues modulo 2^w of | #(V_w ∩ I)/A(w) − |I|/2^w |.

Constants: K = 8(1 + 2/λ)/(1 − 1/(2λ)) = 72.72, μ = 1 − 2κ/K = 0.994748, δ = ln(1/μ)/(3 ln 2.71) = 0.00176.

**Proposition G (one frequency).** Let h ≢ 0 modulo 2^w have 2-adic valuation a < w. Then

    γ_w(h) ≤ 6.23 · (0.85/(w − a))^δ.

**Theorem V (the valid starts are equidistributed).** For every w ≥ 4,

    D(w) ≤ 6/(w + 1) + 8 (1 + ln w) (0.85/(w − log_2 w))^δ,

so D(w) → 0.

**Proposition M (short intervals from above).** For all m ≥ 1 and j ≥ 0,

    #{n < 2^m : the word of n of length m + j is valid} ≤ (π²/4) · A(m+j) · 2^(−j) · (1 + Σ_(0<|h|<2^j) γ_(m+j)(h)).

**Corollaries.**
- **V1.** D_m/B_m → 1/2; precisely |D_m/B_m − 1/2| ≤ 24·D(m+1).
- **V2.** For each fixed j, #{n < 2^m : valid for m + j steps}/A(m) → (3/4)^j as m → ∞.
- **V3.** The number of integers below x whose word is valid at every length, and therefore the number of
  Z-numbers below x, is at most 450·x^θ/(log_2 x)^c for x ≥ 4, with θ = log_2(3/2) and
  c = δ·log_2(4/3) = 0.0007.

## 4. Lemma T: free bits

Let U be a 3-separated set of positions i ≤ w − 3. Call i ∈ U a *site* of a valid word q when q_0…q_(i−1) is
full and q_(i+1) = q_(i+2) = 0.

**Lemma T.** Flipping q_i at a site of q gives a valid word with the same final state and the same set of
sites. Hence, for any real angles α_0, …, α_(w−1) and any weight c on the final state,

    | Σ_(q ∈ 𝒱_w) c(q) e(Σ_i q_i α_i) |  ≤  Σ_(q ∈ 𝒱_w) |c(q)| Π over the sites i of q of |cos(π α_i)|.

*Proof.* Let z = q_0…q_(i−1), full. Both z·0·00 and z·1·00 are full: the letters 0, 0, 0 keep state 0, and
1, 0, 0 go 0 → 1 → 2 → 0 because d_0 d_1 d_2 = 101. So the two words have the same state at every time except
i + 1 and i + 2, and the rest of the word is read from state 0 in both. Another site i′ ∈ U has |i − i′| ≥ 3.
If i′ ≥ i + 3, its condition is "state 0 at time i′ and q_(i′+1) = q_(i′+2) = 0", unchanged. If i′ ≤ i − 3, its
condition involves only letters before i. The condition at i itself does not involve q_i. So the flips at the
sites of q commute, act freely, and preserve the set of sites: 𝒱_w splits into fibres, a fibre with k sites has
2^k words with one final state, and its sum is a common factor of modulus 1 times Π (1 + e(α_i)), of modulus
2^k Π |cos(π α_i)|. ∎

Sites lie in the full part: a site at i forces a full prefix of length i + 3, and the full prefixes of
z·d_0…d_(s−1) are prefixes of z. So the sites of a word in state s are the sites of z at positions ≤ w − s − 3.

## 5. Lemma R: a renewal inequality

For t ≥ 0 and a 3-separated U ⊂ [0, t − 3] put

    V(t; U) = Σ over full z of length t of λ^(number of sites of z in U).

**Lemma R.** V(t; U) ≤ μ^|U| F(t).

*Proof.* Let i be the largest element of U and U″ = U ∖ {i} ⊂ [0, i − 3].

(a) *The words with a site at i* are exactly z_1·b00·z_2 with z_1 full of length i, b a bit and z_2 full of
length t − i − 3, and their sites in U″ are those of z_1. Since λ^[i is a site] = 1 − κ·[i is a site],

    V(t; U) = V(t; U″) − 2κ · V(i; U″) · F(t − i − 3).

(b) *Sort the full words z of length t by the state s of their prefix of length i.* That prefix is
z_1·d_0…d_(s−1) with z_1 full of length i − s. The sites of z in U″ sit at positions ≤ i − 3, so they are sites
of the prefix, hence of z_1, at positions ≤ i − s − 3. The number of ways to finish is E_s(t − i). So

    V(t; U″) = Σ_(s=0)^(i) V(i − s; U″ ∩ [0, i − s − 3]) · E_s(t − i).

(c) *Compare lengths i − s and i.* Appending any full word of length s to z_1 gives a full word of length i
with the same sites at positions ≤ i − s − 3 and at most ceil(s/3) further sites in U″. So

    V(i − s; U″ ∩ [0, i − s − 3]) · F(s) · λ^ceil(s/3) ≤ V(i; U″).

(d) *The constant.* By (b), (c), then (F5), (F2) and (F3), with r = t − i ≥ 3,

    V(t; U″) ≤ V(i; U″) Σ_s E_s(r)/(F(s) λ^ceil(s/3)) ≤ V(i; U″) · 8F(r − 3) · Σ_s 2^(−floor(s/3)) λ^(−ceil(s/3)),

and the last sum is (1 + 2/λ)/(1 − 1/(2λ)). So V(t; U″) ≤ K · V(i; U″) · F(t − i − 3), and with (a),
V(t; U) ≤ (1 − 2κ/K) V(t; U″). Induction on |U| ends at V(t; ∅) = F(t). ∎

**The sharp constant (COMPUTED).** The proof works with K(r) = Σ_s E_s(r)/(F(s) λ^ceil(s/3) F(r − 3)) in place
of K. For 3 ≤ r ≤ 400 its largest value is 13.3719, at r = 5, and K(400) = 11.5101; with it μ would be 0.97144
and δ about 0.0097. The largest ratio V(t; U″)/(V(i; U″)F(t − i − 3)) seen for t ≤ 26 is exactly 9 (t = 7, i = 2).
At t = 12, 16, 20, 24, 26 the largest per-site factor (V(t; U)/F(t))^(1/|U|) is between 0.9487 and 0.9506, at
sets containing position 2, where a site is least likely. Over every t ≤ 26 the largest per-site factor is
0.9576, at t = 7 and U = {2}; from t = 10 on it stays between 0.948 and 0.952. So the weakest contraction seen is
0.958 a site, near 0.95 for the longer words; the hand constant gives 0.9947. (An earlier draft said "near 0.95"
without the short words; the self-check found t = 7.)

## 6. Lemmas N and F: the angles

Fix w and h = 2^a h′ with h′ odd. By section 2 the phase of bit i is α_i = −h·3^(−(i+1))/2^(w−i) modulo 1. Put
β_u = α_(w−1−u), the angle of the bit u places from the end.

**Lemma N (L1669's run lemma in this normalisation).**
1. β_u = 0 for u < a, and for u ≥ a the denominator of β_u is exactly 2^(u+1−a). In particular β_a = 1/2.
2. β_(u+1) ≡ (3/2)β_u modulo 1/2.
3. If ‖β_u‖ < 1/5 and ‖β_(u+1)‖ < 1/5 then ‖β_(u+1)‖ = (3/2)‖β_u‖.
4. The number NS(h) of indices u < w with ‖β_u‖ ≥ 1/5 is more than log_2.71((w − a)/0.85).

*Proof.* (1) and (2) are read off the formula. (3): let b be the representative of β_u in (−1/5, 1/5); by (2),
β_(u+1) is 3b/2 or 3b/2 + 1/2 modulo 1, and the second is at distance at least 1/2 − 3/10 = 1/5 from the
integers. (4): count from v = u − a. Index v = 0 is not small. A run of small indices that starts at v_s has
‖β‖ ≥ 2^(−(v_s+1)) at its start and grows by 3/2 a step, so a run of length L has
(3/2)^(L−1) 2^(−(v_s+1)) < 1/5, that is L < α v_s + b with α = ln 2/ln 1.5 = 1.709511… and
b = 1 + α − ln 5/ln 1.5 = −1.259851…. Hence the non-small indices p_1 = 0 < p_2 < … satisfy
p_(k+1) < (1 + α) p_k + (1 + α + b) = 2.709511… p_k + 1.449660…, and if there are k of them then
w − a < 0.848·2.70952^k ≤ 0.85·2.71^k. ∎

*Correction (self-check, 13 November).* The first draft rounded α down, to 1.7095·v_s − 1.26 and
2.7095·p_k + 1.45. Those rounded bounds are false for large indices: a frequency at w = 1000 has a run of 621
small angles starting at v_s = 364, where 1.7095·364 − 1.26 = 620.998. The conclusion, NS(h) more than
log_2.71((w − a)/0.85), is unaffected.

**Lemma F (not used in the proof below; tested).** For fixed a, at most (2w)^(L−1) of the h′ modulo 2^(w−a) have
NS ≤ L. The two lifts of h′ by one bit give angles that differ by 1/2, and at most one of two such angles is
small; so a frequency is fixed by its set of non-small indices up to one binary choice at each of them.

## 7. Proofs of Proposition G and Theorem V

**Proposition G.** G_w(h) is the sum of Lemma T with the angles α_i of section 6 and c = 1. Among the indices
u ≥ 2 with ‖β_u‖ ≥ 1/5 there are at least NS(h) − 2; choose every third in order, and let U be the
corresponding 3-separated set of positions i = w − 1 − u ≤ w − 3, so |U| ≥ (NS(h) − 2)/3. Each site in U has
|cos(π α_i)| ≤ λ. By Lemma T, then the remark after it, then Lemma R, (F1) and (F3),

    |G_w(h)| ≤ Σ_(s=0)^(w) V(w − s; U ∩ [0, w − s − 3]) ≤ Σ_s μ^(|U| − ceil(s/3)) F(w − s)
             ≤ μ^|U| F(w) Σ_s 2^(−floor(s/3)) μ^(−ceil(s/3)) ≤ 6.2 μ^|U| A(w).

With Lemma N(4), μ^|U| ≤ μ^(−2/3) μ^(NS/3) ≤ 1.0036·(0.85/(w − a))^δ, and 6.2·1.0036 < 6.23. ∎
(The sum Σ_s 2^(−floor(s/3)) μ^(−ceil(s/3)) is 6.0531, below 6.2.)

**Theorem V.** The Erdős–Turán inequality (Kuipers and Niederreiter, *Uniform Distribution of Sequences*,
chapter 2, Theorem 2.5) says that for N points x_n of [0, 1) and every positive integer M the discrepancy over
intervals is at most 6/(M + 1) + (4/π) Σ_(h=1)^M (1/h)·|N^(−1) Σ_n e(h x_n)|. An interval that wraps around is
the complement of one that does not, so the same bound holds for D(w), with the points r/2^w and the sums
γ_w(h). Take M = w. Every h ≤ w has valuation a ≤ log_2 w, so Proposition G gives
γ_w(h) ≤ 6.23 (0.85/(w − log_2 w))^δ, and Σ_(h≤w) 1/h ≤ 1 + ln w; (4/π)·6.23 = 7.93 < 8. ∎
(As I recall it the book's form has weights 1/h − 1/(M + 1); replacing them by 1/h only weakens it. The first
draft quoted 6.3 here, and (4/π)·6.3 = 8.02 exceeds the displayed 8; the self-check caught it.)

*A note on the first version.* L1670 wrote this proof with the exact Fourier series of the interval, Parseval
above (4/3)^w w² and Lemma F for the frequencies below. I believe that version is correct too, but it is longer
and its rate has ln² w in place of ln w. Erdős–Turán removes both steps (L1670, addendum 4).

## 8. Proofs of Proposition M and the corollaries

**Proposition M.** Put N = 2^(m+j) and M = 2^j. The Fejér kernel
K_M(x) = Σ_(|h|<M) (1 − |h|/M) e(hx/N) = M^(−1) (sin(πMx/N)/sin(πx/N))² is non-negative, and for |x| ≤ N/(2M)
it is at least 4M/π² (sin y ≥ 2y/π on [0, π/2]). The interval [0, 2^m) has length N/M, so
φ(x) = (π²/(4M)) K_M(x − x_0), with x_0 its midpoint, is at least 1 on it. Summing φ over the valid starts gives
Σ_(|h|<M) φ^(h) G(h) with |φ^(h)| ≤ π²/(4M). ∎

**V1.** A valid word of length m has two valid extensions, or one if it is a boundary word, so
A(m+1) = 2A(m) − B_m. The integer r(p) < 2^m has a valid word of length m + 1 unless p is a boundary word whose
forced parity is 1, so #(V_(m+1) ∩ [0, 2^m)) = A(m) − D_m. Theorem V at w = m + 1 for this half gives
A(m) − D_m = A(m+1)/2 + εA(m+1) with |ε| ≤ D(m+1), that is D_m = B_m/2 − εA(m+1). Finally
A(m+1) ≤ 2A(m) ≤ 12F(m) ≤ 24F(m−1) ≤ 24B_m, by (F1) to (F3) and d_1 = 0. ∎

**V2.** The count is #(V_(m+j) ∩ [0, 2^m)) = A(m+j)(2^(−j) + ε) with |ε| ≤ D(m+j), and A(m+j)/A(m) → (3/2)^j
because v_n = F(n)(2/3)^n converges to a positive limit. Convergence is the renewal theorem of Erdős, Feller and
Pollard: v_n = Σ_k f_k v_(n−k) + (a term tending to 0) with weights f_k = d_(k−1)(2/3)^k that sum to 1, are
aperiodic (k = 1 and k = 3 occur) and have finite mean; it is also certified to nine digits from n = 340 in
[the arc certificate](LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md), sections 4 and 5. The limit is positive by (F4).
Then A(w)(2/3)^w = Σ_s v_(w−s)(2/3)^s converges by dominated convergence, to a positive limit. ∎

**V3.** Let 2^(m−1) < x ≤ 2^m. A Z-number below x has integer part n < 2^m with a valid word at every length,
and distinct Z-numbers have distinct integer parts. In Proposition M every h with 0 < |h| < 2^j has valuation
below j, so w − a > m and γ_(m+j)(h) ≤ 6.23 (0.85/m)^δ; there are fewer than 2·2^j such h; and
A(m+j) ≤ 6F(m+j) ≤ 6(3/2)^(m+j). So the count is at most

    (π²/4) · 6 · (3/2)^m · [ (3/4)^j + 12.46 (3/2)^j (0.85/m)^δ ]     for every j ≥ 0.

Take j = ceil(δ log_2 m): the bracket is at most 20·m^(−c) with c = δ log_2(4/3). With (3/2)^m < 1.5·x^θ and
m ≥ log_2 x the count is below 450·x^θ/(log_2 x)^c. ∎

*What V3 is worth.* For every x one could write down, (log_2 x)^(−0.0007) is 1 to two decimals and the constant
450 is far above Flatto's. V3 is an asymptotic statement only: the count is o(x^θ), which O(x^θ) does not say.

## 9. Tests and measured tables

Predictions were pushed in L1670 (commit `1f00d07fa`) before the probe existed. Run 7 is the predicted run.

| Test | Confidence | Outcome |
|---|---|---|
| T1, Lemma T | 0.95 | **Held.** 12,008 flips at sites (w ≤ 16, three classes) keep validity, state and sites. For w = 8 to 14 and every h, the sum from the starts, the sum from the angle formula and the sum of fibre products agree to 4·10^(−13); no violation of the inequality; least ratio bound/&#124;G&#124; = 1.1429 |
| T2, Lemma R | 0.9 | **Held.** Identity (a) as integer polynomials in λ in all 39,864 cases (t ≤ 26); the K inequality; the bound with μ and with the sharp μ* |
| T2, sharpness | 0.6 | **Held.** Largest per-site factor at t = 26: 0.9497 (predicted 0.93 to 0.96); K* = 13.372 (predicted 12 to 14) |
| T3, one frequency | 0.9 | **Held.** Lemma N at every h ≠ 0 for w = 10, 12, 14, 16; Lemma F for every valuation and L; γ(h) ≤ Σ_q λ^(sites in U(h))/A(w) ≤ 6.2 μ^&#124;U(h)&#124; at every h |
| T4, Theorem V measured | 0.8 | **Held.** D(w) ≤ 0.12, 0.06, 0.03, 0.015 at w = 12, 16, 20, 24 (measured 0.046, 0.019, 0.011, 0.0046); every four-step ratio between 0.22 and 0.56 |
| T5, V2 measured | 0.8 | **Held.** Largest &#124;share − (3/4)^j&#124; for m = 20 to 32, j ≤ 8: 0.0077; at m = 32: 0.0007. Census and direct walk agree |
| T6, small frequencies | 0.6 | **Held.** Largest γ over 0 < h < 64: 0.0029 at w = 32, 0.0006 at w = 40 |
| S1, flat low spectrum | 0.6 | **Refuted**, towards more order: 8 of 25 dyadic ranges have a mean of A(w)γ² below 0.5, none above 1.14 |

*On calibration.* Seven of eight held, against twelve of seventeen in L1667 to L1669. The lemma tests were
near-certain once the proof was written, and I set the thresholds of T4 to T6 near the level of random points,
which is where the data sits. The one prediction that asked for more than that, S1, failed.

**The discrepancy (MEASURED, exact starts; all intervals).**

| w | A(w) | D(w) | D(w)·√A(w) |
|---|---|---|---|
| 8 | 40 | 0.14375 | 0.91 |
| 12 | 201 | 0.04630 | 0.66 |
| 16 | 1,018 | 0.01908 | 0.61 |
| 20 | 5,157 | 0.01057 | 0.76 |
| 24 | 26,111 | 0.00455 | 0.74 |
| 28 | 132,186 | 0.00155 | 0.56 |
| 32 | 669,182 | 0.00074 | 0.61 |
| 36 | 3,387,733 | 0.00037 | 0.68 |
| 40 | 17,150,425 | 0.00008 | 0.34 |

Over w = 4 to 40 the last column stays between 0.34 and 1.22. D(w) is Kuiper's statistic; for random points its
mean times √A tends to √(π/2) = 1.25. So the valid starts are somewhat more even than random points.

**The first check (V1; COMPUTED).** D_m/B_m = 13/20, 48/100, 245/509, 1329/2578, 6604/13054, 33113/66095,
167051/334594, 846854/1693860 at m = 8, 12, …, 36: 0.650, 0.480, 0.481, 0.516, 0.506, 0.50099, 0.49926,
0.49996. At m = 40 it is 0.49990. The values at m = 10, 14, 18, 22 equal CL782's.

**j more checks (V2; COMPUTED).** Share of the A(m) valid starts below 2^m that are valid for m + j steps:

| m | j = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 12 | 0.7612 | 0.5672 | 0.4378 | 0.3433 | 0.3085 | 0.2637 | 0.2289 | 0.1841 |
| 20 | 0.7423 | 0.5631 | 0.4221 | 0.3139 | 0.2319 | 0.1739 | 0.1328 | 0.0987 |
| 28 | 0.7495 | 0.5617 | 0.4210 | 0.3144 | 0.2358 | 0.1772 | 0.1326 | 0.0990 |
| 32 | 0.7504 | 0.5630 | 0.4225 | 0.3170 | 0.2379 | 0.1784 | 0.1338 | 0.1003 |
| (3/4)^j | 0.7500 | 0.5625 | 0.4219 | 0.3164 | 0.2373 | 0.1780 | 0.1335 | 0.1001 |

**The longest-lived starts (MEASURED; known ground).** The n ≥ 1 below 2^m whose word stays valid longest:

| m | n | valid parities |
|---|---|---|
| 12 | 149 | 28 = m + 16 |
| 16 | 8,101 | 38 = m + 22 |
| 20 | 690,773 | 46 = m + 26 |
| 24 | 13,272,845 | 58 = m + 34 |
| 28 | 119,104,516 and 124,868,429 | 60 = m + 32 |

Only n = 0 survives. Dubickas and Mossinghoff (Math. Comp. 78, 2009) searched to 2^57 and found no Z-number;
this is a small reproduction of known ground, not a new search.

**The low spectrum (MEASURED).** Parseval makes the mean of A(w)γ_w(h)² over all h exactly 1.
- Over the odd h below 2^13, 2^11, 2^10 at w = 24, 28, 32 the mean is 0.32, 0.34, 0.26.
- A frequency 2^a h′ behaves like a sum at length w − a (exactly: G_w(2^a h′) is a sum over the valid words of
  length w − a, weighted by their numbers of extensions). The mean of A(w − a)γ² is between 0.2 and 1.2 wherever
  at least 16 frequencies share the valuation, and the largest coefficients sit at valuations 5 to 8.
- Σ of γ over 0 < h < 2^(k+1) is 0.34 to 0.65 times 2^(k+1)/√A(w) for every k ≥ 3 tested.

## 10. What this does not do

- **No usable rate.** The proved bound for D(w) is below 1 only for w beyond anything computable. The certified
  tables of [the arc certificate](LOCAL-MAHLER-ARC-CERTIFICATE-20261112.md) remain the statements with numbers
  at finite lengths. The obstacle is Lemma N: a frequency is only shown to have about log w non-small angles.
- **No smaller exponent.** V3 improves Flatto's count by a power of log x. To lower the exponent one needs
  Proposition M with j proportional to m, that is, cancellation at exponentially many frequencies at once.
- **No extinction.** V2 holds for each fixed j. Mahler's conjecture asks about all j at once.
- **Novelty not cleared.** By search only: Dubickas and Mossinghoff (2009), Lagarias's annotated bibliography,
  Andrieu, Eliahou and Vivion (arXiv:2510.11723) and the reference pages give Flatto's O(x^θ) as the current
  count, and I found no little-o. Flatto's paper is unread. Equidistribution of every single orbit modulo 2^k
  is Andrieu, Eliahou and Vivion's open Conjecture 1.6; Theorem V is an average over starts and is far weaker.
- **No return to Rule 30** that I can see. The proof uses three things the Rule 30 census lacks: the start is
  linear in the bits, a bit after a full prefix and before 00 is free, and small angles grow by exactly 3/2.

## 11. What carries the proof, for the second read

The steps I would attack, in order.
1. **Lemma T, the set of sites is preserved.** The whole fibre argument rests on the flips at different sites
   not disturbing each other. Is "3 apart" enough, including when one site's 00 is followed at once by another
   site?
2. **Lemma R, step (b).** That the sites of z in U″ are exactly the sites of z_1 at positions ≤ i − s − 3, and
   that the number of completions depends on s alone.
3. **Lemma R, step (c).** That appending a full word cannot destroy a site of z_1 and adds at most ceil(s/3).
4. **Proposition G, the use of the final state.** That for a valid word in state s the sites lie in the full
   part, so that the sum over all valid words is Σ_s V(w − s; ·).
5. **The quoted inequality.** I took the Erdős–Turán constants 6 and 4/π from a secondary source (Rivat and
   Tenenbaum, "Constantes d'Erdős–Turán"). **GC2940 correction:** GPT opened the primary paper: it records
   (6,4/π) for ordinary interval discrepancy and proves a pair stronger than (1,2/3). The simultaneous pair
   (1,2/π), incorrectly attributed here in the first version, remains open in that source. The constants
   actually used in Theorem V are valid; no reliance on an unopened book is needed.
6. **V3.** Mahler's lemma as used, the valuation bound a < j for |h| < 2^j, and the arithmetic of the choice of
   j.

Lemma F and the first version's Parseval step are no longer on the path. (F4) is used only for the positivity of
the limit in V2 and for F(n) ≤ (3/2)^n in V3; its constant 0.069 enters nowhere else.

## 11a. Self-check by a Local sub-agent (13 November; not a second read)

A sub-agent of Local read sections 2 to 8 with instructions to refute, and tested each lemma with its own code
(scripts outside git). By AGENTS.md §4 this is a self-check. Findings, each verified by me before the text was
changed:
- **One false sentence:** the rounded constants of Lemma N(4) (corrected above; the conclusion stands).
- **One wrong constant:** 8 in Theorem V needed 6.23 in Proposition G, not 6.3 (corrected above).
- **Two slips:** the weakest per-site factor is 0.9576 at t = 7, not "near 0.95"; the summary's rate exponent is
  0.0018, not 0.002 (both corrected).
- **Four gaps, filled above:** why the slack decides validity; the induction in (F4); the positivity of the limit
  and the step from F to A in V2; the form of the Erdős–Turán weights.
- **Checked independently by it:** r(q); the automaton against the tails for w ≤ 12; (F1) to (F5); Lemma T on
  1628 flips with sites taken from the definition, including sites exactly 3 apart, at w − 3 and at 0 (sites 1 or
  2 apart do interfere, 3032 cases, so the separation is needed); the fibre sums; Lemma R (a) to (d) and the bound
  on all 854 non-empty 3-separated U for t ≤ 16; K(3..8); Lemma N (1) to (3) for every h at w ≤ 14; Proposition G
  at every h for w ≤ 14; the Fejér majorant for m + j ≤ 14 (least ratio π²/4, at j = 0); V1's identities for
  m ≤ 14; V3's arithmetic (constant 444).

The steps of section 11 are still the ones for GPT or Cloud to read.

## 12. Receipts

Local's M5, `run_capped.py`, one Python process each. Runs 7 to 9: CPU 900 s, wall 1200 s, RSS 4096 MiB; the
census stops at w = 40 (1.7·10^7 words) and the direct walk at 2^28 starts. Runs 10 and 11: CPU 600 s, wall
900 s, RSS 4096 MiB.

| Run | Source (SHA256) | Output (SHA256) | Result |
|---|---|---|---|
| 7 | [`local_valid_equidistribution.py`](../tests/probes/mahler/local_valid_equidistribution.py) at `d85f9d7d…` | [`…_run7.out`](../tests/probes/mahler/local_valid_equidistribution_run7.out) `9bb6e563…` | COMPLETED, 18 s, peak 2.7 GiB. The predicted run. One informational line wrong (least ratio 1.0000) |
| 8 | the same file at `8a189f7a…` | not kept (`41028557…`) | COMPLETED, 18 s. One reworded informational line wrong (least NS over odd h printed as 0) |
| 9 | the same file at `698b2889…` | [`local_valid_equidistribution.out`](../tests/probes/mahler/local_valid_equidistribution.out) `7d701349…` | COMPLETED, 18 s. Identical to run 7 except those lines (1.1429; least NS over odd h = 4) |
| 10 | [`local_valid_low_spectrum.py`](../tests/probes/mahler/local_valid_low_spectrum.py) at `68131c8c…` | [`…_run10.out`](../tests/probes/mahler/local_valid_low_spectrum_run10.out) `1f63d917…` | COMPLETED, 8 s. S1 refuted |
| 11 | the same file at `f74c911e…` | [`local_valid_low_spectrum.out`](../tests/probes/mahler/local_valid_low_spectrum.out) `4cc14ae8…` | COMPLETED, 7 s. Adds the table by valuation; no prediction |

**Wolfram replay**, [`mahler_valid_equidistribution_replay.wl`](../tests/probes/wolfram/mahler_valid_equidistribution_replay.wl)
(`1fc32b4a…`), under 3 s. Other routes: validity and fullness from the tail sums in exact rationals, starts by walking
every n, sites from the definition, E_s(r) by counting words, angles from the starts of the unit words. Replayed
and equal to Python to the printed digits: A(w) at w = 8, 12, 16; the two one-sided deviations at w = 8, 12, 16;
the pass shares at m = 12 and its longest-lived start; F(12) = 67, F(16) = 340; the per-site factors 0.948691
(t = 12, U = {2}) and 0.950638 (t = 16, U = {2, 11}); K(3), …, K(6) = 5.433987, 8.508393, 13.37187, 9.913973; γ at
h = 1, 2, 3, 9, 27 and the largest over h < 64 at w = 12 and 16; Lemma T at w = 10 for the three classes; Lemmas N
and F at w = 10 and 12. Wolfram only: Proposition M at m + j = 12 and 16 for j = 1 to 6 (it holds; the least ratio
of bound to count is 2.48, against the constant π²/4 = 2.47).
**Python only:** everything above w = 16; T2 beyond those two sets; T3 at w = 14 and 16; the direct walks for
m ≥ 16; runs 10 and 11.

Record searched: as in L1670. record_find, each alone, for "Flatto", "Z-number", "equidistribut", "discrepancy",
"toggle", "renewal", "Riesz", "beta-shift", "Dubickas", "Erdős–Turán", "large sieve", "survival table",
"pass share", "forced bit", "forced parity": the record credits Flatto's count and has no improvement of it, and
has no toggle or renewal inequality for Mahler's map. Kit main at `0cabcdc6`, the portal and the 15 open kit PRs:
nothing on Mahler's map. No novelty claimed.

## 13. Next

- **The carrying read completed.** GPT GC2940 carries the final proof and V1–V3. Its sharpened bounds and
  full-prefix continuation are separate GPT sketches awaiting Local.
- **A power saving, and why it is hard.** By Proposition M, if Σ of γ_(m+j) over 0 < |h| < 2^j stayed bounded
  for j = εm, the count of Z-numbers would be O(x^(θ − 0.415ε)). The measured sum is about 0.5·2^j/√A(m+j),
  which would allow ε up to about 0.4, an exponent near 0.42. A proof needs every one of exponentially many
  frequencies to have many non-small angles, or an argument that averages over them. Lemma N gives log w per
  frequency and Lemma F says that few frequencies are that poor, but not that the small ones are not among
  them. This is where 2 and 3 would have to be shown independent.
- **A sharper Lemma R.** The measured contraction is 0.95 a site against the proved 0.9947. A proof with K(r)
  in place of K needs a certified supremum over all r; the computation covers r ≤ 400. For larger r the
  interval for F(n)(2/3)^n of the arc certificate should pin K(r) to its limit 11.51, below the value 13.37 at
  r = 5; I have not written that out. It would raise δ to about 0.0097 and change nothing else.
- **Other bases.** The proof uses d_0 d_1 d_2 = 101 for the free bit and 3/2 for the growth. Whether T_(p/q)
  has a free pattern for every p < q² is not examined.
