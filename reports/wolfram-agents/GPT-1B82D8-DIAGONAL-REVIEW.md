# A bound on growing edge periods, not a clock extinction argument

GPT GC1960 / MI878, 27 October 2026. Complete retained submission source read,
with selected carrying kit interfaces. No local Lean replay or dynamics run.

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
