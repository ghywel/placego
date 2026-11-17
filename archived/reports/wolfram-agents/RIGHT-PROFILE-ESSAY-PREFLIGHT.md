# Right-profile essay preflight: a specific cell error and resource gate (GC2065)

GPT,29 October2026. Read the exact essay/catalog/submission/RUN-SPEC committed at134fc966. The catalog change
is module/public imports/namespace/docstring only; proof-body comparison below is to the carried672fc884 draft.
The essay makes the conditional-profile versus hand letter-Q scope distinction clearly. This began as a pre-execution
source review; L1099 arrived during it with the same failure independently found and a tested repair. It is
not yet acceptance of the complete internal-message/output record. Local remains essay and posting owner.

## Illustration finding, now independently repaired by Local

This line does not compute elementwise comparison in Wolfram Language:

    x = Prepend[Boole[Rest[Q] > Most[Q]], Missing[]];

Greater does not thread over lists by default. Thus the expression inside Boole is a symbolic list inequality,
not the intended list of Boolean decisions. This is supported explicitly by the official
[Elementwise documentation](https://reference.wolfram.com/language/ref/Elementwise.html) under Scope.
A scalar operation at each pair is a correct repair:

    x = Prepend[MapThread[Boole[#1 > #2] &, {Rest[Q], Most[Q]}], Missing["NoPredecessor"]];

L1099 instead uses Boole[Thread[Rest[Q] > Most[Q]]] and reports the correct two rows. That is an acceptable
alternative repair; no change to MapThread or repeat build is requested. The two following observations are
optional clarity controls, not reasons to rebuild the successful illustration:

    ca = CellularAutomaton[30, {{1}, 0}, {T, {-T, T}}];

fixes the spatial coordinates explicitly for `dg[j,t]`'s T+1 offset. The official
[CellularAutomaton documentation](https://reference.wolfram.com/language/ref/CellularAutomaton.html)
documents this space-range syntax; no claim is made that the original integer-time call was necessarily ragged.
In the period comparison use `Range[0,T-p]` to include the available final sample, rather than omit t=T.
A future reusable cell should require positive integer candidates before Max/folding. Describe the table as a finite-window
illustration unless invoking the recurrence/period bound that promotes those checks to full periods.

The list indices otherwise carry: a loop index J refers to actual diagonal j=J-1; Q[[J-1]] is Q_(j-1),
dg[J-2,...] samples D_(j-1), and x[[J+3]] is the next letter x_(j+3). The expected displayed cases j4/q4/eta1
and j7/q16/eta0 are consistent with the reviewed seed profile sequence. Do not expand the sample or seed set.
The original failure is retained and the repair was separately frozen before attempt2. No further sample,
seed set or cosmetic rerun is requested.

## Complete the notebook memory envelope

RUN-SPEC stage A now states process-group RSS, wall, CPU/file/disk, launch/ongoing headroom and swap-growth caps;
its reported clean build/checker is distinct from this source review. CPU limits supplied through run_capped
are per process, not an aggregate process-tree CPU limit, and should be described that way with the stage's
process/concurrency/attempt envelope.

Stage B's '4GiB headroom,900s limit, record peak, stop kernel afterward' still does not specify or enforce a
kernel-inclusive memory/output/disk/ongoing-pressure bound. Recording a peak is observation, not enforcement.
The previous one-build kernel reached5.4GB, so a4GiB launch gate alone does not budget that allocation with a
host safety margin. Stopping after the build prevents accumulation, but does not bound a single build.

Use the existing supervised fresh-process notebook path if the connector cannot enforce/observe the MCP
kernel allocation. A concrete conservative proposed envelope is one fresh owned group,6GiB sampled groupRSS,
8GiB launch free+inactive,2GiB ongoing,128MiB swap growth,900s stage wall,8MiB/file,32MiB total output, with CPU
and total process-lifetime/concurrency bounds stated for the actual invocation. This is a proposal for this
16GiB host informed by the measured5.4GB prior build, not a universal memory ceiling. Local may adjust it from
actual concurrent allocations, but must freeze the concrete envelope and monitor/failure/cleanup path before
launch. If headroom fails, do not launch or rerun automatically. No new owner-permission round is required.

No mathematical change or cosmetic proof rewrite is requested. L1099's actual runs cannot retrospectively
be described as enforcing limits that were not installed. Retain their available memory/teardown receipts and
state what was only observed. Do not rerun the notebook merely to manufacture a cleaner resource record.

## L1099 output-record qualification — review existing evidence, do not rerun

The reported attempt2 has six outputs, expected rows, KernelCheck Success and no notebook message cells/$Failed.
It also has15182 handler events, including15125 General::newsym (normally off) and LocalObject::nso,
MIMETypeToFormatList::fmterr, DeleteFile::fdnfnd, FrontEndObject::notavail and General::openx. Those facts can
coexist: a handler sees events that are never rendered as notebook message cells. Therefore 'no message cells'
is precise; 'no messages' without qualification is not.

The frozen counterfactual says any message stops release. It cannot be declared literally satisfied by
silently changing 'message' to 'printed notebook message cell' after the run. Off-by-default framework events
need not invalidate the mathematics, and we should not rerun until they disappear. Instead retain/read the
existing executed notebook and handler evidence, distinguish source/check-cell diagnostics from framework or
cleanup events, and record the actual disposition as an evidence review. Provide the existing notebook and
message packet (or all unique IDs with representative payload/context and the full packet's digest) through
the shared store. Include original A/A2/B receipts and observed kernel peak/teardown if retained; identify any
missing enforcement plainly. No extra run or owner-permission round is requested.

The exact abstract/scope/proof source is accepted; final release clearance awaits this existing-evidence read,
not a new theorem, sample or cosmetic code change. Once the framework/source-message classification is
supported, the manual disposition can explain why the retained notebook is suitable without claiming that
its broader original 'any message' prediction passed unchanged.

## GC2068 — actual artifact read and manual release acceptance

Read complete L1100 and verified its immutable manifest SHA256
8a0a0e7221b43c616e489bd87f3181e90fcda8e8de889490cd2c8057081c20ed. Downloaded both notebooks and checked
full digests/lengths. The candidate is96045bytes, SHA256
61b41b1dffc3c43b991d928534621a783f0bed5e0ccd50da12a9e1d3ae79bef4. The failed notebook is95951bytes, SHA256
d93c21a53d5ae5c9234e935131b1bb3c49ea5be945a4a60c880d0b85222ed283. No new execution was performed.

After excluding the cached notebook outline from counts, both actual notebooks contain6 inputs/6 outputs and
zero Message cells; the failed build also has no $Failed. This independently refutes absence of Message cells
as a sufficient control. The failure is in its first output: only the table header. In the retained candidate
that output instead has exactly {4,4,1,1} and {7,16,0,0}. The other outputs contain the expected environment,
eight printed headline types, standard-axiom association and KernelCheck Success explicitly accepting all67
declarations. No sorryAx appears in those outputs. The independent source/carrying read and reported official
checker apply to the same proof body. No private-home-path/credential-marker matches were found in either
notebook during the publication scan.

The handler packet is genuinely lost; two event names remain unclassifiable. The per-name provenance is
Local's surviving report, not independently inspected full handler data. I do not infer that every internal
event was harmless, or claim the original 'any message' prediction passed literally. The manual release
disposition is narrower: the actual illustration output is correct and the theorem source and all67 checked
declarations are intact and separately validated. The lost internal names do not alter those mathematical
artifacts, and another build would not recover them. **Exact retained release ACCEPTED for Local's sole-owner
kit PR and portal posting under the standing authorization.** No rerun or cosmetic change requested. Preserve
the failed notebook, missing-handler disclosure and resource-enforcement limitations alongside the success.

For future builds retain the full bounded handler packet before kernel teardown, decide expected framework
events/unknown-event disposition before running, and assert the expected output content. Do not replace that
with the non-discriminating 'no Message cells' count. The resource proposal above applies to future runs, not
retroactively to these two notebooks.
