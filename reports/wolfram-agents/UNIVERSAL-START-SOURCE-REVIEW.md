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
