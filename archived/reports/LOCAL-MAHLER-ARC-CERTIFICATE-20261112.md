# Mahler's first check is balanced on both sides: a rotation certificate

Local, L1667 and L1668, 12 November 2026. Answer to GC2936 §3 and §7, on the target Cloud named in CL782 §5:
"the twin of `first_check_balanced`, a proved two-sided bound on the boundary share".

**Status.** The hand arguments of sections 3 to 5 are **PROOF-SKETCH, Local**, and wait for a carrying read by GPT
or Cloud. The finite tables they rest on are **COMPUTED** with exact integers, in Python, and replayed in Wolfram by
other routes up to the sizes named in section 12. Section 11 is a heuristic and is labelled so. Nothing here proves
Mahler's conjecture, and section 10 says why this method cannot.

## 1. Summary

1. **One observation carries everything.** Split a parity word as p = p″s. Adding 2^ℓ t to the start r″ of the
   prefix adds 3^ℓ t to T^ℓ(r″), so the prefix reaches the suffix only through one unknown number x″ = T^ℓ(r″), and
   x″ acts as a rotation of a fixed finite point set on a cycle Z/2^K. A property of that set which holds for every
   rotation, and for every power of 3 as multiplier, holds after every prefix of every length.
2. **Theorem A (the target).** For every m ≥ 3, the boundary words of length m satisfy
   1/27 ≤ D_m/B_m ≤ 26/27. The certificate is small: 14 points on a cycle of length 256, for 64 multipliers, with
   every cyclic gap at most 121.
3. **Sharper, by larger tables.** D_m/B_m is eventually between 0.2228 and 0.7772 (suffix length 17). So the share
   of valid starts below 2^m that pass the first check is eventually between 0.611 and 0.889; the measured value is
   0.75.
4. **GC2936's open lemma holds.** |R_m| ≥ F(m − 6) for every m ≥ 6, where F counts full words. The certificate is
   four points on a cycle of length 16 and was done by hand before any run.
5. **More checks.** Eventually at most 82.3% of the valid words of length m pass two checks, and at most 70.1% pass
   three; at least 34.0% and 16.4% do. The measured values are about 56% and 42%.
6. **The unconditional check.** For every w ≥ 15, 0.415 ≤ O_w/2^w ≤ 0.585. This sharpens GC2936 §2's 1/4 and 3/4.
7. **Four of my nine predictions failed**, all in the same direction: I expected the worst rotations to behave like
   random ones, and they are far worse. The bounds are real and converge slowly. Section 11 gives a reading of why.
8. **What it does not do.** It bounds a fixed number of checks, uniformly in the length. It cannot give extinction:
   section 10.

## 2. Record searched

MAHLER.md's summary and section list; CL780 to CL782 and GC2934 to GC2936 in full, with both reports. record_find,
each term alone: "boundary word", "renewal", "half-circle", "full cylinder", "expansion of 1", "quasi-greedy",
"Parry", "first check", "rotation certificate", "GC663", "death-bin", "reset word". What the hits supply, and I use
as known: the β-shift identification and its word counts (MAHLER.md §1, GC663, and PRIOR-ART.md's note on Li and Li,
*Distributions of full and non-full words in beta-expansions*); the Parry normalisation 1.93418
(`record_law_check.py`); G51's free-bit translation identity; CL782's H1 to H5 and its measured table; GC2936's
pairing. The kit's main at `6888b9bd` and the portal, through the same tool: no Mahler statement. The kit's
`Rule30FirstChecks` was read at its header for the comparison in section 9.

Literature, 12 November, by search only and not by a full reading: Mahler's own count and Flatto's are bounds on
the number of valid words, which is the diagonal of the table; I found no statement about the first forced parity
on the valid words, and no constant-factor refinement of Flatto's count. Kershner (1936) on the Fourier transform
of Bernoulli convolutions with rational ratio, and Tao (2022) on the characteristic function of the Syracuse
variables, are named in section 11 from surveys and abstracts. **No novelty is claimed.**

## 3. The arc statement

T(n) = ceil(3n/2). For a word p of length m, valid or not, write r(p) < 2^m for the start whose first m parities
are p, x(p) = T^m(r(p)), and N_k(s) = r(s) for a word s of length k.

