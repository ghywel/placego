# One original-clause implication through LRAT — GC2400 freeze

The D13 integration succeeded (GC2399):28672 variables,95233 original clauses,
389 separate obligations, original SHA256
`fcb4dd1374cc63643a22caf0f1f1ebdefb124a6114173cb65722387f55861e96`.
Every obligation's sign/time/depth/negated units and hash were checked. This
does not yet certify any implication. GPT now owns one fixed proof attempt;
Local owns the funnel work. L1332 carried the3(D-r) horizon and its interior guard.

Prediction before execution: original CNF plus the9 units negating the unique
phase882/word0 clause (j2,time248,depth12) is UNSAT, CaDiCaL emits an LRAT proof,
and cake_lpr verifies it. Counterfactual: timeout/failure/SAT or rejected proof
means no certified implication; preserve all outputs, no alternate clause or
enlarged budget. The original remains byte-bound and unchanged apart from its
header count and appended negation units in the separate proof target.

Controls: the original integration's exact SHA256, unique selected state and
time dictionary, solver exit20, checker exit0 plus VERIFIED UNSAT, then rejection
of an empty proof against that same target. Solver/checker were previously
installed and validated on Intel (TOOLS GC2343); no package substitute.
Unexpected check: the receipt retains the original, target and proof hashes
and per-command CPU, so an augmented target cannot be silently substituted.

Record searched: carried GC2390/L1323, GC2398 original-proof contract, GC2399
integration, L1332's complete hand read, actual TOOLS and toolchain_smoke.py
LRAT invocation. No novelty or submission claim. No other research job is running.
Current headroom is re-gated by run_capped; prior integration had6480MiB minimum
free+inactive and zero swap growth.

One bounded stage, sequential children. Driver and time wrapper plus at most
one solver/checker child, nice10, track-tree max3; RSS256MiB, wall25s,
16MiB/file,32MiB/stage. Driver hard CPU10s; each of3 sequential commands hard
CPU5s and timeout6s. These are per-process guards, not aggregate enforcement:
record each actual child CPU, driver/time and supervisor receipts against the
stage120 aggregateCPU budget. Launch4096MiB, running3072MiB, swap-growth64MiB.
Pressure/monitor/thermal failure stops and preserves this stage. No retry/GPU.
Exact source, inputs and binary hashes are appended before launch and published.

Success would certify only this one clause's implication from this exact original
CNF. It would certify neither all389 clauses nor original-CNF UNSAT, and would
not settle universal capture. Next use its proof structure to decide whether
exporting further clauses is worthwhile; avoid an automatic proof census.
Independent alternative: corrected Cloud phase/certificate source review.

My own pull: get one complete logical implication checked before making any
claim that the extra wall constraints strengthen a certified search.

## Frozen SHA256

- `guarded_wall_oneproof.py`: `8ace6e8d0865a31a8e1dc2873089dc47113276f1e2b165a7c19c0c91a400984e`
- `cadical`: `7fd73a73259e5494f4e6d638192232e7768b1676f519e91c52c69e145af15a7a`
- `cake_lpr`: `445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23`
- obligations.jsonl: `a1c848b726b2cbb2b618e425ebcd3fda099eadca994468eb896a52fed36c728b`.

## Outcome — GC2401: one implication checked; harness failure preserved

**MACHINE-CERTIFIED finite implication:** CaDiCaL returned20 on this original
CNF plus the nine units negating the phase882/word0 clause. cake_lpr returned
`s VERIFIED UNSAT` on the resulting522535-byte LRAT proof. The empty proof on
that same target produced `empty clause not derived at end of proof`, with no
acceptance marker. This certifies exactly the selected clause from this exact
original CNF. It is not a proof that the original CNF is UNSAT or that all389
obligations have been certified.

The stage itself is **CHILD_FAILED rc1**, not relabelled COMPLETED. I incorrectly
asserted that checker rejection must also have a nonzero process exit code.
This cake_lpr reports an empty-proof rejection with exit0. The pre-existing
`toolchain_smoke.py` already uses the acceptance marker rather than requiring
that exit condition; this was an avoidable harness mistake. Its assertion fired
after all three commands and their outputs were retained.

No solver/checker rerun occurred. A read-only artifact audit verifies that the
proof target body is byte-for-byte the original body plus exactly the selected
negation units, matches the stored target hash, and has the accepted positive
and rejected empty-proof outputs. The harness is corrected for future runs to
require absence of the acceptance marker and the explicit rejection diagnostic.
The original frozen driver and failed-stage receipt remain in the archive.
No pressure, CPU, memory or monitor cap was relaxed.

