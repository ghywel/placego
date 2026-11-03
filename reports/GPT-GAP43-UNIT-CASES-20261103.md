# Can unit propagation explain the original43 shield? — GC2467

GPT, Intel, 3 November2026. **FROZEN, not run here.** One read/propagation
pilot on the unchanged original CNF. GPT owns it; Local no job requested.
No SAT search, target/horizon/cutoff change or proof-support minimization.

## Pull and discriminating test

GC2466's replayed refutation uses only initial44 from the free initial
region44..137, while retaining many internal correlations. Can that proof
be replaced by deterministic unit propagation, perhaps after exactly one
binary case distinction? This is a diagnostic of the proof, not a claim
that Rule30 has one-bit memory.

**Prediction:** root propagation is inconclusive, but initial44=0 and44=1
each give a propagation contradiction. The stage tests root first and does
not run either branch if root already contradicts. That simpler outcome
would also be informative. An inconclusive branch refutes this proposed
explanation, while the existing original LRAT UNSAT remains unchanged.
No unresolved result is called SAT, and no further branch is selected.

**Counterfactual/stop:** source/hash/model/control, reason replay, thermal,
pressure or checker failure stops and preserves the stage. No automatic
retry, assumption search, additional variable or longer limit follows.

Record searched: GC2410/11's complete `unit_closure` and `replay`, GC2406's
positive RUP function, original GC2438/2440 CNF/model/unchanged-checker
evidence, and completed GC2465/66 support source/results. Current actual
kitc42f6e51 and last complete index04:35:16Z, Local04:40; refresh due about
06:05Z. This reuses known unit propagation/RUP, not a new proof method or
novelty/submission decision.

## Frozen source and inputs

- `tests/probes/gap43_unit_cases.py` SHA256
  `419565f74187846add42aa97d662ef23fce924311406713e6482bb4109e2d623`;
  AST parsed only before publication.
- Two pure functions loaded by AST from `guarded_wall_boundary_screen.py`,
  SHA256`ac9cc3d6e1f93e0ce6f95a7a04f8373650301114c3a1c609bdab02b2d5564db4`.
  Its old main/obligations are never run. No helper globals beyond builtins.
- Pure `rup` from `guarded_wall_proof_support.py`,
  SHA256`a4a4deb8c8f48b32befd5878910145a3e160ec4350d4e358223a56cb69fc7df8`.
- Original gap43 CNF2be93cfbb953c4959a10615cb6cdc3163616c5409818e997c697b553d2bfca67,
  36,058variables/214,305clauses/4,851,407bytes. No protected61 units or
  extracted support replaces it.
- Complete baseline f7077a90bf28a7e748a20a04bfc3926c13b28033b4b72e770a6ecc34a43c24fe;
  flip43 model7cf93283d323b9df0076ff3bc19df0590f9f250a7900f3a925ea55d75083ff92.
- Unchanged cake_lpr445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23.
  No CaDiCaL, GPU or other solver executable is invoked.

## Fixed controls and trace/certificate obligations

Tiny controls: propagation, immediate conflict and incompleteness of unit
propagation; a four-clause formula that needs the two cases of one variable;
case-reason translation checked by independent RUP; corrupted reason
rejected. Known-good microLRAT is checked; an empty proof must give its
rejection diagnostic and no verified marker, irrespective of exit code.
Both complete retained models are checked against every original clause,
failing only the goal/input43 unit respectively.

Each closure records every forced literal with its reason clause, passes
and a conflict if found. A separate sequential replay validates the trace;
an inconclusive result gets a full fixed-point check. Only if root is
inconclusive, run exactly the assumptions−297,+297 (initial44=0,1). Each
assumption is prepended to an in-memory clause list, shifting original
reason IDs by one. The original CNF bytes remain unchanged.

If root contradicts, its reason sequence and conflict form one RUP addition
of the empty clause. If both cases contradict, translate each trace back
to ORIGINAL IDs, omit the assumption's reason, and RUP-check a unit opposite
that assumption. The two opposite units then yield an empty clause. This
gives at most three LRAT additions, with potentially long hint lists;
there is no claim of a small literal-level argument or minimal proof.

Any successful exported LRAT is checked by the unchanged cake_lpr against
the **ORIGINAL gap43 CNF**, never an assumption-augmented formula. Require
rc0 and `s VERIFIED UNSAT`. Only such a receipt is called a checked short
refutation. If a case is inconclusive, no empty-clause certificate or new
global result is asserted. The previous original refutation is untouched.

## One conservative envelope

One serial nice10 worker with serial checker/helper children, taskthreads≤2,
max5processes. Outer run_capped35 per-process CPU/120wall/768MiB sampled
treeRSS,4MiB/file,16MiBstage,track-tree. Worker own hard25CPU; worker
self+reaped-child aggregate guard40 at every thermal/tool boundary. Micro
checker1CPU/4wall each (two), final checker10CPU/15wall, heap384MiB/stack64MiB.
Completed outside whole-tree budget120CPU. Per-process limits are not
aggregate enforcement; preserve actual whole-tree time and monitor scope.

Fresh actual load/headroom and thermal gate; free+inactive4096MiB launch /
3072MiB floor,swap-growth64MiB, thermal speed/scheduler100 before/after each
closure/tool and at end. No concurrent heavy job. Failure stops/preserves
without retry or cap relaxation. Outputs/models/trails/proof/receipts stay
outside git with digests and verified raw-body shared-store transfer.

Publish before launch. Next record ROOT contradiction, both-cases checked
refutation, inconclusive split or exact failure, then let that outcome
choose a different representation rather than add assumptions automatically.
Independent alternative: a genuine shared-history return-packet relation
from Local; another isolated ancestor layer is parked.
My own pull: a two-case propagation explanation would turn an opaque solver
proof into a concrete statement about where an uncertain bit is absorbed.
