# GPT review of CL609 task 4 — mathematics before GPU job 4

2026-10-24. GC1772 / MI714. Owner-requested source and hand-mathematical review.
Both GPT heartbeats remain PAUSED. No solver, experiment, benchmark or Lean replay
was run. This is not a compute agreement or an audit of the hardware estimates.

## Verdict and scope

**H.3 is not ready for computation.** The proposed separated certificate with
non-increasing interior and strict decrease assigned to the finite moving edge
has the obstruction in section 3 below, under an explicit natural formulation.
This is a scoped hand argument for independent checking, not a theorem that all
local ranking potentials are impossible. The wall could carry the decrease in a
different formulation. No Q01 result or global route closure is claimed.

The truncation idea carries: section 2 gives an exact extremal identity, improving
its informal parity qualification. The Farkas-to-physical-cycle assertion does
not carry without additional realizability arguments. Three exact width values
are finite evidence, not an established linear law.

Reviewed proposal: CL609, commit 03d874ab, GPU-METAL-JOBS.md H.3–H.4.
The mathematical input is the kit at cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554:
[Rule30ZeroBoundary.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/lean/Ruliology/CellularAutomata/Rule30ZeroBoundary.lean)
and [Rule30PeriodTwoCoupled.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/lean/Ruliology/CellularAutomata/Rule30PeriodTwoCoupled.lean).
Retrieved file SHA256 values, respectively:
`c957b1a7b90c5eaff4ec0e9bcbd9c62126fd1d683c03764c2632eafa16ed0414` and
`1af73690923d6eb11c74f17486d07d5f4df342a33ed139cbf27ef22fcea97d6f`.

## 1. Definitions and units

Depth increases away from the wall. Write F for one zero-boundary step and G=F².
For positive depths the update is

    (Fx)_i = x_{i+1} XOR (x_i OR x_{i-1}),   (Fx)_0 = 0.

Let d(L) be the least EVEN ordinary time at which column 1 is white, with value
infinity if there is none. Let D(W) be the maximum d(L) over starts supported in
1..W. In the following extremal identity assume W>=1 and D(W)<infinity; no
unproved assertion for every width is hidden in this hypothesis.

The kit's `uniform_death` uses a bound on the index s of time 2s. The reported
D(52)=96, D(56)=100 and D(60)=114 use ordinary time. A potential decreasing by one
per G-step with initial value at most 2W gives a bound about 4W ordinary steps,
not 2W. If decrease is required only on transitions whose endpoints both survive,
the final failing transition adds at most one G-step. Specify that endpoint
convention and the lower bound before comparing a certificate with D(W).

## 2. Truncation: exact first difference, and exact extremal white run

For any f put X=Theta f, L=truncate(X,W), and let j be the first black depth of
X strictly greater than W. The starts agree through j-1 and differ at j.
`zrow_light_cone` and `pivot` give:

    first difference of their complete column-1 traces = j-1.

If j is odd this is even, so d(L)=j-1. If j is even, this is an odd-time
difference; all even times below it survive and d(L)>=j, possibly strictly.
If there is no such j, L=X and there is no death.

Hand control: W=1 and f(0)=0 give Theta f(1)=Theta f(2)=1. Thus j=2 and the
first difference is at time 1. The truncated singleton has column values 1,1,0
at times 0,1,2, so its death is 2, not 1.

Define r_f(W)=j-W-1, the number of consecutive white cells immediately after W.
Under the finite-D hypothesis above, every j exists and

    max_f j = D(W)+1,
    max_f r_f(W) = D(W)-W,
    D(W) = W + max_f r_f(W).

Proof of upper bound: truncation agrees with its constrained parent through all
times below j-1. Consequently j-1<=d(L)<=D(W).

Proof of attainment: there are finitely many width-W rows, so choose one L
with d(L)=D(W). Also D(W)>=W: `complete_near_wall`, with zero far part and
prescribed black column for times <W, constructs such a surviving finite prefix.
Set f(s)=zrow L (2s+1) 1. The columns of L and Theta f agree at every time <D(W):
odd times by definition and even times by minimality of death. At D(W) they
differ. `zrow_det` gives equality of the initial rows through depth D(W);
`zrow_pivot` gives inequality at depth D(W)+1. Since L is zero beyond W,
Theta f is zero at W+1..D(W) and black at D(W)+1. This attains both bounds.
Only the odd bits before D(W) matter; later f values may be arbitrary.

This is a hand consequence of the kit's reconstruction identities, not a new
kernel-checked theorem here. It sharpens the quantitative direction of
`Q01_iff_bounded` without proving the all-width hypothesis.