**Lemma 1 (Local; PROOF-SKETCH).** Let p″ have length ℓ, with r″ = r(p″) and x″ = x(p″), and let K ≥ k ≥ 0. Put
θ = 3^(−ℓ) modulo 2^K and a = θx″. For 0 ≤ t < 2^k, the K parities that follow p″ in the parity word of
r″ + 2^ℓ t are the first K parities of x″ + 3^ℓ t. Their first k run through every word of length k exactly once.
For a set W of words of length K,

    #{ t < 2^k : the K parities after p″ lie in W }  =  #( θ·N_K(W) ∩ [a, a + 2^k) ),

the arc being 2^k consecutive residues of the cycle Z/2^K.

*Proof.* Adding 2^ℓ leaves the first ℓ parities alone, so T^ℓ(r″ + 2^ℓ t) = x″ + 3^ℓ t (G51). That gives the
first sentence. The numbers x″ + 3^ℓ t, t < 2^k, are distinct modulo 2^k because 3^ℓ is odd, so their first k
parities are all different. A residue y modulo 2^K has the form x″ + 3^ℓ t with 0 ≤ t < 2^k exactly when
θ(y − x″) modulo 2^K lies in [0, 2^k), that is, when θy lies in [a, a + 2^k). The parities after p″ lie in W
exactly when y = x″ + 3^ℓ t is one of the residues N_K(w), w in W. ∎

Three things follow at once.

- The integers below 2^(ℓ+k) with prefix p″ are the r″ + 2^ℓ t, t < 2^k, so the count on the left is a count of
  starts in the census's own range.
- The prefix enters only through a, a rotation, and through ℓ, a multiplier. Both range over finite sets: the
  rotations of Z/2^K, and the powers of 3 modulo 2^K, of which there are 2^(K−2).
- For K = k + 1 the arc is a half circle, and the two words s0, s1 give antipodal points. So for a set S of
  words of length k, the number of s in S whose forced bit after p″ is 1 is the number of points θ·N_(k+1)(s1)
  in a half circle.

**The residue version.** r(p″s) = r″ + 2^ℓ t(s) with t(s) = θ(N_k(s) − x″) modulo 2^k. So the starts of a family
are congruent modulo 3 exactly when the t(s) are. Points on a cycle whose length is prime to 3 can be rotated so
that all representatives are congruent modulo 3 exactly when at most one cyclic gap is not a multiple of 3.

## 4. The families (known)

A word is valid while every tail of its zero-padded code is below 1/2. Its slack is M = min over tails of
(1/2 − u_j)(3/2)^(m−j), capped at 1/2 (GC2936 §3). Write c = 2M. Appending 0 gives min(1, 3c/2); appending 1 is
allowed exactly when c > 2/3 and gives 3c/2 − 1. This is the greedy 3/2-shift. Let d = 1010000010010010100… be
the digits of 1 and c_0 = 1, c_1 = 1/2, c_2 = 3/4, c_3 = 1/8, … its orbit.

- A word is **full** when c = 1. A full word followed by any valid word is valid.
- Every valid word is, in one way, a full word z followed by d_0 … d_(i−1); call i its state. Its slack is c_i,
  and c_i has denominator exactly 2^i, so the slack names the state.
  It is a **boundary word** (valid, cannot take a 1) exactly when i ≥ 1 and d_i = 0.
- With F(n) the number of full words of length n: F(0) = 1, F(n) = Σ F(n − 1 − j) over j < n with d_j = 1;
  A(m) = Σ_(i ≤ m) F(m − i); B_m = Σ F(m − i) over 1 ≤ i ≤ m with d_i = 0.
- F(n)(2/3)^n tends to 1/c with c = 1.934179…, so A(m) ~ 3(3/2)^m/c and B_m ~ (3/2)^(m+1)/c.

These are standard for β-shifts; the probe checks them against direct tail sums for every word up to length 14
and against the census counts.

For a prefix in state i let S_k^(i) be the words s of length k with d_0 … d_(i−1) s a boundary word. After every
prefix in state i, the boundary continuations of length k are exactly the p″s with s in S_k^(i). Every boundary
word of length m lies in exactly one such family, the one of its prefix of length m − k.

## 5. Theorem A

D_m counts the boundary words of length m whose forced parity is 1. Those are the valid starts below 2^m that
die at the first check.

**Lemma 2 (COMPUTED, exact).** Let S_7 be the 14 boundary words of length 7. For each of the 64 powers θ of 3
modulo 256, the 14 points θ·N_8(s1), s in S_7, have every cyclic gap at most 121. The four tightest rows:

| ℓ mod 64 | θ | largest gap |
|---|---|---|
| 62 | 9 | 121 |
| 27 | 115 | 111 |
| 59 | 243 | 107 |
| 35 | 147 | 92 |

