# Mahler transfer review: a balanced first check, the right mass question, and stripe recharge

GPT, GC2936, 11 November 2026. Carrying read of Cloud CL781–CL782 at `070f5b5f1`.
The owner requested review of the new kit-to-Mahler programme. Cloud retains its three research
directions; Local owns Wolfram execution. Both schedules remain paused.

**Verdict.** H1–H5, the recognizable-ranking barrier and the planted-survivor construction carry,
at the scopes below. They are now **PROVED, two-party hand read**. The new arguments in sections
2–5 are **PROOF-SKETCH, GPT**, with exact finite self-checks; they await Cloud's carrying read.
Neither the hand read nor the computation proves Mahler's conjecture. No new Lean build was run.

## 1. What carries, and what needs correction

Use T(n) = ceil(3n/2), and chi_w(n) = T^w(n) mod 2 for 0 <= n < 2^w.
In H1–H5 take w >= 1 and set chi_0(0) = 0.

- **H1–H3 carry.** The complement, middle-third shift rule and least-residue formula are exact.
  H3 is the existing least-residue argument specialized to multiplication by 3 at every step.
- **H4 carries in its displayed form:** the number passing is at least A(w+1) - A(w).
  The resulting proportion tends to one half; it need not be at least one half at every width.
  A word permitting an appended 1 also permits 0, which proves the claim without a random model.
- **H5 carries.** Here p0 and p1 mean parity-word extensions, not ordinary binary concatenations.
  Their integer representatives are r and r + 2^(w-1), possibly in reversed order.
- **The recognizable barrier carries.** In Cloud's pigeonhole argument choose j1 and j2 large
  enough for the top window, with the repeated key occurring at distinct values of the unbounded
  nondecreasing lambda(j). Then choose L large enough for all zero runs to be beyond the monoid's
  preperiod and all compared iterates to remain in the valid stripe prefix. Equality of lengths
  follows from lambda(j2)-lambda(j1)=2e; the zero-run difference is 2e+j2-j1, a multiple of pi.
  The resulting chain is an infinite descent across different stripe truncations, not a cycle
  of T. A fixed residue modulo 3^a can be included by taking j1 >= a.
- **Planted-survivor items 1–3 carry, including the strict threshold.** For W >= 2L-1,
  psi_L^(-1)([1,2^W)) replaces t_ceil(W/2) by the stripe -1/3. The removed point has exactly
  2 ceil(W/2)+1 valid parities. Below that width threshold the bounded set is unchanged.

The following interpretations do not carry as written.

**Locality of the planted modification.** Put C_L = {x : x = t_L mod 4^L},
t_L=(4^L-1)/3. The disagreement set of T and T'=psi_L T psi_L^(-1) is exactly

    C_L union T^(-1)(C_L),

not C_L alone. Outside C_L the input is fixed, but output relabelling changes T(x) when it
enters C_L. Inside C_L the inverse changes bit 2L and preserves the odd class; both images
under T are even and thus fixed by psi_L, and odd-branch injectivity forces disagreement.
The two sets are disjoint and have natural density 1/4^L each. A small counterexample to
the original claim is L=2, x=3: T(3)=5 but T'(3)=21, although 3 is not 5 mod 16.
This sharpened exact-support statement is a new GPT sketch, pending Cloud.

**Count-based arguments.** The full tables differ by the proved extra one. They therefore can
distinguish the two maps. GC664 already makes eventual extinction in every bounded positive
range equivalent to Mahler. What the construction defeats is evidence from arbitrarily large
finite portions of the table, or estimates insensitive to one surviving row per width. It
does not exclude all counting proofs.

**Valuation ranks.** GC2342 defeats a uniform recharge bound based only on the episode clock,
phase and a fixed interruption. It explicitly leaves size/full-residue arguments open. The
recognizable barrier does not turn this into a theorem excluding all unbounded valuation ranks.

**Domain and chart.** T is injective on the ordinary integers, with image the residues 0 and 2
modulo 3; a backward orbit is unique when it exists. On Z_2 every y has two preimages,
2y/3 and (2y-1)/3. Only on N union {-1/3} is the added collision at 0 the unique one.
The inverse parity chart has a weighted-sum expression, but it is not linear in either of
the senses being compared. For ordinary binary-coded addition, Psi(2)=-2/9 differs from
2 Psi(1)=-2/3. For XOR, modulo 16 the singleton-bit images are 5 and 14, whose XOR is 11,
whereas the image of their XOR is -5/9 = 3 mod 16. The kit's `LinearCharts` uses pointwise
XOR over F_2. An explicit weighted sum does not dispose of a comparable rigidity question.

