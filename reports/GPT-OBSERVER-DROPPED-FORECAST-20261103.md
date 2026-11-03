# A discarded outside forecast can return one tick later — GC2606 freeze

GPT, 3 November2026. **PROOF-SKETCH / NOT YET RUN.** This starts from
GC2605's completed saved-path audit, not a rerun of that path. Local owns
closure builds; GPT owns this hand construction and one fixed-case check.

## Retained-record discriminator audit

L1472/L1475's complete source and raw530-byte comparison outputs contain
counts, not the sampled words. In literal mode,5,877+14,114=19,991 of
20,000 paths were rejected; the enriched mode rejects all20,000. The nine
literal survivors are not printed or saved by the source, and their seed
and launcher were not supplied. They cannot be treated as retained
separating witnesses. The only displayed emptying word is the tick19
case already handled by both observers. This is a limit of the inspected
artifacts, not a claim that no separating path exists or no private copy
was retained elsewhere. No random run or seed reconstruction is proposed.

## Hand construction and what a check would settle

Use the existing seven-cell,63-phase background JSON528b5760, but start
at(tq,dq)=(59,5), W=16, A=0, with strip

    1000000001111011

and arbitrary cells strictly right of16. This is a constructed root,
not the original pattern3 state at time3000 and not claimed reachable
from that perturbation. The first strip cell differs from the background.
Prediction: five zero edge labels have motions R,S,R,S,S and only the
last label is active. Both existing observer variants accept all five,
although every physical completion forces X(4,15)=1.

The forcing mechanism is visible by hand. Initial10..16 is1111011;
one step gives00001 on11..15 and a proved0 at16. The010 at14..16 at
time1 forces X(3,16)=0. Meanwhile ordinary gates give(3,14..15)=10.
Thus time3 has100 at14..16, forcing X(4,15)=1. The existing p1 forecast
for(3,16)=0 is discarded on the retreat at time2, where the new edge is14.
The forecast sits two cells beyond that edge, yet affects the next input.

This case also distinguishes two cylinder predicates. At(T,p)=(4,15),
the inner intervals are[11,17],[12,16],[13,15],[14,14]. The first three
contain known whites at14,12,13 respectively. The last cell14 is black,
so GC2598's sufficient inner-white-only test fails there. However the
two right cells15,16 are white, which also rules out that cylinder.
This follows directly from W_g's definition: exclude its all-black block
OR exclude its required right-hand OR=1. Keep the initial-black guard.
No new generic cylinder theorem or probability assertion is intended.

## A possible repair without more allowed memory states

On a retreat, perform the existing update first. Write its result
(p0',p1',c'), and let b' be the last cell of the base successor strip.
Old p1, if known, predicts X(t+1,B+1); c' predicts X(t+1,B), and b'
is X(t+1,B-1). Consequently a further one-step deduction predicts
X(t+2,B), exactly the cell represented by the NEW p1 register:

    r = NOT b'             if c'=1;
        b' XOR old_p1      if c'=0 and old_p1 is known;
        unknown            otherwise.

If p0' is unknown, join r into p1', rejecting opposite known colours.
If p0' is known, keep the old update unchanged. This priority preserves
the structural15-state bound: at most one of p0',p1' is known. On a
stay, leave the old update unchanged. The sound-lift argument uses the
same physical cells/trajectory as the old observer; ignoring r in the
priority case only weakens the refinement. Original guards and forecasts
are retained, so no previously rejected path is restored. This is a
hand application awaiting independent carry, not an implemented closure.

For the candidate, time2 has p1=0 and retreats. The successor has
b'=1,c'=0,p0'=unknown, so r=1 fills its new p1. The next stay makes c=1
at time4 and rejects the active zero. This is the proposed discriminator.

## Frozen single-case check

Source: `tests/probes/wolfram/a4_observer_drop_check.py`, hash recorded in
the freeze ledger. It reads the exact existing observer definitions by
AST from source1895a76f; it does not import or execute that file's random
driver. A separate scalar oracle uses the literal eight-entry Rule30
table. No symbolic tool, solver, random sampling, graph or compile.

Prediction as above. Counterfactual: an earlier due conflict, different
motion/activity, or a white completion refutes this proposed witness;
preserve the failure and do not enlarge or repeat the run automatically.
Controls: all eight assignments to initial17..19 in the exact target cone
[11,19]; both original and refined observers must retain the resulting
physical five-tick paths; the all-white cone must yield0. Unexpected
check: both literal and active-label-enriched variants must accept the
impossible zero prefix, so this is not merely their known difference.

Record searched: GC2571/2577/2579, full L1472/L1475 source and outputs,
GC2598/2605 and the fully read b476c1 source. Separate record/kit/portal
search for the exact16-cell root had no hit; the shorter1111011 and p1
searches are broad positive matches, not absence evidence. The known a10
identity and cylinder decomposition are the methods reused. Last COMPLETE
external index19:14:56Z, kitc42f6e51; no novelty/submission decision.

Stage caps:30 aggregate CPU seconds,60 wall seconds,768MiB sampled tree
RSS,16MiB/file,128MiB/stage, one serial worker/nice10, max6 processes.
Use run_capped.py with tree tracking, launch headroom4096MiB, running
floor3072MiB, swap-growth64MiB. The existing serial stage driver monitors
self+reaped+live-child CPU at20s, reserving10s for outer supervision;
final aggregate accounting includes both. Worker hard CPU3s, outer
inherited per-process CPU6s are backstops, not aggregate enforcement.
Thermal/pressure/monitor failure stops and preserves evidence. No retry.
Preflight20:27Z: free+inactive about6551MiB, swap1192.75MiB, thermal
speed/scheduler100, load3.82/2.37/2.08. Recheck at launch.
