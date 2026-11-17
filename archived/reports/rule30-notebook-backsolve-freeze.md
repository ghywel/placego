# GC1985: one exact back-solve extension stage

Owner requests recording the Ouroboros question and returning to Local's waiting test. GPT reviewed L1031's complete driver and the imported evaluator/control definitions plus complete supervisor. One bounded Intel run is frozen here. Local must not duplicate it. Schedules remain paused.

## Question and predictions

Can the retained P/Q and R rows be extended two physical updates backwards under the same alternating wall, shifting their visible words one age later? Follow the full tree for two such delays of P/Q and one of R. No new seeds, sampling, SAT, further ages, or automatic reruns.

Local predicts all P99/Q100, P100 and R100 succeed. Counterfactual: an empty predecessor frontier blocks extending that particular retained row only; it does not exclude the word at the new age. Even complete failure here does not settle the proposed SAT membership questions. Success closes only E34^8 = E100^8 in the clamped right-cone language, not an infinite-age statement or the natural centre prize.

## Carrying review and controls

Choose the two rightmost parent bits; the inverse recurrence uniquely fills the rest. Enforcing the left wall equation is necessary and sufficient. Reverse phase1 then phase0, restoring the starting phase after two forward updates. The shrinking cone gains two cells when reversed. The target widths and output times have enough causal margin.

Corrections before freeze: remove the four-row truncation, retain all candidates, assert complete one-step forward equality at each reversal, bind the full input digest and width, and retain every row and full cell1 trace. A fixed witness is not guaranteed extendible merely because it exists: its delay is a prediction, not an instrument axiom. A separate guaranteed positive control takes the fixed row forward twice, reverses that result, and requires recovery of the original row. The fixed-word delay result is reported even if false. Exhaustive width8 reverse sets are compared with all512 width9 forward rows under both phases. Each successful target is replayed using the literal table evaluator.

Unexpected check: the original top-four pruning could discard the only second-delay success. There is no pruning after amendment; all at most16 first-delay and256 second-delay candidates are processed and retained. This changes completeness of the retained-row extension, not completeness of word membership.

Record searched: record_find.py 'back.solve|Ouroboros|witness delay',10 paragraphs/5 files; read L1031, GC1983 actual review and DQ023's existing support-replacement/finite-state obstruction. No novelty claim.

## Frozen inputs and bounds

Input: cited/l1030-witness-pilot/latest_witnesses.json,15620 bytes, SHA256 ef0ff89cfeee5c4f13def41b9df493d76e5b55f358a1487a27296bffbbccdf90. Reuse the digest-verified local copy; input admission cap64KiB. Exact source hashes:

- `notebook_backsolve_extend.py`: `24cef54728a424f4155946333cc564fa0c6e1570e25371300f6f7dc83022fea5`
- `notebook_death_gate.py`: `6e51527c1198218ed6d1f50e57c09a922ae29713b5bb2258298e7c763f9ff5ee`
- `notebook_witness_pilot.py`: `e25dd2cff3740df3c364ce744ca3c837f77a7f5f1b9302bf80af423466df0a29`
- `run_capped.py`: `38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c`

One CPU worker; no solver, subprocesses or GPU in the probe. Child RLIMIT_CPU60s and55s admission guard; supervisor wall120s; sampled process-group RSS256MiB; per-file4MiB and total output16MiB; launch free+inactive4096MiB, stop below1024MiB or swap growth256MiB. Default one-second sampling has polling/command latency; these are sampled pressure/RSS/wall stops, not hard instantaneous system ceilings. Supervisor CPU is separate and recorded. Control loop has512 target checks, each512 forward candidates; extension at most16+256+16 candidates plus controls, row width at most219. Source allocations and retained output are far below the caps. No network during execution; data stay outside git. Python bytecode disabled.

Invocation: python3 tests/probes/wolfram/run_capped.py --out "$RUN_DIR" --cpu 60 --wall 120 --rss-mib 256 --file-mib 4 --disk-mib 16 --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 256 -- python3 -B tests/probes/wolfram/notebook_backsolve_extend.py "$INPUT_FILE"

The environment sets PYTHONDONTWRITEBYTECODE=1. Fresh output directory only; failures and supervisor receipts retained, no retry or widened follow-up. A separate read of actual retained candidate rows checks literal Rule30 evolution before accepting positive results.
