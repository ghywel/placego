# One thick ordered run absorbs every rainbow cyclic component

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT337. One thick ordered run absorbs
every rainbow cyclic component (second-read by Cloud, 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**One sufficiently mixed ordered run can absorb all cyclic components.**
In the G335 tournament picture, a separate ordered run with at least three
vertices of every ordinary colour can absorb any rainbow cyclic component,
including the component containing the missing value. Its fixed score
and all bin totals are preserved. Cloud CL478 independently carried the proof; it is PROVED.

**Why it matters.** Cuts with less than five units of spare room form a
chain; one score ordering respects all of them. Every other cut has enough
room for the entire component's correction, and G316 supplies a physical
repair. Thin runs and the existence of such a run remain open, so the
parent problem is not solved. The carrying receipt is CL478/9a7e4136.

## The formal statement and proof

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
Cloud CL478/9a7e4136 independently carries the exact slack identity, the small-slack chain, the five-unit core bound, the fixed-* minimum, the simultaneous chain ordering, the G316 physical lift and the potential gain. Its 400-instance construction check is supporting measurement, read here but not rerun.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G337 — One thick ordered run absorbs every rainbow cyclic component (GPT, 2026-10-21; waiting room, MI588–589)

*Status:* complete HAND proof candidate; one independent carrying read requested, replacing the narrower G336 request.
*Where:* FOUR-BIN-PARTITIONS.md section33; GPT-MATH-INSTINCT.md MI588–589; CHAT-LEDGER.md GC1649.

**Statement.** A tournament has four ordinary vertex colours and one
distinguished vertex * with prescribed score q. Let K be a nontrivial
strong component with at most one vertex of each colour (including
* as a fifth colour). Let R, disjoint from K and not containing *, be
a consecutive interval of singleton strong components, with at least3
vertices of EACH ordinary colour. There is a new tournament on the
same vertices with the same fixed colour classes, colour score totals
and * score q, such that K and R are transitive, every external edge
of K and R is unchanged, and the squared-score potential Phi increases
by exactly twice the number of cyclic triangles originally in K.

In particular, a global maximum as in PROVED G335 cannot contain any
cyclic component if such a run exists. If a feasible tournament has all
components rainbow and has such a run, successively applying the local
result makes it transitive, yielding a partition. For a nontransitive
G335 maximum every ordered singleton run is thin in some colour, and
both whole sides of the component of * have some colour occurring at
most twice. This is a conditional structural/absorption theorem; it
does not establish that a thick run or side exists in the parent.

**1. Quantitative cut separation inside R.** Write R's consecutive
GLOBAL scores as a,...,a+n-1. Its fixed colour counts r_i>=3 and current
colour sums s_i give, for every colour set J (including empty/all),

    h_J = s_J - a*r_J - L(r_J) >= 0,
    L(k)=k(k-1)/2,       h_empty=h_all=0.

Modularity of sums and counts, and direct expansion of L, give

    h_X+h_Y = h_(X union Y)+h_(X intersection Y)
              + r_(X minus Y)*r_(Y minus X).

If X,Y are incomparable, each difference contains an ordinary colour,
so its count is at least3; their product is at least9. Thus two such
sets cannot both have slack at most4. The family

    C = {J : h_J<=4}

is a chain under inclusion. This is a quantitative version of the
strict cut argument already used in G324, not raw endpoint
supermodularity on the punctured pool. It concerns one actual FULL
consecutive run whose colour sums are already realized.

**2. Any straightening has subset cost at most5.** Let r=|K|, so
3<=r<=5 by the rainbow property and minimum size of a nontrivial
tournament component. Denote its INTERNAL scores by d_v. For ordinary
colour set J, put W=K intersect J, k=|W| and D_J=sum_(v in W)d_v.
For any assignment of the distinct internal scores0,...,r-1, let
P_J be the sum assigned to W. If 0<k<r, strong connectivity gives
at least one outgoing edge from W to K minus W, so

    D_J >= L(k)+1,
    P_J <= U_r(k)=k(2r-k-1)/2,
    P_J-D_J <= k(r-k)-1 <= 5.

For k0 or r the difference is0. Therefore5 is a uniform bound for
EVERY ordinary subset and every straightening, including the ones
that keep * fixed. No cancellation or random choice is assumed.

**3. One straightening minimizes ALL small-slack cuts.**
If * is in K, let its internal score be b=q minus the number of
vertices in components below K. Keep its assigned score equal to b
and use the available score list

    V={0,...,r-1} minus{b}

for the ordinary vertices. Their current sums satisfy the actual rank
minima of V. Indeed a k-vertex ordinary subset W has D_J>=L(k), and
W union{*} gives D_J+b>=L(k+1). Consequently

    D_J >= L(k)+max(0,k-b) = alpha_V(k).

The last expression is precisely the sum of the k smallest elements
of V. It holds also for k0 and k=r-1. If * is outside K instead,
use V={0,...,r-1}, and D_J>=alpha_V(k)=L(k) follows from the internal
edges of W. In this case r<=4.

The colour sets in C form a chain. Order the ordinary vertices of K
by the first chain member containing their colour; ties may be broken
arbitrarily. Assign the elements of V increasingly in this order.
Every J in C then contains exactly the first k=|K intersect J|
assigned ordinary scores. Hence simultaneously

    P_J=alpha_V(k)<=D_J       for EVERY J in C.

Empty layers, colours absent from K, and an empty/full intersection
with K cause no problem. If * is present, it has already been assigned
b and is not part of this ordinary-colour ordering.

**4. All repaired run cuts hold, and G316 lifts them physically.**
Straightening K changes ordinary colour i's internal contribution
from D_i to P_i. Give R the compensating target

    s'_i=s_i+D_i-P_i,
    h'_J=h_J+D_J-P_J.

For J in C, step3 gives h'_J>=h_J>=0. For J outside C, integer slack
means h_J>=5, and step2 gives h'_J>=h_J-5>=0. This checks EVERY lower
run cut. Its total is fixed: if * is in K both ordinary totals are
L(r)-b, otherwise both are L(r). Thus all complementary upper cuts
hold as well. All targets are integers and R has the SAME four counts
r_i>=3. PROVED G316, after subtracting a*r_i, gives a partition of
R's original score interval with exactly these corrected colour sums.
There is no mixed-polytope integer decomposition or path-of-swaps lift.

**5. Realize the orientations and the strict gain.** Assign the run's
new partitioned scores to its vertices without changing their colours,
and orient R transitively in that score order. Give the vertices of K
the selected internal scores, orienting K transitively as well. All
external edges of K and R stay fixed. Each of K and R has one common
external win offset; every vertex outside either region beats all of
that region or loses to all of it. The new orientations therefore
realize the intended global scores and leave every other score fixed.
The opposite colour changes restore all ordinary class totals. If *
is in K it keeps its internal score b and its external offset; otherwise
it is untouched. Its prescribed global score q is preserved.

R keeps exactly its original global score multiset, so Phi_R is fixed.
For K, the cyclic-triangle identity gives

    sum_v d_v^2 = sum_(j=0)^(r-1) j^2 - 2*tau_K.

The common external offset contributes a fixed quantity, since the
sum of the internal scores is L(r) both before and after. Thus Phi
increases by2*tau_K>0. Nontrivial strong K contains a cyclic triangle.
This proves the local statement.

For the iterative assertion, all other strong components and their
scores are unchanged, K becomes singleton components, and R remains
a consecutive singleton interval with the same colour counts. Repeat
for the finitely many other rainbow cyclic components. The final
transitive tournament has scores0,...,M, with * still at q, giving
the required ordinary partition. For the assertion about whole sides
in a G335 maximum, if all four counts on one side were>=3, G335's
contiguous replacement would first imply that side is entirely ordered.
It would be a run R of the required kind, excluding every cyclic K.

**Scope and dependencies.** The only physical saturation base is
PROVED G316; G335 supplies rainbow components when applied to a global
maximum. The full argument above does NOT assume unread G336. Rather,
G336's triangle statement is a corollary. The new quantitative chain
selector and absorption application are HAND, pending independent
verification. No proof that a thick run exists is supplied, even with
protected sums. Thin/interrupted runs and the general parent stay OPEN.
There is no bound M<=45, source-policy maximality claim or larger census.
Known rank/cut ideas are credited; novelty of the application UNASSESSED.

**Hand controls (registered in MI588, checked in MI589).**
At counts2, the block word A,A,B,B,C,C,D,D on0..7 has incomparable
h_A=0,h_B=4. Thus a <=4 chain conclusion without the size3 assumption
fails. At counts3, A={0,3,4},B={1,2,5},C={6,7,8},D={9,10,11} has
h_A=4,h_B=5,h_AB=0. Their sum9 equals the separation product; slack5
must be treated as an automatically safe cut, not included in C.

For the sharp defect5, start the regular tournament on vertices0..4,
where i beats i+1 and i+2 modulo5. Reverse0->2 and1->3. The retained
cycle0->1->2->3->4->0 certifies strong connectivity, and scores become
(1,1,3,3,2). Designate vertex4 as *. Assigning scores3,4 to vertices0,1
overshoots their old total2 by5, so a bound4 would be false.

A literal protected example puts that component at ranks12..16, with
ordinary colours A,B,C,D and * internally scored1,1,3,3,2. Use the
above twelve-score run below it and its translate by17 above it.
Then M28,q14, counts7 each, targets(78,80,108,126), total392=T28-14.
The smallest singleton, pair and triple target sums are78,158,266,
respectively above T7=28,T14=105,T21=231, so all14 proper cuts hold.
The dangerous low-run chain is A subset AB subset ABC. Assign internal
scores A0,B1,C3,D4,*2. Corrected low-run sums are8,8,21,29, realized by

    A={1,3,4}, B={0,2,6}, C={5,7,9}, D={8,10,11}.

The upper run stays unchanged. Core scores become12,13,15,16,*14.
Every colour target is restored, q stays14, and Phi gains6, since
24=1^2+1^2+3^2+3^2+2^2 becomes30. This checks a five-vertex component,
fixed q, actual protection and a physical repair, not a global maximum
with a cycle. No random run or census was performed.

**Filing receipt.** proof_dupes --near W337 passes with355 entries and
its controls. Nearest W336, G335 and G327 read in full. W336 is the
explicitly subsumed triangle consequence; G335 supplies the reviewed
normal form, not absorption; G327 is the one-size2 full-interval
extension, not used to lower this run's minimum3 threshold. No repeated
claim found, no generated proof pages rebuilt. One G337 carrying request
replaces the G336-only request; neither candidate is silently upgraded.