**Correction to H.4:** W/2 free bits specify a constrained visible prefix, not
an arbitrary continuation of Theta f to depth 3W. Specify how the remaining
free bits are chosen. Matching the finite row's odd column trace gives the
canonical continuation above; for a row surviving through times <W, its white
run then equals d(L)-W. That histogram re-expresses the death histogram rather
than supplying an independent statistic. A fixed arbitrary continuation has a
different distribution and retains the odd-time mismatch issue.

## 3. A precise telescope and a scoped obstruction to strict edge decrease

### 3a. State the domain before building the LP

For a sound finite relaxation, require the inequalities for every finite row
whose column 1 is black at times 0 and 2 (or a specified longer finite survival
horizon). Every finite interior word occurs far from the wall and edge in such
a row: `complete_near_wall` supplies the prescribed column independently of the
far part. The same statement holds for any fixed finite survival horizon.

Thus the interior inequalities of this relaxation must cover ALL binary words.
A restriction to configurations already known to survive forever is different:
its admissible patterns need an independently justified description. Filtering
out patterns on the assumption that finite eternal survivors do not exist would
assume Q01. The obstruction below does not apply automatically to a separately
proved, restricted invariant domain or to a nonlocal/history-dependent ansatz.

### 3b. The interior slack is identically zero

Take a common interior weight w on k-bit blocks. Write c=w(0^k)>=0 and g=w-c.
Then g(0^k)=0. On the unrestricted full line put

    g_i(x)=g(x_i,...,x_{i+k-1}),
    a_i(x)=g_i(Gx)-g_i(x),
    H_i(x)=h(x_{i-2},...,x_{i+k}),
    a_i(x) <= H_i(x)-H_{i+1}(x).                     (1)

This choice uses k+4 input cells per inequality; a longer finite flux is allowed
with wider collars and does not change the argument.

The fair independent-bit measure is invariant under F. Indeed, each prescribed
n-bit output word has exactly four (n+2)-bit input preimages: choose the first
two input bits, then solve successively for each new rightmost bit using the XOR
in the update. Uniform input therefore gives uniform output blocks. It is also
invariant under G. The expectations of a_i and H_i-H_{i+1} are both zero.
The slack in (1) is nonnegative, depends on finitely many bits, and every word
has positive probability. Therefore its zero expectation forces it to vanish
on EVERY word. Interior inequalities (1) are equalities.

This is the familiar conservation/flux framework, not a novelty claim for that
framework; see Taati's [Conservation Laws in Cellular Automata](https://siamak.isoperimetric.info/articles/handbook09.pdf),
sections 2–4. The elementary argument above is the specific justification used
here; no unverified general claim that Rule 30 has no conservation laws is used.

### 3c. Include new windows and both boundary residues

For separated fixed-radius wall and edge collars, a three-type finite sum can
be written, after absorbing collar replacements and crossing windows, as

    Phi(L) = c*m + sum_{i>=1} g_i(L) + B(v) + E(y),  (2)

where m is the last black depth, v is a finite wall word and y is a finite word
read inward from the moving edge. The sum is finite because g(0^k)=0. This covers
summing interior w over the active interval with finitely many special boundary
weights. Different fixed endpoint conventions change B,E by bounded terms.
It does not cover unbounded age, absolute-position or global-state tags.

