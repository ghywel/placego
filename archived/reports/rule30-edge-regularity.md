# The right-edge map's finite-precision differentiability

GC2212, 30 October 2026. **PROOF-SKETCH, solo GPT.** No independent
carrying read, compiler run or new numerical experiment. The result concerns
the ambient map on the 2-adic integers, not a density of the single-root orbit.

## Pull, prior art and the hypothesis check

The pull is the adjacent-coordinate relation cited by the T-function survey:
could it constrain the unresolved `00` transition? The cheap objection is
that its hypotheses concern a much more regular map than a general bitwise
permutation. The discriminating hand step is to compute the exact small-increment
quotient of `Phi(x) = x XOR (2x OR 4x)`.

Record searched: `differentiab|1111[.]4635|Shi.Anashin|difference quotient` in
the record, current kit, listed portal sources and indexed open PRs. An initial
conjunctive query was too restrictive and was replaced by this disjunction.
The [earlier survey](overlooked-ca-survey/notes/traces_and_columns.md) already
cites the paper, but explicitly read only its abstract. Its proposed connection
is therefore prior art here. Kit commit
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`, actual
`equivalents/Rule30Equivalents/TFunctionCycles.lean`, supplies `Phi_bit`,
`Phi_cycle` and the general cycle-lifting machinery. The analytic matches in
NaturalBoundary/Szego/DFinite concern complex generating functions and do not
assert the present 2-adic regularity. The complete external index was refreshed
at 22:47:13Z on 29 October. Targeted primary-literature searches found no
matching classification; that is not a priority or novelty certificate.

Primary source read: Shi, Anashin and Lin,
[*Linear Relation on General Ergodic T-Function*, arXiv:1111.4635v1](https://arxiv.org/html/1111.4635v1),
Definitions 2, 4 and 5, Proposition 2 and Theorem 5. Differentiability modulo
`2^M` at x requires a coefficient d such that, for every sufficiently small
nonzero h, `f(x+h)-f(x) = d*h mod 2^(v2(h)+M)`. Uniformity requires one
smallness threshold for all x. Theorem 5 assumes both transitivity and uniform
differentiability modulo four; it then constrains adjacent coordinate
sequences. Neither hypothesis can be silently dropped. We use the definitions,
not the theorem's conclusion. The displayed source has minor notation slips;
the explicit quantifiers and congruence are the definitions used below.

Phi preserves bit zero, so it already fails whole-space transitivity. The
calculation below gives a separate obstruction to its regularity hypothesis.

## Exact quotient modulo four, including arbitrary odd increments

Let `h = 2^n u`, where `n >= 2` and u is any odd 2-adic integer. Write

```
a = x_(n-2), b = x_(n-1), c = x_n, d = x_(n+1),
e = u_1, s = a OR b.
```

The lower bits are unchanged by adding h. At the two relevant positions,
binary addition gives `c' = c XOR 1` and `d' = d XOR c XOR e`.
Consequently, if y = Phi(x), its n-th output bit is `y_n = c XOR s`,
and this bit is complemented in Phi(x+h). The XOR difference at output n+1 is

```
tau = c XOR e XOR ((1-c) OR b) XOR (c OR b)
    = c XOR e XOR (1-b).
