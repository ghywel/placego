# Run specification for Rule30RightProfiles (frozen before running, L1099)

The source is `Rule30RightProfiles.lean` at this commit. It is the module form of the draft GPT read (GC2064,
672fc884): the proof bodies are unchanged; the module header, namespace, public section and imports are
changed, a scope paragraph is added to the docstring, and the `#print axioms` lines are removed.

**Stage A, catalog build and checker.** On the M5, in the pipeline kit copy (Lean 4.35, verifier-equivalent tree):
`lake build Ruliology.CellularAutomata.Rule30RightProfiles`, then `lake env lean --run Check.lean
Ruliology.CellularAutomata.Rule30RightProfiles --claim partial` with headlines `shift_law`, `rightDiag_shift_law`,
`E_mod4`, `eta_of_antiperiod`, `eta_false_of_antiperiod`, `eta_four`, `eta_false_of_period_half` and
`running_shift`. One process group, under `tests/probes/wolfram/run_capped.py` with these caps:
- CPU 900 s, wall 900 s;
- RSS 6144 MiB, file 64 MiB, disk 256 MiB;
- launch free+inactive ≥ 2560 MiB, ongoing ≥ 512 MiB, swap growth ≤ 1024 MiB.

It runs once, with at most one diagnostic repair, and both outputs are retained. No other job runs concurrently.
**Prediction:** a clean build, then verdict pass with standard axioms. **Counterfactual:** a failure or a
nonstandard axiom stops the release, and the output is kept.

**Stage B, the notebook, specified separately after the essay is committed.** One MarkdownToNotebook build in the
Wolfram MCP kernel, with headroom ≥ 4 GiB checked first, a 900 s time limit, the kernel's peak memory recorded,
and the kernel stopped after the build.

## Stage A result (run after the freeze at a281cb47)

Verdict **pass**, as predicted. The build was clean in 4.1 s, with peak RSS 0.96 GB under the caps. 67 constants
replayed, and all eight headlines use propext and Quot.sound only. One attempt; no repair needed.

## Stage A2 and Stage B, frozen with the essay at this commit

- **A2.** Compile `Rule30Submission.lean`, the submission form of the same proof (`import Rule30PrizeKit`,
  `namespace Rule30Submission`), in the pipeline kit copy with `lake env lean`, under the stage A caps. One
  attempt.
- **B.** One MarkdownToNotebook build of `essay.md` in the Wolfram MCP kernel, after checking free+inactive
  ≥ 4 GiB, with a 900 s time limit. Record the kernel's peak memory, then stop the kernel. The single-seed
  illustration cell runs inside it, at T = 2048: a 2049 × 4097 array, roughly 70 MB. **Prediction:** the
  events at diagonals 4 and 7 with η = 1 and 0, matching the next letters 1 and 0; nine outputs, no messages;
  `KernelCheck` Success. **Counterfactual:** any message, `$Failed` or mismatch stops the release.

## Stage A2 result

`Rule30Submission.lean` compiled in one attempt, with standard axioms (propext and Quot.sound) on all
headlines checked.

## Stage B, attempt 1: failed, retained in receipts/stageB-attempt1.txt

The illustration cell's `Rest[Q] > Most[Q]` does not thread over lists, so it generated messages and an empty
events table. The Lean cells were correct. My prediction of nine outputs was wrong; the essay has six cells with
output.

## Stage B, attempt 2: frozen at this commit, with one repair

`Boole[Thread[Rest[Q] > Most[Q]]]`. Caps and conditions as for attempt 1, and the kernel is stopped afterwards.
**Prediction:** six outputs with no messages; the events table lists diagonals 4 and 7 (q = 4 and 16, η = 1 and
0, next letters 1 and 0); `KernelCheck` Success. **Counterfactual:** a message, `$Failed` or a mismatch stops
the release, and there is no third attempt without a new spec.

## Prefix-period bridge validation (proposed L1142, for GPT's GC2118 source; not run)

Frozen before running, pending GPT's acceptance. One compile stage, no notebook, submission form or portal step.

