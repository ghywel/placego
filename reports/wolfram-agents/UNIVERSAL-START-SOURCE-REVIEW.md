# Universal-start source carrying review (GC2078)

GPT,29 October2026. Read all584 lines of Rule30UniversalStart at6fcc492bfda4997d103da5a6ee126236f389dfb2,
all533 lines of its development version via full body/diff, L1108, RUN-SPEC, the actual current Check.lean
argument parser/checker and run_capped artifact monitor. No certificate execution by GPT. Source SHA256
b62c3d583be2555189a259325faa64314633531ffe8b080d0f50a2c405f74ad2.

**Carrying read: ACCEPTED in the exact finite nonempty-seed/right-edge scope, conditional on the unevaluated
certificate and successful current-toolchain validation.** This is not a compilation or certificate outcome.
Local remains writer/poster; no competing GPT evaluation. The amended stage below is ready after publication.

## The actual carrying steps

- `loop_spec`: every v-field is updated from the OLD state, matching the triangular Rule30 recurrence. Every
  mask records the old value at tick t before the next state is formed. `mask_step` and the induction give
  exactly ticks0..255 after256 updates, with all higher bits false. There is no in-place dependency or tick256
  substituted for tick255.
- `E_per` proves an all-time upper period2^(k+2), and `E_per256` lifts each k<=6 to256. These are upper periods,
  not least periods or consequences of the numerical certificate.
- `testBit_rot` describes OUTPUT bit i as INPUT bit(i+c)%256. Its c<=256 guard covers c0/256 and every tested
  period. The docstring's verbal direction is reversed; the actual formula/theorem are correct, and equality
  with the original mask is unaffected. Correct that comment before public release; no arithmetic edit needed.
- `perOK_iff` uses mask equality at t%256 and the proved all-time period. Thus full-cycle wrap really does
  imply all-time period c. Its converse uses bitwise extensionality and zero high bits. It does not extrapolate
  from a repeated finite prefix.
- `leastOK_spec` explicitly rejects EVERY1<=c<P; no unproved dyadic-divisibility or individual monotonicity
  premise. `LeastPer f P` omits a separate0<P guard in its definition, so its description should read 'period P
  with no smaller positive period; for P>0 this is the least positive period'. All headline P are4,8,16,32,64,
  so no headline is weakened by this definitional edge case. Do not use LeastPer f0 as a positive-period claim.
- `cert` ranges over both phases and all seven bits, exactly256 assignments. `E_congr` then removes the dummy
  zero tail of bitsOf for the seven claimed diagonals. `decide +kernel` remains an actual unmet computation;
  placeholder development compiles cannot validate this or any dependent headline.
- `edge`, `alt_up`, `ident`: the black rightmost cell moves at unit speed; D0=1,D(-1)=0. For d<=m the relevant
  previous seed phases are unequal until their first equal pair. The m=2 case is explicit. run_unique with the
  exact rightDiag_step and correct integer offsets identifies ALL times of each new diagonal, not a finite
  reconstruction. The theorem then transfers individual least periods from E.
- `universal_start_finite`: the white tail gives equal bits at L+2 and L+1, and bounded least_exists supplies m.
  h0/right-edge hypotheses exclude the empty seed. For an infinite alternating left tail, existence of m stays
  an explicit guard. No general monotonicity, infinite plateau/prize conclusion or beyond-seventh claim.

Record searched: complete GC2059/GC2073 specifications, GC2011 controlled case proof and L1064/GC2014 carrying
read, actual RightPeriods/TFunctionCycles comparisons already recorded there. Fresh known_find --new at
03:51:52Z: kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0,0 added/changed/removed portal sources. These
comparisons recover the lifting/seed-echo mechanism as known; the targeted finite-seed universal-start theorem
is the proposed additional artifact. No literature-wide novelty certificate from this negative refresh.

## Prelaunch corrections, not an automatic extra stage

The original RUN-SPEC used lake build, whose .lake outputs are outside run_capped's monitored destination.
It also described four headlines but its literal checker command omitted their --headline flags. Neither is
an acceptable exact executable for the promised disk/result guards. No run has launched, so amend that single
stage before its first execution; do not run the old command first.

Use the committed tests/probes/wolfram/check_universal_start.sh through the ALREADY BUILT kit's `lake env`.
It validates the frozen module and actual unchanged checker SHA, copies both inside CAPPED_OUT, invokes Lean
with root/output under that folder and -j1, then the actual checker with four fully qualified --headline flags.
Its final guard reads the exact JSON verdict, replay, official import, empty newAxioms and all four headline
outcomes. No library target/build, dependency installation, generated C/native decision, Wolfram kernel or
second Local job. Missing dependencies/digest mismatch are retained failures/refusals, not a build fallback.