## 2. A two-sided bound for the unconditional first check

Let O_w count all n < 2^w with chi_w(n)=1, and put

    d_w = (2^w + 2(-1)^w)/3.

For every w >= 2,

    d_w <= O_w <= 2^w-d_w,
    1/4 <= O_w/2^w <= 3/4.

The sharper bounding proportions tend to 1/3 and 2/3. These are bounds, not the observed
limit 1/2, and they concern the whole free cube rather than the subset of valid words.

**Proof.** Set N=2^(w-1). T maps [0,2N) bijectively onto the numbers in [0,3N) whose residues
modulo 3 are 0 or 2. For each r<N exactly two of r, r+N, r+2N occur, since N is prime to 3.
If the two quotients include 1, H2 gives opposite checks and hence exactly one 1. There are
exactly d_w such r. Every remaining pair has quotients 0 and 2, so contributes zero or two.
More precisely,

    O_w = d_w + 2 #{r<N : r = 1-N mod 3 and chi_(w-1)(r)=1}.

This proves the inequalities and isolates the next residue-conditioned count. The constants
1/4 and 3/4 follow directly from the displayed d_w; w=1 must be excluded, since O_1=0.

## 3. The missing conditional bound has an explicit pairing target

A boundary word is valid but becomes invalid on appending 1. Let B_m count those words and
D_m those whose forced check is 1. A two-sided bound on D_m/B_m needs an onset:
D_1/B_1=0 and D_2/B_2=1. The unconditional theorem above supplies no such bound by itself.

Let R_m be the boundary words p of length m with zero-padded real value u(p)<1/4, whose
representative r<2^m avoids the residue 1-2^m modulo 3. Then

    D_(m+1) >= |R_m|,
    B_(m+1)-D_(m+1) >= |R_m|.

**Proof.** Both 0p and 1p are valid: the only extra tail to check for 1p is
1/3+(2/3)u(p)<1/2. Both remain boundary, because the invalid suffix p1 remains present.
Their two representatives are exactly the pair over T(n) mod 2^m=r. The avoided residue
ensures that this pair includes quotient 1, so H2 gives opposite checks. Different suffixes
give disjoint pairs. This proves both inequalities.

The real-value condition is automatic if p begins 00, since then u(p)<2/9. Thus the concrete
open lemma is: a fixed positive fraction of boundary words begin 00 and avoid that one
integer residue modulo 3, uniformly after an explicit onset. This is a **joint** real-slack
and integer-residue question. Neither separate marginal estimates nor a coin model prove it.
Positive control: p=001, r=4, u=4/27; starts 8 and 13 have codes 0001 and 1001 and next
states 41 and 68, hence opposite checks.

An exact state for a Wolfram symbolic attempt is available without a wider census. At length
w retain the representative r, state x=T^w(r), and integer slack a=M_w 2^(w+1), where
M_w is the minimum of (1/2-u_j)(3/2)^(w-j) over the current zero-padded tails j<w.
Use the capped empty convention M_0=1/2, a_0=1. To append parity b, let epsilon=(x mod 2) XOR b. Then

    r' = r + epsilon 2^w,
    x' = (3x + epsilon 3^(w+1) + b)/2,
    a' = min(3a, 3*2^w) - b*2^(w+1).

Appending 1 is allowed exactly when 3a>2^(w+1). The first two equations follow by the free-bit
translation identity; the last is G51's window update used by Cloud's probe. Retain r mod 3
and a prefix-00 tag to count the sufficient pairing set. For the full u<1/4 condition also
retain C, updated by C'=3C+b2^w, with u=C/3^w. Do not truncate x to its parity without a
congruence proof: at w=4, r=5 and r=8 both have r=2 mod 3 and odd x (27 and 41), but appending
0 gives x'=162 and 183. The beta-shift is nonsofic, so a finite-state closure is not automatic.

## 4. Conjecture S means weight, not width

The kit's `Rule30PeriodTwoMass.ConjS` is H+4 <= 7 wt(H,Y), where wt counts seed one-bits.
The Mahler census H*(w) about 2.4w instead uses bit length. It is not evidence for a literal
population-weight analogue.

Write tau(n) for the **first invalid prefix length**, with infinity if none exists. This is
one more than the last valid length. The proposed bound tau(n)<=c popcount(n)+d fails at
n=2^a: there are a initial zero parities. Even subtracting v_2(n) does not repair it.

**Explicit recharge family.** For any k>=3 choose L>=1 with

    27*9^L + 13 = 0 mod 2^(k+2).

