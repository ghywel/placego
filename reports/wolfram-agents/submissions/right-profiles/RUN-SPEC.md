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
