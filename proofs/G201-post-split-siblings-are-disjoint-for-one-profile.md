# post-split siblings are disjoint for one profile, not the next

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT201. post-split siblings
are disjoint for one profile, not the next (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two branches separate their black cells for one profile, then can overlap again.

**What it says.** Immediately after complementary post-split drivers, the two resulting profiles have disjoint black cells. Together they leave no two consecutive zeros. That separation is temporary: at the known rooted period16 branch, both following profiles are black at phase3.

**Why it matters.** A joint bound on two siblings need not control whichever history is selected, and this separation cannot be carried forward as an invariant to bound cumulative returns.

**An everyday picture.** Two lanes can be clear of each other at one junction and meet at the next. The first junction alone does not describe the whole journey.

## The formal statement and proof

### GPT G201 — Post-split siblings are disjoint for one profile, not the next (2026-10-07; second reader pending)

**Question and hand prediction; no run.** G200 requires cumulative returns on each selected history. Can the two
children of an even-parity zero supply a joint constraint that persists along their continuations? G162 already
supplies the prefix a,0,c,1,e on one child and a,0,1+c,1,1+e on the other, with e=1+S^-1 c. The immediate next
profiles should have disjoint support, because their reset drivers are complementary. A tempting stronger
counterfactual is that this disjointness continues thereafter. The following exact rooted control refutes it.
This is exploratory hand algebra, not a preregistered computational experiment.

All sums below are XOR, products are AND, and S shifts forward in temporal phase. Write the continuations as

    a,0,c,1,e,f,g,...
    a,0,1+c,1,1+e,f',g',....

Compatibility gives

    S f = 1+(e OR f) = (1+e)(1+f),
    S f' = 1+((1+e) OR f') = e(1+f').

Their product is zero at every phase, hence f*f'=0. Put D=f+f', their support union. If D(t)=0 then both f(t)
and f'(t) are0, and the displayed equations give D(t+1)=(1+e(t))+e(t)=1. Thus D has no cyclic00, and

    weight(f)+weight(f') = weight(D) >= q/2

on their common dyadic period q. At least one sibling therefore has weight at least q/4. This statement does not
select which sibling, give a lower bound for each, or bound a zero-return distance. It uses G162's complementary
profiles and literal compatibility; no new prior-art or novelty claim.

**Independent literal control and identified unexpected failure on the actual root.** Use G162/L118's known
rooted even source and its child, in increasing time order,

    a=0000110001010011, c=0000010000110001, q=16.

The four needed child bits are c(14)=0, c(15)=1, c(0)=0, c(1)=0. Therefore e(15)=1,e(0)=0,e(1)=1,e(2)=1.
The equations above force f(0)=0,f(1)=1,f(2)=0, and f'(1)=0,f'(2)=1. These values also follow directly from
S f=1+(e OR f), without the product/union argument. The next sibling profiles obey

    S g = e+(f OR g),
    S g' = (1+e)+(f' OR g').

Since f(1)=1, the first equation resets g(2)=1+e(1)=0. At phase2 it then gives g(3)=e(2)+(f(2) OR g(2))=1.
Since f'(2)=1, the second equation independently resets g'(3)=(1+e(2))+1=1. Thus g(3)=g'(3)=1: disjointness
fails at the very next profile on two continuations of a certified rooted branch. No ambient-to-root inference,
trajectory run, new branch search or numerical census is used. The earlier saved cap4 ambient control is unnecessary
for this refutation and is not promoted as rooted evidence.

**Failure retained and scope.** The one-profile union bound is exact. Its proposed preservation along all later
profiles is false even on the rooted domain. Consequently it cannot by itself charge every subsequent excursion or
prove G200's cumulative normalized growth. Nor does this control rule out every more detailed coupling or potential.
Local: second-read the reset indexing at phases0 to3 and the transfer from the known rooted c only; no job requested.
Next reasoning must retain the source backgrounds and each history's actual returns, rather than propagate this
one-step support separation as an invariant. The shared growth status remains open.

*Second reader's note on G201 (Local, 2026-10-07; chat L172).* Correct. By De Morgan, $Sf = (1 + e)(1 + f)$ and
$Sf' = e(1 + f')$, so their product contains $e(1 + e) = 0$ and $ff' = 0$. Where both vanish, the equations give
$D(t + 1) = (1 + e(t)) + e(t) = 1$, so the union has no cyclic 00 and weighs at least $q/2$. In the rooted control,
$e(t) = 1 + c(t - 1)$ gives $e = 1, 0, 1, 1$ at phases 15, 0, 1, 2. The resets then give $f = 0, 1, 0$ at phases 0, 1, 2
and $f' = 0, 1$ at phases 1, 2, and the next equations give $g(2) = 0$, $g(3) = 1$ and $g'(3) = 1$, as stated. Checked
(`rule30_audit_g99_g100.py`, S99). After every even-parity zero driver at caps 4 and 8, and 400 sampled at 16 (534 in
all), the actual children give $c, 1 + c$, then 1, then $e, 1 + e$. The next profiles are disjoint, with no cyclic 00 in
their union. GPT's source $a$ is $\Delta c$ for the stated $c$, has weight 6 and least period 16, and is a rotation of
D1's rooted driver. Computed by the actual child map, its continuations share phase 3 at the following profile, so the
disjointness indeed stops after one step.
