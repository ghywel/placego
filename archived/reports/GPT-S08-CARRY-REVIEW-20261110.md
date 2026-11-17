# S-08: carry the hybrid classification and exact one-row plant, with their guards

GPT GC2804, 10 November. **Worker mathematical carrying read PASS with the repairs below;
new Lean uncompiled.** Independent fixed controls passed below.
Local retains module/build/Wolfram/posting ownership, after current S13/S12 work.

Read the full BR-3 report, BR3.1/3.2 claims and complete mathematical-skeptic reports/verdicts,
plus the relevant l2check/tl definitions. Source: immutable SW02-all archive c231157f…94c.
This carry is sections B and C only, not the width-exact twins, sharp-slack necessity, uniform
locality searches or other survey answers in the report. No prize conclusion follows.

## BR3.1: the alternating90/150 white-wall hybrid

On naturals, bit i represents depth i+1. Define H by

    H(Y)_i = Y_(i+1) XOR Y_(i-1) XOR [i even]Y_i,   Y_(-1)=0.

This is150 at odd physical depths and90 at even depths. The phase against the wall is part
of the theorem. “Shift invariant by2” describes the interior rule only: H does not commute
with shifting a finite row against a fixed wall. H(4)=14, while4H(1)=12.

For finite rows use symmetric Laurent polynomials in S, with A=S+S^-1. The Dickson relation
S^n+S^-n=D_n(A), D_(n+1)=A D_n+D_(n-1), gives a triangular degree-preserving bijection
between natural rows and A GF(2)[A]. Odd powers have odd spatial parity. Thus the row update
is L X=A X+X_odd and raises every nonzero degree by1. Write X=A a(T)+b(T), T=A^2;
physical rows have b(0)=0. The update on (a,b) is (a+b,T a).

**Essential domain repair.** Define the observation on *all* polynomial pairs, not just rows:

    c_s(a,b)=psi(U_(s+1)a+U_s b),
    U_0=0, U_1=1, U_(n+1)=U_n+T U_(n-1),
    psi(T^m)=1 exactly when m+1 is a power of2.

The psi formula is the binomial parity identity for the S^1 coefficient of A^(2m+1).
It gives psi(q)=q(0)+psi(Lambda q), where Lambda retains odd-index coefficients.
Let a_e,a_o and b_e,b_o be even/odd decimations. The **correct extended identity** is

    c_(2s)(a,b) = a(0) + [s>=1]b(0) + c_s(a_o, a_e+b_o).

All sums are in GF(2). The original version omitting b(0) is valid only for physical rows.
For a=0,b=1,s=1 the omitted version gives0 instead of1. The transformed object
Xhat=A a_o+(a_e+b_o) may have a constant term, so this extension is necessary.

Proof: U_(2s)=U_s^2 and U_(2s+1)=U_(s+1)^2+T U_s^2. Put
q=U_(s+1)(T^2)a+U_s(T^2)(T a+b). Its constant term is a(0)+[s>=1]b(0), and
Lambda(q)=U_(s+1)a_o+U_s(a_e+b_o). Applying psi gives the stated identity. These are finite
polynomial identities; the generating-series extension is not needed here.

If an extended polynomial Z has zero column for every s, then LZ is a physical row with
zero column. The triangular initial-bit/column map forces LZ=0. Since L raises nonzero
degree even on constant polynomials, Z=0. This is where the domain repair closes the
original proof. If a(0)=0 and all even observations are1, Xhat has all-ones column; then
(L+1)Xhat has zero column, impossible by the same degree argument. If a(0)=1, Xhat=0.
Consequently the immortal rows are exactly

    X=(A+A^2)p(A^4)+r(A^4),   p(0)=1, r(0)=0,

with finite polynomials p,r. Conversely this family makes Xhat=0 and all even observations1.
For width at most W>=2, independent coefficients give2^(floor(W/2)-1) rows. Width1 has none;
W>=2 is a real guard. In particular3 is immortal; widths<=6 give3,11,53,61.

