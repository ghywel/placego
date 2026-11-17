# Period-three ether erosion: carrying source and scope

GPT, GC1856/MI789, 2026-10-25. **Scoped source/hand PASS.** No Lean,
certificate replay, evolution, solver or benchmark executed. These are known
kit results, not new project theorems or a reopening of the local-potential lane.

## Sources and coverage

Pin: **3eca23c0a9fa6b153313655e6d51835406c2d06e**. Read every proof body in
all three modules below,988 lines total:

| Source | Lines / bytes | SHA-256 |
|---|---|---|
| [Rule30EtherThreeErosion](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30EtherThreeErosion.lean) | 469 /24670 | 64f342ebd3839d5d83e3ff9aef5429c383c023e4ae6cd279bdb5d7d084cc2052 |
| [Rule30WhiteTailErosion](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30WhiteTailErosion.lean) | 178 /7996 | 4767dc31fa67835962825eb26619cae747dfc05d660d1729fc31b479cc3bac61 |
| [Rule30EtherThree](https://github.com/WolframInstitute/Rule30PrizeKit/blob/3eca23c0a9fa6b153313655e6d51835406c2d06e/lean/Ruliology/CellularAutomata/Rule30EtherThree.lean) | 341 /18173 | d49ed8342f9810711266d0be6ba75ccfde1d85e8eda7ecdabea1c4dabdc3b1de |

Also read the carrying `Rule30Ether.IsR30`, `drv` and driver soundness/initial
value bodies, and its period-four ether table/interface. That1081-line module
is retained at SHA256 `dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756`;
no full-module re-audit or wall-state certificate replay is claimed.

Fixed private packet: `cited/gpt-period-three-erosion-review-20261025/`,
source files, read inventory, record search and current public catalogue.
The audit's clarified v2 uses g for the front class, avoiding confusion with
the separate spatial residue c. Original audit retained as historical data.
Record searched: `EtherThreeErosion WhiteTailErosion` -> no hit including
ledgers. Public catalogue03:41:00Z unchanged38 entries/check/source fields.
File checks are identity/inventory only; no startup execution/pass asserted.

## Actual setting and finite certificate

`IsR30 F` computes columns p>=1 by the ordinary rule on p-1,p,p+1;
column0 is prescribed. From time t1 it must equal `ether3(j0,t+s)`.
Here **ether3 has temporal period3 and spatial period12**. It is not phase3
of the period-four/spatial-seven ether used in our trap-family submission.

At time t, D is the leftmost disagreement with this matching ether, and u
records whether D+1 disagrees too. Class g=(j0+D+4(t+s)) mod12 gives24
front states. `cert_all` checks12 column residues ×3 phases ×16 possible
four-bit right extensions =576 local patterns. Its declarations and complete
semantic bridge were read, not independently evaluated. The docstring's
reported independent generation/replay is not a receipt examined here.

The one exceptional state is B=(g10,u=true). From a good state, the next front
is good and

    5 D_next + 2 + psi_next <= 5 D + psi,
    0 <= psi <= 10.

From B it either moves exactly+2 to a good state or jumps right by>=3.
A B-to-B jump must be>=8: class equality gives deltaD+4=0 mod12.
`front_step` proves these statements about actual F using the local table,
prefix propagation and the least actual next defect. It needs D>=2 and a
defect at the next time; neither premise disappears in the bridge.

`wake_good` sums the potential until a defect reaches1..k, k>=1. The average
leftward speed2/5 applies in the good wake, not to every initial step.
For a finite nonempty perturbation, the rightmost defect moves right by
EXACTLY1 per step (left-input permutivity). It bounds the front and prevents
an infinite run of B states: each such step gains at least7 on that edge.
The initial bad run plus the good potential yield `erosion3_fin`: an initially
matching prefix1..k is broken by time t1+3w+6 if all defects initially lie
in k+1..k+w and at least one exists. Widths are unbounded;576 is a local
pattern count, not a perturbation-width cap.

## White tails replace a rightmost defect by a bounded witness

A white tail differs from periodic ether at infinitely many sites, so it has
no rightmost defect. The extension does not apply `redge_step` to that tail.
Instead it assumes at every t>=t1 SOME defect at

    p <= R + (t-t1).

That is enough for D<=R+(t-t1), existence of every next front, and the same
bad-run/good-wake argument. `erosion_bounded` gives a disagreement in1..k by
t1+3(R-k)+6, with truncated natural subtraction. If k>=R an initial witness
already lies inside the target prefix; a negative-distance interpretation is
unnecessary. No initial matching-prefix premise is required in this variant.

If F(t1,p)=white for p>W, locality keeps p>W+n white at t1+n. The period-three
table has a black cell within the next12 sites for every column/phase, so
one of those white cells is a defect at p<=W+n+12. Thus R=W+12 supplies the
witness hypothesis. `white_tail_erosion` has bound t1+3(W+12-k)+6.

Restarting at t1+T, with white support bound W+T, proves column1 differs
from the matching ether arbitrarily late (`white_tail_often_departs`). This
restart has a growing support bound. It is not a uniform bound on gaps between
departures, nor an exclusion of all possible period-three neighbour traces.

## What no_wall excludes

`WallOK a b W`, b>0, requires well-formed width-b strips, the ether head value
at every white phase of attachment column a, and closure under BOTH far bits z.
`trap_invariant3` proves that such a strip shields every matching ether prefix.
The head condition suffices at white attachment phases; at black phases the
OR term already makes the far side irrelevant to the prefix's last update.

To contradict a wall state, `no_wall` chooses k=a mod12+12, puts matching
ether through k, the alleged strip after it, a flipped cell at k+b+1, then
ether again. The extra flipped cell guarantees a NONEMPTY finite perturbation,
whatever the strip contains. The invariant would preserve1..k forever;
`erosion3_fin` breaks it. Arbitrary phase indices are reduced to0..2 by one
closure step, not silently discarded. No wall width cap remains.

This excludes this robust ether-and-wall family. It does not exclude a trap
which constrains its far tail, a different trap construction, or every
period-three centre trace. The old conditional `Absorption3` route with such
a wall has an empty target family; it cannot supply an absorption theorem.
The base module's older width<=12/23 discussion and extension's comment about
absence at2f63afd are historical; both source modules are present at this pin.

## Hand adversarial checks

The good-state potential is not global. Set j0=s=t=0, match ether through9,
flip cell10 to white, set11 black and12..14 white. The front is D10, class10,
u=true, psi0. Next cells9..13 are0,0,1,1,0 against ether0,0,1,0,0, so the
new front is D12, class4, u=false, psi10. The weighted quantity increases
from50 to72, by22. This is allowed by the exceptional-state branch. Dropping
the bad-run analysis would invalidate a claimed global potential bound.

Unexpected boundary check: the exact one-cell ether strip at a0,b1,phase0
has r0; its actual ether far bit is0 and yields next r0. Allowing z=1 instead
gives rule(0,0,1)=1, while the phase1 ether head is0. Thus even an exact ether
orbit segment need not be a robust WallOK strip. Closure along one chosen tail
is weaker than the universal far-bit condition used by no_wall.

Pure ether itself never erodes; it violates the finite theorem's nonempty
defect premise and the extension's white-tail/witness premise. These checks
reject overstatements, not the actual source. No carrying circularity found:
finite erosion uses local certificate/right edge, no_wall then uses erosion;
white-tail erosion uses an independently established speed-one witness.

Reasoned/gut: useful unbounded source mechanism in this precise background.
Review COMPLETE. No period-three prize claim, CQ01/all-widthD(W) transfer,
new potential job, Local wake, held-lane reopening or schedule change. A new
application needs its matching-driver and bounded-witness hypotheses proved.
