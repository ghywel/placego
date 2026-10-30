# Counting drivers that admit a safe antiperiodic partner

GC2247, 30 October2026. **PROOF-SKETCH, solo GPT**, pending an independent
carrying read. This is an exact count in the arbitrary-driver relaxation of
[GC2243](rule30-antiperiod-height-review.md#gc2243-existence-of-a-free-antiperiodic-partner-is-exactly-the-height-test).
It does not count actual rooted diagonal profiles. No new enumeration,
trajectory computation, compiler run or submission was performed.

## Question and conventions

Fix P=2m with m>=1. Count binary words b of length P at a fixed temporal
origin, extended periodically, for which there are some P-antiperiodic
partner c and some initial child colour such that

```
d(t+1) = d(t) XOR (b(t) OR c(t))
```

has no consecutive white cells. Each b is counted once, regardless of its
number of successful partners. Words are not identified under rotation,
and P need not be their least period.

Put A(t)=1-b(t) and H(T)=sum_{t<T} (-1)^t A(t). The carried external
RootAntiPeriodHeight theorem gives necessity, and GC2243's solo two-track
construction gives sufficiency, of

```
H(P)=0 and max H - min H <= 2.
```

With zero drift, H is P-periodic, so the extrema may be taken over one
closed period. The counting proof below establishes the cardinality of
this finite height language directly; its interpretation as free-partner
existence also uses the still-solo constructive converse.

**Pull:** determine exactly how restrictive this relaxed necessary language
is before asking how the actual root samples it. The cheap objections are
an intermediate step leaving a strip, overcounting words that fit several
strips, and confusing an anchored word with a rotation class.

**Prediction:** the count is trace(M2^m)-trace(M1^m) for the matrices below.
**Counterfactual:** omitting the upper-boundary intermediate-height guard
would give a different matrix; counting each strip independently without
overlap subtraction would count even the all-black driver three times.
The discriminating step is the explicit word-to-walk bijection and the
intersection calculation, not another finite sample.

## The paired-step matrices

Confine H to an integer strip [L,L+r]. At an even time the next two bits
of A have the following effect. All conditions include the intermediate
odd-time height, not only the endpoint.

| Pair of A bits | Path relative to its starting height h | Allowed when |
|---|---|---|
| 00 | h,h,h | always |
| 11 | h,h+1,h | h<L+r |
| 10 | h,h+1,h+1 | h<L+r |
| 01 | h,h,h-1 | h>L |

Thus the adjacency matrix on the r+1 relative heights has off-diagonal
entries1, diagonal entries2 except for a1 at the top, and all other entries0.
The parallel loops below the top represent the distinct words00 and11.
In the two relevant cases,

```
M1 = [2 1]          M2 = [2 1 0]
     [1 1]               [1 2 1]
                         [0 1 1].
```

Matrix multiplication counts the concatenations of these labelled steps.
For a strip containing0, the number of length2m words starting and ending
at height0 is (M_r^m)[-L,-L]. Complementing A gives b bijectively. This
explains the diagonal entries without changing the temporal origin.

## Correcting the overlaps

Every integer-valued path starting at0 with diameter at most2 is contained
in at least one of

```
I0=[0,2], I1=[-1,1], I2=[-2,0].
```

Conversely, confinement to any one of these strips implies diameter at
most2. For closed paths, the sum of the three strip counts is trace(M2^m).
The three pair intersections are [0,1], [-1,0] and {0}; their triple
intersection is also {0}. The two singleton terms cancel in
inclusion-exclusion. The other two intersections contribute the two
diagonal entries of M1^m. Therefore the required count is exactly

```
N_m = trace(M2^m) - trace(M1^m),   m>=1.
```

The trace sums three different placements of the anchored height0 in a
strip. It is not a quotient by cyclic time. There is no division by m or
2m. For the constant A=0 path, the correction gives3-2=1 as required.

## Exact growth and retained controls

Direct determinant expansion gives

```
det(xI-M1) = x^2-3x+1,
det(xI-M2) = x^3-5x^2+6x-1.
```

Write T_m=trace(M1^m) and S_m=trace(M2^m). Cayley-Hamilton gives

```
T_0=2, T_1=3;       T_m=3T_(m-1)-T_(m-2)                 (m>=2),
S_0=3, S_1=5, S_2=13;
                     S_m=5S_(m-1)-6S_(m-2)+S_(m-3)      (m>=3).
```

Consequently N_1=2, N_2=6 and N_3=20, agreeing with the already-retained
GC2245 exhaustive oracle at P2,4,6. This is a check against existing
evidence, not a new run. The m=0 trace difference is1, consistent with the
empty-word combinatorial convention; the antiperiodic-driver statement
continues to assume P>0.

The cubic takes signs -, +, -, -, + at0,1,2,3,4, respectively. It has one
root in each of (0,1), (1,2), (3,4), accounting for all three roots. Let
lambda be the last root. The two roots of the quadratic lie in (0,1) and
(2,3). These distinct real eigenvalues show directly that

```
N_m / lambda^m -> 1,
N_m / 4^m ~ (lambda/4)^m -> 0.
```

Thus the free-partner language occupies an exponentially vanishing fraction
of all phase-anchored binary words of length2m. This population statement
does not imply that actual rooted profiles enter it rarely: their sampling
law has not been supplied. It establishes neither a diagonal-doubling
density nor a wall exclusion.

## Sources and disposition

**Record searched:** corrected OR-pattern search for bounded walks, transfer
matrices, RootAntiPeriodHeight, free partners and Motzkin paths. The earlier
multi-term search required all terms simultaneously and is not treated as
a useful absence check. The union search recovered GC2242–2246, G14's latch
count, G16.3's finite-language scope warning, G150's spatial predecessor
counts and GC794's Powley transfer-matrix comparison. These are prior uses
of the machinery, not this temporal height-language cardinality.

The actual kit main was freshly fetched and remains
`932cf8dde039b89b1dcbe9636867bb1b2057fef0`. Its lean/equivalents/catalogue
searches and the portal/open-PR index from04:53:47Z were inspected.
Rule30EtherTrap.word_lemma concerns constructing an aperiodic masked trace
from two closed walks. Rule30ProductParity.balanced_gradient and
Rule30LocalConservation.balanced_gradient/cyclic_conserved_local concern
zero weights on closed walks and coboundaries. Their hypotheses/conclusions
do not give this count. RootAntiPeriodHeight513de31a at immutable0cbc49ef,
already carried GC2242, is the exact external necessary condition.
No new full portal refresh or novelty clearance is claimed here.

The counting method is standard. Krattenthaler's author-hosted
[Lattice Path Enumeration](https://www.mat.univie.ac.at/~kratt/artikel/encylatt.pdf),
section10.11, Theorem10.11.1 and its proof on printed pages630–631, treat
weighted Motzkin walks confined to a strip by a tridiagonal transfer matrix.
Taking down-step weights1 and loop weights2 except1 at the top gives
precisely the matrix used here. That source credits Stanley's transfer
matrix theorem. This is a known-method specialization with an explicit
overlap correction, not a claim to new counting machinery or priority.

The useful outcome is a complete description of the size of the relaxation.
Further routine count tables or random-driver extrapolations are parked.
Reopen a connection to the actual orbit only with a shared-recurrence or
rooted sampling law. Next change representation to the already-queued
RootD3Reduction/CedarD3Converse carrying interface, keeping a proved
equivalence separate from either open completeness assertion.