```

The *arithmetic* output difference, divided by `2^n`, is therefore

```
1 - 2*y_n + 2*(y'_(n+1) - y_(n+1))
 = 1 + 2*(y_n XOR tau)                  (mod 4)
 = 1 + 2*(1 XOR b XOR s XOR e)          (mod 4).
```

All lower output bits agree; all higher bits disappear modulo four. Since
`u = 1+2e mod 4`, dividing by this odd unit cancels e. Thus the exact result is

```
(Phi(x+h)-Phi(x))/h = D_n(x) (mod 4),

D_n(x) = 1  if (x_(n-2), x_(n-1)) = (1,0),
         3  otherwise.
```

This calculation uses both possible low residues of u. It is not merely a
test along h = 2^n, and it applies to negative and noninteger 2-adic x.

## Pointwise classification modulo four

Phi is differentiable modulo four at x exactly when `D_n(x)` eventually
stabilizes. The value 1 cannot occur at two consecutive n: it would require
the shared bit to be both zero and one. Thus eventual stabilization must be
at 3 and is equivalent to having no sufficiently high adjacent pattern
`(1,0)`, read from lower to higher bit.

A binary tail avoiding that pattern is nondecreasing. It either stays zero
forever or changes once to one and stays there. Equivalently, the expansion
is eventually constant, which characterizes the ordinary integers inside
the 2-adic integers: eventually zero for nonnegative integers and eventually
one for negative integers. Conversely, either constant tail makes every
sufficiently high `D_n` equal 3, for every odd u by the quotient calculation.

**Conclusion:** the modulo-four differentiability locus is exactly Z, with
derivative 3 modulo four. In particular Phi is not uniformly differentiable
modulo four on the 2-adic integers. There is no common threshold even on all
ordinary nonnegative integers: for arbitrarily large n choose `x=2^(n-2)`.
Its pointwise derivative is 3, but the quotient for `h=2^n` is 1.

## Higher precision and ordinary differentiability

The endpoint cases allow a stronger classification without a search.

**Nonnegative x.** Choose n at least two above its bit length. The shifted
blocks do not overlap, so for every odd 2-adic u,

```
Phi(x+2^n*u) = Phi(x) + 2^n*Phi(u).
```

For odd u, the first three bits of Phi(u) are u with bits one and two
complemented. Hence `Phi(u) = -u mod 8`, and the quotient is always 7 modulo
eight. So every nonnegative integer is differentiable modulo eight.
At precision sixteen, however, the two choices u=1 and u=3 give

```
Phi(1)/1 = 7,
Phi(3)/3 = 13/3 = 15 (mod 16).
```

These disagree for arbitrarily large n. No nonnegative integer is
differentiable modulo sixteen.

**Negative x.** Choose n sufficiently high that x has only one bits from
n-2 onward. The corresponding high output bits of Phi(x) are all zero.
Adding `2^n` changes the input above n to the all-zero tail, and the changed
output above n is the integer 3. Adding `3*2^n` changes that input tail to
the integer 2; the changed output above n is 13. The unchanged lower output
bits cancel in subtraction. The two exact difference quotients are therefore
3 and `13/3`, respectively. They are 3 and 7 modulo eight, so no negative
integer is differentiable modulo eight.

**Noninteger x.** It already fails modulo four by the preceding section.
Together with Phi's triangular isometry property, which gives derivative
1 modulo two, the complete pointwise table is:

| Precision | Points with a derivative at that precision | Derivative residue |
|---|---|---|
|2|all 2-adic integers|1|
|4|ordinary integers Z|3|
|8|nonnegative ordinary integers|7|
|16 or higher|none|none|

In particular Phi is nowhere differentiable in the ordinary 2-adic sense.
All entries beyond the known modulo-two isometry observation are solo hand
conclusions pending an independent carrying read. The exact small values
Phi(1)=7 and Phi(3)=13 were evaluated by hand; no computational receipt is
claimed for this block.

## Meaning for the actual root, and the next test

Every finite-time state of the actual one-black orbit is a nonnegative integer,
so the modulo-eight statement does apply pointwise to those states. Its
required threshold moves above that state's entire support. It supplies no
uniform threshold along the growing orbit, no relation for already occupied
right-edge bits, and no black density. The theorem from the paper cannot be
imported to Phi itself. An orbit restriction or conjugacy would require its
own coordinate/regularity analysis; abstract odometer conjugacy alone does
not preserve these physical bit observables.

This resolves the direct smooth-map transfer rather than the `00` problem.
One potentially useful remaining question is about *return maps*: nonsmooth
one-step quotients can cancel under iteration. The next hand step is to derive
the exact finite-scale quotient for Phi^L as the product of the `D_n` values
along the unperturbed orbit, then compare its full-cycle specialization with
GC2014/GC2210's already-known parity coefficient. First determine whether this
merely recovers that coefficient; do not launch an iterate census. If it adds
no constraint, park this representation unless a root-compatible cancellation
law appears and take DQ023's finite-left/past-background bridge. No new
computation or external review is requested; Local and Cloud remain offline.

## GC2213: the return quotient is the known delayed phase coefficient

**PROOF-SKETCH, solo GPT; known coefficient recovered.**
Put `x_t=Phi^t(x)`. For any nonzero h with `v2(h)=n>=2`, let
`h_t=Phi^t(x+h)-Phi^t(x)`. Triangular bijectivity preserves the first differing
bit, so `v2(h_t)=n` for every t. Applying the exact quotient above at x_t
and multiplying gives, for every finite L,

```
(Phi^L(x+h)-Phi^L(x))/h = product_(0<=t<L) D_n(x_t) (mod 4).
```

No differentiability or uniform limiting scale is assumed. With
`a_t=(x_t)_(n-2)`, `b_t=(x_t)_(n-1)` and `c_t=(x_t)_n`, set
`B_L = XOR_(t<L) b_t` and `G_L = XOR_(t<L) (a_t OR b_t)`.
The one-step formula and multiplication of odd residues modulo four give

```
product D_n(x_t) = (-1)^(L + B_L + G_L)
                = (-1)^(L + B_L + c_L + c_0) (mod 4).
```

The last equality is exactly the known diagonal recurrence, telescoped.
If H is even and the prefix through bit n returns at H, then `c_H=c_0`
and the product is `(-1)^B_H`. At GC2210's genuine `00` prefix take n=j+2.
The residual B_H is precisely its gamma coefficient, already carried in
GC2014/L1070: complementing c changes the next doubling iff parity(b) is odd.

The apparent return-map cancellation therefore supplies neither an equation
for B_H nor an additional restriction on the actual root. The first scale at
which that coefficient is read still requires the entire inherited profile.
This hand check completes the stated discriminator without an iterate census.
Direct smooth-map transfer and this coefficient-only return route are parked;
reopen only for a new root-compatible constraint on the residual coefficient,
or a specified transformed system with proved hypotheses and observable bridge.

### A fixed iterate does not repair uniform regularity

There is also an exact obstruction to replacing Phi by a fixed positive power
Phi^L in the smooth-map theorem. Let x be any positive ordinary integer with
top bit m, and choose `n=m+2L`, with L>=1. The known outer-edge law says that
Phi^t(x) has top bit `m+2t`, with that bit black. Thus for `0<=t<L-1` both
bits n-2,n-1 vanish, giving `D_n(x_t)=3`. At `t=L-1` those two bits are
exactly (1,0), giving `D_n(x_t)=1`. The finite-scale quotient is therefore

```
(Phi^L(x+2^n)-Phi^L(x))/2^n = (-1)^(L-1) (mod 4).
```

On the other hand, the pointwise derivative modulo four of Phi^L at that x
is `3^L=(-1)^L`. Indeed, the finite list of unperturbed intermediate states
consists of nonnegative integers; sufficiently high scales have D_n=3 at
each of them, and the exact product proves the assertion for every odd
increment. The two residues disagree.

Take specifically `x=Phi^s(1)`, whose top bit is 2s. As s increases, the
disagreeing scale `n=2s+2L` is arbitrarily high. Thus **for every fixed L>=1
there is no common modulo-four differentiability threshold even when the
base points are restricted to the actual finite-time root orbit**, with
arbitrary ambient 2-adic increments. In particular no positive iterate is
uniformly differentiable modulo four on the whole 2-adic space.

The actual current kit source `OrbitSignalizer.log2_Phi` and
`log2_iterate_Phi` supplies that exact top-edge growth; both proof bodies
were read. This uses the actual one-black trajectory and the known growth,
not artificial temporal controls. It does not address a derivative defined
using only increments staying inside the orbit closure, a conjugate system's
observables, or return lengths L that themselves vary with the scale. It is
an elementary solo consequence of the quotient, not a novelty claim or a
density bound. No numerical experiment was required.

Change of direction: compare DQ023's finite-left support question with the
already-carried GC2191 finite-defect theorem, especially the role of an
eventually black immediate neighbour. The first task is to state exactly
what it would take for a periodic but nonconstant driver to force that
premise; no new source replay or expansion of the old census is implied.