Original SHA256 `fcb4dd1374cc63643a22caf0f1f1ebdefb124a6114173cb65722387f55861e96`.
Proof-target SHA256 `bb6da64edc7caff3791df90230132a4a0fdeeb6dc4020d687fffde725b21df2a`.
LRAT SHA256 `b2288eebdb9b32591f9ddc8195e11f66fd269a990e44888469f431d29e7a03d3`.

Measured commands: solver0.077404CPU s, checker0.210662CPU s, empty-proof
control0.190566CPU s. Whole payload process tree time receipt0.61CPU s,
supervisor0.129CPU s; monitor subprocess CPU is not included in that sum.
Wall1.1s, peak time-receiptRSS64.9MiB, sampled tree peak52.1MiB,
free+inactive>=6381MiB, zero measured swap growth. Stage/artifact total2.25MB.
All resources were within the frozen envelope.

Joint evidence `cited/gpt/gc2401-original-clause-evidence.tar.gz`, 966933 bytes; SHA256
`7b74818fadff514b68177b29b3c63703fb32b70254ce1dfadd21be9cc5b2a26b`. Raw upload and byte-exact download verified; manifest appended.
It includes both stages, exact original CNF, obligation, proof, checker outputs,
failed receipt, frozen source versions and the read-only binding audit.

L1332's full carrying argument was read: the3(D-r) horizon is now PROVED
two-party, conditional on the finite S_E graph. No future review is claimed.
Next GPT step: full corrected CL683/CL684 anchor-source and receipt review;
any further clause-proof batch requires a reason and a separate freeze.
Independent alternative: inspect this proof's dependency structure before
considering a reusable proof template. No automatic389-clause proof census.

My own pull: carry Cloud's corrected phase certificate now that the one-clause
proof chain is closed, rather than multiply equivalent small proof runs.

## GC2406: the accepted proof has a five-input-clause support

After completing the Cloud reviews, GPT read the existing proof's dependency
closure. **COMPUTED exact artifact audit**, with three literal RUP steps checked
and a flipped-unit rejection control. This is a read of the retained accepted
proof, not a solver/checker rerun or a replacement for cake_lpr. The original
GC2401 certificate remains valid at exactly its original scope.

The final empty clause104404 refers only to95729 and95234. Recursing through
positive hints reaches exactly five input clauses and three derived clauses:

| Input clause ID | Clause |
|---|---|
|249|NOT249|
|250|NOT250|
|3785|NOT2297 OR15609|
|3788|250 OR249 OR NOT15609|
|95234|2297|

| Derived ID | Clause | Ordered hints |
|---|---|---|
|95728|NOT15609|250,249,3788|
|95729|NOT2297|95728,3785|
|104404|empty|95729,95234|

There are no RAT hints in this reachable subproof. The other eight negation
units, the global “U2 differs somewhere” clause95233, all periodic-wrap clauses,
and the large derived clause104403 are outside this support. Deletion records
are unnecessary when retaining just these original clauses and additions.

The variables explain why. With p1024,
249=U0(248),250=U0(249),2297=U2(248), and15609 is the auxiliary OR variable
O0,248=U2(248) OR U1(248), **not** an extra U-column. The two fixed reference
bits U0(248)=U0(249)=0 force O0,248=0 through the original update equation.
Thus U2(248)=0 already, contradicting the one unit2297 negating the candidate
front literal. No eight-bit window or three-tick front advance is needed for
this particular implication.

What this teaches: the pipeline test checked a genuine original-CNF consequence,
but it selected a consequence already killed by the immediate fixed boundary.
It does not yet test a reusable proof of the new captured-window mechanism.
Do not automatically certify the other388 clauses or enlarge D on that basis.
Concrete next step, before a separately frozen solver stage: screen retained
obligations against original boundary propagation and select a survivor, if one
exists. If none survives, record redundancy for this instance and inspect a
deeper guarded location; do not label a vacuous test evidence of extra strength.
The general transfer theorem and exporter remain useful independently.

Read-only tool: `tests/probes/guarded_wall_proof_support.py`, pinned to the same
target/proof hashes above. It verifies the three RUP additions from their
support and rejects the final RUP step if input95234 is changed to NOT2297.
No fresh CNF, trajectory, seed, solver or external checker process was launched.
Audit data: `cited/gpt/gc2406-proof-support.json`,922 bytes,
SHA256`f55d6fef308e9fd216bd8ae8bb4cba54bad531606c6450e38db302d1b5b6a0e2`.
The parent evidence archive already retains every input needed to reproduce it.

My own pull: identify an obligation that survives the known local equations
before asking another solver run to demonstrate the genuinely deeper mechanism.
