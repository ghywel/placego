# The full threshold-change set has zero length — GC2495/2496

GPT, 3 November 2026. **PROOF-SKETCH awaiting carrying read.**
This is a specialization of classical beta-transformation measure
theory, with an explicit source/convention audit. It is not a new
ergodicity theorem, an ordinary-integer exclusion or a solution of Mahler.
No numerical experiment or new computation was run.

## 1. What is being measured

Use the carried weighted-tail language

`U_j(b)=(1/3)sum_(k>=0)b_(j+k)*(2/3)^k`,

`C_a={b : every U_j(b)<a}`, `0<a<1/2`.

E is the set of a where every increase changes C_a. Carried GC2485/L1392
identifies it exactly by

`a inE iff every G^j(2a)<=2a`,

with `G(x)=(3/2)*x-floor((3/2)*x)` on[0,1). The earlier direct
gap-word cover proved zero ordinary length below13/27, and carried
GC2490/L1395 gives nowhere density on the full interval. Neither of
those facts alone proves full-range zero length.

The claim here is `Leb(E)=0` throughout(0,1/2). Leb denotes ordinary
length, not a measure on binary histories, positive integers or 2-adic
codes. The only state/parameter conversion is the LINEAR relation X=2a.
No measure is pushed through the nonlinear theta coding.

## 2. Primary source and exact convention match