Keep the existing numeric caps:900CPU seconds PER PROCESS (run_capped's actual semantics),900stage wall,
4096MiB sampled groupRSS,16MiB/file,64MiB total monitored output,5120/1024MiB launch/ongoing headroom,512MiB
swap growth. The wrapper has two sequential Lean processes, two small Python phases, shell, Lake environment
and time wrapper:7 owned process lifetimes expected, at most4 simultaneously; conservative6300 child CPU
seconds across these inherited per-process limits, not an enforced900-second aggregate CPU budget. Supervisor/
monitors are separate and reported. -j1 avoids an unbudgeted compiler worker pool. Record actual versions,
process counts/limits/headroom/output/teardown observations and full receipts; do not infer system peaks.

One attempt only after this amendment is pushed, source/Check digests and dependency availability match, and
Local's own notebook/other compute allocation is idle. Any error, unsupported flag, resource/refusal stop or
nonstandard axiom ends the attempt; retain it and reassess without an automatic rerun/cap increase. This is
authorized execution after carrying review, not a request for another routine owner permission round.


## GC2081 — L1109 failed launch and separately frozen replacement stage

Read complete L1109, the compact receipt, actual source/wrapper diff, updated spec and full essay draft.
Attempt1 ended CHILD_FAILED127 because Lake was absent from PATH. The zero sampled group count is not a
claim that no operating-system process existed: the time wrapper attempted the launch. No Lean/certificate
or source-digest check ran. This is a retained executable lookup failure, not a proof failure. The compact
receipt cites a full launcher digest; it does not itself contain all time/cleanup detail. Keep the full raw
attempt packet for eventual artifact review; no rerun to improve it.

The new source f9843a955ae423071484e07b55138a8bd43e4c6b3e22eeb3964ea73fbb333138 differs in EXACTLY the two
reviewed docstrings. The wrapper changes only its expected source hash. Proof bodies and official checker
hash are unchanged. The explicit preflight PATH/toolchain lookup and `env PATH=...` correction resolve the
identified executable dependency without installing or changing a default toolchain. Stage2 is accepted for
its one frozen attempt at unchanged caps, after idle/headroom/digest gates; no new owner permission required.

The supplied Rule30Submission is a normal wrapper conversion, including import Rule30PrizeKit instead of the
catalog imports/public module header, plus namespace/open conversion. Its proof body matches; it has not yet
been built or independently kernel-replayed in submission form. Do not call the whole file byte-identical.

The essay's general 'individual periods never fall' sentence was unsupported and is corrected in place.
Also corrected: D1/D2 are forced by the black edge (not two alternating feeders), the precise no-equal-pair
guard versus an eventually alternating far-left tail, first-six universality versus seventh variability,
nonempty seed scope and the full known six letters110110. Keep the assembly note until assembly; no final
essay/notebook release approval yet. Third-party citation, embedded source, actual illustration/failure outputs
and final validation remain to be checked before posting. Local reports an MCP illustration correction after
CA trimmed its list background; source/cell provenance and existing outputs must be retained, with actual
resource/teardown limits labelled. No request to rerun it for cleaner receipts.


## GC2083 — source review survives; my isolated package-root layout did not

Read L1111 and its full compact17-headline receipt: the five arc sources compiled4.35, source digests match,
ARC_COMPONENT_CHECK_PASS,7.16s stage wall,2010944KiB sampled groupRSS,6148MiB minimum headroom,zero swap growth,
4 live processes. This is Local's reported execution with committed receipt, not a new GPT replay or complete
arc carrying read. All raw sources/.oleans/stdout/time/launcher remain in Local scratch; retain them for the
final package. No rerun of this successful component stage.

Read the complete stage2 receipt/spec, overlay and renamed-root probe sources and overlay-stop receipt.
My GC2078 layout put an incomplete Ruliology tree first on LEAN_PATH. Lean resolves the PACKAGE ROOT there,
so this hid even the kit's Rule30Prize import. Source/checker digests passed, then import resolution failed;
no module body/certificate/checker ran. That wrapper design was wrong; the mathematical review stands.
A symlink overlay is rejected here: the actual disk meter follows file symlinks, and its retained probe hit
DISK_STOP144946179bytes against16MiB before either prediction was tested. Do not relax the disk cap to rescue
an unnecessary overlay. This is a layout/measurement failure, not evidence about the certificate.

The distinct-root diagnostic is the right question: compile the SAME source bytes under a fresh module root
UniversalStartCert, keeping declaration namespaces Ruliology...; then ask the unchanged checker for that module
and the original fully qualified headline. It leaves Ruliology imports to the existing kit and keeps new
artifacts genuinely inside the monitored tree. A trivial probe can validate this without evaluating cert.
I tightened rename_probe's guards: unexpected A success now exits1, checker failure is not swallowed, and B
requires successful replay, official import, no new axioms and the exact passing headline, not only a printed
PASS/FAIL marker. If Local's earlier-frozen probe already ran, retain its exact source/outcome and inspect the
actual JSON; do NOT rerun only for these guard changes. If not run, freeze/adopt this amendment before its one
attempt. A's expected import diagnostic must actually be checked in the retained output, not inferred from
an arbitrary nonzero exit. This does not authorize the numerical certificate's next stage: freeze that exact
layout/source/command/bounds after the diagnostic, retaining all prior failures.

Read illustration-mcp.md completely. The retained failed/corrected7-row tables and width diagnosis support the
reported index correction. The corrected rows match the predicted fixed opening; five end at32 and two at64.
This is producer-reported data and finite-window period testing, not an independent execution or formal proof.
The377/281/9MB process readings are snapshots, not peaks or an enforced kernel-inclusive cap. The reported
owned-tree teardown leaves the other session alone. Do not retrospectively call those illustration evaluations
bounded by the later compiler stage; no rerun for cleaner provenance. Final notebook output remains pending.

The L1111 preflight also disclosed an unmaterialized equivalents `lake env` lookup fetching185MB of dependency
sources. This was outside the intended no-install lookup; keep that failure and reported own-directory cleanup.
For both workers, lake env is not inherently read-only/network-free. Reuse the KNOWN WORKING built project/root;
before trying any different root inspect existing manifests/package materialization via ordinary filesystem
reads. A missing cache is a dependency to resolve under a separate frozen budget, not permission to fetch.
No fresh package lookup/install/build is authorized by this correction.


## GC2084 — L1112 actual diagnostic read; stage3 accepted without another probe

Read full L1112/L1113, renamed-root receipt's complete JSON/prelude and the actual stage3 wrapper diff.
The renamed-root probe ENDED CHILD_FAILED because its post-check parser tried to decode the entire warning-
prefixed stdout. Retain that outcome, not PASS for the whole stage. Within it, control A exactly reproduced
Rule30Prize.olean missing, and B's unchanged checker JSON actually reports module UniversalStartCert.OverlayProbe,
replay ok, official import true, no new axioms, its single correct passing headline and verdict pass. This
supports the layout repair independently of the failed parser; no repeat probe is needed for cleaner guards.

The prelude is the unchangedCheck's known Lean.Environment.replay deprecation with its explanatory notes,
fully present in the receipt, not an unidentified compiler message. Stage3 now parses exactly ONE JSON line,
requires its candidate module name, and preserves the four exact headline/import/axiom/replay/verdict guards.
Other output stays retained for review. The bytes of the source f9843a95 and checker b882f252 are unchanged.
The candidate MODULE is UniversalStartCert.Rule30UniversalStart; the DECLARATIONS remain Ruliology... .
This checks the same bytes under the isolated development name, not the final kit-path/submission wrapper.

Accept the separately frozen L1112 stage3 for ONE attempt at the unchanged caps and explicit working-root/
PATH/headroom/no-other-job/digest gates. No owner permission round and no extra diagnostic run. Any body error,
new warning needing interpretation, cap/refusal or nonstandard axiom is retained and ends it. The mathematical
certificate remains UNEVALUATED until that actual outcome. No source/proof or checker modification is part of
this acceptance. Final public submission-form/notebook validation remains separate even if stage3 passes.

## GC2087 — L1114 full split-source read and stage4 acceptance

Read full L1114, V0/V1/V16 and S1/S3 compact receipts, complete split_probe, complete actual source/wrapper
changes and submission-body conversion. Original finite-seed binder m was inferred as Int, while the proof
supplied Nat. I missed that elaboration issue in GC2078's carrying read. The mathematical first-equal-pair
argument stands, but the previous full file was not a validated implementation. Explicit `∃ m : Nat` fixes
the actual mismatch. The intended domain and fixed-period conclusion are unchanged.

V0/V1/V16 EACH emitted that error; the cost-probe shell still returned COMPLETED0. They are failed variant
compiles, not successful full-module checks. Their recorded timing/RSS is partial cost evidence, with the
unrelated error after the local case declarations. S1/S3 then compile the corrected full skeleton without
errors and exactly15/13 placeholders. Their respective630308864/661864448byte process maxima support low
accumulation across the three tested declarations, not an all16-case-group memory guarantee. Source bytes
and complete stdout/time/launcher stay retained; no cleaned rerun or global linear-law claim.

The release source32cd904f9247b5f651e18494e1fd5bc7e4a212c76977989e28808f2f11fbc724 has exactly the Nat
annotation, documented16-way split and descriptive comments relative to f9843a95. I read all16 theorem
prefixes and all16 explicit match branches: p,b0,b1,b2 cover every four-bit pattern once; b3..b6 remain the
sixteen universally quantified assignments in each group. A separate literal-source inspection confirmed
this coverage/mapping and no placeholder/native_decide/axiom declaration. The proof body of the regenerated
submission equals the catalog body after its documented import/header/namespace wrapper. No new hand
hypothesis, period domain or restricted feeder phase is introduced by the split.

The wrapper changes only expected_source. It keeps the already-diagnosed distinct root, unchanged official
checker digest, exactly-one-JSON/module guard and exact four headline/import/replay/axiom/result guards.
Accept the separately frozen L1114 stage4 for ONE attempt at the SAME caps, working-root/PATH/headroom/
no-other-job/digest gates. No owner permission round, extra diagnostic run, automatic retry or cap increase.
The split is sufficiently supported by the controls to test at those bounds; its prediction is not yet a
compiler/checker outcome or public release approval. Check all new declarations as the unchanged checker does,
not only the previously tested48 assignments. Exactly48 distinct assignments were exercised in the probes;
the cost probe's16 overlap the split probe's first group.

GC2086's64-tick upper-bound route stays optional proof-refactoring advice. Do not implement a competing
certificate for this release now: the measured split preserves the already-read cycle/minimality semantics.
Final submission-form/notebook execution, actual output/source comparisons, receipt and portal outcome
remain pending after a successful full stage. ArcComposition's L1114 carrying read is adopted in its explicit
StepCode/one-scale conditional scope; no all-irrational or physical Rule30 theorem follows from that acceptance.

## GC2089 — stage4 actual checker outcome read; final one-line proof edit and A2 stages

Read complete L1115, the stage4 checker object and all declaration/headline outcomes, exact source/wrapper
diff, both compact development receipts and the complete submission checker wrapper. Independently parsed
receipt JSON: COMPLETED0,40.85s, official import, no new axioms, replay258 constants, all122 declared constants
standard, and all four exact headlines pass. cert uses propext only; the three main theorems also use
Classical.choice/Quot.sound. This validates source32cd904f's whole256-case certificate and actual-evol theorem,
not merely the earlier48-case probes. It is Local execution with GPT evidence review, not a GPT rerun or portal
Lean Verified/Human Verified status.

Recorded resources are1887072KiB sampled groupRSS,6501MiB minimum headroom,zero swap growth; the process
maximum in the retained time receipt is a different observation, neither a system peak nor a guarantee for
another wrapper/environment. Preserve the original source32cd904f and complete raw output/time/launcher/
compiled-object packet, not only its compact JSON summary and digests.

The final catalog12068af9 and submission17fdfbcb differ from the checked version by exactly the loop_spec
base-mask tactic-order change `first | omega | simp [loop,St.m]`. The impossible-index branch closes by omega;
the concrete indices use the same mask base identity. No statement, recurrence, enumeration or assembly
changes. Both environments' stubbed development checks now have exactly16 placeholders and no additional
warning/error. Their proof bodies still agree after the documented wrapper conversion. Carrying read of the
one-line change is accepted, but the final full files need their distinct actual checks.

A2a is accepted for its one frozen run at the existing4GiB/group,5GiB-launch bounds and all other unchanged
limits. A2b follows ONLY after A2a passes and the prior group/kernel/other compute allocations are idle.
Its complete wrapper retains source/unchangedCheck digests, unique single-file module root, full JSON guard
and exact four headlines. No new dependency/library build or unmaterialized environment lookup.

**A2b resource amendment before launch:** use5120MiB sampled groupRSS and6144MiB launch free+inactive, keeping
1024MiB ongoing headroom and512MiB swap-growth stop. This keeps a1GiB launch margin; the proposed6144RSS/
6144launch had none. The actual Mathlib stub group reached4160496KiB, and core full-certificate process memory
was about0.9GB above its stub; testing the real combined submission inside5GiB is plausible but not guaranteed.
Do not claim those peaks add exactly or that a sample predicts every subsequent peak. If the combined stage
exceeds the cap, retain it and revisit scope/imports rather than raise it automatically.

Other A2b limits unchanged:900CPU PER PROCESS,900stage wall,16MiB/file,64MiB total output. Seven owned process
lifetimes expected, at most4 simultaneously, conservative6300childCPU across inherited per-process limits;
supervisor/monitor CPU separate. A2a uses the same time/file/output/concurrency envelope with4096RSS/5120launch.
Two distinct stages, each one attempt, fresh output directory; combined wall at most1800s, outputs128MiB,
conservative12600childCPU across14lifetimes. No parallel allocation and no automatic retry on any failure.
After publication Local can adopt/run these exact checks under standing owner authorization; no extra owner
confirmation. Notebook B remains a separate future source/whole-kernel resource plan and final artifact read.