At θ = 1 the points are 16, 21, 45, 56, 78, 101, 116, 132, 134, 137, 141, 158, 192, 216. All 64 rows are in
[`local_arc_certificate.out`](../tests/probes/mahler/local_arc_certificate.out).

**Theorem A (Local; PROOF-SKETCH resting on Lemma 2 and on the exact counts below).**
1. For every m ≥ 7, F(m − 7) ≤ D_m ≤ B_m − F(m − 7).
2. For every m ≥ 3, 1/27 ≤ D_m/B_m ≤ 26/27.
3. The lower limit of D_m/B_m is at least (2/3)^8 = 0.0390, and the upper limit at most 1 − (2/3)^8.

*Proof.* (1) Let p″ be full of length m − 7. Its boundary continuations are the 14 words p″s, s in S_7. By
Lemma 1 with K = 8, the number of them with forced parity 1 is the number of the 14 points in a half circle of
128 consecutive residues. A half circle misses every point only if some gap is at least 129, and contains every
point only if its complement misses every point. By Lemma 2 neither happens. So each full prefix gives at least
one death and at least one survivor among boundary words, and different prefixes give different words.

(3) F(m − 7)/B_m tends to (2/3)^7·(2/3), by the last bullet of section 4.

(2) Put v_n = F(n)(2/3)^n. The cylinders of the valid words of length n partition [0, 1), and a word in state a
has a cylinder of length c_a(2/3)^n, so

    Σ_(a=0..n) (2/3)^a c_a v_(n−a) = 1.

Also 0 ≤ v_n ≤ 1. Take L = 60, S = Σ_(a=1..60) (2/3)^a c_a = 0.934179624…, τ = 3(2/3)^61 ≥ Σ_(a>60) (2/3)^a c_a,
z = 1/(1 + S), and ε = 8.3·10^(−10). If z − ε ≤ v_i ≤ z + ε for the 60 values before n, then the identity gives
1 − (z + ε)S − τ ≤ v_n ≤ 1 − (z − ε)S, and both ends lie in [z − ε, z + ε] because ε ≥ τ/(1 − S) and 1 − zS = z.
The exact values of v_340, …, v_400 lie in that interval. So v_n lies in [0.517015062, 0.517015064] for every
n ≥ 340. For m > 400,

    27·F(m − 7)(2/3)^m = 27(2/3)^7 v_(m−7) ≥ 0.8170,     B_m (2/3)^m ≤ (3/2)(z + ε) + 3(2/3)^61 ≤ 0.7756,

using Σ over i ≥ 1 with d_i = 0 of (2/3)^i = 3/2. For 7 ≤ m ≤ 400 the exact integers give 27·F(m − 7) ≥ B_m
except at m = 9. With (1) this proves (2) for m ≥ 10 and for m = 7, 8. For 3 ≤ m ≤ 6 and m = 9 the values are
D/B = 1/2, 1/4, 1/6, 3/9 and 16/30. ∎

The onset is needed: D_1/B_1 = 0 and D_2/B_2 = 1, as GC2936 noted.

**Sharper constants (COMPUTED).** The same argument with suffix length k, every prefix state i, and the least
count lo_i(θ) of deaths over all rotations gives, for m ≥ k and θ = 3^(−(m−k)),

    Σ_i F(m − k − i)·lo_i(θ)  ≤  D_m  ≤  Σ_i F(m − k − i)·hi_i(θ),

and so D_m/B_m is eventually between L_k and 1 − L_k, with
L_k = min over θ of Σ_i (2/3)^i lo_i(θ) / (3/2)^(k+1). Forty states are carried; the rest get the trivial bound.

| k | full-state family | deaths, every prefix | L_k |
|---|---|---|---|
| 7 | 14 | 1 to 13 | 0.0392 |
| 9 | 30 | 1 to 29 | 0.0396 |
| 10 | 46 | 3 to 43 | 0.0518 |
| 12 | 100 | 10 to 90 | 0.0840 |
| 14 | 226 | 44 to 182 | 0.1639 |
| 15 | 338 | 77 to 261 | 0.2019 |
| 16 | 509 | 106 to 403 | 0.2122 |
| 17 | 763 | 171 to 592 | 0.2228 |

Since B_m/A(m) tends to 1/2, the share of valid words that pass the first check is eventually between
1 − 0.7772/2 = 0.611 and 1 − 0.2228/2 = 0.889.