This is possible because -13/27=1 mod 8 and 9 generates 1+8Z modulo every power of 2.
For completeness, v_2(9^(2^r)-1)=r+3 by induction using the factorization of a square minus
one; the resulting order and subgroup size are both 2^(m-3) modulo 2^m for m>=3.
For x=9^L the code begins 101. Its second odd state is m=T^2(x)=(9x+3)/4, and
3m+1=(27x+13)/4 has valuation at least k. Thus the valid prefix 1010^(k-1) has length k+2;
its largest zero-padded tail is 13/27<1/2. Therefore tau(9^L)>k+2. But

    T^(2L)(2^(2L))=9^L,
    tau(2^(2L))=2L+tau(9^L).

So tau(n)-v_2(n) is unbounded even at weight one. This is a proposed refutation with a full
hand argument, pending Cloud's carry; it is not a conjectural trend from a census.

**A repaired target.** Mahler is equivalent to the existence, for every s, of some finite B(s)
bounding tau(n) over all **odd positive** n with popcount(n)<=s. A linear B(s) would be a
stronger, genuinely S-type conjecture; no such linear bound is established here.

Proof of equivalence: the set of odd 2-adic integers with at most s set bits is compact and
consists entirely of positive ordinary integers. If valid-prefix horizons there were
unbounded, nested compactness would give a point in K, the closed admissible set. GC664's
half-boundary repair turns such a positive integer into a positive strict survivor after a
forward shift, contradicting Mahler. Conversely any positive survivor reaches an odd positive
integer after finitely many initial even steps; that odd integer has finite weight and
contradicts B(s). This reuses the known compactness and boundary-repair mechanism.

## 5. Stripe rays retain an arithmetic return state

For n=t_L+4^L v, with integers L>=1 and v>=0, put

    a=v_2(3v+1), K=2L+a, q=(3v+1)/2^a.

The initial code is 1 followed by K-1 zeros, and T^K(n)=3^(K-1)q. For K>=3,

    tau(n)=K+tau(3^(K-1)q).

Indeed, attaching 10^(K-1) before any valid tail creates no new obstruction:
1/3+(2/3)^K u < 13/27 < 1/2 for u<1/2 and K>=3; initial zero tails are harmless too.
An invalid tail remains invalid. For fixed v, increasing L by one multiplies the returned
odd state by 9. This arithmetic state must be retained; it is not the kit's finite clone state.

One fixed two-bit upper tail already has **unbounded extra lifetime**. Take v=2 and L>=2:

    n_L=(7*4^L-1)/3,
    T^(2L)(n_L)=7*3^(2L-1),
    k_L=v_2(7*9^L+1).

The k_L are unbounded because -1/7=1 mod 8 and the same subgroup calculation applies.
Whenever k_L>=k, the prefix 10^(2L-1)10^(k-1), of length 2L+k, is valid. Hence
tau(n_L)>2L+k whereas bitlength(n_L)=2L+2. Both the extra lifetime after the initial stripe
and tau(n_L)-bitlength(n_L) are unbounded on this single ray.

This defeats a uniform **additive** post-stripe deadline, including one depending only on
this fixed upper tail. It does not refute a multiplicative linear-in-width bound. Nor does
it classify all census survivors: the record already reports no common low-bit pattern among
record holders. A ray claim needs a specified return/phase normalization.

## 6. Provenance and exact self-check

Record searched: G50/G51, GC664 and its L363 carry, GC1221–GC1224, GC2342's recharge family,
the Mahler census/rung reports, CL781–CL782; current kit `lean/`, `equivalents/`, catalogues,
portal sources and relevant PRs. The explicit powers 27*9^L+13 and 7*9^L+1 and the pairing
above had no matching statement in the scoped record search. No broad novelty claim is made.

`known_find.py --new` completed at **2026-11-11T22:34:08Z**, kit
`6888b9bdd6242dd6fd458a97ebb514d6fbcdcbea`, portal snapshot `2026-11-11T22:33:56Z`, 15 open PRs.
Refresh output SHA256 `17a499bb367660a351c783e6b725a56ebd1781635ce52b37b796be39b10b5552`.
Read current FirstChecks, RecognizableBarrier, PlantedSurvivor, PeriodTwoMass and LinearCharts
statements and carrying arguments. Closed PR bodies, conversations, reviews and empty inline
comment lists were read separately for 209, 241, 260, 275, 288 and 289. Exact main-module heads:

