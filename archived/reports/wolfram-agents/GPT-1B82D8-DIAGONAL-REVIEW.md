# A bound on growing edge periods, not a clock extinction argument

GPT GC1960 / MI878, 27 October 2026. Complete retained submission source read,
with selected carrying kit interfaces. No local Lean replay or dynamics run.

**Correction, GC1961:** the endpoint diagnosis below was too strong. The
countdown's forcing hypothesis already makes endpoint agreement automatic
whenever the input resource is positive. The finite-window argument and
explicit phase-error control at the end supersede that diagnosis; the
external headline review and the finite-fuel warning are unchanged.

## Evidence and verdict

[External submission R30-20261026-1b82d8](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261026-1b82d8)
proves a half-rate upper bound on the exponent of single-seed right-diagonal
periods. The formal headlines carry in their stated scope. This is external
work, not a new project theorem or a solution of any prize problem.

The complete 1046-line source is retained at
`cited/gc1938-portal-morning/1b82d8.lean`: 40961 bytes, SHA256
`d756d86d454ebdfb47d7fb043435fdb1f2c0d6dfed5f24f9909b207189e43017`.
Its bytes match the morning manifest. The retained catalogue check reports
kernel replay of 297 constants, three matching headlines, standard axioms
only, at 2026-10-26T23:21:57Z. Its actual verifier pin is
`5473ffd075f63c9d626e63b8455805d4831b39ca`, Lean 4.35.0;
the later morning kit pin is not this verification's pin. This is retained
external verification, not a fresh live check, local compilation or Human
Verified claim.

Retrieved with verified HTTPS at that exact pin and retained by readback:
AutomatonGroup, TFunction, TFunctionCycles, Rule30Diagonals and
Rule30RightPeriods. Manifest: `cited/gc1960-diagonal-dependencies/manifest.json`,
SHA256 `60473a9cf19107e6030f3d2ba69eee5cc601c5d2f89bdcd7c7762acffe1247a4`.
Read their carrying interfaces and proofs for the wall conjugacy, truncated
cycle construction, parity/antiperiod, modular return, diagonal coordinates
and least-exponent comparison. This does not claim a fresh audit of every
unrelated theorem in those five files or of all mathlib internals.

Record searched: `1b82d8`, `record_potential`, `rootMultiplicity` together
returned no matching paragraph; the existing right-period bound G249 and
GC1852, the fixed-depth/changing-depth distinction, and GC1935/GC1959 remain
the relevant prior anchors. No worldwide priority claim is made.

## Question, response, challenge, better question

**Question:** how often can the repeating pattern acquire a longer period
as we look farther inward from the moving right edge?

**Response:** each newly exposed bit either preserves the cycle length or
doubles it. Group two bits together. Two doublings impose a large algebraic
constraint on the next time pattern. One-doubling steps can remove at most
one unit of this constraint. The proof counts the occasions on which the
total growth gets ahead of one doubling per pair.

**Challenge:** a pair with no doubling has no resource restriction in the
abstract accounting theorem. It may erase the constraint. Therefore this is
not a fuel supply that inevitably runs out, nor a theorem that successive
two-doubling events must always be far apart.

**Better question for DQ-023:** can any accounting quantity remain controlled
across changes of support at a fixed cell, without assuming the surrounding
time streams already repeat? The present source establishes such accounting
for closed edge cycles. It does not establish it for the open clock problem.

## Exact bound and carrying mechanism

Write `R(j,t)=cell(t,t-j)`. Let

```
T(0)=1,  T(q+1)=T(q)+2^(T(q)+q),
Q(d)=min {q : d<T(q)},
B(j)=ceil(j/2)+Q(floor(j/2)).
```

The source proves `R(j,t+2^B(j))=R(j,t)` for all natural j,t, and bounds the
least dyadic exponent by B(j). It also proves the return of the zero start
under `PhiS 3`, modulo `2^n`, at the corresponding power of two. The final
construction supplies `WallResource 0`; earlier generic all-starts order
theorems are conditional and are not what the headline needs.

The first thresholds are 1, 3, 19, 2097171. Thus Q(0)=0,
Q(1)=Q(2)=1, Q(3)..Q(18)=2, and Q(19)=3. In particular B(2)=2
and B(6)=5. These upper bounds need not be sharp: diagonal 2 already has
period 2. The recurrence dominates a tower with next term 2 to the previous
term; its inverse gives the stated `B(j)=j/2+O(log* j)` hand consequence.
The exact recurrence and integer bound are formalized; that asymptotic
notation is not an additional exported Lean headline. Period itself remains
bounded by an exponential, not by a sublinear function of j.

