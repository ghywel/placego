# Finite mass, run structure and one-step ancestry

GC2296, 30 October 2026. **PROOF-SKETCH: solo hand argument, independent
carrying read pending.** No dynamics enumeration or compiler run. This is
outside Package B's current submission scope.

## Pull and cheap objection

GC2289 and GC2291 classify three- and four-black targets, yet their parents
can be arbitrarily heavy. The curiosity is whether the parent's run structure
supplies a useful invariant without another mass-by-mass census. A successful
identity would organize all fixed masses at once. A monotone run count is an
immediate objection: the finite word `1001` evolves to `111111`, so two runs
can become one. That proposed monotonicity is REFUTED, not a new resource.

Record searched: GC2289/GC2291, PROOFS section25 (L215/GC353), GC2238's
cyclic OR run law; actual kit lean/equivalents/catalogues at
`a6399ef15ff409d4dc0c5feb119b289aa31588a4`, the complete21:03 external index,
then unchanged21:44:30 refresh (69 portal entries,17 open PRs). The relevant
PR50 source at `666ee9bfa172034da03313d71b873695ba4b182d` defines
`source_bit_correction`, `changes_telescopes` and `pulse_source_weight`;
portal `R30-20261029-a94f21` contains that temporal pulse-source law. Its
cyclic carrier and prescribed pulse differ from this physical finite-row
image; the common Boolean counting algebra is credited. The actual source
and its hypotheses were read, not equated by the word “weight”.

Primary background includes Wajnberg's2005 [single-seed run counts,
OEIS A110266](https://oeis.org/A110266), and Karttunen's2016
[finite Rule30 integer map, A269160](https://oeis.org/A269160).
The latter explicitly gives the Boolean map, injectivity and width growth.
The elementary counting argument below uses those known objects and standard
compositions. Searches do not establish priority; this is not a novelty or
submission disposition. No paywalled source is needed.

## Exact population identity

Let x be a nonzero finite row on the integer line, with white exterior. Write
W for its number of black cells, r>=1 for its maximal black runs, s for its
internal white gaps of length1, and h for its internal white gaps of length
at least2. Thus s+h=r-1. Let F be physical Rule30,
`F(x)_i = x_(i-1) XOR (x_i OR x_(i+1))`.

Then the number K of black cells in F(x) is exactly

```text
K = 3r - 2s = r + 2 + 2h.
```

Proof: put a_i=x_(i-1), b_i=x_i OR x_(i+1). There are W true a's.
Extending each black run one site to its left shows there are W+r true b's;
even a one-cell gap leaves those extended intervals disjoint. The number of
simultaneously true a_i and b_i is W-r+s. Indeed, label the black site j=i-1.
Every black site except a run's final site has x_(j+1)=1, contributing W-r.
A final site contributes precisely when the next run starts at j+2, adding
one for each one-cell white gap. These cases are disjoint and exhaustive.
Summing the Boolean identity `a XOR b = a+b-2ab` gives the formula.

Consequently a K-black target with a finite parent has a parent with
`ceil(K/3) <= r <= K-2`, `r = K (mod2)`, and `h=(K-r-2)/2`.
At K=3 the parent is a solid interval; at K=4 it has exactly two black runs
and one single-cell gap, recovering the earlier starting shapes. At K=5 it
has exactly three black runs separated by single-cell gaps. This last fact
is only a parent-shape statement, not a five-black age classification.

Hand controls: every nonempty solid block has a three-black image;
`101 -> 11011` has K=4; `1001 -> 111111` has K=6. The second formula excludes
the zero row: using r=h=0 in r+2+2h would be wrong. The first formula does
extend to zero if r=s=0.

## Count all finite-parent targets at fixed width and mass

Normalize nonzero rows by placing their leftmost black cell at0. Let c(w,K)
be the number of width-w normalized words with K black cells that have a
nonzero finite physical parent. The known finite injectivity and endpoint
growth give a bijection from normalized parents of width n=w-2 onto these
targets, after shifting the image one site right. No multiplicity of parents
is counted, and no arbitrary infinite parent is included.

Fix r and h. Choose the h long gaps among the r-1 internal gaps in
`binom(r-1,h)` ways. The shortest such parent has length `2r-1+h`: each black
run has one cell, each short gap one, each long gap two. Extra length is
distributed over r black runs and h long gaps, giving
`binom(n-r,r+h-1)` possibilities when n>=2r-1+h. The exact count is therefore

```text
c(w,K) = sum binom(r-1,h) * binom(w-2-r,r+h-1),
  over r>=1, 0<=h<=r-1, r+2+2h=K, w>=2r+1+h.
```

An empty sum is zero. Equivalently, with z marking target width and u its
black population, the formal generating function is

```text
sum c(w,K) z^w u^K
  = z^3 u^3 (1-z) / ((1-z)^2 - u z^2 (1-z) - u^3 z^3).
```

To derive it, each positive black run has width series z/(1-z). The first
run supplies u^3; each additional run with its preceding gap supplies
`u * z/(1-z) * (z + u^2*z^2/(1-z))`. Sum this geometric series and multiply
by z^2 for the two new support endpoints. This is a formal series identity,
not an independence model or a measured distribution.

Two independent algebraic checks: at u=1 it becomes
`z^3*(1-z)/(1-2z)`, recovering the known parent counts1at width3 and
2^(w-4) for w>=4. At K=3 the coefficient is1for every w>=3; at K=4 it is
w-4 for w>=5. The long-gap endpoint K=w=6 gives exactly one target,
`111111`, from `1001`; this checks the gap-length threshold and support shift.

## A fixed-mass asymptotic, with the ensemble explicit

Fix K>=3. The h=0 term has r=K-2 and is
`binom(w-K,K-3)`. Every h>=1 term has degree K-3-h in w. Thus

```text
c(w,K) ~ w^(K-3)/(K-3)!,
c(w,K) / binom(w-2,K-2) ~ (K-2)/w.
```

The denominator counts all normalized width-w words with exactly K black
cells. Therefore the proportion of that ensemble having even one finite
parent tends to zero, for every fixed mass K. At K=1or2 there is no finite
parent at all. This extends the earlier small-mass observation without
classifying their longer pasts.

It does **not** bound the maximum ancestral age at fixed K, prove that the
mean age tends to zero, or describe the distribution of any actual orbit.
A vanishing fraction can still contain long histories. Nor does K=r+2+2h
close under a second inverse step: it loses the ordered lengths and residues
that governed GC2291's deeper branches.

Next executable curiosity step: inspect whether the inverse pair monoid can
retain a finite set of ordered run-length residues sufficient for a second
step at symbolic width. Do not start a larger mass/width census. If it needs
unbounded unreduced lengths, record that precise obstruction and switch to
the independent period-reflection lead. Simple mass or run monotonicity is
parked unless a different, explicitly proved resource reopens it.
