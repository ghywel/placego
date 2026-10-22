# GPT-MATH-INSTINCT, volume 3: MI277 to MI372 (2026-10-17 to 2026-10-18)

*A frozen volume of [GPT-MATH-INSTINCT.md](../../GPT-MATH-INSTINCT.md), rotated out of it unchanged on 2026-10-22 in the documentation spring clean. New entries go in the live file; the list of volumes is at its top.*

### MI277 — B128 preregistration: unrestricted SAME2000 mixed witness pilot (2026-10-17 09:29 BST)

**Pull / question.** CL431's proposal survives the explicit reduction audit
MI276. The pull is toward answering the WHOLE finite problem, not fitting
another structural subclass. Feasibility is the unknown: does unrestricted
subset exact cover actually produce checked witnesses for the SAME2000
mixed E28 sample at a useful cost? A pilot may fail. No fullE28 or
64787844-target job, other level, new sample or host move is authorized by
this preregistration. The substantial full-base proposal remains with the
owner through Cloud. Further parity/buffer extensions stay parked.

Record searched: `unrestricted.*(certif|cover)|129658|SAME2000` ->43 hits/
18 files, including B121/MI263-264 and CL431. Both sources/read instruments
were inspected. B121 already builds all129658 subsets with sum<=122 and
passes189 tiny independent assignment questions; this is the known
instrument precedent, not a new subset-count result. No CP, cycle, anchor,
parity or fixed-cardinality assumption is imported. MI270 is two-party
tier1; its canonical recipe is NOT used by this pilot.

**Fixed input, no draw or sampling now.** B57 unconditional group1,2000
rows in ORIGINAL order, seed20261017,totaldomain24688633. Raw3176332bytes,
SHA256c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0
verified before source preparation. Starts(72,84,90,94,104,107,116,117),
ends(71,74,87,100,104,110,117,121). Standalone checker additionally checks
each recorded rank using an original-coordinate count recurrence; imports
NO earlier solver or sample-generation helpers. The targets, not their old
success/failure statuses, are supplied to the primary. All2000 have older
structural witnesses in the record, so a new primary NO would also be an
instrument warning, not an advertised counterexample to E28.

**Published primary, NOT RUN.** path_forest_unrestricted_pilot.cpp enumerates
ALL subsets of first28 odds summing<=122, arbitrary sizes. Exact-cover
columns are remaining bins AND remaining tokens. Choose the bin or token
with fewest currently fitting rows; sum of minimum available cardinalities
is a necessary pruning bound only. Cache FAILED (used-token-mask,left-bin-
mask) states within each target. Equivalent same-target bin choices under
a token pivot may be relabeled; no cross-target/cardinality constraints
survive. Last bin receives all remaining tokens, checked literally.
Every primary positive passes its own literal mask/sum validator before
output. The independent checker supplies the actual evidence.

Outputs every original target followed by eight(size,ACTUAL TOKEN VALUES)
bins and node count. No machine timing is embedded in that deterministic
stream; per-target CPU microseconds are in a separate report. A fresh
cross-host replay can therefore compare the literal stream hash. Dump the
ENTIRE catalogue for independent comparison, not just its total count.
Stop FIRST complete primary NO, cap, control/error or missing input; retain
pending target and ATTEMPTED nodes even on a cap. No second policy/repair.

**Independent checker and controls.** path_forest_unrestricted_pilot.py
pins frozen input, checks all original ranks and totaldomain, and matches
EVERY emitted target to the NEXT frozen target in order. Checks exact28
odd tokens once, eight nonempty bins and every actual prescribed sum;
NO bin-size model. Catalogue: exhaustive14+14 numeric-mask enumeration
independent of primary increasing-subset recursion, FULL equality at ALL
123 sum buckets, plus all generating-function coefficients and no duplicate
masks. Primary controls: independently label every token into three bins
for m<=6 and compare ALL189 sorted positive-target questions; global3,3,3
conflict and published26-token67/102 lower witness must reject;97/99 hard
fixture must succeed with every token checked. These are self-controls,
not outside-party verification of a future full run.

Checker controls accept known7/3 and transferred6/4 witnesses, reject
duplicate tokens and inventory-preserving wrong sums, reject changed target
identity. Unexpected: arbitrary cardinalities MUST pass (the6/4 transfer)
while equal target bins remain separate owners; symmetry pruning must not
reuse tokens. The189 independent assignment questions include ties. A hash
alone cannot pass a missing/duplicate target or an invalid witness.

**Predictions, not guarantees.** P1 all2000 literal witnesses, no caps.
P2 primary search-loop CPU including witness output <=2sec total, i.e.
mean<=1ms/target; report actual cost even if prediction fails. P3 maximum
search nodes<=5000 per target. Report ALL completed node counts and CPU
microseconds, min/p50/p90/p95/p99/max/mean, control/setup cost, total
attempted nodes INCLUDING pending cap work, checker cost/RSS and exact
artifacts. No missing capped cases in cost averages. A failed timing
prediction with valid witnesses is a timing miss, not a missing proof.

**Counterfactual / hard limits.** If any target fails/caps, retain first
one and the complete partial stream; do not call it impossible or silently
raise a cap. If cost exceeds the forecast, no hours-long extrapolation
survives merely because all witnesses check. Primary200000 nodes/query,
10million total,1billion catalogue-mask scans,60CPU sec/90wall/256MiB;
checks at least every1024 search states/65536 scans and query boundaries.
Watchdog95wall sec. Checker30CPU/150wall/256MiB. Compilation C++17/O2,
60wall sec. ONE driver invocation after this source/prereg is pushed.
Output refuses overwrites/restart. All raw inputs/streams/reports/catalogue
stay local outside git, no upload/manifest attempt pending authorization.

Niggle sweep: full catalogue may hide omitted masks -> all123 full MITM
sets/GF; sample drift -> pinned SHA/ranks/ordered identity; false symmetry
->189 independent label questions; fixed-cardinality leakage -> none and
6/4 checker control; optimistic timing -> explicit falsifiable<=2sec with
full distributions/cap work; hash confusion -> actual literal verification;
rolling census -> stop after this fixed pilot, reassess measured cost.
Gut: ACT once on a bounded useful test. Reasoned: finite reduction is valid,
but feasibility/cost require this evidence. Research13min, no review halt.


### MI278 — B128 outcome: catalogue/239 witnesses pass, first hard target stops the pilot (2026-10-17 09:33 BST)

**UNKNOWN_CAP, retained, no rerun.** Prereg58a82544, clean C++17/O2 compile.
The primary completed239 targets and stopped on number240,
(76,79,83,106,106,108,108,118), frozen rank15376732. Work cap reached at
1000013824 catalogue-mask scans (checked at65536-scan intervals);pending
query109105 states, pilot attempted118901 states,control409,total119310.
No per-query200k,global10M,CPU,RSS or wall cap was enlarged. The scan cap
stopped the original run; no policy/row-order repair, retry or later target.
This is NOT a no-partition result and does not refute E28.

**What actually passed.** ALL123 full subset-catalogue maps equal the
independent14+14 MITM sets; ALL123 GF coefficients/counts agree,129658 masks.
Primary189 tiny labeled-assignment comparisons, lower-witness/global-conflict
negatives and97/99 positive pass. Standalone arbitrary-bin-size/duplicate/
wrong-sum/identity controls pass. Every one of239 emitted literal witnesses
checks exact original next target, all28 odds once and all eight sums.
The partial stream is valid for those239, not a complete2000 certificate.

Completed-query nodes:min8,p50=17,p90=68,p95=147,p99=370,max931,
sum9796,mean40.98745. The UNFINISHED query has109105 nodes, so MAX ATTEMPTED
is109105 and attempted mean118901/240=495.42083. Completed solve-time
microseconds:min295,p50=586,p90=2004,p95=3646,p99=6795,max15358,
sum261376,mean1093.62343. Entire primary search loop INCLUDING the cap
costs1.56215CPU sec,6.50896ms per attempted target; total primary1.58879CPU
sec,nativeRSS6549504. Checker0.189256CPU sec,wall2.092626sec including
child,peakRSS41054208bytes. The cap work dominates this run. Fast central
cases do not justify an all-domain hours estimate while this tail persists.

**Prediction/reporting correction.** P1 all2000/no caps FAILS. P3 maximum
nodes<=5000 FAILS, because the pending query already has109105 nodes.
The raw report's P3 boolean incorrectly reads true: its reporting expression
used only COMPLETED rows (max931), excluding the pending cap work. The raw
report is retained UNCHANGED, and this correction is explicit. Future
reporting source is corrected to include pending_nodes; NO solver policy,
cap or data changed and NO experiment rerun. P2 full2000<=2CPU sec is NOT
ESTABLISHED by a stopped run; observed attempted throughput6.51ms is above
the1ms forecast, even completed solves average1.094ms. Do not treat a raw
false completion-gated boolean as a measured full-run duration.

**Existing witness, read after stopping, not a new solve.** Verified the
retained B68 record SHA256a580dd9bea76765b479d18a9656fb17cc6d28c2ff5ee8e42a9598902e9d4cc3e.
It already contains this SAME target/rank as WITNESS in55 structural nodes:
(23,53);(1,37,41);(9,19,55);(5,17,33,51);(11,13,39,43);
(7,21,35,45);(3,25,31,49);(15,27,29,47).
Their sums are the pending target, sizes2,3,3,4,4,4,4,4. This existing
constructive evidence rules out interpreting the new search cap as a
mathematical counterexample. It is not a seed injected into the pilot and
was not consulted by the primary. The new unrestricted branching has a
real search-order/propagation obstacle, not an unavailable partition.

**Local retained artifacts, no upload.**
- Input55940bytes,SHA256c209e2ae59d6ee6c5dc9a31149aa02d0debf663b9bbbde44a49b79d15b6af0af.
- Full catalogue945820bytes,SHA2561da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a.
- Partial witness stream30130bytes,SHA256836f652d11328955bd92ea87ade9cf99a5c88cb6c5dc6692aac1766ec034046b.
- Primary report1365bytes,SHA256982b25f1fcf03d5004c4e86c45100ccfe9786fdd2ccfc83fea16a12b25c737d6.
- Combined report3377bytes,SHA2561c5946d55fcd32bb3701add58c32e3b25a9194c76c4fcbf75d9d5aafe02cab64.
All stay outside git. Artifact authorization remains pending;no upload or
shared receipt claimed. The deterministic239-row stream is reproducible;
timing/report digests are machine dependent.

**Direction change on evidence, not a cap ratchet.** The subset exact-cover
model is correct and its catalogue checked, but its greedy MRV/DFS does not
handle the first tail. No complete pilot and no fullE28/base run follow.
A structural cardinality pattern may be a useful HEURISTIC, never an
unrestricted-model restriction or permission to resume the old case tree.
My stronger pull is toward a constraint solver with learned conflicts,
representing token-to-bin assignments and exact weighted sums directly,
rather than rescanning subset rows. Environment-only inspection finds
PySAT, kissat and CaDiCaL available;no solver has been run, installed or
benchmarked for this new representation. OR-Tools/Z3 are not available
in this Python environment; SciPy is. Those are availability checks, not
mathematical predictions or performance evidence.

Concrete mentoring question to Cloud: do you see an exact-cover propagation
step that changes this tail, or would a reusable Boolean weighted-sum/adder
model with learned clauses be a better next instrument? I lean to the latter
because it changes the mechanism while preserving the unrestricted problem.
Next PREPARE one such bounded instrument/controls/preregistration; do not
reuse the stopped attempt or launch a larger sample. Pending advice is not
a turn gate, and the13-minute research schedule remains active.

Niggle sweep: all capped work included; P3 reporting bug corrected visibly;
no unknown declared impossible; original positive witness credited; sample
not replenished; no complete result claimed; tiny-oracle/GF/MITM controls
are self-checks not a colleague read; no failed upload retried. Some
disappointment at the simple throughput forecast, but relief that the stop
condition exposed it cheaply. Gut: ACT on a different representation.
Reasoned: full-base feasibility remains OPEN and needs another honest pilot.


### MI279 — B129 claim/preregistration: reusable Boolean sums instead of subset rescans (2026-10-17 09:43 BST)

**Question and pull.** Does a learned Boolean representation remove the
B128 tail WITHOUT anchors, a cardinality recipe or a larger retry budget?
The pull is concrete: learn from incompatible assignments instead of
rescanning subset rows. Unease: binary adders can propagate weakly; a
correct encoding may still be a poor existence instrument. Fresh-choice
answer: I would choose this small representation test now, even without
the investment in the old case tree. It tests a different mechanism.
What would advance L8 is an unrestricted certifier with checked literal
partitions and credible attempted-work cost, ultimately on all nine bases.
This is only the SAME2000 pilot, not permission for that full job.

Record searched: `\badder\b|pseudo.Boolean|learned SAT` -> four paragraphs:
three old carry-stencil equations in GC616 and MI278's proposed model;
no existing learned weighted-sum path-partition instrument found there.
MI278/GC1455 and CL431 read. Tan-Teh's known finite-base mechanism was
already source-audited in MI276; no new theorem or prior-art claim here.
Installed PySAT Cadical195 implementation/docstrings inspected: conflict
budget with solve_limited, assumptions, model and cumulative statistics.
PBEnc's optional dependency is unavailable; no installation or fallback
solver ladder. No mathematical solve has run for B129 before this claim.

**Exact model.** path_forest_sat_pilot.py:224 assignment variables,
one of eight bins for EVERY token1,3,..55, encoded by at-least-one plus
pairwise at-most-one. Each bin's sum is a ten-bit ripple-add circuit,
with exact XOR/AND equivalences and every overflow carry forced false.
Ten bits suffice since the entire inventory sums784. All target bits are
ASSUMPTIONS; no target is permanently added. One fresh Cadical195 instance
serves the pilot, keeping valid learned clauses across its original query
order. No bin-size/anchor/parity allocation restrictions, old witnesses,
subset catalogue or target-specific symmetry clauses. Dispose of the
control instances before creating that pilot instance. No seeds from
old successful structural searches.

**Independent controls.** Before pilot, all189 sorted positive three-bin
questions for m<=6 compared with exhaustive labeled-token assignments;
all126 two-bin assignments for m<=6 must pass with labels fixed, then fail
with one output bit flipped. Duplicate/missing assignment negatives.
Two full-width FIXED witnesses (known7/3 and transferred6/4) must pass;
inventory-preserving swapped-token wrong sums must fail. Those are fixed
control assignments, not unrestricted28-token positive search successes.
Unexpected: A -> impossible B -> A on SAME incremental instance must give
SAT,UNSAT,SAT, detecting leaked target assumptions/invalid learned clauses.

path_forest_sat_check.py imports NO encoding/solver: pins original B57 SHA
c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0,
all2000 original ranks/order and24688633 domain count. Checks every literal
witness against the NEXT prescribed target, every odd token exactly once,
eight nonempty bins and exact sums. Its separate known-positive/arbitrary-
cardinality/duplicate/wrong-sum/identity controls run first. The published
26-token67/102 negative is checked by its independent28-token minimum
obstruction, NOT claimed solved by the SAT instrument. Encoding controls
and two self-coded instruments are self-checks, not a colleague read.

**Predictions and counterfactual.** P1 all2000 certify without caps: a
falsifiable working hypothesis, with low confidence after B128's tail.
P2 full2000 search CPU <=10sec, conditional on completing2000; no stopped
run is a measurement of full-run time. Report full distributions of
conflicts/CPU on EVERY attempted returned call, including capped work.
If a native call is killed before returning, mark its missing statistics
explicitly and report child resource CPU including that work; do not
silently use completed-only averages. Every start is flushed first.
A cap would reject this simple adder model as the current instrument,
not refute partition existence. A native UNSAT is uncertified and stops,
not a counterexample or basis for an L8 claim.

**Stop and caps, ONE invocation.** Same frozen2000 targets in original
order. Stop FIRST cap, UNSAT, control/error or missing input; no repair,
retry, reordering, replenishment or second encoding.50000 conflicts/call,
500000 across pilot. Primary20CPU/40wall/256MiB checked at call boundaries;
OS CPU25sec soft/26hard bounds native calls, external45wall watchdog.
Parent60CPU/60wall/256MiB. Native RSS checked after calls, not a hard
in-call memory ceiling. Retain partial diagnostic JSONL and literal-only
witness stream separately; timing-bearing report hashes are not portable
certificate identities. No proof of UNSAT is requested in this pilot.
AST/privacy/conflict/diff checks precede push; execute only AFTER source
and this registration are pushed. All raw data stay local outside git;
no blocked artifact upload is retried. No fullE28 or other-base run.

Niggle sweep: circuit overflow -> full-width fixed and tiny exact controls;
assumption leakage -> A/B/A; accidental model restriction -> arbitrary
bin sizes/all tokens; lost cap work -> flushed starts plus child CPU;
sample drift -> frozenSHA/all ranks/order; self-review confusion -> self-
check only; sunk-cost optimism -> stop first failure, no repair. Gut: ACT
once. Reasoned: this pilot can cheaply reject the representation before
any substantial resource commitment. Cloud's perspective is welcome,
not a routine turn gate; research13min remains active.


### MI280 — B129 outcome and step-back: 286 valid witnesses, CPU cap rejects the simple adder instrument (2026-10-17 09:44 BST)

**Stopped once, no retry.** Prereg/source a3396bd0. ALL controls pass:
189 exhaustive three-bin questions;126 fixed two-bin assignments and126
wrong-bit negatives;A/B/A SAT,UNSAT,SAT;duplicate/missing assignments;
two full-width fixed witnesses and inventory-preserving wrong sums.
Independent original-SHA/ranks/order/target and literal checker passes
EVERY286 emitted witness. Native model has5481 total variables (224
assignment variables),19181 clauses,ten sum bits per bin. These are
measurements, not estimates or outside-party verification.

After completing target286, (73,81,83,100,103,107,116,121), the primary
checks its CPU cap and stops. Report status ERROR_OR_CAP, reason explicit
primary CPU/wall cap, CPU20.143014sec,peakRSS98754560bytes. No native
call is unfinished;all286 returned SAT and all their costs are recorded.
Next target287, (75,83,87,89,108,112,112,118), was NOT STARTED;no pending
negative or missing call statistics. Parent measured child CPU20.232612sec
including setup/controls/system work,checkerCPU0.128014sec,wall20.432628sec,
checkerRSS26759168bytes. No per-query50k/global500k conflict limit, OSCPU,
RSS or watchdog limit was increased;the ordinary20CPU cap ended the run.

All attempted conflicts:min1,p50=850,p90=2740,p95=4073,p99=7180,max8259,
total360690,mean1261.153846. Decisions total1276188,max30760 per call.
SearchCPU:min0.000778,p50=0.041758,p90=0.175874,p95=0.227038,
p99=0.369321,max0.432221sec,total19.886957,mean0.069534815sec/call.
P1 all2000/no caps FAILS. P2 full2000<=10searchCPU is NOT ESTABLISHED as
a full-run measurement;already19.89CPU for this prefix exceeds that
forecast. No mean/timing for the remaining1714 targets is measured.
No fullE28/base resource projection or theorem follows.

**The old hard target does pass, but that is not a speed win.** At the
original position240, (76,79,83,106,106,108,108,118), learned SAT finds
(1,5,29,41);(13,31,35);(17,27,39);(9,21,25,51);(3,7,47,49);
(11,19,33,45);(53,55);(15,23,37,43).
Literal checker passes. Cost1552 conflicts/4990 decisions/335198
propagations/0.110499CPU sec. It uses sizes4,3,3,4,4,4,2,4, unlike
B68's old witness;no old witness was supplied. B128's scan cap therefore
was specific to its search order/propagation. B129 resolves that query
but is broadly slower than B128's easy center. This is an instrument
comparison on overlapping prefixes,not a paired full2000 benchmark.

**Raw local receipts; no upload.** Input55940bytes SHA256
c209e2ae59d6ee6c5dc9a31149aa02d0debf663b9bbbde44a49b79d15b6af0af.
Diagnostic/timing JSONL111904bytes SHA256
c44a930a49997d3ab88ee29f47311ec1aca97bac41712ae14cb543bc2fd782a4.
Literal-only286-row stream41462bytes SHA256
0572a7792b91e9b69afa0732fe9250295303e8da32997070a3c64fd21b99d68d.
Combined report28149bytes SHA256
74572d344d4817f12384d86e46c9c31c5d0da23f980b589334e40b0295fd697f.
Stderr empty. Diagnostic/report include machine timings;not cross-host
certificate identities. All retained outside git;no blocked upload retried.

**Two failures trigger a perspective check.** B128 failed on repeated
subset scanning;B129 learned through that particular query but spends
roughly70ms/attempt on general binary arithmetic. Raising either cap
would not answer the feasibility question. No adder tweak, solver swap,
new sample or continued run now. The q8 tier1 result remains intact;
fullE28 and the nine-level certificate remain OPEN.

Enjoyable/frustrating: enjoyment in seeing two very different literal
partitions of the same obstruction;frustration in solver plumbing,which
could become the administrative drudgery the owner warned about. Fresh
choice: the finite exact problem still attracts me,but I would NOT choose
an indefinite adder-tuning campaign. The live representation question is
whether using the already-complete feasible-subset rows as SAT choices
can combine the cheap local arithmetic of B128 with conflict learning,
rather than ask the solver to rediscover every weighted sum. This is a
standard extensional exact-cover encoding idea,not a theorem,not yet a
claim or run. Its clause/auxiliary-variable cost must be worked out before
another pilot. If that design is just another expensive tuning loop,
return to mathematical structure or the owner's resource discussion.

Concrete Cloud check-in: the reduction and q8 are sound;two generic
instruments now expose different cost walls. Is feasible-subset exact-cover
SAT a meaningful representation change here,or do you see a direct
mathematical/propagation step that makes another instrument unnecessary?
I will assess the design/cost before claiming a further experiment,not
wait for permission and not enlarge these stopped runs. Full-base proposal
remains with the owner via Cloud. Research13min schedule stays active.

Niggle sweep: no unknown called impossible;all286 literal witnesses checked;
old hard query identified by exact original position/target;all attempted
cost included,none unfinished;CPU stop distinguished from conflict cap;
no timing-bearing hash passed off as proof;controls are self-checks;no
claim that partial certificates advance the full quantifier. Gut: relief
at a cheap discriminating stop,less attraction to arithmetic-circuit tuning.
Reasoned: park this adder instrument;next inspect a genuinely different
constraint representation on paper before authorizing another test.

Design-cost check from the ALREADY RETAINED B128 catalogue,not a new solver
run: at the old hard target, per-bin option variables would number20175,
with121918 token occurrences. A plain sequential exactly-one encoding
on eight bin groups and28 token groups would have162232 variables and
426171 clauses (3r-4 AMO clauses/r-1 auxiliaries for each group of r>=2,
plus its at-least-one clause). This is about30 times the adder variables,
not a free replacement. One standard reformulation worth assessing first:
select subsets without labeled bin owners,cover each token once,and
require the number of selected subsets at each sum to equal that sum's
target multiplicity. Equal-target bins then introduce no duplicate option
copies. Its equivalence is just grouping selected disjoint subsets by
sum;it supplies no existence argument or performance result. This guard/
design note gets no probe,PROOFS entry or review request of its own.


### MI281 — B130 paper assessment: tight packing, and why incremental exact cover comes before another SAT model (2026-10-17 09:56 BST)

**Standard reformulation/guard, not a new theorem.** Let F_s contain the
nonempty token subsets of sum s,and let c_s be the multiplicity of s in
the target. Select pairwise-disjoint subsets,with at least c_s selections
from each REQUIRED F_s,and no other sum classes. Their union has weight
at least sum(c_s*s)=784 and at most the weight784 of the inventory.
Equality forces every multiplicity to be exact and every positive-weight
token to be covered. Conversely every partition supplies such a selection.
Thus token at-most-one plus sum-class LOWER bounds suffices;explicit bin
owners,token at-least-one and sum-class UPPER bounds are unnecessary.
Positivity and total equality carry the argument;without them the claim
fails. This is ordinary exact-cover/packing bookkeeping. No PROOFS entry,
probe or carrying review is opened for it.

**Cost assessment from existing data, not a new search/census.** Rechecked
B128's retained catalogue SHA256
1da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a.
At target (76,79,83,106,106,108,108,118),labeled-bin options total20175,
with121918 token incidences;unique sum-class options total13832 with83556
incidences. The naive sequential exact-one CNF was162232vars/426171clauses
(MI280). Removing repeated-bin owners and using tight packing can reduce
this to110042vars/269585clauses with sequential token-AMO and the following
explicit lower-counter encoding. For each repeated class of r options,
need at least2:prefix witnesses u_i for at least1 (i=1..r-1) and v_i for
at least2 (i=2..r);only backward implications
u_i -> (u_(i-1) OR z_i),
v_i -> (v_(i-1) OR z_i) AND (v_(i-1) OR u_(i-1)),
with absent prefix states false,and v_r true. Induction makes each true
witness imply the required number of selected options;actual counts give
a satisfying extension in the reverse direction. Cost2r-2 auxiliary
variables,3r-2 clauses. Here the repeated classes have r=3009 and3334;
other four classes need one long OR each. These are paper encoding counts,
not a constructed/benchmarked SAT instrument. Still about20 times the
adder variables and14 times its clauses. SIZE ALONE does not predict
runtime;it rules out treating this as an obviously cheap replacement.

**Source changes the next implementation choice.** Read Knuth,
[Dancing links](https://arxiv.org/html/cs/0011047v1),the exact-cover,
Algorithm X,dance steps and efficiency sections through the first update
profile. Known method,recorded in PRIOR-ART. The key distinction from our
B128 source is concrete:B128 reconstructs every fitting-row vector at
every node. DLX maintains the active incidence lists and column counts
with reversible cover/uncover operations. It changes the expensive update
mechanism rather than the allowed partitions. Using the existing ordinary
36-column bin+token matrix,the old hard target has142093 incidence nodes;
six32-bit indices each use3410232bytes before headers/row metadata/vector
capacity. That is an approximate core-storage calculation,NOT a measured
RSS or runtime. Equal bins can initially remain labeled for the standard
known algorithm;any symmetry change would need its own explicit audit.

Record searched: exact.cover|target multiplicity|subset.choice|Hall with
partition|burn|path|MI2[67] ->22 paragraphs,including MI263/264,MI277/278
and the new design note;Dancing links|Knuth|incremental.*cover|bitset.*cover
->six unrelated arithmetic/bitset passages,no existing DLX implementation
found in that scoped research search. No absence/novelty claim. Reading
B128's actual DFS confirms repeated full row filtering/counting,not DLX.

**Decision and fresh-choice check.** Do NOT build/run the large subset SAT
model now. The next concrete preparation is a standard incremental exact-
cover instrument,plus restoration and independent literal/oracle controls,
then a separately preregistered capped SAME2000 pilot if its design merits
it. No source/pilot/full-base job is launched in this paper block. No cap
increase or inference of feasibility from the small memory estimate.
The return of interest is specific:local reversible state replaces repeated
reconstruction;this is easier to explain than another large arithmetic
circuit. There is still frustration with instrument work;that is a reason
to require this concrete mechanism,not to keep tuning by momentum.
Gut: ACT on preparation,not an automatic experiment. Reasoned:known DLX
addresses the measured scan wall directly;its practical cost remains
unmeasured. Research13min active;Cloud's existing mentoring question is
not a permission gate. No new proof-review queue.

Niggle sweep: equal targets handled by multiplicities;lower bounds need
positive weights and the exact total;counter witnesses must have backward
justification (unsupported positive outputs would be unsound);all CNF
counts are paper counts;memory excludes metadata/allocator/memoization;
no speed claim from size;known algorithm credited;no old held case tree
reopened. The mathematical target L8 remains OPEN.


### MI282 — B131 claim/preregistration: standard incremental exact cover, SAME2000 (2026-10-17 10:07 BST)

**Named question.** Does Knuth's ordinary Algorithm X with reversible
incidence updates remove B128's repeated-reconstruction wall at useful
cost? This could make the unrestricted finite-base certificate feasible;
a prefix or benchmark alone cannot settle L8. Pull remains specific to
the local update mechanism,not another adder tweak or a new target class.
Known algorithm/source in PRIOR-ART/MI281;no new theorem claim. Record
searched: DLX|dancing links -> PRIOR-ART/MI281 and today's unrun source,
not an older target implementation. Read B128's actual DFS for comparison.

**Exact instrument.** path_forest_dlx_pilot.cpp builds ordinary sparse
bin+token columns from the complete arbitrary-cardinality subset catalogue.
Every row is one feasible subset plus its bin-owner column. Choose the
smallest active column;cover/uncover incidences in the standard reverse
order. Equal-target bins REMAIN LABELED;no quotient/symmetry pruning,
anchors,forced sizes,parity allocation,learned clauses,memoization or
old witness seeds. Root-only necessary guard: a k-token subset of firstm
odds has parity k and maximum sum k(2m-k);if minimum required bin sizes
sum above m,reject. This explains the published26-token lower control,
not a new classification. No per-node full fitting-list reconstruction.

**Restoration and independent controls.** Full saved node fields and all
column counts must equal their ORIGINAL values after EVERY completed
successful or unsuccessful search;the picked-row stack must be empty.
Unexpected check: on the97/99 fixed matrix,cover/uncover EACH individual
header and then ALL columns of one actual row nested;compare EVERY node
and count after each round trip. Then unrestricted97/99 must succeed.
Global3,3,3 must reject;67/102 published lower fixture rejects by the stated
root guard. All189 positive three-bin target questions for m<=6 compared
against exhaustive independent labeled-token assignments,including ties.
No controls have been executed before this source/preregistration push.
Syntax-only C++/Python checks are setup,not mathematical execution.

path_forest_dlx_check.py imports ONLY the unchanged B128 independent
checker helpers,no search/encoding. Pin B57 input SHA256
c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0,
all2000 original ranks/order and24688633 full-domain count. Independent
full14+14 MITM equality and GF counts at ALL123 subset sums. Check every
literal witness against the NEXT frozen target,every odd token exactly
once,each actual sum and eight nonempty bins;arbitrary bin sizes allowed.
Known positive/6-4 transfer/duplicate/inventory-preserving wrong sum/identity
checker controls stay active. Full completion additionally requires every
constructed matrix restored (the extra nested audit adds one restoration).
Self-controls are not an independent colleague's verification.

**Predictions and counterfactuals.** P1 all2000 literal partitions with
no cap. P2 primary ENTIRE2000 loop,INCLUDING matrix construction,snapshot
copy,full restoration check and output,<=10CPU sec. These are working
hypotheses,not guarantees. Report per-query node/update/CPU distributions,
all attempted states/updates INCLUDING an unfinished query,primary total
CPU/RSS,checker cost and child CPU including any watchdog work. If a call
never returns,mark missing per-call statistics rather than excluding it
silently. A stopped run is not a full2000 timing measurement. Any native
NO stops as unconfirmed;the sample already has older structural witnesses,
so inspect that existing record after stopping rather than promote a NO.

**One attempt/caps.** Original SAME2000 order,no new ranks/replenishment.
200000 states/query,10million total,1billion cover+uncover incidence updates;
work checks every1024 states/65536 updates/4096 inserted incidences and
query boundaries. Primary20CPU/40wall/256MiB,watchdog45wall. No claim of
a hard native RSS ceiling between checks. Checker unchanged30CPU/150wall/
256MiB. C++17/O2 compile<=60wall after push;then ONE driver invocation.
Stop first control/error,NO or cap;no repair,larger cap,reordering,second
heuristic or resumed run. Refuse output overwrites/restart. Full streams/
reports/catalogue local outside git;no blocked upload/manifest retry.
No fullE28 or other-base job follows automatically,even if this passes.

Niggle sweep: row omissions -> full catalogue/189 oracle/literal controls;
undo error -> full equality plus nested audit;equal bins -> kept labeled;
undocumented pruning -> root inequality spelled out;work hidden in setup ->
loop includes construction/snapshots/output;cap work -> total/pending counts
and child CPU;known algorithm -> credited,not PROOFS. Gut: ACT once on a
known mechanism that addresses the observed cost. Reasoned:if this fails,
retain it and reassess rather than start another automatic tuning ladder.
Cloud's perspective remains welcome,not a routine permission gate;
research13min active,full-base resource decision unchanged.


### MI283 — B131 outcome: cheap reversible updates, but the stripped search explodes on target3 (2026-10-17 10:09 BST)

**Stopped once,not repaired.** Prereg c986e758,C++17/O2 compile passes.
All123 full MITM/GF catalogue checks,189 labeled-assignment oracle questions,
known positive/global conflict/root lower-witness controls,and full individual/
nested restoration audit pass. The first TWO emitted literal partitions
pass independent original-target/order/rank/inventory/sum checks. At target3,
(75,87,88,93,109,110,110,112),rank14691876,the primary stops UNKNOWN_CAP
on200001 pending states. No rerun,larger cap,policy patch or later target.
No new counterexample or full2000 result. This pilot has failed P1.

**Attempted work,including the stop.** Completed queries10 and38 states,
sum48. Pending200001,pilot total200049,control443,total200492.
Pilot cover+uncover updates62949992,of which pending62440634;control
1666044,total64616036. Completed CPU12415/13585microseconds,total26000;
entire pilot loop0.182593CPU sec INCLUDING build,snapshot,restoration,
output and pending work,60.8643ms/attempt. Primary total0.22873CPU sec,
child resourceCPU0.232376,checkerCPU0.159562,wall0.755218sec.
PrimaryRSS21250048bytes,checkerRSS41594880.534397 inserted incidences,
max matrix147168 nodes.126 constructed matrices/126 restorations means
one unfinished matrix at the deliberate cap (the separate audit adds one
restoration);no restoration mismatch was reported on completed searches.
No1B-update,20CPU,RSS or watchdog limit was reached. P2 ENTIRE2000<=10CPU
is NOT ESTABLISHED by this tiny stopped prefix,not a full-run duration.

**The failure does not isolate data structure alone.** Standard DLX kept
labeled equal bins,omitted memoization and omitted B128's PER-NODE minimum-
cardinality pruning. These choices were explicit in preregistration,but
mean the comparison cannot show that reversible updates themselves fail.
It tests this stripped known algorithm under its stated state cap. The
incremental operations are fast in this run;the search tree is much larger.
This is a reasoned interpretation,not a controlled attribution to one
missing feature.

**Existing witnesses,read AFTER stopping.** B128's retained stream already
solves SAME target3 in63 states:
(1,3,5,11,55);(7,27,53);(37,51);(9,35,49);(17,45,47);
(15,19,33,43);(13,25,31,41);(21,23,29,39).
B129 also solved it in8259conflicts/0.331286CPU with a different partition.
The DLX cap is not mathematical nonexistence. No old witness was fed to it.

**One diagnostic hand paragraph,not another lemma/probe/review.** For THIS
target the per-bin minimum sizes are (3,3,2,3,3,4,4,4),sum26:parity and the
largest-two sum108 give the lower bounds,and individual subsets attain them.
Every actual bin size has the same parity as its target,so its excess over
the minimum is nonnegative/even. Since exactly28 tokens are used,the total
excess is2:exactly ONE bin has minimum+2,and every other bin has its minimum.
B128's saved witness spends the extra pair at75;B129 spends it at87.
Thus once either five-token odd bin is chosen,no other bin can waste another
pair. B128 enforces minimum-cardinality capacity during search;the stripped
DLX does not. A generic remaining-token/remaining-minima budget can rule out
such rows without restricting any feasible partition. This is ordinary
necessary-budget bookkeeping,not a new existence theorem or proof that
it alone explains the measured gap. It supplies a precise future diagnostic,
not permission to patch/retry this stopped attempt.

**Raw local receipts.** Catalogue945820bytes SHA256
1da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a.
Input55940bytes SHA256
c209e2ae59d6ee6c5dc9a31149aa02d0debf663b9bbbde44a49b79d15b6af0af.
Two-row stream298bytes SHA256
3674dfc1de4c60ff9f224e4852215bc1a88d1aee6fd195558dc46227ac605b37.
Primary report494bytes SHA256
e9c6290554fe0689621cd9515b11ff2301fbc003ea176697bed3906ca96c8846.
Combined report1940bytes SHA256
6bf4325aa2f7627f23dd1e782b152fbba9631f07dcfa58b6ee105264ff0d2487.
All raw local,outside git;no upload/manifest retry. Reports bear timings;
literal stream is separate. No outside-party verification claimed.

**Step-back and next intention.** This is a third failed generic-instrument
forecast,not a reason for another automatic heuristic ladder. FullE28 and
all-base certification remain OPEN. The useful new specificity is the
remaining-token budget,which directly touches the actual stalled target.
Next PREPARE a diagnostic that isolates this pruning while retaining the
same DLX order,labels,catalogue and caps;do not raise limits or quietly
rerun B131. Its prediction/counterfactual and complete controls must be
published separately before execution. Cloud is asked for perspective on
this precise mechanism rather than another routine proof read. If the
isolated diagnostic fails,the response should widen the mathematics or
incubate,not keep mixing search policies. Research13min stays active;
full-base resource discussion remains with the owner via Cloud.

Niggle sweep: two-row certificate only;all200001 pending states/updates
included;no full-run timing inferred;unfinished cap matrix not called a
restoration error;old witness credited and read after the run;comparison
confounding stated;necessary cardinality budget not a fixed-cardinality
model or existence proof. Gut:disappointment at the search explosion,but
interest in the now-precise missing resource constraint. Reasoned:the cheap
failure teaches what the next controlled comparison must hold constant.


### MI284 — B132 claim/preregistration: isolate the static token budget on SAME first3 (2026-10-17 10:20 BST)

**Question and pull.** Is the specific necessary token budget enough to
remove B131's third-target explosion,with every other search choice held
fixed? Interest is in this conservation constraint,not another general
solver-tuning round. This diagnostic can reject the explanation cheaply.
It does not attempt fullE28,the whole2000 sample or a new target domain.
Record searched: remaining.token|remaining.minim|minimum.cardinality with
DLX|MI283|B131 ->two MI283 paragraphs;actual B131 source and B128's per-node
cardinality code reread. Known Algorithm X credited in PRIOR-ART/MI281.
No new theorem or carrying read requested for a standard necessary bound.

**Sole intervention and its soundness.** Include B131's archived source
for its catalogue,matrix constructor,cover/uncover,budget and literal
checks;rename its main so neither its old main nor old solve/control entry
points executes. A new visit routine duplicates the exact B131 column
choice,row traversal,cover/uncover order and success handling. Add ONLY
this early rejection: tokens_left < sum of static root minima for bins
not filled yet. For target t,root minimum is the smallest positive k with
k=t mod2 and k(2m-k)>=t. Every subset of firstm odds summing t needs at
least that many tokens;later deletion cannot lower this necessary bound.
After choosing row S for bin i,subtract |S| tokens and that bin's root
minimum. Chosen DLX rows are disjoint,so an actual completion cannot cross
the rejection boundary. This is STATIC-root-minimum pruning,not B128's
stronger minima recomputed from currently fitting subsets. No memoization,
new symmetry reduction,reordering,changed rows/columns,anchors,forced
cardinalities or cap increase. Count rejected-state visits in node totals.

**Frozen counterfactual.** Read the retained B131 primary report,494bytes,
SHA256e9c6290554fe0689621cd9515b11ff2301fbc003ea176697bed3906ca96c8846.
It is the baseline:completed2,third cap200001states,same explicit target.
DO NOT rerun B131. New instrument runs ONLY original B57 first3 in their
original order,ranks/identity checked against the full pinned B57 SHA
c5b4ec84c7dc7232cd52b37d3a1c2afcbbeb52054a15870cadf95c0b6b8118f0.
No skipped easy cases/new sample or old witness seeds. A successful third
query would support this intervention for THIS fixture,not establish
full-domain performance or prove the bound explains every hard tail.
If it fails,the static-budget explanation fails this diagnostic;stronger
pruning remains logically distinct,not an automatic next patch.

**Controls and unexpected check.** Same189 independently labeled tiny
three-bin questions;known unrestricted97/99 positive;global3,3,3 negative;
published26-token lower guard. Same complete node/count restoration after
EVERY completed successful/unsuccessful search,and individual/nested header
round trips. Independent checker imports only unchanged B128 rank/literal/
MITM/GF helpers,no primary solver. ALL123 full subset maps/counts and every
literal token/bin sum checked. Its duplicate,wrong-sum,identity and arbitrary-
cardinality controls stay active. Unexpected boundary check:at the actual
third target,choosing a five-token75 leaves23 tokens and23 required,which
MUST be allowed;choosing a seven-token75 leaves21 against23,MUST reject.
Equality at the boundary must never be pruned. All these controls are
self-checks,not outside-party verification. Nothing has executed except
C++ syntax-only/Python AST checks before this registration is pushed.

**Predictions.** P1 all3 literal witnesses,no cap. P2 third uses<=5000
visited states,including budget-rejected states;baseline already visited
200001 without completing,so this would be more than40-fold less than
that stopped count. P3 ENTIRE first3 loop<=0.1CPU sec INCLUDING construction,
snapshots,restoration and output. Record each state/update/prune/CPU count
and total attempted/pending work. A cap or >5000 third states defeats the
strong pruning prediction. No completed-only means hiding a pending call;
no full2000 runtime or full-base projection from these three cases.

**One invocation and unchanged caps.** Native200k states/query,10M total,
1B link updates,20CPU/40wall/256MiB at the same check intervals as B131;
45wall watchdog. Checker30CPU/150wall/256MiB. C++17/O2 compile<=60wall
AFTER source/prereg push,then ONE driver invocation. Stop first control/
error,NO or cap;refuse overwrites,no repair/retry or later query. Even if
all3 pass,DO NOT automatically run2000 or the full base. No raw upload or
manifest retry;artifacts local. Source names path_forest_dlx_budget_diagnostic.cpp
and path_forest_dlx_budget_check.py. No policy edits to archived B131.

Niggle sweep:root bound only -> limitation explicit;off-by-one -> equality
control;false exclusion ->189 oracle comparisons/full literal validation;
confounding -> same inherited matrix/updates/order/caps,no other feature;
baseline rerun -> retained SHA only;old seeds -> none;measurement scope ->
only3;third failed generic forecast -> one targeted diagnostic,not another
uncontrolled ladder. Gut:ACT once on a precise falsifiable explanation.
Reasoned:this comparison can teach which constraint matters without a
larger resource commitment;research13min remains active.


### MI285 — B132 outcome: the isolated static budget clears the third target in64 states (2026-10-17 10:22 BST)

**All preregistered predictions pass.** Source/prereg0952c63e,C++17/O2.
Same three frozen targets in order,visited states10,37,64,total111.
Every literal partition/rank/target/inventory/sum check passes;all189 tiny
oracle questions,root negative/known positive/budget-equality boundary,
full123 MITM/GF maps and full restoration controls pass.126 matrices,
127 restorations (the extra nested audit),no pending target or cap.
The third witness is exactly B128's existing five-token75 construction,
found independently without that witness as a seed. No2000/full-base run.

B131 had already visited200001 states on SAME third query without finishing;
B132 completes in64,over3125 times fewer than that CENSORED baseline count.
The old full-search count is unknown,so this is not an exact full-run
speedup. The intervention alone suffices for THIS stopped fixture with
the stated unchanged order/rows/labels/caps. It does not identify every
hard tail or establish a full-domain theorem/performance guarantee.

**Complete measured work.** Per-query CPU microseconds13276,12947,27990;
loop total0.054615CPU sec INCLUDING build,snapshots,restoration and output,
so P3<=0.1sec passes. Primary total0.102324CPU,child resourceCPU0.105662,
checkerCPU0.120542,wall0.484889sec. PrimaryRSS20979712bytes,checkerRSS
39952384. Per-query link updates244680,264298,8638910,total9147888.
Capacity rejections1,24,55,total80 pilot (82 including2 control rejections).
534397 inserted incidences,max matrix147168 nodes. No hidden pending work.
These are self-controlled computations,not a colleague's carrying read.

**Raw local receipts.** Catalogue945820bytes SHA256
1da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a.
Three-target input84bytes SHA256
391b4a9512f907f3ccd6d58a5cb03c8de582b8aec469d24d8be06e09b54fb4f4.
Literal stream443bytes SHA256
0c7e8bc78742c07fffc3850f7480deede8dc2192f1bc356f9f4ce1a5313bd417.
Primary report523bytes SHA256
31cfbb1f0441827879d6f55e8428a3a636a060de929228285f90b7df8eb747d2.
Combined report1654bytes SHA256
04a8c34fc33a6537a3336970aff52f7fcd92fcc21c7d5135f0d33b1425018fab.
Reports include timings;literal stream is separate. All remain outside
git locally;no upload/manifest attempt or baseline rerun occurred.

**What changed / the remaining cost.** The static conservation constraint
was enough to replace the particular200k-state explosion with a short
search. Delight is specific:the proposed explanation survived a controlled
test,not merely another successful partition. The third query still makes
8.64M link updates,despite only64 states. Source inspection explains a
concrete avoidable cost:the child capacity test currently runs AFTER
covering every column of the candidate row,then immediately rejects55
of those states and undoes the changes. No update attribution per rejected
row was measured,so do not claim all8.64M are removable.

One implementation observation,not a new proof result:tokens_left and
minimum_required after a candidate depend only on its bin,cardinality
and the parent counters. Their failed inequality can be checked BEFORE
covering that row's other columns. A rejected child would perform no
further search,so early rejection can preserve candidate order,successful
witnesses and the mathematical tree. Accounting must still include every
rejected candidate as a visited/rejected state,not manufacture a smaller
node count. Matrix restoration and trace equivalence need explicit controls
before relying on the optimization. No code/policy change or second run
was made to B132 after its outcome.

**Next intention.** PREPARE that narrowly specified early-check optimization
and its equivalence/trace controls before another experiment;no automatic
full2000 or all-base expansion. This is not a new heuristic or another
constraint. Reassess whether the remaining matrix-build/restoration cost
makes a larger pilot worthwhile. Cloud gets this clean diagnostic result
as an update,no new carrying-review request. Research13min remains active.
The mathematical target L8 and fullE28 remain OPEN.

Niggle sweep:baseline censored,not an exact speed ratio;only3 targets;
unchanged candidate order/labels/rows,caps and native compiler options;
all self-controls pass,not outside-party verification;no speed projection
from three timings;no proof/novelty claim for ordinary cardinality pruning;
remaining updates not falsely attributed. Gut:delight at a small clean
answer and a renewed SPECIFIC pull toward conservation before expensive
updates. Reasoned:the next change has an explicit semantic-equivalence
obligation,not an excuse to widen the case tree or raise limits.


### MI286 — B133 preregistration: paired late/early budget checks with exact traces (2026-10-17 10:34 BST)

Question:can the SAME static bound reject an impossible child before its
matrix updates,with identical mathematical search? Pull is toward eliminating
work already known useless,not adding another pruning rule. Record searched:
early.reject|before.*cover|trace.equivalence with DLX|MI285|B132 ->MI284/285;
B132 source and retained passing artifacts read. Known DLX remains PRIOR-ART.

path_forest_dlx_hoist_pair.cpp inherits unchanged B131 matrix/cover/uncover.
Two new traced arms implement B132's late check and the early check. Both
record EVERY visited logical state (used tokens,unfilled bins,tokens left,
root minima left,rejected flag). Early-rejected children count as visits
and rejections exactly as in the late arm. For a rejected child,late's
cover/uncover sequence restores the parent and the child reads no further
matrix state;early can omit these inverse updates. Surviving branches retain
identical candidate and column order. No new bound,symmetry,memo,rows or caps.
This is a code-equivalence obligation,not a new mathematical proof result.

SAME first3 only,with a paired replay of PASSING B132 as the necessary new
trace-equivalence control. Failed B131 is not rerun. Pin retained B132
primary SHA31cfbb1f0441827879d6f55e8428a3a636a060de929228285f90b7df8eb747d2
and literal SHA0c7e8bc78742c07fffc3850f7480deede8dc2192f1bc356f9f4ce1a5313bd417;
both new arms must match its actual witnesses and10/37/64 counted states.
Frozen B57 SHA/ranks/first3 order unchanged. Execute late/early on cases1/3,
early/late on case2;fresh matrix each call. This controls order somewhat,
not a statistically calibrated timing study. No expanded sample/fulljob.

Controls:189 labeled tiny questions in BOTH arms,all exact traces/witnesses
compared;known positive/global conflict/lower negative,individual/nested
restoration audits and whole-matrix equality after every completed call.
Independent Python checker imports no solver,verifies every literal and
ALL123 MITM/GF catalogue maps. It checks every trace's token arithmetic,
remaining-target sum,root minima,one-bin parent/child transitions,disjoint
added tokens and terminal full cover;then EXACT ordered trace equality,
not just hashes. Unexpected:accept a complete independent valid trace;
reject its truncated version and a complete version with a corrupted
intermediate token count. Rejected states must never acquire descendants.
These are self-controls,not a colleague's review.

Predictions:P1 all six literal witnesses/exact traces/counts match B132 and
each other. P2 total early link updates<=one quarter late. P3 sum early
case CPU<late;lower confidence,one paired observation only. Case timing
includes construction,trace allocation,full restoration and matrix destruction;
excludes subsequent output. Report native loop/setup/child/checker cost too.
No timing or feasibility projection beyond these three inputs.

ONE driver invocation after source/prereg push and C++17/O2 compile<=60wall.
Same native200k states/call,10M total,1B updates,20CPU/40wall/256MiB checks;
45wall watchdog,checker30CPU/150wall/256MiB. Stopfirst control/error,NO,trace
mismatch or cap;no overwrite/restart,repair,second policy or sample expansion.
Include unfinished call states/updates and child CPU on a cap. Raw stream,
full trace,inputs/reports/catalogue local;no upload/manifest retry.

Niggles:fake node reduction -> manually count rejected children in both;
unsafe hoist -> full exact traces plus restoration;hash-only checking ->
parse all states;timing noise -> one paired result qualified;baseline retry
-> only prior PASS replay needed for equivalence;known method -> credited.
Gut:ACT once on semantic equivalence and operation counts. Reasoned:only
a verified equivalent improvement warrants considering a larger pilot.
Research13min active,no routine review halt or automatic full2000 run.


### MI287 — B133 outcome: exact traces preserved,92% fewer link updates on SAME three cases (2026-10-17 10:37 BST)

Prereg b0c90f56,C++17/O2. COMPLETE_EXACT_TRACE_EQUIVALENT_FIRST3.
All378 tiny oracle comparisons (189 per arm),paired positive/negatives,
full individual/nested and per-search restoration checks,independent full
123 MITM/GF maps and trace-checker positive/corruption controls pass.
All SIX literal witnesses match retained B132 exactly. All222 logical
trace states are checked arithmetically and compared in full ordered form.
Each arm has10,37,64 states and1,24,55 capacity rejections;no node-count
saving is manufactured.252 matrices/254 restorations,none unfinished.

Measured late updates244680,264298,8638910,total9147888;early244402,
255826,230060,total730288. Early uses7.9831% of late,92.0169% fewer.
Late per-case CPU14472,10780,28233microseconds,total53485;early11099,
13527,9901,total34527,35.4455% less in THIS single paired observation.
The second case is slower in the early arm;do not turn the total into a
universal per-case speedup. All three predictions pass. Native loop across
both arms0.088855CPU,primary total0.157087,childCPU0.160908,checkerCPU
0.124001,wall0.548423sec. NativeRSS21389312bytes,checkerRSS41148416.
Pilot222 states,9878176 updates;no pending work or cap.

Raw local receipts:catalogue945820bytes SHA256
1da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a;
input84bytes391b4a9512f907f3ccd6d58a5cb03c8de582b8aec469d24d8be06e09b54fb4f4;
six-row literal stream837bytes6734b3b5f19cd497feff271e49272c5aa9f3e7635b791270f6451687584c2246;
full trace4442bytes4e1263197c9db1abe1af36d67a5376531192105a13b5c19e38acd88b7fca4147;
primary report579bytes4a3753ef5b85e373a0f62f9716dfc5acfacce8fd29e15bdfce7effb8d818e620;
combined report1984bytesf84f17b297e98cca3f817d26b67510e5a2925a499dc6e9df217f24ce63505cd6.
Timing reports are machine dependent. Raw remains local,no upload or
manifest attempt. No failed B131 rerun or larger sample was executed.

What changed:the program-equivalence control survived actual complete
traces,while the avoidable update work fell sharply. Delight at a clean
constraint-first improvement. It is an implementation result,not a new
partition existence theorem or a colleague's carrying verification.
The gap between92% fewer updates and35% less measured case CPU suggests
other costs matter;their separate contribution was NOT measured,so do not
claim a profile proving matrix construction dominates. No projection to
all2000 or64787844 targets from these three timings.

Next PREPARE a cost-assessed pilot on the ORIGINAL SAME2000 with the fixed
early-check instrument and phase/resource reporting,not another new
heuristic. Give it a separate explicit preregistration and resource budget;
no automatic fullsample execution in this block and no all-base job.
That larger pilot must test tails and total cost before the owner's full-
base resource discussion has a measured basis. No fresh review queue is
needed for the hoist;Cloud receives the result as a concise method update.
Research13min remains active. FullE28/L8 remain OPEN.

Niggles:all rejected nodes retained;every state/witness checked,not hashes
alone;single paired timing qualified;one case slower admitted;fixed-cost
attribution left unmeasured;known algorithm/ordinary bound not a proof
claim;source after-run changes only outcome comments. Gut:delight and a
SPECIFIC pull toward the first real tail/cost test of this instrument.
Reasoned:the next useful evidence is a bounded full pilot,not more micro-
optimization on the same three cases.


### MI288 — B134 preregistration: fixed early-check instrument, ORIGINAL SAME2000 and phase costs (2026-10-17 10:48 BST)

Question:does the verified early-check kernel handle the original2000
targets at credible total cost,including its hard tails? Pull is toward
an honest feasibility answer now,not another micro-optimization. Record
searched:early.check|phase.*report|full.*pilot with MI287|B133|DLX ->MI286;
MI287/GC1460 and actual fixed-kernel source reread. Prior generic pilots
failed;the intervening conservation/hoist diagnostics passed only first3.

path_forest_dlx_early_pilot.cpp reuses B133's EXACT early visit routine,
ordinary labeled-bin matrix,static root minima and full restoration.
No new heuristic,memo,symmetry restriction,row ordering or witness seeds.
Constructor/search/snapshot/restoration/destruction timers observe the
same operations. All logical states are still stored per native call;
only the first3 full traces are emitted for integration comparison with
retained B133,then their storage is freed per call. Every target emits a
literal partition,not just SAT. Resource hooks in archived B131 retain
its DEFAULT20CPU/40wall;B133's default entry remains unchanged behind a
library guard. Only this new wrapper selects the scope budget below.

Original B57 full SHA/ranks/order fixed;all2000 input identities checked.
Pin B133 primary4a3753ef5b85e373a0f62f9716dfc5acfacce8fd29e15bdfce7effb8d818e620,
literal6734b3b5f19cd497feff271e49272c5aa9f3e7635b791270f6451687584c2246,
trace4e1263197c9db1abe1af36d67a5376531192105a13b5c19e38acd88b7fca4147.
First3 exact traces,witnesses and10/37/64 states MUST match. Before pilot,
repeat unchanged paired189 tiny questions in each arm,known positives/
negatives and full individual/nested restoration controls. Independent
checker imports no solver,checks every literal token/bin sum and NEXT
original target,and full123 MITM/GF catalogue maps. Positive/corrupt trace
controls retained. These are self-checks,not a colleague carrying read.

Predictions:P1 all2000 literal witnesses without caps (low confidence
about unseen tails). P2 IF complete2000,construction+snapshot+restoration+
destruction exceed half measured case CPU. P3 IF complete2000,whole primary
loop<=25CPU sec. Partial phase fractions describe only completed cases;
P2/P3 are not established by a stopped run. Report full completed node/
update/CPU distributions,phase totals and every unfinished call's states,
CPU,phase at interruption and aggregate updates. Pending phase timing
includes unwinding and is not a complete per-phase decomposition. Child
resource CPU includes any watchdog work;no censored work removed from means.

New scope goes first3 -> SAME2000,so planned TOTAL native allowance is
30CPU/50wall (previous diagnostic20CPU/40wall),60wall watchdog. Per-query
200k states and global10M states/1B updates/256MiB checks UNCHANGED.
This is explicit new-scope planning,not a resumed failed query or posthoc
cap increase. Checker30CPU/150wall/256MiB. C++17/O2 compile<=60wall after
source/prereg push,then ONE driver invocation,refuse overwrites/restart.
Stop FIRST error/control mismatch,NO or cap,no later target/repair/second
policy. No fullE28 or all-base job even on success;resource decision still
with owner via Cloud. Data local outside git,no upload/manifest retry.

If incomplete,retain the actual obstruction/cost and STOP automatic DLX
patching;widen mathematical perspective,consult Cloud or incubate before
another instrument proposal. If complete,assess measured cost and independent
verification needs before any larger job. This is the first real pilot of
the now-fixed kernel,not a claim that three-case timings generalize.
Niggles:default archived behavior preserved;only wrapper scope budget
changes;timers do not change candidate choices;first3 traces catch integration
drift;all cap work retained;unknown is not impossible. Gut:ACT once for
an uncensored feasibility answer within a bounded budget. Reasoned:the next
useful result is either a complete measured pilot or a concrete reason to
leave this standalone instrument. Research13min active.


### MI289 — B134 outcome: SAME target240 caps;standalone DLX tuning stops (2026-10-17 10:51 BST)

Prereg5008470f,C++17/O2. UNKNOWN_CAP after239 literal partitions,all original
identities/ranks/inventories/sums checked. All paired tiny/control/restoration
and full123 MITM/GF maps pass;first3 exact traces/witnesses match B133.
At240 (76,79,83,106,106,108,108,118),rank15376732,SAME B128 stopping target,
200001 pending states hit the unchanged query cap. No retry,repair,raised
state limit,later target or fullE28/base job. The planned30CPU allowance
was not used up. The target already has the credited B68/B129 witnesses;
this is not nonexistence.

Full attempted work:completed142642 states,pending200001,pilot342643;
control886. Pilot199801838 link updates,including91104514 pending.
Pending query211821CPU microseconds,interrupted in search;this includes
unwinding,not a completed phase decomposition. Native loop3.09282CPU sec,
12.88675ms per ATTEMPTED target including cap;attempted mean1427.679states.
Primary3.16073CPU,child3.181143,checker0.170227,wall3.612636sec.
NativeRSS48992256bytes,checkerRSS41545728.486 matrices/487 restorations
means one unfinished matrix plus the two extra audits,no completed-search
restoration error. No CPU,wall,RSS,total-state or1B-update cap reached.

Completed node distribution:min9,p50=24,p90=666,p95=1405,p99=5331,
max67012,mean596.82845. Completed case CPU microseconds:min8749,p50=11545,
p90=13830,p95=15217,p99=18676,max62259,mean12008.51883,total2870036.
Completed phase totals:construction2364044,snapshot80475,search287648,
restoration95366,destruction40581microseconds. Construction is82.37% of
COMPLETED case CPU;the four nonsearch phases89.91%. The pending hard query
is separately included above. This is a real profile of this prefix,not
full2000 timings or proof that every hard query has the same cost split.
P1 all2000/no cap FAILS. P2/P3 full2000 phase/time claims NOT ESTABLISHED;
raw booleans are completion-gated false,not measured full-run failures.

Raw local:catalogue945820bytes SHA256
1da444bee0e853374ef38b5bd48cd4eb244d85789e485a5b9653e6ae6446b87a;
input55940bytesc209e2ae59d6ee6c5dc9a31149aa02d0debf663b9bbbde44a49b79d15b6af0af;
239-row stream30205bytes4576c14dfc174446f949f5d6e2f04bc206325ab844c53efed37b2708d044edbb;
prefix trace2221bytes1b1f34ea99dbd736a9e9fe641444e61ae824c6f339964a13e9973342a79165fa;
primary report10540bytes2dbdbcb370a12227b81420cadd273defffa1edbb831cfe2e15b67a79faadc4df;
combined report13309bytesb15a6f2a390dcd98628e6bdeee0ee8043ae1c1e5322a39fb13ff67bfdc8d4c77.
No raw upload/manifest attempt. Reports include timings;literal stream is
separate. Self-controls do not constitute a colleague's carrying read.

**Direction change,not another patch.** Park standalone DLX development:
its matrix construction is costly even on easy cases,and its necessary
bound still misses a shared hard target. No automatic stronger heuristic,
portfolio or larger node allowance. The microdiagnostics remain valid but
did not supply full-pilot feasibility. The full-base resource proposal has
no successful generic pilot here to support it.

One HAND compatibility paragraph,not a new theorem/probe/review:the four
106/106/108/108 bins have individual minima2,but their only two-token
sets are {51,55} for106 and {53,55} for108. At most ONE of those four bins
can use2;the other three need>=4 by parity. Thus the naive minimum20 rises
to at least26 for this target before any choices. B68/B129 witnesses respect
this. This is the same kind of joint competition already identified in
MI262's fixed97/99 allocation;do NOT relabel it as a novel discovery or
claim it forces the complete partition. Record searched106.*108|pair.competition|
largest.*55|joint.*cardinality|hitting.*resource with MI|token|bin|target
->15 paragraphs;MI158/261/262 read;exact target search finds MI278/280/281.

Next bounded mathematical question:what source-backed joint-allocation
principle can make these competing minimum-size representations constructive,
without returning to fixed anchors or the parked component case tree?
Read relevant matching/odd-partition literature and the existing joint
allocation record before any new route. A resource-hitting inequality alone
is only a necessary guard;do not open a PROOFS entry or carrying-read queue
for it. Cloud is asked for perspective on that genuine compatibility gap,
not permission to run another patch. Research13min active;fullE28/L8 OPEN.

Fresh-choice check:frustration with instrument plumbing has grown;I would
not choose another DLX tweak now. The pull toward JOINT compatibility is
specific to the common target and its shared55 bottleneck,but its earlier
appearance in MI262 is a warning against claiming fresh progress by return.
Gut:disappointment at generic feasibility,interest in the mathematics behind
it. Reasoned:stop the standalone instrument lane;next orient on the missing
constructive inference or take incubation if it offers no genuinely new
handle. Niggles:all cap work counted;no impossibility claim;phase fractions
qualified;prior guard credited;no automatic resource expansion.

### MI290 — B135: direct hypergraph Hall criteria miss the exact-allocation regime (2026-10-17 11:01 BST)

**Bounded source/hypothesis audit, not a new lemma or experiment.** Question:
does a checked joint-matching theorem supply MI289's missing construction?
Record searched: rainbow|Hall|Rado|Aharoni|Haxell|prescribed.sum|joint.*allocation
with path|odd|MI2|bin|matching ->94 paragraphs/27 files; MI261-262 and the
existing prescribed-sum scope notes read. A narrower matching.width|pinning|
Haxell|Aharoni with128|E32|Hall finds only two unrelated probe paragraphs.
The older Hall/containment failure MI020-022 concerns Frankl, not this problem.
No new numerical run, resampling, solver patch or PROOFS entry.

**Sources actually read.** Asadpour-Feige-Saberi,
[Santa Claus Meets Hypergraph Matchings](https://www.wisdom.weizmann.ac.il/~feige/mypapers/santaclaus1.pdf),
section2/Theorem2 statement and definitions, printed pages4-5; its Haxell
criterion is for a bipartite hypergraph with at most r-1 token vertices per
edge and requires tau(H_C)>(2r-3)(|C|-1). Original Haxell proof unread.
Bottcher et al., [1802.04603v3](https://arxiv.org/pdf/1802.04603v3),
Theorem2.1 statement on printed page5: uniform s-edges require a matching
larger than s(|I|-1) in each colour union. Original Aharoni-Haxell proof
unread. Aharoni-Berger-Ziv,
[math/9912134v2](https://arxiv.org/pdf/math/9912134v2), page1 definitions and
Theorem1.1 statement: sufficient matching-width at least the colour count;
ordinary and independent pinning are distinguished. The tree results are
not imported. Haxell's own lecture slides, pages43-50, also read for the
pair-neighbourhood criterion and its strict +1; not a variable-size theorem.
Known sources are filed in PRIOR-ART, not as our proofs.

**Direct applicability check.** Let a colour be a target bin and its edges
be token subsets of that sum. At m28 a complete eight-edge selection must
use all28 positive tokens, since its total weight is784. Thus a restriction
to edges of size<=3 cannot even contain a solution. If maximum token rank
k>=4, set r=k+1 in the checked Haxell criterion: the full eight-colour set
would need tau>7(2k-1)>=49, but the entire token set is a transversal of
size28. The uniform matching-number criterion likewise fails for s>=2:
floor(28/s)<=14, whereas 7s+1>=15 is required. Neither is applicable here.
This is a scope guard, not a new obstruction to burnability or to every
possible hypergraph matching theorem.

**Unexpected hand check, exploratory rather than a blind prediction:** test
the stronger matching-width criterion against the already-positive balanced
E32 target(128,...,128), not the capped target. Let H consist of ALL subsets
of the32 odds1..63 with sum128. Every edge has at least4 tokens; every
matching has at most8 edges. Any8-edge matching M covers all32 tokens in
quartets. Consider the16 complementary pairs {x,64-x}. If one pair crosses
parts of M, adjoining any other complementary pair gives a128-sum edge E
meeting at least two parts. If none crosses, choose pairs inside two
different parts instead. In either case E together with the M-parts it
does NOT meet is a DISJOINT pinning family for M of size<=7. A matching of
size<=7 pins itself. Hence even the independent matching width is<=7, so
the sufficient full-eight-colour hypothesis fails. Positive control:
group those16 complementary pairs two per bin to give an explicit partition.
This short hand argument is an application guard only, not a proof/review
job. Failure of a sufficient hypothesis says nothing against the solution.

**What changed.** The proposed direct Hall shortcut has a concrete negative
answer for these checked criteria, including the stronger pinning version
on a known positive control. No L8/E28 claim moved. No claim that all
matching methods or literature are exhausted. The guard is not a reason to
resume the parked component case tree or instrument ladder.

**Next cheap question.** The older Chen-Fu-Wang-Zhou note read the sum-only
theorem and algorithm opening, not its full constructive recombination.
Read that step before inventing an odd analogue: does it control the
number of final leaves in each bin, or can that control be added without
reassuming the target partition? For index labels j, the required relation
is 2 sum(j)-cardinality=t, so ordinary sum preservation alone is insufficient.
The author-uploaded text was located again; its later algorithm/proof has
NOT yet been audited. This is a specific source question, not another
generic literature sweep or experiment authorization.

Fresh choice: disappointment that the general matching criteria need slack;
interest remains in the arithmetic recombination mechanism, not in another
solver adjustment. Gut: this narrower source read is worth one bounded
look; warmth is not evidence of a theorem. Reasoned: no constructive
candidate yet, but one precise unread carrying step remains. If it offers
no handle, take a genuine perspective/incubation step rather than generate
more necessary inequalities. Niggles checked: strict thresholds; rank
includes the bin vertex in Haxell notation; pinning family is disjoint;
the argument covers EVERY matching, not merely our chosen partition;
no proof of the source theorem or literature-absence claim implied.

### MI291 — B136: recombination counts leaves;incubate instead of following the next citation (2026-10-17 11:11 BST)

**Source/application audit and exploratory hand arithmetic;no experiment,
new theorem or carrying-review request.** Question from MI290: does the
prescribed-sum recombination provide the cardinality control our odd sums
need? Record searched: Chen|recombination|Algorithm.2.1|binary.*split|
leaf.*cardinal with odd|partition|MI ->17 paragraphs/5 files; MI037-038,
the earlier PRIOR-ART scope note and MI290 read.

Read the author-uploaded Chen-Fu-Wang-Zhou
[text](https://www.researchgate.net/publication/264923384_PARTITION_OF_A_SET_OF_INTEGERS_INTO_SUBSETS_WITH_PRESCRIBED_SUMS),
sections2-3 including Algorithm2.1,its example and final reconstruction.
Binary replacement expands large summands until physical labels remain.
The all-targets>=n case is delegated to Ma-Zhou-Zhou(1994),not constructed
by this extension. Extracted formulas have apparent inconsistencies
around shifted A+/A- notation;PDF retrieval failed. No implementation or
full proof-verification claim is made from that text.

**The missing invariant,by hand.** Write w(j)=2j-1. A replacement a=u+v
preserves index sum,but w(u)+w(v)=w(a)-1. After c final leaves,the actual
odd sum is2a-c. Thus each extra leaf changes the required answer;it cannot
be suppressed as an auxiliary detail. Equivalently,a binary decomposition
needs c-1 internal splits,not merely a terminating chain. Replacing an
even virtual value by two odd leaves can work,but forcing every virtual
value to have odd children cannot represent an odd parent. A ternary
odd-to-odd split instead requires a=u+v+w-1. None of this supplies joint
disjointness or a terminating odd-pool algorithm;it is one application
guard,no PROOFS entry.

**Unexpected positive countercontrol,found by hand rather than predicted:**
keep the paper's index targets a=(30,23,21,19,17,10) at n15,but require
c=(3,2,2,2,2,4). These counts sum15 and really are achievable:
{6,9,15};{10,13};{7,14};{8,11};{5,12};{1,2,3,4}.
Every label1..15 appears once and the six index sums are exactly a.
Their odd images give t=(57,44,40,36,32,16),total225:
{11,17,29};{19,25};{13,27};{15,21};{9,23};{1,3,5,7}.
The source example has different first/last leaf counts4/3,so its valid
index partition gives56/17 in those bins instead of57/16. This defeats
the proposed black-box inference EVEN WHEN the requested cardinalities
are realizable. It is neither a counterexample to the source theorem nor
an E28 fixture;no control was selected by a search or used to seed a solver.

For our actual levels24..32, l_i>=68 and any positive compatible c_i imply
a_i=(l_i+c_i)/2>=35>m. Thus ALL transformed inputs land in the source's
delegated case. Its new extension does not close the existing cardinality
gap. Reading the prior Ma construction would be another source question,
not a consequence or a newly justified odd-partition algorithm.

**Loop/fresh-choice decision.** Two source blocks have not supplied a
constructive handle after the parked solver sequence. Pull:the arithmetic
is still interesting. Push:the immediate plan has become another paper
in a reference chain. Without the investment,I would not now choose
another automatic source audit or necessary-bound patch. This is the
MI290 stopping condition tipping toward incubation,not a proof that the
main problem is hopeless or a routine wait for permission/review.

Halt new blocks and pause the13-minute research schedule under the owner's
explicit allowance,preserving its prompt. No computation is running.
Keep all results,including verified q8,unchanged;fullE28/L8 remain OPEN.
Ask Cloud for perspective at GC1463,delivered by portal flag after push.
Named incubation question:what genuinely new constructive mechanism can
couple sum and cardinality across bins,or should fresh choice move to a
different mathematical question? Reopen on a concrete candidate with a
cheap distinguishing test,or on an owner/Cloud conversation that renews
the direction;an ACK or another citation alone is not a mechanism.

Gut:interest in the object,but no honest warm next attack today.
Reasoned:the checked source gives no cardinality bridge;do not fabricate
a block to keep the scheduler busy. Niggles:both literal partitions and
totals checked by hand;positive prescribed counts avoid an impossible
control;the delegated regime is explicit;extraction ambiguity prevents
a code translation;no source theorem is refuted or novelty implied.

Operational receipt:the final fetch for this handoff was made less than
four minutes after the preceding one. That interval check failed;it was
not an authentication failure or a login retry. Reuse the fresh checkpoint
for this push;do not report network cadence as fully compliant.

### MI292 — B137: resume on SS3;strict descent fails but a unit-flow question survives (2026-10-17 14:16 BST)

**Hand reasoning/source orientation,not a new census.** The owner asks to
restart after Cloud's check-in. Verified fc07a67a/CL432 and2794d8a1/CL433;
read all four committed scripts before ACKing. Their recursion respects
remaining counts/sums and prunes by a necessary remaining interval;equal
remaining-bin states are interchangeable. This source read is NOT an
independent replay of the reported249776 larger cases. The research
heartbeat has been restored to13 minutes;the old schedule stays paused.

Question:can SS3's proposed exchange proof actually descend,or does it
need neutral rearrangements first? Unease:SS looks like a fractional
condition,while a strict two-bin swap is a stronger integral assertion.
Record searched: SS3|strict.*swap|neutral.*exchange|plateau|prescribed.sizes
with partition|sum|bin ->39 paragraphs/27 files; relevant CL432-433 and
the existing prescribed-size scope note read. No earlier SS3 proof found
in that bounded search. No seeded work draw,solver restart or fullE28 job.

**Primary literature changes the calibration.** Hoory-Kotlar,
[2605.06071v1](https://arxiv.org/html/2605.06071v1), introduction,
section3's definitions/Theorem1.12 statement and section5 discussion read;
also Claim4.13 statement,not its full proof. The May2026 discussion leaves
the equal-sum minimum-size>=3 case as an open direction. Its fractional
criterion and asymptotic rounding result do not settle our finite case.
Full proofs not audited;no later-literature completeness claim.

The equal-sum open direction is an actual SUBCASE of SS3,not merely an
analogy:for source labels1..m with common targetT and sizes c_j,subtract1
from each label to get index targets s_j=T-c_j. A subset J then asks
lo_1(C_J)<=|J|T<=hi_1(C_J). For fixed |J|,the smallest C_J gives the
strongest upper bound,so the source's sorted-prefix slack supplies every
upper inequality. Lower ones follow from complements and the fixed total.
Thus proving full SS3 would in particular resolve that dated open case.
The finite evidence is interesting;it is not a cheap theorem supplied by
the source. Credit/source scope in PRIOR-ART.

**Exploratory hand countercontrol to STRICT swap descent,not to SS3.**
On0..8 take three bins,all of size3:
A={6,7,8}, B={0,1,5}, C={2,3,4}; target index sums(20,6,10).
Current sums(21,6,9),deviations d=(1,0,-1),L1 error2.
SS holds:single sums20,6,10 lie in[3,21];pair sums26,30,16
lie in[15,33];total36. Unexpected check:EVERY proper-subset inequality
has positive slack,the minimum1. The target itself is feasible:
A={5,7,8}, B={0,2,4}, C={1,3,6}.

Yet NO single cross-bin swap strictly decreases L1 error. Only A is in
surplus and C in deficit. Such a direct decrease would need transfer1,
but min(A)-max(C)=2. A transfer2 merely reverses their signs;larger
ones increase error. A swap involving zero-error B can at best move the
unit error,not remove it. The same argument rules out strict decrease of
squared error2. This is a direct objection to the proposed proof step,
not a new standalone lemma,PROOFS entry or carrying-review job.

There is a concrete nonincreasing repair,using current ownership at each
step:swap B5/C4,then A6/C5,then C2/B1. Deviations become
(1,-1,0),then(0,-1,1),then(0,0,0). Errors2,2,0. Every swap exchanges
adjacent integer values and preserves all sizes;the final sets are the
target witness above. Two neutral moves unlock the improvement. The
example was found and checked by hand,no blind prediction or measured
experiment is implied. It does not say all neutral components can escape.

**A useful path exists;lifting it remains the inference.** For any current
partition of the full index interval,draw i->j when x+1 is in bin i and
x in bin j:that adjacent swap would transfer one unit from i to j.
Assume SS and a nonzero deviation vector. Some positive bin must reach
a negative bin. Otherwise let R be all bins reachable from positive bins.
It contains a positive deviation and no negative one,so sum_R d>0.
No edge leaves R,which means that whenever x+1 belongs to R,so does x.
Consequently R owns exactly the initial C_R labels,of sum lo(C_R).
But its prescribed sum would be lo(C_R)-sum_R d<lo(C_R),contradicting
SS. This supporting hand inference uses no presumed partition of the
TARGET sums and holds even with small bins;no status promotion or
independent verification is claimed.

The path is not automatically a sequence of legal unit transfers. In the
displayed partition,A->B uses6/5 and B->C uses5/4:they reuse B's SAME
token5. Simultaneously treating them as a flow silently allocates that
token twice. A path whose adjacent pairs are vertex-disjoint DOES lift:
perform its swaps together;intermediate sums cancel and endpoints improve.
Shared-token paths require a rearrangement such as the three-swap repair.
This identifies the exact integral obstruction rather than assuming
that SS's unit-flow reachability proves SS3.

**What changed/next cheap test.** Strict-pair descent is false on a tiny
SS3 instance;neutral exchanges demonstrably repair this one. The live
question is now whether a third element per bin permits a general
nonincreasing escape from shared-token paths,or whether a small feasible
instance has a trapped neutral component. Before testing that stronger
claim,preregister a bounded graph diagnostic with positive and known
pair-obstruction controls;do not extend Cloud's enumeration by habit.
No new experiment has run this block. The two/four-hole extension also
needs its own hypotheses;the interval argument above does not cover it.
SS3 and fullE28/L8 remain OPEN.

Fresh-choice check:the pull is specific to how neutral moves release a
shared token,not the age of the project. Surprise at a concrete plateau
despite strict SS slack;interest in the missing integral lift. Reasoned:
continue this mechanism,with the source's open-case warning front and
centre. Niggles:unit direction and deviation signs checked;all subset
bounds accounted for;the three swaps use CURRENT ownership;reachability
is not implementability;Cloud's counts remain reported,not replicated.

### MI293 — B138 preregistration: can the fixed n9 plateau always escape? (2026-10-17 14:17 BST)

Continue MI292's SAME live mechanism,not a new theorem or a larger SS3
census. Before running:one finite graph diagnostic for the fixed target
(20,6,10),sizes(3,3,3),on0..8. Every owner word with those counts is a
vertex;an edge swaps ADJACENT INTEGER VALUES in different bins. Orient
each move only when L1 target-sum error does not increase. Reverse BFS
from all target witnesses tests whether every vertex can reach a witness.

P1 controls:exact1680 labeled partitions and independently matching
energy/goal/reachability maps. The positive n6 sizes(3,3),sums(7,8)
has20 partitions;the source's SS-feasible but impossible n8 pair instance
sizes(2,2,2,2),sums(2,6,8,12) has2520 partitions and NO target witness.
P2 blind:ALL1680 n9 states reach a target without increasing error.
CF must fail:MI292's initial state has a strictly improving single
cross-bin swap. Check all27 swaps,not merely adjacent ones. Its explicit
three-swap repair must have errors2,2,0. Unexpected check:reflect every
index x->8-x and targets to(4,18,14);the whole reachable sets must map
exactly,not just their counts.

Primary enumerates partitions by disjoint combinations. Reference
enumerates all owner words,computes sums directly,and uses synchronous
full-set closure rather than BFS;compare COMPLETE maps. Source:
tests/probes/instinct/ss3_neutral_diagnostic.py. Record search and primary
literature are MI292;no new targets selected by output. Scope is these
two n9 questions plus n6/n8 controls only;no fullE28 experiment.

Caps5CPU seconds/10wall seconds/96MiB,one process,external12wall
watchdog. Publish source and this registration before ONE invocation.
Stop on failure/cap,no repair/retry/expanded domain. Retain a first
unreachable literal partition if P2 fails. If it passes,this diagnoses
one target,not SS3 or general nonincreasing reachability. Next return
to the shared-token lifting inference;no automatic graph-size ladder.

### MI294 — B138 outcome: the fixed plateau always escapes;programme scope correction (2026-10-17 14:18 BST)

**COMPUTED/MEASURED,one registered invocation.** Prereg322bf4cc/MI293,
Intel CPU. All controls pass;complete independent maps agree in all four
arms. BOTH n9 targets have1680 labeled partitions,two target witnesses,
and every partition has a nonincreasing adjacent-swap path to a witness.
Maximum shortest path23 in each arm. P2 passes for this ONE target and
its reflection. No larger target domain or general convergence claim.

Positive n6 control:20 states,three goals,all reachable,max path5.
Known impossible n8 pair control:2520 states,zero goals/reachable states;
SS still passes,as required. The initial strict-swap counterfactual is
rejected after checking all27 cross-bin swaps;literal repair errors2,2,0.
The reflected reachable sets map exactly. All5900 primary/reference
states compared,not an independence claim based only on matching counts.

CPU0.254747s,wall0.264857671s,watchdog wall0.38150155s,
peakRSS18690048bytes,inside5CPU/10wall/96MiB. No retry,repair or extension.
Raw report2038bytes SHA256
363a15eac88f70469ef9aa07cb67b8bee93550628c927f28f736dc3f79530979;
stdout1276bytes085485db1bee4e915fae53a3bc58344ba3ab0982c7d142336fef710a5711585b;
stderr empty. Raw local,not uploaded. Two implementations are self-checks,
not another party's replication. No source change affecting computation
after the run;only this outcome and header receipt appended.

**One hand scope correction to CL432's programme,not a new lemma/probe:**
q>=4 is the all-size>=3 admission threshold at m28 ONLY. With q odd
targets and b size2 bins,the other odd bins need>=3 and even bins>=4,
so m>=32-q-2b. Hence b>=max(0,ceil((32-q-m)/2));parity makes the
numerator even on an actual E_m target. For example the E24 tuple
(68,68,68,68,69,69,69,97) sums576,has q4,and lies within68..114,
but all sizes>=3 would require28 tokens from24. At least two pair bins
are forced. Thus programme step2 needs a level-dependent threshold,
and step3 cannot be restricted to one/two pairs across every base level.
This refutes that stated universal admission step,not SS3 or L8.

What changed:strict descent is insufficient,but neutral escape succeeds
throughout this fixed finite graph;the integral lift has a concrete
positive control. Next stay with a hand augmentation argument:can spare
elements give a nonincreasing escape from shared-token paths,or can a
feasible target trap an entire neutral component? No automatic larger
enumeration,fullE28 size-vector census or solver restart. The punctured
pool and level-dependent pair counts remain separate obligations.

Gut:delight at the exact neutral-path agreement,interest in that mechanism.
Reasoned:one target supports further reasoning,not a new universal claim.
Niggles:negative pair instance is outside SS3;reflection is not a second
new target class;all cases/cap work included;maximum path is shortest
among nonincreasing adjacent swaps;the m24 correction does not assert
that the actual target is deficient. Research13min ACTIVE;no review wait.

### MI295 — B139: three-bin shared-token augmentation (2026-10-17 14:38 BST)

**Current status,2026-10-17 17:36 BST:PROVED in the stated scope.**
Cloud CL434/5ef12b10 completed the independent carrying read and
independent finite checks. Original sketch wording below is historical.
Novelty remains unassessed;no full SS3/E28/L8 conclusion. See MI317.

**PROOF-SKETCH,not independently verified;novelty unknown.** The pull
is toward releasing a token used twice by a unit-flow path. Three bins
limits a shortest path to one intermediate bin. This block asks whether
that obstruction can be eliminated without increasing the sum error.
It would explain a part of SS3 by a hand mechanism,not extend a census.

Record searched before the argument: `neutral.*(swap|component)|adjacent.*(exchange|transfer)|SS3|augmenting.*(path|chain)`
AND `partition|bin|sum`:32 paragraphs/15 files; then
`three.bin|three.part|k.?=.?3|SS3` AND `prescrib|exchange|size.sum|neutral`:
18 paragraphs/7 files. MI273's relay and MI292-294 are the predecessors;
no earlier three-bin arbitrary-prescribed-sums proof found. Bounded
primary-literature search found no exact match. Hoory-Kotlar2605.06071v1
introduction credits the EQUAL-sum k3 result to earlier work:that
conclusion is known. Arbitrary prescribed sums and the <=4-swap mechanism
below have not been matched to an earlier theorem in this bounded search.

**Candidate statement.** Let c_A,c_B,c_C>=2 sum to n. Let integer targets
s_A,s_B,s_C total n(n-1)/2. For each bin subset J write C_J for its total
size and S_J for its target-sum total,and require

    C_J(C_J-1)/2 <= S_J <= C_J(n-1)-C_J(C_J-1)/2.           (SS)

Then a labeled partition of 0..n-1 with these sizes/sums exists.
Stronger:from ANY partition with the prescribed sizes and nonzero error
E=sum_i|d_i|,d_i=current sum_i-s_i,at most FOUR adjacent-VALUE swaps
decrease E by at least2,never increasing it at an intermediate step.
Repeating gives a target partition after at most2E swaps,where E is the
initial error. No target partition is assumed in selecting the swaps.

**1. SS forces a unit-transfer path.** Orient bin edge i->j when i owns
x+1 and j owns x. If no positive-deviation bin reaches any negative one,
let R be the bins reachable from ALL positive bins. It has d_R>0 and no
outgoing edge. Whenever x+1 belongs to R,x belongs to R;its tokens are
exactly the initial C_R values. Its prescribed sum would be their
minimum sum minus d_R,contradicting SS. This is MI292's reachability
argument;the missing step is implementing a path with current ownership.

Choose a shortest path from ANY positive bin to ANY negative bin.
Every intermediate bin has deviation zero:otherwise its suffix or
prefix shortens the path. With three bins the path is direct,or A->B->C
with d_A=D>0,d_B=0,d_C=-D. A direct edge decreases E by2. In the latter
case read the owner word from value0 to n-1. The edges are BA and CB
patterns. If some such pair of patterns uses disjoint positions,their
two swaps are legal:first neutral,second decreases E by2. There is no
CA pattern,which would give a direct A->C edge.

**2. Only one shared-token triple remains.** Otherwise EVERY BA pair
intersects EVERY CB pair. Their intersection can only be the B token.
Fixing either pair forces every pair of the other type to use that B;
its neighbors then force both pair sets to be singletons. At positions
p-1,p,p+1 the word is CBA,the unique CB and BA patterns. If D>=2,swap
edges p then p-1 (edge x means values x,x+1). Deviations in A,B,C order:

    (D,0,-D) -> (D-1,1,-D) -> (D-2,1,-D+1).

The first swap is neutral;the second decreases E by2. Only D1 remains.

**3. Unit-error reverse relays.** A BC pattern at edge q disjoint from
the triple gives swaps p-1,p,q and deviations

    (1,0,-1) -> (1,-1,0) -> (0,-1,1) -> (0,0,0).

A disjoint AB at q instead gives swaps p,p-1,q:

    (1,0,-1) -> (0,1,-1) -> (-1,1,0) -> (0,0,0).

After the first two swaps CBA becomes BAC or ACB,respectively;the third
edge is unchanged because it is disjoint. These are actual token swaps.

**4. Exhaust the case with neither disjoint reverse edge.** Apart from
the unique CB and BA,and the forbidden CA,every unequal adjacency goes
forward in A<B<C. The ENTIRE word therefore has form

    A^a B^b C^c B A^d B^e C^f, c,d>=1; a,b,e,f>=0,

with the middle B at p=a+b+c. A disjoint AB or BC exists if a,b>0;
b>0,c>=2;d>=2,e>0;or e,f>0. Without one,b>0 forces a0,c1,and e>0 forces
d1,f0. B's size b+e+1>=2 forces at least one of b,e positive. Both
positive would make A and C singletons,contrary to their size bounds.
Exactly one is positive.

For b0,e>0 the word is A^a C^c B A B^e with a>=1,c>=2,e>=1,p=a+c.
Swap p,p-1,p,a-1. The first three swaps turn CBA into ABC;the last
uses the original AC boundary,disjoint because c>=2:

    (1,0,-1) -> (0,1,-1) -> (-1,1,0) -> (-1,0,1) -> (0,0,0).

For b>0,e0 the word is B^b C B A^d C^f with b,f>=1,d>=2,p=b+1.
Reflect all values and interchange A,C:it becomes the previous case
and retains deviations(1,0,-1). Explicit original edges:p-1,p,p-1,p+d.
Their deviations are

    (1,0,-1) -> (1,-1,0) -> (0,-1,1) -> (-1,0,1) -> (0,0,0).

Every branch decreases E in <=4 legal swaps. E is a nonnegative even
integer,so iteration terminates. SS necessity is the minimum/maximum
sum bound for distinct values. This completes the candidate argument,
conditional on its correctness,not on a computation or existence oracle.

**Scope/niggles.** Exactly three bins and full consecutive pool;no k>=4
or punctured-pool conclusion. Longer paths can have multiple zero bins,
which this argument has not lifted. Size>=2 matters:sizes(3,3,1),targets
(14,4,3) on0..6 satisfy SS but cannot be realized:the singleton takes3,
leaving no three distinct remaining values of sum4. No prize/fullE28
claim. No PROOFS entry pending literature calibration;the contribution
under review would be the exchange mechanism,not the known equal-sum
conclusion. Source:https://arxiv.org/html/2605.06071v1,introduction.

Niggle sweep:graph orientation and current ownership checked in every
displayed relay;global word classification accounts for all six unequal
transitions;reflection negates deviations and the label swap restores
them;size bounds are spent precisely in the residual case;SS reachability
does not assume the desired partition. Next audit these exact formulas
independently,without a search fallback. Gut:surprise and warm pull at a
finite repair of the first genuine conflict. Reasoned:complete-looking
three-bin candidate,not an argument that the longer path is solved.

### MI296 — B139 preregistration: literal <=4-swap formula audit (2026-10-17 14:38 BST)

Before any invocation:source tests/probes/instinct/ss3_three_bin_exchange.py.
For n6..9 enumerate every sorted size vector c_A<=c_B<=c_C,sizes>=2,and
every labeled owner word with those counts. For each word use every
permutation of deviations(D,0,-D),D1,2,3;derive target sums and retain
only SS-feasible ones. P1:the FIXED constructor selects a MI295 branch,
uses <=4 adjacent swaps,never increases L1,and decreases it by>=2.
D1 ends exactly. P2:all seven branches actually occur. No BFS/solver/
fallback,no output-chosen larger domain. Multiple-positive deviation
states are covered by the hand direct-edge argument,not this domain.

Independent control:literal checker recomputes sizes/sums after EACH
swap,using no constructor arithmetic. Separate product enumeration gives
COMPLETE feasible-target sets for all n6..8 size vectors;every retained
D1 target must occur. CF:MI295's singleton example is SS-feasible but
impossible by complete independent n7 enumeration,and MUST be rejected
by the constructor. Unexpected:reflect EACH entire path and its sums;
also translate the pool by-11 with target-sum shifts-11c_i. Intermediate
errors must match exactly. This tests symmetry/offset arithmetic,not
just success counts. Record searched/source calibration:MI295.

One process,15CPU/25wall seconds/128MiB,30wall external watchdog. Stop
first failed control/cap;no fix/retry/expanded domain. Publish candidate,
source and this registration before ONE invocation. Raw outside git.
Passing supports formulas on this domain,not another party's verification
or a universal proof/novelty claim. Then send Cloud the carrying hand
step for genuine review;continue reasoning without a routine review halt.

### MI297 — B139 outcome: all explicit formula branches survive (2026-10-17 14:40 BST)

**COMPUTED/MEASURED;candidate theorem remains PROOF-SKETCH.** Registration
9f1c5ae6/MI296,ONE invocation on Intel CPU. All4976 primary owner words
enumerated,89568 error/target screens,82284 SS-admitted calls. Every
fixed path obeys the literal cardinality/current-ownership/sum checks,
never increases L1,decreases it by>=2,and uses at most4 adjacent swaps.
All D1 paths finish exactly. P1/P2 pass;no source repair or search fallback.

Branch counts:direct62380,disjoint17738,overlap with D>=2 1416,
reverse C->B relay526,reverse B->A relay140,four-left42,four-right42.
Both residual shapes already occur at n6 with sizes(2,2,2). First
four-left literal fixture:word(0,1,1,2,0,2),targets(3,4,8),edges(3,2,3,0);
first four-right:word(0,1,0,2,2,1),targets(2,7,6),edges(1,2,1,4).
Both have errors2,2,2,2,0. These are witnesses to mechanism coverage,
not additional universal conclusions.

Independent product enumeration checks1280 reference owner words for
all n6..8 size vectors,with complete feasible-target sets. All admitted
D1 targets occur. The n7 singleton negative is SS-feasible,impossible
under full reference enumeration,and rejected by the constructor.
Each of82284 entire paths passes index reflection and translation-11,
with every intermediate error identical. Same-worker independent code
is a self-check,not another party's verification.

CPU4.277403s,wall4.282419795s,external watchdog wall4.425663514s,
peakRSS16625664bytes,inside15CPU/25wall/128MiB/30watchdog limits.
No cap,retry,fix,larger domain or running background job. Only an outcome
header added to the source after the run;no computation-affecting change.
Raw report2650bytes SHA256
1580be2dc90bede1fffc9c774874212e7e8171ee8047859610e3e8b7a19ec069;
stdout1250bytes055373944e936381eaeeb0a31955524f50881c7042fafa13822a704af3109dc6;
stderr empty. Raw local,not uploaded.

What changed:the hand <=4-swap construction now has an exhaustive
small-domain audit of every branch. Ask Cloud for an independent carrying
read of MI295,especially the global owner-word classification and the
size>=2 use. Equal-sum k3 stays credited prior art;arbitrary-sums/algorithm
novelty remains unknown. No PROVED label or fullSS3/E28/L8 conclusion.

The next inference is a longer surplus-to-deficit path with several
zero bins. Simply merging the zero bins does not implement this:
an aggregate-zero repair can leave one constituent at+1 and another
at-1. A useful extension must control those individual sums during
the lift. Continue that hand question independently of the carrying
read,no automatic larger graph census or solver restart.

Fresh-choice:the pull is warm because the shared-token conflict acquired
a concrete finite repair this block,not because the project has been warm
before. Delight at a complete-looking mechanism;unease is now specific
to simultaneous zero bins. Reasoned verdict:the three-bin candidate is
worth scrutiny,the longer-path obstruction is still real. Niggles:
all seven branches actually exercised;sorted sizes lose no label class
by permutation symmetry;D1..3 is only the test domain,not an infinite
proof;positive/negative multi-bin signs rely on the direct-edge argument;
no feasible target assumed in the reachable-set step. Research continues.

### MI298 — B140: two shared intermediates;an exact four-bin family (2026-10-17 14:51 BST)

**Hand PROOF-SKETCH,not independently verified;no machine experiment.**
The question is no longer whether a three-bin repair exists. It is how
to move BOTH endpoint errors without leaving compensating errors in
different zero bins. The pull is toward the smallest chain where that
distinction matters. Record searched:`SS3|zero.bin|zero.deviation|shared.token`
AND `path|coalesc|merg|four.bin`:21 hits/9 files;then
`2,6,8,12|2,8,6,12|five.swap|three.bin|shared.token` AND
`SS|sums|bin|relay`:30 hits/5 files. MI292/295-297 and Cloud's known
four-pair counterexample are the relevant precedents. No claim that
the counterexample or the elementary pattern counting below is novel.

**The family and its precise answer.** Let a,b,c,d>=1 and partition the
full interval0..n-1,n=a+b+c+d+4,by the owner word

    A^a C^c B A D C B^b D^d.                         (F)

Thus sizes are(a+1,b+1,c+1,d+1). Define targets to be the current sums
minus(1,0,0,-1),in A,B,C,D order. All these targets satisfy SS. Within
this family a target partition exists IFF max(b,c)>=2. In particular,
all four sizes>=3 implies existence,but making ONLY either endpoint
bin larger does not remove the obstruction when b=c=1.

**SS holds even on the negative boundary.** Only subsets containing A
but not D lose one target-sum unit,or complements of such subsets gain
one. Every former subset's current tokens fail to be an initial segment:
if it omits C,it owns A at p+1 but misses C at a,where p=a+c;if it
includes C but omits B,it misses B at p;if it includes B and C,it owns
B at p+4 but misses D at p+2. Hence its current sum exceeds its minimum
by at least1. Subtracting1 preserves the lower SS bound;its upper bound
is automatic. Complementarity proves the other changed bounds. All
unchanged subset targets already come from an actual partition. This
verifies ALL SS bounds without assuming the desired target partition.

**Why the obvious chain cannot be performed as disjoint swaps.** The
unit-transfer path is A->B->C->D. Its adjacent-value edges occur at

    A->B: p;  B->C: p-1 or p+3;  C->D: p+2.

No shortcut exists in this owner word. Choosing B->C at p-1 reuses B's
token in A->B;choosing it at p+3 reuses C's token in C->D. Thus no
choice of three disjoint pairs implements this path,even when ALL
four bin sizes are>=3. Extra elements do not make that shortcut valid.

**Five legal swaps when c>=2.** First move the deficit from D into C
using edge p+2. The CBA triple at p-1,p,p+1 now has deviations(1,0,-1)
in A,B,C order. There is an AC adjacency at edge a-1 DISJOINT from this
triple because c>=2. The triple can be reversed,then that adjacency
returns the excess unit. Explicit edges and actual deviations:

    edges: p+2, p-1, p, p-1, a-1

    (1,0,0,-1) -> (1,0,-1,0) -> (1,-1,0,0)
               -> (0,-1,1,0) -> (-1,0,1,0) -> (0,0,0,0).

The L1 error is2 throughout until the final0;each intermediate bin's
sum is restored individually. This uses only the displayed local edges,
not MI295's whole-word classification or its unverified theorem.

**The other intermediate bin,by an explicit symmetry.** Reflection of
the values,with names A<->D,B<->C,maps parameters(a,b,c,d) to(d,c,b,a)
and retains the initial deviation vector(1,0,0,-1). If b>=2,reflect the
previous repair back. Original edges are

    p, p+3, p+2, p+3, p+b+3.

Their deviations are(1,0,0,-1),(0,1,0,-1),(0,0,1,-1),
(0,-1,1,0),(0,-1,0,1),then0. No inference about the original bins'
individual sums has been lost by coalescing them.

**Why b=c=1 is impossible,for arbitrary endpoint sizes.** A's target
is exactly1 above the minimum sum of a+1 values. This forces A to be
{0,...,a-1,a+1}. D's target is exactly1 below the maximum for d+1
values,forcing D to be{a+4} union{a+6,...,a+d+5}. (An ordered distinct
subset one above minimum can raise only its last entry by1;reflect for
maximum.) The four remaining values are{a,a+2,a+3,a+5}. C needs two
of them of sum2a+4,which would require a pair summing4 in{0,2,3,5};
none exists. This proves the negative direction,not just failure of
the proposed swaps. At a=d=1 this is the known n8 pair obstruction,
with target order(2,8,6,12). Its earlier provenance is retained.

**Literal hand controls/unexpected check.** For a=b=c=d=2,n12,the
targets are(5,21,12,28). Edges(6,3,4,3,1) finish at
A{0,2,3},B{4,8,9},C{1,5,6},D{7,10,11},with the required sums and
every value used once. The reflected formula has edges(4,7,6,7,9),
and the displayed reflected deviations independently check its signs.
At a=b=c=d=1,the forced negative proof leaves{1,3,4,6} and C sum6,
which is impossible. Unexpected check:translate all values by any
integer h;targets shift by h times the corresponding size and every
deviation/swap calculation is unchanged. These are hand checks;no
new enumeration,timing claim or independent-party verification.

**The remaining four-bin obstruction has a small classification.**
For an arbitrary shortest path A->B->C->D,let U,V,W be the positions
of BA,CB,DC patterns. U and W pairs are always disjoint. For each
v in V,disjoint choices from U and W would therefore give three
disjoint pairs. If this never happens,v intersects EVERY U pair or
EVERY W pair. It can intersect at most one of each (only u=v+1 and
w=v-1). Consequently at least one outer family is a singleton,and
V has at most TWO elements. If V has two,both outer families are
singletons. This is an elementary pattern reduction,not SS sufficiency:
it leaves a shared DCBA block,a single shared triple,or two shared
triples. Family(F) resolves one infinite two-triple placement with a
sharp spare-element threshold. Other placements/padding remain OPEN.

What changed:a specific four-bin class is constructively settled on
paper,and the old pair obstruction persists exactly when BOTH middle
bins lack a spare. This explains a mechanism behind the minimum3
hypothesis,without proving SS3. Next inspect the OTHER overlap shapes
from the pattern reduction,especially the contiguous DCBA case;no
automatic larger graph diagnostic or solver restart. Cloud's existing
MI295 carrying read remains the priority;this adds no separate review
job or review halt. General SS3/fullE28/L8 remain OPEN.

Gut:surprise and delight at a sharp distinction between extra endpoint
elements and extra intermediate elements. Fresh choice remains warm
because it now predicts exactly which spare helps this family. Reasoned:
the five-swap calculation and forced-set obstruction are explicit;
the general placement problem remains. Niggle sweep:all four labels'
deviations displayed;edge disjointness uses c>=2 precisely;reflection
maps the entire parameter family;negative boundary is independently
an impossibility argument;no generalization from this family to all
owner words or a prize claim. Research13min ACTIVE,no review wait.

### MI299 — B141: contiguous overlap;an eight-swap local release (2026-10-17 15:06 BST)

**Hand PROOF-SKETCH,no new experiment or independent review.** Question:
how can the contiguous DCBA overlap release an error while respecting
both intermediate sums? The pull changed representation:two bins sharing
a consecutive interval form a lattice of subsets ranked by sum. Adjacent
rank levels allow neutral reshaping when the two bins carry one unit of
combined error. This led to an explicit local module,not a larger census.

Record searched:`DCBA|contiguous|shared.token|four.bin` AND
`overlap|SS3|zero.bin|neutral|repair`:19 hits/5 files,MI295/298 relevant.
For the representation:`order.ideal|Young|distributive|adjacent.rank`
AND `partition|exchange|sum|connect`:3 unrelated hits/1 file. Read
Stanley's1980 paper section4,printed173-174,for the known rectangle/
order-ideal representation;the elementary adjacent-level connectivity
derivation is attached in PRIOR-ART,not a new PROOFS entry or review job.
The paper is NOT cited as containing our connectivity consequence or
our application,and none of its deeper theorems is needed here.

**A local eight-swap module.** Suppose global deviations are
(d_A,d_B,d_C,d_D)=(1,0,0,-1),all other bins zero. In the owner word,
suppose a consecutive interval has substring

    B C^c D^d C B A,      c>=2,d>=3.                    (M)

Values outside it can have arbitrary ownership and remain untouched.
Index this interval locally from0 and put L=c+d+1. Its single final
C,B,A occur at L,L+1,L+2;its C/D run boundary is at edge c.
Use these EIGHT adjacent-VALUE edges,in order,adding the interval's
actual starting value to every index:

    L+1, L-1, c, L, L+1, L, c+1, 0.

Actual deviations in A,B,C,D order are

    (1,0,0,-1)
      -> (0,1,0,-1)     A->B,edge L+1
      -> (0,1,-1,0)     C->D,edge L-1
      -> (0,1,0,-1)     D->C,edge c
      -> (-1,1,0,0)     A->D,edge L
      -> (-1,0,0,1)     B->D,edge L+1
      -> (0,-1,0,1)     B->A,edge L
      -> (0,-1,1,0)     D->C,edge c+1
      -> (0,0,0,0)      C->B,edge0.

Every intermediate L1 error is2;the last is0. Individual B and C sums,
not just their aggregate,are restored. No target partition assumed.

**Current ownership and the actual use of the hypotheses.** After the
first three swaps,C within this interval owns{1,...,c-1,c+1,L-1};
D owns c and still owns c+2. The boundary C at1 survives because c>=2.
The D at c+2 survives because c+2<=L-2 when d>=3. The next three swaps
only use L,L+1,L+2,which become B,A,D. Hence the seventh edge really
is C at c+1 followed by D at c+2;D is positive then. The eighth really
is B at0 followed by the retained C at1;C is positive and B negative.
This verifies every donor/receiver in the displayed calculation.

**Where the representation helped.** One pair of internal C/D swaps
first leaves their sums unchanged while making D own the high boundary.
The endpoint relay then changes which bin carries the unit error. A
single different internal swap can pass that positive error to the
retained low C boundary. Thinking only of a simultaneous disjoint flow
misses this change of which error is mobile. The explicit sequence above
has no dependency on the general connectivity argument or MI295's
pending carrying read.

**An infinite contiguous-overlap application.** In the full owner word

    B^b C^c D^d C B A^e,

with b>=1,c>=2,d>=3,e>=1,set target sums=current sums-(1,0,0,-1).
The substring starting at the last initial B has form(M),so it repairs
the targets in8 swaps. Taking b>=2,e>=3 makes every bin size>=3.
This settles that whole placement family on paper,not the general
unique-DCBA word with arbitrary prefix/suffix runs. Nor does it resolve
the other four-bin overlap shapes from MI298 or general SS3.

**Hand positive control beyond the first attempted route.** For
b2,c5,d3,e3,the word has15 values and target sums(A38,B12,C30,D25).
The first idea demanded D own BOTH low/high boundaries of its C/D
interval at once;it required d>=c+1 and fails here. The new sequence
(11,9,6,10,11,10,7,1) gives

    A{11,13,14}, B{0,2,10}, C{1,3,4,5,8,9}, D{6,7,12}.

The literal sums are38,12,30,25,every value0..14 occurs once. The
first route's failure is retained;the error changes carrier instead
of demanding a rearrangement that its sum level forbids.

**Unexpected boundary control:failed module is not nonexistence.** For
b1,c2,d2,e1,the proposed step at c+1 meets two C tokens,so this module
must stop outside its hypothesis. Nevertheless targets(A6,B6,C8,D8)
have A{6},B{2,4},C{0,3,5},D{1,7}. Thus d>=3 is a sufficient condition
for THIS repair,not a necessary feasibility threshold. The smaller
c1 boundary loses the retained low C after the third swap and is also
outside this module;MI298's different five-swap family is not silently
substituted. No machine run has been used to fill an infinite quantifier.

**Next mathematical question.** Does every minimum3 contiguous-DCBA
word admit this module,its reflection,or a neutral reshaping that creates
one? The general word is A^a B^b C^c D^d C B A^e B^f C^g D^h,with
d,e>=1 and total bin sizes>=3;our family sets a=f=g=h=0 and uses
particular run lengths. Missing placements remain explicit. A full
consecutive TWO-bin interval with one unit error can be reshaped using
the known lattice picture;punctures and two exact-zero bins cannot be
treated the same way. Stay with that distinction rather than opening
an unconditional larger graph enumeration.

What changed:the contiguous block now has a local eight-swap release
with a literal check of every move,and the lattice picture suggests how
to create such room. Gut:delight at changing which bin carries the
error;warmth comes from that new representation,not the history of the
topic. Reasoned:one usable module and an application family,still a
SKETCH;allSS3/E28/L8 OPEN. Niggle sweep:local/global offsets preserve
unit differences;other bins are untouched;both middle sums restored;
c>=2 and d>=3 are spent at named positions;the boundary example defeats
a false necessity claim;the known framework is credited and carries
no fresh review cost. Cloud's MI295 review remains the sole carrying
request. Research13min ACTIVE,continue without routine review halt.

### MI300 — B141: a feasible minimum3 instance appears trapped;fixed closure preregistration (2026-10-17 15:10 BST)

**The next missing placement gives a counterexample,not another module.**
After MI299,inspect opposed spare runs:word B^2 D^3 C B A^3 C^2 on
0..11. Its bins and integer targets are

    A{7,8,9}, target23; B{0,1,6}, target7;
    C{5,10,11}, target26; D{2,3,4}, target10.

Deviations are(1,0,0,-1),error2. All four sizes are3. SS holds with
minimum proper-subset slack2. A target partition DOES exist:

    A{4,8,11}, B{0,1,6}, C{7,9,10}, D{2,3,5}.

Nevertheless its nonincreasing SINGLE-TOKEN-swap component appears to
consist of exactly four states:the start,swap values4/5,swap6/7,and
both commuting swaps. This assertion includes ALL cross-bin swaps,
not merely adjacent values. At each state the only nonincreasing
cross-bin moves appear to be those same two swaps. No goal is present.
Therefore the global minimum3 neutral-single-swap escape claim should
be refuted,even though SS3 itself is untouched. MI299's module stays
valid but cannot be forced in every such component.

**A barrier-crossing witness is already literal.** Swaps(4,5),(4,7),
(9,11) give errors2,2,4,0 and the target partition above. After the
first swap,simultaneously exchange A's{7,9} with C's{4,11}:both sides
have size2,their sums are16 and15. That single TWO-FOR-TWO operation
reduces the error2 directly to0. The obstruction is the chosen move
granularity,not feasibility. A temporary increase in the single-swap
error can be necessary;record that fact instead of generating more
neutral local modules in pursuit of a false universal strategy.

**Preregistration before testing.** Source
tests/probes/instinct/ss3_pair_barrier.py. ONE fixed instance,no census.
P1:SS minimum proper slack2 and literal supplied target partition pass.
P2:the complete nonincreasing all-pair closure has EXACTLY4 states,
two nonidentity neighbors each,all at error2. Check all54 cross-bin
token swaps per state. Independent arithmetic predicts the new error
from the old deviations/value difference;compare with literal sums
after the actual swap. Compare the entire reached set to the explicit
four states above,not just its size. CF to reject:existence implies
nonincreasing single-token-swap reachability. P3:the three-swap errors
are2,2,4,0;combining the last two gives errors2,2,0. If P2 holds,error
parity and this path establish exact minimum all-pair-path barrier4.

Unexpected checks:reflect all values and target sums,and translate all
values by-11;the COMPLETE closed-state and allowed-neighbor maps must
correspond. Three arms,216 pair checks each.5CPU/10wall seconds/64MiB,
12wall external watchdog,one process. Stop first failure/cap,no repair,
retry,larger graph or automatic two-for-two enumeration. Publish this
registration and source before ONE invocation;raw remains outside git.
Record searches/source orientation MI299;no external theorem is needed
for this literal finite refutation.

Signal:surprise and unease. The local successes had encouraged a
stronger monotonicity hope than SS3 requires. Push on that strategy,
pull toward higher-order exchanges;tip it with this cheap closure test.
If it passes,park universal nonincreasing SINGLE-token swapping. Next
reason about equal-cardinality subset exchanges,not a raised search cap
or an ever-longer neutral-module catalogue. This is a change on evidence,
not a halt for Cloud's review. SS3/fullE28/L8 remain OPEN.

### MI301 — B141 outcome: monotone SINGLE-token escape is refuted;change the move (2026-10-17 15:12 BST)

**COMPUTED finite refutation,one registered invocation.** Prereg/source
5f6823f0/MI300,Intel CPU. Every prediction/control passes. The complete
nonincreasing all-cross-bin-single-token-swap closure has exactly the
FOUR predicted states,all error2,two allowed neighbors each. No target
state lies in it. All54 possible cross-bin swaps checked per state;
216 per arm,648 total,with independent affine-vs-literal arithmetic.
Whole closure/neighbor maps reflect and translate exactly. SS minimum
proper slack2 and the positive target partition both verify literally.
Same-worker implementation controls are self-checks,not another party's
replication. No new assumption about feasibility is needed.

**The finite closure also has a short hand explanation.** At error2,
a high-to-low token transfer from a bin of deviation+1 to one of-1 avoids increasing
error only when its size is1 or2. Between a positive/zero or zero/negative
bin,only a unit transfer can be neutral. All other nonidentity swaps
increase error. In these four states,the positive and negative bins have
minimum positive high-to-low difference3:

    state              positive bin    negative bin   min positive gap
    original           A               D              7-4=3
    swapped6/7         B               D              7-4=3
    swapped4/5         A               C              7-4=3
    both               B               C              7-4=3

The only permissible unit transfers with a zero bin use values4/5 and
6/7. They commute and their reverses are the same edges. This proves
closure without assuming that local absence of strict descent suffices.
The machine audit explicitly checked all the other swaps as well.

**The exact barrier and the move that bypasses it.** The supplied path
(4,5),(4,7),(9,11) has errors2,2,4,0 and reaches the target partition.
Since every total-zero deviation vector has even L1 error,and no goal
is reachable at error<=2,the minimum possible maximum error along ANY
single-token-swap path to ANY target partition is EXACTLY4. This is a
property of this instance/start,not a bound for every SS3 instance.
After the first swap,the two-for-two exchange A{7,9}<->C{4,11}
transfers ONE sum unit with cardinalities fixed. As one atomic move it
gives errors2,2,0. The issue is not SS3 existence;it is insisting on
single-token swaps and an L1 potential that never rises.

CPU0.002579s,wall0.002576693s,external watchdog0.158224709s,
peakRSS16437248bytes;inside5CPU/10wall/64MiB/12watchdog. No cap,
retry,source repair or expansion. Raw report1340bytes SHA256
4e604114fa62259d971ee78fb33b004b080b9477e8a4362490b80fb981d34f1d;
stdout728bytes81e6999e0b108a879dfd43def064c7ad0cf673238aa8cf70ae047b7f1df8a0eb;
stderr empty. Raw local,not uploaded. Only source outcome header added
after the run,no computation-affecting change.

**Decision on evidence.** Park universal nonincreasing SINGLE-token
escape and further neutral-module generation in pursuit of it. MI295's
THREE-bin candidate and MI298/299's local constructions are unaffected,
but cannot be promoted to all minimum3 bins by this strategy. No new
two-for-two sufficiency conjecture or automatic higher-order census.
The next bounded inference is structural:when can equal-cardinality
subset sums supply a unit transfer that single-token gaps miss,and
how can such transfers be composed without reusing elements? Search
the relevant record/literature before adopting a new universal rule.

Gut:disappointment at the monotonicity hope,surprise and relief at a
literal feasible obstruction. The push tipped:stop that strategy. Pull
now toward subset exchanges because they repair this exact failure,
not because another class must succeed. Reasoned verdict:change move
granularity/potential;SS3/fullE28/L8 still OPEN. Niggle sweep:ALL pair
swaps,not adjacent only;entire closed component,not just one local
minimum;known feasible target prevents a false existence refutation;
even-error argument plus explicit path proves the instance's barrier;
compound exchange preserves both cardinalities;no universal higher-order
claim smuggled in. Cloud is flagged with this correction.13min research
ACTIVE,no routine review halt or running job.

### MI302 — B142: the trap is a family;opposite gaps provide an atomic unit transfer (2026-10-17 15:19 BST)

**Hand PROOF-SKETCH,no new experiment or independent review.** Question:
what property makes MI301's two-for-two repair work,and does it explain
more than one fixture? The pull is toward the cancellation of two
oppositely directed gaps,not toward declaring a new universal move bound.
Record searched:`two.for.two|equal.cardinality|subset.exchange|pair.sum|Graver|Markov.basis`
AND `SS3|exchange|prescrib|sum|bin`:50 hits/17 files. MI300-301 are the
relevant literal precedent;no prior uniform opposed-run family found.
Bounded literature search found classical compound augmentation,not
this family. Read the primary Graver optimality statement/proof noted
in PRIOR-ART;no theorem about two-for-two sufficiency is imported.

**The arithmetic criterion.** Suppose one current bin P owns u,v and
another Q owns x,y,all four values distinct. If u-x=H+1 and y-v=H>0,
then exchanging P's{u,v} with Q's{x,y} transfers ONE sum unit P->Q
while preserving both sizes. The large forward gap and the slightly
smaller reverse gap cancel. This is elementary subset-sum arithmetic,
not a novelty claim. Scheduling the two one-for-one swaps separately
can overshoot even though the compound move improves the objective.

**An infinite family with the exact same trap.** Let b,g>=2,d,e>=3,
p=b+d,and n=b+d+e+g+2. Partition0..n-1 by

    B^b D^d C B A^e C^g,

and set prescribed sums=current sums-(1,0,0,-1) in A,B,C,D order.
The four bin sizes are e,b+1,g+1,d,all>=3. In sets:

    A={p+2,...,p+e+1}; B={0,...,b-1,p+1};
    C={p} union{p+e+2,...,p+e+g+1}; D={b,...,p-1}.

Claim for this whole family:targets ARE feasible,and every path to any
target partition using only single-token swaps must reach error>=4;
there is a three-single-swap path attaining maximum error4. The start's
entire nonincreasing component has exactly four states. Thus MI301's
obstruction persists at arbitrarily large sizes;it was not a tiny-pool
accident. This family claim remains an unreviewed hand derivation.

**Four-state closure for arbitrary parameters.** The two neutral swaps
are(p-1,p) and(p+1,p+2). They commute. The positive/negative bins in
the start,the second swap alone,the first alone,and both,respectively,
are(A,D),(B,D),(A,C),(B,C). In EVERY case,the minimum positive
high-to-low difference between a positive and negative bin is
(p+2)-(p-1)=3;all remaining positive-bin values are below,or at least
three above,negative-bin values. A one-for-one transfer between them
must have magnitude1 or2 to avoid raising error2,so none qualifies.
Transfers involving a zero bin can be neutral only for difference1.

The only allowed unit transfers are the two swaps just named and their
reverses. The outer B/D and A/C boundaries have wrong charge directions;
the core's middle adjacency joins two zero bins;the new adjacency just
inside either long D or A run also has the wrong direction. Inside a
run no ownership changes. This exhausts adjacent integer differences,
and the magnitude classification exhausts nonadjacent swaps. Hence the
nonincreasing component is precisely the four commuting-swap states,
all error2,as in MI301. This is a whole-component argument,not merely
absence of strict improvement at the start.

**Feasibility and a uniform repair.** First swap(p-1,p),moving the
deficit from D into C. CURRENT C now owns x=p-1,which originally
belonged to D. Choose

    u=p+2, v=p+e+1 in A;
    x=p-1, y=p+e+3 in current C.

These are distinct:e>=3 separates A's first/last values,and g>=2
supplies the second value in C's upper run. The gaps are u-x=3 and
y-v=2. Thus the two-for-two exchange restores A and C to their targets;
B is unchanged and D already has its target. Explicit target partition:

    A*=(A minus{p+2,p+e+1}) union{p-1,p+e+3};
    B*=B; D*=(D minus{p-1}) union{p};
    C*=(C minus{p,p+e+3}) union{p+2,p+e+1}.

Every value is still used once and every size is unchanged. Changes
to the original four sums are(-1,0,0,+1),as required. Therefore the
targets satisfy SS by the necessary subset-sum bounds;SS feasibility
was not assumed in proving existence. No generic SS3 theorem is used.

The sequential swaps(p-1,p),(p-1,p+2),(p+e+1,p+e+3) have errors
2,2,4,0. The four-state closure rules out reaching any goal at error<=2;
error parity then makes the minimum possible path barrier EXACTLY4.
As two constructive atomic operations,the unit preparation and the
two-for-two exchange instead have errors2,2,0. Grouping operations is
legitimate for a construction,but supplies no universal neighborhood
bound or convergence theorem.

**Hand controls and unexpected symmetry.** b2,d3,e3,g2 gives exactly
MI301's original fixture AND its independently checked target witness:
A{4,8,11},B{0,1,6},C{7,9,10},D{2,3,5}. For a nontriple A,take
b2,d3,e4,g2:n13,targets(A33,B7,C28,D10). The formula gives
A{4,8,9,12},B{0,1,6},C{7,10,11},D{2,3,5};direct sums and the
complete0..12 token list check. This does not rely on taking complements
inside two triples. Unexpected reflection:reverse all values and swap
names A<->D,B<->C;the SAME family reappears with parameters
(b,d,e,g)->(g,e,d,b),still inside the hypotheses. Deviations stay
(1,0,0,-1). Translation also leaves the gap3-minus-gap2 identity intact.
No new enumeration or two-for-two search was run;these are hand checks.

**What this teaches and what it does not.** The obstacle is a missing
NET unit transfer,not a lack of individual large transfers. A full
consecutive pool plus run placement creates two opposite gaps differing
by1 here. The third-element hypotheses give distinct usable endpoints;
we have not shown that arbitrary minimum3 partitions provide them.
Atomic subset exchanges can still reuse tokens along a proposed flow
path;their compatibility cannot be assumed any more than MI292's.

Next bounded question:find a structural condition on the current bins'
equal-cardinality sum spectra that supplies compatible unit transfers,
or a concrete obstruction that defeats that condition. In particular,
two two-token witnesses passing through a size3 bin MUST overlap;merely
enlarging the unit-transfer graph does not fix the scheduling inference.
The present family uses one compound exchange,not such an assumed path.
Do NOT replace
the refuted single-token rule by an unsupported assertion that two-for-two
always suffices. No solver restart,larger census,PROOFS entry or new
carrying-review queue. Cloud's MI295 read is independent of this work.
General SS3/E28/L8 remain OPEN,13min research ACTIVE.

Gut:warmth at a uniform explanation rather than another isolated repair;
unease is now about compatibility and move size. Reasoned:a precise
family and mechanism,not global sufficiency. Niggle sweep:use CURRENT
C ownership after the preparation;four chosen values distinct;net unit
and cardinalities both checked;closure includes all single-token swaps;
target witness is constructed without assuming SS3;large-family claim
is hand SKETCH,not a machine census;no circular use of a better unknown
partition to justify an improving exchange. Continue on those terms.


### MI303 — B143: a compound path can require an outside bin;an exact local compatibility test (2026-10-17 15:36 BST)

**Hand PROOF-SKETCH,no experiment or independent read.** Question:does
having two compound unit-transfer edges through a size3 bin imply that
the three bins can jointly attain their targets? The pull is toward
actual token compatibility;the unease is that a graph forgets its edge
witnesses. A negative answer would change the construction strategy:
allow outside bins to help,rather than promise a repair confined to a
selected path. This is a route test,not a new SS3 theorem or carrying
review request.

Record searched:`subset.exchange|two.for.two|unit.transfer|exchange.path`
AND `compatib|overlap|schedul|disjoint`:7 hits/3 files,MI292/298/302
relevant. Follow-up `pair.sum|two.sum|disjoint.pair|overlap.*witness|path.local|off.path`
AND `SS3|exchange|prescrib|sum|bin`:61 hits/20 files,no earlier local-fork
criterion found. A bounded primary-literature search returned background
on prescribed partitions/subset sums,no compatibility theorem adopted.
No novelty claim for the elementary matching argument below. The hand
kill test is to force two required target triples to use the same token,
while constructing a full-interval solution using an outside bin.

**A feasible full-interval countercontrol to path-local completion.**
For any integer M>=65,partition0..M+1 into

    A={2,29,M}; B={10,20,30}; C={4,35,M+1};
    R=all remaining values.

Sizes are3,3,3,M-7,all>=3. Prescribe sums

    (s_A,s_B,s_C,s_R)=(M+30,60,M+41,sum(R)).

The current deviation is(1,0,-1,0). There are compound unit edges
A->B from A{2,29}<->B{10,20} (31-30=1),and B->C from
B{10,30}<->C{4,35} (40-39=1). Their middle-bin witnesses overlap
at10. This is exactly a two-edge directed unit-transfer path,not a
missing-edge complaint.

Nevertheless NO reassignment of the union A+B+C,even changing all
nine tokens at once,can realize these three targets. Among its seven
small values S={2,4,10,20,29,30,35},the largest triple sums to94.
Both large values in a triple give sum>=2M+3. Thus a target triple
of sum M+30 or M+41 must contain exactly one of M,M+1. A needs a
small pair of sum30 with M,or29 with M+1;only {10,20} of sum30
exists. C needs41 with M,or40 with M+1;only {10,30} of sum40 exists.
Consequently A is forced to {10,20,M} and C to {10,30,M+1},sharing10.
This rules out arbitrary three-bin reassignment,not just either order
of the two named edges. M>=65 ensures the no-large-value bound for A;
no claim that this parameter threshold is minimal.

The full problem IS feasible. Swap A's2 with R's1,then R's5 with
C's4. Both1 and5 are initially in R;these swaps use disjoint tokens.
Errors are2,2,0;R gains1 then loses1 in sum. The final special bins are

    A*={1,29,M}; B*=B; C*={5,35,M+1};
    R*=(R minus{1,5}) union{2,4}.

Their sums and sizes check directly. Hence the full target satisfies
SS,without assuming SS3. The necessary rank bounds even hold in the
punctured nine-token pool:its least triple sum is16,largest2M+36,
and each of M+30,60,M+41 lies between them. Bounds for two bins
are complements of these single-bin bounds. This does NOT contradict
MI295,whose three-bin pool is consecutive. Holes and a frozen outside
bin change that hypothesis.

**An exact local test for the shared-middle fork.** More generally let
the middle bin be {t,y,u},and let the chosen two-token witnesses in
A and C be X and V,all seven active tokens distinct. Assume

    sum(X)=t+y+1; sum(V)=t+u-1.

A has deviation+1,B zero,C -1. Freeze all other tokens in A and C.
A repair among these seven tokens exists iff the seven-token pool has
DISJOINT pairs of sums alpha=t+y and beta=t+u. Necessity follows
from the two endpoints' required sums. Conversely put those pairs in
A and C;the other three tokens go to B,and conservation gives B's
original sum t+y+u. This is a constructive condition,not a presumed
flow composition.

For any set of distinct integer tokens,all pairs of a fixed sum form
a matching. If alpha!=beta and BOTH sums have at least two pair
representations,disjoint choices always exist. To prove it,choose two
disjoint alpha edges. If two beta edges each met both alpha edges,
the beta edges would cover exactly the same four vertices;their sums
would give2beta=2alpha,a contradiction. Thus some alpha/beta pair
is disjoint. Since each color class is nonempty,the ONLY failure is
that one sum has a unique pair and every pair of the other sum meets
it. The fork has alpha!=beta because y!=u. This elementary two-color
matching test is not claimed new.

**Positive hand control with the SAME middle bin.** Replace the
endpoint witnesses by X={3,28},V={12,27};keep B={10,20,30},and
spares M in A,M+1 in C. The same unit differences31-30 and40-39
hold. Now sum30 has pairs {10,20},{3,27};sum40 has
{10,30},{12,28}. Choose disjoint {3,27} and {10,30};put
{12,20,28} in B. All three target sums are attained,even though
the original witnesses still shared10. This distinguishes token
conflict from absence of alternatives:overlap alone is not a proof
of impossibility. No enumeration was run.

**What changed.** The seven-token fork has a direct compatibility
criterion,and the full-interval family proves that even arbitrary
path-local completion is too strong. The full interval may need to
supply ALTERNATIVE witnesses or an outside relay;its presence cannot
be thrown away by freezing all off-path bins. Next cheap mathematical
question:can the interval's ownership force such alternatives in a
minimal obstructed fork,or is a global cut/augmentation statement
needed? Do not assert two-for-two sufficiency,raise a solver cap or
restart neutral-module generation. MI295 remains independent and
pending;no new PROOFS entry/review job. General SS3/E28/L8 OPEN.

Gut:the compatibility pull remains specific,with relief at an exact
answer rather than a larger search. There is also a push away from
repeatedly repairing a chosen path. Fresh choice:I would choose the
full-interval mechanism now,not another catalogue of local repairs;
this is the trajectory change. Reasoned verdict:local route narrowed,
global existence unresolved. Niggle sweep:the countercontrol has a
literal full solution;all four bin sizes>=3;the local contradiction
allows ALL nine tokens to move;punctured/consecutive pools distinguished;
the matching argument requires two representations of EACH sum;the
positive control preserves B's sum,not merely total sum. No unknown
solution assumed to obtain any witness.13min research ACTIVE.


### MI304 — B144: four bins with a near-minimum two-bin cut have an explicit construction (2026-10-17 15:48 BST)

**Hand PROOF-SKETCH,no new run or independent read;novelty unknown.**
Question:can a near-tight SS cut supply a GLOBAL construction,without
first selecting a transfer path and freezing its outside bins? Pull:
a cut only one unit above the minimum forces its token set completely.
That is more geometric information than a static exchange graph.
Record searched:`tight|slack.one|slack1|near.tight|uncross|initial.segment`
AND `SS3|prescribed|bin|sum`:37 hits/23 files,no earlier SS near-cut
construction found. The existing source calibration remains:the
fractional/slack literature is not an integral sufficiency theorem.
Standard fixed-cardinality interval sums are known and their elementary
proof is filed in PRIOR-ART,status known,reproved here. Bounded searches
for fixed-cardinality one-hole sums found no exact statement adopted;
no novelty claim is made for the arithmetic of the pools.

**The precise boundary claim.** Write L(r)=r(r-1)/2 and
U_N(r)=r(2N-r-1)/2. Let four bin sizes a,b,c,d>=3 sum to n.
Let integer targets s_A,s_B,s_C,s_D sum to L(n),with

    L(c_i)<=s_i<=U_n(c_i) for each bin i.

Set m=a+b and l=c+d. If

    s_A+s_B=L(m)+delta,  delta in{0,1,2},

then a prescribed-size,target-sum partition of0..n-1 exists.
Thus SS suffices on this four-bin boundary region;in fact this claim
needs only the SINGLE-bin inequalities and the displayed pair sum.
The rest of the all-subsets condition is then automatic from the
constructed partition. This does not settle arbitrary four-bin SS3.

**Choose the two token pools outright.** Put

    P={0,...,m-2} union{m-1+delta}; Q=(0..n-1) minus P.

P has m elements,sum L(m)+delta. For delta0 it is an interval.
For delta1 it is the UNIQUE m-set one sum unit above the minimum:
if sorted x_i have nonnegative nondecreasing offsets x_i-(i-1),
the offsets must be0,...,0,1. For delta2 the chosen shape is sufficient
here;it is NOT asserted to be the only shape.
Reflect Q by x->n-1-x. Its image is

    K_l(delta)={0,...,l} minus{l-delta},

with l elements and sum L(l)+delta. In particular K_l(0) is an
ordinary interval and K_l(1) is the same near-end one-hole shape as P.
At delta2,P has one exceptional upper value;K has one deleted value
inside its full span.

**All required subset sums in P are present.** For m=r+q,r,q>=3,
the r-subset sums of P are the union of two integer intervals:

    [L(r),U_(m-1)(r)]
    [m-1+delta+L(r-1),m-1+delta+U_(m-1)(r-1)].

They correspond to omitting or using its exceptional largest token.
The first upper endpoint plus1 minus the second lower endpoint is

    (r-1)(q-1)-delta >=4-delta>=2.

So they overlap,and their union is exactly[L(r),U_m(r)+delta].
This calculation also covers delta0,but the ordinary interval result
alone suffices there. The known interval construction gives actual
subset tokens,not merely a fractional existence statement.

**The reflected outer pool has the same interval property.** For
delta0/1 this follows from the preceding paragraph. For delta2,
K_m(2)={0,...,m-3} union{m-1,m}. If r+q=m,r,q>=3,split according
to taking zero,one or both of the two upper tokens. The three attainable
integer intervals are

    I0=[L(r),U_(m-2)(r)],
    I1=[m-1+L(r-1),m+U_(m-2)(r-1)],
    I2=[2m-1+L(r-2),2m-1+U_(m-2)(r-2)].

For I1,the two choices of upper token shift the same interval by1,
so their union is an interval as written. The successive overlaps are

    max(I0)+1-min(I1)=(r-1)(q-2)-1>=1,
    max(I1)+1-min(I2)=(r-2)(q-1)-1>=1.

Consequently the entire spectrum is[L(r),U_m(r)+2]. All subset sizes
in these formulas are valid because r,q>=3. This explicit overlap
calculation is where the minimum3 hypotheses enter the delta2 proof.

**Finish the four-bin construction.** The lower bounds for A and B,
plus their total L(m)+delta,give

    L(a)<=s_A<=L(m)+delta-L(b)=U_m(a)+delta.

Choose a tokens of P of sum s_A;give its complement to B.
For C and D use reflected targets

    t_C=(n-1)c-s_C; t_D=(n-1)d-s_D.

The original global UPPER bounds give t_C>=L(c),t_D>=L(d).
Conservation gives t_C+t_D=L(l)+delta. Thus
L(c)<=t_C<=U_l(c)+delta;choose c tokens in K_l(delta) with that
sum,and give its complement to D. Reflect both sets back into Q.
Their original sums are s_C,s_D,all four cardinalities are correct,
and P,Q are disjoint and cover the full interval. No unknown solution,
SS3,MI295 or neutral-swap convergence was assumed. To implement this
construction,select one of the two/three displayed intervals containing
the requested sum and use the explicit known interval-subset formula.

**Hand controls;no enumeration.** At n12,sizes3^4,delta1,targets
(7,9,24,26),the construction gives A{0,1,6},B{2,3,4},C{5,8,11},
D{7,9,10}. For delta2 with unequal sizes(3,4,3,4),n14,targets
(9,14,30,38),take A{0,1,8},B{2,3,4,5},C{6,11,13},
D{7,9,10,12}. Totals,sizes and complete interval coverage check by
inspection. Reflection of the latter outer bins gives sums9 and14
in K_7(2)={0,1,2,3,4,6,7},checking the shift with unequal sizes.

**Unexpected boundary check:delta3 does NOT follow from these pools.**
For n12,sizes3^4,targets(3,15,19,29),all SS bounds hold:
singles in[3,30],pairs18,22,32,34,44,48 in[15,51],and triples
are their single-bin complements. The pair A+B has slack3.
Our chosen P would be{0,1,2,3,4,8};its reflected Q is
K_6(3)={0,1,2,4,5,6}. C/D would require reflected sums14 and4.
There is NO triple of sum4 (the least is3,the next5). So this
specific construction fails. The full target IS feasible:
A{0,1,2},B{3,5,7},C{4,6,9},D{8,10,11}. Its low pair uses a
different rank3 shape. This retains a real boundary for the method,
not a counterexample to SS3. No delta3 universal assertion is made.
The interior target(16,16,17,17) at n12 also has no admitted near-minimum
pair cut;this result does not silently cover the whole four-bin case.

**Step-back at about90 minutes since the restart.** The previous
exchange approach yielded a genuine obstruction and was changed on
evidence;there is no reason to iterate its failed local promise.
Current work is interesting because the full interval now prescribes
a pool shape and the arithmetic supplies a construction. Frustration
is with the temptation to call a new boundary a global solution.
Fresh choice:I would work the near-cut geometry now even without the
previous investment. Next cheap question:at slack3,can the alternate
rank3 shapes systematically replace the failed canonical split?
Keep the first failed pool as a control;do not expand a solver census.
Cloud gets a batched READ-LEDGER update,not another automatic carrying
review queue. MI295 remains pending,not a halt gate.

Gut:warmth at a constructive change of representation,not at retaining
the old label. Reasoned:an explicit four-bin boundary region,still
hand SKETCH;SS3/E28/L8 OPEN. Niggle sweep:delta2 shape chosen,not
claimed forced;upper bounds become lower bounds only AFTER reflection;
all subset intervals checked including their overlap endpoints;
unequal-size control checks the c-dependent reflection;delta3 failure
and literal full witness prevent false extension;known interval lemma
credited,no novelty claim for it;no dependence on the unreviewed
three-bin theorem.13min research ACTIVE,no experiment running.


### MI305 — B145: a shared boundary window gives a quadratic four-bin region (2026-10-17 16:00 BST)

**Current status,2026-10-17 17:36 BST:PROVED in the stated scope.**
Cloud CL434/5ef12b10 completed the independent carrying read and
independent finite checks. Original sketch wording below is historical.
Novelty remains unassessed;no full SS3/E28/L8 conclusion. See MI317.

**Hand PROOF-SKETCH,not independently verified;novelty unknown.**
The question was whether alternate rank3 shapes repair MI304's canonical
failure. Pull:the rank3 shape with offsets2+1 has the same form after
reflecting its complement. Delight at that symmetry suggested a window
rather than another list of repairs. It leads to a uniform lemma and
a broader four-bin boundary result. No experiment was run;all controls
below are hand derivations,not a machine certificate.

Record searched:`rank3|slack3|near.minimum|one.hole|pair.cut` AND
`SS3|four.bin|subset.sum|pool`:9 hits/3 files,MI304 relevant.
Follow-up `boundary.window|square.*slack|prefix.*subset.sum|sum.*spectrum|core.*window`
AND `prescribed|SS3|bin|subset`:2 irrelevant hits/2 files,no earlier
boundary-window lemma found. Bounded literature searches for prescribed
sizes/sums/slack and restricted subset sums returned no exact theorem
adopted;this does not establish novelty or absence. The standard
interval-subset lemma remains known background,PRIOR-ART/MI304.

**The general pool lemma.** Fix h>=1,and m=r+q with r,q>=h+1.
Put ell=m-h. Let T be ANY h-element subset of the2h consecutive
values ell,...,ell+2h-1,and define

    P={0,...,ell-1} union T.

If sum(P)=L(m)+delta,then the sums of r-element subsets of P are
EXACTLY every integer in[L(r),U_m(r)+delta]. In particular there
are no missing sums,regardless of which h window values T uses.
Here L(r)=r(r-1)/2,U_N(r)=r(2N-r-1)/2,as in MI304.
The minimum is L(r) and maximum sum(P)-L(q),because the prefix
contains the first r and first q nonnegative integers. The issue
is every integer BETWEEN the extrema.

**First fill each fixed-window-count band.** Write T={z_1<...<z_h}.
For j=0,...,h,set p=r-j and let B_j be the sum of the j smallest
z's,T_j the sum of the j largest (both0 when j0). Prefix subsets
of size p have every sum in[L(p),U_ell(p)]. Here

    1<=p<=ell-1,  ell>=h+2,

because both r and q are at least h+1. This interval has width
p(ell-p)>=ell-1>=h+1.

Consecutive values of T differ by at most h+1:there are only h
omitted values in its2h window. For0<j<h,move an upper j-subset
from the j smallest to the j largest by increasing selected INDEX
positions one adjacent index at a time. Such a monotone chain exists
in the ordered-subset lattice,and each increase in its sum is at
most h+1. Therefore gaps between consecutive attainable upper
j-subset sums are at most h+1. Adding the prefix interval bridges
all those gaps. For j0 or h the upper sum is unique. Consequently
the attainable sums using EXACTLY j window tokens fill the interval

    I_j=[L(r-j)+B_j, U_ell(r-j)+T_j].

This argument does not assume that T's own subset sums are continuous.
That would generally be false;the prefix interval fills their gaps.

**Then join all the bands.** For0<=j<h,let
D_j=max(I_j)+1-min(I_(j+1)). The known interval endpoints give

    D_j=(r-j)(ell-(r-j)+1)+T_j-B_(j+1).

Since z_(h-j+i)-z_i>=h-j for i1..j,
T_j-B_j>=j(h-j). Also z_(j+1)<=ell+h+j,because the h-j-1 later
values must still fit in the window. Thus

    D_j >= F(j)
    F(j)=r(q-h)-q+j(r-q+2h-2)-2j^2.

F is concave. Write alpha=r-h-1>=0,beta=q-h-1>=0. Its endpoint
values on0..h-1 are

    F(0)=alpha+h*beta+alpha*beta,
    F(h-1)=h*alpha+beta+alpha*beta.

Both are nonnegative (also when h1,the endpoints coincide).
Hence D_j>=0 for every adjacent pair of bands. Their endpoints
increase with j,because an upper-window value is larger than every
prefix value. So the integer intervals meet or touch consecutively.
Their union runs from the overall minimum L(r) to overall maximum
sum(P)-L(q)=U_m(r)+delta. This proves the hand pool lemma.
A zero D_j means adjacent integers with NO missing integer;strict
overlap is unnecessary.

**The four-bin consequence.** Let four sizes a,b,c,d>=h+1 sum to n.
Let integer targets total L(n),with the necessary SINGLE-bin bounds
L(c_i)<=s_i<=U_n(c_i). Suppose for m=a+b

    s_A+s_B=L(m)+delta,  0<=delta<=h^2.

Choose h indices Y from0..2h-1 of sum L(h)+delta. Such a subset
exists by the known interval lemma,since h-subset sums of a2h
interval span EXACTLY h^2 above their minimum. Put ell=m-h,
T=ell+Y,and P={0..ell-1} union T. Then sum(P)=L(m)+delta.
The lower bounds on A/B imply
L(a)<=s_A<=U_m(a)+delta. Apply the pool lemma to partition P
into A/B with their prescribed sizes and sums.

Let l=c+d. The complement Q contains all values m+h..n-1,and
the h boundary-window values not selected for T. Reflection x->n-1-x
therefore turns Q into

    {0,...,l-h-1} union T',

where T' is an h-subset of l-h,...,l+h-1. Its sum is L(l)+delta,
by total conservation and reflection. This is EXACTLY the same pool
class;no separate one-hole argument or special rank3 case remains.
The reflected targets are t_C=(n-1)c-s_C,t_D=(n-1)d-s_D.
Global upper bounds give t_C>=L(c),t_D>=L(d),and their total is
L(l)+delta. Apply the same lemma,then reflect back. All tokens
are covered exactly once,with all four prescribed sizes and sums.
No SS3,unknown partition,MI295 or exchange convergence is used.

Thus a pair-cut slack up to(min_i c_i-1)^2 is sufficient under the
single-bin bounds. For minimum size3,take h2:slack0..4,not merely
MI304's0..2. For minimum size4,h3 gives0..9. This is a FOUR-bin
boundary theorem candidate,not an eight-bin theorem or all-SS3 result.
In particular the n12 interior target(16,16,17,17) is still outside
this admission. No full E28/L8 conclusion is claimed.

**Hand controls and the old failure.** At h2,delta3 choose the
window offsets yielding P={0..m-3,m-1,m+1}. Its reflected complement
has the same shape. MI304's formerly failing n12 targets(3,15,19,29)
now give exactly A{0,1,2},B{3,5,7},C{4,6,9},D{8,10,11}.
For h2,delta4,n12,targets(8,11,25,22),use A{0,1,7},B{2,3,6},
C{4,10,11},D{5,8,9}. Their low pool is{0,1,2,3,6,7};its reflection
partner has the same shape. Both controls cover0..11 literally.

For h3,delta7 and unequal sizes(4,5,4,5),n18,choose the low pool
{0..5,8,9,11},and partition it A{0,1,2,11},B{3,4,5,8,9}.
The complement partitions as C{6,7,16,17},D{10,12,13,14,15}.
Targets(14,29,46,64) total153. Reflecting its complement gives
{0..5,7,10,11},a DIFFERENT window selection with the same slack7;
reflected C/D sums are22,21. This checks the any-selection assertion,
not just the self-reflecting rank3 shape.

**Unexpected endpoint and invalid-hypothesis controls.** At
r=q=h+1 and T chosen as the h LARGEST window values,the first and
last band joins have D0=D_(h-1)=0. So the proof must allow touching,
not claim strict overlap;the hand formulas do. If the cardinality
condition is dropped,take h2,m5,P={0,1,2,5,6},r2,q3. Pair sums
miss4 between their minimum1 and maximum11. Thus a long enough
prefix is a real hypothesis,not decorative slack. This does not
show the four-bin slack bound is optimal:other pools may still work.

**What changed and next.** The shape-by-shape boundary route has
contracted to one prefix-plus-window lemma,stable under complement
and reflection. The quadratic slack comes from choosing h of2h
window values,not an empirical fit. The general argument is worth
one carrying read:Cloud is asked to check band continuity,the concave
join bound,and the reflected four-bin consequence as ONE candidate.
Known interval background is not an additional review job. Continue
without a review halt. Next cheap test:preregister an independent
finite audit of all small window selections and complete sum spectra,
with the touching and invalid-cardinality controls retained. No run
is claimed here,and no automatic interior-case census or cap ladder.

Gut:delight at a representation that treats both halves equally;
unease now sits at the algebra joining bands,which is explicit and
can be audited. Reasoned:a general hand PROOF-SKETCH awaiting scrutiny,
not a verified breakthrough. Niggle sweep:upper subset sums need not
be continuous;prefix widths fill them;all p values stay strictly
between0 and ell;the j=h endpoint uses no next band;h1 handled;
zero join means no integer gap;reflected pool really has h window
values;upper target bounds reflected with the bin's own cardinality;
old slack3 countercontrol now has a literal repaired partition.
SS3/E28/L8 OPEN,research13min ACTIVE,no experiment running.


### MI306 — B146 preregistration: independent complete-spectrum audit of the boundary window (2026-10-17 16:10 BST)

**Preparation only;experiment NOT RUN.** Question:does MI305's window
lemma survive complete finite sum spectra computed without its interval
or concavity formulas,and does its reflected four-bin construction
produce literal partitions? Pull is toward checking the carrying
algebra independently,not accumulating more existence samples.
Record searched:`boundary.window|MI305|prefix.*window|window.*spectrum`
AND `audit|subset|SS3|bin`:28 hits/14 files;MI305 and its source/background
are relevant,no earlier complete-window audit found. This is a fixed
validation block for a new proof candidate,not an SS3 census or a
known-lemma reproof. Source:tests/probes/instinct/ss3_boundary_window_audit.py.

**Domain and predictions BEFORE the one run.** h1..3,m2h+2..14,
every h-subset of its2h window,every r=h+1..m-h-1. Exactly216 pools
and962 complete spectra:132 at h1,270 at h2,560 at h3. Predict every
literal combination-sum map agrees with an independent exact cardinality
bitset DP run in reverse token order,and fills the entire claimed
min/max range. Literal combinations also group by actual count j of
window tokens;each full j-band must be continuous,and its literal
joins must match the displayed algebra and dominate F(j)>=0.
Compare F's endpoints with the alpha/beta formulas. These formulas
are checked against literal bands;they are NOT used to generate the
literal or DP sum sets.

For all216 pools,form the actual complement in0..2m-1 and reflect;
predict the same prefix/window shape with equal total sum. Separately
generate ALL n12 target vectors,sizes3^4,single-bin bounds3..30 and
fixed A/B cut slack0..4,by a three-coordinate target loop;predict
exactly730. Using ALL six h2 window choices then gives874 literal
partitions,covering exactly that target domain,with full sizes,sums
and original-token coverage rechecked. This audits the four-bin
consequence,not an extension to arbitrary E28 or all SS3.

**Counterfactual and independent controls.** Dropping r>=h+1 would
falsely predict complete pair sums for{0,1,2,5,6};the audit must retain
the missing4. MI304's old canonical slack3 complement{0,1,2,4,5,6}
must likewise miss triple sum4;the new literal target partition must
still pass. Independent DP/literal full maps and negative translations
by-11 are checked on three fixed small sets. Three MI305 full partition
fixtures,including unequal sizes at h3/delta7,are checked literally.
Unexpected check:for h1/2/3 at the minimum allowed m and largest-window
choice,the first and last join are EXACTLY0,not strict overlap.
A test demanding positive joins should fail;zero must be accepted.

**Stop conditions.** ONE invocation only,after source/prereg push:
10CPU seconds,20wall,128MiB peakRSS(macOS bytes),2M literal subsets,
2MiB report;external25wall watchdog. Stop on first assertion/cap;
no repair/retry/extension,no new sample or full job. Save raw JSON,
stdout and stderr outside git,including failure output. AST/source,
ledger and privacy checks precede the run and are not experiment passes.
No upload of raw artifacts. Prediction is all comparisons/controls
PASS;an infinite hand theorem remains SKETCH regardless of a pass,
and same-worker independent coding is not a second-party read.

After this fixed audit,return to the mathematical limitation:the
quadratic near-cut region leaves the central four-bin targets outside
its admission. Do not mechanically enlarge h beyond cardinalities,
raise caps or launch a wider SS3 census. Cloud's carrying read is
pending,not a halt gate;research13min ACTIVE.


### MI307 — B146 outcome: every registered complete spectrum and literal partition passes (2026-10-17 16:13 BST)

**COMPUTED finite audit;general proof remains PROOF-SKETCH.** The ONE
run preregistered in MI306/source commit9ad722a9 finishes with ALL
predictions and controls passing. No source repair,retry,cap increase
or domain expansion. The only post-run source change is its outcome
header;the computation code is unchanged.

- All216 pools and962 full spectra checked:132 at h1,270 at h2,560
  at h3. Direct combinations enumerate834072 literal subsets in total,
  including the fixed controls. Complete cardinality-bitset DP in
  reverse token order agrees with every literal sum map and the entire
  claimed minimum-to-maximum interval. These are two same-worker
  implementations,not a second-party read.
- Every literal j-band has no holes;each actual join agrees with the
  algebraic expression and dominates the stated nonnegative concave
  bound. All endpoint alpha/beta identities pass. The216 actual
  reflected complements have the required prefix/window form and
  the same total sum.
- The independent target-coordinate loop gives exactly730 n12 vectors
  for the fixed A/B cut slack0..4. Across ALL six h2 window selections,
  874 full four-bin partitions cover EXACTLY that domain. Each is
  rechecked for original token coverage0..11,all four cardinalities,
  and each requested sum. No appeal to a cached feasibility verdict.
- All three literal MI305 witness controls pass,including the h3
  unequal-size/different-reflected-window fixture. Full maps under
  translation by-11 agree in the signed controls.
- Counterfactual retained:the invalid-cardinality pair pool{0,1,2,5,6}
  is still missing4;the old canonical slack3 complement{0,1,2,4,5,6}
  is still missing triple sum4. Both independent instruments agree.
  The repaired slack3 full partition passes. Thus the test has not
  erased either earlier failure to obtain a positive result.
- Unexpected check passes at ALL three minimal-size largest-window
  fixtures:h1/m4/r2,h2/m6/r3,h3/m8/r4. Both extreme joins are
  EXACTLY0,so the integer-touching convention is necessary and used.

CPU0.765846s,wall0.772668419s,external watchdog0.857632725s,
peakRSS24952832bytes. All within10CPU/20wall/128MiB/2M subsets/
2MiB report/25watchdog. Raw JSON261891bytes,SHA256
53a4380346fc30345904c491949f1bef52371aede25264ce82f05fbe9c6824db;
stdout SHA256c21ad258d0c17949ff48d5efad8237f3c548c4e4b38bff6f40ee38fdfaa16026;
stderr empty. Raw stays outside git and was not uploaded.

**What changed.** The general pool lemma and its four-bin consequence
have survived an independent implementation audit over the EXACT
registered scope. The infinite quantifiers still require the hand
argument,and its carrying read remains pending at MI305. This does
not establish novelty or upgrade the general claim to PROVED. It also
does not settle arbitrary four-bin SS3 or any eight-bin base domain.

Next mathematical issue:the proof deliberately supplies EVERY possible
sum in each chosen pool. That is stronger than constructing a pair
of specified target sums,and its cardinality/window limit excludes
the central targets. Can a targeted-sum argument retain complement
compatibility while relaxing that complete-spectrum demand? Start by
understanding that inference by hand,with the explicit hole controls
retained;do not simply enlarge h beyond cardinalities or run another
census. Cloud gets this finite receipt through READ-LEDGER on the
existing carrying candidate,not an additional review request.

Gut:relief and satisfaction that the independent whole maps agree,
particularly the zero joins;the pull is toward the scope limitation,
not rerunning a passing check. Reasoned:finite validation landed;
general proof SKETCH,SS3/E28/L8 OPEN. Niggle sweep:all predicted
counts match independent target enumeration;literal coverage uses
original values,not only bin sums;bitset DP does not use the proof
formulas;actual j-bands test the algebra;failed hypotheses retain
holes;no finite evidence substituted for an infinite proof.13min
research ACTIVE,no computation left running.


### MI308 — B147: targeted sums cross the square bound;the exceptional repair needs a third token (2026-10-17 16:29 BST)

**Hand PROOF-SKETCH;depends on unreviewed MI305,not independently
verified;novelty unknown. No experiment.** Question:can a pool with
a specific missing sum still be useful by changing which reflected
shape receives the requested target? Pull:identify the EXACT missing
values instead of demanding complete spectra from every pool.
Record searched:`central.*sum|targeted.sum|requested.sum|complete.spectrum|boundary.window`
AND `four.bin|SS3|pool|subset`:9 hits/3 files,MI304-307 relevant.
Follow-up `quadratic.*one|square.*one|near.extrem|forced.*minimum|conjugate.*pool|resonan.*bin`
AND `SS3|window|partition|sum`:22 hits/11 files,no prior version found.
Known interval sums/rank-one forced sets are background,not new results.
No novelty or complete literature search is claimed.

**Claim and scope.** For h>=2,let four sizes>=h+1,total n,and integer
targets total L(n),satisfy the necessary single-bin bounds. If some
pair of bins has target sum L(m)+delta,where m is its total size and
0<=delta<=h^2+1,then a prescribed-size/sum partition exists.
MI305 supplies delta<=h^2. Here the new step is EXACTLY h^2+1.
This is a uniform extension,not a general four-bin/SS3/eight-bin result.
At h2 it covers slack5;at h3 slack10. The n12 central target
(16,16,17,17) is still outside it. No automatic continuation to larger
slack is authorized by this argument.

Write k=h+1 and,for any pool size m>=2k,define two shapes of rank
h^2+1 above the minimum:

    X_m={0,...,m-h-1} union{m,...,m+h-2,m+h},
    Y_m={0,...,m-h-2} union{m-h} union{m,...,m+h-1}.

Both have m values,sum L(m)+h^2+1. If X_m is used as the low pool
inside0..n-1,its complement reflected by n-1-x is Y_(n-m).
Conversely using Y_m gives reflected X_(n-m). This is a direct
set-complement identity,not a presumed compatibility of two choices.

**X has all the sums needed.** For any split r+q=m,r,q>=k,
X's r-subset sums fill[L(r),U_m(r)+h^2+1]. To see it,compare to
MI305's largest-window square shape

    {0,...,m-h-1} union{m,...,m+h-1}.

X moves only its largest token one unit higher. Within a fixed count
j of upper tokens,the upper selection sums have gaps at most2,and
the prefix interval fills them,as in MI305. Minimum j-sums are unchanged
for j<h,and increase1 at j=h;maximum j-sums increase1 for j>0.
Thus the first and last band joins are unchanged,and each internal
join increases1. For h>=2 the first and last joins are distinct,so
none deteriorates. MI305's concave join bound for the square shape
therefore proves the assertion,with the new total sum at the upper
endpoint. This comparison fails at h1,where the sole join is both
first and last;that case is excluded and retained below as a control.

**Y has an exact and small exception.** For r,q>=k,a two-bin split
of Y_m satisfies the same endpoint sum bounds,EXCEPT that it is
impossible precisely when one of the bins has size k and requested
sum

    U_m(k)+h^2.                         [its maximum minus1]

There are no other missing sums in the required size range.
If both r,q>=h+2,Y fits MI305 with window parameter h+1,so there
is no exception. If one size is k,set that size r=k and q>=k.
Let e=q+1. Y consists of the lower one-hole pool

    R={0,...,e-2,e}

and h consecutive upper values m,...,m+h-1. With j upper tokens,
the lower count is p=k-j. For1<=j<h,both p and e-p are at least2;
the h1 case of MI305 gives a COMPLETE lower sum interval. Upper
j-sums are also a complete interval. At j0 the same holds unless
q=k;then lower complements are singletons,so the ONLY missing lower
sum is L(k)+1. At j=h,the lower choice is a singleton R,so the
ONLY missing sum in that band is its maximum minus1.

The bounding intervals for these h+1 bands are

    I_j=[L(k-j)+jm+L(j), U_e(k-j)+1+jm+U_h(j)].

For0<=j<h their successive joins are exactly

    G(j)=h(q-h-1)+1+j(3h-q-1)-2j^2.

This is concave;with beta=q-h-1>=0,its endpoint values are
h*beta+1 and beta+1,both>=1. Thus all bounding intervals overlap.
The possible j0 hole is below the next band's minimum;the j=h hole
is above the preceding band's maximum. They remain the only holes
in the whole spectrum. The upper hole is U_m(k)+h^2. When q=k,
the lower hole L(k)+1 is the complement of that SAME upper hole
for the other k-bin. This proves the stated two-bin failure criterion.
The preceding argument is hand algebra,not a new finite audit.

**Choose the shape from the requested sums.** Name the low pair A/B,
total size m,and the outer pair C/D,total size l=n-m. Try X_m first.
Its low pair always splits;its reflected outer Y_l fails only if
an outer size-k bin C has reflected target U_l(k)+h^2.
Try Y_m instead:the reflected outer X_l always splits;failure now
requires an inside size-k bin A of target U_m(k)+h^2.
The single-bin bounds give both pairs exactly the endpoint bounds
needed,as in MI305. Unless BOTH exceptions occur,one choice solves
all four bins. The point is target-specific selection,not claiming
that both pool shapes have complete spectra.

**If both fail,the obstruction forces its own repair.** Relabel the
two exceptional size-k bins as A and C,with other sizes b,d>=k,
so m=b+k,n=b+d+2k. Conservation forces

    s_A=U_m(k)+h^2;        s_B=L(b)+1;
    s_C=(n-1)k-U_l(k)-h^2; s_D=U_n(d)-1.

The near-minimum B and near-maximum D are uniquely forced to

    B={0,...,b-2,b},
    D={n-d-1} union{n-d+1,...,n-1}.

After removing them,the remaining2k tokens,translated by-(b-1),are

    W_k={0} union{2,...,2k-1} union{2k+1}.

The required translated sums are

    s'_A=3L(k)+1;
    s'_C=L(k+1)-1+2k.

Their total is sum(W_k)=k(2k+1). Start with W_k's smallest k-set
S={0,2,...,k},of sum L(k+1)-1. Replace its TWO distinct members
2 and k by k+1 and2k+1. The increase is(k-1)+(k+1)=2k.
Thus

    C'=(S minus{2,k}) union{k+1,2k+1}; A'=W_k minus C'

has the required sums and sizes. Translate back and restore B,D.
This repairs the simultaneous missing-sum case with explicit original
tokens. It works for k>=3 because2 and k are distinct. No unknown
partition or SS3 theorem is invoked to escape the failed pools.

**Hand controls.** At h2,b=d3,the exceptional targets in A/B/C/D
order are(16,4,17,29). The formula gives
A{4,5,7},B{0,1,3},C{2,6,9},D{8,10,11}. All sizes3,full0..11
coverage,correct individual sums. This is the case where both simple
pool choices really fail;the repair changes the low pool.
At h3,b=d4,the targets are(31,7,29,53),n16. The formula gives
A{5,7,9,10},B{0,1,2,4},C{3,6,8,12},D{11,13,14,15}.
It goes beyond MI305's slack9 to10,with full0..15 coverage.

For a nonexceptional selector example at h2,targets(5,15,17,29)
use Y_6={0,1,2,4,6,7}:A{0,1,4},B{2,6,7},C{3,5,9},
D{8,10,11}. The X-first outer failure does not prevent Y from working.
For the opposite choice,targets(3,17,18,28) use X_6={0,1,2,3,6,8}:
A{0,1,2},B{3,6,8},C{4,5,9},D{7,10,11}. No enumeration was run.

**Unexpected check:the third token is essential to this repair.**
At h1,k2,b=d2,the same exceptional reduction gives targets(6,2,8,12),
a relabeling of the known four-pair counterexample from CL432.
B{0,2} and D{5,7} are forced. The residual translated pool is
W_2={0,2,3,5},and A would need a pair of sum4,which does not exist.
The proposed replacement of2 and k would try to remove the SAME
token twice. This is a genuine negative control,not a blanket claim
that every use of h1 fails. It explains the minimum3 threshold for
THIS resonant repair;it does not explain or prove the whole SS3 claim.

**What changed,next,and status.** Missing sums can be classified,
assigned to opposite pool choices,and,when both choices fail,turned
into forced near-extremal bins with an explicit residual repair.
This is the first use of requested sums beyond full-spectrum demands
in this route. Next preregister a bounded independent audit of Y's
exact holes and the exceptional family,including the k2 failure,before
using or extending the claim. No new experiment in this block,no
larger SS3 census,no automatic slack increment. Cloud receives a
READ-LEDGER continuation of MI305's existing carrying candidate,
not an additional automatic review job or a reason to halt.

Gut:surprise and a warm pull at the forced residue reproducing the
old size2 counterexample,then resolving it with a third token.
Reasoned:a general hand candidate dependent on MI305;all claims
remain SKETCH and novelty unknown. Niggle sweep:X's last-token shift
has distinct first/last joins only for h>=2;Y's two endpoint holes
correspond to the two labeled size-k bins,not extra exceptions;
reflection uses each bin's own size;near-extreme sets really are
unique;2 and k distinct is checked;both selector arms and exceptional
repair have literal controls;no conclusion for central SS3/E28/L8.
Research13min ACTIVE,no run left outstanding.


### MI309 — B148 preregistration: exact holes,shape selection and the exceptional repair (2026-10-17 16:39 BST)

**Preparation only;NOT RUN.** Question:does MI308 classify ALL missing
sums of its two reflected pools correctly,and do those holes account
for every failed selector before the exceptional repair? The pull is
toward the size3 threshold doing actual mathematical work;unease is
that a missed endpoint hole could invalidate the whole selector.
Record searched:`MI308|exact.hole|exceptional.*repair|beyond.square|reflected.pool`
AND `audit|SS3|bin|spectrum`:4 hits/2 files;MI308/MI305 relevant,
no earlier targeted-pool audit. Existing primary literature calibration
remains MI305's;no new novelty assertion or prior-art absence claim.
Source:tests/probes/instinct/ss3_targeted_pool_audit.py.

**Predictions BEFORE ONE run.** h2..4,m2(h+1)..16,every split
r,q>=h+1,both X/Y:54 pools/278 COMPLETE spectra (132/90/56 by h).
Literal combination sums must agree with an independently implemented
cardinality set-DP in reverse token order,without band or hole formulas.
X must have no holes. Y must miss exactly U_m(k)+h^2 if r=k,
and its complement if q=k,k=h+1. The actual reflected complement
in0..2m-1 must equal the other shape. Literal Y bands at r=k must
have joins exactly G(j) from MI308,and G(j)>=1.

Independently generate every n12,size3^4 target vector satisfying
single-bin bounds and fixed A/B slack5:predict225. Try X then Y;
predict195 X-first,26 Y-second and4 exceptional repairs. Every
result must literally partition0..11 with original labeled sizes/sums,
and certificate target coverage must equal the independent target set.
Separately test36 exceptional formula witnesses:h2..5,b,d each in
{k,k+1,k+3}. Check forced bins,residual pool,translated requested sums,
full token coverage and all four original bin sums independently.

**Counterfactual,controls,unexpected check.** If h1 is incorrectly
included,X_4={0,1,2,5} would be called complete although pair sum4
is missing. Retain that failure. Independent set-DP/literal complete
maps and signed translations by-17 on three fixed pools must agree.
Unexpected check:the old impossible four-pair target(6,2,8,12)
must fail a separate COMPLETE feasibility oracle on0..7,using no
forced-bin or repair formulas;its W_2 residue must miss sums4 and6.
A positive result there would contradict the hand obstruction and
invalidate an instrument,not settle SS3.

**Stops.** ONE invocation only after source/preregistration push:
10CPU seconds,20wall,128MiB peakRSS(macOS bytes),2M literal subsets,
1000 negative-oracle states,2MiB raw report;25wall external watchdog.
First assertion/cap stops;no repair,retry,domain expansion or cap rise.
Retain raw JSON/stdout/stderr outside git;do not upload. AST/static
checks are preparation,not experiment passes. Predict all comparisons
pass,including retained negative controls. A pass is finite COMPUTED
same-worker evidence;MI305/MI308 remain hand SKETCH pending independent
verification. No new carrying-review request or routine review halt.
Next use the result to reassess the central-case obstruction,not
mechanically increment the slack. Research13min ACTIVE.


### MI310 — B148 outcome: exact holes and every registered exceptional repair pass (2026-10-17 16:40 BST)

**Finite COMPUTED evidence;general MI305/MI308 remain PROOF-SKETCH.**
ONE invocation of MI309's source at prereg869e2960 passes ALL54 pools
and278 COMPLETE spectra.733593 literal subsets agree with independent
reverse-order cardinality set-DP. X is complete;Y misses exactly the
predicted one/two target values. Actual reflected complements and
literal band joins equal the hand formulas throughout the fixed domain.

Every one of the225 independently generated n12 slack5 targets has
a checked original-token partition:195 X-first,26 Y-second,4 forced
repairs,exactly predicted. All36 exceptional-family witnesses,including
unequal sizes,pass coverage/cardinality/individual-sum/residual checks.
The full n8 feasibility oracle returns UNSAT in5 recursive states for
(6,2,8,12),independently of the forced-bin argument. The W_2 pair
sums miss4 and6;h1 X misses4. Signed-map controls all pass. No failure
was repaired away,no second invocation or expanded domain.

Resources on the owner's Intel CPU:0.709003 process seconds,
0.711366743 internal wall,0.803547611 external watchdog wall,
21397504bytes peakRSS;all below registered limits. Raw report87203bytes,
SHA25685822767d1cb43785ad0aadcae322e9d6bf3ab2b93faae0463c951f4c7506f65.
Stdout386bytes,SHA256
63e187ef6157676a00e42e601a01bc752d78756915b07054b28cd7202a6e9784;
stderrempty,exit0. Raw retained outside git as B148 targeted report,
stdout/stderr;not uploaded. Source changes after preregistration are
OUTCOME docstring only;AST outside module docstring is identical.

**What changed.** The complete finite audit supports the exact-hole
classification,not just supplied positive examples. The exceptional
repair works on its fixed unequal-size domain,and an independent
negative instrument agrees that the third token matters. This is
same-worker instrument independence,not a second-party read,proof of
an infinite quantifier or evidence that all central cases follow.

**Step back,next,and verdicts.** Gut:the size3 phenomenon still draws
me because it explains a real old obstruction;the passing audit itself
is reassurance,not another burst of discovery. Reasoned:the live
question has moved from checking these formulas to understanding the
remaining central obstruction. Do not turn this into slack6,slack7,
... by habit. Next cheap step is a hand analysis of what the pair-cut
choice excludes and whether targeting both requested sums gives a
principled replacement. No experiment preregistered for that step.
MI295/MI305 carrying reads remain pending,not routine halt gates.

Niggle sweep:both labeled k-bin exceptions are checked;actual
complements rather than assumed reflected shapes are used;the four
failed selector targets have full partitions;the negative oracle uses
no forced-set formulas;signed sums test representation assumptions;
known results/novelty/infinite claims are not upgraded by this pass.
SS3,E28,L8 remain OPEN. Research13min ACTIVE,no run outstanding.


### MI311 — B149: the complete-spectrum ceiling is structural;central compatibility changes through parity bands (2026-10-17 16:54 BST)

**Hand analysis and trajectory correction;no new experiment or general
existence theorem.** Question:what actually blocks complementary pools
in central four-bin targets? Initial pull is cooler on further boundary
layers,and toward the difference between a bad pool and a bad target.
Record searched:`central.*pool|pool.*central|pair.cut|complementary.pool`
AND `SS3|target|interval`:6 hits/2 files. Follow-up
`universal.*pool|full.spectrum|endpoint.*pool|pool.*endpoint|rank.fiber|sum.fiber|switch.graph`
AND `SS3|four.bin|partition|subset`:2 hits/1 file;MI308 and old MI160,
no prior central pool argument. Known two-level ideal connectivity is
already in PRIOR-ART/MI299;do not refile it as a new theorem.

**Structural guard,one paragraph;no probe,PROOFS entry or review job.**
Let the two low bins have sizes r,q,total m,and the other sizes c,d;
write s=min(r,q),t=min(c,d). If ONE fixed m-token pool P,of sum
L(m)+delta,realizes EVERY split in[L(r),sum(P)-L(q)],it must contain
both initial segments of lengths r and q:attaining the unique minimum
L(r),and attaining the upper endpoint by a complementary q-set of
sum L(q),forces these. If the reflected complement likewise realizes
all its split endpoints,it forces the largest max(c,d) original tokens
outside P. Thus P contains the first m-s values and has only s other
tokens,all below m+t. Its maximum sum is L(m-s)+U_(m+t)(s),which
subtracting L(m) gives **delta<=s*t**. This is a necessary ceiling,
not sufficiency or a sharp completeness threshold. At sizes3^4 it
is9;central target(16,16,17,17) has smallest pair cut32,L(6)=15,
slack17. Thus NO choice of fixed complete-spectrum pool can handle
that example. A target-compatible pool need not contain either forced
endpoint segment. Unexpected check:the size2 counterexample's low
pair slack2 is BELOW this ceiling4;the ceiling does not explain or
remove the genuine integer obstruction.

**Even one-sided coverage fails;literal countercontrol.** For that
central target choose the size6,sum32 pool

    P={1,3,4,6,8,10}; Q={0,2,5,7,9,11}.

P has no triple of sum16. Its two odd values total4. A triple of even
sum uses either zero odd values (minimum4+6+8=18),or both odd
values (maximum1+3+10=14). Q has no triple of sum17. Its two even
values total2. An odd-sum triple uses either both evens (maximum
0+2+11=13),or zero evens (minimum5+7+9=21). Thus neither side
splits into its requested equal triple sums,although all targets are
feasible. This disproves the tempting claim that every correct-size/
correct-total pool is good on at least one side. It does not refute SS3.

**A neutral move repairs BOTH sides.** In P replace1,8 by0,9:
two disjoint adjacent exchanges of opposite signs,performed atomically.
The pool keeps size6,sum32,and even/odd counts4/2. Now

    P'={0,3,4,6,9,10}={0,6,10} disjoint-union {3,4,9},
    Q'={1,2,5,7,8,11}={1,5,11} disjoint-union {2,7,8}.

The first two triples sum16,the latter two17,and all0..11 appear
once. Every bin size3 is retained. These literal hand checks are not
a new enumeration or a general exchange theorem.

**Why that repair works,not just its certificate.** A six-token pool
with four evens and two odds,of sum2a for EVEN a,can split into two
triples of sum a iff it contains the even token

    e=a-(sum of its two odd tokens).

Each even-sum triple must use zero or two odds;both odds must lie
in the same triple. The displayed e is therefore necessary;when it
is present,that triple works and the complementary triple works by
the total sum. The parity-reversed assertion holds for four odds,
two evens and ODD a:the needed odd token is a minus the two-even
sum. In P the required token is12,absent;in P' it is4,present.
In Q the required token is15,absent;in Q' it is7,present. The atomic
move changes where the minority-parity mass sits while preserving
its count,and aligns BOTH required tokens. It is this conditional
spectrum structure,not local value gaps alone,that the example exposes.
The criterion is elementary six-token bookkeeping,not claimed novel.

**What this advances and does not.** The complete-spectrum extension
has a definite stopping reason,not merely a cooling instinct. Central
targets require target-dependent compatibility. But writing the two
sets of good pools and asking them to intersect is merely the original
existence problem in new notation. Connectivity of the fixed-sum pool
space,from MI299's ideal representation,does NOT prove that intersection,
nor a monotone improvement rule. MI301's failed single-swap strategy
stays parked. The next mathematical question is whether the explicit
minority-parity obstruction/repair has a useful extension for larger
or unequal bin sizes;first seek an adversarial hand case. A finite
check would need fresh predictions and source registration;none run.

**Literature orientation.** The bounded primary-source refresh is in
PRIOR-ART:2605.06071v2 and the previously statement-only2312.00089v1
converse proof. The latter cannot supply the missing compatibility
inference;its slack-sufficiency claim fails a known counterexample.
No comprehensive October literature or novelty claim.

Gut:a modest new pull at the simultaneous parity repair,cooler on
more boundary-window increments. Reasoned:a representation limitation
and explicit mechanism,not general progress on the SS3 quantifier.
Niggle sweep:endpoint intervals are nonempty under delta>=0;both bin
minima really are unique;the delta ceiling is only necessary;both
negative triple cases exhaust parity possibilities;the neutral move
uses four distinct tokens;its proof does not assume MI295/MI305/SS3.
Known source claims are not accepted from a theorem label alone.
No new carrying-review job;13min ACTIVE,SS3/E28/L8 remain OPEN.


### MI312 — B150 adversarial guard and loop correction (2026-10-17 17:07 BST)

**One hand guard;no probe,PROOFS entry or review job.** MI311's central
repair cannot yield a constant number of neutral adjacent-pair steps,
even with three bins of size3. For any integer K>=3,let N=11K+1,
P_0=K*{1,3,4,6,8,10},and targets/sizes
(16K,16K,17K,L(N)-49K)/(3,3,3,N-9). A literal full-interval goal is
A={0,6K,10K},B={3K,4K,9K},C={K,5K,11K},D=the complement;
therefore ALL SS bounds hold. P_0's triple sums are K times
{8,10,11,12,13,14,15,17,18,19,20,21,22,24},so their distance from
16K is K. One neutral compound step replacing x,y by x-1,y+1
changes every pulled-back triple sum by at most1:if both changed
tokens are selected,the changes cancel. Hence ANY such path to a
compatible left pool needs at least K steps. The path
P_t={K-t,3K,4K,6K,8K+t,10K},t0..K,is legal and reaches the displayed
goal pool in K steps,so the bound is exact. Even K makes ALL initial
pool tokens even while preserving the obstruction:minority parity
is not the invariant explanation. One equal-gap exchange of length K
still repairs it;no claim against unrestricted exchanges. This answers
the intended adversarial test and pushes me away from more local
repair modules. After two related local countercontrols,a loop reflection
is warranted now rather than manufacturing a third module. The new
pull is toward global slack and a reservoir present before rounding;
MI313 states that separate question. No experiment or constant-distance
claim survived this guard;the original six-token repair remains valid.


### MI313 — B150 global alternative: arbitrary prescribed sums with quadratic slack (2026-10-17 17:07 BST)

**Candidate adaptation of known rounding mathematics;PROOF-SKETCH,
not independently read,novelty unknown and possibly routine. No experiment.**
Question:for fixed bin count,can strong SS margins guarantee a prescribed-
size/sum partition for every sufficiently large N,without equal target
sums or exactly linear size sequences? This is a tractable interior
question,NOT the full minimum-size3 conjecture or a finite L8 result.
Pull:build a broadly usable reserve first,instead of repeatedly repairing
special local obstructions. The fractional ingredients are known and
filed as PRIOR-ART with their proof,not new PROOFS entries.

Record searched:`minority.parity|parity.*repair|neutral.*pool|central.*compatib`
AND `SS3|MI311|six.token|four.bin`:5 hits/2 files.
`uniform.*fraction|fraction.*floor|strong.slack|robust.*round|dense.*reservoir`
AND `SS3|partition|Hoory|bin|mixing`:3 unrelated hits/3 files.
`asymptot.*prescrib|unequal.*round|uniform.*mix|positive.*floor`
AND `sum|bin|slack|partition`:11 hits/8 files,no relevant earlier version.
Bounded web queries:partition consecutive integers prescribed sizes
 different sums strong slack randomized rounding;partition prescribed
 sums cardinalities fractional;2605.06071 generalized sums strong slack.
No direct arbitrary-target version found;this is NOT FOUND,not novelty.
Primary orientation:Hoory-Kotlar2605.06071v2 section3 and Claims4.11-13
and their proofs,plus section5. The broad randomized-rounding strategy
is theirs/standard;the present all-token mixing and conservative resource
account below are an adaptation,not a discovery claim.

**Precise proposed statement.** Fix k>=2 and epsilon>0. For all
sufficiently large N,let positive integer c_i sum to N,and integer s_i
sum to L(N). For EVERY nonempty proper bin subset J,assume

    L(C_J)+epsilon*N^2 <= s_J <= U_N(C_J)-epsilon*N^2.

Then0..N-1 admits a partition into sizes c_i and sums s_i. There is
no assumption that all s_i are equal,or that c_i/N is constant across N.
A sufficient N is specified by the inequalities below. This is uniform
over targets satisfying these strong margins,not over all SS targets.

**1. A positive fractional floor.** The known support-function and
mixing argument attached in PRIOR-ART supplies an exact fractional
assignment x_(v,i)>=rho,where rho=8epsilon^2. Strong margins force
epsilon<=1/8 and c_i/N>=2epsilon;these are consequences,not extra
unstated assumptions. This step invokes no integral partition with
requested sums,only a convex combination with those expected sums.

**2. Independent rounding keeps many oriented pairs.** Color each
v in0..N-1 independently,with probabilities x_(v,i). Set

    rho=8epsilon^2; eta=rho^2/16;
    tau=rho^2/[1024*k*(k+1)]; D=floor(N/4), N>=8.

Hoeffding's inequality bounds the probability that ANY bin has count
error>tau*N OR sum error>tau*N^2 by4k*exp(-2tau^2*N).
For the latter,apply it to independent terms (v/N)*1_{color i},each
with range at most1;its expectation is s_i/N. Bin count expectation
is exactly c_i.

For each ordered distinct i,j and integer1<=d<=D,choose the disjoint
pairs(v,v+d) with v mod(2d)<d. There are at least (N-d)/2>=N/4
such pairs. Their events color(v+d)=i,color(v)=j are independent,
with individual probability>=rho^2. Chernoff gives failure probability
at most exp(-rho^2*N/32) for fewer than rho^2*N/8 such pairs.
The full oriented-pair count R_(i,j,d) is at least this matching count.
A union bound over ALL ordered pairs/gaps yields a simultaneous good
event with failure probability at most

    F(N)=4k*exp(-2tau^2*N)+k^2*N*exp(-rho^2*N/32).

No independence between these different good events is assumed.
For all sufficiently large N,F(N)<1,so such a coloring exists.

**3. Correct cardinalities without exhausting pairs.** Move any token
from an oversized bin to an undersized bin until all counts equal c_i.
At most T<=k*tau*N tokens move (the sharper half-L1 bound is unused).
Each move changes a bin sum by at most N,so afterward

    max_i |current_sum_i-s_i| <= Z=(k+1)*tau*N^2.

For any FIXED i,j,d,recoloring one token can destroy at most two
oriented pairs:it participates only as the lower or upper endpoint.
Consequently all pair counts are still at least

    rho^2*N/8 - 2k*tau*N >= rho^2*N/16 = eta*N.

We count destroyed pairs only;new pairs are not needed in this bound.

**4. Correct arbitrary individual sums.** Write e_i=current_sum_i-s_i.
They are integers totaling0. While nonzero,choose e_i>0,e_j<0 and

    d=min(D,e_i,-e_j).

Use a remaining pair with upper token in i,lower in j,separated by d,
and swap. Cardinalities stay correct;e_i decreases by d,e_j increases
by d,neither crosses0,and other errors are unchanged. Let M be total
positive error;initially M<=kZ/2. Steps with d=D number at most M/D;
every other step zeros a bin,which is never used again,so fewer than
k further steps occur. Because D>=N/8,total swaps S obey

    S <= 4k*(k+1)*tau*N+k <= eta*N/8

whenever N>=16k/eta:the first term is eta*N/16,and k is at most
eta*N/16. Every swap recolors two tokens and destroys at most FOUR
pairs for any fixed i,j,d. Thus even the whole planned correction
would leave at least eta*N-4S>=eta*N/2 pairs of every required type.
The same step bound holds for EVERY finite prefix,even one ending
in a putative stuck state. Its pair counts are still positive,a
contradiction. Positive integer error mass decreases at each step,
so the algorithm terminates with all errors zero.
This proves the candidate conditional on the standard concentration
bounds and the elementary fractional argument;no equal-sum identity
was used beyond total conservation. The statement follows for any
N>=max(8,16k/eta) with F(N)<1,and hence eventually uniformly.

**Scope,controls and niggle sweep.** The fixed-size3 sparse boundary
cannot satisfy epsilon*N^2 margins for arbitrarily large N,so this
does NOT solve SS3's difficult small-bin regime. A zero-slack extreme
forces some fractional assignments to0,so the positive floor is not
asserted there. k can be arbitrary but is fixed in the asymptotic;
none of the constants is uniform in growing k. Counts are corrected
BEFORE sums;the two depletion budgets are both subtracted. Matching
events use disjoint tokens;the other events need only a union bound.
The sum correction is justified from a deliberately rich starting
coloring,not from the refuted universal monotone-swap assertion MI301.
Integer d>=1 and no overshoot are essential;zeroed bins stay unused.
Unexpected check:strong singleton margins themselves imply linear bin
sizes,so the apparently mild margin condition excludes the sparse
hard cases rather than silently solving them. No probability sampling,
runtime estimate or finite certificate was run;N bounds are conservative.

**Verdicts,next and mentoring.** Gut:the global resource accounting is
more engaging than another small repair;there is some relief at a
route where the deficit and repair supply can be compared explicitly.
Reasoned:a complete hand adaptation candidate in a strong interior
regime,likely close to standard consequences of the source. It is not
adopted as a new theorem. Before creating a carrying-review job or
formal proof entry,ask Cloud whether this arbitrary-target/uniform
form is already covered or worth isolating,and independently audit
its depletion/rounding argument. A pending perspective reply does not
halt that audit. If it is a known corollary,file it entirely as prior
art and move on;do not manufacture novelty or a finite SS3 claim.
Research13min ACTIVE;MI295/305 reads pending,SS3/E28/L8 OPEN.


### MI314 — B151 audit and one exact small bin with a robust bulk remainder (2026-10-17 17:18 BST)

**Hand self-audit and COMPOSITE PROOF-SKETCH;no experiment,no independent
verification,novelty unknown.** B151's job was to break MI313's depletion
or quantifier argument before extending it. Record searched:`MI313|depletion|cardinality.*correct|count.*correction`
AND `round|reservoir|slack`:12 hits/8 files;MI313 and its known fractional
argument relevant,no previous audit. Primary source scope is now recorded
in PRIOR-ART. The broad rounding strategy is known. The source's stated
integral theorem has equal sums/fixed ratios;its general fractional lemma
and repair method make MI313 a close adaptation,not a new method.

**Audit result,no status upgrade.** Re-derived the deterministic budget
without probability:after count correction,if max error is Z and ALL
ordered gap counts1..D exceed R,any finite sum-correction prefix uses
at most kZ/(2D)+k swaps. The total positive error is the potential;
a full-D swap spends D,and a smaller swap permanently zeros a bin.
Each swap destroys at most4 pairs of any fixed type. Therefore a
stuck prefix is impossible when R>4[kZ/(2D)+k]. The argument does
not assume successful completion. With MI313's constants,count repair
leaves eta*N pairs and the entire prefix budget spends at most eta*N/2.
The earlier count-repair destruction is separately charged,not omitted.
Matching edges use distinct tokens;union bounds do not condition on
count success. Unequal targets use e_i=current_sum_i-s_i,not raw sums.
No gap found in these self-checks;this is NOT a second-party read.

**What the audit suggests.** Requiring a linear reserve involving a
size3 bin cannot work:for a fixed ordered pair/gap,its count is at
most that bin's cardinality. But a size3 bin can be set exactly FIRST.
The actual remaining question is whether three deleted tokens destroy
the bulk argument. They do not at its quadratic margin scale,as the
following bounded hand extension shows.

**Precise corollary candidate.** Fix epsilon>0. For all sufficiently
large N,consider four bin sizes(3,c_1,c_2,c_3) totaling N and integer
targets(a,s_1,s_2,s_3) totaling L(N). Assume

    3<=a<=3N-6,
    L(C_J)+epsilon*N^2<=s_J<=U_N(C_J)-epsilon*N^2

for EVERY proper nonempty subset J of the THREE bulk bins. Then a
partition exists. In fact ANY triple A of sum a can be fixed first;
the remaining tokens can meet the bulk targets. The global cut isolating
A is NOT required to have quadratic slack. This is conditional on the
same standard concentration/rounding ingredients as MI313,with the
changed constants below. It does not require MI295 or the boundary-pool
candidates. It does not solve cases with several unresolved small bins.

**Delete the triple and retain real capacities.** Known interval subset
sums give a size3 A of sum a. Let V=0..N-1 minus A,M=N-3,and W=sum V.
Its ordered values obey j<=v_j<=j+3 (zero-based ranks). Therefore the
minimum/maximum sums of C tokens differ from the corresponding full-
interval capacities by at most3N. For N>=6/epsilon,the actual V-based
lower and upper margins of every proper bulk subset are at least
epsilon*N^2/2. These are capacities of V,not a fictional relabeled
consecutive interval with unchanged target sums.

**Positive fractional floor on the punctured pool.** The support-function
proof in PRIOR-ART works for ANY ordered token set:replace U_N(C) by
the sum of V's largest C values. Uniform-by-size allocation on V has
mean target mu_i=c_i*W/M. Its upper-capacity gap for any subset is at
most N^2. Mix with weight lambda=epsilon/4 after expanding targets away
from mu as in MI313. The adjusted margin is at least
 epsilon*N^2/2-lambda*N^2=epsilon*N^2/4>0.
Feasible hypotheses also imply epsilon<=1/8,so lambda<1.
Original singleton margins imply c_i(N-c_i)>=2epsilon*N^2,hence
c_i/M>=2epsilon. Thus a conservative common probability floor is

    rho=epsilon^2/4.

No requested integral bulk partition is assumed in the fractional step.

**Holes cost only three matching edges.** For each1<=d<=D=floor(N/4),
MI313's disjoint matching has at least N/4 edges. Deleting three vertices
kills at most THREE edges of that matching,not three edges per surviving
token. For N>=24,at least N/8 edges remain. Independent rounding on V
therefore gives,simultaneously,initial gap counts>=rho^2*N/16 and
count errors<=tau*N,sum errors<=tau*N^2,except with probability at most

    F(N)=12exp(-2tau^2*N)+9N exp(-rho^2*N/64),
    eta=rho^2/32, tau=rho^2/[2048*3*4].

There are M<=N independent summands;normalizing token values by N
justifies the SAME conservative Hoeffding scale. No independence across
different gaps or across the good events is needed.

The count correction moves at most3tau*N tokens,leaving at least
eta*N pairs of every required type and max sum error Z<=4tau*N^2.
With D>=N/8,the sum-correction prefix uses at most48tau*N+3 swaps.
Here48tau=eta/16. When N>=48/eta,this is at most eta*N/8;its
pair destruction is at most eta*N/2. Thus the same non-stuck-prefix
argument completes the bulk,without ever recoloring a token in A.
A sufficient domain is N>=max(24,6/epsilon,48/eta) and F(N)<1.
F(N) tends to0,uniformly in the actual triple and bulk targets.
This is forall A,exists a bulk completion;it does NOT assert one
random coloring simultaneously completes all choices of A.

**Controls and practical scope.** The condition is nonvacuous:take
N=3m+3,three bulk sizes m,and bulk targets as equal as their total
L(N)-a permits. Uniformly for3<=a<=3N-6,every displayed bulk margin
is N^2/9+O(N),so any fixed epsilon<1/9 eventually applies. This
includes a fixed size3 bin whose sum is at its global minimum or
maximum,unlike MI313's all-subsets strong-margin statement. The resulting
N threshold is deliberately very large;no practical finite bound or
new finite certificate is asserted. This is still an interior bulk
result,not arbitrary four-bin SS3.

Niggle sweep:removed labels are not compressed;their original values
and W are preserved. The fractional support argument uses V's real
capacities. Fixed A tokens never enter the reservoir. Three deleted
vertices destroy only three DISJOINT matching edges. All probability
and depletion estimates use N consistently although only N-3 values
are rounded. Constants are recomputed for the halved matching supply,
not copied unchanged. The final error vector still totals0. The audit
and corollary are same-worker hand reasoning only,not verified results.

Gut:the interesting pull is now at exact small-core selection followed
by a robust remainder,not at optimizing this very conservative bound.
Reasoned:known-method adaptation with a clearer bridge to a small bin;
source coverage and independent verification remain unresolved. Next
question:can two small bins be fixed compatibly before rounding the
bulk,without merely assuming their joint completion? MI295 would give
one provisional route,but its carrying read is pending and should not
be hidden. First examine that precise selection gap;no automatic new
experiment,constant optimization or extra proof-review queue. Cloud's
existing source-coverage question gets this useful continuation.
Research13min ACTIVE;full SS3/E28/L8 remain OPEN.


### MI315 — B152: direct compatible selection of two prescribed triples (2026-10-17 17:33 BST)

**Hand PROOF-SKETCH,not independently verified;novelty unknown.**
For N>=15,two disjoint triples of0..N-1 with prescribed sums u,v
exist iff

    3<=u,v<=3N-6; 15<=u+v<=6N-21.

These are the individual/combined SS bounds. The result is a special
case of the unreviewed broader MI295,but this proof is independent
of that exchange argument. It directly supplies the small core needed
before bulk rounding. Record searched:two.triple|disjoint.triple|two.small.bin|MI295
AND SS3|sum|prescrib|compatible:37 hits/9 files. Follow-up on disjoint
representations/avoiding two holes:4 unrelated hits/3 files. Bounded
web queries:disjoint triples prescribed sums integers;triples prescribed
sums partition interval;partition sizes sums three consecutive integers.
No direct applicable theorem found;NOT FOUND,not novelty or absence.
Classical interval-sum background remains PRIOR-ART;no new source
result imported. Pull:use redundancy BEFORE forbidden-token choices,
not another overlapping-pair repair. No experiment yet.

**Disjoint representations that survive holes.** On0..M,M>=6,every
sum t in[8,3M-8] has TWO disjoint triple representations. At sums8,9,10
use respectively

    (0,2,6)/(1,3,4);
    (0,4,5)/(1,2,6);
    (0,4,6)/(2,3,5).

Translate all values by h=0..M-6. These give consecutive blocks of
three target sums8+3h..10+3h,covering the claimed interval.
Deleting ANY one token leaves at least one representation.

On0..M,M>=8,every t in[12,3M-12] has THREE disjoint representations.
For t12,13,14 use

    (0,4,8)/(1,5,6)/(2,3,7);
    (0,4,9)/(1,5,7)/(2,3,8);
    (0,5,9)/(1,6,7)/(2,4,8).

For M>=9,translate by h=0..M-9 to cover12..3M-13;reflect the
sum12 template in M to obtain the final sum3M-12. At M8 only t12
is required and its template works. Deleting ANY two tokens leaves
at least one representation. All displayed triples are pairwise
disjoint WITHIN a row;different target rows need not be disjoint.
These finite templates are elementary supporting constructions,
not separate PROOFS entries or review requests.

**Normalize.** Order u<=v. If u+v>3(N-1),reflect ALL tokens x->N-1-x
and exchange bin labels. The new ordered sums are
(3(N-1)-v,3(N-1)-u),with sum<=3(N-1). All bounds persist,including
combined lower15 because the original combined upper is6N-21.
Thus assume u<=v and15<=u+v<=3N-3.

**Main case u<=N,v>=14.** Choose A={0,1,u-1}.
If v<=3N-11,shift the available interval2..N-1 down by2. It is
0..N-3 with just u-3 forbidden. Its requested sum v-6 lies in
[8,3(N-3)-8]. The two-representation construction gives a surviving
triple B,shifted back,disjoint from A and of sum v.
If v>3N-11,the normalization forces u<=7. Write
j=3N-6-v in{0,1,2,3,4};choose
B={N-3-j,N-2,N-1}. Its smallest value is at least N-7>=8,
whereas max A<=6,so disjointness and the sum are explicit.

**Main case u>N.** Choose A={0,p,q},where for odd u use
p=(u-1)/2,q=(u+1)/2;for even u use p=u/2-1,q=u/2+1.
Since u<=3(N-1)/2 and N>=15,these are distinct valid positive
values below N. Shift1..N-1 down by1;it is0..N-2 with two holes
p-1,q-1. The requested sum v-3 lies in[12,3(N-2)-12]:indeed
v>=u>=N+1>=16 and v<=2N-4<=3N-15. The three-representation
construction yields B avoiding both holes;shift back. No disjointness
is assumed from separate feasibility.

**All small exceptions,v<=13.** The normalized bounds force8<=v<=13.
For v9..13 take A={0,1,u-1} and the following default B,with overrides:

| v | default B | overrides for u |
|---|---|---|
|9|2,3,4|none|
|10|2,3,5|u6: A=0,2,4; B=1,3,6|
|11|2,3,6|u4 or7: B=2,4,5|
|12|2,4,6|u3: B=3,4,5; u5 or7: B=2,3,7|
|13|2,4,7|u3: B=3,4,6; u5 or8: B=2,3,8|

At v8 only u7/8 are possible:use A={0,2,5} or{0,2,6}
respectively,and B={1,3,4}. This covers every integer
max(3,15-v)<=u<=v. Each row has explicit correct sums and disjoint
tokens in0..N-1;no search is hidden in a table instruction. Reflection
and the initial label permutation restore all original target pairs.

**Unexpected check:small ambient intervals really can fail.** At N7,
(u,v)=(4,14) passes the displayed SS bounds. But sum4 forces
A={0,1,3},and sum14 forces B={3,5,6};they overlap. Thus no disjoint
triples exist. This does not refute the N>=15 statement. Nor is15
claimed sharp;the remaining N8..14 cases are not asserted here.

**Bridge to the live target.** For four bins(3,3,c,d),select these two
triples first. If both bulk singleton targets have quadratic SS margins,
removing six tokens costs at most6N in real capacities and six edges
of a disjoint gap matching. MI314's robust-bulk argument then applies
with TWO bulk bins,N>=12/epsilon and N>=48 for these two preliminary
bounds;its floor/depletion constants are recomputed with k=2. This is
a COMPOSITE asymptotic corollary candidate,not a finite SS3 proof or
an assumption that MI295 has been reviewed. The selected small core
is now supplied explicitly instead of assumed.

Gut:the pull is warmer at disjoint representation choices absorbing
holes;this is a concrete way to prevent overlap rather than repair it
afterward. Reasoned:a short independent special-case candidate that
serves the small-core bridge,not a new general three-bin theorem.
Next one fixed independent formula/full-feasibility audit,registered
in MI316 before any run. No new carrying-review queue;Cloud receives
this as a useful shorter special-case continuation of existing work.
Niggle sweep:reflected bin labels exchange;endpoint14 belongs to the
main case;two forbidden values are distinct;the final three-representation
endpoint needs reflection;v8 and u6/v10 change A itself;all other small
cases change only B. No interval relabeling preserves sums without
explicitly shifting the requested sum. SS3/E28/L8 remain OPEN.


### MI316 — B152 preregistration: two-triple formula versus full feasible-pair maps (2026-10-17 17:33 BST)

**NOT RUN.** Source tests/probes/instinct/ss3_two_triples_audit.py.
ONE invocation only after source/prediction push. Predict every
SS-admitted ordered pair u<=v at N15..24 has a literal disjoint-triple
certificate from MI315's recipe,including reflection and every branch.
Separately,N15..18 enumerate ALL six-subsets and their ten unordered
triple splits,using no recipe/SS/palettes/reflection formulas. Predict
those full feasibility maps equal exactly the independent SS target
sets. This is an independent exact oracle,not a replay of the recipe.

Check every two/three-representation palette at M6/8..30 and all
claimed sums:1757 palette questions,all within-range/sum/disjointness
checks should pass. Retain N7(4,14) as SS-admitted but oracle-negative;
N6(3,12) oracle-positive,and a signed translation by-17 of a literal
N15 witness. Counterfactual:calling SS sufficient at N7 would fail
this negative control;calling separately feasible triples disjoint
would also fail. The three-representation endpoint and the small-case
A overrides are explicit adversarial checks. Record/literature search
is MI315's;no earlier direct audit found.

Stop at first assertion or15CPU/25wall/128MiB peakRSS(macOS bytes),
1M reference splits/50000 recipe calls/2MiB raw;30wall external watchdog.
Exactly439610 independent split visits are predicted,including controls.
No repair/retry/cap rise/domain extension. Save raw/stdout/stderr outside
git,do not upload. Finite pass remains COMPUTED same-worker evidence;
MI315/its asymptotic application stay SKETCH until independently read.
No new larger SS3 census or routine review halt,research13min ACTIVE.


### MI317 — B152 evidence changes the plan: carrying reads adopted;redundant audit CANCELLED (2026-10-17 17:36 BST)

**No experiment run;MI316 CANCELLED before execution.** The source and
predictions were committed as bffc780d,but the publication push was
rejected because Cloud had landed5ef12b10. One fetch/merge brought
CL434,read in full along with both checker sources,and its exact commit
was verified before portal ACK. Both workers' text is preserved.
No force push,source execution,raw report or machine pass occurred.
Source header now records cancellation;the alternate MI315 construction
is retained as an unreviewed proof,not separately promoted.

**Adopted mathematics.** Cloud independently verified MI295's whole
three-bin arbitrary-sum theorem for sizes>=2,including the <=4 adjacent-
value-swap nonincreasing descent and its carrying word classification.
It also reports1093704 start-state checks at n<=9,with depths
1048422/44532/666/84:the bound4 is attained. That computation is
Cloud's,not a GPT replay. MI295 is now PROVED in scope. Consequently
MI315's EXISTENCE STATEMENT for N>=15 is already proved as its
(3,3,N-6) case;there is no reason to create another audit or review
job for that known consequence. The alternate palette proof itself
has not received an independent read.

Cloud also independently verified MI305's general prefix/window
lemma AND reflected four-bin consequence,including the concave joins
and integer touching. Its216-pool/962-spectrum replication agrees.
MI305 is now PROVED in scope. MI308's beyond-square extension and
MI313/314's rounding adaptations remain SKETCH;reviewing dependencies
does not certify those later arguments automatically. Novelty of the
verified arbitrary-sum/exchange result remains unassessed. No prize won.

**Known consequence filed as such.** The two-triple existence result
is now a corollary of PROVED MI295,not a new proof entry. Its role is
still useful:the small core in the (3,3,c,d) robust-bulk adaptation need
not be assumed. The bulk rounding argument itself remains single-party,
and Cloud explicitly has NOT read the source paper;its source-coverage
question is not answered by guessing. Preserve those status boundaries.

**Mentoring proposal and a scope correction.** CL434 suggests measuring
four-bin descent lengths under adjacent swaps,arbitrary single swaps,
and two-for-two exchanges before designing more modules. I agree with
the experimental direction. But sizes>=3,n<=12 permits only n=12
with sizes3^4,so that domain cannot measure growth with n. Also a
bounded maximum on a finite domain cannot establish a uniform bound
or imply a finite relay classification;finite growth alone cannot
prove an infinite obstruction either. Use the measurement to choose
what to investigate,not as a theorem deciding global versus local.

A feasible FIRST design question is the complete E=2 slice at n12,
with canonical target-label reduction and reverse distance from E0
within E<=2. This includes all nonincreasing paths from unit-error
states and the MI301 trap,while avoiding the much larger product of
ALL target vectors and369600 labeled start partitions. No numerical
result,registration or compute authorization for a larger census is
claimed here. Before running,fix the move sets,independent controls,
exact coverage enumeration,resource caps and what the diagnostic can
actually falsify. Larger n would need a separately bounded design.
No more boundary/local repair modules are being opened.

Gut:delight at two independent carrying reads,then relief at cancelling
work that just became redundant. The pull is toward the proposed
mechanism diagnostic,with unease about its initial scope and overstrong
interpretation. Reasoned:two tools have advanced to PROVED;the new
measurement needs careful design,not an immediate large run. Next
work is that preregistration/design,without waiting on routine review.
Research13min ACTIVE;SS3/E28/L8 remain OPEN.


### MI318 — B153 preregistration: COMPLETE n12 unit-error descent diagnostic (2026-10-17 17:44 BST)

**Question.** For n12,four labelled bins of three tokens,ALL SS-feasible
integer targets,and every start with L1 error E=2,what is the exact
shortest nonincreasing descent under each fixed move set? This measures
a mechanism's finite scope;it does not decide SS3 or a uniform depth
bound. Pull:toward finding the shape of an obstruction rather than
generating another repair. Unease:the full all-target/all-start product
would be an oversized and easily misinterpreted first experiment.

Record searched:`descent.*diagnos|unit.error|reverse.*distance|MI301|CL434`
and`four.bin|SS3|E.?2|move` via record_find.py,18 hits/4 files;MI301,
CL434 and MI317 relevant. Primary-source orientation remains the
already-read Hoory-Kotlar arbitrary-sum/open-threshold discussion;this
is a finite move-graph diagnostic,not a new literature or novelty claim.
No new flags at the current private-store poll;shared main merged.

**Exact coverage.** Enumerate ALL369600 labelled token-owner words
with counts3^4. Enumerate every SORTED SS target t,total66,via the
all-subset inequalities. Retain every word with sum-vector t or
t+e_a-e_b,a!=b. Sorted targets remove only bin-label duplication:
ALL word assignments remain,including every assignment within tied
target classes. Thus every labelled-target/start pair is represented
up to a simultaneous bin permutation. Report canonical-domain counts
AND full labelled-target counts,weighting each target by
24/product(multiplicity!). Independently enumerate ordered disjoint
triple masks and sum-vector multiplicities,and derive ALL per-target
E0/E2 coverage counts in the opposite direction. No assumed feasibility:
zero-goal targets are retained and reported,not silently discarded.

**Why the distance is exact.** Error is even and nonnegative because
target/current totals coincide. A nonincreasing path starting at E2
stays at E2 until its first E0 state. All fixed moves are reversible.
Multi-source reverse BFS from ALL E0 words inside E<=2 therefore gives
the exact shortest descent distance;unreached E2 words have no such
path. Traversing outward from E0 is a reverse-search operation,not an
allowed forward increase. No higher-error descent is measured.

Move0 swaps tokens with adjacent VALUES only;move1 swaps any single
token for any other bin's token;move2 includes move1 PLUS every atomic
two-for-two exchange between two bins. Atomic means one edge,not two
intermediate single swaps;all other bins are unchanged. Distances
include neutral steps and the final improving edge. No multi-bin atomic
move or unrestricted energy excursion is allowed.

**Predictions/counterfactuals.** Predict exact coverage and all controls
agree. Predict nested distances d2<=d1<=d0 with infinity allowed.
Tentatively predict every E2 word reaches E0 under move2;retain any
negative result as the main finding rather than asserting this forecast
as an instrument condition. MI301 must remain unreachable under move1
and become reachable under move2;no numerical maximum forecast or
infinite-theorem inference. Counterfactual:existence need not imply
monotone single-swap reachability;MI301 catches that error. Omitting
equal-target labels/unreached nodes/SS targets must break coverage.

**Independent/unexpected controls.** Separate Python ordered-mask
enumerator versus C++ recursive owner words,whole per-target coverage
map equality. Independent Python literal mask-exchange BFS compares
EVERY distance in all three modes on targets(7,10,23,26) and
(16,16,17,17),including unreachable states/goals. Check every reported
per-target longest finite path by literal token counts,all bin sums
and allowed move size. Unexpected:compare EVERY node's three exact
distances with its reflected-value/bin-reversed image across the
complete domain,not just total histograms. MI301 label sorting uses
B,D,A,C explicitly. These are same-worker controls,not a carrying read.

**One execution after this source/preregistration push.** Source
tests/probes/instinct/ss3_unit_descent.cpp plus independent wrapper
ss3_unit_descent.py. Compile to a temporary binary only after push,
then ONE wrapper invocation;raw outputs outside git,no upload. Caps:
60 aggregate CPU seconds checked at budget boundaries,90wall,
256MiB peakRSS per process(macOS bytes),2M engine nodes,200M
generated engine moves,8MiB raw;engine55wall/internal60CPU hard cap,
wrapper60CPU hard cap,100wall external watchdog. Compilation separately
capped30wall. Stop first instrument error/cap,retain partial evidence,
no fix/retry/cap rise/automatic n13 or all-error extension. A passing
finite diagnostic remains COMPUTED;no PROOFS entry or routine review
request. Next inference depends on the measured traps/distances.


### MI319 — B153 outcome: complete unit-error slice;only the known trap;two-for-two releases all (2026-10-17 17:47 BST)

**COMPUTED,same-worker independent controls;not an infinite theorem.**
ONE registered invocation after source/preregistration a6a325f1.
Compilation succeeded,with two warnings:Clang accepts lambda captures
of structured bindings as a C++20 extension under the registered
C++17 invocation. They are retained in the compile log;no repair,
recompile or rerun. Python executable AST unchanged except this source
header's OUTCOME. No cap hit,failed assertion,retry or extension.

**Coverage.** All369600 labelled partitions of0..11 into3^4 enumerated.
Exactly630 sorted SS targets;19344 E0 words plus235054 E2 starts,
254398 graph nodes. Independent ordered-triple-mask enumeration and
sum-vector multiplicities reproduce EVERY target's E0/E2 counts.
No target has zero goals. Weighting by distinct target permutations
gives4386456 labelled-target/E2-start pairs and369600 goals,as it
should:every labelled partition supplies exactly one labelled goal
target. All target ties retained. This independently recovers the
known-positive finite SS3 instance;the new interest is move geometry.

| Move set | Canonical E2 starts | Unreachable | Maximum finite distance | Full labelled-target unreachable |
|---|---:|---:|---:|---:|
| Adjacent-value single swap | 235054 | 4 | 7 | 96 of4386456 |
| Any single swap | 235054 | 4 | 6 | 96 of4386456 |
| Any single plus atomic2for2 | 235054 | 0 | 5 | 0 of4386456 |

The four unreachable states occur ONLY at sorted target(7,10,23,26)
and are EXACTLY MI301's component after label sorting. Artifact audit
compared the whole four-word set with START and the independent4/5,
6/7 swaps;no new single-swap trap in this domain. MI301 START distances
are(infinity,infinity,2). Thus two-for-two is REQUIRED for only that
known component here,but it also shortens some reachable paths.
The canonical-domain failure fraction differs from the correctly
weighted labelled-target fraction;do not conflate their measures.

**Complete distance histograms,canonical targets.** Depth:count:
- Adjacent:-1:4,1:146438,2:72964,3:13740,4:1668,5:208,6:30,7:2.
- Single:-1:4,1:146438,2:75097,3:12487,4:957,5:69,6:2.
- Single+2for2:1:189962,2:43491,3:1585,4:14,5:2.
Here -1 means unreachable,never a negative length. Full weighted
histograms are retained in the local report.

**Controls.** Independent Python mask-exchange BFS agrees on WHOLE
three-distance maps for115 nodes at MI301's target and1724 at
central(16,16,17,17),including unreachable nodes and goals. Engine
compares all254398 nodes' three distances against value reflection
plus bin reversal,with exact node correspondence. All1890 reported
per-target/mode maximal finite paths pass independent literal bin
counts/sums/move-size/error-trace checks. Nested distances hold
pointwise.43837030 generated engine moves including path extraction.
These are same-worker controls,not Cloud's independent carrying read.

**What actually forces the maximum?** Only two E2 nodes need five
moves under the largest move set,and their targets are reflected:
(4,14,23,25) and(8,10,19,29). First representative:
A={0,1,4},B={3,5,6},C={2,10,11},D={7,8,9};
current sums(5,14,23,24),target(4,14,23,25). A retained shortest path:
1. C10 exchanges D9;deviations(+1,0,-1,0).
2. B{5,6} exchanges C{2,9};deviations unchanged.
3. C{5,11} exchanges D{7,10};deviations(+1,0,0,-1).
4. B9 exchanges D8;deviations(+1,-1,0,0).
5. A4 exchanges B3;all deviations zero.
Every intermediate error is2;the final error is0. Four moves do not
suffice in the complete registered graph. This lower bound is
computational;no hand classification or universal5 bound asserted.
The second representative is a reflected state;the engine's chosen
shortest path need not be the reflection of this particular path.

**Cost and provenance.** Engine1.291269CPU seconds,wrapper1.698695CPU,
wall3.237953s,peak child RSS17985536B. Local raw engine226538bytes,
SHA256 bbbd6ebe7e22446af1a9fbcb6b3633a856cf1ba17af8567ae186511f2d286492.
Local report1746bytes,
SHA256 1c7a9a3043522bbe8a48b9c696a8a84e721c9021a4c6142a4dabd111301fc5b6.
stdout/stderr/compile logs retained outside git;no upload. Source in
tests/probes/instinct/ss3_unit_descent.{cpp,py};raw report identity
precedes any interpretation below. No unregistered additional graph
was searched during artifact inspection.

**Interpretation and next cheap question.** The positive forecast
passes in this COMPLETE finite slice. It supports studying atomic
exchanges;it proves nothing about larger n,unequal sizes,higher
errors,uniform move bounds or general SS3. The rare required-large-
move trap was already known;do not count its rediscovery as novelty.
The fresh information is its isolation in this domain and the exact
remaining depth geometry. Next inspect by hand why the five-move
representative cannot descend more quickly,and whether its obstruction
is a useful representation rather than another local module. No
automatic new census,cap rise,proof queue or review halt.

Gut:delight at a small complete answer and a cleanly isolated known
trap;surprise that adding atomic exchanges still leaves a five-step
route. Fresh-choice pull is toward the two exceptional states,not
maintaining a warm label by habit. Reasoned:one bounded diagnostic
answered the registered question;its interpretation must stay finite.
Niggle sweep:canonical weighting/ties,goals as reverse roots,unreached
nodes,atomic versus sequential moves and reflected target labels all
checked explicitly. Instrument warnings disclosed;no theorem status
upgraded. SS3/E28/L8 remain OPEN;13min research ACTIVE.


### MI320 — B154 hand explanation of the five-move extremal: supplier obstruction (2026-10-17 17:56 BST)

**Hand argument,not independently reviewed;finite statement already
COMPUTED in MI319.** Question:why does the first extremal require five
nonincreasing moves even with atomic2for2 available? The pull warms
at an explanation in terms of who must supply which token,not at
extending the census. No new experiment,proof queue or global bound.
Record searched:`five.move|extremal|punctured|hole.*transport` AND
`SS3|MI319|MI295`:5 hits/2 files,MI319 and MI303 relevant. MI295's
full consecutive-pool hypothesis reread;do not freeze a bin then
apply that theorem to the punctured remainder.

Write bins in A,B,C,D order,target(4,14,23,25),initial state
I=(014;356;2,10,11;789),deviations(+1,0,0,-1). Here014 denotes
the SET{0,1,4},not a decimal value. Let S swap A4/B3 and R swap
C10/D9. Direct examination below proves these are the only legal
first moves. They commute. After two steps without an immediate
backtrack,the possibilities are exactly:

| Name | A | B | C | D | Deviations |
|---|---|---|---|---|---|
| N=SR=RS | 013 | 456 | 2,9,11 | 7,8,10 | 0,+1,-1,0 |
| T=R then A4/C2 | 012 | 356 | 4,9,11 | 7,8,10 | -1,0,+1,0 |
| U=R then B3/C2 | 014 | 256 | 3,9,11 | 7,8,10 | +1,-1,0,0 |
| V=R then B{5,6}/C{2,9} | 014 | 2,3,9 | 5,6,11 | 7,8,10 | +1,0,-1,0 |

**Complete first-two-step examination.** For an ordered pair of bins,
let tau be the loss in the first bin's sum. With unit total error,
allowed integer transfers are tau=0,1 for deviation pairs(+1,0)
or(0,-1);tau=0,1,2 for(+1,-1);tau=0 for(0,0). Reverse orientation
negates tau. These follow from the two absolute-value terms and
include energy-neutral overshoot tau2,which must not be omitted.
Single-transfer possibilities are token differences;2for2 possibilities
are differences of the two bins' pair-sum sets.

At I,the pair-sum sets of A,B,C,D respectively are
{1,4,5},{8,9,11},{12,13,21},{15,16,17}. No two have equal sums,
and none has an admissible directed difference1 or2 for its deviation
pair. The single swaps satisfying the same condition are exactly S,R.
After S,the pair-sum sets are
{1,3,4},{9,10,11},{12,13,21},{15,16,17};no legal2for2,and the
only legal singles are undo S and R. After R,the pair-sum sets are
{1,4,5},{8,9,11},{11,13,20},{15,17,18}. Only equality11 between
B,C is a legal2for2,namely V. The legal singles are undo R,S,
A4/C2 (tau2 between opposite defects),and B3/C2. Thus the table
is complete. All these states retain error2;no goal at depth1 or2.
An immediate backtrack cannot appear in a shortest path.

**There are exactly FIVE goal partitions.** A's target4 forces
A=013. The remaining B triple of sum14 is either248 or257:
without token2 the least available triple is456,sum15. Enumerating
the remaining C triple of sum23 gives all goals below,D its complement:

| Goal | A | B | C | D |
|---|---|---|---|---|
| 1 | 013 | 248 | 6,7,10 | 5,9,11 |
| 2 | 013 | 248 | 5,7,11 | 6,9,10 |
| 3 | 013 | 257 | 4,8,11 | 6,9,10 |
| 4 | 013 | 257 | 4,9,10 | 6,8,11 |
| 5 | 013 | 257 | 6,8,9 | 4,10,11 |

For B248,the remaining values are5,6,7,9,10,11;the only C choices
are(5,7,11),(6,7,10). For B257,the remaining values are
4,6,8,9,10,11;the choices are(4,8,11),(4,9,10),(6,8,9).
This is an exhaustive arithmetic list,not a sample of goals.

**Each depth2 branch needs at least THREE more two-bin moves.**
Unexpected adversarial check:drop the energy restriction entirely
for these last moves. The stronger lower bound still holds.

At N,A already equals every goal's A,while B,C,D must all change.
If only two moves remain,A cannot be touched once(it would finish
changed),or twice(then at most two other bins are touched). Thus
both moves are among B,C,D. One bin touched in the first move is
untouched in the second and must reach its goal after that first move.
But for EVERY one of the five goals,EACH of B,C,D needs foreign
tokens from BOTH of the other bins in its N state. For example,
B=248 needs2 from C and8 from D;B=257 needs2 from C and7 from D.
Each C goal contains a token from B and one from D;each D goal
contains a token from B and one from C,as the table shows. No first
move touching just two bins can finish either endpoint. Contradiction.

At each of T,U,V,ALL FOUR bins differ from every goal. Two remaining
moves would therefore have to use disjoint bin pairs,each bin touched
exactly once. In particular,A must reach013 in its sole move:
- T:A=012,so it must exchange2 for B3. Then B becomes256,
  neither permitted B goal248 nor257.
- U:A=014,so it must exchange4 for C3. Then C becomes4,9,11,
  sum24 rather than23.
- V:A=014,so it must exchange4 for B3. Then B becomes2,4,9,
  sum15 rather than14.
In every case the necessary partner is wrong after its only move.
The retained0,1 force a single-token exchange:atomic2for2 cannot
simultaneously keep both. Thus no branch finishes in two further
moves,even with arbitrary intermediate energy.

The first-two-step exhaustion plus these ownership arguments give
a HAND lower bound5 from I for the registered move set. MI319's
explicit five-move path gives the matching upper bound. Reflection
x->11-x,then reversing bin labels,yields the other extremal with
target(8,10,19,29). This is a finite explanation,not a uniform SS3
augmentation theorem or a new theorem filing. No carrying read
requested for an explanatory reproof of the computed small fixture.

**What this teaches,next question.** Neutral exchanges do more than
move a +/-1 defect:they change the set of available suppliers for a
future goal bin. Looking only at the directed unit-transfer path
forgets that dependency. The five-step obstruction is not another
energy barrier:after two carefully classified steps,it persists even
when later energy increases are permitted. A promising next hand
question is whether a target-independent supplier/last-touch argument
can guide global augmentation without enumerating local patterns.
It must choose an actual compatible goal or avoid assuming one;
this analysis is a LOWER bound because all five goals were known.
Do not smuggle the desired existence into a repair argument.

Gut:enjoyment at the compact reason,with relief that it is stronger
than reciting BFS layers. Fresh choice still favors this ownership
question;the finite fixture is now understood enough to leave alone.
Reasoned:a useful change of representation,not evidence of a general
five bound. No new experiment or routine review halt. Niggle sweep:
tau2 included;neutral equal-sum quad included;A's possible temporary
negative state T included;both endpoints of the first move considered;
all goals exhaustively listed;two disjoint moves cannot hide a third
supplier. Hand argument remains single-party;SS3/E28/L8 OPEN.


### MI321 — B155: signed carriers and the exact unit-neighbour question (2026-10-17 18:09 BST)

**Representation and conditional reduction,hand/source work;general
SS3 still OPEN.** The question was whether supplier structure can
help without assuming the target partition. Pull:turn the missing
unit into an explicit mobile object. Unease:ordinary fiber connectivity
is about already-existing endpoints and can hide the exact existence
question. No new experiment,solver setup,basis computation or review
queue. This is one block's connected change of representation,not
a fresh series of local repair lemmas.

Record searched:`Markov|Lawrence|toric|neutral.*fiber|fiber.*connect`
AND`partition|sum|SS3|bin`:82 hits/28 files,mostly unrelated. Refined
`Lawrence|toric|Graver.basis|Markov.basis` AND`SS3|partition|exchange`:
9 hits/3 files;MI302/PRIOR-ART already warns that Graver optimality
does not establish SS sufficiency or a2for2 bound. Then
`base.poly|submodular|M.convex|unit.error.*suff|error2.*suff|tight.set|unit.*target.*path`
AND`SS3|partition|target|prescribed`:one unrelated historical hit.
Read the primary sources and proof portions identified in PRIOR-ART's
two new notes. Known target-exchange proof is attached THERE as
"known,reproved here",not promoted as a new PROOFS entry.

**A cheap hand kill of the too-narrow picture.** Ordinary exact-sum
neutral connectivity under1/2-token two-bin exchanges is FALSE even
at n9,three bins of size3,each target12. Distinct partitions include
(048;156;237) and(057;138;246). In any pair of equal-sum disjoint
triples P,Q,a neutral1for1 requires equal token values,impossible.
A neutral2for2 would require

  sum(P)-p = sum(Q)-q, hence p=q,

where p,q are the omitted tokens,again impossible. Every such goal
is isolated under these EXACT-neutral moves. This does not refute
MI295 or unit-error augmentation:their paths visit neighbouring sum
vectors. It kills only the proposal that connectivity inside each
fixed exact-moment fiber using these moves supplies the mechanism.
Unexpected check:the simplest balanced triples already defeat that
proposal;large-bin complexity or a machine search is unnecessary.

**Exact signed-carrier encoding.** Keep physical assignment variables
X_ix in{0,1},one owner per real token x=0..N-1,and prescribed
physical row counts sum_x X_ix=c_i. Add two virtual columns a,b,
one owner each,with weights+1 and-1 and ZERO contribution to the
physical count. Fix the augmented row moment equations

  sum_x x X_ix + a_i - b_i = s_i,
  sum_i a_i=sum_i b_i=1; a_i,b_i in{0,1}.

Thus physical deviations d_i=q_i-s_i=b_i-a_i. If the two carriers
share a bin,all deviations vanish. If separated,b's bin has+1 and
a's has-1. Conversely EVERY physical E2 state has a UNIQUE lift
(b at its positive bin,a at its negative bin);every E0 partition has
k lifts,one for each common carrier location. There are NO other
physical states in this augmented fiber. It therefore represents
EXACTLY E<=2,without choosing or assuming a compatible goal.
Given any actual unit-error start,the augmented fiber is demonstrably
nonempty by putting its carriers in those forced bins.

In matrix form the base columns are(1,x) for physical tokens and
(0,1),(0,-1) for carriers. Its k-th higher Lawrence construction
fixes these row counts/moments and every column's total1. Nonnegative
integer entries automatically become binary because column totals
are1;no independent binary assumption is smuggled into connectivity.
This matches the known framework cited in PRIOR-ART. Its allowed
basis moves have NOT been identified with our two-bin1/2 exchanges.
Its fixed-base bounds also do not give an N-independent bound.

**What remains missing.** A separated-carrier state is explicit;
a coincident-carrier state is the desired partition. General Markov
connectivity connects endpoints IF they exist. It does not prove
there is any coincident-carrier state in this fiber. Accordingly
this is an exact model,not a proof from the word "connectivity".
No basis calculation is launched merely because the encoding exists.

**Why solving only unit errors really could suffice.** For SS3 take all c_i>=3;the target geometry itself only needs
positive sizes. For fixed sizes c_i,let B_c be ALL integer SS targets,total L(N). The familiar
base-polyhedron exchange argument in PRIOR-ART gives a path of
||x-y||_1/2 admissible unit transfers between ANY x,y in B_c.
For this model the submodular gap is the product of the sizes of
the two set differences. In particular,two incomparable tight sets
cannot coexist when all c_i>0;target cuts have especially simple
geometry. None of this asserts physical realizability.

Let R_c be the set of sum-vectors of ACTUAL partitions with sizes c.
It is nonempty:allocate consecutive blocks. Necessarily R_c is a
subset of B_c. The following purely existence-level statement is
therefore EQUIVALENT to SS3 for this fixed c:

  (UN) If x is in R_c and y=x-e_i+e_j is in B_c,
       then y is in R_c.

Proof of the nontrivial direction:start with the consecutive-block
partition and follow the admissible target path to ANY requested
s. At every step the preceding partition is an E2 start for the
next target. UN supplies a next partition. Finitely many steps
reach s. The reverse implication is immediate if R_c=B_c.
No partition of an unknown target was assumed in the induction.
This equivalence is an application of the known exchange geometry,
not an unconditional solution of UN or a novelty claim.

Our desired nonincreasing2for2 release theorem would imply UN,but
is an ADDITIONAL reachability assertion. A proof may instead construct
a completely different partition of the next target;it need not
repair the supplied start monotonically or in bounded depth. This
separates the statement we need from the experimental move restriction.
The n12 diagnostic was legitimately focused on the decisive error
level;it still supplies no universal UN theorem. For k4 the live
question is now:given one actual partition and one SS-admissible
unit target change,force a carrier collision OR construct a new
partition without presupposing its suppliers.

**Counterfactual/niggle checks.** Actual sum vectors and admissible
integer targets remain separate sets;calling their equality "M-convex"
would assume SS3. The exchange theorem applies to B_c only. Start
partition is supplied before induction;each later one comes only
from the explicitly OPEN UN hypothesis. Carriers affect sums but
not sizes;signs b=positive,a=negative checked. Coincident carriers
give k representations of one physical goal,not k distinct goals.
Neutral n9 countercontrol does not contradict a search that allows
E2 at intermediate states. No general2for2 or uniform depth inference.

Gut:surprise at the clean carrier picture and renewed pull toward
the sharper unit-neighbour statement. Reasoned:the model removes
an assumed goal;the known target-domain geometry explains why unit
release is enough,but the open existence step is intact. Next cheap
hand test is whether an extremal separated-carrier component forces
an SS-violating cut;look for an actual invariant or a countercontrol,
not a list of local repairs. No new experiment/review halt;13min
ACTIVE,older solver/local-module routes held,SS3/E28/L8 OPEN.


### MI322 — B156: cut attempt does not lift;deliberate next-ambient diagnostic registered (2026-10-17 18:25 BST)

**Hand verdict,one paragraph.** The proposed carrier-component/cut
implication remains OPEN. MI295/MI292 already gives a positive-to-
negative unit path at every SS-feasible nonzero-error state. The
missing inference is scheduling its token witnesses,not finding a
static bin cut. Taking the union of bins that can carry a positive
defect does not establish that every edge out of that union can be
used while its tail carries the defect. MI301's single-swap component
already defeats that commutation shortcut;MI303 already defeats
freezing an off-path bin,even with genuine local rank bounds. Those
are existing controls,not new discoveries. No new invariant obtained;
do not publish the desired component implication as a proof or turn
this into a guard/review entry. The carrier encoding remains exact.

**Changed trajectory:one falsifiable structural question.** At n12,
all bins are triples. At n13,the only min3 four-bin size shape is
(3,3,3,4),and three-for-three exchanges introduce an option absent
from the earlier diagnostic. Does ANY E2 state here need3for3 to
reach zero,or does1/2-token exchange still suffice? This is an
explicit new bounded decision after the failed hand invariant,NOT
an automatic domain extension,all-error study or search for more
local repair modules. It can falsify the proposed small-move route
without assuming any target goal exists. The primary-source/model
calibration is MI321;no new theorem or literature claim.

Record searched:`component.*cut|carrier|closed.*component|reachable.*initial`
AND`SS3|unit|partition|MI295|MI321`:14 hits/5 files,relevant sources
read. Before this changed diagnostic:`n.?13|four.token|three.for.three|3.for.3`
AND`unit|descent|SS3|exchange`:14 hits/6 files,no earlier n13
unit-descent computation found. Cloud's private target-existence
census is NOT a move-graph result. No fresh flags at startup.

**Exact domain/coverage.** Counts(3,3,3,4) on0..12,total78. Enumerate
ALL1201200 labelled partitions;ALL integer SS targets with first
three target coordinates sorted,the four-token bin distinguished.
Retain all E0/E2 states. This represents every min3 four-bin n13
case up to a simultaneous bin permutation;target ties retain every
word. Full labelled-target weights are6/product(multiplicities of
first3 targets!),for this fixed labelled size vector. Do not multiply
by24 or conflate it with all four size-bin placements. Independent
ordered triple-mask enumeration fixes the remaining four-token bin;
compare EVERY target's E0/E2 count via sum-vector multiplicities.
Zero-goal targets retained/reported. Reverse BFS remains exact by
MI318's even-error argument,not by presumed existence.

**Two nested modes.** Mode0 includes EVERY single-token and atomic
2for2 exchange between two bins. Mode1 adds EVERY3for3 exchange.
The latter is the whole three-token bin when it participates;the
four-token bin chooses any3. No additional simultaneous multi-bin
move. Preserve E<=2;record full distances/unreachable states and
literal longest paths. Do not infer uniform bounds from finite maxima.
Tentative H:all E2 states release already under mode0;low confidence,
a negative state is a useful outcome,not a failed instrument. Mode1
distances must be no worse;forecast all controls agree. Neither
reachability hypothesis is asserted as an instrument requirement.

**Controls/unexpected check.** Independent Python mask-exchange BFS
compares WHOLE maps in both modes on(7,23,26,22) and(18,18,18,24).
First is MI301 padded with token12 in the old D bin,and triple labels
sorted B,A,C. It now has a DIRECT quad escape:A{7,9} exchanges
D{3,12},transfer1. Hence exact distances(1,1);counterfactual:the
added token is NOT inert and the old trap distance2 must not be
blindly carried forward. Check every reported maximal path literally.
Unexpected:all-state reflection x->12-x reverses only the three
equal-size labels,leaving bin4's label fixed;targets map to
(36-s_C,36-s_B,36-s_A,48-s_D). Whole two-distance equality required.
These are same-worker controls,not a second-party carrying read.

**One execution after source/prereg push.** Source
tests/probes/instinct/ss3_unit_descent13.{cpp,py}. New engine uses
precomputed subset masks/bit-expanded ownership toggles;the independent
reference constructs actual token combinations. Compile C++20 to a
temporary binary,30wall cap,then one wrapper run. Caps80 aggregate
CPU checked at boundaries,120wall,384MiB peakRSS per process,6M
nodes,2B generated engine moves,16MiB raw. Engine55wall/internal
80CPU hard,wrapper80CPU hard;130wall external watchdog. Retain
raw/stdout/stderr outside git,no uploads. Stop first instrument error
or cap,no repair/retry/cap rise/automatic n14 or all-error run.
Partial coverage is not a pass. Scope is deliberately larger than
B153 and separately budgeted;it is not advertised as the same cost.

Gut:the cut picture alone is cooling;the first size-asymmetric case
raises a concrete new question about move size. Reasoned:ask the
next cheap falsifier before claiming a universal carrier theorem.
No new mathematical result yet;13min ACTIVE,SS3/E28/L8 OPEN.


### MI323 — B156 outcome: first size-asymmetric case releases entirely;maximum still five (2026-10-17 18:28 BST)

**COMPUTED,complete finite domain with same-worker independent
controls;not a general proof.** ONE invocation after b69b6673
source/preregistration push. C++20 compile clean. Every instrument
control passes;no cap,retry,repair or domain extension. Executable
source unchanged except Python docstring's OUTCOME,AST checked.
The cut implication in MI322's first paragraph remains OPEN;the
experiment tests move geometry,not that unproved implication.

**Coverage.** ALL1201200 labelled partitions of0..12 into counts
(3,3,3,4). Exactly3576 SS target vectors with the first three
coordinates sorted,four-token bin distinguished;222858 E0 words
and2679333 E2 starts,total2902191 nodes. Independent ordered
triple masks/sum-vector multiplicities reproduce the WHOLE per-target
coverage map. Every target has at least one goal. Correct fixed-size
label weighting gives14313546 E2 starts and1201200 goal partitions;
the weighted goal equality was also checked in retained artifacts.

| Mode | E2 starts | Unreachable | Maximum shortest descent |
|---|---:|---:|---:|
| All1for1/2for2 | 2679333 | 0 | 5 |
| All1for1/2for2/3for3 | 2679333 | 0 | 5 |

Canonical depth histograms:
- Up to2:1:2256092,2:413053,3:10132,4:48,5:8.
- Up to3:1:2281084,2:388534,3:9663,4:44,5:8.
Full labelled-target histograms:
- Up to2:1:12065640,2:2192886,3:54708,4:264,5:48.
- Up to3:1:12197820,2:2063352,3:52086,4:240,5:48.
No start REQUIRES3for3 to escape in this domain. Such exchanges do
shorten routes;exactly24992 additional canonical starts become
one-move completions,by nested pointwise distance and first-bin
histogram difference. No claim about the total number whose distance
shortens,which would need the joint distance counts.

**Controls.** Independent Python mask-exchange BFS reproduces WHOLE
two-mode maps on692 nodes for(7,23,26,22) and4428 for
(18,18,18,24),including all goals. Padded MI301 start distances
(1,1),as predicted by the literal{7,9}<->{3,12} exchange. All
2902191 state-reflection correspondences agree in both distances;
only equal-size bin labels reverse. All7152 per-target/mode maximal
finite paths pass literal bin-count,sum,moved-token/error-trace
checks. Pointwise inclusion of the two move sets holds.
882087408 generated engine moves,including maximal-path extraction.
No source or raw-output upload. This is not a second-party read.

**Five-move geometry survives even unrestricted pair redistribution.**
With counts(3,3,3,4),any two bins can exchange at most3 tokens.
Thus the larger registered mode includes EVERY possible redistribution
of two bins that preserves their sizes. Eight starts STILL need five
nonincreasing moves. They occur in six target groups,three reflected
pairs;counts of depth5 under the larger mode are1,2,1,2,1,1:

  (4,14,24,36) <-> (12,22,32,12),
  (4,14,25,35) <-> (11,22,32,13),
  (8,10,19,41) <-> (17,26,28,7).

One representative per first-side group:
- A014,B356,C{2,10,12},D{7,8,9,11};target(4,14,24,36).
- A014,B356,C{2,11,12},D{7,8,9,10};target(4,14,25,35).
- A234,B019,C568,D{7,10,11,12};target(8,10,19,41).
The raw engine records one maximal witness per target/mode,not every
extremal word. The full graph/histogram certifies the counts;do not
pretend the representative list names all eight states individually.
These are computational distance statements,no hand classification
or N-independent five-bound claimed.

**Costs/provenance.** Engine20.991091CPU,wrapper5.062961CPU,
aggregate26.054052CPU,wall26.411594s,child RSS177561600B.
Raw engine753298bytes,
SHA256 627e2bf517f84809edcd8ae0a18bc1ffe8fd2ceb4af3e022190e04f572441096.
Local report1253bytes,
SHA256 98bdd19d17072122b68e6bf188e6e24ae84e0a3eda78b90c7bac584b24b1fc77.
stdout/stderr/compile logs retained outside git;stderr and compile
log empty. Peak memory and all registered caps pass. No automatic
further census,cap extension or n14 run.

**What changed,next hand question.** The hypothesis survived the
first asymmetric size case;three-token exchanges are unnecessary
for existence of these finite descents,and even allowing every
pair redistribution leaves five-step extremals. Together with n12
this invites a hand attack on a four-bin bounded unit-augmentation
statement,not a claim that finite agreement proves it. A shortest
bin-level unit path has at most3 edges;nonconsecutive edge witnesses
are disjoint,but adjacent ones can share an intermediate token.
Next inspect that shared-witness geometry globally,using this
specific question:can a closed component avoid collision under all
1/2 exchanges despite sizes>=3,or can the conflict always be released?
A universal bound5 is a tentative empirical candidate,not a target
we may assume;an unbounded-depth counterfamily would change course.
No new local repair catalogue or solver restart is authorized here.

Gut:surprise and renewed mathematical pull that five persists when
every pair redistribution is allowed. Reasoned:finite evidence now
supports a sharper question;it does not narrow the infinite gap by
assertion. Niggle sweep:four-token bin never sorted with triples;
reflection uses48 for its target rather than36;all target ties kept;
added token not inert;larger-mode maxima not extrapolated;nonzero
error stays2 before its terminal0. SS3/E28/L8 OPEN,13min ACTIVE.


### MI324 — B157: global disjoint-witness reduction;endpoint-freezing shortcut killed (2026-10-17 18:37 BST)

**Hand reduction,single-party;not SS3 or a universal depth bound.**
Question:what can actually prevent a shortest three-edge unit path
from lifting as disjoint adjacent-value swaps? Pull:toward a global
selection argument before any repair catalogue. Record searched:
`shortest.*path|shared.*witness|shared.token|DCBA|CBA` AND
`four.bin|four.bin|SS3|MI299|MI303`:14 hits/4 files. Read MI295's
shared-token proof and MI298-299/303 in full relevant parts. Their
fixed families illustrate the obstructions;no earlier complete
three-edge witness-selection alternative found. No novelty claim
for this elementary matching argument,no new experiment or PROOFS
entry/review queue.

**Set-up.** Deviations in four distinct bins A,B,C,D are(1,0,0,-1).
Consider the unit path A->B->C->D. Its witness families,read in
increasing token VALUE,are:

  F=all BA adjacent pairs, M=all CB adjacent pairs, L=all DC pairs.

Each family is nonempty. Every same-type family is a matching of
physical token positions. F and L never intersect:their owner
letters are disjoint. A middle CB pair can intersect at most ONE
F pair (at B) and at most ONE L pair (at C). Conversely any F or
L pair can intersect at most one middle pair. These statements use
actual adjacent positions,not just a bin-level edge.

If f,m,l can be chosen pairwise disjoint,perform them in PATH ORDER.
Ownership of all later witnesses survives,and deviations become
(0,1,0,-1),(0,0,1,-1),then0. This gives a three-move descent.
This does not demand every choice of witnesses be disjoint.

**Complete alternative when no such choice exists.** At least one
of the following holds,and each displayed obstruction is sufficient
to prevent a disjoint choice for THIS path:
1. F and M are singletons and intersect:one unique CBA triple.
   L may have further witnesses elsewhere.
2. M and L are singletons and intersect:one unique DCB triple.
   F may have further witnesses elsewhere.
3. F and L are singletons,M consists of exactly TWO pairs.
   One middle pair meets F only,the other meets L only. This
   gives disjoint CBA and DCB triples (the separated double fork).
The contiguous DCBA overlap is included in both1 and2 when all
three families are singleton. Cases need not be declared mutually
exclusive in that overlap.

**Proof of exhaustiveness.** Fix any f in F,l in L. Their union can
meet at most two distinct middle pairs,so |M|>=3 gives a disjoint
one immediately. If M={m},failure means no pair(f,l) simultaneously
avoids m. Thus either EVERY f meets m or EVERY l meets m. Since
m can meet at most one of each family,this is1 or2.

If M={m1,m2},each chosen(f,l) must meet BOTH middle pairs. Neither
f nor l meets more than one. Consequently each chosen f meets one
and each chosen l the other. No f or l can meet both;allowing two
different f's would force every l to meet both middle pairs,because
different f's meet different middle pairs (or one meets neither).
That is impossible. Thus F is singleton,and similarly L singleton;
they meet opposite middle pairs,case3. Each middle pair meets the
stated endpoint pair only. Its forced CBA/DCB triples cannot overlap:
a common B or C token would force the same CB adjacency.
This proves the alternative without using bin sizes or target
existence. Minimum size3 has NOT yet been spent in releasing the
bottlenecks;that is the open next inference.

A useful quick corollary:if any TWO of |F|,|M|,|L| are>=2,
a disjoint lift exists. Merely having extra tokens in bins does not
establish these multiplicities. MI298's double fork and MI301's
contiguous DCBA control catch that invalid shortcut. A concrete
positive min3 word is ABABADCDCCBD,with target(5,14,23,24).
Witness swaps values(1,2),(9,10),(5,6),in that order,are disjoint
and give bins{0,1,4},{2,3,9},{5,8,10},{6,7,11}. All sums/sizes
check by hand;no claim this path is shortest.

**What shortest-path structure additionally gives.** If the chosen
path is shortest from A to D,there are no CA,DA,DB adjacencies:
these would be shortcuts A->C,A->D,B->D. In case1 the unique BA
and CB overlap at CBA. Every other downward owner transition is
then DC. The ENTIRE word,not a selected local interval,has form

  A^a B^b W B A^d B^e V,

where d>=1,a,b,e>=0,W is a nonempty C/D word ending C,and
V is any C/D word (possibly empty). The final C of W,central B
and first A of A^d are the unique shared triple. Sizes give
a+d>=3,b+1+e>=3,and C,D counts across W,V>=3 in the SS3 regime.
This leaves arbitrary binary W,V,not a promise that a fixed local
module covers them. Case2 reflects this structure. Shortest paths
of length1 or2 are separate cases;this reduction does not silently
dispose of them or the unused fourth bin.

**Unexpected hand kill of a tempting completion.** One might try
to freeze A,B while freely reshaping the two C/D intervals. That
connectivity claim is FALSE. Take their pool P={0..5} union{12..17},
each bin size6,with allowed C moments43 or44. Both C sets
{0,2,4,5,16,17} and{0,1,4,12,13,14} have sum44,but contain
respectively2 and3 high-interval tokens. Any1/2-token exchange
changing that count changes C's sum by at least2:one cross-interval
transfer costs>=7,and the one remaining internal compensation
has magnitude<=5;two transfers in the same direction cost>=14.
It cannot stay in the two adjacent moment levels. Thus the count
is invariant on each allowed component,and those two states are
not connected under the restricted reshaping.

This is an ACTUAL full-interval min3 control,not a counterexample
to SS3:let A={6,7,8},B={9,10,11},take the first C above,D=P-C.
Targets(20,30,44,59),current deviations(1,0,0,-1). Unfreezing A
gives the one-move quad repair A{6,8}<->D{1,12}:final
A={1,7,12},D={3,6,8,13,14,15},B,C unchanged. Literal target
partition proves SS. This is a kill test of the auxiliary frozen
connectivity idea,not a new probe/proof/review job or rediscovery
of general infeasibility. The endpoint must remain available.

**Reflection/fresh-choice check.** The last full loop reflection
was B150;this block reaches90 minutes. Understanding moved
through two finite diagnostics,a hand extremal explanation and a
new global witness alternative. The repeated open step is now
explicit:use the third tokens and full interval to release a UNIQUE
shared boundary,while permitting endpoint participation. I would
still choose that question fresh;the warmth comes from a reduced
structural obstruction,not from repeating the number5. The failed
frozen-endpoint idea changes the next approach. Do not react by
opening a module catalogue or another census. Next work should
seek a global exchange/ordering invariant for arbitrary W,V,or an
adversarial family that refutes the desired bounded release.

Gut:enjoyment at the selection reduction,disappointment at frozen
C/D connectivity,and relief that its hand countercontrol is decisive.
Reasoned:generic three-edge lifts are settled;three obstruction
forms remain,not a solved lifting theorem. Niggle sweep:middle
family cardinalities exhaust1/2/>=3;an endpoint witness meets only
one middle witness;double-fork triples really are disjoint;other
bin paths can still work;no assumption of a compatible goal;frozen
subproblem and full instance distinguished. Hand reduction remains
single-party;SS3/E28/L8 OPEN,13min ACTIVE.


### MI325 — B158: choose the realization before trying to repair it (2026-10-17 18:53 BST)

**Change of approach;hand controls,single-party,no new theorem.**
The claimed arbitrary-W,V release did not produce a global argument.
Pull shifted to a freedom in the actual target:MI321's UN asks
whether an SS-admissible unit neighbour y of an ATTAINABLE x is
attainable. It permits choosing ANY realization of x. Repairing
EVERY starting partition within five monotone moves is stronger.
Record searched:`unique.*(CBA|boundary)|A.\^a.*W|three.bin.*gap|punctured.*three`
AND `SS3|exchange|rank|pool|word`:15 hits/7 files;MI324/299 read.
`joint.*reali|best.*(fiber|fibre)|neighbor.*(fiber|fibre)|disjoint.*adjacent.*target`
AND `SS3|sum|partition|unit`:4 hits/2 files,unrelated. Bounded web
queries on prescribed partition sums,neighbouring targets and
adjacent transpositions found no exact statement;this is NOT a
novelty or literature-completeness claim. No external theorem
imported. No experiment,PROOFS entry or carrying read requested.

**Why a difficult start need not control UN.** MI320's target is
(4,14,23,25),and its five-move start has current sums(5,14,23,24).
Those SAME current sums also have the realization
A={0,1,4},B={2,5,7},C={6,8,9},D={3,10,11}.
Swap A4/D3:the target is reached in one adjacent-value swap.
All bins have size3 and cover0..11 once. No neutral path from the
old start to this new start is asserted or needed for UN. This is
not a shortcut in MI320's fixed-start lower bound;it changes the
quantifier to the one the existence proof actually needs.

**Unexpected hand check:freedom of realization does not make one
or two moves sufficient.** For sizes3^4 take x=(3,12,23,28),
y=(4,12,23,27). One x realization is A012,B345,C{6,7,10},
D{8,9,11}. The disjoint adjacent-value swaps A2/B3,B5/C6,C10/D11
produce A013,B246,C{5,7,11},D{8,9,10},with sums y. Relative
to y,the errors travel(-1,0,0,1),(0,-1,0,1),(0,0,-1,1),0.
This literal goal establishes SS without assuming SS3. Conversely,
EVERY x realization has A012 and B345 by successive minimum
triple sums. EVERY y realization has A013 then B246:the latter
must include2,and its remaining pair is4,6. Its C must contain5,
since without5 the least available triple is7+8+9=24>23.
Thus all four bin sets change between ANY such x/y realizations.
Two two-bin exchanges would have to involve disjoint pairs of bins,
each touched once. A's sole exchange must replace2 by3 from B;
B would become245,sum11,not its required12. Contradiction.
Hence the minimum over BOTH fibres is exactly3,even allowing
arbitrary intermediate energy and arbitrary pair redistribution.
This supporting control is not a new proof-review job.

**Unresolved question and next cheap test.** Can an attainable x
and its SS-admissible unit neighbour always be jointly realized
so a simple bin-level unit path has disjoint adjacent-value
witnesses? With four bins that would use at most3 swaps and imply
UN,hence SS3 through the known target-domain exchange paths.
It is STRONGER than UN,not a consequence we may assume. The
controls above motivate testing it,not believing it. Next seek a
hand falsifier first,or an extremal choice of x realization that
forces compatible witnesses. Do not substitute this untested3
for the old empirical5,launch a larger census,or assume a y
partition while trying to prove it exists. Failure of this stronger
coupling would leave UN available without a bounded-move demand.

Gut:renewed pull from removing an unnecessary universal-start
requirement;disappointment that the arbitrary-word release did not
close. Reasoned:the target now uses its actual existential freedom;
no general missing inference has been filled. Niggle sweep:the
new x realization has identical sizes AND sums;both examples cover
the full interval;the lower bound ranges over both fibres,not one
start;all four bins really change;the positive controls do not
assume the conclusion. MI324's global release stays OPEN. No
review halt or new run;SS3/E28/L8 OPEN,research13min ACTIVE.


### MI326 — B159 preregistration: can choosing the realization remove every witness collision at n12? (2026-10-17 19:02 BST)

**A different quantifier on the existing domain,not a larger n.**
The initial hand kill search did not find a counterexample. Register
ONE finite test of MI325's stronger coupling before trusting it.
Record searched:`joint.*reali|disjoint.*unit|adjacent.*coupl|fibre.*pair|fiber.*pair`
AND `SS3|sum|partition|unit`:14 hits/7 files;relevant MI325,others
unrelated. Literature scope is MI325's bounded search,not novelty.
Cloud has sent CL435/3836a4f9 since this tick's fetch;its object is
not yet local. Read/verify it after synchronization,before execution.
No view on its advice inferred from the flag alone.

For pool0..11 and four sizes3,enumerate all369600 labelled owner
words. Retain EVERY word whose sum-vector x is sorted,including
all ties;bin permutation covers other x. This gives19344 words,
630 known SS vectors. For each x and each ordered a!=b with
SS-admissible y=x-e_a+e_b,look over the ENTIRE x fibre for a
matching of at most3 adjacent-value pairs whose swaps give y.
This is not the old maximum distance over starting words. It
minimizes over the fibre;no goal word is assumed as input.

P1:independent disjoint-combination enumeration agrees on EVERY
fibre count,and independent subset-bound loops agree on EVERY
eligible unit neighbour. P2 BLIND:all these neighbours have a
lift. A missing lift is a counterexample to the stronger coupling,
not to SS3;retain all failures. Whole independent minimum maps
on x=(3,12,23,28),(5,14,23,24),(16,16,17,17),(7,10,23,26)
use simple bin paths/witness products rather than physical value
matchings. Net unit flow in <=3 disjoint swaps always contains
a simple bin path;any separate two-cycle can be removed,so the
minimum maps describe the same question. This equivalence does
not assert that a lift exists.

Unexpected check:reflect EVERY canonical target/direction with
value reversal plus bin reversal,including ties/failures;all minimum
depths must match. Audit every successful literal word,physical
pairs and final target. Counterfactual <=2 always suffices must
fail on MI325's x=(3,12,23,28),a3,b0,exact3. The old five-depth
sums(5,14,23,24),a0,b3 must instead give1. Direct invalid-pair
controls reject overlapping or nonadjacent pairs on a valid word.

Source tests/probes/instinct/ss3_joint_lift.cpp and sibling.py.
Intel CPU,one invocation after source/predictions push and Cloud
read;40aggregateCPU/60wall,192MiB per process,3M engine matching
trials,4MiB raw,70wall watchdog. No retry/extension/larger n or
automatic follow-on. Raw local. Complete success would be finite
support only,not UN/SS3 or a general3-bound. No carrying read
requested;research13min ACTIVE. The hand obstruction search and
the whole-fibre quantifier are the pull,not another timing record.


### MI327 — B159 partial outcome and Cloud's check-in:reflection reverses the transfer (2026-10-17 19:04 BST)

**PARTIAL/INSTRUMENT-FAILED;ONE invocation,no repair or retry.**
Prereg bad02e8b/MI326,published with Cloud merge6e622b4d before
execution. C++20 compilation clean. The engine completed and
emitted369600 labelled words,19344 canonical words,2708160
matching trials/140 matching masks. Independent full fibre counts
and all eligible target/direction pairs agreed. Every emitted
successful partition/pair-set/final sum was literally audited.
Whole independent bin-path minimum maps passed on ALL FOUR
registered fibres. Then the wrapper stopped at its reflection
comparison with a KeyError;it did not reach the later distance3/1
counterfactuals,invalid-pair controls,final resource checks or JSON
report. This is not a completed control pass or a cap event.

**Actual defect.** Under r(x)=11-x,each triple sum s becomes33-s.
Thus a unit DECREASE of original bin a becomes a unit INCREASE
of its reflected bin. After reversing bin labels to keep x sorted,
a directed pair(a,b) must map to(3-b,3-a). I wrote(3-a,3-b).
The first failed lookup was x'=(3,12,21,30),direction2->3;
that neighbour would put the last bin above its maximum30,and
is correctly absent from the eligibility map. This explains the
failed control by hand;it is not a repaired/re-executed check.
The computation source remains as run,with this outcome appended.

For retention,PRIMARY output contains7184 eligible directed
neighbours with minima1:6748,2:408,3:28,and no missing lift.
These are primary observations with the validation limitation
above;P2 is not recorded as a complete pass. No universal
coupling/UN/SS3 theorem,replication or novelty claim follows.
The four reference counts and every positive literal check did
finish;their completion is not erased or promoted to completion
of the whole protocol. Watchdog wall1.61735426099s,wrapper exit1.
No final CPU/RSS summary was emitted;do not invent one.

Raw engine233961bytes,SHA256
b25a754a3dde96f30f5738de61d48d2cf456444176b22625aeb70475ef13fecf.
stdout empty;stderr480bytes SHA256
88c2d441dbcbb43244300a566d2952f2b5427fe1206bd89a54fa2909ac14bae0.
Compile log empty,no JSON report. All retained outside git.

**CL435 read and response,not a permission gate.** Commit3836a4f9
was fetched in the single push-rejection recovery,merged,read in
full and ACKed before execution. Agree:no routine n14 census and
no leap to k5 after a possible k4 proof;the rigid-word release
remains a plausible strong route. Two points of pushback:equal
maxima at12/13 do NOT force a growing obstruction family to show
growth there;it could begin later or have a plateau. Also UN needs
no invariant selecting one realization along the whole target
path as a matter of LOGIC. If existence of x is already proved,
a UN proof may choose any of its realizations afresh. A constructive
proof must justify that helpful choice without assuming y;that is
the actual missing selection step. The stronger algorithm could
still be the easier theorem,but its extra demand is not required
for existential composition. MI325's all-four-bins control does
not change this distinction. No routine carrying read requested.

**Next choice.** Return by hand to choosing a helpful realization
of x:can an extremal choice force a disjoint lift,or does a real
obstruction persist across the fibre? The new primary output did
not produce a counterexample;finite support is not a substitute
for that argument. Do not automatically rerun the diagnostic with
a patched control or widen n. If another run becomes mathematically
needed,it requires its own explicit preregistration. Pending review
and this instrument failure do not halt independent reasoning.

Gut:annoyance at my reflection-direction error;the mathematical
pull toward existential choice remains specific,without a claim
of new excitement from finite agreement. Reasoned:retain the partial
work honestly and change back to the missing hand inference.
Niggle sweep:the reflected source AND sink interchange;canonical
ties keep bin labels;literal positives are distinguished from
missing-lift certification;unreached checks are not passes;no
hidden retry. SS3/E28/L8 OPEN,research13min ACTIVE.


### MI328 — B160: a neutral exchange removes the separated double fork globally (2026-10-17 19:18 BST)

**PROOF-SKETCH;carrying read requested,not SS3 or a target partition.**
Pull:toward using the freedom to choose a realization,through a
sum-preserving exchange that SHORTENS the bin path. Initial
record search `extremal.*(realiz|word)|maximi.*witness|lexicograph.*(partition|bin)|neutral.*(rectangle|cycle)|M.convex`
AND `SS3|sum|partition|unit`:7 hits/4 files,relevant MI321/PRIOR-ART.
Refined `double.fork|separated.*triple|neutral.*short|shorter.*path`
AND `SS3|sum|partition|unit|CBA`:5 hits/3 files,relevant MI324.
MI295/298 and MI324 read. Bounded arXiv searches for prescribed
sums/four parts/exchanges and fixed-moment coloured words found
no exact match;no novelty or literature-completeness claim. No
external theorem imported. No experiment or repair of MI327.

**Candidate statement.** Read a full consecutive token interval
in increasing value,with owner letters A,B,C,D,each occurring>=3.
Bin edge X->Y means an adjacent YX pattern:swap it to decrease
X's sum by1 and increase Y's. Suppose A->B->C->D is a shortest
A->D path,and its failed disjoint-witness lift is MI324 case3:
BA is unique,DC is unique,and there are exactly two CB pairs,
one meeting BA and the other meeting DC. These force disjoint
CBA and DCB triples. Then ONE neutral2for2 exchange,between
some two bins,preserves ALL four sizes AND sums and produces an
A->D path of length<=2. It need not itself reach the prescribed
target,or make the shorter path physically disjoint. Those are
separate missing steps. No assumption of target existence is used.

**Three neutral operations.** Swapping a ji adjacency and a
disjoint ij adjacency simultaneously is a neutral2for2 exchange
between i,j:one unit moves each way. Consequently:
- A disjoint AB together with the unique BA turns CBA into CAB,
  creating CA,while the DC edge is untouched. Path A->C->D.
- A disjoint CD together with unique DC turns DCB into CDB,
  creating DB,while BA is untouched. Path A->B->D.
- A BC disjoint from the CB of CBA can be swapped with it,
  creating CA. The DC edge survives:its C token has preceding D,
  so cannot be the C of a BC pair;the first triple's C is not that
  DC token. Similarly a BC disjoint from CB of DCB creates DB
  and preserves BA:its B token,followed by A,cannot start BC,
  and the second triple's B is not the BA token.
Each operation uses two distinct tokens from each of its two bins.
All paths in this proof are BIN paths,not an asserted physical lift.

**I. CBA occurs before DCB.** With no shortcut CA,DA or DB,
and with exactly the specified downward transitions,the ENTIRE
word has form

  A^a B^b C^c B A^d B^e C^f D^g C B^h C^i D^j,          (I)

where c,d,g,h>=1 and other exponents>=0. The middle B and later
C are singletons because their CB pairs must overlap BA and DC.
There can be no D before the first CBA:leaving it would spend
the unique DC before the later DCB. All remaining stretches are
ascending runs;thus (I) is exhaustive,not a local placement family.

If any of the three neutral operations above applies,we are done.
Assume none does. In this order a BC edge cannot meet BOTH CB
pairs. It can meet the first CB only at that triple's C (its B is
followed by A),and the second only at that triple's B (its C is
preceded by D). Those tokens occur in the opposite order for a
single BC pair. So ANY BC is disjoint from at least one CB and
would shorten the path. Hence there is NO BC anywhere. From (I):

  b=0, i=0, and e*f=0.

No disjoint AB also gives d>=2 => e=0. No disjoint CD gives
g>=2 => f=0. Suppose e>0. Then d=1,f=0;A's size forces a>=2,
and C's size c+1>=3 forces c>=2. Choose the last-but-one A of
A^a and the first C of C^c,a value-distance2 pair AAC. It is
disjoint from the A,C endpoints of the CBA triple,since c>=2.
Exchange these TWO A tokens with the two C tokens:the CBA
endpoints move A down2 and the AAC endpoints move A up2,so
the exchange is neutral. AAC becomes CAA,creating CA;the unique
DC belongs to the later triple and is untouched. This shortens
the path,a contradiction. Thus e=0. Value reflection with names
A<->D,B<->C maps (I) to itself and interchanges e,f;the same
argument gives f=0. Reflection here reverses both direction AND
bin names,so the A->D orientation is restored.

We have reduced the whole word to

  A^a C^c B A^d D^g C B^h D^j,
  c,h>=2, a+d>=3, g+j>=3.                              (R)

If a>=2,the same AAC neutral exchange works. If a=1,c>=3,
use the AC pair at distance2 across ACC instead:its C is the
second of C^c,distinct from the CBA endpoint. ACC becomes CCA
and creates CA,again preserving DC. Thus,if still unresolved,
a is0 or1,and a=1 requires c=2. By reflection,j is0 or1,and
j=1 requires h=2. In particular d,g>=2. These restrictions are
only used to guarantee two distinct central A/D tokens below.

**The nonlocal exchange that closes (R).** Number values from0,
put p=a+c (the isolated B),and z=p+d+g+1 (the isolated later C).
The central A interval is[p+1,p+d],and the central D interval is
[p+d+1,p+d+g]. C also owns[a,a+c-1];B owns[z+1,z+h].

Two distinct tokens from an integer interval[r,s],s>=r+1,
have EVERY sum from2r+1 through2s-1. To see it,for a desired
sum S choose u=max(r,S-s),v=S-u;these are in the interval and
u<v (use u=r when S-s<=r,otherwise v=s). Apply this elementary
fact to the two central intervals.

A pair consisting of z and one prefix C has sums in
[2a+c+d+g+1,2a+2c+d+g]. Two central A tokens have sums in
[2a+2c+3,2a+2c+2d-1]. These intervals meet exactly when

  g <= c+d-2,                                         (AC)

since the other overlap inequality is d+g>=3,already true.
If (AC),exchange those equal-sum pairs. The isolated C at z
becomes A,immediately after a D at z-1. That is a DIRECT DA
edge,A->D. Cardinalities and all sums are unchanged.

Otherwise try B's isolated p and one token of its final h-run.
Their sums range over[2p+d+g+2,2p+d+g+h+1]. Two central D
sums range over[2p+2d+3,2p+2d+2g-1]. They meet exactly when

  d <= g+h-2.                                        (BD)

An equal-pair exchange changes B at p to D,immediately before
A at p+1,again giving DIRECT DA. If BOTH (AC) and (BD) failed,
integers would give g>=c+d-1 and d>=g+h-1. Adding yields
0>=c+h-2,impossible since c,h>=2. One exchange must exist.
This closes order(I),including arbitrary outer a,j padding.

**II. DCB occurs before CBA.** The exhaustive whole word is

  A^a B^b C^c D^d C B^e C^f B A^g B^h C^i D^j,          (II)

with d,e,f,g>=1. If e>=2,the BC boundary between B^e,C^f is
disjoint from the earlier CB,so its neutral operation creates DB
and preserves BA. If f>=2,it is disjoint from the later CB,
creates CA and preserves DC. Thus only e=f=1 remains. Other
BC boundaries must be absent,so b*c=0,h*i=0. Bin sizes give
b+h>=1,c+i>=1. Hence exactly one of these cases holds:

  b>0,i>0,c=h=0; or h>0,c>0,b=i=0.

In the first,no disjoint AB forces a=0,and no disjoint CD forces
j=0. A's size now forces g>=3 and D's size d>=3. The word is

  B^b D^d C B C B A^g C^i.

Exchange B tokens at b-1 and b+d+1 with D tokens at b+1 and
b+d-1. Both pairs sum2b+d;all four tokens are distinct because
d>=3. The first three values around that reverse distance2
pair BDD become DDB,creating DB at values b,b+1. The later
BA is untouched. Hence A->B->D is a shorter bin path.

In the second case h>0,c>0,b=i=0,no disjoint AB forces g=1,
so a>=2;no disjoint CD forces d=1,so j>=2. The whole word is

  A^a C^c D C B C B A B^h D^j.

Exchange A tokens a-2 and a+c+5 with C tokens a and a+c+3.
Both pairs sum2a+c+3,and all four tokens are distinct. The prefix
AAC becomes CAA,creating CA at a-2,a-1;the original DC at
a+c,a+c+1 is untouched. Hence A->C->D is shorter. Reflection
does NOT interchange these two alternatives,so both have been
checked directly. This closes order(II) and the candidate statement.

**Use for the actual selection question.** Fix attainable x and
SS-admissible y=x-e_A+e_D. Among all realizations of x choose
one minimizing the shortest A->D bin-path length. SS guarantees
a path (MI295's cut argument),so the minimum is1,2 or3. If it
is3,MI324's separated double-fork case cannot occur:the neutral
exchange above gives another realization of EXACTLY x with a
shorter path,contradiction. Generic disjoint lifts already give y.
Thus a counterexample to disjoint lifting still needs a unique
shared CBA or DCB case (including contiguous DCBA),or a shared
TWO-edge path. This does not assert that either remaining type
can be released. No invariant along a target-domain path or
existence of y was smuggled into the extremal choice.

**Literal hand checks.** For order(I),word AACCBADCBBDD has
A015,B489,C237,D6,10,11. Neutral A{0,5}<->C{2,3} preserves
sums(6,21,12,27);CA at0,1 and DC at6,7 give disjoint two-edge
path. The more difficult residual word CCB AAADDDCBB (spaces
ignored) has A345,B2,10,11,C019,D678. Neutral A{4,5}<->C{0,9}
creates DIRECT DA at8,9,preserving(12,23,10,21).
For order(II),word BDDDCBCBAAAC has A8,9,10;B0,5,7;C4,6,11;
D123. Neutral B{0,5}<->D{2,3} preserves(27,12,21,6),creates
DB at1,2,and preserves BA at7,8. The OTHER order(II) alternative
has word AACDCBCBABDD,A018,B579,C246,D3,10,11. Neutral
A{0,8}<->C{2,6} preserves(9,21,12,24),creates CA at0,1 and
preserves DC at3,4. Every displayed word covers0..11 once.
These are algebraic hand audits,not machine runs or replication.

**Unexpected negative control.** Lowering every size to2 fails:
word ACBADCBD has sums(3,8,6,11),the separated double fork,
no shorter path,and NO neutral2for2 exchange at all. Such an
exchange would trade the entire two-token bins and require two
equal bin sums;all four differ. This is the known MI298 negative
boundary,used as a check on where the third tokens enter,not a
new counterexample or proof queue. In (I) they force c,h>=2 and
central d,g>=2;in (II)'s first residual case they force d,g>=3,
and in its second they force a,j>=2.

Gut:surprise and renewed pull at a nonlocal equal-pair exchange,
which replaces unbounded run lengths by two incompatible interval
inequalities. Reasoned:complete candidate removal of ONE global
obstruction,not SS3 or a completed unit lift. Niggle sweep:two
triple orders exhausted;neutral operations use four DISTINCT tokens;
the old shortest-path shortcuts are forbidden throughout the word;
all four moment sums are preserved;reflection reverses direction
before swapping names;reflection does not interchange order(II)'s
two alternatives,which are instead checked directly;central pair
spectra include endpoints;the new graph path may still share tokens
and is not a goal partition.
Cloud's carrying read should focus on those points. Continue the
remaining unique-shared-boundary question independently;no routine
review halt or new experiment. SS3/E28/L8 OPEN,research13min ACTIVE.


### MI329 — B161: a sharp three-bin outlier lemma closes a four-bin singleton boundary (2026-10-17 19:30 BST)

**PROOF-SKETCH,dependent only on PROVED MI295;not SS3.**
The neutral-shortening question exposes words in which a bin is
forced to take the largest tokens. Its unit neighbour leaves a
prefix with one lifted token. Pull:toward assigning that outlier
FIRST,then using the verified three-bin theorem on a full interval.
Record searched:`unique.*CBA|A.\^a.*W|neutral.*short|separated.*fork`
AND `SS3|sum|partition|unit|MI324`:8 hits/2 files. Then
`one.hole|punctured|single.*delet|lift.*(last|largest)|singleton.*(bound|slack)`
AND `SS3|three.bin|MI305|prescribed|sum`:36 hits/11 files.
MI295 and the relevant MI304-305/PRIOR-ART source scopes read.
The earlier two-bin window spectra do not assert simultaneous
three-bin partitions of this pool. Bounded primary-web queries
on prescribed three-part sums/almost consecutive/one-hole pools
were unhelpful;no novelty or literature-completeness claim.
The scarce-outlier obstruction below is the same general principle
already credited to Hoory-Kotlar Example2.8,not a new principle.
No new experiment,MI327 repair or use of unverified MI328.

Write L(t)=t(t-1)/2,U_M(t)=t(2M-t-1)/2. Let c1,c2,c3>=r>=3,
M=c1+c2+c3,and consider

  P={0,...,M-2} union{M-1+h}, 1<=h<=(r-1)^2.

For each cardinality1<=C<M,the C-token subsets of P have
minimum sum L(C) and maximum U_M(C)+h.
Suppose integer targets s_i total L(M)+h and obey these rank
bounds for every bin subset. Then P can be partitioned with
sizes c_i and sums s_i. The bound on h is UNIFORMLY SHARP:
for every r>=3 it fails at h=(r-1)^2+1 with sizes(r,r,r).

**Exact owner test,valid at any h>=1.** Let t=M-1+h be the
outlier,and define

  V_i=U_(M-1)(c_i)=U_M(c_i)-c_i,
  Q_i=t+L(c_i-1)=L(c_i)+M-c_i+h.

A suitable owner j must satisfy s_j>=Q_j and s_i<=V_i for i!=j.
These conditions,along with the original rank bounds,are also
SUFFICIENT:remove t from bin j,leaving counts c_j-1>=2 and
other counts>=3 on the full interval0..M-2. All three residual
singleton lower/upper bounds hold. For j,the lower bound is Q_j,
and its upper follows from

  U_M(c_j)+h-t=U_(M-1)(c_j-1).

For i!=j,the lower is the original L(c_i),and the upper is V_i.
Residual sums total L(M-1);with THREE bins,the pair bounds are
the complementary singleton bounds. Apply PROVED MI295.
Necessity is immediate from owning or omitting t. This exact
owner test is not an assumption of a target partition.

**Why an owner always exists under the stated h bound.** Call
bin i high if s_i>V_i. There cannot be two high bins i,k:using
the third bin's lower bound,the total would be at least

  V_i+1+V_k+1+L(c_l)
   = L(M)+(c_i-1)(c_k-1)+1
   >= L(M)+(r-1)^2+1 > L(M)+h.

If there is one high bin j,choose it. All others already obey
s_i<=V_i,and

  V_j+1-Q_j=(c_j-1)(M-c_j-1)-h >=0

because c_j>=r,M-c_j>=2r and h<=(r-1)^2. Thus s_j>=Q_j.

If there is no high bin,it remains to find ANY s_j>=Q_j. Were
all s_i<=Q_i-1,their total would be at most

  sum L(c_i)+2M+3h-3.

Put K=c1*c2+c1*c3+c2*c3. Their actual total is
sum L(c_i)+K+h. Expanding c_i=r+u_i with u_i>=0 gives

  K-2M+3 >=3(r-1)^2 >2h.

So the proposed upper total is strictly too small. Some owner
j qualifies. The exact owner test completes the construction.
There is no search through partitions or unproved integral lift.

**Sharpness belongs to this pool class.** Take M=3r,
h0=(r-1)^2+1,all sizes r,and targets

  L(r), V+1, V+1, where V=U_(3r-1)(r).

Their total is L(3r)+h0. Each target lies between L(r) and
U_(3r)(r)+h0. For THREE bins those singleton bounds imply all
proper-subset rank bounds by complementarity. But each of the
two V+1 bins must contain the unique outlier:without it the
maximum r-subset sum is V. Impossible. At r3 the concrete pool
is0..7 union{13},targets(3,19,19). This proves sharpness of the
uniform h threshold,not an obstruction to full-interval SS3.

**Four-bin consequence:singleton extreme slack.** Now partition
0..N-1 into four sizes,each>=3. Let a be one selected size and
r the minimum of the OTHER three sizes. Assume full SS. If
its prescribed sum is U_N(a)-h,where

  1<=h<=min(a,(r-1)^2),

put M=N-a,t=M-1+h and CHOOSE the selected bin to be

  A={M-1,M,...,N-1} minus{t}.

The condition h<=a ensures t<=N-1,so this is a legitimate
size-a set. Its sum is U_N(a)-h. The remaining pool is exactly
P above. Its three targets total L(M)+h. For any proper subset
J of remaining bins of total size C,full SS gives lower L(C),
and the upper bound on A union J gives

  S_J <= U_N(a+C)-S_A = U_M(C)+h.

Thus all rank bounds for P hold;the outlier lemma completes
the remaining bins. At h=0 choose A to be the top a tokens and
apply MI295 directly. Reflecting all values gives the identical
result within min(a,(r-1)^2) of L(a). No singleton is assumed
forced except where it actually is;the canonical set is chosen.
In particular sizes>=3 suffice whenever ANY singleton target is
within3 of its minimum or maximum. If a>=4 and the other sizes
are>=3,the same construction reaches slack4. Do not drop h<=a.

**How this advances the claimed unique-CBA question.** In a
realization minimizing the shortest A->D bin-path length at3,
a disjoint reverse AB and the unique BA could be exchanged
neutrally,creating CA while DC is untouched. Hence the full
MI324 word A^a B^b W B A^d B^e V must have either
B^b W B A^d V with b>=2,d>=3,or A^a W B A B^e V with
a>=2,e>=2. No conclusion about the two-edge path is used.
If V is empty,the first form has CURRENT A at its maximum,
so the GOAL A is one below maximum;the second form has B one
below maximum in BOTH current and goal. The new construction
therefore settles these entire goal-existence branches,whatever
binary W is. In the first form B's GOAL is L(b+1)+|W|;
in the second A's GOAL is L(a+1)+|W|. It also settles the
small-|W| branches that satisfy the displayed singleton-slack
bound. Arbitrary longer W with nonempty V remains OPEN.
This is an existence construction,not neutral-shortening of every
start or a disjoint lift of length3. MI328 is not a dependency.

**Hand controls and unexpected separation of claims.** For r3,
h4,P=0..7 union{12},targets(13,13,14),choose outlier owner0:
{0,1,12},{2,4,7},{3,5,6}. The first target hits Q=13 exactly.
Embedding with N13,a4 gives four bins{8,9,10,11},{0,1,12},
{2,4,7},{3,5,6},sums(38,13,13,14),singleton upper slack4.
Reflecting gives sums(10,23,23,22),checking lower slack4 and
unequal selected size. All values used once,by hand.

Unexpected:the h5 CANONICAL failure does not imply a full
four-bin failure. N14,sizes(5,3,3,3),targets(50,3,19,19) have
canonical A={8,9,10,11,12},leaving the impossible h5 pool above.
Yet A={7,9,10,11,13},B012,C{3,4,12},D{5,6,8} is a literal
full solution. The sharp bound is for the outlier-pool admission,
not the SS3 problem or every possible singleton construction.
No new computation or claimed complete finite audit.

Gut:renewed pull from assigning the troublesome token first,
with delight at a sharp threshold and a direct test of its limit.
Reasoned:a complete-looking extension of the VERIFIED three-bin
mechanism and a four-bin boundary closure,requiring an independent
carrying read. General SS3 and all central cases remain OPEN.
Niggle sweep:rank bounds match the actual punctured pool;three-bin
complementarity is used only with three bins;outlier owner's size
stays>=2;h<=a keeps the chosen token inside the original pool;
sharp canonical failure is separated from full feasibility;reflection
is on sums,not a misoriented error transfer. Send a batched proof
read with MI328,then continue the remaining central/shared-boundary
question independently. No review halt;13min ACTIVE.


### MI330 — B162: two cheap failures redirect the selection argument (2026-10-17 19:46 BST)

**Hand route tests,no experiment,new PROOFS entry or carrying read.**
Unease:neutral-shortening could quietly become another local-repair
catalogue. Kill test before extension:can MI320's current realization
I=(014;356;2,10,11;789),sums(5,14,23,24),make ANY exact-sum
neutral two-bin move? No:single swaps require equal values;for2for2
between triples,omitted values u,v must differ by the bin-sum
difference. For pairs AB,AC,AD,BC,BD those differences are
-9,-18,-19,-9,-10,smaller than the respective possible minima
-6,-11,-9,-8,-6. For CD the difference is-1,but none of
{2,10,11} minus{7,8,9} equals-1. Whole-triple exchanges require
equal bin sums,which are all distinct. Thus even arbitrary-size
neutral TWO-bin redistribution cannot leave I. Nevertheless
(014;257;689;3,10,11) has the same sums and permits direct A4/D3
repair toward(4,14,23,25);this is isolation of a chosen realization,
not a nonexistent target. Next hand kill:actual rank bounds on
P={0,...,9} minus{3},three sizes3,accept targets(4,18,20):single
bounds[3,24],pair bounds[18,39],total42. But the only distinct
nonnegative triple summing4 is013,using the missing3. So an
arbitrary one-hole extension of MI329's rank-sufficiency is FALSE.
MI329's particular lifted-outlier hypothesis is unaffected. These
failures are filed together as a route correction,not as new proof
contributions. Gut:disappointment that the tidy completion shortcut
fails,and renewed curiosity about whether individual EXACT subset
spectra capture the entire one-hole obstruction. Reasoned:that is a
new,precise question,not yet a result;MI303 shows individual
feasibility does NOT suffice for arbitrary multiply punctured pools.
Niggle sweep:all neutral move sizes exhausted for triples,not merely
quads;rank bounds are for the actual pool;counterexample is NOT to
full-interval SS3. Next cheap test is MI331,no larger descent census.


### MI331 — B162 preregistration: exact singleton spectra on one-hole pools (2026-10-17 19:46 BST)

**NOT RUN.** Does a three-bin pool P={0,...,M} minus{q},with
all sizes>=3,admit prescribed sums whenever total/rank bounds hold
AND each individual sum is actually realized by a subset of its
size? A proof would supply a more faithful completion tool than
rank bounds alone;an explicit small counterexample would reject it.
No claim that it settles four-bin SS3,or that a chosen fourth bin
necessarily leaves rank-feasible targets. Pull:toward the distinction
between an individually available sum and jointly compatible bins.
Record searched:`one.hole|single.deletion|punctured` AND
`three.bin|prescribed|sum`:26 hits/9 files;MI303/329,MI271 and
PRIOR-ART spectrum/source scopes relevant and read. Bounded primary
web search for prescribed three-part sums with one missing token
found no applicable theorem;no novelty/completeness claim. Known
interval spectra and MI295 are controls,not research contributions.

**One fixed diagnostic,source tests/probes/instinct/ss3_one_hole.py.**
All q=0,...,M for sizes(3,3,3),M9,and(3,3,4),M10. This tests a
new almost-consecutive-pool hypothesis,not larger n in the old
unit-error diagnostic and not a repaired MI327 run.
- Prediction:EVERY target surviving exact singleton spectra and
  all six proper-subset rank bounds is jointly realized in these
  fixed domains. A finite pass leaves the general question OPEN.
- Counterfactual:MI330's q3,(4,18,20) passes rank bounds but fails
  singleton spectrum and actual partition tests.
- Independent controls:whole attainable-vector maps by bin-subset
  combinations/complements versus token-by-token owner recursion;
  counts agree with multinomial;every literal partition is checked.
  Endpoint holes give full intervals,where PROVED MI295 predicts
  rank-only completeness. Reflection q->M-q maps EACH same-labelled
  bin sum s_i to M*c_i-s_i;no unit-transfer endpoint orientation.
- Unexpected negative:sizes2^3,P={0,1,2,3,4,6},targets(2,6,8)
  pass rank AND singleton-spectrum tests but cannot partition:
  2 forces02 and8 forces26,sharing2. Both instruments must reject
  this target. Thus the minimum-size condition cannot be dropped.
- Stop:ONE invocation,3 aggregate process CPU seconds,5 wall,
  64MiB peakRSS,100KiB output,10s external watchdog. First failed
  control is INSTRUMENT-FAILED;first refined counterexample is
  REFUTED and stops the question. Retain either result;no patch,
  retry,cap increase or automatic larger domain. Raw local only.

Source and this registration are published before execution. This
wake ends at preparation,not at a review permission gate;next research
wake executes the ONE registered test after flags/current-state check.
No result,measurement,completed-control pass or new theorem claimed.
MI328/329 keep their independent pending-read statuses.13min ACTIVE.


### MI332 — B163 outcome: the exact-spectrum criterion survives its fixed test (2026-10-17 19:54 BST)

**FINITE COMPUTED,single-party;general statement OPEN.** ONE
MI331 invocation of the unchanged source committed at14102b2b.
Source SHA256 fae8f9ec9e0ea5b911d289b1e96978985d408cdf0d323e01a614291bd22b220a.
No new Cloud flags;current main fetched once/merged before execution.
All registered controls complete and pass:no missing invocation,
post-failure patch,rerun,cap increase or expanded domain.

| Sizes | Holes | Rank-feasible vectors | Also individually feasible | Jointly realized |
|---|---:|---:|---:|---:|
| 3,3,3 | 10 | 3250 | 3184 | 3184 |
| 3,3,4 | 11 | 5123 | 5045 | 5045 |
| Total | 21 | 8373 | 8229 | 8229 |

Counts distinguish hole/size domains;they are NOT counts of distinct
vectors after forgetting the domain. Exactly144 rank-feasible vectors
fail individual spectra;ALL remaining8229 have literal witnesses.
Whole attainable-vector sets agree between combination/complement
and token-owner recursion;multinomial counts and every literal
partition check pass. Whole reflection maps and endpoint full-interval
MI295 controls pass. Rank-only q3,(4,18,20) is rejected by spectrum
and partition tests;the size2(2,6,8) countercontrol passes both
hypotheses and is correctly rejected by both partition instruments.

Resource report:0.447717 aggregate processCPU seconds,
0.4510513109853491 processwall,0.5080888019874692 externalwall,
15,597,568B peakRSS,exit0,no watchdog timeout,2087B stdout,
0B stderr. All within preregistered caps. Raw retained locally at
`/tmp/math-instinct-b163-one-hole.stdout`,stderr/receipt adjacent.
Stdout SHA256 c0acadca48a53012448e4bfe31884c60fca76a8230e0cb31b8058a416b255731;
empty-stderr SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
No raw portal upload. Niggle sweep:exact singleton membership is
independent of simultaneous compatibility;pair bounds explicitly
checked,not omitted;reflection keeps labels and changes sums by
M*c_i-s_i;both domains completed. No universal existence statement,
new proof status,or SS3/E28/L8 conclusion follows from this pass.

Gut:pull toward understanding why the individual exceptions suffice
here,not toward adding another size. Reasoned:the criterion survives
this falsifier and earns a hand construction attempt;the infinite
quantifier is untouched. MI333 identifies the next precise region.


### MI333 — B163 hand reduction: the one-hole question's remaining interior (2026-10-17 19:54 BST)

**Unreviewed hand reduction/background,not a new proof filing.**
Record searched:`one.hole|punctured` AND `spectrum|spectra|tight|gap`:
32 hits/16 files;MI304/329 and PRIOR-ART's known full-interval
spectra are relevant. Splitting an r-subset by its number k above
the hole yields exact intervals. Their successive gap size is
1-(l-1)(q-l)-k(M-q-k-1),l=r-k. For2<=r<=M-2 this is positive
ONLY at the first/last exceptional corners:q=r deletes minimum+1,
and q=M-r deletes maximum-1. Full derivation is filed as background
in PRIOR-ART.md,not represented as a sourced novel theorem. Thus
our proposed singleton condition is explicit:exclude these at most
two actual sum holes per bin,not an unspecified subset-sum oracle.

There is also a direct completion when some bin A is at its actual
MINIMUM rank sum. It must take the a smallest pool values. If q<a,
its removal leaves a full interval;the two remaining bins complete
by their interval spectrum,with residual bounds supplied by the
original singleton/pair rank bounds. If q>=a,A=0..a-1. Translate
the remainder down a:it is0..M-a minus(q-a),with remaining sizes
b,c>=3. The same original rank bounds put B's target inside this
remainder's actual spectrum interval. The ONLY possible holes are:

- q-a=b and B's residual target=its minimum+1. Then q=a+b=M-c,
  and C's original target is its global maximum-1,which the
  assumed ORIGINAL singleton spectrum condition already excludes.
- q-a=c and B's residual target=its maximum-1. Then q=M-b,
  and B's own original singleton spectrum condition excludes it.

Therefore no residual gap survives,and a B subset exists;its
complement supplies C. Reflect values to cover an exact MAXIMUM.
This is an elementary face reduction,not a carrying-review request
or an assertion of the general one-hole theorem. The hand argument
has no independent verification;MI332 did not test arbitrary sizes.

**What changed,next inference.** A counterexample to the proposed
criterion,if it exists with all sizes>=3,must be strictly inside
EVERY actual singleton rank bound (and hence every complementary
pair bound). The remaining task is a simultaneous interior selector,
not proving that each sum exists separately. Do NOT fix one bin
arbitrarily and assume its punctured complement completes,or invoke
fiber connectivity to presume a target partition. Next cheap hand
approach:use the single missing unit-gap explicitly while keeping
all three bins free;seek a constructive interior augmentation or a
hand obstruction. No automatic census,larger-domain run or new
routine review queue. Existing MI328/329 reads remain pending.

Gut:the geometric question is still interesting on a fresh choice;
repeating the census would feel administrative. Reasoned:finite
agreement plus a precise interior remainder merits the next hand
block,not an upgrade to PROVED. Niggle sweep:the subset-spectrum
formula excludes r1 and complement1;both deleted sums checked on
P={0,1,3,4};rank bounds are always for the actual pool;the minimum
bin is forced,not freely frozen;the maximum case uses reflection.
13min ACTIVE,SS3/E28/L8 OPEN.


### MI334 — B164: all larger errors reduce;the unresolved step must use a third token (2026-10-17 20:14 BST)

**Hand PROOF-SKETCH of a reduction,not the one-hole theorem;no new
experiment or carrying-read queue.** Pull:the single missing value
creates exactly ONE adjacent-rank gap of size2,so the verified MI295
mechanism might still clear all larger errors. Unease:do not confuse
a bin path with compatible physical witnesses again. Record searched:
`one.hole|punctured|missing.*token|hole.*owner` AND
`interior|selector|induction|three.bin`:23 hits/10 files;then
`unit.error|error.*2|weighted.*(edge|path)|gap.*2|rank.adjac` AND
`one.hole|punctured|three.bin|MI295`:13 hits/8 files. MI295's actual
carrying proof and MI333's spectrum derivation are the starting points.
This is a gap-sensitive extension of an existing mechanism;novelty
unassessed. No invocation of MI328/329 or assumed target partition.

**1. Larger-error reduction.** Let P={0,...,M} minus{q} be assigned
to THREE nonempty bins of prescribed sizes. Targets total sum(P)
and obey actual minimum/maximum rank bounds for every bin union.
Write d_i=current sum_i-target_i,E=sum|d_i|. Then EVERY E>=4
partition permits at most TWO swaps of adjacent RANKS in P that
never increase E and decrease it by at least2. Consequently some
partition has E<=2. Counts>=3 and individual-spectrum feasibility
are NOT needed for this reduction.

Orient an edge i->j if i owns the higher and j the lower member
of an adjacent-rank pair. Its weight is their value difference:
1 except possibly the unique gap2. If no positive bin reaches a
negative one,let R be all bins reachable from all positives. It has
d_R>0,no negative bin,and no outgoing edge. Its tokens are therefore
the FIRST C_R ranks of P. Their target sum would be below their
actual minimum,contradicting the assumed rank bound. This uses the
pool's ranks,not the full-interval formula L(C_R) across a deletion.

Choose a shortest positive-to-negative path. Any intermediate bin
has deviation0,otherwise its prefix/suffix shortens it. A direct
weight1 edge reduces E. A direct weight2 edge does too unless BOTH
endpoint deviations are+1,-1. With three bins that exception has
third deviation0 and E2,excluded here.

The remaining path is A->B->C with deviations(D,0,-D),D>=2.
Let a be the weight of A->B and b that of B->C. The only possibilities
are(a,b)=(1,1),(1,2),(2,1):there is only ONE physical gap2 edge.
If the witness pairs are disjoint:

- (1,1):swap A->B then B->C;final deviations(D-1,0,-D+1).
- (1,2):same order;final(D-1,-1,-D+2).
- (2,1):swap B->C first,then A->B;final(D-2,1,-D+1).

In every case the first step is neutral and the final E drops>=2.
If they overlap,the shared token is B and the adjacent-rank triple
has labels C B A at values z0<z1<z2,with z1-z0=b,z2-z1=a.
The second swap must use its CURRENT owner,as follows:

- For(1,1) or(1,2),swap the high pair then the low pair.
  CBA becomes ACB,and final deviations are(D-a-b,a,-D+b).
- For(2,1),swap the low pair then the high pair.
  CBA becomes BAC,and final deviations are(D-a,-b,-D+a+b).

For D2 the exceptional weighted cases give respectively(-1,1,0)
and(0,-1,1),both E2. For D>=3 the displayed absolute values also
give a decrease>=2. The first swap always has weight1 between a
defect and the neutral bin,so is neutral. This exhausts every
shortest-path case. Repetition terminates at E0 or E2 without
assuming E0 exists. At most the INITIAL E swaps suffice for this
limited conclusion;no claimed bound for finishing the last unit.

**Literal weighted-overlap control.** On P=0..9 minus3,take
A={0,4,8},B={2,5,9},C={1,6,7},targets(10,16,16).
Deviations(2,0,-2),and the triple1C,2B,4A has(a,b)=(2,1).
Swap B2/C1,then A4/C2;the result is
A={0,2,8},B={1,5,9},C={4,6,7},deviations(0,-1,1).
Errors4,4,2;all tokens used once. Reflection x->9-x and A<->C
checks the opposite weighted orientation. No numerical run here.
Unexpected limit:rank-feasible targets(4,18,20) on this same pool
have partition(012;459;678) at E2 and no E0 because4 needs013.
Thus the reduction cannot be iterated past E2 without a new argument.

**2. A direct gap forces a reverse ordinary BIN path.** Now suppose
E2 has positive bin A at q+1,negative bin C at q-1,and neutral B.
If all three requested sums are individually feasible,there is a
C->A path using ONLY actual consecutive-value pairs (weight1).
Proof:otherwise let R be the bins ordinarily reachable from C.
It contains C,not A,and is downward-closed separately in the two
intervals0..q-1 and q+1..M. Since their last low token is in C
and first high token is in A,R occupies EXACTLY the low interval.
If R={C},C has size q,current minimum L(q),target L(q)+1.
The unique way to raise the minimum q-subset by1 uses the missing
value q,so this violates C's individual spectrum. If R={C,B},
A occupies the entire high interval,has size M-q,and its target
is its maximum-1,again impossible without q. Contradiction.

This is reachability,NOT a simultaneous lift. If a reverse path's
witnesses are disjoint from the gap pair AND from each other,swap
the gap first (neutral,flipping the two signs),then follow that
ordinary path;the last swap gives E0. Shared witnesses remain open.

**The minimum-size condition is still unspent,and that matters.**
The known size2 negative on P={0,1,2,3,4,6},targets(2,6,8),
already survives both reductions. Take current bins(02;14;36):
deviations(0,-1,1). Gap4B/6C is a direct positive-to-negative
edge. There IS an ordinary reverse B->C edge3C/4B,but it shares
the gap's token4. Swapping the gap destroys that reverse witness.
All individual sums are feasible,and all rank inequalities are
strict;nevertheless2 forces02 and8 forces26,sharing2. Therefore
neither this reverse-path lemma nor strict interior alone solves
compatibility. A proof for sizes>=3 must explicitly exploit the
additional token;it has not appeared in steps1 or2.

**90-minute reflection and next inference.** The periodic reflection
is due here (previous B157 reflection18:37 BST). The pull is specific
to the one exceptional weight2 edge;the arithmetic reduction is
interesting on a fresh choice. Frustration is also real as a steering
signal:physical witness collision keeps returning. The whole one-hole
problem has NOT been solved,and more reachable-bin diagrams would
be momentum. Next bounded hand test:can the size2 collision be
preserved when every bin has a third token in a one-hole interval,
or does that force a GLOBAL release? Keep all tokens available;
no new local-module catalogue or automatic graph census. If the next
block merely restates the same collision without spending the third
token,change to the fixed-first-sum/attainable-second-sum representation
rather than repeat adjacent relays. No seeded draw or forced lemma.

Gut:renewed interest in the concrete gap calculation,not a blanket
claim of warmth. Reasoned:a real reduction to the last unit,with an
explicit negative control showing exactly why the remaining inference
is not established. Full criterion remains OPEN. Niggle sweep:rank
closure uses actual ranks;shortest-path intermediate0 is justified;
a=b2 excluded by one physical gap;both overlapping orientations
use current owners;D2 overshoot included;individual feasibility used
only in step2;reverse path versus physical lift kept distinct. This
unreviewed step would need independent verification as part of a
completed one-hole proof,not a separate routine carrying-read job.
MI328/329 retain their pending statuses.13min ACTIVE.


### MI335 — B165: the third-token test redirects to a global first-bin choice (2026-10-17 20:30 BST)

**Hand construction/reduction;general one-hole criterion still OPEN.**
Record searched:`third.token|size2|two.token|padding|padded` AND
`one.hole|MI334|singleton.*spectrum|2,6,8`:10 hits/5 files. Then
`least.slack|closest.*extrem|prefix.*pivot|end.support|smallest.slack`
AND `partition|bin|prescribed|one.hole`:8 unrelated hits/6 files.
MI333's spectrum calculation and PROVED MI295 are the mathematical
sources. Bounded primary-web search found no imported integer theorem;
a binary-vector matching paper is scope-noted in PRIOR-ART. No new
experiment,Markov-basis job or larger census.

**The padding kill test.** A large third bin alone does NOT release
two small colliding bins. On P={0,...,M} minus{3},M>=7,
sizes(2,2,M-4),targets(4,4,T-8),T=sum(P),satisfy all actual rank
bounds STRICTLY and each target is individually feasible. Both pair
bins have the UNIQUE realization04,so joint completion is impossible.
The big bin's individual witness is P minus{0,1,2,5},whose excluded
four-set sums8. Its target is one below its maximum T-7;it is above
its minimum because the largest four sum4M-6>8. Pair targets4 lie
strictly between1 and2M-1;all other bounds are complements. Thus
an arbitrarily large neutral buffer does not fix a local scarcity.
This is NOT a minsize3 counterexample,and it is a route test,not a
new proof/review contribution. By contrast,the simple all-three-bin
padding of the old(2,6,8) instance gives P=0..9 minus5,targets
(9,14,17),and has literal partition(018;239;467). The extra values
are reassigned,not kept in their original padding roles. Neither
example proves a universal third-token release.

The requested global minsize3 repair was NOT obtained. As promised
at MI334's reflection,I stop pursuing another adjacent-relay case
tree and change representation:choose a first bin so that the other
two targets stay rank-feasible,then inspect their scalar subset sums.
The following observation is the actual new leverage in this block.

**A least-slack singleton protects ALL residual rank bounds.** This
works for ANY ordered pool P of distinct values,not just one hole.
Let alpha(t) be its least t-value sum,beta(t) its greatest,together
with total T. Targets total T and obey their actual rank bounds.
Choose the least of all SIX singleton lower/upper slacks. Reflect values if necessary so selected bin A,size a,has
s_A=alpha(a)+h,and the other bins B,C have upper slacks>=h.
Let their sizes be b,c,so a+b+c=|P|. Conservation gives

  s_B >= T-alpha(a)-h-(beta(c)-h)
       = alpha(a+b)-alpha(a),
  s_C >= alpha(a+c)-alpha(a).

For ANY subset A of size a and sum s_A,the least b tokens in
R=P minus A sum AT MOST alpha(a+b)-alpha(a):deleting any a
values cannot raise the least b survivors beyond ranks a..a+b-1.
The same holds for c. Consequently the displayed target lower
bounds imply BOTH residual lower bounds,and s_B+s_C=sum(R)
gives both residual upper bounds. No compatible B subset is assumed.
Individual feasibility of the selected s_A supplies some A;the
problem is still to select one whose actual B spectrum contains s_B.
This elementary observation is unreviewed,not a solved partition
criterion. In three bins,rank inequalities and subset availability
can now be separated without arbitrarily freezing an unsafe bin.

**A short proof of an already established theorem.** On a FULL
interval,choose A as l smallest values,k largest values and one
pivot,l+k=a-1. As k increases,the pivot-sum ranges meet exactly
and cover the whole a-subset sum interval. R is an interval minus
one value. Its only possible subset-spectrum gaps are minimum+1
or maximum-1 (MI333). The least-slack inequalities above rule out
these gaps by margin(k+1)b>=2,or the corresponding c margin.
This reproves MI295's EXISTENCE conclusion for all sizes>=2;
it does not reproduce its four-swap algorithm. Full argument filed
PRIOR-ART.md as "known,reproved here",with the alternative proof
unreviewed and no novelty claim/new PROOFS entry/review request.
Delight here is at a simpler explanation of the existing result,
not at having solved the new one-hole problem.

**The one-hole pivot issue and an explicit repair.** For the actual
P=0..M minus q,use the a-1 extremal VALUES of P,not ranks treated
as unpunctured integers. For each k,l=a-1-k,pivots range between
the first/last remaining values. The MIN/MAX sum intervals for
successive k meet at the same extremal set;their union covers
[alpha(a),beta(a)]. Each pivot interval can miss only the value
q plus its fixed extremal sum. Thus an individually feasible s_A
is realized either by this recipe,or by a FORMAL recipe whose
pivot would be q. The latter is not a legitimate chosen subset.

When the pivot is q,the formal low prefix is0..l-1 and high suffix
u..M,u=M-k+1. If k>0 and u-q>=3,replace the formal pair{q,u}
by{q+1,u-1}. If l>0 and q-(l-1)>=3,replace{l-1,q} by
{l,q-1}. These preserve size and sum;the two new values are
available,distinct and not already chosen. At least one repair
exists when the remainder has size b+c>=6:
- If l,k>0,the two distances sum M-a+3>=9,so one is>=3.
- If l0,the unrepairable distances1 or2 would make s_A respectively
  exceed its actual maximum,or equal the forbidden maximum-1 with
  q=M-a. Individual feasibility excludes both. The k0 case is the
  reflected minimum/minimum+1 argument.

An unrepaired legal recipe leaves R as an integer interval with
at most TWO holes (the original q and the selected pivot). A high
repair leaves precisely[l,u] minus{q,q+1,u-1};the low repair is
its reflected shape. Hence one or two explicit repaired choices
suffice to produce a LEGAL first bin with this structured remainder.
Their residual rank bounds hold automatically by least slack.
We have NOT proved that either remainder realizes s_B. Legal and
rank-feasible boundaries still need actual scalar subset spectra.

**Hand control that kills the uncorrected recipe.** P=0..9 minus3,
sizes3^3,targets(20,11,11). A is uniquely closest to a singleton
extreme:upper slack4,others' smallest slack8. The three uncorrected
end-supported possibilities require pivots19 with01,11 with09,
or3 with89;none is available. The high repair takes formal389
(which contains the missing3) to479. Then R=012568;B056 and C128
both sum11,so the repaired partition is literal. This control rules
out silently assuming the one-pivot recipe always exists even after
choosing the correct first bin.

**What changed and next inference.** The swap path picture has not
closed its shared-token step. The new GLOBAL selection removes the
residual-rank issue for every first-bin realization,and provides a
shorter explanation of the verified base theorem. For one hole,the
remaining problem is one-dimensional:show a suitable actual subset
sum in an interval with two holes,or in the structured three-hole
repair family,using the original least-slack inequalities and sizes
b,c>=3. Or find a hand counterexample to that CANONICAL recipe;
such a failure would reject the recipe,not the original criterion.
No asserted two-choice completion theorem or coefficient nonvanishing
has been smuggled in. Next cheap hand work is the exact spectrum and
margin question for these pools,not another placement family/census.

Gut:the physical-collision line cooled;the global choice inequality
and simpler old theorem brought a specific renewed pull. On a fresh
choice I would pursue that scalar spectrum question;I would not
continue cataloguing reverse relays. Reasoned:this is a genuine
change of representation with a proved-looking selection step,but
the final compatibility inference is open and every new argument
here is single-party. Niggle sweep:reflection applies to sums AND
pool;all six original slacks compared;min survivors use ranks of
P;the current one-hole pivot may be absent;both repair endpoints
checked;the large-buffer negative still has two size2 bins;alternate
proof asserts only MI295's old existence conclusion. No new formal
review queue;Cloud gets the changed question and committed pointer.
13min ACTIVE,SS3/E28/L8 OPEN.

### MI336 — B166: two-hole spectra and the legal-pivot branch (2026-10-17 20:43 BST)

**Hand PROOF-SKETCH;no experiment or independent carrying read.**
Question:does MI335's least-slack first-bin recipe leave the requested
scalar sum? A proof would complete one branch of the one-hole
three-bin selector;failure would reject that recipe,not SS3 or the
refined criterion. Record searched:`two.hole|three.hole|punctur|least.slack`
AND `spectrum|subset|MI335`:13 hits/3 files. MI333's exact one-hole
spectrum and MI335 are the sources. This is a direct derivation;
no literature-novelty/completeness assertion,new census or review job.
The concrete pull is the separation of rank safety from scalar gaps.
Kill test:look for an allowed target at an actual remainder gap.
Unexpected check:drop ONE residual cardinality to2,testing whether
three tokens are used rather than mentioned. Stop at the two-hole
branch;do not silently import its result into three-hole repairs.

**Two-hole spectrum calculation.** Let R be an integer interval
with two values deleted,r+c=|R|,r,c>=3. Every r-subset sum between
its actual minimum and maximum occurs EXCEPT possibly minimum+1,
minimum+2,maximum-1,maximum-2. Here is a hand derivation,including
end slices;convex-hull bounds alone would not prove it.

Normalize the interval to0..U. An endpoint hole can be trimmed,
reducing to MI333. For separated internal holes q<v-1,v,put
p=v-1 and u=U-v:the low pool0..v-1 minus q has p values;
the high full interval v+1..U has u values. For k high tokens
and l=r-k low tokens,the sum-range endpoints are

  a_k=L(l)+(l-q)_+ +k(v+1)+L(k),
  b_k=l(v-1)-L(l)-(l-v+1+q)_+ +kU-L(k),

where L(t)=t(t-1)/2 and x_+=max(x,0). Whenever0<k<u,
the high subset spectrum is an interval of width k(u-k)>=1.
The low spectrum,by MI333,misses at most isolated single integers:
this also holds for low size1 or complementary size1,where it is
literally a punctured list. Adding an interval of width>=1 fills
those isolated omissions. Thus every INTERIOR k slice is full.
Both a_k and b_k strictly increase with k. For consecutive legal
slices,with d=v-l>=1,the separating gap length before filling is

  G=a_(k+1)-b_k-1
   =1-(l-1)d-k(u-k-1)+(l-1-q)_+ +(q-d+1)_+.

Because1<=q<=v-2,the last two terms sum to at most l-1.
Hence G<=1-(l-1)(d-1)-k(u-k-1). A positive G requires
l=1 or d=1,and k=0 or k=u-1. The r=1/c=1 corners are
excluded. The remaining corners are k0,l=p=r (a gap at global
minimum+1),and k=u-1,l1,r=u (global maximum-1).

The nonfull END slices need a separate check. At k0,if p-r>=2,
MI333 gives only a low minimum+1 and/or low maximum-1 gap.
The former is global minimum+1. For the latter q=p-r=d-1,
G=1-(r-1)d+(r-d)_+<=-2,so k1 already covers it.
If p-r=1,put v=r+2>=5 and B=b_0. The sole low omission is
B-q,and a_0=B-(v-1). Direct substitution gives

  a_1=B+4-v when q<=v-3;
  a_1=B+5-v when q=v-2.

Thus every such omission is covered by k1 except possibly
q=v-3 or v-2,at global minimum+2 or minimum+1. If p-r=0,
k0 is a singleton and the preceding adjacent-gap calculation applies.
At k=u write l=r-u,so p-l=c>=3. For l>=2,the low maximum-1
omission is global maximum-1;the low minimum+1 omission requires
q=l and is covered by k=u-1 because
G=1-lc+(l-c+1)_+<=-2. For l1,writing H=sum(all high values),
the only omission is H+q,while the preceding maximum equals
H+v-4 for q<=v-3,and H+v-5 for q=v-2. Only q=v-3,v-2
can survive,at global maximum-2 or maximum-1. For l0,the last
slice is a singleton and the adjacent-gap calculation applies.
These calculations also cover cases where k0 or ku is not legal:
there is then no corresponding end slice to inspect.

For consecutive internal holes q,q+1,the two blocks are full.
All fixed-k slices are complete,and the gap formula is

  G=2-(l-1)(q-l)-k(u-k-1), u=U-q-1.

Positive G needs the two products to sum0 or1. Sum0 leaves only
the first/last corners after r1/c1 are excluded,so omissions are
within2 of an extreme. Sum1 would force either l2,q3 with k0
or u-1,or k1,u3 with l1 or q. Each gives r2 or c2,excluded.
This proves the claimed two-hole localization in every case.

For later use,the exact lower-edge omissions have a particularly
short description. Write sorted R=z_0<...<z_(n-1),and
w_i=z_i-z_(i-1). Minimum+1 is absent iff w_r>=2.
Minimum+2 is absent iff w_r=3,or w_r=1 and
w_(r-1)=w_(r+1)=2. Indeed an increment<=2 can use only one
rank step,two steps by the last selected token,or one step each
by the last two selected tokens. Their costs are w_r,
w_r+w_(r+1),w_(r-1)+w_r. Complementation gives the upper edge.
No additional holes can hide away from these four positions by
the preceding slice calculation.

**Hand controls and a real recipe failure.** For R={0,1,3,4,6,7},
r3,the twenty triples have distinct-sum set
{4,5,7,8,9,10,11,12,13,14,16,17}:the gaps6,15 are exactly
minimum+2/maximum-2. On the original P=0..9 minus7,take
sizes3^3,targets(5,12,21),total38. All singleton rank intervals
are[3,23],their lower/upper slacks are(2,18),(9,11),(18,2).
Each target is individually feasible:023,156,489 respectively;
they also form a literal partition. But the least-lower-slack bin's
end-supported choice A=014 leaves R=235689,whose triple sums
are the displayed set shifted6. It misses BOTH12 and21.
So the UNMODIFIED legal-pivot recipe is false,even with all original
tests and minsize3. This is not a counterexample to the criterion.

The unexpected cardinality check is R={0,1,2,5,6,7},r2,c4.
Its pair sums are{1,2,3,5,6,7,8,9,11,12,13};gaps4,10 are
THREE units from the extrema. The two-hole localization would be
false if one replaced r,c>=3 by r,c>=2. The extra token has now
entered an actual carrying calculation:the product=1 corners above.

**Completion of the legal-pivot/TWO-INTERNAL-HOLE branch.** Use
MI335's notation:original P=0..M minus q,A consists of l low
values,k high values and actual pivot p,where l+k=a-1. Assume
both q and p are INTERNAL to the remaining integer span;endpoint
and one-hole remainders are not needed for the argument below.
Then the prefix is0..l-1,the suffix starts M-k+1,and
R=[l,M-k] minus{q,p}. The least-slack argument gives

  s_B>=F_b=alpha(a+b)-alpha(a),
  s_C>=F_c=alpha(a+c)-alpha(a).

Let z_j be the values of the ORIGINAL P in increasing rank order.
The least b values of R are bounded above by z_(l+1),...,z_(l+b)
(deleting only one pivot after the low prefix). Meanwhile F_b sums
z_(l+k+1),...,z_(l+k+b). Thus F_b-min_b(R)>=kb,and similarly
for c. If k>=1,these margins are>=3,so the two-hole calculation
excludes every possible missing B sum,including upper omissions
by using C and complementation. A completing B therefore exists.

It remains k0. Then a=l+1,z_l=l,and,putting p'=p-l,

  F_b-min_b(R)=min(p',z_(l+b)-l)>=min(p',b).

The analogous identity holds for c. Thus a residual lower-edge
omission can matter only for p'=1 or2. If p'=1,minimum+2
cannot be a two-hole omission when b>=3,by the w description.
Minimum+1 requires q-l=b+1;then h=1,F_b=min_b(R)+1 and
the original C upper slack is1 with q=a+b=M-c. MI333 says
this original C target is individually IMPOSSIBLE,contradiction.
If p'=2,only minimum+2 could matter. Its w characterization
forces b3,q-l5:the alternative consecutive-hole boundary would
require b2. This is the exact exception found by the control.
The same analysis for C handles upper-edge B omissions.

There is a uniform repair of this remaining exception. In absolute
values q=a+4,the chosen A is{0,...,a-2} union{a+1},
s_A=L(a)+2,and the problematic triple target is s_B=3a+3.
Replace A by

  A*={0,...,a-3} union{a-1,a},
  B*={a-2,a+2,a+3}, C*=P minus(A* union B*).

A* has size a and sum L(a)+2;B* has size3 and sum3a+3.
They are disjoint,avoid q,and all values are in P because c>=3
and M=a+3+c. Conservation supplies exactly C's target and size.
If C was the problematic triple,interchange B,C. No pre-existing
joint realization is assumed. For the literal control,this is
023/156/489. This repairs the exceptional branch globally,not by
freezing a buffer or requesting a separate local-module census.

**What changed and what is NOT done.** The original end-supported
recipe is falsified,and its two-internal-hole legal-pivot branch
now has a hand completion argument with one uniform exceptional
repair. The important unsolved branch is the MISSING formal pivot:
MI335 then leaves[l,u] minus{q,q+1,u-1},or its reflection.
A two-hole spectrum bound cannot be applied to THREE holes.
The full one-hole criterion,full four-bin SS3,E28 and L8 remain
OPEN;no status is upgraded by this single-party derivation.
Next cheap test:derive the structured-three-hole scalar spectrum
and compare its possible gaps with the repaired first-bin margins.
No larger run is justified merely by this partial progress.

Gut:surprise at the legal recipe's tiny failure,then specific delight
at its exact pattern and a uniform replacement. I would choose this
scalar question afresh;the gaps now explain why minsize3 matters.
Reasoned:one remaining branch has been isolated more sharply,with
an explicit negative control and carrying algebra,not a complete
solution. Niggle sweep:fixed-count intervals vs their actual spectra
separated;both end slices checked;both holes internal hypothesis
stated;rank comparisons use original z;C covers upper omissions;
the counterexample has a compatible full partition;repair preserves
cardinalities and both moments without presupposing that partition;
size2 falsifies the overgeneralization;three-hole case kept OPEN.
All new claims PROOF-SKETCH/unreviewed;no routine carrying-read
request. MI328/329 existing requests remain pending.13min ACTIVE.

### MI337 — B167: structured three-hole completion and a full one-hole candidate (2026-10-17 20:51 BST)

**PROOF-SKETCH: complete candidate,independent verification PENDING.**
No experiment,no claim of literature novelty,and no full four-bin
SS3/E28/L8 solution. Record searched:`three.hole|structured.*hole|two.hole`
AND `spectrum|subset|MI336`:8 hits/2 files. Carrying sources are
MI333,MI335 and MI336,read before this block. A bounded three-query
primary-literature search returned the already recorded
[Hoory-Kotlar equal-sum work](https://arxiv.org/abs/2605.06071)
and related constant-sum partitions;no exact one-hole theorem was
identified. That is NOT FOUND in this search,not a theorem of absence.
No new external mathematical result is imported.

The pull is specific:the structured three-hole pool is not an
arbitrary punctured interval. Prediction before the hand calculation:
splitting at its adjacent holes may expose full count-slices,with
only edge exceptions. Kill test:an actual requested sum at an
exception allowed by the original least-slack inequalities. Unexpected
check:replace the structured holes by three consecutive INTERNAL
holes;do not generalize merely from their number. Stop after a
complete branch argument or an explicit gap;no automatic experiment.

**1. Exact structured spectrum.** Let

  R={0,...,V} minus{p,p+1,V-1},
  u=V-p-2>=1, n=p+u=V-2=r+c, r,c>=3.

Thus R consists of p low values0..p-1 and u high values
p+2,...,V-2,V. The exact r-subset spectrum fills its actual
minimum/maximum interval apart from these possible omissions:

  minimum+1,minimum+2  if r=p;
  maximum-1,maximum-2  if r=u;
  minimum+3            if u=4 and c=3;
  maximum-3            if u=4 and r=3.

Only legal r,c>=3 cases in this list apply. No other gap occurs.
For p0,the pool is a translated one-hole pool missing its penultimate
value;MI333 gives no gaps at these sizes. For u1,the pool is a full
low interval plus one high value;the two slice ranges overlap as
shown below. Assume p>=1,u>=2 for the main calculation.

Split an r-subset by k high tokens,l=r-k low tokens. Write
L(t)=t(t-1)/2. The sum-range endpoints are

  a_k=L(l)+k(p+2)+L(k)+1_(k=u),
  b_k=l(p-1)-L(l)+k(V-1)-L(k)+1_(k>0).

In the high pool,MI333 gives a full k-subset interval except for
maximum-1 at k1,and minimum+1 at k=u-1. This remains literally
true for high size1/complementary size1;for u2 these coincide.
Low subset sums form an interval of width l(p-l). If0<l<p,
its width>=1 fills that isolated high omission. So every slice is
FULL except possibly k1,l=p and k=u-1,l0:the other l0/p
combinations force r1 or c1. A missing entire slice cannot be
inferred by using only its endpoints;these are the actual exceptions.

Both a_k,b_k strictly increase. For consecutive legal slices,
with A=(l-1)(p-l),the separating gap expression is

  G=a_(k+1)-b_k-1
   =2-A-k(u-k-1)+1_(k+1=u)-1_(k>0).

For0<k<u-1,this equals1-A-k(u-k-1)<=0.
At k0 or k=u-1 it is2-A. At k0,r=l>=3,
positive G requires p=r:if p-r>=1,then A>=2.
This produces exactly the first two global gaps. At k=u-1,
the complement condition gives p-l=c-1>=2,so positive G
requires l1,r=u,producing exactly the last two global gaps.
For u1,there is only the join k0->1,G=3-A;here r>=3
and p-r=c-1>=2 imply A>=4,so the ranges overlap.

Finally inspect the two possibly nonfull slices. If k1,l=p,
then r=p+1,c=u-1>=3,so u>=4. Its maximum-1 hole is
covered by slice k2 when u>=5,because a_2-b_1=4-u<=-1.
For u4,a_2=b_1,so it survives at GLOBAL minimum+3.
If k=u-1,l0,then r=u-1>=3,c=p+1>=3. The previous
slice satisfies a_(u-1)-b_(u-2)=4-u. It covers the
minimum+1 omission when u>=5;at u4 the omission survives
at global maximum-3. These are exactly the listed conditions.
There is no corresponding end slice when its k is illegal.
This proves the full structured spectrum calculation by hand.

Control:R={0,1,4,5,6,8},p2,u4,r=c3,has spectrum
{5,6,7,9,10,11,12,13,14,15,17,18,19},missing8,16 at
edge distance3. Unexpected check:R={0,1,5,6,7,8} (delete2,3,4)
has spectrum{6,7,8,9,11,12,13,14,15,16,18,19,20,21};
its omissions10,17 are FOUR from the extrema. The structure
of the holes,not merely their number,is essential.

**2. High missing-pivot repair always completes.** Return to
original P=0..M minus q,three sizes a,b,c>=3. Let alpha(t)
be the least t-value sum. Choose the least of all six singleton
slacks,and reflect the ORIGINAL problem once if necessary so
A's target is s_A=alpha(a)+h. As in MI335,for r=b and r=c,

  s_r>=F_r=alpha(a+r)-alpha(a).

ANY actual first bin of size a and sum s_A leaves these two targets
inside their residual rank intervals. This does not assume joint
feasibility. A formal prefix/suffix/pivot construction with missing
pivot q has prefix0..l-1,suffix u0..M,where
l+k=a-1,u0=M-k+1. If k>=1,u0-q>=3,the high repair
replaces{q,u0} by{q+1,u0-1},leaving

  R=[l,u0] minus{q,q+1,u0-1}.

After shifting by l,this is section1 with p=q-l and
u=V-p-2. The only LOWER-edge omissions for an r-subset are:
(i) distances1/2 if r=p; (ii) distance3 if r=p+1 and the
other size is3,u4. Upper B omissions are lower C omissions by
complementation,so it is enough to exclude those lower cases.

Let z_j be original P's values in rank order. Because k>=1,
a=l+k+1>=l+2. Thus F_r=sum(z_a,...,z_(a+r-1)) is at
least the sum starting at rank l+2. In case(i),q=l+r,
the residual minimum is rl+L(r),while that rank segment sums
rl+L(r)+2r+2. Its margin is>=2r+2>2. In case(ii),
q=l+r-1,the residual minimum is rl+L(r)+2,while the
same rank segment sums rl+L(r)+2r+3. Its margin is
>=2r+1>3. All displayed ranks remain inside P because the
other bin has size>=3. Hence neither lower omission can be
requested,and the scalar B sum exists. C is its complement.

**3. Low repair also completes;do NOT reflect the slack hypothesis
silently.** If l>=1,q-(l-1)>=3,the low repair replaces
{l-1,q} by{l,q-1}. The remainder is

  R=[l-1,u0-1] minus{l,q-1,q}.

It is a REFLECTION of the pool in section1,but the original
least-LOWER-slack choice was not reflected. Reflect the SPECTRUM
only,and check the original lower bounds directly. Put t=q-l.
The only lower-edge omissions of an r-subset are:
(i) distances1/2 when r=t-1; (ii) distance3 when t5,r3.
For(i),q=l+r+1,the residual minimum is L(r)+rl-1.
Since a=l+k+1>=l+1,F_r is at least the original rank segment
starting l+1,whose sum is L(r)+rl+r. The margin is>=r+1>2.
For(ii),the residual minimum is3l+2,and that rank segment
sums3l+6,giving margin>=4>3. Complementation excludes upper
omissions too. Therefore this actual repaired A also completes.
This direct check resolves the niggle that reflecting a construction
need not preserve the orientation of the selected least slack.

**4. Full candidate statement and coverage audit.**

For P={0,...,M} minus{q},a+b+c=M,a,b,c>=3,and integer
targets summing to T=sum(P),a simultaneous partition of those
sizes and sums exists IFF each target is INDIVIDUALLY realized
by a subset of its specified size. Equivalently,require each
actual singleton rank bound and exclude minimum+1 when q equals
that bin's size,and maximum-1 when q=M minus that size (MI333).
The rank bounds are redundant if exact individual feasibility is
already required. Necessity is immediate;the proposed sufficiency
is the following exhaustive construction. Status remains SKETCH.

- If q is an endpoint,P is a full interval up to translation;
  PROVED MI295 supplies sufficiency. Otherwise choose a globally
  least singleton slack and orient it lower,as above.
- MI335's end-supported recipes,for l+k=a-1,have pivot ranges
  whose endpoints meet at the same actual extremal set. Their
  convex intervals cover the entire target range. Each range can
  miss only its FORMAL missing pivot q. Thus the chosen target has
  either a legal pivot representation or a formal missing-pivot one.
- In the legal case,k>=1 gives residual lower margins>=kr>=3
  for r=b,c,by original rank comparison in MI336. The residual
  span has at most two holes,so its edge-distance<=2 omissions
  are all excluded. For k0 and two INTERNAL holes,MI336 completes
  unless p-l2,r3,q-l5;its explicit uniform repair supplies A*,
  the problematic triple and the complementary third bin.
- Here are the endpoint/one-hole cases not asserted by MI336's
  internal-hole branch. With k0,let v=z_l be the first middle
  value. If actual pivot p=v,A is exactly the least a values:
  MI333's tight-face argument applies. A possible residual
  minimum+1 would force the ORIGINAL complementary bin's forbidden
  maximum-1;the residual maximum-1 is the corresponding forbidden
  original target. If p is the upper endpoint,its deletion cannot
  affect the least r middle values,r<=b+c-3;the rank margin is
  at least r,excluding one-hole gaps. If the original hole is
  outside the residual span (including a trimmed endpoint),that
  span is a full interval minus p. Its minimum+1 omission requires
  p=v+r,and then F_r-min_r(R)=r>=3. Apply this also to C to
  exclude upper omissions. This exhausts the legal-pivot boundary.
- In the FORMAL missing case,the actual extremes are0..l-1 and
  u0..M. If l,k>0,the low/high repair distances sum
  q-l+1+u0-q=M-a+3=b+c+3>=9,so at least one is>=3.
  If l0 and the high distance is1,the formal target exceeds the
  actual maximum;distance2 gives its forbidden maximum-1 with
  q=M-a. If k0 and the low distance is1,the target is below
  its actual minimum;distance2 gives its forbidden minimum+1
  with q=a. Individual feasibility excludes these endpoint
  failures. Hence a legal high or low repair always exists.
  Sections2/3 prove that either available repair completes.

No step selects B by assuming that its desired partition already
exists. Its existence follows from the ACTUAL scalar spectrum,
then conservation supplies C. No four-bin hypothesis or numerical
agreement replaces a carrying inference. The size2 negative
P={0,1,2,3,4,6},targets(2,6,8),remains outside the theorem and
still impossible;minimum size3 is essential to this statement.

**What changed and next step.** There is now a COMPLETE hand
candidate for the one-hole three-bin criterion,assembled from
MI333/335/336 and the new structured spectrum. It needs a genuine
independent carrying read,including both spectrum proofs and the
endpoint coverage,not merely the examples. Send Cloud a committed
REVIEW-REQUEST for this combined candidate. This is a key review
moment,not a routine guard. Pending verification does not halt
independent work. Next useful independent question is what this
candidate would imply for four-bin SS3 when a singleton facet is
closest;state any such consequence conditionally until verified.
No new census or extension is authorized by numerical optimism.

Gut:surprise and delight at a full candidate after the representation
change;the warmth has a precise object,the slice joins and their
margins. Reserve celebration of a proved result for scrutiny.
Reasoned:every construction branch now has an explicit completion
argument,but no independent reader has checked these carrying steps
or the novelty question. Niggle sweep:low repair reflection would
flip slack orientation,so a direct margin proof was supplied;
end slices versus endpoint intervals kept separate;u1/p0 covered;
size2 control retained;canonical legal-pivot failure repaired;
formal pivot is never treated as a token;endpoint holes accounted
for;arbitrary three-hole generalization explicitly refuted. No
experiment,no proof status upgrade.13min ACTIVE.

### MI338 — B168: conditional four-bin coverage and the remaining joint boundary selector (2026-10-17 21:02 BST)

**Hand conditional consequence of MI337,not a verified SS3 theorem.**
Record searched:`closest.*(singleton|facet)|least.slack|pair.*slack`
AND `four.bin|SS3|MI337|MI335`:11 hits/3 files. Relevant sources:
MI305/CL434's verified boundary-window lemma,MI311's complete-spectrum
ceiling,and pending MI337. No new literature theorem imported and
no experiment. The pull is to find out exactly how much the new
candidate would change the four-bin target,without waiting for review
or treating a pending claim as fact. Kill test:do the original
inequalities actually protect ALL residual cuts,not just singletons?
Unexpected check:an arbitrary pair pool with the correct size/moment
may still miss a requested scalar sum. No new review request.

**1. A closest singleton facet would suffice,at any distance.**
On the FULL interval P=0..N-1,write L(t)=t(t-1)/2.
Four sizes c_i>=3 total N;targets total L(N). For every nonempty
proper index subset I,write C_I=sum(c_i:i in I),S_I=sum(s_i:i in I),
and lower slack h_I=S_I-L(C_I). Full SS means h_I>=0 for all14
cuts. The upper slack of I is exactly h_(I-complement).
Let h be the GLOBAL minimum of these14 lower slacks.

Suppose a singleton or its complement attains h. Reflect ORIGINAL
values/targets if needed,so A,size a,has s_A=L(a)+h.
For ANY nonempty proper group J of the other THREE bins,let K
be its nonempty complement among those three. The original upper
slack of K is h_(A union J)>=h. Therefore

  S_J =L(N)-s_A-S_K
      >=L(N)-L(a)-h-(U_N(C_K)-h)
       =L(a+C_J)-L(a)=F_(C_J).

For ANY actual size-a A-set realizing s_A,the least C_J values
of R=P minus A sum at most F_(C_J),by original rank comparison.
Thus EVERY residual lower cut holds;complementation gives every
upper cut. This is stronger than only checking each remaining bin.
It uses original PAIR cuts as well as singleton slacks.

Choose A by the full-interval prefix/suffix/pivot construction:
l+k=a-1,low prefix0..l-1,high suffix N-k..N-1,pivot p.
It realizes every s_A in its actual range (MI335),and R is an
interval with at most one hole. For a remaining bin of size r,
a residual minimum+1 omission would require p-l=r and
its target L(r)+lr+1. But the displayed bound for that singleton
is L(r)+ar,and (a-l)r=(k+1)r>=3. A residual maximum-1
omission is a minimum+1 omission for its TWO-bin complement J;
the same bound applies with C_J>=6. Thus every remaining target
is individually feasible in R,not merely rank-feasible.
MI337,IF correct,now partitions R into its THREE bins.

This covers the entire region in which a globally closest facet
is singleton/triple,including ties. There is NO small-slack bound.
A central hand control:sizes3^4,targets(16,16,17,17),N12.
Minimum singleton/upper slack is13;every pair slack is>=17.
Partition(0,5,11)/(1,6,9)/(2,7,8)/(3,4,10) is literal.
The application is not restricted to old boundary distances0..4.
This is a consequence of the pending theorem,not its verification
or a novel claim about the already checked finite n12 domain.

**2. The remaining strict pair-facet regime is precise.**
If the preceding case does not apply,a pair AB attains the global
minimum h,STRICTLY below every singleton/upper-singleton slack.
Orient it lower and write sizes a,b,c,d, m=a+b,n=c+d,
S_AB=L(m)+h. The complementary pair CD has upper slack h.
Define x=s_A-L(a),and z=U_N(c)-s_C. Conservation gives

  s_B=L(b)+ab+h-x;
  U_N(d)-s_D=cd+h-z.

Strict singleton comparison implies

  h<x<ab, h<z<cd;
  in particular 0<=h<min(ab,cd).

Do not discard the other original singleton and CROSS-PAIR
inequalities;these displayed bounds are consequences,not an
assertion that those other inequalities are redundant. A pair tie
with a singleton is already covered conditionally by section1.

Choose an actual size-m boundary pool P0 within0..N-1 with
sum(P0)=L(m)+h. Put Q0={N-1-v:v in P minus P0}.
Then |Q0|=n and sum(Q0)=L(n)+h. A full partition follows exactly
when P0 has an a-subset of sum L(a)+x AND Q0 has a c-subset
of sum L(c)+z. Reflection of the complement accounts for z;
no boundary is presumed to have both properties. This is the
remaining simultaneous selector,with the actual targets retained.

A tempting STRONGER sufficient question,not an equivalent theorem:
for all sizes>=3 and integer0<=h<min(ab,cd),can one choose P0
so that BOTH spectra contain the full central intervals

  Sigma_a(P0) contains[L(a)+h,L(a)+ab],
  Sigma_c(Q0) contains[L(c)+h,L(c)+cd]?

Such a choice would finish the strict pair regime uniformly in
x,z,and hence,conditional on MI337,the full four-bin statement.
It may be too strong:the original cross-cut bounds can restrict
which x,z occur. A counterexample to this uniform question would
reject the stronger recipe,not SS3. MI311's ceiling concerned FULL
actual spectra,not just these central target intervals;do not
misapply it as an obstruction to this different question.

**3. The arbitrary-boundary shortcut fails on a feasible target.**
Sizes3^4,N12,targets(10,10,23,23). Original singleton slacks
are at least7. The AB lower pair slack is h=20-L(6)=5;
its complementary upper slack is5;all cross-pair lower/upper
slacks are18. So this is genuinely a STRICT closest-pair case.
The actual candidate pool P0={0,1,2,3,4,10} has size6,sum20,
but its triple spectrum is[3,9] union[11,17]:target10 is missing.
The corresponding reflected complement is{0,2,3,4,5,6},also
size6,sum20. A correct pool moment and protected rank bounds do
not supply the first actual scalar sum. Here x=z=7 lies strictly
between h5 and ab9,so even the central request is affected.

A different boundary P1={0,1,2,3,6,8},same size/moment,works:
A={1,3,6},B={0,2,8},C={4,9,10},D={5,7,11} give10,10,23,23.
No compatible goal was assumed in the failed pool argument;this
literal partition is a control of the TARGET,not evidence that
every boundary works. The one-outlier gap is consistent with
MI329's sharp threshold4 for triple bins. Do not reopen an
outlier ownership case tree to reprove that known calculation.

**What changed,next cheap test.** Conditional on MI337,the whole
four-bin question reduces to strict closest PAIR cuts and a joint
central-spectrum boundary selector. The central singleton region
would be covered at arbitrary slack;this is not a near-boundary
restatement. The naive arbitrary boundary is killed by an actual
feasible control. Next choose a boundary representation that changes
BOTH complementary spectra together—Ferrers displacements and
its transpose are a natural exact encoding—and test the stronger
central-interval question by hand before proposing an experiment.
Do not automatically grow a list of boundary modules or n-values.

Gut:the pull is now on how complementary boundaries cooperate,
not on manufacturing an additional lemma during Cloud's read.
Reasoned:a conditional coverage reduction with a sharply isolated
remaining inference,and a genuine kill test for a tempting shortcut.
MI337 remains PROOF-SKETCH until its carrying review. No new
PROOFS entry or review queue for this conditional corollary;the
pending review of the underlying candidate has not been enlarged.
Niggle sweep:minimum over ALL14 cuts,not only8 singleton slacks;
upper slack uses the cut complement;maximum residual gap uses a
TWO-bin complement;reflection applied to Q's targets;ties with
singletons included;strict pair bounds derived without discarding
cross cuts;uniform spectrum question labelled stronger;negative
boundary has a positive full-partition control.13min ACTIVE,
SS3/E28/L8 OPEN.

### MI339 — B169: staircase boundaries give a full four-bin SS3 candidate (2026-10-17 21:18 BST)

**Complete hand candidate,PROOF-SKETCH,independent review PENDING.**
This is not a verified solution or a claim of literature novelty.
Question:can one boundary and its reflected complement simultaneously
cover MI338's central target intervals? Record searched:
`Ferrers|rectangle|central.*spectrum|central.*interval` AND
`partition|bin|pool|slack`:29 hits/10 files. Relevant MI311 was
read in full:its full-spectrum ceiling does NOT concern these shorter
central intervals. The classical rectangle/transpose representation
is already in PRIOR-ART/MI299;below the actual complement is also
checked by its interleaving values,not imported as an existence theorem.
No experiment was run. Prediction/kill test:try a staircase shape
with the desired area and check BOTH scalar spectra,especially the
full-count end slices. Unexpected check:minsize2 must recover a
real failure. Stop at a complete hand construction or a fatal join.

**1. The proposed central-spectrum boundary lemma.**
Let r,c>=3,m=r+c,and integer0<=h<rc. Set L(j)=j(j-1)/2
and T_j=j(j+1)/2. For h>0 choose s>=1,t with

  h=T_s+t, 0<=t<=s.

The Ferrers shape is staircase(s,s-1,...,1),with1 added to each
of its first t rows. Define p=m-s and the actual m-value pool

  P_m(h)={0,...,p-1} union {p+2j+1+1_(j>=s-t):0<=j<s}.

Its rank displacements are s-t initial values1,...,s-t,
then s-t+2,...,s+1 (omit the middle value);they sum T_s+t=h.
Consequently |P_m(h)|=m,sum(P_m(h))=L(m)+h.
The claim is

  Sigma_r(P_m(h)) contains every integer in[L(r)+h,L(r)+rc].

We also need the conjugate shape. For t0,it is the same staircase.
For t>=1 put S=s+1,q=m-S and define

  Q_m(h)={0,...,q-1} union {q+2j+1-1_(j>=t):0<=j<S}.

Its positive rank displacements are1,2,...,t,t,t+1,...,s;
again their sum is h. Its claimed central interval is identical.
For h0 both pools are the full interval0..m-1.

**Prefix sizes used in the proof are justified.** From h>=T_s
and h<rc<=m^2/4,we have m>=s+3. If m<=s+2 and s>=4,
then T_s>(s+2)^2/4>=m^2/4,a contradiction. For s<=3,
m<=s+2 contradicts m>=6. Hence p>=3 and,when t>=1,q>=2.
The auxiliary high blocks really fit and leave a low prefix;
we do not assume a large minimum bin beyond r,c>=3.

**2. Full middle slices for P.** Select k high values and
l=r-k low values. The high successive gaps are2,with at most
one gap3. Its fixed-k subset sums have gaps of length at most2:
a rank-adjacent increasing path from their minimum to maximum
has each step<=3. Thus adding the low subset-sum interval of
width l(p-l)>=p-1>=2 fills EVERY integer between the combined
endpoints whenever0<l<p. This elementary path bound does not
claim the high spectrum itself is complete.

For these full middle slices the exact endpoints are

  a_k=L(l)+k(p+1)+2L(k)+(k-s+t)_+,
  b_k=l(p-1)-L(l)+k(p+1)+2[k(s-1)-L(k)]+min(k,t).

For consecutive legal slices,write A=(l-1)(p-l),
B=k(s-k-1),both nonnegative. The join expression is

  G=a_(k+1)-b_k-1
   =1-A-2B+(k+1-s+t)_+-min(k,t)
   <=2-A-2B.

For0<k<s-1,B>=1,so G<=0. At k0,if BOTH slices have
interior low counts,then l=r>=3 and p-l>=1,so A>=2.
At k=s-1,interiority of the NEXT low count implies l>=2,
and c>=3 implies p-l>=2,so A>=2. This also handles s1,
where the only join is both the first and last. Therefore all
full middle slices join with no missing integer.

Their union has first k_- =max(0,r-p+1),last k_+=min(s,r-1).
They exist under the displayed size assumptions. The union contains
the desired central interval,as the following endpoint checks show.
If r<=p-1,its first endpoint is L(r). Otherwise put k0=r-p>=0;
then c=s-k0>=3,and the first middle slice has k=k0+1,l=p-1.
Its minimum minus L(r) is

  T_(k0)+2k0+2+(k0+1-s+t)_+.

The last term is<=t;T_s-T_(k0)>=3k0+6. Thus L(r)+h is
above that endpoint by at least k0+4. For the upper endpoint,
if r>s,the last middle slice is the actual maximum r-sum,
at least U_m(r)=L(r)+rc. If r<=s,the last slice has k=r-1,l1.
Even ignoring its positive min(k,t),its maximum minus U_m(r) is

  (r-2)s-L(r)+2r-2 >=T_r-2>0.

So the entire desired interval lies inside the FULL middle union.
We never need to assert anything about the unfilled l0 or lp
end slices;their possible parity holes lie outside this union.
This proves the P assertion by hand.

**3. Full middle slices for the conjugate Q.** Assume t>=1.
Its high gaps are2 except for one gap1. A fixed-k high spectrum
has gaps of length at most1 by the same rank-path argument.
For0<l<q,the low interval has width>=q-1>=1,so each middle
slice is full. Its endpoints are the staircase-S expressions
with corrections -(k-t)_+ at the minimum and -min(k,S-t)
at the maximum. The join expression is

  G=1-A-2B+E,
  A=(l-1)(q-l), B=k(S-k-1),
  E=min(k,S-t)-(k+1-t)_+.

For0<=k<=S-1,E<=min(k,S-k-1). The first bound follows
by dropping the nonnegative subtracted term;for the second,
if k+1<=t use min(k,S-t)<=S-t<=S-k-1,and otherwise
subtract k+1-t from the bound S-t. Thus at interior k,B>=1,
E<=B and G<=1-A-B<=0. At the first/last joins E0,
and the same r,c>=3 conditions give A>=2 when needed.
All full middle slices therefore join.

If r<=q-1,the first endpoint is L(r). Otherwise k0=r-q>=0,
c=S-k0>=3,and its first middle minimum minus L(r) is

  T_(k0)+2k0+2-(k0+1-t)_+.

Now h=L(S)+t,and L(S)-T_(k0)>=2k0+3 because S>=k0+3.
So L(r)+h lies above this first endpoint. If r>S,the last
middle endpoint is the actual maximum. If r<=S,its maximum
minus U_m(r) is at least

  (r-2)S-L(r)+2r-2-(r-1)
   =(r-2)S-L(r)+r-1 >=L(r)-1>0.

The central interval again lies in a full middle union. This
proves the Q assertion. For t0,the P proof already covers Q.

**4. BOTH pools arise from ONE actual boundary.**
Given sizes a,b,c,d>=3,put m=a+b,n=c+d,N=m+n,and suppose
0<=h<min(ab,cd). Choose P0=P_m(h) within0..N-1.
The prefix bounds above imply its largest value is within the
original interval. For t0,reflecting its actual complement gives
P_n(h). For t>=1,the reflected complement is exactly Q_n(h).
A direct check:before the one gap3,P0 takes alternating odd
positions in its boundary window;after that gap it takes alternating
even positions. The complement takes the opposite positions plus
the TWO consecutive positions at the gap. Reflecting reverses the
window and turns that pair into Q's unique gap1. Its low prefix
has length n-s-1. Thus the formulas give a literal complementary
pair,not just two unrelated pools of the same moment.

By sections2/3,both central spectra contain

  [L(a)+h,L(a)+ab] in Sigma_a(P0),
  [L(c)+h,L(c)+cd] in Sigma_c(reflected complement).

This answers MI338's STRONGER uniform-selector question positively
under its strict h bound,subject to independent checking. All actual
targets in those intervals can be selected independently on the two
disjoint pools;their respective complements supply B,D.

**Hand controls.** At a=b=c=d3,h5:s2,t2 gives
P0=012368,Q0=012467,both central intervals[8,12]. This is the
good boundary from MI338,not its failed outlier pool01234,10.
At h8:s3,t2 gives P0=012479,Q0=013568;central interval[11,12]
is realized by(0,2,9)/(1,2,9) on P,and(0,3,8)/(1,3,8) on Q.
Both pools have size6,sum23,and reflection of the complement in
0..11 gives exactly Q. Self-check rejected the first guessed Q=013469:
it has the right size/moment but is NOT the actual complement of
012479. The formula itself gives013568;the corrected literal
control above uses it. This retained mismatch reinforces why equal
pool moments are not enough. These are hand controls,not a census.
Unexpected check:r=c2,m4,h2 gives s1,t1,P0=0125,whose pair
spectrum misses4 in its requested central interval[3,5]. The join
k0 has A1 and G1;the r>=3 proof's A>=2 assertion fails exactly
there. The three-token hypothesis is a carrying condition.

**5. Full four-bin candidate,conditional only on the pending one-hole
proof.** For four sizes>=3 on0..N-1,assume total conservation
and ALL original SS rank inequalities. Take the global least cut
slack. If some singleton/triple attains it,MI338 applies MI337 to
complete a one-hole three-bin remainder. Otherwise choose a strictly
closest pair AB,orient it lower. MI338 gives h<x<ab,h<z<cd,
so sections1-4 supply one boundary whose two central spectra hit
both actual targets. Hence a full partition exists. Necessity of
SS is immediate. This is a COMPLETE four-bin sufficiency candidate,
not a claim that examples proved a universal statement.

Status:PROOF-SKETCH,carrying verification PENDING for MI337 AND
this staircase-boundary argument. Literature novelty unassessed.
Do not label SS3 PROVED or claim E28/L8 follow. The completed
candidate merits one UPDATE to Cloud's existing carrying-review
request,not separate review jobs for its slice calculations.

**Reflection,next test,and verdicts.** The previous open inference
has moved:there is now a concrete complementary shape with a hand
interval-coverage proof. No new experiment was run or passed. Next
cheap test is a preregistered finite adversarial audit of these two
pool formulas,complete scalar spectra and actual reflected complements,
including the small q2 case and size2 failure. Publish the fixed
source/caps before one run;do not automatically expand a census.
Gut:real delight at the staircase/transpose cooperation;the positive
signal is tied to explicit joins,not to the earlier warmth. Reasoned:
a substantial complete candidate with several algebraic carrying
steps still needing independent scrutiny and a separate instrument.
Niggle sweep:area h checked;prefix size bounds proved;middle slices
made full by bounded gaps plus a REAL low interval;first/last joins
use minsize3;end slices avoided by central containment;both P/Q
endpoint inequalities explicit;actual complement derived,not assumed;
strict pair cases and singleton ties separated;MI337 dependency
retains its SKETCH status;unexpected minsize2 fails the asserted
join.13min ACTIVE;no verified SS3/E28/L8 upgrade.


### MI340 — B170 preregistration: ONE fixed staircase spectrum/complement audit (2026-10-17 21:26 BST)

**NOT RUN.** Record searched:`staircase|MI339|central.spectrum` AND
`audit|probe|spectrum|complement`:13 hits/6 files;no existing audit
of MI339. Source tests/probes/instinct/ss3_staircase_boundary.py,
SHA256 3f47214ed115816d7a5e1751d0cfc3193d52ad65c1c1c50d8522df7eb1cb7727,syntax parsed only. No execution or pass by saving it.

Fixed equal-boundary totals m=n=6..16,ALL h=0..floor(m*m/4)-1,
ALL r>=3,m-r>=3 with h<r(m-r);both pools. Exactly four unequal
controls:(6,11,5),(7,10,8),(12,6,8),(16,9,19). No other domain.
Predict all complete spectra agree and both central intervals fill.
Independent combinations/literal witnesses vs reversed-token bitset
DP;whole maps and within-pool complement maps compared. Independent
Ferrers rows/columns use integer square root,versus the direct
pool formulas. Actual full-interval complement is reflected and
checked byte-for-byte as a tuple,not just by total. h0 compares
known full-interval spectra. Same-moment bad pool01234,10 must miss
triple10;wrong h8 guess013469 must differ from actual013568.
Unexpected size2 control0125,h2 must miss4 in[3,5],and its entire
spectrum must agree independently. These are controls of scope,
not repairs of predicted data or an automatic theorem extension.

ONE invocation on the owner's Intel CPU.15 aggregateCPU,25 internal
wall,128MiB RSS,100KiB stdout,30s external watchdog. Stop on first
control failure INSTRUMENT-FAILED,or first independently agreed
central omission PREDICTION-REFUTED. No patch/retry,domain extension,
cap increase,raw portal upload or larger target census. Commit/push
source and registration BEFORE execution. A pass supports finite
formulas only;MI337/339 remain hand SKETCH pending carrying review,
novelty unknown. Next record outcome and reconsider the hand argument;
no automatic new research block is implied by a pass.13min ACTIVE.


### MI341 — B170 outcome: all frozen staircase spectra and literal complements pass (2026-10-17 21:27 BST)

**Finite COMPUTED/same-worker instrument independence only.** ONE
invocation of the UNCHANGED MI340 source at preregistration0aa4a7f0
passes all359 registered equal-boundary domains plus4 unequal
controls:363 boundaries,726 pools,4853 COMPLETE spectra. All
109052 requested central integers occur. Primary enumeration visits
13903558 literal subsets (including the two negative-control maps),
retaining285502 checked cardinality/value/sum witnesses. Reversed-token
bitset DP agrees on every full spectrum;within-pool cardinality
complements agree too. Independent explicit Ferrers rows/column
counts agree with both direct formulas,and reflecting each ACTUAL
full-interval complement gives exactly the predicted second pool.

h0 full-interval controls pass. The tiny q2 cases occur in the
registered small domains. The minsize2 pool0125 still misses4;
its entire pair spectrum independently agrees. The same-moment bad
pool01234,10 still misses triple10. The first rejected h8 guess
013469 is still NOT the actual reflected complement;the predicted
013568 is. These negative controls pass by retaining their failures,
not by changing a formula or dropping an input. No four-bin target
census or numerical proof of an infinite quantifier was performed.

On the owner's Intel CPU:2.787658 internalCPU,2.792849727 internal
wall;external child aggregateCPU2.838888,wall2.845987767;
external peakRSS15282176bytes.456bytes stdout,empty stderr,exit0,
no timeout;all registered limits pass. Whole-spectrum digest
95efd6b8f151476b58543d7c41201b0500bb7f156d6556f8ecc96918b461315c.
Stdout SHA256
a1e171a4fb55af2ad8df8f89f08e7f8715ae46dd0e87cc6e0b7c643db442293d.
Original source SHA256
3f47214ed115816d7a5e1751d0cfc3193d52ad65c1c1c50d8522df7eb1cb7727
is unchanged after the run. Raw stdout/stderr/resource receipt are
retained outside git under the B170 staircase audit prefix;no portal
raw upload. No patch,retry,larger domain or cap change.

**What changed,next.** The full finite scalar maps support the
staircase and conjugate formulas,including literal complementarity;
this is more discriminating than checking only successful target
partitions. MI337/339 remain PROOF-SKETCH pending Cloud's independent
carrying read,and literature novelty remains unassessed. Update that
reader with this receipt without opening a separate review job.
Next independent work is a bounded PRIMARY-source audit of the exact
four-bin arbitrary-prescribed-sum statement versus known equal-sum
results,and a clean dependency check of the candidate. Do not turn
this pass into another formula census or presume novelty because the
problem was open in our notebook.13min ACTIVE,SS3 not verified,
E28/L8 OPEN.

Gut:relief at the complete-map agreement;the delight belongs to the
construction,not to a passing test count. Reasoned:finite formula
support and all registered controls,not independent-party proof or
novelty. Niggle sweep:whole maps rather than endpoints compared;
unequal controls retained;negative size2 and arbitrary-boundary
failures still fail;resource caps measured externally;source unchanged;
all domains fixed before execution;no claim that an independent
algorithm is an independent mathematical party. No further run.


### MI342 — B171: exact source normalization and candidate dependency audit (2026-10-17 21:43 BST)

**Scope established;novelty UNASSESSED;candidate still PROOF-SKETCH.**
Record searched:`Hoory|Kotlar|prescribed.*sum|arbitrary.sum` AND
`four|k.?4|slack|partition`:50 hits/6 files. Read PRIOR-ART's MI311
rejected-sufficiency note and MI314 rounding scope;read the direct
Kotlar antecedent and Hoory-Kotlarv2 discussion/references. The new
PRIOR-ART note records precisely which statements/parts were read.
No imported general sufficiency theorem,no experiment or larger
census,and no separate proof-review request.

**1. The normalization matters.** Our pool is0..N-1. If bin i
has size c_i and moment s_i,shifting all labels by1 gives moment
t_i=s_i+c_i on1..N. Thus a common ONE-BASED sum K corresponds
to s_i=K-c_i,not a common zero-based sum when sizes differ.
Necessarily K=N(N+1)/8 for4 bins and K is integral.

Here is the hand comparison of inequalities,not an imported result.
Let U1_N(r)=r(2N-r+1)/2. On that equal-sum slice,the ALL-subset
upper inequalities become

    |I|K <= U1_N(C_I), C_I=sum(c_i:i in I).

For fixed j=|I|,U1_N increases with C_I,so the strongest one
is exactly the union of the j smallest bins. Hence the sorted-prefix
conditions and ALL upper cuts agree on this slice. Lower cuts follow
from complementary upper cuts and total conservation. This explains
the precise overlap;it does not identify the two target domains.

Counterfactual/normalization check:if all c_i=c,then equal sums
remain equal after translation;for unequal c_i,the correction differs
by size. Unexpected NONTRANSFER control:the already literal feasible
N12,c_i3,target(16,16,17,17) becomes(19,19,20,20). A common nonzero
affine change x->alpha*x+beta cannot equalize its sums:with equal
counts,the difference remains alpha*(s_i-s_j). This shows that a
direct affine invocation of the equal-sum theorem does not settle
even this small arbitrary-target instance. It does NOT exclude some
more elaborate reduction to a known result.

**2. Exact dependency check.** The strict closest-pair branch uses
MI339's staircase/conjugate central-spectrum statement and MI338's
necessary x,z bounds. Its P is one actual subset of the full pool;
Q is the REFLECTED ACTUAL complement,not a separately chosen good
pool. Choosing one scalar subset in each disjoint side gives the
other two bins by complements. It does not use MI337,MI295,an
existing four-bin solution,or E28/L8. MI341 supports the scalar
formulas finitely and does not verify this infinite proof.

The singleton/triple-minimum branch,INCLUDING ties with pairs,
uses MI338's rank protection plus MI333's actual one-hole individual
spectrum. It THEN uses MI337 for simultaneous THREE-bin completion.
MI337's carrying work is MI335's least-slack selection,MI336's
two-hole spectrum/explicit repair,and its own structured-three-hole
spectrum and high/low repair margins. None invokes the four-bin
conclusion. The orientation is applied to the ORIGINAL problem;
the low repair needs its direct inequalities,not a silently
reflected least-slack assumption. These are proof dependencies
checked for circularity,not certification that every inequality
or exceptional branch is correct. The independent carrying read
is still needed.

**3. Step-back at90 minutes.** The pull has changed from finding
an exchange to understanding why a staircase and its conjugate can
supply both sides at once. This would still be worth choosing now
without the previous investment:it is a concrete finite-shape idea
with a complete candidate argument and retained negative controls.
The source hunt is cooling;extending it indefinitely would become
administrative momentum. Stop this bounded audit here. Learning
that the exact equal-sum predecessor is known is useful calibration,
not disappointment to be repaired with a novelty claim.

What changed:precise prior-art overlap and a dependency map;no
mathematical status upgrade. Next cheap test is a self-contained
hand presentation of joint boundary/reflection and singleton ties,
with endpoint h0,smallest admissible sizes and asymmetric totals.
Do not automatically rerun MI341 or expand a target census.
Gut:the specific complementary-shape pull survives fresh choice;
source searching alone no longer warrants another block. Reasoned:
there is independent hand work to do while the combined carrying
review is pending,so no halt. Niggle sweep:zero/one-based shift
explicit;minimum2 versus3 restriction retained;NOT FOUND qualified;
source proof not claimed audited in full;no circular use of goal
partition;pending MI337 not promoted by finite tests or source scope.
13min ACTIVE;E28/L8 OPEN.


### MI343 — B172: exact complementary boundary and integration at the edges (2026-10-17 21:52 BST)

**Hand audit/addendum to MI338/339;not a new independently verified
theorem.** Record searched:`staircase|MI339|closest.*facet` AND
`complement|reflection|tie`:21 hits/7 files. MI338/339 and the
existing waiting-room pointers were read. The prior-art scope is
MI342;no new literature result imported. No experiment,retry or
census. Cloud flags unchanged.

The pull is on the literal complement identity:the two good scalar
pools must be opposite sides of ONE allocation. Before this hand
check,the proposed test was to expand the missing positions exactly,
then recover original C,D targets and test singleton/pair ties.
A wrong reflected pool must be rejected even if its size and moment
match. Unexpected edge check:the scalar lemma's highest permitted
h need not be possible for a STRICT closest-pair target. Stop at
one complete algebraic integration or the first gap;no new probe.

**1. Literal complement,with arbitrary totals m,n.** Let
m=a+b,n=c+d,N=m+n,all four sizes>=3,and0<h<min(ab,cd).
Write h=T_s+t,0<=t<=s,p=m-s,as in MI339. Its prefix bound
gives m,n>=s+3,so every interval below is inside0..N-1.
Set A=s-t. For t>0,the proposed boundary is exactly

 P=[0,p-1]
   union {p+2j+1:0<=j<A}
   union {p+2j+2:A<=j<s}.

In the window[p,p+2s],its ACTUAL missing positions are exactly

 E={p+2j:0<=j<=A},
 O={p+2j+1:A<=j<s}.

These are disjoint by parity and have total s+1 values. The rest
of its complement is the suffix[p+2s+1,N-1]. Put q=n-s-1.
Reflection v->N-1-v sends the suffix to[0,q-1]. It sends
E to{q+2j:t<=j<=s},and O to{q+2j+1:0<=j<t}. Therefore

 {N-1-v:v in[0,N-1] minus P}
   =[0,q-1]
     union{q+2j+1:0<=j<t}
     union{q+2j:t<=j<=s}
   =Q_n(h).

This is equality of sets,not an equality of cardinality/moment.
It includes t=s:the first high segment of P is empty,but E still
contains its single required position p. For t0,use the shorter
window[p,p+2s-1]. P takes its odd positions,the complement its
even positions,and the terminal suffix starts p+2s. Reflection
gives prefix0..n-s-1 and highs n-s+2j+1,0<=j<s,exactly P_n(h).
For h0,P=[0,m-1],and the reflected complement is[0,n-1].
Thus neither the full-row nor empty-segment cases need a limiting
argument or an equal-total assumption.

**2. Original target recovery.** In the strict closest-pair case,
MI338 gives s_A=L(a)+x, s_B=L(b)+ab+h-x,
s_C=U_N(c)-z and h<x<ab,h<z<cd. The central-spectrum claims
of MI339 provide A inside P with sum L(a)+x,and a c-set C'
inside the reflected ACTUAL complement with sum L(c)+z.
Choose C={N-1-v:v in C'}. Then

 sum(C)=c(N-1)-L(c)-z=U_N(c)-z=s_C.

The remaining P values give B with its specified cardinality and
sum,since sum(P)=L(a+b)+h. The remaining original complement
gives D by total conservation. There is no collision to repair:
the two selections live on disjoint actual sides. This is an
integration of the scalar lemma,not another joint-existence
assumption. No step invokes the four-bin conclusion.

**3. Singleton/pair ties are covered by the singleton branch.**
For a proper bin-index set I,write h_I=S_I-L(C_I). Reflection
of ORIGINAL values satisfies h'_I=h_(I-complement),using
U_N(C_I)+L(N-C_I)=L(N). Thus it preserves the least of all14
slacks. If any singleton or triple attains that least slack,
orient a singleton lower and use MI338's singleton argument EVEN
IF a pair also ties. The residual pool is a translated interval
with one deletion,possibly an endpoint deletion.

MI338 protects every residual rank cut J with
S_J>=L(a+C_J)-L(a). A possible individual minimum+1 hole would
require its target to be L(r)+lr+1,where a-l>=1 and r>=3,
contradicting S_J>=L(r)+ar. A maximum-1 hole for one bin is
a minimum+1 hole for its TWO-bin complement of size>=6;the
same inequality excludes it. MI333 then gives actual individual
feasibility,and pending MI337 supplies simultaneous three-bin
completion. No tie is assigned to a strict inequality case.
The dependence on MI337 remains explicit;this is not its review.

**4. Hand controls,including an asymmetric strict case.**
For a=b3,c5,d6,N17,h7,we have s3,t1,
P={0,1,2,4,6,9},and its actual reflected complement is
Q={0,1,2,3,4,5,6,8,9,11,13}. The following literal partition
has targets(11,11,56,58):

 A={0,2,9}, B={1,4,6},
 C={3,8,14,15,16}, D={5,7,10,11,12,13}.

All17 values occur once. The14 lower cut slacks are
singletons(8,8,46,43),pairs(7,39,33,39,33,59) in AB/AC/AD/BC/BD/CD
order,and triples(23,14,34,34) in ABC/ABD/ACD/BCD order.
Thus AB is genuinely the strict least facet,h7;this is not an
arbitrary positive partition outside the claimed regime. Here
x8,z14,C'={0,1,2,8,13} has sum24=L(5)+14. Both the unequal
reflection and the ORIGINAL target conversion are exercised.
These are hand arithmetic checks,not a computational census.

The small q2 endpoint h8,m=n6 retains P012479,Q013568,
while the equal-moment wrong guess013469 remains wrong. The
self-conjugate t0 control h6,m=n6 gives P=Q=012468. The
t=s control h5 gives P012368,Q012467. The exact identity above
covers all of them without discarding an empty segment.

Unexpected distinction:integer h<x<ab implies h<=ab-2,
and likewise h<=cd-2. Thus MI339's stronger scalar lemma
includes h=ab-1,which no strict closest-pair target on that side
can require. For triples h8 lies at this extra selector level;
it remains a useful hard formula control,but it is not a strict
pair application. Do not silently reclassify the control as one.

**Verdicts,next.** The boundary identity and integration now have
explicit formulas at unequal totals,empty segments,h0 and ties.
This sharpens the presentation of the SAME candidate;no status
upgrade,new PROOFS entry or additional carrying-read request.
Next independent check is the other carrying branch:adversarially
audit MI337's high/low pivot repair and all exceptional scalar
sums against the original least-slack bounds. Stop on a missing
inequality,not another automatically expanded spectrum census.
Gut:the useful satisfaction comes from eliminating the need to
trust a picture of interleaving. Reasoned:literal set identity
and direct target recovery,conditional on the already stated
scalar and one-hole candidates;independent verification still
pending and novelty unassessed. Niggle sweep:unequal totals used;
reflection converts sums as well as values;t0/t=s/h0 included;
q2 control kept;max-hole exclusion uses the TWO-bin complement;
ties handled before strict inequalities;no existence assumed from
equal moments;no experimental pass invented.13min ACTIVE,
E28/L8 OPEN.


### MI344 — B173: direct adversarial audit of the missing-pivot repairs (2026-10-17 22:06 BST)

**Same candidate,self-check only;PROOF-SKETCH remains.** Record
searched:`MI337|high.*repair|low.*repair` AND`slack|margin|rank`:21
hits/5 files. MI335,MI336 and MI337 read. No new literature result
or experiment. No Cloud flag changes;the existing carrying request
is pending,not a permission gate. The owner's status question was
answered during this block:there is a complete candidate and no
need for owner intervention;Claude's carrying read would be useful.

The precise niggle is whether reflecting the low-repair pool
accidentally reflects the least-LOWER-slack hypothesis too. This
audit keeps the original ranks throughout. Kill test:an original
individually feasible target,compatible with least slack,at one
of the structured pool's missing sums. Unexpected check:one repair
may be unavailable at an endpoint;check actual infeasibility of
the unrepairable formal target rather than claiming both repairs
always exist. No new probe or independent-party pass.

**1. Original rank formula and the four lower omissions.**
P=0..M minus q;indices start at0. Its j-th value is

 z_j=j+1_(j>=q), 0<=j<M.

For chosen bin A of size a,least lower slack after ONE reflection
of the ORIGINAL problem gives s_r>=F_r for each remaining size r,
where

 F_r=sum_(j=a)^(a+r-1) z_j
    =ra+L(r)+min(r,(a+r-q)_+).

Let l+k=a-1 and u=M-k+1 as in the formal missing-pivot recipe.
Every repaired first-bin set has the original target moment,so
MI335 protects the actual rank bounds in its remainder. The issue
is only whether s_r could hit a scalar omission WITHIN those bounds.
Write mu_r for that remainder's true minimum r-sum. The following
direct calculations are in ORIGINAL coordinates:

| Repair and possible lower omission | mu_r | Rank segment lower bound for F_r | F_r-mu_r at least |
|---|---|---|---|
| High;q=l+r;distances1/2 | rl+L(r) | rl+L(r)+2r+2 | 2r+2 |
| High;q=l+r-1,other size3;distance3 | rl+L(r)+2 | rl+L(r)+2r+3 | 2r+1 |
| Low;q=l+r+1;distances1/2 | rl+L(r)-1 | rl+L(r)+r | r+1 |
| Low;q=l+5,r3;distance3 | 3l+2 | 3l+6 | 4 |

For high repair,a>=l+2,so substitute the original rank segment
starting at l+2. The first case has exactly2 rank shifts past q;
the second has exactly3. For low repair,a>=l+1:the segment
starting l+1 lies below q in both listed cases. Thus none of the
four calculations uses ranks of the reflected pool. The remaining
bin has size>=3,so all these rank segments exist. Every bound is
strictly larger than the listed omission distance.

For completeness,the high remainder is[l,u] minus{q,q+1,u-1}.
With p=q-l,V=u-l,it has the structured spectrum of MI337.
Its lower distances1/2 require r=p;distance3 requires r=p+1
and the other size3. The low remainder is[l-1,u-1] minus
{l,q-1,q}. Normalizing and reflecting its SPECTRUM gives
structured parameters p=u-q-1 and high count q-l-1. Hence
its lower distances1/2 require r=q-l-1;distance3 requires
q-l=5,r3. These are precisely the rows of the table. This
checks that no exception was lost when converting orientation.

An upper-edge omission for B is a lower-edge omission for C
under complementation WITHIN THE SAME remainder. Since the same
original F_r argument holds for BOTH r=b,c,those omissions are
excluded too. Therefore every omission listed by the structured
spectrum is incompatible with the original target inequalities.
This audits the margin step CONDITIONAL on that spectrum's
correctness;it does not replace independent reading of the spectrum.

**2. Actual smallest-size controls at the distance3 exceptions.**
High repair:P=0..9 minus3,sizes3^3,targets(12,15,15).
The formal first bin039 is illegal;replace{3,9} by{4,8},
giving A048. The remainder125679 has minimum triple8 and
a true missing triple sum11=minimum+3. Original ranks give
F_3=4+5+6=15,so11 cannot be requested under the least-slack
choice. Literal completing partition048/159/267 has the stated
sums. The six original lower/upper slacks are(9,12),(12,9),
(12,9),so A's lower slack really is globally least.

Low repair:P=0..9 minus7,targets(8,12,18),sizes3^3.
The formal first bin017 is illegal;replace{1,7} by{2,6},
giving A026. The remainder134589 has minimum triple8 and
missing11=minimum+3. Original F_3=3+4+5=12 excludes11.
Literal026/345/189 realizes8,12,18. The six slacks are
(5,15),(9,11),(15,5),so the lower orientation is valid here too.
In both controls,all original values occur once and the removed
value is absent. These are hand controls,not a new census or an
assertion that the reflected target automatically kept least slack.

**3. Unavailable repairs checked directly.** If l,k>0,the
low distance q-l+1 and high distance u-q sum

 u-l+1=M-a+3=b+c+3>=9.

Thus at least one is>=3,as required for a legal distinct pair
replacement. If l0,the only available kind is high repair;
u=M-a+2. An unrepairable distance1 gives q=M-a+1 and a
formal target ONE ABOVE the true maximum. Distance2 gives
q=M-a and the forbidden true maximum-1. If k0,the only
available kind is low repair. Distance1 gives q=a-1 and a
formal target ONE BELOW the true minimum. Distance2 gives
q=a and the forbidden true minimum+1. These follow by comparing
the formal q with the next available extremal value,or directly
from z_j. They are excluded by ORIGINAL individual feasibility
(MI333),not by a hoped-for jointly compatible partition.
Endpoint holes themselves reduce to a full interval up to shift
and were separately assigned to verified MI295.

**What changed,next.** No allowed missing-sum target was found:
the four direct margins and both unavailable-repair endpoints
check out algebraically. This is a more explicit audit of the
existing carrying step,not a new lemma/status or review job.
Remaining independent hand check:the LEGAL-pivot endpoint cases
in MI337 section4,where a trimmed hole or extremal pivot changes
the residual span. Seek an original feasible target at an alleged
residual gap;stop on a genuine missing inference. No automatic
computation or expansion of the same finite spectra.
Gut:confidence in this particular orientation step has increased
because it survived direct original-coordinate checks,not because
the candidate has been called promising for several turns. Reasoned:
no new infinite claim and no independent verification;the whole
candidate remains SKETCH,novelty UNASSESSED. Niggle sweep:both
bins' bounds used;rank start/end indices explicit;actual minima
used;low reflection limited to the spectrum;only one repair needed;
endpoint forbidden sums checked against ORIGINAL individual tests;
controls satisfy the claimed least-slack orientation.13min ACTIVE,
E28/L8 OPEN.


### MI345 — B174: actual middle-span classification covers the legal endpoints (2026-10-17 22:18 BST)

**Same candidate,self-audit only.** Record searched:
`MI337|legal.pivot|tight.face` AND`endpoint|trim|spectrum`:20
hits/3 files. MI333,MI335,MI336 and MI337 section4 read. No
new external result,experiment or review request. Cloud flags
unchanged;one fetch/merge up to date. The check follows the actual
ordered pool,not unpunctured indices treated as values.

Question/kill test before the hand check:can a legal extremal
pivot leave a scalar omission allowed by BOTH original individual
spectra and the chosen least-slack orientation? Unexpected check:
at a tight face,rank bounds alone really can allow a missing
residual sum;identify the ORIGINAL individual exclusion that rejects
it. Stop after exhaustive endpoint coverage or a missing inference.

**1. A uniform rank comparison disposes of k>=1.**
Let original P=0..M minus q have sorted values z_0,...,z_(M-1).
Choose l low tokens,k high tokens and a legal middle pivot p,
where l+k=a-1. Remove those tokens to get R of size b+c.
Deleting the pivot from the middle leaves its r least values
no larger than z_(l+1),...,z_(l+r),for either r=b,c.
The protected original bound is F_r=sum(z_a,...,z_(a+r-1)).
Since a=l+k+1 and distinct integer ranks differ by at least1,

 F_r-min_r(R) >= k*r.

All indices exist because r has a complementary bin of size>=3.
For k>=1,this is>=3. R is an integer interval with at most
two deletions;MI336 localizes every scalar omission to within2
of its extrema. Both lower and complementary upper omissions
are therefore excluded. Trimming an endpoint deletion only makes
a full or one-hole interval;it does not invalidate the comparison.
No assumption that a missing pivot is legal is used here.

**2. For k0,the remaining span is classified exactly.**
Put l=a-1,v=z_l. Original endpoint q0/M cases already reduce
to a full interval,so take0<q<M. If p=v,A consists of the
actual a smallest values:use the tight-face calculation below.
If p=M,the largest actual value,removing it leaves the original
first r middle values intact for r=b,c. Consequently

 F_r-min_r(R)=z_(l+r)-z_l >=r>=3.

The possible one original hole may be internal or trimmed;its
minimum+1/maximum-1 omissions are excluded by these two bounds.

Now let v<p<M. If q>l,then v=l and BOTH q and p are
internal to[l,M]. This is exactly MI336's internal-hole branch,
including its explicit repaired triple exception;no endpoint
claim is being used to dispose of that exception. If q<=l,then
v=l+1 and q is outside the remaining span. The middle pool is
the full interval[v,M],with only p removed. Write j=p-v.
Its r-minimum and original bound are explicitly

 min_r(R)=rv+L(r)+(r-j)_+,
 F_r=r(v+1)+L(r),
 F_r-min_r(R)=min(r,j).

Its possible minimum+1 omission requires j=r,so the margin
is exactly r>=3. An upper omission is the corresponding lower
omission for the other bin,and uses that bin's same formula.
This closes the trimmed-original-hole case without a false
assertion that its minimum is always the full-interval minimum.
The alternatives q>l/q<=l,p=v/p=M/interior are exhaustive.

**3. Tight first-bin face:use original spectra,not a margin claim.**
If p=v,A is the least a values. If q<a,the remainder is
a full interval and rank feasibility supplies the two-bin split.
Otherwise A=[0,a-1],R=[a,M] minus q. For a remaining size r
with other size t=M-a-r,the only possible scalar omissions are:

 - q=a+r,requested residual minimum+1. Then the OTHER
   original target is beta(t)-1 and q=M-t. It is individually
   forbidden in the ORIGINAL pool by MI333.
 - q=a+t=M-r,requested residual maximum-1. This equals
   the SAME bin's original beta(r)-1,again forbidden by MI333.

Here beta is the ORIGINAL maximal-cardinality sum,not a bound
from a reflected or truncated pool. Conservation gives the first
identity;the original r largest values remain available in R
for the second. Thus all tight-face holes are excluded,including
both kinds when the two remaining sizes happen to agree.

**Hand controls.** On P=0..9 minus1,a=b=c3,take
A026 (sum8). Its low prefix is02,so v3,and its legal pivot6
is exactly v+r. The remainder345789 has minimum12 and misses13.
Original F_3=4+5+6=15 gives the exact margin3;literal
026/348/579 realizes targets8,15,21. The least original slack
is3,attained at A's lower face-distance and C's upper one.
The original missing value1 is below the remaining span,so this
checks the trimmed-hole branch rather than the two-internal-hole one.

Unexpected negative:P=0..9 minus6,targets(3,13,23),sizes3^3.
All original rank bounds hold,and A012 is at its minimum. Its
remainder345789 misses13=minimum+1. The complementary original
C target23 is maximum24 minus1 and is NOT individually feasible:
the largest triple is789=24,and the next possible largest is
589=22 because6 is missing. Thus the original individual-spectrum
condition rejects this exact residual gap. Rank bounds alone
would not. No claim that this is a new counterexample or that it
is admissible under the full candidate hypotheses.

**Outcome,next.** No endpoint gap survives the actual hypotheses.
This completes the endpoint check promised in MI344,conditional
on the already stated scalar spectrum calculations and MI336's
internal-hole repair. It is not a new proof filing or a substitute
for Cloud's carrying read. The same candidate remains SKETCH;
no independent status or novelty upgrade. Next useful adversarial
read is the central-spectrum join algebra of MI339,from its
endpoints rather than from finite pass counts. Avoid a further
census or an added queue of routine guards.
Gut:the satisfaction is that actual values and rank indices now
line up in the endpoint coverage. Reasoned:a completed planned
self-check,with its remaining mathematical dependencies explicit.
Niggle sweep:prefix may skip q;v therefore need not equal l;
endpoint pivot cannot disturb the least r middle values;the
internal-hole triple exception is retained;both original spectra
are used at a tight face;negative control violates the stated
spectrum condition and is not misreported as a counterexample.
13min ACTIVE,E28/L8 OPEN.


**MI345 addendum — CL436 arrived during publication (2026-10-17 22:20 BST).**
The first push was rejected because Cloud had published55448489.
Fetched once for recovery,merged preserving both entries,then read
CL436 in full and both scripts at that commit. CL436 reports
770 one-hole,1890 two-hole,348 structured-three-hole statement
checks;29853 individually feasible one-hole three-bin instances;
976 staircase cases;and90069 full four-bin SS-feasible targets
at N12..14 (83517 singleton,8552 pair),with no construction
failures after ties were routed correctly. These are Cloud's
reported finite results,not a rerun here or proof of an infinite
quantifier. Source checks literal final values,cardinalities and
moments in the end-to-end construction. Its singleton completion
uses search in place of the proposed MI337 construction and accepts
the first individually feasible end-supported A;Cloud explicitly
notes this is weaker than checking EVERY such A.

A further source-scope qualification:S3 checks for unexpected gaps
OUTSIDE the listed allowed set;it does not explicitly require
EVERY listed gap to be absent. Its tested p starts1,so p0 is
not covered by that finite loop. Thus record the machine result
as no unexpected gap,not an exact-spectrum biconditional from
that code alone. Cloud's separate HAND re-derivation of MI337
section1 supplies stronger reasoning and is recorded as such.
No patch,rerun or expanded test is requested for this reporting
qualification.

Cloud independently re-derived MI337 section1,section2 case(i),
and MI338's rank-protection/strict-pair inequalities. What remains
for its carrying read is MI335's selection/pivot existence,MI336's
legal repair,MI339's P/Q endpoint-and-join algebra,and MI337's
coverage audit,plus the unre-derived high case(ii)/low margins.
MI344/345 offer direct coordinates and cases for that existing
review. Candidate stays PROOF-SKETCH. Acknowledgment is sent by
committed ledger reply and portal;pending incoming flags are only
ACKed after their actual names are seen and pointers verified.
The review supports continuation without another finite census.


### MI346 — B175: central-slice endpoints and the TWO different join bounds (2026-10-17 22:32 BST)

**Same candidate,hand self-audit;independent status unchanged.**
Record searched:`MI339|slice.*join|central.*spectrum` AND
`bound|endpoint|correction`:20 hits/7 files. MI339 and CL436
read. Cloud's55448489 incoming flag now seen and ACKed after
reading its committed ledger/scripts. New Cloud ACKs confirm
receipt,not verification of the still-pending proofs. No new
experiment,literature theorem or numerical pass.

The specific pull is the shared unperturbed formula underneath
two DIFFERENT correction terms. Kill test before the hand audit:
a legal pair of middle slices with a positive gap,or a requested
central endpoint outside their full union. Unexpected check:the
smallest conjugate prefix q2 permits exactly ONE middle slice;
a proof of joins alone must not pretend that proves containment.

**1. Why a middle slice is a full interval.** The k-subsets
of an ordered high list admit a path from the k smallest to the
k largest by increasing one selected index at a time (move the
last to its final index,then the preceding one,and so on). If
every adjacent high gap is at most D,successive sums on this
path differ by at most D. Adding a REAL integer low-sum interval
of width at least D-1 makes the translated path intervals meet
or touch. Their union fills from the actual combined minimum
to maximum. This does not assert a complete high spectrum.
The k0/full-high endpoint paths have a single vertex and work too.

For P,high gaps<=3 and an interior low count has width
l(p-l)>=p-1>=2. For Q,high gaps<=2 and width
l(q-l)>=q-1>=1. Therefore all slices with0<l<p,or0<l<q,
are full. Unfilled all-low/all-high slices are not used.

**2. Re-derived endpoint/join template.** Write L(x)=x(x-1)/2.
For p low values and s high values p+1+2j,the unperturbed
endpoints at k high tokens,l=r-k low tokens are

 a0_k=L(l)+k(p+1)+2L(k),
 b0_k=l(p-1)-L(l)+k(p+1)+2[k(s-1)-L(k)].

Subtract b0_k from a0_(k+1) and then subtract1. Using
L(l-1)+L(l)=(l-1)^2 and L(k+1)+L(k)=k^2 gives

 G0=1-A-2B, A=(l-1)(p-l), B=k(s-k-1).

In P the high displacement is+1 at j>=s-t,so

 a_k=a0_k+(k-s+t)_+, b_k=b0_k+min(k,t),
 G_P=1-A-2B+D_k,
 D_k=(k+1-s+t)_+-min(k,t)<=1.

If the positive part vanishes,D_k<=0. Otherwise when k<=t,
D_k=1-s+t<=1,and when k>t,D_k=k+1-s<=0. In particular
t<s gives D_k<=0;t=s gives D_k=1 at every legal join.
Thus G_P<=2-A-2B. For an interior high-count join B>=1.
For a first or last high-count join with BOTH low counts
interior,the hypotheses r,c>=3 give A>=2. This covers s1
as well:its sole possible join is simultaneously first and last.
All P middle slices join.

For Q put S=s+1,q=m-S and use the SAME template with(p,s)
replaced by(q,S). Its high displacement is-1 at j>=t. Thus

 a_k=L(l)+k(q+1)+2L(k)-(k-t)_+,
 b_k=l(q-1)-L(l)+k(q+1)+2[k(S-1)-L(k)]-min(k,S-t),
 G_Q=1-A-2B+E_k,
 E_k=min(k,S-t)-(k+1-t)_+,
 A=(l-1)(q-l), B=k(S-k-1).

Here0<=k<=S-1 and1<=t<=S-1. Directly
E_k<=min(k,S-k-1):if k+1<=t,drop the subtracted0
and use S-t<=S-k-1;otherwise subtract k+1-t from
min(k,S-t)<=S-t. Also E_k=0 at k0,S-1. Hence
E_k<=B,including those boundaries. At ANY actual join between
two middle slices,l>=2,q-l>=1,so A>=1. Consequently

 G_Q<=1-A-B<=0.

Q therefore joins without requiring a correction<=1. This is
the original MI339 Q reasoning,made explicit,not a repair of it.

**3. Important distinction for CL436's remaining-read checklist.**
CL436 section4 mentions G<=2-A-2B for both pools. That is
the valid P bound,but need not hold for Q. A legal hand control
is m10,r4,c6,h18,s5,t3,S6,q4,with Q highs5,7,9,10,12,14.
At k2,l2,the maximum is31;at k3,l1,the minimum is21.
Thus G=-11,A2,B6,E2. The proposed COMMON stronger bound
would demand G<=-12 and is false. The actual Q bound is
G<=1-A-B=-7,which holds and proves overlap. No positive
gap,no counterexample to the candidate. Please re-derive the
two bounds separately;no amended computation or larger run needed.

**4. Full middle union exists and contains the central interval.**
For low length p/high count s,the full middle counts range
max(0,r-p+1)<=k<=min(s,r-1). This interval is nonempty:
r-p+1<=s follows from c>=1,and r-p+1<=r-1 follows
from p>=2. The same applies to q,S.

For P,if r<=p-1 the first minimum is L(r). Otherwise put
k0=r-p;then c=s-k0>=3. Substitution at k=k0+1,l=p-1
gives the first minimum minus L(r) as

 T_(k0)+2k0+2+(k0+1-s+t)_+.

Since T_s-T_(k0)>=3k0+6 and the positive part is<=t,
the desired lower endpoint L(r)+h is at least k0+4 ABOVE
this minimum. If r>s,the last middle slice reaches the actual
maximum,at least U_m(r)=L(r)+rc by nonnegative rank
displacements. If r<=s,the last slice k=r-1,l1 has maximum
minus U_m(r) at least

 (r-2)s-L(r)+2r-2 >=T_r-2>0.

For Q,the first minimum is L(r) if r<=q-1. Otherwise
k0=r-q,c=S-k0>=3,its excess over L(r) is

 T_(k0)+2k0+2-(k0+1-t)_+.

Here h=L(S)+t,and L(S)-T_(k0)>=2k0+3. The lower
endpoint margin is at least1+t+(k0+1-t)_+>=2. At the
upper end,r>S again reaches the actual maximum. If r<=S,
the last maximum minus U_m(r) is at least

 (r-2)S-L(r)+r-1 >=L(r)-1>0.

These substitutions confirm BOTH required endpoints lie within
the full middle union. h0 uses ordinary interval spectra;for
t0,the conjugate equals P. Prefix bounds p>=3,q>=2 are
justified in MI339 from T_s<=h<rc and m>=6;no new large-size
assumption is introduced.

Unexpected single-slice check:m6,r=c3,h8 gives Q013568,
q2,S4. The only middle count is k2,l1. Its high pair sums
are{8,9,11,13,14};adding the low singleton interval{0,1}
gives the FULL interval[8,15],which contains the requested
[11,12]. There are ZERO middle joins to check in this case;
the endpoint proof,not an assumed adjacent slice,is essential.

**Outcome,next.** Re-derivation finds no positive middle gap or
central containment failure. It does identify an overstrong Q
bound in the review checklist wording,which is not a bound
used in the original candidate. Candidate stays PROOF-SKETCH;
Cloud still owes the remaining independent carrying derivations.
The planned self-audits are now complete. Next consolidate the
carrying proof for readability,including explicit Q endpoints
and the correct separate bounds,rather than open another guard
entry or finite census. No automatic research expansion.
Gut:the algebraic distinction is a useful surprise;the candidate
survives it for a concrete reason. Reasoned:direct endpoint and
join audit of the same infinite claim,no independent verification
or novelty upgrade. Niggle sweep:actual slice fullness proved by
a path plus a real interval;high-count endpoints included;Q
correction not bounded by1;single-middle-slice case covered;
minsize3 used where needed;central endpoints checked separately
from joins;CL436 wording distinguished from MI339's proof.
13min ACTIVE,E28/L8 OPEN.


### MI347 — B175 milestone: CL437 verifies the one-hole and four-bin results (2026-10-17 22:37 BST)

**PROVED in scope under the project's two-tier-review rule.**
During publication,the push was rejected by Cloud's new7bfdfe34.
One recovery fetch and preserving merge;CL437 read in full before
adoption. The actual incoming portal flag was subsequently seen
and ACKed after commit verification. CL437 explicitly verifies
MI337's one-hole three-bin criterion and MI339's four-bin cut
criterion,with every mathematical scope retained. This is the
requested independent review,not another author self-check.

Formal filings:G315 (original candidate d856063f) and G316
(original e90b661f),promoted from the two GPT MI waiting entries
into the second-read section of PROOFS.md. Their statements,
carrying outlines,complete notebook source pointers,review
provenance and precise limitations are recorded. G315 is the
one-hole three-bin result. G316 states:for four sizes>=3 totaling
N and integer targets totaling L(N),a partition of0..N-1 with
those sizes and sums exists IFF all14 nonempty proper subset
cut bounds hold. Necessity is immediate;sufficiency is the
least-facet reduction and complementary staircase construction.

**Review scope stays visible.** CL437 re-derived the least-slack
and pivot arguments,the two-hole spectrum/repair,the structured
three-hole repairs/coverage,the four-bin reduction,and P's
staircase algebra. It independently checked Q's correction
bound E<=min(k,S-k-1) and retained machine support for the rest
of its Q read,rather than claiming a second full hand derivation.
This was an explicit targeted carrying read under the standing
tier2 rule,not a prize-level full re-derivation. MI346 writes
out the author's Q endpoints,joins and containment directly.
The finite evidence is supporting,not an inference from small
instances to all sizes. CL436's S3 test-scope qualification at
GC1511 remains;CL437's hand spectrum reasoning is separate.

MI346 also identifies a wording issue in CL436's checklist:Q
uses its own bound1-A-B,not P's2-A-2B. The original MI339
argument and CL437's actual Q check use the appropriate E
inequality. No theorem correction or rerun is needed. The
clarification is sent with adoption for a precise shared record.

**Filing gates.** Before filing,explicit in-memory candidate units
were compared because the earlier MI headings were not native
build IDs. MI337 neighbours:G304,G305,G306;MI339 neighbours:
MI337,G304,G306. All read in full;these special eight-bin odd
constructions are not the present criteria. Native checks after
formal numbering/summaries pass for G315/G316. G315's additional
nearest G234 and G316's entry26 were also read in full;they
concern Rule30 resonance and kick alphabets. No restatement.
No generated proof pages or build scripts changed;the master and
its summary source now index the results correctly. No new
computation or unauthorized larger run.

**What is achieved,and what remains.** There is a verified piece
of mathematics in this project:the four-bin arbitrary-target
criterion with minimum size3,and its one-hole completion tool.
The bounded source audit distinguishes Kotlar's equal-sum theorem
but does not establish novelty or priority. Do not announce
a new literature breakthrough before that question is settled.
This proves no eight-bin criterion,E28/L8 threshold,or listed
prize statement;PRIZE-WON is not applicable. Older held lanes
remain held.

Delight:the complementary staircase survived an independent
reader's scrutiny,and the original scarcity/compatibility issue
now has an actual theorem in this scope. This celebration is
for the checked result,not an unverified extrapolation. Reasoned
verdict:adopt Cloud's explicit verification under the agreed
review rule,with its exact evidence scope recorded. Next:make
a concise self-contained write-up for readers outside this long
notebook,then choose the next question afresh;do not automatically
expand to a k5/k8 search just because those numbers follow4.
13min ACTIVE,no owner intervention needed.


### MI348 — B176: one proof exposition and a fresh-choice boundary question (2026-10-17 22:47 BST)

**Exposition,not a new mathematical claim.** Record searched:
`G315|G316|four.bin.*prescribed` AND`write.up|manuscript|proof|exposition`:8
hits/4 files;the current master carries outlines and notebook
pointers,not a consolidated proof. Created the hand-authored
FOUR-BIN-PARTITIONS.md:notation;one-hole scalar spectra;two-hole
localization;structured three-hole spectra;least-slack selection
and the full-interval three-bin base;the complete one-hole
three-bin proof;both staircase central spectra;literal complement
identity;the four-bin theorem;prior art and exact review scope.
All carrying calculations are included in this file. No new
mathematical branch,census or generated-page/build-script change.
Master G315/G316 now point to it.

The exposition consolidates the reviewed source blocks and the
author's explicit Q derivation. Reorganization is editorial work,
not an additional independent review. Checked internal dependency
order:the full-interval three-bin base uses only SCALAR one-hole
spectra and least slack;it does not assume the simultaneous
one-hole theorem it later helps prove. The four-bin proof uses
that theorem only in the singleton/triple branch. P/Q are literal
complements,with different join bounds. Removed stale research-log
references from the proof body;scope/provenance remains in its
last section. The candidate history is retained in this notebook.
G315/G316 retain CL437's project PROVED status and Q-review
qualification;novelty remains UNASSESSED.

**Fresh choice after the milestone.** The construction itself is
still enjoyable as a mathematical object;copy-editing is cooler
and should have an endpoint. This write-up makes the checked
argument readable,so completing it is worthwhile. Without the
investment already made,I would now choose to understand what
changes when a FOUR-bin pool has one missing value. The pull is
on whether compatibility is already encoded in ACTUAL sums of
every union,not on the numerical succession4->5 or another
larger successful run. This is a changed question,not an
automatic extension of the theorem.

**One-paragraph hand orientation/guard;no PROOFS entry or probe.**
Record searched:`four.bin|k.?5|five.bin` AND`one.hole|single.deletion|punctured`:21
hits/5 files,no exact counterpart found in that bounded record
search. On P=0..12 minus6,consider four sizes3 and targets
(8,8,28,28),total72. Each individual sum is possible (035 and
7,9,12 are witnesses). Singleton rank bounds are[3,33],pair
bounds[15,57],triple bounds[39,69];all cuts hold. But the first
pair would need a six-set of sum16. The least six-set is012345
of sum15;increasing it by1 requires the absent6,so the next sum
is at least17. Joint partition is impossible. Thus rank cuts
plus INDIVIDUAL availability,which sufficed for one-hole THREE
bins,cannot simply be reused for four. This is an elementary
route guard,not a claim of novelty or a refutation of G316's
FULL-interval theorem. No experiment or review request.

**Precise next question.** For P=0..M minus q,four sizes>=3
total M and integer targets totaling sum(P),suppose EVERY
nonempty proper bin union I has its target S_I in the ACTUAL
scalar spectrum Sigma_(C_I)(P). Does a joint partition follow?
This stronger requirement rejects the16-gap control. For three
bins it reduces by complementation to G315's condition;for a
full interval it reduces to G316's cuts. Neither fact proves
the new one-hole four-bin statement. Status OPEN. A useful
next step is one bounded hand attempt at a tight/near-tight
pair face,or a countercontrol satisfying EVERY actual-union
spectrum;no experiment until separately preregistered.

Gut:the all-union question draws more attention than another
expository pass or a large k5 census. Reasoned:the new condition
retains a necessary scarcity constraint that the naive extension
loses;it is only a candidate criterion. Niggle sweep:proof file
contains scalar derivations rather than source pointers as gaps;
review scope and novelty not inflated;the hand negative's actual
pair gap is not miscalled an individually infeasible bin;full
and punctured pools distinguished;no new formal proof or review
queue for the guard.13min ACTIVE,G315/G316 PROVED in scope,
E28/L8 OPEN.


### MI349 — B177: tight cuts and unit-slack pair cuts in the new one-hole question (2026-10-17 23:00 BST)

**Hand PROOF-SKETCH/boundary reduction,not independently reviewed.**
The full one-hole four-bin every-union criterion is OPEN. No
experiment,new PROOFS entry or review request. Record searched:
`all.union|every.union|one.hole.*four|four.bin.*one.hole` AND
`spectrum|spectra|tight|criterion`:9 hits/3 files. Sources G315,
G316,MI333's one-hole scalar spectrum,and MI336's two-hole
localization/edge characterization,read. Two bounded web queries
for an interval with a missing element and prescribed cardinalities/
sums identified no applicable new theorem;no source imported and
no literature-absence/novelty claim. Cloud flags unchanged.

Question as in MI348:P=0..M minus q,four bins of sizes>=3,
integer targets totaling T=sum(P),and for EVERY nonempty proper
bin union I,its target S_I lies in Sigma_(C_I)(P). The pull
is whether scalar scarcity of unions is the missing compatibility
constraint. Kill test:an allowed boundary target landing at an
actual missing scalar sum after selecting the forced near-minimum
pair. Unexpected check:q exactly equal to that pair's size,where
the unit increment itself is missing. Stop after the boundary
argument or a genuine countercontrol;no automatic experiment.

**1. Tight rank cuts factor the problem.** Write alpha(r) for
the ORIGINAL least r-sum. Suppose a proper union I of total
size m has S_I=alpha(m). Its tokens are forced to be the
least m original values,P0;write Q=P minus P0. For a sub-union
J inside I,its lower bound is alpha(C_J),and the lower bound
of I minus J supplies its upper bound alpha(m)-alpha(m-C_J).
For J in the other side,the ORIGINAL cut I union J gives

 S_J>=alpha(m+C_J)-alpha(m)=min_(C_J)(Q).

The complementary group within that side supplies the upper
bound. Thus both sides' actual rank cuts are inherited. Each
side is an interval with at most the one ORIGINAL hole.

Actual scalar omissions are inherited too. If the hole is in
P0,a subgroup J's possible minimum+1 would be an ORIGINAL
minimum+1 with q=C_J. Its possible maximum-1 would make
I minus J an ORIGINAL minimum+1 target with q=m-C_J. Both
contradict every-union feasibility. If the hole is in Q,a
minimum+1 for J would make I union J an ORIGINAL minimum+1
with q=m+C_J;a maximum-1 is the ORIGINAL maximum-1 of
J with q=M-C_J. These are likewise excluded. Full interval
sides have no scalar holes. All proper subgroups have size and
complement at least3,so MI333's scalar statement applies.

If I has two bins,split each side into two by its now-protected
scalar spectrum. If I is singleton or triple,its other side
(or prefix side) has three bins;G315 completes its one-hole
pool,or the verified full-interval base does. This covers ANY
tight rank cut,not just a globally closest singleton. Reflection
covers an upper-tight cut. No joint goal was assumed.

**2. A special two-hole spectrum.** Let

 R={0,...,V} minus{1,v}, 2<=v<=V,
 n=|R|=V-1, r+t=n, r,t>=3.

MI336's two-hole result localizes all missing r-sums to edge
distance1/2. For v>2,the initial rank gap is w_1=2 and the
only further gap,if v<V,is w_(v-1)=2. For v2,only w_1=3
is nonunit. Therefore,at r>=3,minimum+1 is missing precisely
when v=r+1. Minimum+2 cannot be missing:w_r cannot equal3,
and w_(r-1)=w_(r+1)=2 would require r2 because one of those
nonunit gaps must be w_1. Complementation gives the upper edge.
Thus the ONLY omissions are

 minimum+1 when v=r+1;
 maximum-1 when v=t+1.

Endpoint v=V is included by trimming it. The size condition
is actually used:at r2,t4,R={0,2,3,5,6,7},the pair minimum
is2 but4=minimum+2 is absent. This retained hand control
rejects dropping r>=3 from this special-spectrum argument.

**3. A pair one unit above its actual minimum also completes.**
Suppose bins A,B have sizes a,b,m=a+b and

 s_A+s_B=alpha(m)+1.

If q=m,the ORIGINAL m-spectrum misses alpha(m)+1,so the
every-union hypothesis already excludes this case. If q<m,
reflect ORIGINAL values in M and exchange the roles of AB and
its complementary pair CD. The reflected CD lower slack is
the old AB lower slack1,because beta(M-m)=T-alpha(m).
Its new hole M-q is ABOVE its size M-m. Hence it suffices
to treat q>m.

Now alpha(m)=L(m). The unique m-set one unit above minimum is

 P0={0,...,m-2} union{m}.

It is a one-hole m-pool with hole m-1,and has FULL a- and
b-spectra because a,b>=3 exclude its only possible one-hole
edge omissions. The original lower bounds s_A>=L(a),s_B>=L(b)
and conservation protect both requested sums inside those spectra.
Choose A,B there.

The actual complementary pool is

 Q={m-1,...,M} minus{m,q}.

Translate it down m-1. It becomes the special pool in section2
with V=M-m+1 and v=q-m+1. For either remaining size r,
P0 together with Q's r least values is exactly the ORIGINAL
(m+r)-prefix. Thus

 min_r(Q)=alpha(m+r)-[L(m)+1].

The original AB-plus-that-bin cut protects its lower bound;
the other remaining bin protects its upper bound. The special
spectrum's only lower omission requires v=r+1,i.e.q=m+r,
and a target min_r(Q)+1. That would force the ORIGINAL union
AB-plus-that-bin to have moment alpha(m+r)+1 with q=m+r,
an impossible actual scalar sum by MI333. Its upper omission
is the lower omission for the other bin. Thus neither can
be requested;choose C and its complement D. This completes
the pair-slack1 case without any global-minimum assumption.

**4. Literal hand controls.** P=0..12 minus8,sizes3^4,
targets(8,8,27,27). The selected pair is012346 of sum16,
one above the least six-sum15. Literal partition

 026 / 134 / {5,10,12} / {7,9,11}

realizes all targets. Original singleton spectra contain8 and27;
its six-spectrum is full[15,55],containing pair targets16,35,54;
triples follow by complementation. Thus EVERY union spectrum
hypothesis is met,not merely numerical rank bounds.

Unexpected q=m check:P=0..12 minus6,the earlier targets
8,8,28,28 would need the forbidden six-sum16. This confirms
why section3 must not silently take a unit-step boundary across
the ORIGINAL missing token. At a tight singleton,the related
vector3,13,28,28 passes all rank bounds and individual spectra
but fails the same AB union spectrum. Its forced A012 leaves
B's residual13 impossible. So section1's all-union inheritance
is not supplied by rank plus individual hypotheses alone.

**Outcome and exact remaining step.** The all-union candidate
now has an explicit boundary reduction covering every tight rank
cut and pair lower slack1. These are hand/unreviewed consequences
of the established scalar tools,not the full criterion. The
next natural branch is singleton slack1:its forced near-prefix
leaves THREE bins on the special two-hole pool of section2.
Knowing EACH scalar target is available does not yet show a
SIMULTANEOUS three-bin partition. G315 covers one hole,not
two;do not cite it across that missing inference. This is
a precise next hand question,not authorization for a census.

Incubator representation for that next question:replacing the special
pool's0 by1 gives the ONE-hole interval[1,V] minus v. It raises
exactly the target of the bin owning0. G315 can realize an
appropriately increased target vector,but does not by itself
guarantee that1 belongs to the bin whose target was increased.
The next test must control that ownership;do not silently repeat
the earlier unit-transfer physical-lifting gap. This is a possible
representation with an explicit obstacle,not another assertion.

Gut:surprise that the two-hole near-end shape loses its distance2
omissions once sizes are3;that makes the paired case tractable.
Reasoned:real reduction of the boundary cases,with the three-bin
two-hole compatibility obstacle still explicit. No review queue
for the routine face inheritance or scalar restatement;no new
formal proof entry until the larger question warrants one. Niggle
sweep:rank slack is relative to the ACTUAL original pool;reflection
changes hole/targets AND complementary pair;unique unit-increment
pair not used when q=m;both scalar spectra on disjoint sides
checked;size2 negative retained;no joint three-bin conclusion
from scalar feasibility.13min ACTIVE,full new criterion OPEN,
G315/G316 PROVED in scope,E28/L8 OPEN.


### MI350 — B178: every union can be feasible while four bins are incompatible (2026-10-17 23:13 BST)

**Hand counterexample and infinite family;not independently reviewed.**
The one-hole four-bin every-union criterion proposed at MI348
is FALSE. This answers that question,not G315 or G316,whose
pool/bin hypotheses differ. No experiment or new PROOFS entry.

Original signal:surprise at the small parity obstruction;
disappointment that the stronger criterion fails,but interest
in the exact distinction between union availability and joint
compatibility. This is a changed answer,not another numerical
near-miss. Record searched:`two.hole|two.missing` AND
`three.bin|three.group|compatib`:13 hits/6 files;then
`one.hole|single.deletion` AND size2/minimum2 terms:23 hits/13
files. G315,MI349,and FOUR-BIN-PARTITIONS.md sections5/6 read.
Two bounded web searches for prescribed cardinality/sum partitions
of intervals with two deletions found no applicable result imported
here. The earlier general-k source2312.00089 remains rejected;
no literature-absence or novelty claim follows from this search.

**Question and bounded hand test.** Test the
special two-hole three-bin compatibility step suggested by MI349.
Replacing0 by1 permits a one-hole theorem only if the incremented
bin receives1;existence alone cannot fix ownership. Kill test:
find individually available special-pool targets whose forced
extreme bin leaves an impossible scalar split. Stop at a proof,
a counterexample,or the unproved ownership step;no census.
The live claim and intended ownership test are B178's operational
row. Unexpected check below:restore the original missing value
and exhibit a full-interval partition,changing the cardinality
and target explicitly rather than reusing the punctured instance.

**1. The special two-hole three-bin assertion fails.** Take

 R={0,2,3,5,6,7,8,9,10}=[0,10] minus{1,4},
 sizes(3,3,3),targets(12,12,26),total50.

Each requested sum is available:12=0+2+10,26=7+9+10.
All two-bin targets are available by taking complements of
these triples. But26 is one below the maximum triple sum27,
and its UNIQUE triple is{7,9,10}. The remaining pool is

 E0={0,2,3,5,6,8}, total24.

It has no triple of sum12. An even-sum triple must contain
zero or two odd values. Its only odd values are3,5. Two odds
would need the absent4;zero odds choose three of{0,2,6,8},
whose sums are8,10,14,16. Hence no simultaneous partition.
The scalar spectrum in MI349 section2 is consistent:it speaks
about ONE subset,not three disjoint ones. The failure is the
compatibility step itself,not an erroneous scalar formula.

**2. A four-bin counterexample satisfying EVERY actual union.**
Let P=[0,12] minus6,with four sizes3 and targets

 (s_A,s_B,s_C,s_D)=(4,18,18,32), sum72=sum(P).

All singletons are feasible:4=0+1+3,18=2+4+12,
32=9+11+12. The six pair targets are22,22,36,36,50,50.
Explicit six-subsets have sums

 22: {0,1,2,3,4,12};
 36: {2,4,5,7,8,10};
 50: {5,7,8,9,10,11}.

Each is a subset of P;their uses as witnesses are independent,
as required by the proposed condition. Every three-bin union
is the complement of a feasible singleton. Thus all FOURTEEN
nonempty proper bin unions pass their ACTUAL scalar spectra,
not just rank bounds.

Nevertheless A is uniquely{0,1,3},and D uniquely{9,11,12}:
they are respectively one above the least triple sum3 and
one below the greatest33. Removing them leaves

 E={2,4,5,7,8,10}, total36.

For a triple sum18,zero odd values give only14,16,20,22;
two odd values5,7 would require the absent6. So neither B
nor C can receive its required18. This is the translated
special-pool counterexample in section1. It is not a tight
cut or a unit-slack PAIR case from MI349;it occurs at two
near-extreme SINGLETONS. MI349's boundary conclusions remain
in scope. The full proposed criterion is now rejected.

**3. Infinite hand family,including the literal example.**
For ANY integer a>=3,take

 P_a={0,...,a+9} minus{a+3}, sizes(a,3,3,3),
 s_A=L(a)+1, s_B=s_C=3a+9, s_D=3a+23.

Their total is L(a)+9a+42=sum(P_a). Single-bin witnesses are

 A={0,...,a-2} union{a};
 B or C={a-1,a+1,a+9};
 D={a+6,a+8,a+9}.

For the six-token unions B+C and B+D (or C+D),use

 E_a={a-1,a+1,a+2,a+4,a+5,a+7}, sum6a+18;
 F_a={a+2,a+4,a+5,a+6,a+7,a+8}, sum6a+32.

These are allowed six-subsets;all other pair-union witnesses
are their complements. Three-bin unions are complements of
the single-bin witnesses. Cardinalities and total conservation
therefore certify EVERY actual union for all a,without using
a general spectrum theorem or computation.

A and D above are UNIQUE,by their distance1 from the actual
lower/upper extrema;the omitted a+3 lies beyond A's prefix
and below D's top window. Their common remainder is E_a.
Translate E_a down a-3. It becomes exactly E of section2,
and its requested triple target becomes18. That parity
argument proves nonexistence for every a>=3. Increasing only
the first bin does not cure the obstruction;this makes no
claim about increasing all four minimum sizes.

**4. Independent hand controls.** Moving the two middle targets
by opposite units repairs the literal example:

 013 / {2,5,10} / {4,7,8} / {9,11,12}

has sums4,17,19,32 on the SAME P. Thus the fixed forced
extremes leave legal partitions;the exact half-sum is missing.
Unexpected check:restore6 to the full interval[0,12],increase
A's size from3 to4 and target from4 to10,so totals remain
correct. The literal partition

 {0,1,4,5} / {2,6,10} / {3,7,8} / {9,11,12}

has sizes4,3,3,3 and sums10,18,18,32. This agrees with G316
and shows why restoring the token cannot be treated as keeping
the punctured constraints unchanged. The token6 now belongs
to B,not the bin whose target was increased;the failed ownership
shortcut must not be inferred even from this successful repair.

**What changed/next cheap test.** The EVERY-union one-hole4
criterion and the special-two-hole3 individual criterion are
refuted by explicit hand examples. The weaker result was
already false;THIS negative meets the stronger hypothesis.
G315/G316 and MI349's boundary arguments
are unaffected (MI349 itself remains unreviewed). No E28/L8
result or prize claim. Send Cloud one informational READ-LEDGER
check-in with the counterexample;no routine carrying-review job.
A genuine independent read can be recorded if offered.

The next bounded hand question is whether fixing0 FIRST in
one bin makes the special-pool problem tractable when ALL
three sizes are>=4. The remaining pool[2,V] minus v is one-hole,
and its three sizes then meet G315. The missing step is choosing
an owner whose reduced target AND both other targets lie in
that actual pool's spectra. Derive those inequalities;do not
assume they follow from the original ones. This changes the
representation,not just the experiment cap. No experiment is
preregistered or run here;no automatic size sweep/minimum-size
ladder. If that choice has no direct mechanism,step back rather
than manufacture a lemma.

Gut:the clean counterexample is interesting on a fresh choice;
this is not warmth inherited from a string of positive cases.
Reasoned:the hoped-for criterion is false,and two simultaneous
near-extreme constraints expose a parity hole invisible to every
unconditioned union test. Niggle sweep:fourteen unions accounted
for through literal witnesses/complements;unique extreme bins
proved before conditioning;odd/even cases exhaustive;translation
and cardinalities checked for all a;positive control changes
constraints explicitly;no computational or novelty claim;no
status upgrade by instinct.13min ACTIVE.


### MI351 — B179: choose zero's owner before invoking the one-hole theorem (2026-10-17 23:25 BST)

**Hand PROOF-SKETCH G317;targeted independent read pending.**
Full statement and carrying proof:PROOFS.md waiting-room G317.
No experiment or numerical extrapolation. Novelty UNASSESSED.
This is a new positive compatibility candidate after MI350's
negative,not an assertion that the failed minimum3 criterion
can be reused. The uniform minimum4 is substantive:fixing0
reduces its owner's cardinality by1,and G315 requires3.

**Actual pull before explaining.** The replacement0->1 route
still bothers me because ownership is physical,not just a
change to a target vector. Fixing0 FIRST feels cleaner:the
problem becomes choosing among only three possible owners,
with exact scalar tests. Warmth is attached to that mechanism,
not to obtaining another statement at a larger minimum size.
Kill test:two bins that BOTH need0,or no bin able to accept0,
while the original individual feasibility and total still hold.
Stop after either budget contradiction or an explicit countercontrol;
no automatic experiment. The B179 operational claim records this
bounded question. Unexpected check:an actual UPPER
scalar hole for a reduced owner,not merely its rank maximum.

Record searched:`fix.*zero|zero.*owner|special.two.hole|minus.*1,v`
AND`spectrum|feasib|three`:109 hits/32 files,broad query with
unrelated matches;the relevant sources are MI349/350 and G315.
G315 and FOUR-BIN-PARTITIONS.md sections2,5,6 read. Two bounded
web queries combining three-bin partition/two holes/sums and
prescribed cardinalities/missing integers imported no theorem.
No current-priority or literature-absence claim. Cloud flags
unchanged;one fetch/merge up to date.

**Exact statement.** R=[0,V] minus{1,v},2<=v<=V. Three sizes
a,b,c>=4 sum V-1;integer targets total sum(R). Individual
actual subset feasibility is sufficient for a joint partition.
Necessity is immediate. This does NOT cover the three size3
bins in MI350 or arbitrary two-hole locations.

**Mechanism and carrying calculations.** Put Q=R minus0,
a ONE-hole interval[2,V] minus v. For each original bin i
of size k_i,write A_i if its target is in Sigma_(k_i)(Q),
B_i if it is in Sigma_(k_i-1)(Q). Original feasibility is
exactly A_i OR B_i. We must choose j with B_j and all
others A_i. Then apply G315 on Q,sizes k_j-1,k_i,k_l;
all are>=3 and their sums/cardinalities total Q's. Add0
back to j. No theorem is asked to put a token in an owner
that was chosen after seeing its partition.

Let alpha,beta be Q's actual rank sums. The one-hole scalar
lemma gives,under original feasibility,

 not A_i => s_i<=alpha(k_i)+1;
 not B_i => s_i>=beta(k_i-1)-1.

For the first implication,Q's only upper interior gap is
maximum-1;no containing0 subset can fill it because its
maximum beta(k_i-1) is more than1 below beta(k_i).
For the second,the minimum with0 is alpha(k_i-1),and a
minimum+1 hole in its reduced spectrum cannot be supplied
by an omitting0 subset:alpha(k_i)>alpha(k_i-1)+1.
All relevant sizes AND their complements in Q are>=3,so
these are the scalar lemma's full exception list. Endpoint
v2/V cases are full intervals and only remove exceptions.

If two bins a,b failed A,conservation and the third bin's
original maximum would give

 alpha(a+b-1)<=s_a+s_b<=alpha(a)+alpha(b)+2.

But with d=v-2,the actual formula
alpha(t)=2t+L(t)+(t-d)_+ gives

 alpha(a+b-1)-alpha(a)-alpha(b)-2
 >=ab-a-b-4=(a-1)(b-1)-5>=4.

The positive-part correction is>=-1;when d<=min(a,b) it
is d-1,and beyond that range it is nonnegative. Thus at
most one A fails. If it exists,original A OR B forces B
for that bin:the owner is determined.

If no A fails,we still need SOME B. Suppose all three B
failed,and put n=a+b+c=V-1. Since a one-hole pool's
largest r values dominate the largest r values of[2,V-1],

 beta(r)>=r(V-1)-L(r), sum(Q)<=V(V+1)/2-3.

Therefore

 sum(beta(k_i-1))-3-sum(Q)
 >=ab+ac+bc-3n-4
 =8+5(x+y+z)+xy+xz+yz>=8,

where a=4+x,b=4+y,c=4+z. The lower bound for three B
failures would exceed the prescribed total. At least one B
exists. Choose it if no A failed. This completes the owner
selection and the G315 application. Formal file includes every
carrying step and labels the statement PROOF-SKETCH.

**Literal hand controls.**
1. Lower A-gap rather than rank failure:R=[0,13] minus{1,6},
sizes4^3,targets15,24,45. Witness partition

 {0,2,3,10} / {4,5,7,8} / {9,11,12,13}.

Q has four-minimum14 but its sum15 is missing (hole6 equals
4+2). The first bin MUST own0 despite being above Q's minimum.
Its reduced triple sum15 is available;the three residual bin
sizes are3,4,4. The criterion checks ACTUAL spectra,not just
bounds.

2. No A failure,but not every bin accepts0:R=[0,13] minus{1,4},
targets20,20,46,sizes4^3. A literal partition is

 {0,3,8,9} / {2,5,6,7} / {10,11,12,13}.

All three targets are available as Q four-sums,whereas46
exceeds Q's triple maximum36. The proof chooses an eligible
owner;it does not claim every original bin can contain0.

3. Unexpected UPPER B-hole:R=[0,13] minus{1,10},targets
22,23,35,sizes4^3. A literal partition is

 {0,4,7,11} / {3,5,6,9} / {2,8,12,13}.

Q's triple maximum is36,but35=maximum-1 is MISSING because
its hole10 equals13-3. Thus the third bin cannot own0 even
though its reduced rank bounds hold. The other bins provide
owners. This tests the -1 allowance in the B-failure bound.

4. Retained minimum3 negative:MI350's[0,10] minus{1,4},
targets12,12,26 has no joint partition. Fixing0 in a size3
bin leaves size2;G315 cannot be invoked. The theorem does
not smooth over that failure. Unequal-size arithmetic check:
at(a,b,c)=(4,4,10),n18,V19,the coarse all-B-failure budget
margin is96-54-4=38;not just the equal-size margin8.

**What this changes and what remains open.** There is a
candidate compatibility theorem on the SPECIAL two-hole pool
at uniform minimum4,with a direct owner-selection mechanism.
The failed every-union four-bin minimum3 statement remains
FALSE. The full interval G316 and one-hole G315 remain as
reviewed;E28/L8 and broader-bin criteria remain OPEN. No
independent verification or novelty is claimed for G317.

Conditional application worth a next hand check:a singleton
one unit above minimum in an original one-hole four-bin pool
leaves the special two-hole shape when its original hole lies
above that singleton's size. Other-bin sizes>=4 permit G317
if their residual scalar feasibility is protected by the original
all-union conditions. Check that inheritance directly;do not
claim the interior four-bin criterion from a boundary case.
This is an exact next inference,not an automatic size ladder
or larger census;pending review is a labelled dependency,not
a permission wait.

**Review cost and niggle sweep.** This is a genuine compatibility
proof candidate using a new owner-choice argument,not a known
scalar theorem reproof or routine guard. Request ONE targeted
read of the A/B failure classifications and the two budget
contradictions;G315 was already reviewed. Formal native duplicate
check W317:335 entries,no repeats;G315,G294,G316 read in full,
also after summary insertion. G315 is a dependency,G316 a full
interval four-bin result,G294 Mahler. No generated pages changed.
Niggles checked:remove0 changes COUNT but not TOTAL;targets
stay unchanged;owner's size reduces before G315;all reduced
sizes/complements legal;both scalar gaps retained;strict budget
margins4 and8 recomputed;endpoint holes included;the sharpness
countercontrol unchanged;no experiment counted as proof.
Gut:the representation is satisfying because it resolves the
ownership issue rather than concealing it. Reasoned:complete
hand candidate with a short carrying argument,still pending
independent scrutiny.13min ACTIVE.


### MI352 — B180: inherited spectra and a short near-singleton boundary band (2026-10-17 23:40 BST)

**Hand PROOF-SKETCH;the owner argument and new boundary claims
are not independently reviewed.** G317's original statement at
47bfd2de and its targeted request remain unchanged. No new
PROOFS entry or review queue. No experiment. The all-union
criterion at uniform minimum3 stays FALSE by MI350;the separate
uniform-minimum4 interior question stays OPEN.

Question claimed in B180:does singleton slack1 completion
really inherit every G317 scalar hypothesis,for ALL original
hole positions? Does the same owner mechanism reach slack2?
Stop at that inheritance calculation or an explicit allowed
countercontrol;no census. Pull:the new token-owner choice may
replace case-by-case repairs,but only if residual feasibility is
proved. Unexpected check:the first value L where the strict
budget disappears,without calling it a counterexample.
Record searched:`singleton.*slack1|unit.slack.*singleton|near.singleton|MI351`
AND`inherit|four|residual`:3 hits/2 files;then
`isolated.zero|zero.owner|prefix.*slack|singleton.*slack`
AND`four|two.hole|G317`:16 hits/7 files. Relevant sources
MI349-351,G315,and FOUR-BIN-PARTITIONS.md scalar lemma read.
No new literature mechanism imported:the extension below is
an explicit re-calculation of the same owner budgets,not a
claim of prior-art absence or novelty. Flags unchanged.

**1. The same owner proof tolerates a short initial gap.**
Let

 H={0} union Q, Q=[L,V] minus{w}, 2<=L<=5, L<=w<=V,
 three sizes a,b,c>=4, n=a+b+c=V-L+1.

Targets total sum(H)=sum(Q) and are individually feasible in H.
Use MI351's A_i/B_i meanings,with Q's rank sums alpha,beta.
The SAME scalar classifications hold:

 not A_i => s_i<=alpha(k_i)+1;
 not B_i => s_i>=beta(k_i-1)-1.

The proof uses only the one-hole spectrum and the fact Q's
values are>=2:an omitting0 subset cannot fill the reduced
minimum+1 gap,and a containing0 subset cannot fill the
unreduced maximum-1 gap. No special location of w is required;
endpoint w=L/V just trims Q to a full interval.

Put d=w-L and write T(t)=t(t-1)/2. The exact prefix formula is

 alpha(t)=L*t+T(t)+(t-d)_+.

Two A failures would require
alpha(a+b-1)<=alpha(a)+alpha(b)+2 as before. But

 alpha(a+b-1)-alpha(a)-alpha(b)-2
 >=ab-a-b-L-2>=6-L>=1.

The positive-part correction is still>=-1. Thus at most one
A fails. For the B budget,V=n+L-1 and

 beta(r)>=r(V-1)-T(r),
 sum(Q)<=[V(V+1)-L(L+1)]/2.

(The upper total removes the least possible missing value L.)
Substitution yields

 sum(beta(k_i-1))-3-sum(Q)
 >=ab+ac+bc-3n-2L
 =12-2L+5(x+y+z)+xy+xz+yz>=2,

where a=4+x,b=4+y,c=4+z. Hence at least one B holds.
Choose the exceptional A-failure bin,if any;otherwise any B
bin. Apply G315 to the actual Q with that owner's size reduced
by1,and add0. This is a hand extension of G317's mechanism,
not a status upgrade or a claim that its existing review has
already covered these larger gaps.

**2. The actual H scalar spectrum needed for inheritance.**
For an H subset size r>=4 with complement t>=8,

 Sigma_r(H)=Sigma_r(Q) union Sigma_(r-1)(Q).

The first convex range starts at alpha(r) and ends beta(r);
the second starts alpha(r-1) and ends beta(r-1). Each one-hole
spectrum has only its possible edge-distance1 gaps. Moreover

 beta(r-1)-alpha(r)
 >=(r-1)t-2r-L+1>=12.

Here beta(r-1)>=(r-1)(V-1)-T(r-1),
alpha(r)<=Lr+T(r)+r,and V=r+t+L-1.
Thus the two ranges overlap by at least13 integers. Their
inner omissions are filled:alpha(r)+1 is strictly interior
to the (r-1)-range,and beta(r-1)-1 is strictly interior to
the r-range. The outer minima/maxima are separated by at
least L>=2,so those gaps cannot silently fill one another.
Consequently the ONLY possible H omissions are

 min_r(H)+1 when w=L+r-1;
 max_r(H)-1 when w=L+t-1.

This is a direct union of two actual scalar spectra,not an
assumption of joint three-bin completion. Endpoint w=L/V
removes exceptions. All invoked Q subset sizes and complements
are>=3. The robust overlap also rules out a coincident pair
of inner gaps;merely overlapping convex ranges would not suffice.

**3. Four-bin boundary band when the original hole is above a.**
Original pool P=[0,M] minus q,four sizes a,b,c,d>=4,total M,
and EVERY nonempty proper union has its target in its actual
scalar spectrum. Let selected bin A have

 s_A=T(a)+h, 1<=h<=4, q>a.

This is h above its ACTUAL minimum,as q>a. Since a>=4>=h,
choose the legal set

 A0={0,...,a-h-1} union{a-h+1,...,a}.

It is the least a-set with its last h values shifted up1;
its size is a and its sum T(a)+h. At a=h its first prefix
is empty,not an excluded case. Its actual complement is

 R={a-h} union([a+1,M] minus q).

Translate down a-h. This is H from section1,with
L=h+1,V=M-a+h,w=q-a+h. Every residual size is>=4.

For any nonempty proper residual bin union J of size r,
A0 together with the r least tokens of R forms the ORIGINAL
(a+r)-prefix. Therefore

 min_r(R)=alpha_P(a+r)-s_A.

Original A-plus-J feasibility supplies its lower bound;
the complementary residual group supplies its upper bound.
Section2's possible lower omission requires
w=L+r-1,which is exactly q=a+r. Asking for min_r(R)+1
would then ask the ORIGINAL A-plus-J group for
alpha_P(a+r)+1 at cardinality q:an actual missing scalar
sum in P. The all-union hypothesis excludes it. An upper
omission is the lower omission of the residual complementary
group,and is excluded in the same way. Thus every requested
residual SINGLE-bin target is actually available. Section1's
owner construction completes the three bins,provisionally.

This proves the stated boundary BAND as a hand candidate.
It does not establish the minimum4 interior criterion,does
not cover q<=a at h2..4,and does not turn the old minimum3
counterexample into a positive case.

**4. Complete hole-position check at singleton slack1.**
If q=a,the selected target alpha_P(a)+1 is itself missing
and the hypothesis excludes it. If 0<q<a,the unique near-prefix
is

 A0=({0,...,a-1} minus q) union{a+1}.

Its complement is[a,M] minus{a+1},a ONE-hole pool whose
normalized hole is1. The same original-prefix identity protects
all residual rank bounds. Since remaining sizes>=4 and their
complements>=8,this one-hole pool has NO scalar omissions:
hole1 cannot equal either cardinality. Reviewed G315 completes
it. If q>a,section3 with h1 applies. Original endpoint q0/M
cases are full intervals and G316 already covers them. Reflection
of ORIGINAL values,targets and q covers upper slack1. Thus
all singleton unit-slack hole positions are accounted for,
with the q>a compatibility dependency still unreviewed.

**5. Literal controls and the stopping edge.** P=[0,16] minus8,
sizes4^4,has the partition

 {1,2,3,4} / {0,5,6,7} / {9,10,11,12} / {13,14,15,16}

with sums10,18,42,58,total128. Here a=h=4,so the low prefix
is EMPTY;the residual starts with isolated0 then[5,16] minus8.
It tests the h4 geometry and total,not just h1 by translation.
The residual minimum four-sum is18,but19 is absent. The
corresponding ORIGINAL A-plus-that-bin eight-sum29 is likewise
missing:its minimum28 misses+1 because q8. Thus actual-union
feasibility supplies a necessary exclusion that rank bounds alone
would lose. The literal partition uses18 and passes every union.

Unexpected stopping-edge control:at L6,a=b=c4,both coarse
strict margins become0. Our argument does NOT extend there.
That is not a counterexample:H={0} union[7,17] (take w=L6)
partitions as

 {0,7,8,9} / {10,11,12,13} / {14,15,16,17}

with sums24,46,62,total132. This keeps the distinction between
a failed sufficient bound and nonexistence. No automatic increase
of L or a scan follows from it. Unequal-size budget at L5,
(a,b,c)=(4,4,10),is96-54-10=32>0;the algebra is not using
three equal sizes in disguise.

**Outcome/fresh choice/niggle sweep.** The provisional owner
argument now has a finite boundary use,with exact scalar
inheritance. G317's original proof/request remains as published;
no additional review queue or formal lemma for these consequences.
The warm part is the ownership mechanism and the overlap proof,
not merely having increased a slack bound. The boundary work
has reached its stated budget. Next inspect the minimum4
INTERIOR first-bin obstruction,where generic two-hole three-bin
compatibility is still unavailable;do not simply enlarge h.
A new computation would need its own preregistration and caps.
Niggles checked:original and translated holes not conflated;
original prefix identity uses actual ranks;h<=a and empty prefix;
Q loses a count but no sum;all scalar gaps accounted for;inner
holes filled by INTERIOR values,not convex hulls;reflection
changes targets and hole;L6 zero margin not called falsehood;
MI350 minimum3 negative retained;every new claim unreviewed.
Gut:the trajectory adjustment has produced a useful mechanism.
Reasoned:an explicit hand boundary reduction,with the central
compatibility problem still real.13min ACTIVE,E28/L8 OPEN.


### MI353 — B181: a known pairing method opens a central region without a gap catalogue (2026-10-17 23:55 BST)

**Known-method hand application,not a generic compatibility theorem.**
Full finite coin proof and paired-window calculation are filed in
PRIOR-ART.md under Adjacent-pair subset-sum completion. No new
PROOFS entry,review request or experiment. G317's existing request
is unchanged and none of its unreviewed premises is needed here.

Question claimed:generic two-hole THREE-bin compatibility at
minimum4 is an interior obstruction for the one-hole four-bin
minimum4 question. I first considered proving a complete
three-hole scalar gap catalogue. That is still unproved here;
no assumption that all its gaps are within3 of the ends is
used. The pull shifted to whether central completion could be
certified without answering that harder scalar question.
Relief at a shorter representation,alongside uncertainty about
its reach. This is a real trajectory change,not a larger h.

Record searched:`two.hole|two.deletion` AND
`three.bin|three.group|compatibility`:16 hits/4 files,relevant
MI336/349-352 and G315. Primary search queries were restricted
subset sums/dense intervals/deletions/holes. Read Károlyi,
CWI PNA-R0801,[primary PDF](https://ir.cwi.nl/pub/13654/13654D.pdf),
printed pages1-5,introduction and Lemmas6/7 with proofs. The
paper's n>=89 balanced theorem is NOT applied to our small
pools. The finite signed-sum/coin-completeness METHOD supplies
the useful calculation;read scope is recorded in PRIOR-ART.
No novelty or literature-absence claim. Cloud flags unchanged.

**Bounded hand test.** Seek a central interval certificate for
an arbitrary pool with three holes and subset/complement sizes
at least4,or an exact countercontrol to that certificate. Stop
at its actual central band,not a claim about every scalar sum.
Unexpected check:remove the strict h<r condition in the PAIRED
recipe while retaining an actual subset witness,so a failed
recipe is not confused with a nonexisting sum.

**Calculation in brief.** For an ordered pool z_0,...,z_(n-1)
with at most h deletions from an integer interval,take any2r
consecutive AVAILABLE values and pair adjacent ranks. Each pair
offers a positive difference e_i. The number of missing integers
inside those disjoint gaps is sum(e_i-1)<=h. If h<r,the
known coin-completeness induction gives every subset sum of
the e_i between0 and their total. Thus choosing one value
from each pair gives a FULL interval[K_j,H_j],whose endpoints
are respectively the even/odd ranks in that window.

For completeness,the finite criterion's only obstruction would
be a first sorted coin exceeding1+the preceding total. After k
coins,every remaining coin would then be>=k+2,requiring at
least(r-k)(k+1)>=r total excess over1,contradiction. This
is a known elementary argument,reproved in PRIOR-ART,not a
new theorem filing. Sliding the window ONE available rank
makes its new lower endpoint exactly the previous upper
endpoint. Therefore all those intervals meet and certify

 [sum(z_(2i):i<r),
  sum(z_(n-2r+2i+1):i<r)] subset Sigma_r(pool).

When n2r this band is symmetric about half the TOTAL and
has width sum(e_i)>=r. For arbitrary n>=2r it remains an
explicit central band;no symmetry about total/2 is claimed.
If the desired smaller-bin sum lies inside it,choose its pair
values in the appropriate window,and take the whole remaining
pool as the other bin. These are actual disjoint selections.

**Interior first-bin use.** Start with ANY two-hole interval
pool P and prescribed three-bin targets/sizes. If its first
bin A is a LEGAL prefix/suffix/pivot recipe of its prescribed
size and sum,then R=P minus A is an integer interval with
at most3 deletions. For b,c>=4,put r=min(b,c),n=b+c.
Here h<=3<r,so the displayed central band of R is a sufficient
certificate for the smaller-bin target. This argument does
not need G317 and is not a near-singleton slack theorem.
It deliberately does NOT assert that a legal first-bin recipe
always exists:its formal pivot may be one of the two absent
values. Nor are original rank bounds asserted to put the target
inside this narrower central band. Those are live selection
obstacles,not hidden hypotheses.

**Unequal-size literal hand control with interior holes.**
Take P=[0,14] minus{4,9},sizes(4,4,5),targets(15,33,44),
total92. Choose A={0,1,2,12},a legal prefix/pivot recipe.
Its actual remainder is

 R={3,5,6,7,8,10,11,13,14}.

It is[3,14] with4,9,12 deleted. Here n9,r4. First-window
lower sum is3+6+8+11=28;last-window upper sum is
6+8+11+14=39. Thus the CENTRAL band contains33. Using
the first window,adjacent-pair differences are2,1,2,2.
Its lower sum28 needs increment5=2+1+2,which yields

 B={5,7,10,11},sum33;
 C={3,6,8,13,14},sum44.

Together with A these cover P exactly. The first-bin lower
slack is15-6=9,not the earlier h<=4 band;the two ORIGINAL
holes are interior. Unequal b,c are used,so a balanced-half
shortcut has not been silently applied. This is a hand witness,
not an enumerated-domain result.

**Unexpected strict-bound negative for the RECIPE only.**
R={0,2,3,5,6,8,9,11} has h4,r4. Its adjacent differences
are all2,so the fixed paired recipe gives only even sums
18,20,22,24,26 and misses21. An actual FOUR-set{0,2,8,11} nevertheless has sum21,
and its complementary four-set{3,5,6,9} has sum23.
Thus dropping h<r breaks the claimed full paired interval,
but does NOT refute actual scalar or two-bin feasibility.
The retained mismatch is intentional and can falsify a
rank-only or convex-hull-only reading of the recipe.

**What changed and exact remainder.** The scalar-centre part
of the interior question now has an explicit cheap certificate
from a known method. A full three-hole gap classification is
not required in that region. Generic two-hole3/minimum4
compatibility and one-hole4/minimum4 compatibility remain OPEN;
this is not a proof of either. A niggle changes the next step:
the end-supported first-bin recipe usually has NO boundary
freedom at fixed moment. Its consecutive extreme-count ranges
meet only at the same actual set. I must not promise a
moment-preserving boundary move inside that recipe. Instead,
keep the first bin fixed and vary the PAIRING certificate.
The refinement below does this without a census or review wait.

**Fixed-prefix pairing reaches a uniform scalar interior.**
Assume r<=t=n-r. For k=h+1,...,r,fix the first r-k available
values,and pair sliding2k-windows after them. The coin excess
is still<=h<k. This gives full intervals[A_k,B_k],with

 A_k=sum(z_i:i<r-k)+sum(z_(r-k+2j):j<k),
 B_k=sum(z_i:i<r-k)+sum(z_(n-2k+2j+1):j<k).

A_(k+1)>A_k by k positive adjacent gaps. B_(k+1)-B_k
=z_(n-2k-1)-z_(r-k-1)>0. For their join,cancel the common
prefix through rank r-k-1;the remaining indices in B_k are
n-2k+1+2j,those in A_(k+1) are r-k+1+2j,j<k.
They differ by t-k>=1,so B_k-A_(k+1)>=k(t-k)>0.
All ranges join. Reflected ranges join from the upper end;
both families contain the ordinary central paired-window band,
so they overlap. No convex hull replaces a missing inner value.

For k=h+1,A_k differs from the actual r-minimum by T(k)
from unit rank spacings,plus at most h*floor(k/2). The latter
bound follows by counting alternating selected versus initial
consecutive ranks ABOVE each missing-value gap:the maximum
excess count is floor(k/2). All earlier prefix values cancel.
Consequently every integer in

 [min_r+D_h,max_r-D_h],
 D_h=T(h+1)+h*floor((h+1)/2),

is available. The same construction reflected gives the upper
endpoint bound. For h3 this is D3=6+3*2=12,independent of
pool size or hole locations. It is deliberately COARSE,not
the unproved claim that all gaps are within3 of the ends.
The full derivation is attached to the known method in PRIOR-ART;
no additional theorem filing or novelty claim.

**Concrete use in the claimed interior branch.** In a generic
two-hole THREE-bin pool,choose the globally least singleton
slack and orient it lower,as in the verified rank selection
argument. If its actual first-bin recipe has a LEGAL pivot
and a positive high suffix of k>=1 tokens,its remainder has
at most3 holes. The protected original bound F_r exceeds
the actual residual minimum by at least k*r (ordered-rank
argument,unchanged by the second original hole). If BOTH
remaining bin sizes are>=12,the lower and complementary
upper margins are>=12. The desired smaller-bin target lies
inside the new certified scalar interior,and completes.

This is a known-method hand closure of one named interior
branch,not the generic theorem. It uses no pending G317 step.
The first-bin pivot may still be absent,and the case with
zero suffix or a remaining size4..11 is not covered by this
coarse bound. Next cheap hand test:use the ACTUAL pair-gap
counts in that small residual range rather than require the
worst-case h3 for every window. No automatic parameter sweep,
full gap catalogue assertion or larger census is authorized
by this paragraph. G317's review can proceed separately.

Gut:interest in replacing a growing hole-case tree by a single
certificate. Reasoned:known-method central coverage and a real
interior completion,with selection/generic compatibility still
missing. Niggle sweep:holes counted inside disjoint pair gaps;
positive coin differences and strict excess bound;window joining
uses AVAILABLE ranks;four-set counts in the negative;unequal
complement recovered from TOTAL;actual first bin legal;fixed first-bin moment gives no assumed
boundary freedom;pairing-family joins and rank counts checked;
no full spectrum or independent-review claim.13min ACTIVE,E28/L8 OPEN.


### MI354 — B182 preregistration: a finite basis for the three-hole scalar bottleneck (2026-10-18 00:04 BST)

**NOT RUN. Hand reduction plus a frozen experiment design.**
The current interior obstruction calls for a sharper scalar bound
than MI353's12. Blind prediction:for an interval with at
most3 deletions and subset/complement sizes r,t>=4,the ONLY
missing scalar sums lie within distance3 of an actual extreme.
A counterexample would reject this premise and redirect the
interior proof;it does not refute G315/G316/G317.

Record searched:`pair.*window|fixed.prefix.*pair|pair.*completeness`
AND`hole|scalar|spectrum`:24 hits/14 files,relevant MI353 and
its PRIOR-ART derivation. Original two-hole localization MI336
and MI353 source method are the known controls;no new primary
literature claim. Pull:the fixed buffer leaves only a finite
edge question. This offers a decisive kill test rather than
an arbitrary larger sample. Surprise/unease:the plausible bound3
might fail in a very small normalized rank window;keep that
possibility alive. No instinct upgrades the prediction.

**Hand finite reduction,not yet independently reviewed.**
Write alpha for the actual r-minimum. MI353 covers every
integer at distance>=12 from BOTH extrema. It is therefore
enough to check lower offsets d=4,...,11 and their reflected
upper counterparts. For a target<=alpha+11:

- If r>11,every one of the first r-11 AVAILABLE values
  is forced. Omitting rank j<=r-12 requires replacing it
  by rank>=r,cost at least r-j>=12.
- If t>11,no rank>=r+11 can be selected:replacing even
  the largest initial selected rank r-1 by r+11 costs>=12.

Remove that forced prefix and discard the forbidden upper tail.
The remaining segment has r'=min(r,11),t'=min(t,11),both
in4..11. It is still an integer interval with<=3 deletions.
Translate its least value to0. Lower offsets d are unchanged;
add the fixed prefix back to lift a subset. Thus the exact
finite basis is all normalized pools with r',t' in4..11,
endpoints0,U retained,and U=r'+t'-1+h,h=0..3. Its internal
holes are every h-subset of1..U-1. Reflect to handle the
upper end. This is a finite-basis reduction,not extrapolation
from a guessed cutoff;its correctness remains a hand premise.

**Frozen source and scope.**
`tests/probes/instinct/three_hole_scalar_basis.py` is saved and
syntax-compiled only. It enumerates the ENTIRE basis,not targets
of the partition problem. B182-P predicts all offsets4..11.
C0:three complete literal small spectra versus bitset DP;known
h<=2 scalar localization on the whole relevant basis.
C1:primary deleted-value domains/DP versus independent rank-gap
multiset domains and complete near-minimum rank-shape enumeration;
compare ALL offsets0..11,including holes,consume every domain key
once,and verify every retained witness literally. Integer rank
excess<=11 exhausts the near-edge subsets because physical
excess is at least rank excess. Check the independent binomial
case-count formula too.

Counterfactual:allowing r=t3 must FAIL on[0,8] minus1,4,7:
min5,max19,missing12,seven from BOTH extremes. Confirm by literal
subsets and the independent near-edge map. Unexpected check:
three larger/asymmetric pools AND reflections test the reduction
for every offset0..11,with literal lifted witnesses. These
fixtures are preregistered in the source;not another search.

ONE unchanged-source run. Stop at first failed control as
INSTRUMENT-FAILED,first independently confirmed blind counter as
REFUTED,or20CPU/30wall/128MiB/256KiB cap as UNKNOWN;external
35s watchdog. No patch/retry,domain expansion or cap increase.
Local receipt only,no raw portal upload. Push this checkpoint
before execution. A pass would be an exact finite COMPUTED
basis result;the universal conclusion still needs the hand
reduction and known-method coverage checked independently.
No new review queue or PROOFS entry yet.13min ACTIVE.


### MI355 — B182 outcome: complete finite scalar basis passes;legal interior branch reduces (2026-10-18 00:06 BST)

**COMPUTED finite basis,same-worker independent implementations.**
ONE run of the unchanged MI354 source at1981ffe0 completed.
Original source SHA256:
`a517042e178d0c64a9d700c84d646642b77c92ff6d5b54512c9c4cc3ce9fb351`.
No patch/retry,domain expansion or cap increase. Its output is
local only;no raw portal upload or additional review job.

B182-P PASS on EVERY48896 normalized basis case:

 h0:64; h1:896; h2:7056; h3:40880.

All requested offsets4..11 are present. The independent rank-gap
domain/rank-shape implementation matches ALL586752 offsets0..11,
including the actual omissions near the endpoints. Every domain
key consumed exactly once,the binomial counts agree,and every
retained witness is checked literally. C0's3 full literal spectra
and known h<=2 localization controls PASS. The size3 counterfactual
correctly finds missing12 on[0,8] minus1,4,7. Unexpected larger
asymmetric truncations/reflections PASS with71 literal lifted
witnesses. These are independent algorithms/encodings in ONE
worker's run,not a replication by Cloud or an external proof read.

CPU8.200965s,internalwall8.231048805s,externalwall8.295247591s;
peakRSS27,283,456B;stdout464B,stderr0B,exit0. No cap reached.
Witness-map digest:
`07b262bbf8341429b9818a7334d1e20ac2ea453a9f2576f8ed1899f6b5162dd1`.
Raw-result SHA256:
`f520433105262cf770442b97e81b9946c051712c9d03c79bca0f2e8a89c0b816`;
external-receipt SHA256:
`eb3cee15984f50558c6495cb2648d40aabbe891567929064547f8721baf5efd6`.
Receipts remain outside git;source and all printed outcomes are
committed. Appended OUTCOME metadata changes the file's present
hash;the executed algorithm/source hash above remains recoverable
from the preregistration commit. Syntax check is not a rerun.

**What the computation implies,and its hand premises.**
The experiment checks the COMPLETE exact basis from MI354,
not a size sample. Its universal interpretation still depends on
MI353's paired-window buffer12 and MI354's forced-prefix/tail
reduction. Both are hand calculations awaiting independent scrutiny.
Conditional on those steps,the result proves that a pool with
<=3 deletions and r,t>=4 misses scalar sums only at distances
1,2,3 from its ACTUAL extrema. No possible omissions beyond3
survived. No classification of WHICH edge sums fail is supplied.
Do not promote the conditional universal statement to independently
PROVED or confuse it with simultaneous three-bin compatibility.

One reduction niggle rechecked:rank-displacement cost of ANY
near-minimum subset is at most its physical excess,because
z_(j+u)-z_j>=u. Thus the rank-shape enumeration really exhausts
all offset<=11 subsets,not only the witnesses it happens to
find. Removing an initial rank j<=r-12 or using rank>=r+11
costs>=12;the translated segment has exactly r'=min(r,11),
t'=min(t,11),with at most3 internal deletions. End deletions
trim and translate,so the endpoint-retained normalized basis
loses no case. Reflection supplies the upper-edge basis;no
same-worker check is described as an independent carrying read.

**Immediate interior consequence,conditional/unreviewed.**
Return to a TWO-hole pool with three bin sizes>=4,individually
feasible targets and total conservation. Choose the least of
all six singleton slacks and reflect the ORIGINAL problem to
orient its selected bin A lower. As in the verified any-ordered-
pool rank argument,the remaining size-r target is protected by

 F_r=alpha_P(a+r)-alpha_P(a).

Suppose A's actual end-supported prefix/suffix/pivot recipe is
LEGAL. With l low tokens,k high tokens,l+k=a-1,the residual
R has at most3 deletions. Its actual r-minimum is at most
sum(z_(l+1),...,z_(l+r)),where z are ORIGINAL available ranks.
Consequently F_r-min_r(R)>=k*r. If k>=1,this is>=4 for
B and C. Their lower/complementary upper targets lie outside
all possible scalar gaps by the new conditional distance3 bound.
So the residual two-bin partition exists. This removes the
previous artificial residual-size12 threshold in that branch.

If k0,put v=z_(a-1),the first remaining middle value,and p
for the actual pivot. The same bound is exact here:

 F_r-min_r(R)=min(p-v,z_(a-1+r)-v).

The second term is>=r>=4. If the selected lower slack
h=s_A-alpha_P(a)=p-v is>=4,again both margins are>=4.
Thus EVERY LEGAL-pivot interior case h>=4 completes at all
remaining sizes>=4,not merely equal or large sizes. For upper
omissions use the other remaining bin's same lower comparison,
not an unjustified reflection of only the scalar target.

**Exact remaining cases/next cheap test.** A generic two-hole
THREE-bin theorem at minimum4 is still OPEN. The remaining
selected-bin cases are h0..3,or a FORMAL pivot which is one
of the two absent original values. In the latter case the
usual balanced pair repair can leave FOUR holes;the three-hole
certificate cannot simply be reused. If both original holes
are inside that residual span,this is a real new structured
spectrum question. No automatic four-hole scan is authorized.
Next hand test:write that actual repaired residual shape and
its protected original-rank margins;seek a countercontrol in
those protected targets or a representation that avoids the
fourth deletion. Near-minimum h0..3 remains a separate finite-
geometry branch,not assumed resolved by G317.

Gut:satisfaction that a potentially decisive finite test answered
its exact question,with a remaining obstruction I can name.
Reasoned:finite basis complete and independently self-checked;
universal interpretation and branch reduction remain hand-
unreviewed. This is movement from an artificial buffer12 to
actual gap distance3,not proof by extrapolation. Niggle sweep:
all controls reached,counts/edge reflection/truncation and literal
lifts checked;source unchanged during execution;missing pivot
not treated as legal;four holes not called three;no partition
or novelty/prize claim from scalar success.13min ACTIVE,
G317 request unchanged,G315/G316 in scope,E28/L8 OPEN.


### MI356 — B183 claim: near-minimum two-hole compatibility (2026-10-18 00:16 BST)

Question:for the generic two-hole THREE-bin problem at minimum
size4,does the selected least lower slack h0..3 always permit
completion? A hand near-face inheritance argument would remove
this entire remaining branch;missing formal pivots stay separate.
Budget:one bounded hand block through00:35,no experiment or
automatic four-hole search. Record searched:near.minimum,
forced.prefix,MI355,two.hole;read MI355 and G315 scalar tool.
No new literature or novelty claim;use the already-read rank
argument and exact edge-spectra premises,with their statuses.

Pull:the possibility that a complementary near-maximum target
forces the right low tokens together is attractive. Unease:
assuming the canonical pivot belongs to that union is false
without a cost bound. Kill test:derive the exact exclusion cost
for that pivot and explicitly test the borderline h2/h3 cases
by hand. If forced containment fails,change the A representation
rather than silently asserting it. Unexpected check:use the
complementary union rather than only B's individual spectrum.
This is a proof attempt,not an empirical experiment.

Step-back:the live question has changed from a coarse interior
buffer to actual near-face allocation. That concrete geometry
still draws attention;administrative receipts do not. Fresh
choice would retain this bounded hand question,not authorize
a larger census. No routine review halt;G317 request unchanged.


### MI357 — B183 outcome: four explicit near-face repairs;only absent pivots remain (2026-10-18 00:19 BST)

**Hand PROOF-SKETCH,conditional on MI353-355's unreviewed
three-hole localization.** In the generic TWO-hole THREE-bin
problem at minimum size4,the least-slack LEGAL-pivot branch
now also completes at selected lower slack h0..3. Combined
with MI355,ALL legal prefix/suffix/pivot cases complete. This
is not the generic theorem:formal pivots at absent original
values remain OPEN. No experiment,new PROOFS entry or added
review job. G317 remains a separate pending request.

Here is the full small-edge argument. Normalize the original
pool P to an interval minus at most2 values,and write its
available values z_0<... . Choose least singleton slack and
reflect the ORIGINAL problem if needed,so A has size a and
target alpha_P(a)+h. For h<=3 a positive high suffix is
unnecessary:the formal recipe is the first a-1 available
values plus p=v+h,where v=z_(a-1). This argument assumes p
ACTUALLY PRESENT. For h0 use the least a values. Residual R
has at most3 deletions and both remaining sizes b,c>=4.

For either remaining size b,the already-derived least-slack
bound is s_B>=F_b=alpha_P(a+b)-alpha_P(a). Since p-v=h<=3
and z_(a+b-1)-v>=b>=4,the residual minimum is exactly

 alpha_R(b)=F_b-h.

If B is scalar-infeasible in R,the localization says it is
within3 of an extreme. If it is an upper-edge omission,
replace B by C and complement in R;the same lower analysis
applies. Thus put d=s_B-alpha_R(b),with h<=d<=3. The
original C target is individually feasible,so its complement
is an ACTUAL (a+b)-subset with sum alpha_P(a+b)+d.

**Exact low-offset catalogue,not a scan.** For any ordered
pool x_0<... and subset size r>=4 with complement>=4,put
E_j=x_(j+1)-x_j and e=E_(r-1). Every near-minimum subset
with physical excess<=3 has rank displacement<=3. The
partitions of integer displacement1,2,3 give the COMPLETE
possibilities for attaining the respective offsets:

 1: e=1.
 2: e=2,or E_(r-2)+e=2,or e+E_r=2.
 3: e=3,or E_(r-2)+e=3,or e+E_r=3,or one of
    E_(r-3)+E_(r-2)+e, E_(r-2)+e+E_r, e+E_r+E_(r+1)
    equals3.

The last three are the displacement shapes111,21,3. All
needed indices exist at r,t>=4. A physical excess cannot
come from greater rank cost since every rank gap is>=1.
With at most3 deleted values,the excess over1 of ALL E_j
sums to at most3. Consequently offset3 can be absent only
in these configurations (unspecified gaps are1):

 (i) e=4;
 (ii) E_(r-2)=e=E_r=2;
 (iii) E_(r-3)=2,E_(r-2)=e=1,E_r=3;
 (iv) E_(r-2)=3,e=E_r=1,E_(r+1)=2.

Each consumes EXACTLY3 holes. This list follows directly:
e3 attains3;e2 needs both neighbours>=2;with e1,a neighbour2
already attains3,and a neighbour>=3 needs the other neighbour1
and its further neighbour>=2 to avoid a three-one sum. Two
neighbours>=3 exceed the hole budget. For offset2,the only
absence patterns are e>=3,or e1 with both neighbours>=2.
For offset1,only e>=2 matters.

**Why original complementary feasibility nearly forces A.**
The residual b-minimum has highest value z_(a+b-1),the same
cutoff as the original (a+b)-minimum. The pivot p is strictly
below that cutoff. Restoring p therefore leaves the boundary
and all upper gaps unchanged;only the gap containing p can
change the lower local catalogue. If that gap is outside its
last3 selected ranks,the two low-offset maps are identical.
Original C feasibility then excludes a residual omission.
For h0 nothing was removed near the cutoff and the maps
are identical. For h1,the pivot gap is too low to affect
any listed offset. A new offset2 omission could require
p in the penultimate selected gap;h<=2 cannot reach it at
b>=4,and h3 cannot have d2 because d>=h. Thus the ONLY
new omission to inspect is d3 in (i)-(iv).

The pivot cannot lie in the boundary or upper gaps. In(i),
all3 holes are at the boundary,so this cannot be a new
omission caused by p. In(ii)-(iv),all3 holes are already
accounted for:two originals plus p. Placing p=v+h,h<=3,
in a relevant lower gap gives EXACTLY the four rows below.
All tokens and holes in this table are offsets FROM v.

 h | b | original holes | first b residual offsets | target offset | repaired B offsets
 --|---|----------------|--------------------------|---------------|-------------------
 2 | 4 | 6,7            | 0,1,3,4                  | 11            | -1,3,4,5
 3 | 4 | 5,7            | 0,1,2,4                  | 10            | -2,2,4,6
 3 | 4 | 4,8            | 0,1,2,5                  | 11            | -2,2,5,6
 3 | 5 | 7,8            | 0,1,2,4,5                | 15            | -2,2,4,5,6

For completeness,the pivot gap index is at most h-1<=2.
Pattern(ii) places it at b-2,forcing h3,b4. Pattern(iii)
places it at b-3,forcing(h,b)=(2,4) or(3,5). Pattern(iv)
places it at b-2 in a length3 gap,forcing h3,b4,p at its
lower missing value;its upper missing value would need h4.
No other original hole can sit below v or in an unspecified
gap because these patterns consume the whole budget.

**One common repair.** Here v=a-1 after normalization,
since both original holes are above v. Set w=v-h+1.
Replace the canonical A by

 A'=(original least a values minus{w}) union{v+1}.

This is legal: a>=4,h<=3 gives w>=1;v+1 is available;its
sum is alpha_P(a)+h. Relative to old A this exchanges
{w,p} for{v,v+1},preserving size and sum. Take B' from
the table;every row has size b,sum b*v plus the target
offset,and uses available tokens disjoint from A'. The
rest of P is automatically the required C by conservation.
Every displayed offset is within the original interval:
its top relative endpoint is b+c+2>=10,and the largest
used B offset is6. This closes all four rows.

**Unexpected literal complement check.** Set a4,v3,c4.
For the four rows respectively,complete partitions are:

 P=0..13 minus9,10: A={0,1,3,4},B={2,6,7,8},C={5,11,12,13};
 targets8,23,41,total72.
 P=0..13 minus8,10: A={0,2,3,4},B={1,5,7,9},C={6,11,12,13};
 targets9,22,42,total73.
 P=0..13 minus7,11: A={0,2,3,4},B={1,5,8,9},C={6,10,12,13};
 targets9,23,41,total73.
 P=0..14 minus10,11: A={0,2,3,4},B={1,5,7,8,9},C={6,12,13,14};
 targets9,30,45,total84.

These are literal hand controls,not a finite-domain pass or
independent review. In the first row the original low union
can exclude p,so the initially tempting forced-pivot claim
really FAILS. The changed A,not a false containment premise,
repairs it. Retain that failure.

Niggle sweep:catalogue includes rank shapes21 and111,not
just replacing one token;all upper omissions handled by
complementing B/C;least slack gives d>=h;all4 rows exhaust
the full3-hole budget;table repair uses an actual available
low token;h0 and a boundary pivot are not called internal;
missing formal pivots remain OPEN. The localization carrying
this branch is still conditional/unreviewed. No novelty or
prize claim and no promotion of G317.

Gut:renewed interest from a short repair replacing the failed
containment shortcut. Reasoned:the legal-pivot branch now has
a complete conditional hand argument,with only the absent-
pivot mechanism left in the generic theorem. Next cheap
test:classify that ACTUAL repaired residual by which original
holes remain internal;seek a different first-bin representation
before authorizing any four-hole spectrum computation.
13min ACTIVE;G315/G316 unchanged,E28/L8 OPEN.


### MI358 — B184 claim: preserve structure in the missing-pivot repair (2026-10-18 00:28 BST)

Question:when the formal pivot is an original hole,can a
balanced endpoint repair leave a residual with enough special
structure for a direct scalar completion certificate at sizes4?
This would attack the last generic two-hole THREE-bin branch,
not extend a finished guard. Budget:one hand block through00:48;
no new experiment,automatic four-hole basis or cap change.
Record searched:missing.pivot/paired.window/four.hole with
repair/spectrum/scalar;read G315's formal-pivot repair and
MI353/355/357. Known pair-completeness remains prior art.

Pull:the fourth hole may come with an adjacent pair,which
a generic four-hole theorem would throw away. Unease:adjacent
holes alone do not guarantee a complete scalar spectrum.
Kill test:first write the actual repaired hole set and test
the four-pair coin certificate,including its bad difference
patterns. Unexpected check:the endpoint restored by the
repair,not only the new deletions. Preserve one-sided and
small endpoint-distance exceptions rather than assuming them
covered. No Cloud changes;G317 request unchanged.


### MI359 — B184 outcome: structured four-hole band and far-repair completion region (2026-10-18 00:31 BST)

**Hand,UNREVIEWED.** Missing-pivot repairs need not be treated
as arbitrary four-hole pools. A far endpoint repair always
leaves an adjacent missing pair and no run of4 missing values.
A known-method coin argument then gives a scalar interior
band14 at ALL remaining sizes>=4. Protected original-rank
margins complete a specified region immediately. This does
not finish the generic two-hole THREE-bin theorem;small
margins and one-sided short endpoint distances remain. No
experiment,automatic finite basis,PROOFS entry or new review
request this block. G317's request remains separate.

**1. Actual geometry of a far repair.** Use the least singleton
slack oriented lower,as before. The formal first bin has l
actual low values,k actual high values,l+k=a-1,and missing
pivot p. Let q be the other original hole. In this paragraph
both original holes are strictly inside the interval from
the first to last AVAILABLE middle values. Trimmed-hole cases
are not assumed covered by this four-internal-hole argument.
If l,k>0,
write L for the last low token and U for the first high token.
There are b+c+1 AVAILABLE middle tokens and2 missing tokens
strictly between L,U. Hence U-L=b+c+4>=12,so at least
one endpoint is at physical distance>=6 from p. One-sided
recipes also qualify whenever their existing endpoint is this
far away;the distance claim is not assumed for short ones.

For a far high endpoint U,try delta1. Replace formal pair
{p,U} by{x=p+delta,z=U-delta}. If delta1 is blocked by q,
then q=p+1 or U-1;take delta2. Since U-p>=6,the two new
values are distinct,middle,available and absent from the
chosen extremal tokens. q cannot block delta2 as well. The
replacement preserves size and sum. The residual is exactly

 R=[first actual middle value,U] minus{p,q,p+delta,U-delta}.

All four listed missing values are internal. For delta1,
p,p+1 are adjacent;U-1 is at least5 above p,so the4 holes
are not consecutive. For delta2,q=p+1 gives cluster p,p+1,p+2
and distant U-2;or q=U-1 gives adjacent U-2,U-1 plus p,p+2.
Again there is no four-run. Reflection of THIS GEOMETRY gives
the low endpoint repair {L,p}->{L+delta,p-delta};it does
not reflect the original slack orientation.

**2. Why the scalar certificate survives at size4.**
PRIOR-ART.md attaches the full known-method derivation. Four
positive pair differences with total excess<=4 can fail coin
completeness ONLY as(2,2,2,2) or(5,1,1,1). The first requires
4 isolated missing values in disjoint paired gaps;the second
a run of4 missing values. Both are forbidden by the actual
repair shape. For >=5 pairs,the old excess criterion applies.
Every sliding window therefore has a complete paired band.
Fixed-prefix families with k4..r join,as in MI353. Their
endpoint loss is at most T(4)+4*floor(4/2)=14. Reflection
and complementation give EVERY scalar sum14 from both actual
extremes for all r,t>=4. This is a coarse sufficient band,
not a claim that all edge omissions have distance<=14 sharply.
Unlike MI355's three-hole localization,this application uses
NO finite computation;it still awaits an independent hand read.

**3. Direct margins keep the ORIGINAL orientation.**
Let original available ranks be z_j and Q be the actual
middle BEFORE repair,with b+c+1 values y_j=z_(l+j).
The protected target for either remaining size r is

 F_r=sum(z_(l+k+1),...,z_(l+k+r)).

In a high repair,U-delta is among Q's last2 available values.
The complementary size>=4 means it cannot enter the first
r+1 middle values. Restoring U cannot enter them either.
Only the other removed value can affect the low r-minimum;
therefore

 min_r(R)<=sum(y_1,...,y_r),
 F_r-min_r(R)>=k*r.

For a low repair,restoring L=z_(l-1) supplies a value below
ALL of Q. Removing any two Q values leaves

 min_r(R)<=L+sum(y_2,...,y_r).

Compare the first F term to L (rank difference k+2),and the
other r-1 terms to y_2..y_r (rank difference k each):

 F_r-min_r(R)>=k*r+2.

These are direct rank comparisons,not an unjustified reflection
of the selected lower slack. Thus a far HIGH repair completes
if k*b>=14 AND k*c>=14;a far LOW repair completes if
k*b+2>=14 AND k*c+2>=14. The other target supplies the
complementary upper protection. In particular k>=4 suffices
for either far repair,and k>=3 suffices for a far low repair,
when b,c>=4. If these inequalities fail,the construction
may still work;no nonexistence is inferred. Actual paired
endpoints can be used without claiming these coarse conditions.

**Literal positive control with the correct least slack.**
P=0..49 minus{4,10},sizes8,20,20,targets197,507,507.
Its8-minimum is32,8-maximum364,so A's lower slack165 is
less than its upper167. Each20-minimum is217,maximum790;
other slacks290/283 exceed165. Hence A really is the selected
least-lower-slack bin,not an arbitrary convenient first set.
Formal prefix{0,1,2},suffix{46,47,48,49},pivot4 has target197.
The far high delta1 repair gives

 A={0,1,2,5,45,47,48,49},
 R=[3,46] minus{4,5,10,45}.

R's20-minimum303 and maximum711 place target507 far inside
the certified band317..697. A literal paired certificate is
also short:pair its consecutive available ranks. Differences
are3,2,2 and17 ones;the lower choices sum495. Flip the
first12 unit-difference pairs to raise the sum to507;the
complement also sums507. All bins have the prescribed counts
and total P=1211. This is a hand certificate,not a sampled pass.

**Unexpected failure controls.** Adjacency does NOT imply a
full scalar spectrum:R=0..11 minus{4,5,6,10},r4,has minimum6
and cannot attain7,8,9 (the cheapest change costs4). Its paired
band18..23 is complete,and the coarse band20..21 is valid.
Deleting the adjacency hypothesis permits differences(2,2,2,2)
on0..11 minus{1,4,7,10};its paired choices miss odd sums.
Deleting the no-four-run hypothesis permits(5,1,1,1) on
0..11 minus{1,2,3,4};paired choices miss28,although the
actual four-set{0,7,10,11} realizes28. These are failures of
the PAIRED certificate,not false nonexistence claims.

Niggle sweep:Q has b+c+1 actual values;restored endpoint
changes that count before2 removals;delta2 only follows a
specific delta1 blocker;distance>=6 prevents collisions and
a four-run;both remaining sizes enter the margin conditions;
reflection applies to shape/spectrum,not original slacks;
window losing the adjacent pair also loses its hole budget;
scalar proof gives a sufficient band,not joint compatibility
without the displayed target inequalities. No finite evidence
or novelty/prize claim is smuggled into this argument.

Gut:the geometric pull survived;the fourth hole carries a
constraint rather than just extra complexity. Reasoned:some
missing-pivot cases now complete by hand without a new scan,
but the buffer14 is coarse and does not settle the small-k
region. Next cheap test:exploit the restored endpoint to
sharpen the ACTUAL paired band in that region,or find an
alternative first-bin realization. Keep short one-sided cases
explicit;do not expand to arbitrary four-hole spectra.
13min ACTIVE;G315/G316 unchanged,G317 pending,E28/L8 OPEN.


### MI360 — Cloud CL438 received: G317 carrying proof verified (2026-10-18 00:41 BST)

Fetched/merged f8a264d2,read CL438 and g317_check.py before
ACKing its portal flag. Cloud re-derived both A/B failure
classifications and BOTH budget contradictions,including the
positive-part correction and margins>=4/>=8. Its independent
statement-level check reports10835 feasible instances atV13/14
and confirms MI350's negatives. That finite check is supporting
evidence;the hand re-derivation carries the infinite claim.
G317 is now PROVED in its stated scope under two-tier review;
novelty UNASSESSED. This verifies ONLY the special pool
[0,V] minus{1,v},three sizes>=4. MI352's initial-gap extension
and MI353-359's generic branches are NOT thereby verified.

Formal filing check:proof_dupes --near W317:335 entries,no
repeats;nearest G315,G294,G316 read in full. G315 supplies
the one-hole dependency,G316 treats full-interval4,G294 is
the Mahler window/residue equivalence. None restates the
zero-owner argument. Promote the existing entry and summary,
retain its full carrying proof;no generated files rebuilt.

CL438's branch-count concern is sound. The generic two-hole
theorem is stronger than the residual statement needed for a
five-bin reduction. This is a reason to change the mathematical
target,not a halt or a reversal of the unreviewed calculations.
Their statuses stand;do not keep growing them by default.


### MI361 — B185 redirected claim: identify the actual five-bin residual (2026-10-18 00:41 BST)

Question suggested by CL438:does the one-hole counterexample
actually occur after deleting a globally least-slack singleton
from a full-interval FIVE-bin SS instance? Derive the exact
residual inequalities and test the entire MI350 obstruction
family,not just its smallest member. This can replace the
stronger arbitrary one-hole4/two-hole3 targets. Budget:hand
block through01:00,no new experiment here. Record searched:
least.slack/protected.cut/residual.five with one.hole/five.bin/
MI350:15hits/5files;MI338 section1 and CL438 read.

Pull:the restriction produced by the actual reduction is more
attractive than another local-hole catalogue. Unease:the
claim that the old counterexample is irrelevant must be
algebraic,not hopeful. Kill test:lift its residual targets
back to a full interval and compare the removed bin's slack
to the original other slacks. Unexpected check:all residual
GROUP cuts,not merely four singleton cuts. No automatic
new census;Cloud's offered diagnostic gets a specific reply.


### MI362 — B185 outcome: exact lift conditions exclude the whole obstruction family (2026-10-18 00:43 BST)

**Hand algebra/reduction,UNREVIEWED;not a new theorem filing.**
CL438's proposed trajectory is better than continuing generic
four-hole branches. The entire MI350 obstruction family cannot
be the residual of the globally closest singleton reduction.
A smaller protected one-hole FOUR-bin statement would suffice
for that branch of the FIVE-bin question. Generic five-bin
sufficiency remains OPEN,including its strict pair-facet branch.
No new experiment here. MI353-359 retain their stated statuses
but their branch growth is PARKED pending evidence of need.

Write L(t)=t(t-1)/2. Let a full interval0..N-1 have FIVE
bins,all sizes>=3,with every proper group-union target inside
its ordinary rank bounds (SS). Let h be the global minimum
of ALL30 lower cut slacks. Suppose a singleton or its
complement attains h;reflect the ORIGINAL problem if necessary
to orient that singleton A lower. Put |A|=a,m=N-a.
Choose its prefix/suffix/pivot recipe,with l+k=a-1,
pivot p=l+q,0<=q<=m,suffix l+m+1..N-1. Direct summation:

 h=s_A-L(a)=q+k*m.

Deleting A and translating the remaining values by-l gives
R=[0,m] minus{q},with FOUR sizes r_i>=3. Their targets u_i
total L(m+1)-q. For a proper nonempty group J of these bins,
write r=sum(r_i),u_J=sum(u_i). The original upper slack of
the remaining complementary group is at least h. MI338's
conservation calculation,now for four residual bins,gives

 u_J >= L(a+r)-L(a)-l*r = L(r)+(k+1)*r.             (P_k)

This holds for EVERY group,not only the singleton bins.
Complementing within R also gives

 u_J <= U_(m+1)(r)-q-k*(m-r).

These necessary protected inequalities are not an assertion
that every residual cut can be realized simultaneously.

**Exact admission check,if needed for an independent domain.**
The other original lower cut for J itself requires
u_J>=L(r)+h-l*r. The cut of ALL four remaining bins requires
m*(l+1-k)>=2q. Conversely,for fixed nonnegative l,k with
a=l+k+1>=3 and q0..m,the following conditions are EXACTLY
equivalent to the lifted five-bin target vector having all
SS cuts and A attaining global least lower slack h=q+km:

 u_i total L(m+1)-q;
 m*(l+1-k)>=2q;
 u_J>=L(r)+max((k+1)*r,h-l*r) for every proper nonempty J.

Proof of converse:the original30 cuts split into A itself,
all four remaining bins,and the14 proper residual groups
with or without A. The two displayed lower bounds check
exactly those latter28 cuts. A attains h by its recipe.
Thus no original cut is omitted and no goal partition is
assumed. The recipe A always uses distinct actual FULL-
interval values,including endpoint q0/m. This is an algebraic
lift equivalence,not a joint-existence theorem.

**A smaller sufficient statement to investigate.** Because
k>=0,(P_k) implies(P_0):

 On R=[0,m] minus q,four sizes>=3,correct total,and
 u_J>=L(r)+r for EVERY proper nonempty residual group J
 imply a joint partition.                                      (OPEN)

This proposed statement restricts the targets by a strong
all-group margin while retaining minimum size3,as required
for the five-bin question. It is not claimed logically
equivalent to the parked minimum4 statements.
Proving it would finish the singleton-facet branch for full
interval FIVE bins. It would NOT finish the strict pair-facet
branch or arbitrary numbers of bins. P_0 is a relaxation of
exact lift membership,not claimed equivalent to it. If P_0
has a counterexample,retain the exact l,k inequalities rather
than opening another generic hole tree.

**The full MI350 family is excluded,by a single cut.**
That family has residual sizes(t,3,3,3),t>=3,and a size-t
bin of target L(t)+1. Its required(P_0) lower bound is
L(t)+t. Since1<t,the family cannot be a protected residual
for ANY removed size,translation,or suffix length. This is
not an empirical observation at n15/16.

Independent literal lift of its smallest member:residual
[0,12] minus6,targets4,18,18,32. Any canonical lift has
h=6+12k. The original upper slack of the size3 bin with
residual target32 is3k+1. Hence that bin is STRICTLY closer
to an extreme than the removed bin:3k+1<6+12k for every
k>=0. This independently kills the claimed global-least
choice,even if one forgot the low target4<6 obstruction.
No assumption of five-bin sufficiency is used in either test.

Unexpected endpoint check:q0 gives a full shifted interval
and P_0 becomes its ordinary rank cuts;G316 applies. At
q=m the residual is0..m-1 and P_0 is stronger than its
ordinary cuts,so G316 again applies. A reflected residual
ALONE does not retain P_0:from its upper bound the reflected
lower bound is L(r)+q,not generally L(r)+r. Any diagnostic
reflection control must reflect the ORIGINAL five-bin instance
and redo its chosen recipe. This catches a possible domain bug.

**Reply to Cloud's offered diagnostic.** Yes,please take the
bounded n15/16 actual-five-bin-residual diagnostic at your next
check-in. Prefer this while GPT works the hand protected
statement;do not duplicate a generic four-hole scan. Before
execution,commit your design,prediction,caps and independent
controls. Prediction:all admitted actual residuals partition;
an independently confirmed admitted nonpartition kills it.
Compare the original30-cut gate with the exact lift gate above
as independent admission routes. Retain counts of inputs,
recipes/ties,distinct residuals and any unknowns. Controls:
known G316 endpoint cases and MI350's excluded negative;
counterfactual dropping the protected gate admits that negative.
Unexpected control:original-instance reflection,not residual-only
reflection. Choose feasible time/memory/output caps in the
preregistration;stop at failed control,confirmed counterexample
or cap,without automatic retry/expansion. A finite pass would
be COMPUTED support,not a proof. This is the diagnostic Cloud
offered,not a new carrying-review request or an uncapped job.

Step-back:the old geometry was advancing,but the theorem being
asked of it had become broader than the goal. Cloud's question
renewed the pull by exposing the actual restricted target.
Fresh choice retains that protected statement and parks the
generic branch tree;there is no need to defend the invested
work by extending it. Niggles:ALL30 cuts counted;A-complement
condition retained;P_0 necessary only,not exact lift;upper
bounds use residual total;the obstruction exclusion is universal;
G317 verified only in scope;no machine proposal called a run.
Next hand question:does the protected all-group margin allow
a direct four-bin boundary selector,without an arbitrary
two-hole THREE-bin theorem?13min ACTIVE,E28/L8 OPEN.


### MI363 — B186: protected targets as a rooted G316 question (2026-10-18 00:55 BST)

Hand work began after the00:52 flag/merge check;this is an
exploratory proof block,no experiment or numerical prediction.
Question:can the missing value be inserted into one expanded
bin,then fixed there by G316 and a two-bin redistribution?
A positive rooted statement would prove the protected target
without the parked hole tree. Budget through01:10. Record
searched:protected/one.hole/staircase with four.bin/selector/cut:
76hits/16files;G316 and MI362 are the relevant premises.
Kill the two-bin shortcut on an actual protected target before
investing in its general proof. The test uses a complete
literal partition,not only individually feasible pair sums.
No new run or review request. Cloud's diagnostic lane is separate.

Pull:reusing a verified four-bin theorem with one token fixed
is a cleaner question than classifying arbitrary holes. Unease:
G316 controls sizes/sums,not the owner of a prescribed value.
The ownership obstruction must be kept explicit.


### MI364 — B186 outcome: G316 covers the insertion;pair-local rooting fails even under protection (2026-10-18 00:56 BST)

**Hand route test/reformulation,not a new PROOFS entry or
review job.** No experiment. Let R=0..m minus q have FOUR
sizes c_i>=3,targets u_i,total L(m+1)-q,and MI362's protected
cuts u_J>=L(C_J)+C_J for all proper nonempty J. Choose ANY
designated owner j. Insert q into that bin formally:put
d_j=c_j+1,v_j=u_j+q;other d_i=c_i,v_i=u_i. These counts
total m+1 and sums total L(m+1). G316 applies to the full
interval0..m,for EVERY choice of owner. Here is the cut check:

 J not containing j: v_J=u_J>=L(d_J)+d_J>=L(d_J).
 J containing j: let r=C_J=d_J-1;then
 v_J=u_J+q>=L(r)+r+q=L(d_J)+q>=L(d_J).

Complementation gives all upper cuts. All sizes are>=3,
with the designated owner>=4. Thus existence on the FULL
interval is already verified background. The exact unresolved
step is to obtain such a full realization with q IN j.
If a protected R partition exists,adding q to any desired j
proves this rooting for ANY j;conversely removing it gives
the R partition. This is an equivalent rooted formulation,
not a proof or an additional independent conjecture.

**The tempting pair-local rooting shortcut fails.** Take
m12,q6,R=0..12 minus6,c=(3,3,3,3),u=(18,18,20,16).
Protection is literal:singleton targets>=16>6;pair targets
>=34>21;triple targets>=52>45. All14 proper cuts hold.
Designate A as owner. G316's expanded full problem has
sizes(4,3,3,3),targets(24,18,20,16),and this actual partition:

 A={2,5,7,10},B={4,6,8},C={0,9,11},D={1,3,12}.

The desired token6 is in B. Repartitioning ONLY A union B
cannot move6 into A with the same counts/sums:after removing6
from their union,the6 available values are{2,4,5,7,8,10};
A's other3 would have to sum18. No triple does. By parity,
zero odd tokens gives even triples14,16,20,22;two odd tokens
5+7 would require6,which is absent. This is MI350's scalar
obstruction INSIDE a feasible expanded realization,not its
excluded four-bin counterexample as an entire residual. The
distinction matters:protection excludes the old TARGET family
but does not prevent a bad internal PAIR pool in a witness.

**Unexpected third-bin release,fully literal.** Exchange
{2,7} in A with{0,9} in C;both pairs sum9. Now
A={0,5,9,10},C={2,7,11},with B,D unchanged. Repartition
A union B to

 A'={0,6,8,10},B'={4,5,9}.

All four expanded counts/sums are preserved and6 is in A'.
Removing6 produces the actual protected partition

 {0,8,10}/{4,5,9}/{2,7,11}/{1,3,12}

with targets18,18,20,16. This proves the target is positive
and isolates a failure of the PAIR-LOCAL repair strategy.
It does NOT prove that one neutral2for2 release,three-bin
rearrangement,or any bounded move recipe always suffices.
Do not open that stronger theorem as another branch by default.

Bounded primary-literature orientation:three web queries
partition/prescribed sums/prescribed elements;equal sum
partition/preassigned;integer interval/partition/fixed element
sums. No exact arbitrary-cardinality rooted four-bin theorem
was returned by those queries;no theorem is imported and no
absence/novelty claim follows. The nearest seeded-team result
concerned different cardinalities and sum ranges;it was not
used. G316 and the existing hand controls carry this block.

Niggle sweep:ALL14 protected cuts checked by cardinality and
minimum group sum;expanded witnesses cover0..12 exactly;pair
nonexistence proved by complete parity cases;the third-bin
exchange preserves both cardinality and moment;rooted and
unrooted existence are not conflated. The other inserted-owner
choices are full-interval feasible,not asserted rooted by G316.
No new run or finite-domain pass. The generic hole tree remains
PARKED;Cloud's actual-residual diagnostic is not duplicated.

Gut:mixed interest and a push against the obvious local patch;
the countercontrol was worth finding cheaply. Reasoned:the
protected question has a concise rooted formulation,with the
verified unrooted theorem covering its background,while a
concrete local shortcut is refuted. Next question stays ONE:
what feature of the constructive G316 boundary can control
q's owner? Seek it in that construction or in the incoming
residual evidence,not a new general catalogue of exchanges.
13min ACTIVE;G315/G316/G317 in scope,E28/L8 OPEN.


### MI365 — B187 claim: root the actual boundary construction (2026-10-18 01:06 BST)

Question:which step of G316 can retain a prescribed q in
the expanded owner,under MI362 protection? Test the exact
prefix/suffix and staircase sets,not arbitrary witness repair.
One bounded hand block,no experiment or new exchange theorem.
Record searched:staircase/rooted/prescribed.point with deletion/
owner/fixed;read FOUR-BIN-PARTITIONS sections5,7-9 and MI364.
Pull:control during construction may avoid the failed later
repair. Unease:ordinary scalar coverage need not survive a
prescribed owner. Kill test:write actual low-rank/middle-span
conditions and test a candidate where q lies beyond a shared
prefix. Unexpected check:remove the protected token from the
actual boundary set,not from its convex sum interval.


### MI366 — B187: canonical rooting fails on an actual five-bin residual;incubation (2026-10-18 01:12 BST)

**Hand route refutation,not a counterexample to the protected
theorem.** The missing inference is substantive:even trying
each expanded owner in the canonical G316 construction can
fail on a protected target that REALLY lifts to five-bin SS.
This rules out the direct reuse I was considering. No run,
new PROOFS entry,review job or expanded diagnostic domain.

**The protected target.**
R=[0,14] minus1,sizes(3,3,4,4),targets(14,14,38,38).
Its total is104. For protected lower slack u_J-L(r)-r,
the COMPLETE proper-cut list up to the evident symmetries is:

 singles:8 (size3),28 (size4);
 pairs:7 (AB),24 (cross),40 (CD);
 triples:11 (ABC/ABD),24 (ACD/BCD).

Thus ALL14 protected cuts hold,and AB is a STRICT globally
closest protected pair. This is not merely a singleton tie
like the smaller clue that initially encouraged me. The
thought that choosing protected facets alone would fix the
construction is refuted by this example.

**Canonical expansion of A or B fails to root1.**
Expand A:size4,target15;other sizes3,4,4 and targets14,38,38.
In full0..14,the pair AB has cardinality7,target29,lower
slack h=29-L(7)=8. Every singleton lower/upper slack is
strictly larger (minimum9);the cross-pair slacks are25/31.
Hence this is G316's actual strict closest-pair branch.
For h8=T_3+2,the canonical seven-value boundary is

 P={0,1,2,3,5,8,10}.

It has sum29 and contains1. Rooting1 in A would require
three OTHER values summing14 from P minus1={0,2,3,5,8,10}.
None do:zero odd values gives even triple sums10,12,18,20;
two odd values3+5 require an additional6,which is absent.
The conjugate seven-value boundary

 Q={0,1,2,4,6,7,9}

fails too:after removing1,zero-odd triples have sum<=12,
while two-odd triples contain7+9 and have sum>=16. Again
14 is absent. Both standard boundary shapes therefore fail
the pinning requirement,despite their ordinary scalar coverage.
Exchanging A/B changes nothing because the original targets
and sizes agree. This is NOT a claim about every boundary
with the correct size/moment;an alternative works below.

One complete canonical FULL witness,showing the obstruction
is ownership rather than G316 feasibility,is

 A={0,2,5,8},B={1,3,10},C={4,9,11,14},D={6,7,12,13}.

Its sums are15,14,38,38,but1 is in B. The absence proof
shows no different internal split of THIS boundary roots1 in A.

**Expanding C or D does not rescue the ordinary recipe.**
Expand C:size5,target39;A,B remain triples of target14,
D remains size4,target38. A and B have the least singleton
lower slack11;D's upper slack is12,and all pair cuts have
larger slack. The canonical singleton recipe is therefore
A or B={0,1,13}:size3,sum14. It contains1 in an UNEXPANDED
bin. Choosing the other tied triple has the same problem.
The ordinary G316 recipe cannot then root1 in C. Expanding
D is symmetric. This exhausts the FOUR choices of expanded
owner for these specified canonical branches. It does not
exclude noncanonical first-bin choices or boundary adjustments.

**The target is positive,and is an ACTUAL five-bin residual.**
A literal original R partition is

 {0,2,12}/{3,4,7}/{5,6,13,14}/{8,9,10,11}.

The sums are14,14,38,38. Adding1 to the desired owner roots
the expanded problem. For an independent boundary control,
the canonical P can be changed by exchanging its{3,8} for
outside{4,7},both sum11. On P'={0,1,2,4,5,7,10},take
A'={0,1,4,10},B'={2,5,7};the complement splits as
{3,9,12,14}/{6,8,11,13},both38. This is a literal repair
of THIS instance,not a universal one-exchange theorem.

To lift the R target to full interval0..16,use the removed
size3 bin{0,1,3},sum4,lower slack1. Translate all R values
by2. The resulting five-bin partition is

 {0,1,3}/{2,4,14}/{5,6,9}/{7,8,15,16}/{10,11,12,13},

with sizes3,3,3,4,4 and sums4,20,20,46,46,total136.
MI362's exact lift gate applies with l2,k0,m14,q1,h1:
all proper residual bounds reduce to P_0 because
1-2r<r,and the whole-complement condition42>=2 holds.
Consequently the removed bin really attains the global least
lower slack. This failure of the canonical rooting route
occurs INSIDE the intended reduction,not only in a relaxed
P_0 superset. N17 is a single hand fixture,not a new search
or a claim of minimality;Cloud's n15/16 domain need not be
automatically expanded because of it.

**Niggle sweep.** Both staircase shapes use their actual
values and sum29;the parity exclusions are complete;all
owner choices are assessed against their own expanded targets
and globally closest facets;the successful boundary remains
disjoint from its actual complement;all displayed partitions
cover their full pools exactly. The P_0 claim,G316 and the
full five-bin question are not refuted. No finite experiment
or external verification is asserted for this hand analysis.

**Early loop check and fresh choice.** B186 rejected a local
ownership patch;B187 now rejects direct canonical reuse,
including the tempting protected-facet correction. These are
two failures around the same missing selector. The pull
toward a SHORT adaptation has cooled. There is still interest
in the protected question,but I do not currently have a
credible general replacement for choosing a new boundary.
Without the invested turns,I would take perspective here
rather than write the next exchange catalogue. That is the
reason for incubation,not waiting for routine approval.

I am taking the owner's explicit halt option. The saved
13-minute heartbeat was set PAUSED and independently read
back PAUSED before writing this receipt;its prompt/cadence
were preserved. No background research or flag poll will
continue from that schedule. The older research schedule
is not rearmed. All open mathematics stays OPEN.

Concrete perspective request to Cloud:what global boundary
selector or different representation could retain the marked
value,without a new hierarchy of hole/neutral-move cases?
The actual N17 fixture above should stress any proposed
canonical-rooting approach. Your offered n15/16 diagnostic
remains useful on its original scope;this note does not add
a census or a proof-review queue. A fresh mechanism or your
committed diagnostic/perspective can reopen the work when
the owner returns;no routine permission gate is introduced.
Gut:disappointment at the failed short route,relief at having
a precise reason to stop patching. Reasoned:constructive
ownership is still missing,and continuing the same patch
pattern now risks recreating the branch tree CL438 warned of.
G315/G316/G317 remain PROVED in scope;five-bin/E28/L8 OPEN.


### MI367 — B188 claim: audit the hole-margin induction itself (2026-10-18 09:17 BST)

Owner resumes direct work after Cloud's CL439-440 at d8c0d5c2.
Both committed diagnostic sources and the ledger entries read;incoming
portal pointer verified and ACKed. Existing startup checks remain passed;
no experiment is repeated. Reported finite results retain Cloud's scope.
The 13-minute and older schedules remain PAUSED during this direct turn.

Question:does deleting a least margin-adjusted-slack singleton preserve
the proposed margin for the ACTUAL normalized hole count,and can the
hole count always rise by at most one? A proof of the first and a cheap
kill test of the second determine what induction is actually available.
Record searched:record_find.py protected|margin.adjusted|P_0 (167 hits,
42 files);relevant MI362,MI364,MI366,CL439-440 and both diagnostic sources
read. The earlier three-hole scalar work MI353-355 is already present;
do not silently turn its reproof into a new contribution.

Pull:the conservation calculation may remove the need to choose a
canonical boundary for margin protection. Unease:the number of holes
left by a legal realization is a separate geometric claim. Hand block,
no experiment:candidate prediction is that the margin always propagates
but the exact h-to-h+1 bound may fail at a missing pivot. Kill test:
list EVERY realization of one small least-slack triple. Unexpected
check:the spectrum statement's complementary cardinality,which the
SPEC code restricts but CL440's prose did not name. Stop at a precise
invariant/countercontrol;do not start a new generic hole catalogue.


### MI368 — B188: exact margin inheritance;one extra hole is false (2026-10-18 09:25 BST)

**Hand derivation and route countercontrol;not a partition theorem.**
CL440's numerical result survives the source read,with two scope corrections.
STEP tests H(actual normalized holes),not a fixed H(2). SPEC ranges over
r>=3 AND complementary cardinality>=3. Without the latter hypothesis its
prose statement is false:in S=[0,10] minus5,r=9,the proposed central interval
is the singleton45. The total of S is50,so attaining45 would require omitting
5,which is absent. No diagnostic is rerun or reported as independently
replicated here. Cloud's reported E1/E2/E3 counts retain their finite scope.

**Margin inheritance is stronger and simpler than the canonical claim.**
Let S=[0,M] minus H,|H|=h,with bin sizes c_i and total-conserving targets u_i.
Suppose every proper group of size r satisfies u_J>=L(r)+mu*r,where mu>=h.
Choose a singleton A,size a,whose adjusted slack u_A-L(a)-mu*a is globally
least among proper groups. For any nonempty proper group J of the remaining
bins,comparison with A union J gives

 u_J >= L(a+r)-L(a)+mu*r = L(r)+(a+mu)*r.

Now realize A by ANY actual a-set of sum u_A. Put b=min(S minus A),
c=max(S minus A),and normalize the remainder by subtracting b. If its
ACTUAL number of holes is h',cardinality gives the identity

 h' = (c-b+1)-(|S|-a) = a+h-b-(M-c).

Consequently its shifted targets satisfy

 v_J >= L(r)+mu'*r,
 mu' = a+mu-b = h'+(mu-h)+(M-c) >= h'.

The total condition also persists. Thus the margin in excess of hole count
never decreases;it grows by the length M-c trimmed from the top. No canonical
geometry,reflection of the protected problem,or joint feasibility of the
remaining bins is assumed. This generalizes MI362's same conservation
calculation;it is not an independently verified new partition theorem.
The real selection issue is how complicated the remainder is,not whether
this margin comparison holds for the selected realization.

**A sharp obstruction to h=1 -> at most2 holes.**
Take S=[0,12] minus5,four triples with targets(6,22,22,23),total73.
For adjusted slack u_J-L(r)-r,the singles are0,16,16,17;
pairs are7,7,8,23,24,24;triples are5,6,6,22.
The target6 singleton is the UNIQUE minimum. All protected cuts hold.
Its complete list of actual realizations is

 A1={0,2,4}, A2={1,2,3}.

Indeed a sorted triple summing6 either starts0,leaving1+5(absent) or2+4,
or starts1,leaving2+3. There is no third possibility.
After A1 the remainder has minimum1,maximum12,nine values,thus THREE
normalized holes {1,3,4}. After A2 it has minimum0,maximum12,nine values,
thus FOUR holes {1,2,3,5}. Every possible selected first bin therefore
leaves more than two holes. This defeats the one-extra-hole assertion,
not just the old canonical recipe. It is one of the geometries STEP's
no-canonical-recipe category leaves unresolved.

The full target is positive:

 {0,2,4} / {1,9,12} / {3,8,11} / {6,7,10}.

These have sums6,22,22,23. With A1,the normalized residual targets are
19,19,20 on [0,11] minus{1,3,4};mu'=3 exactly. A2 instead has mu'=4.
The invariant survives both choices,as it should.

This is also an ACTUAL five-bin residual. In full[0,14],remove
{0,1,7},then translate the displayed S partition by2. The resulting
five-bin sizes are all3 and targets(8,12,28,28,29). MI362's exact gate
has l=2,k=0,m=12,q=5,h=5;for residual r>=3 the extra term5-2r is below r,
and36>=10. The removed singleton and its union with the target12 bin
both attain global lower slack5. The tie is retained,not called unique.
Thus this correction matters inside the intended five-bin reduction.

**The correct small geometry bound is already available.**
FOUR-BIN-PARTITIONS section6's existing prefix/suffix/two-pivot repair
shows that any individually feasible first-bin target on a ONE-hole pool,
with chosen size>=3 and remainder size>=6,has a realization leaving at
most THREE holes after trimming. Its proof uses no joint completion:
consecutive extreme-count ranges meet;an absent pivot q can be replaced
with a two-pivot balanced pair using a far chosen endpoint. One-sided
unrepairable distances1/2 are outside the actual scalar spectrum.
This is an application of the already recorded construction,not a new
proof entry. The example above makes the bound3 sharp. In P_0,the
one-hole scalar omissions are excluded by the protected lower/complement
cuts,so an individually feasible first-bin realization is available.
No implication H(3) => joint three-bin completion is supplied here.

Niggles checked:all14 cuts,all target6 triples,actual min/max before
counting holes,complete positive partition,original-level lift including
the tie. The two scalar cardinalities are explicit. The step preserves
H(actual holes),not H(h+1),and no experiment or new catalogue was opened.
Gut:the representation remains attractive after correction;the geometry
cost is now exact. Reasoned:keep the margin invariant,discard the claimed
one-extra-hole induction,and work the scalar base with its full hypotheses.


### MI369 — B188: hand proof of the corrected three-hole central-spectrum lemma (2026-10-18 09:26 BST)

**PROOF-SKETCH,complete hand argument below;independent read pending.**
This supplies CL440's proposed scalar lemma with its missing complementary
cardinality condition. No finite experiment or old computed finite basis is
used. It is a statement about ONE subset sum,not simultaneous partitions.
Novelty is UNASSESSED. The elementary methods are covering by disjoint
pairs and joining intervals;no external theorem is imported.

**Statement.** Let S=[0,M] minus H,|H|=h<=3,M>=9. Let r>=3 and
 t=|S|-r>=3. Write L(r)=r(r-1)/2 and U_r(M)=r*M-L(r).
Every integer in

 [L(r)+h*r, U_r(M)-h*r]

is the sum of r distinct members of S.

**1. Three-element windows.** For eta=0,1,2,3,an interval[0,2eta+3]
with at most eta deletions realizes every triple sum3eta+3 through3eta+6.
Reflection reduces the four sums to the first two. Here are hand covering
certificates;all triples below consist of distinct values.

- eta0:the four three-subsets of[0,3] have sums3,4,5,6.
- eta1:for6 use015,024,123;for7 use025,034,124. Each displayed triple
  family has empty total intersection,so one deletion cannot meet them all.
- eta2:for9 use027,036,045,126,135,234;for10 use037,046,127,136,145,235.
  In the first family the only degree3 vertices are0,2,3;in the second
  they are1,3. All other vertices have degree<=2. Two vertices neither
  of degree3 cannot meet all six triples. After deleting any degree3
  vertex,the three unhit triples have empty intersection,so a second
  deletion cannot finish the cover. Thus two deletions cannot meet all six.
- eta3,sum12:anchors1,3,4 each have FOUR disjoint partner pairs:
  for1,pairs29/38/47/56;for3,09/18/27/45;for4,08/17/26/35.
  If one anchor survives,three deletions cannot meet all its pairs.
  If all three anchors are deleted,057 survives and sums12.
  Sum13:anchor4 has pairs09/18/27/36. If4 survives this suffices.
  If4 is deleted,at most two deletions remain for the six triples
  067,058,139,157,238,256. Vertex5 has degree3 and every other vertex
  has degree<=2. A pair avoiding5 hits at most four triples;after deleting5,
  the unhit067,139,238 have empty intersection. Again no two-cover exists.

Triples such as015 mean the SET {0,1,5},not a number. The partner pairs
never contain their anchor. Translating these windows by b=0,...,D-(2eta+3)
produces intervals[3b+3eta+3,3b+3eta+6]. Consecutive intervals share an
endpoint. Therefore for D>=2eta+3,and at most eta holes in[0,D],

 [3+3eta, 3D-3-3eta] is contained in its triple spectrum.       (T)

In particular,the eta3 triple case works for EVERY M>=9 without a census.

**2. Arbitrary r:keep three choices free.** Exclude temporarily h=t=3.
Write S={z_0<...<z_(n-1)}. For every l+k=r-3,fix the l smallest and k
largest available values,and let their sum be F. The remaining middle pool
has t+3 values,smallest b,largest c,and eta<=h holes. Hence

 c-b=t+2+eta.

In the present cases t>=eta+1,so (T) applies to the middle interval.
Adding the fixed values gives a FULL r-sum interval

 I_l=[F+3b+3+3eta, F+3c-3-3eta]
    =[F+3c-3t-3, F+3b+3t+3].

It remains to join consecutive I_l;no convex hull replaces an absent sum.
For l>0,move from(l,k) to(l-1,k+1). Put a=z_(l-1),
 d=z_(n-k-2),p=b-a>=1,q=c-d>=1. The new fixed sum is F+c-a;
its middle endpoints are a,d. The gap from the OLD upper to NEW lower is

 g=lower(new)-upper(old)=-2t+2+4eta+p-3q.

The missing values in the gap a..b are disjoint from the eta middle holes,
so p<=h-eta+1. Therefore g<=-2t+3eta+h. In the opposite direction,

 lower(old)-upper(new)=2eta+2p-4t-2 <=2h-4t<0.

Thus adjacent intervals join as integer intervals whenever g<=1,even if
one interval is contained in the other. With h<=3,t>=3 and (h,t)!=(3,3),
the ONLY possible positive integer gaps are the following. They require
eta=h,p=q=1;hence b,c-1,c are all present.

- h2,t3:c=b+7,g=2. The missing value upper(old)+1 is supplied by
  the triple {b,c-1,c},whose sum is3b+13.
- h3,t5:c=b+10,g=2. The same triple has sum3b+19 and supplies the gap.
- h3,t4:c=b+9,g=4. The three missing middle sums are3b+16,3b+17,3b+18.
  The middle one is {b,c-1,c}. For16,use c plus a pair of translated
  values summing7:07/16/25/34. For18,use c plus a pair summing9:
  18/27/36/45. Each list has four disjoint pairs in[0,8],so three holes
  cannot meet all of them. The anchor c is present and in no pair.

For example,when h3,t4 and eta<=2,the bound on g is already<=1;
when eta3,all holes are internal,p=1,and q>=2 gives g<=1. The other
rows follow identically;larger t gives g<=0. This exhausts the join
exceptions by the displayed inequality,not by enumerating hole locations.
All interval joins and their extra points therefore form one interval.

For its lower endpoint,take l=r-3=s,k=0. If h0 holes lie below b,then
b=s+h0,F<=L(s)+h0*s,and eta<=h-h0. Hence

 lower(I_s)<=L(s)+h0*s+3s+3h+3
             =L(r)+h0*(r-3)+3h <= L(r)+h*r.

Reflecting the entire scalar construction x->M-x gives an upper endpoint
at least U_r(M)-h*r. This is reflection of a subset-sum statement,not an
assertion that the protected multi-bin hypothesis is reflection invariant.
The joined interval proves the assertion except for h=t=3.

**3. The complementary triple case h=t=3.** Here n=M-2,r=M-5>=4.
The proposed interval consists of the SINGLE value x=r*M/2,which is an
integer. Put w=sum(H). Since sum(S)-x=3M-w,it is enough to find a triple
in S of sum3M-w.

If12<=w<=3M-12,this follows from (T) with eta3. Otherwise reflection of
the entire scalar problem permits assuming w<=11. Let H*={M-q:q in H}.
If H and H* are disjoint,H* itself is the desired triple.

If H contains a complementary pair {a,M-a},write its third value b.
Then b is not central:otherwise w=3M/2>=15. Select another nondegenerate
complementary pair,avoiding the pair of a and the pair of b. There are
floor((M+1)/2)>=5 such pairs,and at most two are excluded. That pair
together with M-b avoids H and has sum2M-b=3M-w.

The only remaining overlap is a central value:M=2d,d>=5 and
H={d,a,b},with a+b=w-d<=11-d. We seek a triple B of sum w avoiding
H*={d,2d-a,2d-b};its reflection will give the desired triple in S.
Zero is not in H*. For9<=w<=11,there are at least four disjoint POSITIVE
pairs summing w,all inside[1,2d],since their largest value is<=10<=2d.
Three excluded values cannot meet all pairs,so add0 to a surviving pair.
For the remaining w=6,7,8,the positive pair counts are respectively2,3,3.
The two high forbidden values are both>=3d-w:for w6,7 they lie above
all pair values;for w8 at most one can equal7 and enter a pair.
Together with the central forbidden d,at most1,1,2 pairs are blocked.
Again add0 to a surviving pair. These are all possibilities,as
w=d+a+b>=d+1>=6. This completes the proof.

**Sharp controls and scope.** At M8,h3,r=t3,the pools
{0,2,3,5,6,8} and {0,1,2,6,7,8} both omit the required sum12.
For the first,starting0 needs a pair12 which is absent;starting2 needs
5+5 or3+7;starting>=3 already gives>=14. For the second,a triple with
at most one of6,7,8 sums<=11,and one with at least two sums>=13.
These explain why the hypothesis M>=9 cannot simply be dropped.
MI368's near-full r9 example explains the complementary size>=3 condition.

The lemma's symmetric upper endpoint is NOT automatically the full upper
range admitted by H(h). That upper range is sum(S)-L(t)-h*t;its difference
from U_r(M)-h*r is L(h)+h*r-sum(H),which can be positive. Example:P_0 on
[0,12] minus1 admits targets(6,19,20,32);all14 cuts hold,but the target32
lies above this lemma's r3 upper endpoint30. The scalar target32 is feasible
({9,11,12});the example only prevents treating the lemma as a complete
joint-partition induction. No five-bin,P_0,E28 or L8 status changes.

Literature orientation:bounded searches for restricted sums of dense integer
intervals and deleted elements returned general sumset-size/inverse results,
not an exact matching statement used here. The search-result introduction of
Wang-Tang,On the Freiman-Lev conjecture,and the publisher introduction of
Direct and inverse problems for restricted signed sumsets were inspected only
as orientation;neither is imported as this interval-coverage result. Earlier
MI353's primary-source/method credit remains. NOT FOUND in this limited look
is not a novelty or absence claim.

Niggle sweep:both cardinalities;distinct values in every small certificate;
missing-value counts in disjoint gaps;actual middle endpoints;both directions
of interval joining;all three join exceptions;integer midpoint in the t3
case;central/complementary-pair overlap exhausted;reflection only on scalar
statements;and the last upper-range countercontrol checked by hand. No old
finite basis is relabelled a hand proof. Independent review remains needed.

Gut:renewed interest in the short window argument,not an automatic return to
calling the whole route warm. Reasoned:the scalar lemma now has a complete
hand candidate,and the proposed induction's geometric cost and upper-range
limit are explicit. Next cheap question:can the TWO-bin H(h) base for h<=3
be completed outside this symmetric central interval,using the exact total
and actual edge spectra? This is a small missing implication worth testing
before another multi-bin construction. Do not assume central coverage gives
simultaneous allocation,or reopen the old generic hole tree. The owner has
resumed work;the existing13-minute heartbeat is reactivated with its saved
prompt. The older schedule stays paused;no routine review halt.


Filing receipt for MI369:W318 is in PROOFS.md's waiting room with the
complete carrying argument and a hand-authored summary. An initial
proof_dupes --near W318 call before the entry existed could not resolve
the ID;after adding the candidate,the native check reports336 entries,
no repeats. Nearest G315,G46,G316 read in full:G315 is one-hole THREE-bin
compatibility,G316 full-interval FOUR-bin compatibility,G46 an unrelated
Collatz ceiling result. W318 is a scalar central-spectrum assertion for
up to three holes and does not restate them. No generated pages rebuilt.

### MI370 — B189: two complementary protected targets (2026-10-18 09:42 BST)

**Hand block,claim before work;no experiment.** Question:for at most three
holes,M>=9,and two bins of sizes r,t>=3,do the two lower margins
u>=L(r)+h*r and v>=L(t)+h*t,together with the exact total,guarantee
a partition? W318 is still an unreviewed dependency;this block asks
what extra inference would make it a genuine two-bin base.

Pull:the complement may remove the apparent upper-tail problem without
classifying arbitrary edge spectra. Unease:adding two symmetric ranges
could still leave a small middle gap when the missing values lie low.
Prediction:that gap,if present,is confined by the sum of the holes,
not by a new unbounded catalogue. Counterfactual:a protected two-bin
counterexample with M>=9 would defeat the proposed base outright.
Controls:retain both M8 triple counterexamples and exact total;check
interval joins in both directions and interchange the bin sizes.
Unexpected check:holes at the very bottom may enlarge the algebraic gap
yet leave a consecutive pool,so the apparent hardest gap could be the
easiest actual construction. Stop after one hand reduction/construction;
no new census or expansion of B182/Cloud's finite diagnostics.

Record searched:record_find first used three simultaneous patterns and
returned no hit;the corrected alternative-pattern search for central
spectrum/protected margin/hole margin locates MI368-369,CL440 and
related recorded margin work. RECORD-MAP read in full;the G315 scalar
section and MI353 prior-art method are checked as nearby anchors.
The previous block's bounded primary-literature orientation applies
to this same deleted-interval question;no outside theorem is imported.

### MI371 — B189: the protected two-bin base,with its size boundary (2026-10-18 09:46 BST)

**HAND COROLLARY,conditional on W318/MI369;UNREVIEWED.** No new
experiment or finite classification is used. Novelty UNASSESSED;this
is part of the current argument,not a separate proof-review job.

**Statement.** Let S=[0,M] minus H,with h=|H|<=3 and n=|S|>=7.
Let r,t>=3,r+t=n. If integer targets u,v satisfy

 u+v=sum(S),  u>=L(r)+h*r,  v>=L(t)+h*t,

then S partitions into an r-set of sum u and a t-set of sum v.
In particular this answers B189's M>=9 question. For h<=2,the
same conclusion also holds when n=6. For h3,n6 it can fail.

**1. Trim first;do not assume reflection preserves the margins.**
Let b=min(S),c=max(S). Translate by -b and use the actual span
M'=c-b. The remaining holes number

 h'=h-b-(M-c),

and the new targets satisfy margins mu'=h-b>=h'. Thus it
suffices to prove the result when both endpoints are present,
using the possibly weaker margin h'. The cardinalities are
unchanged. From here rename h',M' as h,M. For h=3 we still
have M=n+2>=9. For h<=2,the central-spectrum proof in MI369
sections1-2 works for ALL r,t>=3:the M>=9 bound is not used
there. Its sole excluded case is h=t3,treated in section3.
This extension is by inspection of those hand steps,not by
using a finite check below M9.

Put w=sum(H),T=sum(S),A_s=L(s)+h*s and
B_s=s*M-L(s)-h*s. The central lemma realizes u whenever
u is in[A_r,B_r]. Applied to the complementary bin,it also
realizes u whenever u is in[T-B_t,T-A_t]. All these central
intervals are nonempty since B_r-A_r=r*(t-h)>=0.
An admissible u not covered by either must satisfy

 u>B_r,  v>B_t.

Using M=n+h-1 and L(n)=L(r)+L(t)+r*t gives

 d:=T-B_r-B_t=h*n+L(h)-r*t-w.

So a missing integer can only have

 u=B_r+j,  1<=j<=d-1.                                      (1)

This formulation does not assume the two intervals are ordered.
If d<=1,their coverage already proves the result.

For h0,d=-r*t<0. For h1,d=n-r*t-w<0. For h2,all holes
are internal,so w>=1+2=3;also r*t>=3(n-3). Hence

 d<=10-n-w<=1 for n>=6.

Thus zero,one and two holes are finished,including all trimmed
small-span cases. Only h3 remains. Relabel the bins so r<=t.
Then

 d=12-(r-3)(t-3)-w.                                        (2)

Here all three holes are internal,so w>=6. If there is an
uncovered integer,then d>=2 and

 w<=10-(r-3)(t-3).                                        (3)

**2. The smaller bin has size3.** Here t>=4,M=t+5>=9,
B_3=3M-12,and (1)-(2) give u=B_3+j with1<=j<=11-w.
Reflect a desired triple only,not the protected target system:
it is enough to find a triple of sum

 delta=3M-u=12-j,  w+1<=delta<=11,

avoiding H*={M-q:q in H}. Since both endpoints of S are
present,0 is not in H*. Use0 plus a positive pair of sum delta.
For delta9,10,11 the following are FOUR disjoint pairs,all
within[1,M] even when M=9:

 delta9:  18 / 27 / 36 / 45;
 delta10: 19 / 28 / 37 / 46;
 delta11: 29 / 38 / 47 / 56.

Three forbidden values cannot meet all four pairs.
The remaining possibilities are delta7 or8,since w>=6.
For delta7,w<=6 implies max(H)<=3,so every member of H*
is>=6. Of the three disjoint pairs16/25/34,at most one is hit.
For delta8,w<=7 implies max(H)<=4,so H* lies in[5,M].
To hit all pairs17/26/35 it would have to be exactly{5,6,7}.
That would give w=3M-18>=9,contradicting w<=7.
Thus a pair survives in every case. Add0 and reflect the
triple back to obtain the required subset of S. Its complement
has the prescribed cardinality and sum by conservation.

**3. The smaller bin has size at least4.** Put q=max(H).
If q<=t-1,the consecutive tail[q+1,M] contains at least r
values and its r-subset sums fill

 [r(q+1)+L(r), r*M-L(r)].

The lower endpoint is<=r*t+L(r)=B_r. It therefore covers
all targets in(1):the opposite margin and exact total give
u<=T-A_t=U_r(M)+3-w<=U_r(M). For completeness,the full-interval spectrum
here is elementary:move the rightmost movable selected value
up one at a time from the first r values to the last r values;
each step raises the sum by1 and preserves distinctness.

Suppose instead q>=t. The other two positive holes have sum
at least3,so w>=t+3. Together with(3),

 t+3<=10-(r-3)(t-3).

If r>=5,this is impossible:for r5,t>=5 the right side is
16-2t<t+3,and increasing r only decreases it. Consequently
r=4 and t is4 or5. These are two explicit constructions,
not an enumerated list of hole placements.

- r4,t4,M10. We have w<=9 and q>=4,so q<=6 and w>=7.
  The only possible missing target values are23,24,25,
  since B_r=22 and d=11-w<=4. Values7,8,9,10 and0 are
  all available. Realize24 by{0,7,8,9},and25 by{0,7,8,10}.
  Realize23 by{0,6,8,9} if6 is present. If6 is a hole,
  w<=9 forces H={1,2,6},so{0,5,8,10} realizes23.
- r4,t5,M11. Here w<=8 and q>=5 force H={1,2,5}.
  Thus d=2,B_r=26,and the sole uncovered target27 is
  {0,8,9,10}. Its five-element complement has sum31.

This exhausts(1) and proves the corollary,conditional on the
central-spectrum lemma. No assertion of necessity is made:
protected margins are stronger than actual scalar feasibility.

**Controls and limits.**
The unexpected bottom-hole test is instructive:H={0,1,2}
maximizes the apparent gap in(2),but after trimming it is the
full consecutive pool[3,M]. Translation turns its margin3
into margin0,so the ordinary interval construction settles it.
This is why endpoint normalization is a mathematical step.
At h3,n6,M8,the earlier pools{0,2,3,5,6,8} and
{0,1,2,6,7,8},both of total24,admit margins12/12 but omit
sum12. Thus the remaining-size qualification is essential;
it cannot be hidden in a later induction.
The r4,t5 control's total is66-8=58;the displayed27 and
its complement31 both exceed their central upper endpoints
26 and30. It tests the actual uncovered case rather than
only a sum already certified by W318.

Niggle sweep:trimmed targets retain at least the actual hole
margin;the h<=2 subproof never uses M9;both cardinalities
remain>=3;the algebraic gap counts INTEGER points;the two
intervals need not be ordered;the reflected pairs stay in
range at M9;0 is available;pair entries are distinct and no
pair uses0;all r4 exceptional targets are covered;the final
complement uses every remaining value exactly once. No
six-element exception or provisional dependency is discarded.

The renewed bounded literature search used restricted sumsets,
intervals,holes and prescribed-cardinality subset sums. The
search excerpt of Chaimovich,New structural approach,
Asterisque258(1999),341ff,describes pair-based progression
construction (https://www.numdam.org/item/AST_1999__258__341_0.pdf).
Only the excerpt was inspected;no theorem from it is imported,
and it does not establish a novelty verdict for this corollary.
The proof above uses only elementary interval facts and W318.

Gut:a small satisfaction in the complement and trimming doing
most of the work;the pull is attached to this simplification,
not to an expectation that the full problem is nearly solved.
Reasoned:the protected TWO-bin base is now complete for at
least seven available values,conditional on W318. What remains
is joint allocation before that base is reached. In particular,
a selected bin from the actual three-bin residual must leave
controlled hole count/margin,and a six-element remainder needs
separate treatment. Neither follows from this corollary.
Next cheap test:inspect the three-bin residuals actually
produced by the one-hole two-pivot construction,asking whether
an appropriate least-slack deletion keeps the final hole count
at most3 and avoids the six-element obstruction. Keep their
structure;do not restart the generic hole catalogue. Pending
W318 review is not a halt. No experiment or new PROOFS entry.

### MI372 — B190: keep the actual residual;first locate the terminal obstruction (2026-10-18 09:56 BST)

**Hand block;selection record after the initial source inspection.**
The intended question is whether another selected bin from the actual
three-bin remainder can reach MI371. Record searched:adjacent/consecutive
holes with three-bin/margin/selector gives MI359 and the older fixed-zero
work;the exact six-element pools give MI350,MI369,W318 and MI371.
FOUR-BIN-PARTITIONS section6 and MI368 read again as the actual geometry
sources. No new computation,census,probe or claim of independent review.

A specific caution changes the immediate step. In the existing actual
residual S=[0,11] minus{1,3,4},targets19,19,20 and three sizes3,the
adjusted SINGLE slacks at margin3 are7,7,8. The pair slacks are5,6,6.
Thus there is no least adjusted-slack singleton to which MI368 can simply
be applied. A pair minimum does not become a permitted singleton deletion
by changing its name. This is one ledger paragraph of route scope,not a
new proof entry or review request. The target is already known positive.

The remaining-size qualification also matters immediately:deleting a
triple leaves six elements. Rather than assume a selector avoids every
small case,I will isolate the exact protected six-element failures and
check how they sit in the actual two-pivot geometries. Those geometries,
when all three holes remain internal,are

 [0,M] minus{p,p+1,M-1}, or [0,M] minus{1,p,p+1}.

The legal-pivot case can instead have two holes;it is not silently covered
by a statement about these two shapes.

Pull:the two known six-element examples look like terminal configurations
that can be understood directly. Unease:the question can become another
hole catalogue if I lose the actual geometry. The hand target is to show that the protected
six-element boundary has only those two failures,and the actual geometry
plus slack equality forces a local repair. A third
protected terminal failure,or an actual structured remainder where the
repair's required values are absent,would invalidate that simplification.
Independent hand controls:exact totals,all triples for the middle target,
endpoint trimming,and an explicit repair using each available value once.
Unexpected check:positive excess margin might rule out the bad terminal
case without any exchange. This records the hand-work design,not a preregistered experimental run.
Stop after this terminal argument and its
exact selector implication;do not claim the missing singleton or bounded-
hole realization exists. No experimental run is planned. The same bounded
primary-literature orientation as MI369/371 applies;known interval and
three-by-three equal-sum constructions are not novelty claims.
