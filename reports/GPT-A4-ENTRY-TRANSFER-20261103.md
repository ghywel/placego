# A4 entry transfer to arbitrary right tails — GC2532

GPT, 3 November 2026. **PROOF-SKETCH pending carrying read.** No new
simulation, certificate search, compilation or novelty claim. This applies
the known radius-one half-line agreement lemma to the two carried A4
entry certificates. It does not prove universal capture.

## Exact statement

Fix one of these backgrounds and its stated alignment. E(t,x) is the actual
whole-line periodic background, and G is Local's inserted-edge orbit:
initially E(0,x) for x<0, black at zero and white for x>0. Let H be any other
whole-line Rule 30 orbit. Assume **inclusive initial agreement**

`H(0,x) = G(0,x) for every integer x <= M`.

No restrictions are imposed on positions x>M. Then the following sufficient
cutoffs preserve the same checked entry and all subsequent anchored laws:

| Source namespace | Background/alignment | t0 | A0 | W | M = t0+A0+W |
|---|---|---:|---:|---:|---:|
| MovingWall / Ring57 |100100000, (0,0)|300|-72|24|252|
| MovingWall63 / Ring63 |1010000, (0,4)|300|-55|16|261|

For every t>=300 there is an anchor A_H(t), an intact half-line x<=A_H(t),
and a leftmost mismatch F_H(t) in (A_H(t),A_H(t)+W]. The same potential
bounds hold:

```
-14 <= 19(A_H+72)+5(t-300) <= 22   [Ring57];
-20 <=  9(A_H+55)+2(t-300) <=  4   [Ring63].
```

The derived front bounds are respectively

```
  5 <= 19(F_H+72)+5(t-300) <= 478;
-11 <=  9(F_H+55)+2(t-300) <= 148.
```

In particular F_H(t)/t tends to -5/19 or -2/9, for every such initial right
tail, including nonperiodic tails. There is no assertion of an exact front
recurrence or a fractional displacement at each individual tick.

## Proof, including the infinite half-line

For any two whole-line evolutions agreeing initially on x<=M, induction gives

`H(t,x)=G(t,x) whenever x+t<=M`.

At time t+1 a position satisfying x+t+1<=M has all three parents y=x-1,x,x+1
satisfying y+t<=M. Apply the induction hypothesis to the literal Rule 30
update. This proves the statement also at the inclusive boundary. It is
already `Rule30EtherEdgeZero.agree_cone` in PR104, not a new locality lemma.

At t0, every x<=A0+W satisfies x+t0<=M. Thus H and G have identical entire
half-lines through A0+W, not just identical strips. Transport Local's
`entry_inv` from G to H: the phase equalities and bit bound are unchanged;
all x<=A0 still equal E; the W actual strip bits are the same, with the same
non-reference strip, start lookup and zero potential.

Apply the carried generic `anchored` theorem to H, its Rule 30 law and that
entry. Its input at A_H+W+1 is the **actual H value at that tick**, which may
differ from G's. Closure checks both values, so the invariant and potential
identity hold along H's own path forever. Bounds on the closure potential
and the non-reference-mask witness give the displayed inequalities. There
are no mismatches to the left of A_H and at least one in the finite strip;
therefore a leftmost mismatch exists. Add P(F_H-A_H), between P and PW, to
get the scaled front bounds, then divide by t for the velocity limit.

We do **not** continue using the initial light-cone agreement forever. That
cone alone only protects x<=M-t, which eventually falls left faster than the
certified wall. It is entry into the all-input closure that supplies the
permanent continuation. H need not have the same post-entry anchor sequence,
front positions or potential values as G; the common bounds suffice.
Nothing here identifies first entry/capture times or all earlier ticks.

## What “finite shield” means, and does not mean

Only the *right* constraints are finite: with the periodic left half and
the black cell at zero fixed, one imposes 252 or 261 following white cells.
The left-half premise remains infinite. The result is not a finite-seed
statement and does not imply any centre-column prize claim. In fact replacing
the whole periodic left tail by white would leave mismatches with E
arbitrarily far left, so this definition of a leftmost mismatch would no
longer apply to that approximation.

In an ensemble that fixes that exact left half and black origin and chooses
the positive positions as independent fair bits, the guaranteed set has
probability at least 2^(-252) or 2^(-261). These are lower bounds from one
specified prefix, not basin measures or capture distributions. If the origin
is randomized too, include its required black bit and obtain 2^(-253) or
2^(-262). With the entire initial row chosen as independent fair bits, the
infinite periodic-left premise has probability zero. Do not transfer this
restricted-ensemble statement to a typical whole-line row or the single seed.
No independence assumption is used in the deterministic theorem.

## Cheap controls and the route around a coarse cutoff

The inclusive guard is essential for the general locality statement. On an
all-white background, place one initial black bit at M+1. Its left edge is
black at M+1-t (the kit's `Rule30Jen.cell_left_edge`, translated); the all-white
orbit stays white. Thus the generic guarantee x<=M-t cannot be enlarged by
one cell uniformly over all initial data. This does **not** prove either
specific cutoff 252/261 minimal: the actual gates can mask influences.

A later checkpoint along the same fixed-width anchor path cannot improve
this plain cone cutoff. Let K(t)=t+A(t)+W. Since each anchor increment is
0 or -1, K(t+1)-K(t) is 1 or 0. Hence K is nondecreasing. Extending the same
trajectory to a later time gives no smaller initial agreement requirement
by this argument. No later-horizon census is warranted for that purpose.

A concrete stronger route is the known A1/RootedFront method: propagate
sound partial information from a shorter prescribed right prefix, using
actual forced gate masks, and certify that every unknown completion enters
the A4 set. A single chosen trajectory's masking is not sufficient for that
universal claim. Another route is an earlier independently checked entry
or a smaller checked window. Each would require a new certificate and its
own frozen test, not automatic enlargement of the present run. The current
proof requires none of those optimizations.

## Exact source and prior-art scope

Record searched: record_find query
`entry.transfer|half.line.agree|arbitrary.right.tail|cone.*(252|261)|prefix.*shield`;
GC2412/GC2416 arbitrary-tail theorem (198), subsequent A1 RootedFront cutoff87;
actual PR104 head 12dc145efeb4307205c4c9ce3407cfeabbdef6d4, `Rule30EtherEdgeZero.agree_cone` and
`pinned_of_check_tail` complete proofs; actual current kit c42f6e51
Rule30Jen rule and left-edge statement. The former generic argument is known;
252/261 are applications of the new A4 entry parameters, not a new method.
Local owns A4 formalization/release, so no duplicate Lean module is started.

Carried A4 sources: MovingWall
c2b5a0f844bfa25952d9bcdf41cb273c5f3d020a63834fcb973430830dd60c0b,
MovingWall63
48ea26e3d39a5b454df66eb88c799e1f94a8855a0128dea524cf5fd514782dc9.
The generic closure/entry proofs were fully carried in GC2528; the explicit
front arithmetic was carried L1427. New transfer, ensemble qualifications
and later-checkpoint monotonicity above await an independent hand read.
No new official Check or public verification claim. External COMPLETE
13:15:12.187707Z remains current; no novelty/submission decision here.

**Next executable step:** carry the transport of the full inclusive half-line
and strip into `anchored`, and the nondecreasing K(t) obstruction. If a smaller
right prefix matters, specify an actual universal-completion certificate
before any search. Do not merely rerun the trajectory farther.
