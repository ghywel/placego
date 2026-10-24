# Submission d-exact-60: the death time at width 60 is exactly 114, a complete chunk certificate and its witness (Local, 2026-10-24)

One module (tests/probes/wolfram/d3_submission.py, width 60): the 4,096 chunk checks `check 60 115 18 c = true` by
`decide +kernel` in 256 namespaces of 16 with `range` trees, `all_chunks`, `q01_width_le_60` (t <= 114), the witness
0xe77a4e77b8f99b5 through the kit's `prun` and `run_toFun`, `death_time_60_exact`.
- **Headlines:** `Rule30Submission.death_time_60_exact`, `Rule30Submission.q01_width_le_60`.
- **Local check (W6, supervised, L844):** `lake build` 1,181 s (1,011 s user, 158 s system, process maximum resident size 4,455 MiB,
  sampled process-group peak 5,042 MiB); the kit's checker 1,169 s (replay of 8,466 constants, 4,363 declared, standard axioms,
  no new axioms; process maximum 4,270 MiB, group peak 4,930 MiB); all nine final predicates true; `check.json` in the W6 output folder.
- **Imports:** `Rule30PrizeKit`, `Ruliology.CellularAutomata.Rule30ZeroBoundarySmall`, `...Rule30ZeroBoundaryLanes`.
- Expected notebook outputs: {60, 114}; the orbit plot; the environment; the headline and the three statements; the first
  and last chunk checks and `all_chunks`; `Axioms` standard; `KernelCheck` Success. The notebook build repeats the
  kernel work through LeanLink; its own wall time, memory and outcome are recorded from its run, not inferred from W6.
- Provenance wording follows GC1744's and GC1759's corrections. Byline and API fields as for the earlier submissions.
