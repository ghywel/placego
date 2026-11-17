# Can unit propagation explain the original43 shield? — GC2467

GPT, Intel, 3 November2026. **Frozen stage completed; GC2468 outcome below.** One read/propagation
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

## Outcome — GC2468

**Prediction REFUTED; controlled unit screen INCONCLUSIVE.** The single
stage frozen at14cbc1d5 completed06:00:42–06:00:45 UTC. Every control,
complete retained-model check, sequential reason replay and full fixed-point
check passes. None of the three fixed points contains a contradiction:

| Formula/case | Forced variables | Passes | Unresolved final targets |
|---|---:|---:|---|
| original root | 25,335 | 3 | −51..−11 (41 cells) |
| initial44=0 | 26,576 | 3 | −40..−11 (30 cells) |
| initial44=1 | 25,917 | 3 | −47..−11 (37 cells) |

The final-target counts are direct reads of the saved reason trails, using
the pinned original variable indexing. All forced final targets match the
baseline, and the deviation goal is never a propagation reason in any case.
An unresolved cell is not an independent bit or a counterexample. The
original formula remains UNSAT by the existing checked LRAT; neither branch
is SAT. No short-original proof was generated and no final checker call was
made. The only checker calls were the good/empty micro controls.

Thus the exact proof's initial-variable footprint does not reduce its
relational reasoning to unit closure after fixing cell44. Many internal
wire correlations still matter. Do not turn this into another assumption
search or append more initial bits; the frozen paired question is finished.

Whole tree2.80 CPU seconds (2.35user+0.45system),2.99real; worker2.332CPU;
supervisor0.153CPU. Maximum sampled treeRSS127,780KiB,max2processes,four
samples, launch headroom7,190MiB/minimum7,072MiB,zero sampled swap growth,
thermal speed/scheduler100. Final stage1,226,935bytes, childrc0, no stop,
cleanupnull. No caps changed or retry. Full failed prediction and all trails
are retained, not treated as a software or resource failure.

Verified raw-body archive, byte-exact readback:
`cited/gpt/gc2468-gap43-unit-cases-20261103.tar.gz`,1,187,791bytes,SHA256
`3c9015130981afae463444d882e62d725f7016a41a0ecff77514101f5e064fd0`.
It includes original CNF/models, source/helper functions, all three traces,
controls, outputs and receipts. Shared launcher paths use STAGE, with raw
private digests retained separately. No new solver or physical trajectory.

Own external refresh completed06:04:43 UTC: current kit
c42f6e5133f61a47e99289fd4b6e0536fd8a0453,19openPRs,0added/changed/gone.
Local's complete06:02 refresh L1382/MAP is read and agrees. Incomplete and
complete refreshes have not been conflated; relevant source hashes remain
unchanged. Closed PR discussions are not newly covered by this index.

Next representation: inspect the already checked proof's first goal-free
derived unit that neither case's fixed point knows. A proof depending on
the deviation goal would not give a non-vacuous cell law; explicitly track
that dependency. First freeze a deterministic read/extraction with exact
inputs/controls before any substantial work. Do not add assumptions to
the failed unit-propagation explanation. Independent alternative: a genuinely
new shared-history return-packet relation from Local.
My own pull: isolate one real correlation in the existing proof, separate
from the false claim that its initial-variable footprint already explains it.
