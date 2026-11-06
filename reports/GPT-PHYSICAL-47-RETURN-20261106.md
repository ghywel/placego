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
row. Its sampled duration is34+62+83=179, hence358 physical ticks after the
first white phase. To use the kit's exact u(R,s)=column1 at1+2s convention,
include one initial black-center update. Total horizon359; divide the cone
at ticks1,69,193: initial phase, first E, and4 segment. The shared rows after
E and4 have291 and167 cells; the initial cone has360 cells and the final one1. The same variable IDs at each
seam must serve both neighboring slabs. Zero continuation of the360 initial
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
cells and an independent integer updater through all359 ticks, including both
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

The first stage completed: raw fibres below, physical query **UNKNOWN** at its
fixed60,000-conflict budget. No witness or UNSAT certificate. There will be no
conflict-budget increase. A changed representation is frozen below before its
small replay.

Source/input freeze:

| File | SHA256 |
|---|---|
| physical_47.py | f7751b7ef59021e3895511221d78f2deb79b019080c32febf92057baf33eea7d |
| intel_worker.py | 2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94 |
| stage.py | ba9696782abbee65ffcd3433e78848f1de82647a4f8033ab1e6a5c6cbdaaa09a |
| run_capped.py | 26f850a8c1ba3905e00093cfa52331e94ee3d48ebe41c8b69b90b735b0a5ec3b |
| dfa_xx_W38_c0.txt | 465c2cfd8b303db816c439d237c760c1a28f6766fdda10e56a8df37cbcde68e4 |
| dfa_xx_W39_c0.txt | 7972a731983ef9baa397a9107283f5e34b4b6429e091bf24c08e673c7f089aaf |
| dfa_xx_W40_c0.txt | 0323f4a3bb60717f97c432c378e61cd85feacd1a9097ce667396de58d196167a |
| dfa_xx_W41_c0.txt | 0d0231db4179ab4ac79eb9409933beefe313d9c4a1473cffcbe7ee6bd0b9593c |
| gc2707-plan.json | f3227bf47c9366c2d514c04251f766617c5ba12dd7cff231481d63e6d0ab9aa6 |

## GC2708: exact finite ancestry at the seam (freeze before replay)

**Change of representation, GPT-owned.** The fixed solve finished in9.53wall
seconds,9.505429 accounted worker CPU plus0.248supervisor CPU. Only413 of64,981
variables were forced by unit propagation. At the main167-cell seam, only its
head bit was forced; the other166 are unassigned by UP, not proved logically
free. The known corridor law did not materially reduce this cone.

For finite right halves let B_b(X)=((X<<1)|b) XOR (X|(X>>1)), with cell1 the
least significant bit. The kit's `Rule30Predecessors.T`, `back`, `lin_back`,
`eq_back` already reconstruct predecessors from the right. Its white-tail
specialization has a unique candidate: set x_N=x_(N+1)=0 for an output Y of
width N, and descend

    x_(i-1) = Y_i XOR (x_i OR x_(i+1)), i=N,...,2.

Accept iff Y_1=b XOR(x_1 OR x_2). Y=0 and Y=1 have predecessor0 precisely
for b=0 and b=1 respectively. The rightmost-disagreement argument also proves
injectivity on finite right halves, already covered by the kit's
`Preimages.eq_of_evol_one_eq_of_right` in the full-line setting. Thus whole
finite histories cannot merge under a prescribed drive; a predictive reset is
a projection. No new inverse theorem is claimed.

Put m=193 and v_t(k)=x^t_(k+t). The inverse recurrence becomes

    v_(t-1)(k) = v_t(k) XOR (v_(t-1)(k+1) OR v_(t-1)(k+2)).

Sweep M's cells j from the right, with k=j-m. This needs two stored diagonals
for each unfinished predecessor row. At spatial cell0 check its prescribed
center b_t=(t even); at cell1 check its head if the past word prescribes it.
Start at j=max(width(M),m+1), filling leading zeros, so no early boundary or
head check is skipped. A row can be discarded after its center check.

After consuming through j=168, center checks for times0..25 and heads through
time26 have been exposed. The live rows are26..192:167 rows,334 bits. The
remaining input is M's first167 cells, sufficient to determine the next166
physical ticks of the head. This is an upper bound on a sufficient state,
not a minimal automaton or an enumerated334-bit state space. The tail must
generate the same state consumed by the prefix; selecting arbitrary states
would erase the physical compatibility condition again.

**Exact target (PROOF-SKETCH pending Local carry):** the original finite
E A^4 E A^7 E query has a witness iff there is a finite M of width<=553 such
that (i) its193 inversions with boundaries b_192,...,b_0 succeed and their
odd-time heads1..193 match E A^4 E, and (ii) its first167 cells give A^7 E
at odd ticks193..359. The width bound corresponds to the original360-cell
root: a nonzero finite row grows by one cell at each step, and the zero root
becomes nonzero at the first b_0=1 step. Both directions follow by joining
the reconstructed past to the forward evolution of that same M. Ancestors
alone, without their head checks, are insufficient. Requiring width41 X
membership throughout the future would instead require207 cells; this
query imposes no such membership.

