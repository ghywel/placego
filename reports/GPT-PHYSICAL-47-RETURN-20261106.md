# Physical 4-to-7 return: keep the shared row

GPT GC2707, 6 November 2026. Owner-requested continuation of the
[two-state return automaton](GPT-BRIDGE-RETURN-AUTOMATON-20261106.md).
GPT owns this bounded block; no Local run is duplicated and schedules remain paused.

## The missing state, before computation

The raw gap DFA retains sets of possible current windows. Its two-state
quotient retains only their future gap languages. These are different objects.
At width41, initial E reaches raw state20 with31,339 windows. A^4 E reaches
state60 with14,865, then A^7 E reaches state200 with30,163. The quotient has
returned to R but the current-window fibre has changed. These numbers are
read directly from the retained tables; the planned checker below replays them.

Let B be all black windows of the chosen component, S_E=Post_E(B), and
C=A^4 E A^7 E. Since C ends in E, Post_C(S_E) is contained in S_E.
Post_C is monotone, so its repeated images form a decreasing chain. The raw
DFA can check this chain without reconstructing the large window graph.
This is a finite-window relation with exterior choices, not yet an actual
right-half return. The inclusion argument is PROOF-SKETCH pending Local carry.

For the physical query, retain the initial E as well as C. This anchors the
claimed start at an actual completed excursion rather than an arbitrary black
row. Its sampled duration is34+62+83=179, hence358 physical ticks. Divide the
backward cone into three slabs at ticks68 and192: the first E, the4 segment,
and the7 segment. Their shared rows have291 and167 cells respectively; the
initial cone has359 cells and the final one1. The same variable IDs at each
seam must serve both neighboring slabs. Zero continuation of the359 initial
bits gives a finite right half if the complete constraint system has a model.
There is no equality requirement on the initial and final row.

Known corridor law: at the white/odd phase,

    F(R)_1 = NOT(x_1 OR x_2 OR x_3),   F=B_1 composed with B_0.

Thus each sampled black forces a three-cell white corridor at the preceding
sample. This follows immediately by two Rule30 updates and is already reflected
in the kit's `Rule30CoupledGerms.double_corridor_of_u_succ_true` and its exact
germ factorizations. It is prior art, not a new theorem. We retain these forced
cells and the *whole remaining seam*, rather than erasing it to the R/S label.

## Frozen questions and predictions

1. Replay the raw C-return chain and exact unary return fibres at38–41.
   Prediction: C fixes a strictly smaller nonempty fibre after one return;
   the window-fibre reset threshold exceeds the predictive threshold7.
   Counterfactual: later shrinkage, an empty fibre or no longer reset threshold.
2. Construct the physical three-slab constraint and propagate all fixed trace
   bits before solving. Export the forced and free positions on both shared
   rows and the full simplified CNF. Prediction: the shared seam remains
   nontrivial after propagation; a symbolic reset to one state is insufficient.
3. One fixed physical E A^4 E A^7 E query, at60,000 conflicts, on the propagated
   reduced CNF. Prediction (tentative): a finite witness; counterfactual UNKNOWN
   or uncertified UNSAT, retained without a larger conflict budget. This is the
   newly identified4,7 cycle and an explicit shared-row encoding, not a repeat
   of GC2698's all4/all6 queries. No claim that propagation itself adds a new
   implied restriction: it preserves the original trace CNF.

Controls: fixed small rows replay the phase and both seam conventions; reversing
one observed bit rejects the fixed row; every reported propagation assignment
must be independently replayed as unit propagation on the original CNF, and a
corrupted assignment must fail. A positive target model is replayed by scalar
cells and an independent integer updater through all358 ticks, including both
complete shared rows. An UNSAT solver answer without a separately checked proof
is not a certified exclusion. A literal trace witness need not remain in X at
every intermediate step; X membership is not silently imposed or asserted.

Record searched: GC2698/GC2706, L1569/L1572, original lift.c subset semantics;
record_find column-word trees, shared interfaces and physical returns; actual
kit CoupledGerms corridor equations and current source index at9d837cd5,
portal21:02:12Z. The adjacent-column extension relation is standard Rule30
preimage logic; no novelty claim about the encoding or corridor law.

## Resource plan

One serial Intel Python worker, one thread, nice10, under run_capped and the
existing aggregate-accounting stage driver. Ceiling120 aggregate CPU/300wall;
worker stop105, individual100CPU/240wall,15CPU supervision reserve. RSS8192MiB,
launch headroom4096MiB, running floor1024MiB, swap-growth4096MiB, at most6
processes,16MiB/file and128MiB/stage. A pressure/thermal/monitor/control failure
stops the stage. Source and plan hashes follow before launch. No GPU, Lean,
new window lift, seed census or adaptive increase.

## Outcome

Pending the frozen computation.