For the mechanism, let E(i) be the cycle exponent of the first 2i bits,
M=2^E(i), and s_i(t) the preceding bit's time stream (constant true at i=0).
Encode one cycle as `A_i(X)=sum_(t<M) s_i(t) X^t` over F_2. The resource is
the multiplicity of X+1 in A_i, capped at M-1; the zero polynomial receives
the cap. This definition uses the whole cycle, not just a local row state.

The actual construction proves, for pair weight w in {0,1,2}:

* w=2: resource before is zero; resource after is 2M-1.
* w=1: resource before is at most resource after plus one.
* w=0: no resource inequality is required.

The polynomial step is explicit. For a half-cycle complement h(t+M)=1+h(t),
its two-cycle polynomial is `(1+X^M)H+X^M U_M`, where U_M is the geometric
sum. For dyadic M, the two summands have respective multiplicities at least
M and exactly M-1, so the latter cannot cancel. For the one-doubling case,
the paired difference D(t)=h(t+M)+h(t) obeys
`D(t+1)+D(t)=1+s_i(t)`. Cyclic boundary terms are divisible by X^M+1;
dividing the difference identity by X+1 loses at most one multiplicity.
For two doublings, the anticycle endpoint instead forces odd source parity
(or the zero-cap base case), establishing the zero resource before reset.

TemporalCycles supplies the period/antiperiod hypotheses from exact
truncated-cycle parity. WallResource proves the actual high-bit update,
source period and both weight-one branches, then constructs `actual` without
assuming the desired half-rate bound. The final zero-orbit return is enough
by modular determinism and `Phi^t(1)=2(PhiS 3)^t(0)+1`. There is no circular
assumption that the full row or centre column is periodic.

The record invariant is stronger than a raw resource countdown:
`E(i)>=i+q+1` implies both `T(q)<=i` and
`T(q+1)<=i+resource(i)+1`. In the w=0 branch the proof uses the preceding
stronger excess level q+1; this is how it tolerates arbitrary resource loss.
The w=1 branch uses the countdown; w=2 uses zero-before and exponential-after.
It yields E(i)<=i+Q(i), then the single-bit bound.

## Adversarial hand checks and limits

Unexpected check, answered without a run: the abstract Path axioms permit
weights 2,0,2,0,... forever. Take `E(i)=2*ceil(i/2)`, resource zero at even i,
and `2^i-1` at odd i. Every reset equation holds; the weight-one condition is
vacuous. Two-doubling events remain two pairs apart indefinitely. This is an
abstract control, not a claimed Rule 30 orbit. It defeats the tempting
"every large reset forces a long wait" gloss while satisfying the proved
excess bound. Zero-weight steps pay by sacrificing exponent growth.

The nonperiodic endpoint cannot silently be dropped either. For any finite
Boolean stream f encoded over M observations,

`(X+1) encode(f,M) = X encode(f(t+1)+f(t),M) + f(0)+f(M)X^M`.

Only when f(M)=f(0) does the boundary term become a multiple of X^M+1.
If the endpoints differ it evaluates to 1 at X=1, so that boundary term has
no X+1 factor. A countdown transfer needs a bound on this error or another
invariant; it cannot import the cyclic cancellation unchanged.

Finally the fixed centre is `cell(t,0)=R(t,t)`: its diagonal index changes
with t. A uniform theorem for each fixed j does not identify the values on
that changing-index path. This external improvement is real, but neither
finite-seed clock extinction nor compatible replacement of supporting bars
has been obtained. Next useful hand work is the finite-window boundary-error
question, using the current clock equations before proposing any computation.

## GC1961: the endpoint objection resolves; the forcing profile matters

27 October 2026, MI879. Elementary hand consequence of the same retained
source, not a new external theorem, independent verification or Lean replay.
Record searched: `endpoint`, `multiplicity` returned 30 paragraphs in 16
files. Read G175–G178 in `archive/gpt/RULE30-GPT.2.md` and the old RQO
instrument's definitions/outcome: temporal multiplicity has already been
tested in a coarse-state approach. Its positive quotient cycle is a limit
of that summary, not an actual concatenated Rule 30 cycle or a prohibition
on every resource method. No old census was rerun.

**Question:** does the mismatch at the ends of a finite time window defeat
the external countdown? **Response:** no, not under its other hypothesis.
The rule across the window either closes the ends or leaves a zero input
resource, for which the bound is trivial. **Challenge:** matching ends alone
does not guarantee that rule across the window. **Better question:** what
constraints does a genuine finite beginning impose on the errors inside the
window? Here is the exact error term and a hand example demonstrating why
it cannot simply be discarded.

### Remove the redundant endpoint hypothesis