| PR | Head | Module SHA256 |
|---|---|---|
| 209 | 89f0698f7050e5547128f35eca4fd034c119d6dd | 18a01ef281d8dda99d5a4358bcaa1e770b00cdada803a250ba688697b8c9f95b |
| 241 | cc4acee85a43bfaab82f1c604fd45d144cf7eeb8 | b7ecc429591d2bf1a1aebd0b22208be1d48fb7ab2a7032715753e048e9542a31 |
| 260 | b51eb348cecdf3d14eee8209a937f1417c1b6e38 | 372ad3943bf4d530752fe6b4bc77b7cbb70a149e19ae9a5d20931e9bbbf02730 |
| 275 | 80b7da43c7cd36ea31232df69d6e44959c95c0e8 | d038a98647bd6ef4ca4b5d916bf7d2deccbe1cc52b6b479e12733a2a90216adb |
| 288 | b42c8ea041f2b13608dc607bceb4ecb635e39a8f | ae18f8937cea5a262005084085c1187593622ef46260a12243e027468a5e1cdb |
| 289 | 55563892d539e05cbfd9cb5ebb4be561e3f7a527 | 768e67885b8901c198e341bd8b34e6a979eaa234ca116c0db1a1b0f6f15eb749 |

The later mass extensions leave ConjS's definition intact. PR288's exact threshold/parity
corollaries reinforce the finite-table qualification; PR289 does not exclude arbitrary
value-unbounded ranks. Existing portal packages are not recreated.

Primary literature checked: Andrieu–Eliahou–Vivion,
[A Normality Conjecture on Rational Base Number Systems](https://arxiv.org/html/2510.11723v1),
Conjecture 1.6 and Theorem 1.7. Equidistribution of positive T-orbits modulo all powers of 2
is a stronger open conjecture, not a theorem supplying the boundary-conditioned balance here.
The beta-shift/Flatto and GC664 mechanisms remain credited prior art.

The source [gpt_transfer_review_check.py](../tests/probes/mahler/gpt_transfer_review_check.py)
was frozen at `04b41395f` before execution, SHA256
`fb26559a3527900fc9176bf45c53bb97a6428a28ecf12307275995258266b4b0`.
Direct rational backward tail sums provide an oracle independent of Cloud's integer slack.
Cloud's int64 intermediates fit the declared width-26 range and its width-18 H3 check.
Its floating H4 diagnostic should become the exact comparison P1 >= A(w+1)-A(w) in a future
probe revision; the independent check here already uses integers.
All starts through width 10 pass H1–H3/H5 (H4 through width 9), the new unconditional recurrence and the sufficient
00-prefix pairing test. Planted inverses/support/range replacement pass for L=1..3 on the
declared small ranges. Both explicit recharge families pass for requested valuations 3..9,
and the exact stripe return identity passes for L=2..6, v=0..3. Negative controls reject the
one-class support and onset-free boundary-balance claims. These checks support the proofs;
they do not upgrade new hand deductions to two-party status.

Intel receipt: **PASS**, 0.321422 seconds aggregate CPU recorded, 0.15 seconds worker wall,
12,697,600 bytes maximum worker RSS; no pressure/thermal stop. GC2935 caps were CPU15s,
wall30s, tree RSS768MiB, max3 processes, file2MiB, stage8MiB, free floors4096/1024MiB,
swap-growth4096MiB, nice10. Raw data stay outside git. Shared-store pointer:
`cited/gc2936-mahler-transfer-review/out.txt`, SHA256
`ba07a83176b366b1d3328ae1161a85e7422f5821db7beae45c6d16b8489a85cf`.
Time receipt SHA256 `f93e4c6afa590ccf64f5508440e4ab6a76fbddf2bf4e40c80880f80b5c4d405e`;
aggregate monitor SHA256 `6713a371304fa696c10c2820858af324dfea72ee895ba5fa83bdde05363e1ad3`.

## 7. Handover

Cloud: please carry the pair-count proof and its boundary restriction, the odd-weight
compactness equivalence, and the two explicit recharge families with the tau convention.
The support correction also needs your read before being promoted beyond its checked counterexample.
Then the first research target is the density of R_m, with a modulus-dependent onset if needed.
Local's possible Wolfram task is symbolic transport of the exact joint state in section 3,
looking for an inequality or a finite certified decomposition; it is a proposal, not a
dispatched run or an authorization to enlarge the census. Full x/a ancestry stays intact.

The mass alternative is an odd-start bound B(s); the ray alternative retains q and the
multiplication-by-9 exponent. The fixed-tail v=2 family is a mandatory control for any
post-stripe deadline. P-A, lift persistence, P13/P14 and Collatz stay parked.

My own pull: the joint real-slack/modulo-3 pairing. It names exactly what must be controlled
to convert the new unconditional first-check theorem into the conditional theorem we want.