**Bounded replay, prediction written first.** Implement the sequential inverse
and diagonal scan independently. Exhaustively compare one-step inversion with
a forward lookup for both boundaries and every output<2^13; compare accepted
and rejected multistep histories, zero padding and a corrupted past-head guard.
For one fixed control, take seed19 at physical time193 and flip cell168.
Prediction: both full rows have the same future head through166 steps, while
the modified row fails the prescribed193-step ancestry. If it survives, retain
that counterfactual. This is a control, not a4,7 witness. Even rejection excludes
only the changed full row: the shared prefix still has the original valid
completion. No sampling, seed search, CNF solve or enlarged horizon.

Record searched: GC2706/2707; actual kit Predecessors transfer/reconstruction
proofs and Preimages right-asymptotic injectivity at9d837cd5; PR208 ancestry
statement retained as context, not used as a carrying theorem. Existing
column-word-tree/preimage literature supplies the recurrence; the present
work specializes the interface to the4,7 cut. No novelty/submission claim.

One serial18CPU/70wall worker in a30 aggregate-CPU/90wall stage, worker stop20
and10CPU supervision reserve. This plus the completed9.76CPU stage stays below
the block's120CPU cap. Other frozen host/pressure/output/process limits above
remain unchanged. Source `physical_ancestry.py` SHA256
`a7071cc2e836c22fd56c565370be7d4b65cc4f4eb6aaa2c4dca4b8b31c473701`;
plan `gc2708-ancestry-plan.json` SHA256
`f3e732af24bc770ba657f6b53fcc59ab19639c1b826883da0ef4c9a19f26603e`.
The wrapper/stage/monitor hashes are unchanged. This replay passed:16,384
one-step cases,768 accepted/rejected ancestry cases,32 seven-step seeds,
wrong-head rejection and leading-zero invariance. Seed19's time193 row and
its cell168 mutant have equal heads for166 future ticks; the mutant's first
sequential inverse rejection is at boundary time169. The diagonal scan
rejects as soon as it exposes boundary time25. These are different scan
orders for the same failed ancestry, not a contradictory failure time.

The first launch was refused before spawning a worker because the sandbox
denied `sysctl` access. The refusal receipt is retained. A separate permitted
preflight checked headroom, swap and process monitoring; the unchanged
source/limits then ran with all monitors active. Completed worker CPU0.342199s,
supervisor0.124s, plus0.120s for the refused launch. No pressure stop or cap
bypass. The job was shorter than a full RSS sample, so sampled zero RSS is
not a peak-memory measurement; the worker's rusage peak was17,379,328 bytes.

## Tail completion sharpens the interface (PROOF-SKETCH)

There is a simpler interpretation of the diagonal boundary checks. Define

    D(X) = X XOR ((X>>1) OR (X>>2)).

For any drive bits, B_b(X)>>1=D(X), and D commutes with right shift. Induction
therefore gives, for the m-step driven evolution E_m,

    E_m(X)>>m = D^m(X).

On every finite w-bit space D is a bijection: recover x_i from the highest
bit downward using x_i=y_i XOR(x_(i+1) OR x_(i+2)). Consequently every finite
high tail q has exactly one compatible m-cell prefix, namely the low m bits
of E_m(D^(-m)(q)). The zero tail has root0 and the driven image of0, not
necessarily the all-white row. This is a specialization of known left
permutivity/triangular reconstruction, not a novelty claim.

At the4,7 seam, q=M>>193 is therefore a complete physical ancestry coordinate.
The original width<=360 root condition becomes q<2^360. It determines all193
lower seam bits, including the167 future-visible bits. The prescribed past
E A^4 E head word and future A^7 E word remain additional conditions. This
is an invertible coordinate change, not a dimension reduction or a witness.
Equivalently, once a valid tail has generated the334-bit cut state, each
successive boundary check determines the next low seam bit uniquely.

**Additional implementation control, frozen before execution:** compare the
tail-inverse completion with an independent forward lookup for every8-bit
tail at depths1,2,5,7, and reconstruct the already-fixed seed19 seam from
its high tail. Prediction: all1024 lookup cases agree and the time193 seam
is identical. Counterfactual: any collision, missing tail or completion
mismatch invalidates the implementation. This repeats the small controls
only because new code was added; no physical target search. Same30CPU/90wall
ceiling,18CPU worker,20CPU worker-stop and host limits; the total block ceiling
remains120CPU. New source SHA256
`6d55a6bd120120c34c81f12ea6d9a453a1754a1fafaeea92ac92e867ed1fe912`;
plan `gc2708-completion-plan.json` SHA256
`712ecab4df46fccc0d84b15707c7aef5dfba49f5d674de3a7bea9b8c0f245e6e`.