The certified ranges are far wider than what actual prefixes show. At k = 10 the certificate allows 3 to 43
deaths of 46; every full prefix of length up to 12 gives 14 to 28. For 10 ≤ k ≤ 13 and k = 16, 17 the least
count of the full-state family sits in one nested class of total lengths, m ≡ −2622 modulo 2^(k−1).
The constants are rounded towards the weaker side throughout this report.

## 6. GC2936's lemma

R_m is the set of boundary words p of length m with u(p) < 1/4 whose start avoids the residue 1 − 2^m modulo 3.
GC2936 proves D_(m+1) ≥ |R_m| and B_(m+1) − D_(m+1) ≥ |R_m|, and asks for a positive density of R_m.

**Theorem B (Local; PROOF-SKETCH; the certificate was computed by hand).** For every m ≥ 6, |R_m| ≥ F(m − 6).

*Proof.* S_4 = {0001, 1001, 0101, 1010}, with N_4 = 8, 13, 6, 9. For the four powers 1, 3, 9, 11 of 3 modulo 16
the point sets are {6, 8, 9, 13}, {2, 7, 8, 11}, {1, 5, 6, 8}, {2, 3, 8, 15}, with cyclic gaps (2, 1, 4, 9),
(5, 1, 3, 7), (4, 1, 2, 9), (1, 5, 7, 3). Each has three gaps prime to 3. By the residue version of Lemma 1,
after every full prefix the four boundary words p″s take at least two residues modulo 3, so at least one avoids
any given residue. Take p″ = 00y with y full of length m − 6. Then u(p″s) < 2/9 < 1/4. ∎

So |R_m|/B_(m+1) has lower limit at least (2/3)^8, the same constant as in Theorem A. Longer suffixes give more:

| k | family | least number of gaps prime to 3 | starts guaranteed off any one residue |
|---|---|---|---|
| 4 | 4 | 3 | 1 |
| 6 | 9 | 5 | 2 |
| 8 | 20 | 9 | 6 |
| 10 | 46 | 21 | 18 |
| 12 | 100 | 50 | 44 |

At k = 12 this is |R_m| ≥ 44·F(m − 14), a lower limit of 0.067 for |R_m|/B_(m+1). The enumerated value at m = 21
is 1278/5804 = 0.22. Theorem A does not use the pairing, so it does not wait on Cloud's carry of GC2936 §3.

## 7. More forced bits (COMPUTED)

With j forced bits, take W to be the valid words of length k + j after a prefix in state i, and arcs of length
2^k in Z/2^(k+j). Summed over states as before, the share of valid words of length m whose start stays valid
through m + j is eventually inside:

| j | k = 7 | k = 10 | k = 13 | coin value |
|---|---|---|---|---|
| 1 | [0.5196, 0.9804] | [0.5259, 0.9741] | [0.5578, 0.9422] | 0.750 |
| 2 | [0.2118, 0.8756] | [0.2643, 0.8696] | [0.3401, 0.8227] | 0.563 |
| 3 | [0.0438, 0.8516] | [0.0865, 0.7427] | [0.1643, 0.7009] | 0.422 |

In the census's terms: the number of starts below 2^m that survive m + 3 steps is eventually at most 0.701·A(m).
That is a constant factor on the count of valid words, not a smaller exponent.

## 8. The unconditional check (COMPUTED)

O_w counts all n < 2^w with T^w(n) odd. Every prefix is allowed, so the family after a prefix is all 2^k words
and the set is Y_k = {n < 2^(k+1) : T^k(n) odd}. For every w ≥ k, O_w/2^w lies between the least and greatest
half-circle shares of θ·Y_k.

| k | least | greatest | O_w/2^w for every w ≥ k |
|---|---|---|---|
| 5 | 8 of 32 | 24 | [0.2500, 0.7500] |
| 8 | 79 of 256 | 177 | [0.3085, 0.6915] |
| 10 | 362 of 1024 | 662 | [0.3535, 0.6465] |
| 12 | 1523 of 4096 | 2573 | [0.3718, 0.6282] |
| 14 | 6527 of 16384 | 9857 | [0.3983, 0.6017] |
| 15 | 13600 of 32768 | 19168 | [0.4150, 0.5850] |

k = 5 gives GC2936 §2's constants again, by another route. The half-width falls by a factor of about 0.87 a
step from k = 10. For 9 ≤ k ≤ 13 the least count sits at the multiplier 3^(k−5): section 11 says why.
With two forced bits, each of the four forced pairs has share between 0.130 and 0.390 for every w ≥ 12.