Aperiodicity needs its own lemma: triangular trace injectivity applies to H, not by importing
the Rule30-specific free_not_eventuallyPeriodic unchanged. An eventual period of an immortal
row's odd-time word makes two different H^2-orbit rows have the same full column, since their
even entries are all1. Trace injectivity contradicts their widths differing by2P. This
carries the aperiodicity conclusion without transferring a theorem between systems.

## BR3.2: Rule30's exact table with one row added

Use the kit's actual F, with bit0 at physical depth1. Set theta_i=1 for even i and
u_m=(4^m-1)/3. For L>=1, Psi flips even bit i>=2L exactly when the *input* agrees with theta
below i. Prefix-triangularity makes Psi a tree automorphism, fixing bit0. Psi(theta)=u_L.
For every finite z, the first mismatch with theta occurs at finite a, so Psi(z) is finite;
the inverse of a natural is finite except at u_L, whose inverse is theta. Thus

    Psi(N union {theta})=N,   T_L=Psi F Psi^-1,

is a well-defined natural map with T_L(0)=0 and fixed row u_L. The restricted source domain is N union {theta}, not N: Psi is not a permutation of naturals. This is precisely how the extra natural survivor can appear under conjugation. This is not a local homogeneous
Rule30 CA: it is a different finite-state map on the same natural-row space.

The exact counting step is a set identity, not a numerical fit. If first mismatch a>=2L,
Psi(z)=u_L+2^a+(bits of z above a). Width changes only at z=u_m, m>=L, where it increases
by2. Hence, writing N_W for0<=Y<2^W,

    Psi^-1(N_W)=N_W                           if W<2L-1,
    Psi^-1(N_W)=(N_W minus {u_ceil(W/2)}) union {theta}   otherwise.

The theta column is all1. The kit's **trunc_survives at n=2m-1**, not pivot alone, says
u_m is black through2m-1 and first fails its even check at2m. Count survival through the
current tick *inclusively*. Therefore at every W and even t,

    S^T_W(t)=S^F_W(t)+[W>=2L-1 AND t>=2 ceil(W/2)].

The same observation convention extends to odd t by retaining the last even check. W=0
uses the first branch. No unknown Rule30 survival table entry is assumed.

Rule30 F-images have their top two bits11, whereas u_m has top10 (or is1). No finite row
maps to u_m. It follows that T_L raises width by1 except at u_L (change0) and
u_L+4^m, m>=L (change-1). The exact-width law is lost, visibly at the fixed point. Psi and
its inverse need only a counter to2L, a parity state and a prefix-match state; composition
with F gives a finite-state transducer with one-symbol lookahead.

The changed set is the cylinder C of theta-prefix length2L together with the even cylinder
in F^-1(C), of length2L+1. The odd preimage cylinder lies inside C. Their total Haar measure
is3*2^(-2L-1). A finite-state/triangular witness with the stated exact table identity is
additional content; the general use of conjugation is not claimed new.

## Riders to delete from a submission

- Do not claim the slack-one hypothesis is necessary. Slack at all but finitely many widths
  is a sufficient way to preserve specified upper estimates; tight positive bounds at
  unbounded widths are not covered by the purported dichotomy.
- Do not claim an unconditional immortal/nonimmortal pair with all the same width bounds.
  The unmodified Rule30 member is nonimmortal only if Q01 holds. Generic90/150 plants can
  raise width by3; for rule150 the input14 already gives that negative control.
- Do not attach one-cell translation invariance or the exact width-growth law to T_L.
- Do not transfer classification, trace injectivity or free-word theorems between H and F
  without the short generic lemmas above. Finite support is crucial in the degree argument.
- The width-exact twin construction, universal slack claims and full survivor census are
  not part of this carry.

## Search, validation and next action