Brown and Yin,
[beta-transformation, invariant measure and uniform distribution](https://doi.org/10.1017/S1446788700036703),
J. Austral. Math. Soc. A66(1999),418–428, uses the map
`T_beta(x)=beta*x-floor(beta*x)` on[0,1). Its background on418–419
states ergodicity with an invariant probability having the same null
sets as ordinary length. Page421 gives its normalized Parry density

`rho_beta(x)=h_beta(x)/c_beta`,

`h_beta(x)=sum_(n>=0) beta^(-n)*1_[0,z_n)(x)`,

`c_beta=integral_0^1 h_beta(x) dx`.

The critical convention on420 is z_0=1,z_1=beta-floor(beta), with the
usual recursion thereafter. Only this background is imported, not its
separate numbered results. Printed418–421 were visually checked;
original Renyi/Parry proofs were not reread.

At beta=3/2 this is exactly G, including G(2/3)=0. It is NOT the
paper's other map S_beta, a normalized orbit sequence y_n, a random
beta map, or an extended greedy map on[0,2]. The critical z_0=1 is
used only in the density formula;1 is not added to G's state domain.

The n=0 density term is1 throughout[0,1). The positive geometric sum
is3, so, directly,

`1<=h<=3`, `1<=c<=3`, and `1/3<=rho<=3`.

Thus for every Borel set A,

`(1/3)*Leb(A)<=mu(A)<=3*Leb(A)`.

In particular all upper intervals(q,1) with q<1 have positive mu mass;
zero mu mass implies zero ordinary length. This explicitly checks the
direction of absolute continuity needed below.

The retained primary PDF has296783bytes, SHA256
`78360236e2be2d1230416097f68eb099d6f16a8ee6b45b10d904fd80281f2588`,
shared store `cited/gpt/gc2496-brown-yin-1999.pdf`.

## 3. A direct invariant-set proof

Fix0<q<1 and let

`B_q={x in[0,1) : G^n(x)<=q for every n>=0}`.

It is Borel, as a countable intersection of Borel preimages. Its forward
invariance gives `B_q subset G^(-1)(B_q)`. Therefore the preimages

`B_q subset G^(-1)B_q subset G^(-2)B_q subset ...`

are nested and have equal mu mass by invariance of mu. Let

`D_q=union_(k>=0) G^(-k)B_q`.

This is the set of states whose orbit eventually stays at most q.
The nesting makes `G^(-1)D_q=D_q` EXACTLY, and continuity of measure
from below gives `mu(D_q)=mu(B_q)`.

But B_q is contained in[0,q], so

`mu(B_q)<=1-mu((q,1))<=1-(1-q)/3<1`.

Ergodicity forces the exactly invariant D_q to have mass0 or1. The
strict upper bound excludes1. Consequently

`mu(D_q)=mu(B_q)=0`, and `Leb(D_q)=Leb(B_q)=0`.

This avoids relying on a silently different definition of invariance
modulo null sets. It needs no mixing rate, independence, finite escape
time bound or empirical frequency calculation.

For a inE, put X=2a<1. Its orbit never exceeds X. Choose any rational
q with X<q<1. Then X belongs to B_q. Hence

`2E subset union_(q rational,0<q<1) B_q`.

The union is countable and null, and the linear scaling by1/2
preserves null sets. Therefore **Leb(E)=0 on the full(0,1/2)**.

As a related standard consequence, the union of these D_q is precisely
the set of states with limsup G^n(x)<1. Thus almost every G-orbit has
limsup1. This is an almost-every-state statement, not a conclusion
about any specified arithmetic orbit.

## 4. A normalization identity for the full word bands

GC2494, now carried L1397, describes every nonzero flat component by
a unique strict-suffix word w with S_w<1/2. Its OPEN component is
(S_w,T_w); the complete constant-language interval is(S_w,T_w]. The
wording in L1397 joining these two notions must be read with this
endpoint distinction, as in the original carrying proof.

These countably many disjoint open components, together with(0,1/3),
are(0,1/2) minusE. By the nullity just proved, their total length is1/2.
The bottom zero-language component has length1/3. Therefore the exact
positive series identity is

`sum_(w inW) (T_w-S_w)=1/6`.

Here W is the FULL strict-suffix/sub-half word class of GC2494; no
extra cyclic rotations or nonprimitive repetitions are counted.
Using the carried endpoint identity gives equivalently

`sum_(w inW) (2/3)^(L_w-1)*(1-2S_w)=1/2`.

This is a global normalization for parameter widths. It is not a law
for how frequently an integer orbit visits a band, nor the sum for an
incomplete gap-only catalogue. No numerical summation was used as
evidence for the identity.
Widths in the doubled state coordinate X would instead sum to1/3;
the stated1/6 is explicitly in the original ceiling coordinate a.

## 5. What this adds and what remains arithmetic

The full formal change set is now, subject to this carrying read,
relatively closed, nowhere dense, without isolated points, and of zero
ordinary length. The word plateaus occupy full ordinary length. The
earlier explicit dimension bounds below13/27 remain valid, but zero
length does NOT supply a Hausdorff-dimension bound below1 globally.
No such global dimension conclusion is made here.

This does not improve a single ordinary-integer exclusion by itself.
The positive-integer code starts occupy a specified countable arithmetic
set; an ordinary-length-null exceptional set can contain that entire
set. The invariant probability here is on x=2U, not a proposed random
law for integer starts or for the original real Mahler parameter xi.
The old record's measure-versus-specified-orbit barrier applies exactly.

Also, pointwise fractional survival below1/2 may have supremum1/2.
Such histories are not controlled by the uniformly smaller ceilings
used to define the plateaus. The full Mahler question and G51's
integer realization condition remain open.

## 6. Review, retained evidence and next step

Record searched: GC2485/L1392, GC2490/L1394/L1395 and GC2494/L1397;
G50/G51 and the old wide survey's measure/individual barrier. The
ergodic+Mahler search used actual kit/portal c42f6e51/24PR snapshot
08:52:43Z. The source is known classical background, not a novelty
claim inferred from a negative keyword search.

L1397's complete hand review, complete_plateaus_check.py and all output
were read. Its random finite controls are not proofs of the general
claims, nor a new Intel replay. Component(S,T) and plateau(S,T] are
kept distinct. GC2494's mathematics is adopted PROVED hand/two-party;
the imported measure theorem and the new E/sum consequences here
remain PROOF-SKETCH until Local carries this source/convention and
invariant-set step.

Next executable step: test a periodic dominating word as a route to
an explicit Hausdorff-dimension bound on E below ANY fixed A<1/2.
Its Parry base gamma should be less than3/2; a verified asymptotic
prefix-count growth rate log(gamma) would give log(gamma)/log(3/2)<1
in the ACTUAL parameter metric. First prove the count/admissibility
statement and direct prefix cover, not dimension transfer through a
homeomorphism. An upper cover needs no lower separation bound. No global
dimension1 claim or larger word census is authorized by this hint.

Independent alternative: apply the EXISTING G50 moving-age height
filter to the newly constructed separated-block histories. Explicitly
distinguish deliberately oversized zero padding from minimal padding;
do not repackage that known filter as a new universal obstruction.

My own pull: a compact-range dimension bound would quantify how the
zero-length exceptional set thickens toward1/2, while the arithmetic
filter continues to decide which formal histories can be realized.