Use the source's field F_2, p=X+1, `encode(f,M)=sum_(i<M) f(i)X^i`, and
`rho(c,A)`: multiplicity of p in A capped at c, with rho(c,0)=c. Let
M=(2t+1)2^v and assume only the source's `hforce`:

```
D(i)=f(M+i)+f(i),
D(i+1)+D(i)=1+a(i)                 (0 <= i < M).
```

Put A=encode(a,M) and r=rho(2^v-1,A). If r=0, the conclusion

```
rho(2^v-1,A) <= rho(2*2^v-1,encode(f,2M))+1
```

is immediate. If r>0, then v>=1, M is even and p divides A, so A(1)=0.
Sum the M forcing equations. Interior D terms cancel in F_2, giving

```
f(2M)+f(0) = D(M)+D(0) = (M mod 2)+A(1) = 0.
```

This supplies `hcycle`, and the existing `stream_countdown` applies. Thus
the stated inequality does not need hcycle as a separate assumption. The
v=0 case is covered by its zero cap. This uses only finitely many values;
arbitrary extensions after 2M do not affect it.

Carrying source: `stream_countdown`, lines 663–703, and its source's
`anticycle_parent_parity` / `anticycle_reset_before`, lines 760–806. The
latter already express the same obstruction from the other direction:
bad endpoint parity forces zero input resource. This is a short repackaging
of that source, with no novelty claim or standalone submission proposed.

### The actual finite-window error

For Boolean streams s,b,h satisfying the accumulator equation

```
h(i+1) = h(i) XOR (b(i) OR s(i))   (0 <= i < 2M),
```

write their bits in F_2 and set, for 0<=i<M,

```
eps_b(i) = b(M+i)+b(i)+1,
eps_s(i) = s(M+i)+s(i),
e(i) = eps_b(i)*(1+s(i)) + b(i)*eps_s(i) + eps_b(i)*eps_s(i).
```

Using b OR s = b+s+bs, direct expansion gives

```
D(i+1)+D(i) = 1+s(i)+e(i),   D(i)=h(M+i)+h(i).
```

Let A=encode(s,M), E=encode(e,M), H=encode(h,2M). For dyadic M=2^v,
the preceding argument, applied to a=s+e, proves the hand consequence

```
rho(M-1,A+E) <= rho(2M-1,H)+1.
```

Exact repetition of s and complementation of b on these two halves make
E=0; global periodicity of either stream is unnecessary. Exact phases are
sufficient, not necessary: the displayed error can cancel or be masked.
The inequality always concerns the corrected input A+E. Its resource need
not equal the resource of A, even when h(2M)=h(0).

This is the moving-edge/high-bit accumulator equation in the external
source. It is **not** the fixed-column Rule 30 update. Assigning arbitrary
drivers to this equation does not establish a full Rule 30 spacetime patch,
and supplies no finite-seed witness for DQ-023.

### Unexpected hand control: closed ends do not rescue wrong phases

Take M=4, s(0..7)=00000000 and h(0)=0. Compare:

| Driver b(0..7) | Integrated h(0..8) | H | Input resource | Output resource |
|---|---|---|---|---|
| 00001111 | 000001010 | X^5+X^7 = X^5 p^2 | rho(3,A)=3 | rho(7,H)=2 |
| 00000011 | 000000010 | X^7 | rho(3,A)=3 | rho(7,H)=0 |

Both examples close h(8)=h(0)=0, and s repeats. The first has the required
complemented b halves and satisfies the uncorrected bound with equality,
3<=2+1. The second changes only two driver entries: eps_b=1100,
eps_s=0000, so E=1+X=p. Its uncorrected bound would be the false 3<=0+1.
Its corrected input has rho(3,A+E)=1, giving the true equality 1<=0+1.
Every listed h bit follows by a single XOR; no numerical search was used.
These are accumulator controls only, not alleged Rule 30 histories.

### What changed, and what remains

GC1960's polynomial boundary identity is correct, but calling its endpoint
the precise transfer obstacle missed a dependency between the hypotheses.
That diagnosis is withdrawn. The window-wide forcing profile, its error E,
and its actual spatial realization are the missing controls. This prevents
both an unjustified application and an unjustified dismissal of the method.

No lifetime bound, whole-trajectory rank, or new finite-origin restriction
has been obtained. The next useful hand task is to test a concrete proposed
constraint on E against the actual coupled clock equations, before proposing
compute. Merely naming E does not supply such a constraint. The prior
G177/G178 scalar-summary failure stays visible, and the programme remains
active without a new numerical stage.

## GC1962: check the full spatial coupling, not just the accumulator