## 9. Against the kit's theorem

`Rule30FirstChecks.first_check_balanced` bounds the share of the 2^n rows that pass the first check past the
free range between 1/40 and 39/40, for two of any three lengths. Its proof is an exact pair law between a
check and the check of the shifted word, and two linear inequalities.

Mahler's twin is the share of the A(m) valid starts that pass, 1 − D_m/A(m): between 0.611 and 0.889
eventually, and bounded on both sides at every length m ≥ 3 by Theorem A. The proof is different in kind. It uses neither H2 nor H5. It uses three things: free bits act on the state by a translation; the
admissible language restarts after a full word; and a finite table that is uniform in the hidden state.

Rule 30's F has the second and third in some form and not the first: adding a high bit to Y does not translate
F^ℓ(Y). So I see no direct return to Rule 30, and I say so plainly. The one thing that might go back is the
form of the argument: bound a check by a finite family after each restart, uniformly in what the prefix hides.

## 10. What the method cannot do

For k free bits and j forced bits, the arcs have length 2^k in a cycle of length 2^(k+j), and they cover it. The
valid set is never empty, so some arc always holds a survivor. The certified number of survivors per prefix is
therefore at least 1, whatever j is, and the bound on the survivors of a width never falls below F(m − k).
Extinction in a fixed range is a statement about the one arc that starts at 0. The certificate forgets that
the rotation comes from an integer prefix; it has to, since that is what makes it finite. It also gives no
smaller exponent than Flatto's: for j proportional to m it would need k proportional to m.

## 11. Why the constants converge slowly (HEURISTIC, not a proof)

*Tested the same day, L1669: [the sequel](LOCAL-MAHLER-FIRST-CHECK-LIMIT-20261112.md). The product formula is
exact and gives a proof that the unconditional share tends to 1/2. The steady factor guessed below was refuted:
the largest product falls in drops and plateaus. The text below is left as written.*

Three observations from the tables, and one reading.

1. **Small multipliers copy narrow windows.** With multiplier 3^j the family is the set of rationals v/3^j, v in
   a window of 2^k consecutive integers. After j steps these are integers again, in windows of length 2^(k−j)
   whose positions differ by at most (3/2)^j/2. While that is below 2^(k−j) the windows overlap, and the family
   inherits the bias of one narrow window. That is the multiplier 3^(k−5) in section 8.
2. **The forced bit is a binary digit.** For a word p of length m, the start r(p) is the first m binary digits
   of the 2-adic number −u(p), and the first forced parity is its next digit. H3 is the same fact.
3. **A cocycle.** Splitting the free bits as k_1 + k_2 writes the law of j forced bits after k_1 + k_2 free bits
   as a mixture, over the law of k_2 + j forced bits after k_1 free bits, of the laws of j forced bits after k_2.
   So a certificate is a bound on a contraction coefficient of a Markov kernel, and it improves with k only as
   fast as laws with many forced bits become uniform.

*Reading.* For the unconditional check the Fourier coefficients of the point set are Riesz products,
Π cos(π y_s), along orbits of the two-valued map y → 3y/2 or 3y/2 + 1/2 on the circle. The certified half-width
is then a largest value over about 2^k such products, a large-deviation quantity, which decays exponentially at
a small rate. The observed factor 0.87 a step fits that. A proof that O_w/2^w tends to 1/2 would be a bound on
these products for every branch sequence. The pure product, with no branch choice, is the Fourier transform of
the Bernoulli convolution of ratio 2/3, for which Kershner's 1936 argument gives a power of a logarithm. The
conditional case replaces the product by a renewal sum over the 3/2-shift, the shape of the characteristic
function Tao bounds for the Syracuse variables. I have read neither paper in full.

## 12. Checks and receipts

All runs on Local's M5 under `run_capped.py`: one Python process, CPU 600 s, wall 900 s, RSS 4096 MiB; each
COMPLETED. No start above 2^22 is enumerated, so the census is not enlarged. Raw receipts are outside git under
the run directories; the outputs are small and are in the repository.

| Run | Source (SHA256) | Output (SHA256) | Time |
|---|---|---|---|
| 1 | [`local_arc_certificate.py`](../tests/probes/mahler/local_arc_certificate.py) at `ee846fa5…` | [`…_run1.out`](../tests/probes/mahler/local_arc_certificate_run1.out) `83d0d5ef…` | 13 s |
| 2 | the same file at `090b6252…` | [`local_arc_certificate.out`](../tests/probes/mahler/local_arc_certificate.out) `c9e37963…` | 70 s |
| 3 | [`local_arc_unconditional.py`](../tests/probes/mahler/local_arc_unconditional.py) `2fa03c5c…` | [`local_arc_unconditional.out`](../tests/probes/mahler/local_arc_unconditional.out) `b1c2120e…` | 11 s |

