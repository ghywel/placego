# SW-02 Phase C batch 2: carrying review

GPT, GC2825; manual block requested by the owner on 10 November 2026. Both recurring
schedules remain PAUSED. Cloud owns batch3. Verdicts below are pending until the
source read is complete; no new mathematical status follows from this freeze.

## Fixed replay freeze

Record searched: CL763 and its complete triage/handover; the eleven original pending
door cards; original RS-1, BR-2 and SKM-BR-2-1, LN-13, LN-06, PE-2, R-03/R-04/R-13,
CP-5 and CM-1b source material in the raw archive (SHA256
`c231157f6daeb1433d2c8aaf2e0190f78b5c4723009fdcc32ee8842a5c11d94c`).
Current kit `03a19bf6240b63c6d15894c5f7552f3a6091d937`: actual
ZeroBoundaryBarriers, PeriodTwoSideways, UniversalLeftSide/FourFrontsBase,
StripCertificates/EtherTrap/Width20 and Realization definitions/proofs. Refreshed
complete kit/portal/open-PR index at 15:47:19Z, portal 15:47:08Z, 37 open PRs.
The index delta is not a carrying read of all new sources. Primary Delacourt–Ollinger
and Rowland papers opened; exact carrying sections are recorded with the verdicts.

Prediction, before execution: the guarded local 010 two-update identity, one-wheel
healing, and RS-1's parent pulses/window inequalities pass; all four kit strips obey
the corrected birth inequalities through wheel87866 at W=1 (hence W>=1 and s>=0).
The original `k_guard3.py` replay reproduces controls116976/117702, minimal prefix19197
for its two guarded rules, and the recorded 19656 endpoints54841/58753. The claimed
minimum also requires a monotonicity argument; binary search alone is insufficient.

Counterfactual: a mismatch refuses the corresponding numerical carry and preserves
its output; no larger seed, horizon, parameter box or automatic retry. Positive
controls: exact parent pulse 1..7, 16-step strip return and archived prefix endpoints.
Negative/unexpected controls: replace010 by000 (must lose shielding); compare the
depth1 discrepancy cancellation and persistence cases. No conversion of finite
checks into universal trajectory observations; the universal parts need the hand
arguments below. No other RS-1 simulation, ring/strip census or formal build.

One fixed Intel CPU stage, at most120 aggregate CPU seconds/300 wall seconds,
768MiB process-tree RSS, maximum2 processes (one worker, no worker subprocesses),
one CPU thread/nice10. Output outside git,16MiB/file and32MiB/stage; total stage disk
at most32MiB. `run_capped.py --track-tree --cpu 120 --wall 300 --rss-mib 768
--max-procs 2 --file-mib 16 --disk-mib 32 --launch-free-mib 4096
--min-free-mib 1024 --swap-growth-mib 4096`. Real tree accounting and host monitoring
stay active. Pressure, swap, thermal warning or monitoring failure stops the job;
no retry under enlarged caps. Headroom checked before launch; no other heavy job,
no GPU and no Wolfram. Source hashes are frozen in the pre-run commit; original
guard replay additionally asserts SHA256
`db4bd5ccd897071ac660251274caee3926c0cf4f9889ba216633465c16da3ce7`.

Executable: `tests/probes/swarm/sw02/carry/gpt_batch2_checks.py --raw-root RAW
--kit-root KIT`, with the verified outside-git raw extraction and current kit.
Only this fixed run is authorized by this freeze. Hand review continues separately.
Frozen runner SHA256: `f2f1af074d7caafdcefd6410eec2f17ea959c7c177d68558f3418392efc17398`.

### Additional fixed witness validation, frozen after the topology issue was found

The first run completed PASS,15.189060 aggregate CPU seconds. The deadline card's
closed-family argument is false: InFamily is a union of cylinders. A finite
eight-tick discrepancy from every ether column repairs the argument. To validate
its exact input independently, one additional fixed certificate search/check is
frozen here: starting temporal-column pair(136,14), period8, at most512 pairs;
find one spatial lasso, then check every edge with an independent scalar Rule30
equation. This is one existing witness, no classification or period enlargement.
Prediction: a lasso exists, column1 has least temporal period8; the seven ether
columns pass and a one-cell mutation of the returned lasso fails. Counterfactual:
no lasso within512 pairs leaves the deadline conclusion conditional, with no retry.

Second run ceiling5 aggregate CPU/30wall/128MiB RSS/tree2processes/1thread/nice10,
1MiB per file/4MiB disk; same4096MiB launch/1024MiB running/4096MiB swap-growth
guards. Stop on pressure, thermal or monitor failure. Combined charged CPU will
be at most20.189060 seconds, within the original120-second pilot allowance.
Source `tests/probes/swarm/sw02/carry/gpt_deadline_witness.py`; its pre-run commit
freezes the complete source. The first run and its evidence are not repeated.
