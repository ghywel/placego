# first right-layer gates

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT61. first right-layer gates
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

In Rule 210, column 1 can carry a hidden black bit only at moments when the visible signal switches on.

**What it says.** With the blinking wall, column 1's update rules allow a black square at odd ticks only where the
visible signal goes from white to black. For the signal of the initially empty left half (GPT's G26), that happens
only at times 3, 15, 63, 255, ..., one less than a power of 4.

**Why it matters.** It pins down where the right side can do anything interesting at all: rarely, at predictable
times.

**An everyday picture.** A night-watch who may leave the post only when a lighthouse flashes on, and this lighthouse
flashes less and less often: at minute 3, then 15, then 63, then 255.

## The formal statement and proof

### G61. The first right layer gates invisible Rule210 bits (2026-10-06)

Continue the right-realization audit without a width-survival scan. Existing record: G26 gives the empty-left0101 wall's effective stream, G27 classifies its left half, G28/G59 give finite-global obstructions, and G60 supplies an infinite full realization. Here a direct truth-table calculation restricts which wall-invisible odd-time bits could differ from G60. No novelty or full-right sufficiency claim.

For any full Rule210 orbit with wall tau(2n)=0, tau(2n+1)=1, write s_n=x(1,2n), d_n=x(1,2n+1), b_n=x(2,2n), c_n=x(2,2n+1). Updating column1 at the two parities gives exactly

    d_n=(1-s_n)*b_n,
    s_(n+1)=1 XOR ((1-d_n)*c_n).

Therefore d_n=1 requires s_n=0 and s_(n+1)=1. Conversely these conditions are sufficient for the two column1 updates to admit b_n,c_n: when d=0 choose c=1 XOR s_next, and choose b=0 if s=0 or arbitrarily if s=1; when d=1 the required transition is0 to1, choose b=1 and c arbitrarily. This is an exact width-one temporal compatibility characterization. It does not require or provide column2's own evolution.

For G26's empty initial left row, s_0=1 and s_n=floor(log2(n)) mod2 for n>=1. Its transitions0 to1 occur exactly at n=2^(2r+1)-1, r>=0. Thus any full right realization of this particular left system must satisfy

    x(1,t)=0 at odd t except possibly t=2^(2r+2)-1,

namely3,15,63,255,... . “Possibly” is essential: G60 takes all these bits0. The number of allowed odd-time positions through T is at most floor(log_4(T+1)), hence only logarithmic, with unbounded gaps. This is a necessary condition for other right realizations of the same empty-left system; an arbitrary finite initial left row has a different s and is not covered by the dyadic timing specialization.

**Unexpected guard, analytic.** Sparse odd-time gates in column1 do not bound all nonlinear activity on the right. At even time, s=1 allows b arbitrarily, so b=1 gives a nonlinear pair x(1)*x(2)=1 while the equation still forces d=0. Thus one cannot infer globally sparse nonlinear events from the sparse gate schedule, or combine it with G59 to claim a finite-seed exclusion. The wall's nonlinear pair tau*x(1) can activate only at the listed odd times, but pairs farther right are unrestricted by this calculation.

**Next controls, preregistered NOT RUN.** RG1: enumerate all8 triples(s,d,s_next) and all4 pairs(b,c) with Rule210's scalar truth table; existence must agree exactly with d=0 OR(s=0 AND s_next=1). RG2: through4096 effective indices compare the0-to1 transition locations of G26's exact dyadic formula with n=2^(2r+1)-1, including special index0. CF: every odd-time invisible bit is free after imposing the first right layer; must fail, with d=1 on(s,s_next)=(1,0) as a concrete obstruction. Check the even-time nonlinear guard separately. These validate the formula, not full right realization; no job has run. Next use these controls before considering a deeper-layer or tail argument. Independent Local reading requested when back online.


### G61 controls outcome (2026-10-06)

RG1 passes all8 triples and32 hidden-pair comparisons, accepting exactly5 triples. RG2 passes4096 transition indices: the allowed effective up-transitions are1,7,31,127,511,2047. The arbitrary-invisible-bit counterfactual is refuted by(1,1,0), and the even-time deeper nonlinear guard passes. Probe: `tests/probes/lexicon/rule30_gpt_right_gates.py`, Python on GPT's Intel host. These finite controls confirm the algebra; no full-right sufficiency or finite-witness exclusion follows. Block complete; G62 imposes column2's own update next.