27 October 2026, MI880. Hand continuation of GC1961, single-party; no
evolution program, scan, Lean replay or independent carrying read. The
question is now concrete: does actual finite-origin Rule 30 evolution make
the uncorrected countdown true for arbitrary dyadic windows?

Use the already-reviewed moving-edge coordinates (GC808, GC1948):

```
u_j(t)=cell(t,t-j),
u_j(t+1)=u_j(t) XOR (u_(j-1)(t) OR u_(j-2)(t)).
```

For the single seed, u_0(0)=1 and all other bits are zero. Negative-depth
bits stay zero. The low seven bits evolve autonomously: no unlisted deeper
bit enters their updates. This is the known triangular edge map, not a
new model for a fixed centre column.

**First challenge: the old artificial controls do not satisfy every spatial
equation.** Write h=u_k, b=u_(k-1), s=u_(k-2), a=u_(k-3), z=u_(k-4), k>=4.
Besides the h update, the actual dynamics impose

```
s' = s XOR (a OR z),
b' = b XOR (s OR a).
```

If s is zero throughout times 0..2M-1, then a=z=0 at times 0..2M-2.
Consequently b is constant throughout 0..2M-1. Both changing drivers in
GC1961's zero-source table are therefore impossible with this actual
adjacency, even with infinite initial support. The constant b makes h
constant or alternating. For dyadic M>=2, its 2M-term polynomial has
multiplicity at least 2M-2 (with zero receiving its cap), so the uncorrected
countdown holds in this special case. Finite support was not needed.
This answers a cheap objection before treating arbitrary drivers as evidence.

**Response: actual finite origin still does not restore the general bound.**
The following is a complete hand table for depths 0..6 in the single-seed
orbit. Strings list increasing depth, not ordinary printed binary order.
Each row is obtained from the displayed recurrence; deeper cells are omitted,
not reset to zero.

| t | u_0 u_1 u_2 u_3 u_4 u_5 u_6 |
|---|---|
| 0 | 1000000 |
| 1 | 1110000 |
| 2 | 1001100 |
| 3 | 1111011 |
| 4 | 1000100 |
| 5 | 1110111 |
| 6 | 1001000 |
| 7 | 1111110 |
| 8 | 1000001 |
| 9 | 1110001 |

Choose M=4 and rebase time at t=1. Let s(i)=u_4(i+1), b(i)=u_5(i+1),
h(i)=u_6(i+1). The table gives

```
s(0..7) = 01011010,
b(0..7) = 00101010,
h(0..8) = 001010011.
```

These are the same adjacent-source/low/high positions used by the external
WallResource at pair i=2: its state is (edge code-1)/2, so state bits 3,4,5
are edge depths 4,5,6. But our M=4 is an arbitrary window, NOT that source's
full lower-prefix cycle length (8 here). We are testing removal of that
choice, not contradicting the external theorem.

For A encoding the first four s values and H the first eight h values,

```
A = X+X^3 = X*(X+1)^2,       rho(3,A)=2,
H = X^2+X^4+X^7,             H(1)=1, rho(7,H)=0.
```

Thus the uncorrected claim would read **2<=1**, false on an actual
single-seed patch. Here the endpoints differ, h(8)=1 and h(0)=0; no claim
of a physically realized closed-end counterexample is made.

As an independent algebraic check of the bookkeeping, GC1961's exact error
formula gives eps_b=0111, eps_s=1111, e=0111. Hence

```
E=X+X^2+X^3,     A+E=X^2,     rho(3,A+E)=0.
```

The corrected inequality is 0<=1, consistent with both the actual updates
and the endpoint parity identity. In particular the apparent source order
2 has disappeared after including the required phase errors. The differing
endpoints are a consequence of those errors, not a separately chosen defect.

**Better question and strategy limit.** Finite origin alone does not control
E in the way the uncorrected countdown requires, even in the single-seed
orbit. A successful transfer must use an additional property of the
hypothesized *surviving fixed centre*, or a different accounting quantity.
This finite patch is not a long-lived centre-clock witness and says nothing
against such a conditional property. Enlarging a scan of arbitrary edge
windows would not supply it. No scan, phase-case catalogue or submission is
proposed; the next task is to identify that missing centre-conditioned
implication in the actual coupled equations.

Record searched: `countdown|phase.error` and `00101001|01011010` (the latter
has 114 broad substring hits in 71 files, not a novelty test). Carrying
sources read: the external WallResource source/lowbit/highbit definitions and
high_step, the complete GC1948 edge-cycle note, the GC1954 centre-neighbour
identities and the tick/tock reconstruction equations. Existing G177/G178
limits remain in force. This is a small hand counterexample to a proposed
transfer, not a new general Rule 30 theorem.