Current source search: record BR3/planted; kit03a19bf6 lean/equivalents/catalogues,
portal10:53:59Z and20openPRs, known_find planted/relabel/hybrid. No matching statement was
located among those hits. CL752's rule210 analogue has a different rule/wall, and is known.
The hybrid90/150 object itself is standard; a primary literature search found finite
null-boundary90/150 models (e.g. [2022 primary paper, definitions](https://eprint.iacr.org/2022/041.pdf)).
Those have two fixed finite endpoints, unlike this finite-support half-line with growing
width. That comparison is not a blanket novelty certificate or a claim of priority.
Kit zrow_stripe, pivot, trunc_survives and top-bit lemmas were read at actual source and
are credited; they are inputs, not re-proved contributions.

[Fixed checker](../tests/probes/swarm/sw02/block10/s08_read_check.py): a,b<8 and s<=6 for the
extended identity, the physical family through width6/tick32, L1..3 exact table checks
W0..6/even t<=12, literal-cell F against the finite conjugation definitions, width/cylinder
checks below256. Predictions: all repaired assertions pass; missing b0, fixed-wall shift
commutation and generic plant width<=1 fail their negative controls. No producer imported,
no expanded census. Shared serial stage/resources are frozen in the S07 review/GC2804.
Local may formalize these repaired statements in distinct internal modules if useful;
GPT reads the exact Lean and release artifacts later. Build, essay/notebook and final release read remain; standing owner consent covers
posting/PR once those normal gates pass.


Freeze hashes: checker `edc6a658b7cc6204efff2a8c4edbc698a0f52f27aa356ebb72bb41e7021ccb9f`;
shared private plan `c58c5bff3639be1fc20d34831a1f8210208633cbc77efd22a49ddb3bb4469299`.
Grouped SKG5 prior-art verdicts read: the closing Rule90/150 nonimmortality comparison is
known, with Rule150's exact white-wall statement already in rule30-open `Rule150Descent`.
Credit it as context; it need not be re-proved inside the new hybrid module. The survey's
abstract conjugated-repeller door is an idea-level precursor to the plant, without its
exact counting identity; cite that method context without a priority claim.


## Outcome — GC2804

The single serial stage completed both frozen jobs,0.441115aggregateCPU including outer
monitor/0.54wall, no retry. S08's448extended-domain renormalization identities, exact
width6 family3/11/53/61,147table identities for L1..3/W0..6, inverse/cylinder/width checks
below256 all PASS. The missing-b0, fixed-wall shift and generic rule150width3 negatives
all reject the false riders. Child0.064483CPU/11,509,760bytes peakRSS. No live tree RSS
sample before completion; launchfree6334MiB/swapgrowth0, thermal controls normal, no job.
These are COMPUTED controls of the independently carried hand arguments, not Lean checks.
Both mathematical components may now proceed to Local's formalization with the stated repairs.


## L1632 shorter proof carried — GC2815 (10 November)

The decimation identity is correct on all extended polynomial pairs over GF(2), with T denoting multiplication by the polynomial variable. Write q_e and q_o for even/odd coefficient decimation. Then (Tq)_o=q_e and (Tq)_e=Tq_o. For P(a,b)=(a+b,Ta) and D(a,b)=(a_o,a_e+b_o), the two components of D(P²(a,b)) are respectively a_o+b_o+a_e and Ta_o, exactly P(D(a,b)). This is a **semiconjugacy**, not a conjugacy: D is not injective, for example D(0,1)=D(0,0). No inverse of D may be used.

Iterating gives D P^(2s)=P^s D. Apply psi(q)=q(0)+psi(q_o) to the first component of P^(2s)(a,b). Its constant is a(0) at s=0 and a(0)+b(0) at s>=1, since one P-step clears the second constant. This recovers the complete extended even-observation identity above, including the b(0) term. This carrying read is of Local's hand argument, not of its 20,000-pair random checks or the new width12 census. The physical Dickson bridge and extended observation injectivity still need their own formal source/read; semiconjugacy alone supplies neither. No additional research or census is requested during the delivery queue.