Controls inside the runs:
- the slack rule, direct rational tail sums and the state automaton agree on every word up to length 14, and the
  counts equal the renewal formula and the census's A(1..10);
- N_12 and T^12 against a direct walk on every valid word of length 12;
- the fast arc routine equals the simple one for k ≤ 12;
- Cloud's B and D at w = 10, 14, 18, 22, and its list of O_w − 2^(w−1) for w = 2 to 20, are reproduced;
- every prefix family for k = 2 to 10 and every prefix of every length up to 22 − k, 45,161 families, lies
  inside its certified range, and the per-length inequality of section 5 holds for every m ≤ 22;
- |R_m| ≥ F(m − 6) and both of GC2936's pairing inequalities hold for m ≤ 22.

**Wolfram replay** ([`mahler_arc_certificate_replay.wl`](../tests/probes/wolfram/mahler_arc_certificate_replay.wl),
SHA256 `918cf85b…`). Other routes: validity by direct tail sums, starts by walking every n, arcs by cumulative
sums over every rotation. Equal to Python on every compared entry:
- section 6's table for k = 2 to 8;
- section 5's table for k = 4 to 10, with L_k as exact rationals (k = 7: 11074486528/3^24);
- section 7 at (j, k) = (2, 6) and (3, 5);
- section 8 for k = 2 to 11, and the forced pairs at k = 7, 8, 9;
- B and D at m = 10 and 14; the failure of 27·F(m − 7) ≥ B_m at m = 9 only, up to 400.

**Not replayed in a second language:** section 5 for k = 11 to 17, section 7 for k above 6, section 8 for
k = 12 to 15. Those rows are Python only.

In plain mathematics, what the tables say: for a finite set X of residues modulo 2^K and each power θ of 3,
slide a window of 2^k consecutive residues around the cycle and record the least and greatest number of points
of θX inside it.

## 13. Predictions and outcomes

All were pushed before the run they concern (L1667 and its two addenda).

| | Prediction | Outcome |
|---|---|---|
| P1 (0.9) | the residue certificate holds at k = 4 | **held** |
| P2 (0.85) | the half-circle certificate holds at some k ≤ 8 | **held**, k = 7 |
| P3 (0.6) | at k = 12 the certified interval is inside [0.25, 0.75] | **refuted**: [0.084, 0.916] |
| P4 (0.95) | enumeration reproduces Cloud's counts; every family in range | **held** |
| P5 (0.5) | two forced bits certify a share below 0.75 at k ≤ 12 | **refuted**: 0.841 |
| Q1 (0.75) | lower end at k = 17 between 0.22 and 0.32 | **held**, at 0.2228 |
| Q4 (0.7) | three forced bits at k = 13 between 0.70 and 0.72 | **held**: 0.7009 |
| U1 (0.6) | unconditional half-width at k = 12 at most 0.10 | **refuted**: 0.128 |
| U2 (0.5) | unconditional half-width at k = 14 at most 0.06 | **refuted**: 0.102 |

The explicit constants of Theorem A (2) were first seen in a smoke test, so they were observed and not
predicted. The four refutations share one cause, in section 11.

## 14. What carries the proof, for the second read

1. Lemma 1: the translation identity, and the step from "t < 2^k" to "an arc".
2. Section 4's two facts: a full prefix allows exactly the family S_k, and the families partition the boundary
   words. Both are standard, and are checked against tail sums.
3. Lemma 2 and Theorem B's four rows: finite tables. Theorem B's can be checked by hand in a few minutes.
4. The interval argument in Theorem A (2), and the identity it rests on.

## 15. Next

- The carrying read. Until then the theorems stay PROOF-SKETCH.
- Lemma 2 is a statement about 14 residues, 64 multipliers and 256 rotations, so a kernel check is possible.
  There is no place for it in the Rule 30 kit; I am not building it unasked.
- The limit 1/2 was open when this was written. For the unconditional check it is now a PROOF-SKETCH
  ([sequel](LOCAL-MAHLER-FIRST-CHECK-LIMIT-20261112.md), L1669); for the boundary share it is open, with one
  lemma named there.
- Cloud's two other directions, the odd-weight bound and the stripe rays, are untouched by this.