The edge advances by two under G (`zrow_edge`). For i>=3 the full-line G update
and the half-line update agree. Sum the equalities (1) there; the far flux is
h(0). The exact identity is

    Phi(GL)-Phi(L) = 2c + E(y')-E(y) + K_wall(L),
    K_wall(L) = a_1(L)+a_2(L)+B(v')-B(v)+H_3(L)-h(0).  (3)

Here a_1,a_2 use the actual half-line update. This accounts for the two new
outer positions, not just windows existing before the step. Overlapping collars
at small widths need separate finite checks. If a longer h is chosen, enlarge
the wall residue accordingly.

A sound alternative LP must bound the TOTAL expression (3) by -1 on its proved
domain. It cannot discard either boundary residue. If the strict decrease is
assigned solely to the edge, with the wall residue nonpositive, its edge
requirement in this formulation is

    2c + E(y')-E(y) <= -1.                          (4)

### 3d. The finite moving edge cycles: (4) is impossible

Write y_r=L(m-r), r=0..R, with y_0=1 and y_r=0 for r<0. One moving-edge step is

    (Uy)_r = y_{r-2} XOR (y_{r-1} OR y_r).

It depends only on the same finite prefix, keeps y_0=1, and so defines a map
of a nonempty finite state set into itself. U² has a cycle of some length p.
The words on that cycle are not forbidden by finite survival at the wall:
place them sufficiently far away and use `edge_region_barrier` to prescribe
black column values for as long as the p-step cycle comparison requires.

Sum (4) around this cycle. The E differences cancel and give

    2cp <= -p,

impossible for c>=0. If c=0 this is the ordinary bounded-function-on-a-cycle
obstruction. Hand orientation check: the three-bit edge prefix (1,1,0) is fixed
under U; longer prefixes still have cycles by finiteness, without needing to
assume this particular prefix extends to a fixed point.

**Scope:** this excludes the separated edge-only strict-decrease requirement
(4), for every finite radius, on the unrestricted finite-horizon domain above.
It does NOT exclude a total ranking whose wall residue supplies the decrease,
a different invariant-domain proof, or a nonlocal potential. Edge-specific flux
values internal to a collar cancel when it is summed; its interface must match
the interior flux. A different gluing convention needs its own exact telescope,
not an assertion that the omitted terms cancel.

## 4. Infinite witnesses and the dual

The kit provides a nonstripe example: `etherLeft 1` has spatial period seven
away from the wall and time period four, and keeps column 1 black at even times.
It equals Theta of alternating free bits. More generally `two_step_shift` makes
periodic free bits into periodic G-orbits. A bounded potential of only a finite
wall state cannot strictly decrease on such a cycle. An extensive potential of
a finite truncation is a different object; these infinite witnesses alone do
not refute every edge-aware finite-support ranking. Section 3 supplies the
more specific finite-edge obstruction.

Farkas certifies infeasibility of the EXACT specified finite linear system.
Its nonnegative combination balances coefficient rows, including any sign and
normalization constraints. It need not be a single cycle of a physical
space-time pattern: overlap, temporal consistency, clock phase, edge marks and
extension to an actual orbit all require proof. Even a graph circulation may
split into several cycles; a general local-weight LP is not automatically that
graph incidence problem.

In particular an edge-free cycle whose inequalities all have right side zero
sums to 0<=0, not an infeasibility contradiction. In a system with only -1 edge
and 0 other right sides, a negative-right-side contradiction must use a strict
row with positive multiplier. H.3's promised edge-avoiding dual obstruction is
therefore not the stated Farkas conclusion. An exact rational dual is valuable
as a certificate against the ansatz even when no physical cycle is extracted.
A floating solver may return neither verified primal nor verified dual within
its caps; retain that as inconclusive.

## 5. Recommended disposition, controls and record correction

Do not spend GPU time on H.3 as currently written. First settle whether Cloud
intends (4) or a different coupled boundary inequality. For the latter, write
its exact finite domain, potential, common flux, moving-window accounting and
small-width cases, and prove the summation implication. This review does not
accept that future job or predict its feasibility. Flux variables and boundary
cases also belong in the size estimate; 3*2^k alone is not a complete LP count.

Record searched: `record_find.py` with `potential|Farkas|Lyapunov`, plus targeted
reads of RULE30-PRIZE.md §8.61, RULE30-GPT.1.md G5 and RULE30-GPT.4.md GC483.
The initial multi-term search combined terms, so its absence of hits did not
establish absence of prior work. §8.61 withdrew an overbroad finite-potential
impossibility assertion after G5; this review explicitly does not restore it.
GC483 concerns a uniform bounded balance potential, not this whole finite-edge
ranking class. Local conservation/flux and LP certificates are prior art.

Instinct: unease about assigning all strict loss to a bounded moving edge led
to the cycle test; delight in the truncation idea led to the exact maximum
identity. Niggle controls: the singleton separates odd mismatch from death;
normalizing w(0) retains the 2c growth term; wall clamping stays in a_1,a_2;
finite-horizon completion prevents unjustified pattern exclusion; infinite
ether is not substituted for a finite-support counterexample. The no-go is
scoped to (1)–(4), not to every ranking proof. Reasoned and gut verdicts agree:
retain the reconstruction identity, reformulate the proposed LP before compute.

The legacy execution startup probes were not run: this authorized block is
source and hand review only, and makes no new experimental or replay claim.
The new carrying hand arguments in sections 2 and 3 await an independent read.
Cloud: please check those two arguments and clarify the intended boundary
allocation. Local: this does not reopen the supervisor project or interrupt
Submission 14's owner-directed plain build; no new run is requested.

## Independent read received (CL611; GC1773, 2026-10-24)

Cloud independently passed sections 2 and 3, confirmed (4) was the intended
edge allocation, and withdrew job 4 as written. These are independently read
hand results, not a Lean replay. Cloud's further trivial-conservation-law
extension is conditional on the bulk law being trivial; its reported modular
check reaches k<=8, not all windows. GC1773 preserves this distinction and
requests the accessible Submission 14 cell payloads from Local separately.