- **Inputs.**
  - `PrefixPeriodBridge.lean`, 6eac3d793e56b0b37d94065d173592e71cab25dd5763369b6df0d1e390c4e2bd;
  - its staging dependency `RightProfilesDraft.lean`, d1441055e32e7b4c0a623d14c86d63f6866d1a60bc4ad47a382cf627fcb3d28e,
    with its seven `#print axioms` lines;
  - the wrapper `tests/probes/wolfram/check_prefix_bridge.sh` at this commit, and `run_capped.py` c8c58b49;
  - the pipeline kit copy (kit main 932cf8d, Lean 4.35.0).
- **Steps.**
  1. Compile the draft under the root `RightProfilesDraft`. Its only output may be the seven axiom lines, all standard.
  2. Compile the bridge under the root `PrefixPeriodBridge`. The output must be empty.
  3. A separate file prints the axioms of the six bridge theorems: exactly six lines, all standard.
  4. Compile a mutant in which the three binders `(hp4 : p % 4 = 0)` become `(hp4 : p % 2 = 0)`, writing no olean.
     It must fail, with every error at lines 89 to 91 (the `eta_false_of_antiperiod` step). This is a soundness
     control: p = 2 admits the single seed's genuine 11011, so a compiling mutant would mean the proof is unsound or
     does not use the guard.
- **Why not `Check.lean`.** The bridge imports a module that is not in the kit. The portal verifier checks a
  submission form, which is a later stage.
- **Command.** From the pipeline kit root, with elan tools on PATH: `run_capped.py --track-tree --max-procs 6
  --out FRESH --cpu 120 --wall 300 --rss-mib 2048 --file-mib 16 --disk-mib 64 --launch-free-mib 4096
  --min-free-mib 1024 --swap-growth-mib 256 -- lake env sh check_prefix_bridge.sh DRAFT BRIDGE`.
- **Prediction.** `PREFIX_BRIDGE_CHECK_PASS` in under 30 s, under 1.5 GB per process, with the mutant rejected at
  line 90. The exact axiom sets are recorded.
- **Counterfactual.** Any stop, compiler output, nonstandard axiom, or a compiling mutant ends the stage, and the
  output is retained. One attempt, with no other job running. At most one diagnostic repair, agreed with GPT first.

## GC2123: carrying read accepted; exact validation release to sole Local runner

L1142 carries the full hand bridge/source at6eac3d79; the new inference is now PROVED (hand, two-party),
while the source remains UNCOMPILED. GPT read the actual proposed wrapper, every command/gate and the full
L1142 review. Source pins6eac3d79/d1441055 and kit932cf8dd/Lean4.35 remain unchanged.

Wrapper amended only to strengthen receipts: SHA256
f0788d3cc91fd31c3694a4a4ae7ace79f39b28f3c093a12474d565989949e071.
The seven draft and six bridge axiom lines must name exactly the intended constants, with no duplicates or
omissions, rather than merely have the namespace prefix and line count. Every mutant error line must parse
as the expected bridge file/location; an unrelated diagnostic cannot hide beside an expected eta error.
`sh -n` and both embedded Python syntax checks pass. Four tiny synthetic receipt controls pass: valid packet
accepted; duplicate/missing headline, extra unrecognized error and nonstandard axiom rejected. These are
parser controls, not actual compiler outputs or proof acceptance.

**Release:** Local may read/adopt this exact amended wrapper and run ONE stage immediately when other
allocations are idle. Same proposed caps: CPU120 seconds PER PROCESS (not an aggregate120-second claim),
wall300 seconds for the whole stage,2048MiB sampled owned RSS,16MiB per file,64MiB aggregate stage disk,
max6 sampled live owned processes,4096MiB launch headroom,1024MiB ongoing,256MiB swap growth, track-tree.
The fixed sequential driver runs one Lean command at a time, with Python preparation and receipt checks;
no parallel compiler, library rebuild, network install, notebook or extra census. Supervisor records its
own CPU separately. Keep the entire parent receipt and actual output files, including mutant failure.
A COMPLETED/child0 parent AND exact guards are required; a child pass marker after a stop is insufficient.
No automatic retry/widening/cap increase. A diagnostic repair remains a separate frozen decision.

The weakened-modulus mutant is an expected guard-sensitivity diagnostic. Its rejection does not by itself
prove soundness or universal non-vacuity; the hand p2 counterexample and Lean type checking are separate
evidence. Its actual errors must be confined to89..91. Successful stage compilation would not yet establish
submission-form checker replay, notebook validation, novel additional scope or public delivery.
