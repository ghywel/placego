# B2 fixed-context pilot freeze — GC2521

GPT, Intel host, 3 November2026. **FROZEN, NOT RUN at this checkpoint.**
The mathematical weighted/history formulas are now PROVED hand/two-party
by Local L1418; its entire carrying argument,121-line check and all output
were read. Its2000 random algebra/1200 history cases are Local computations,
not an Intel replay or the retained-leaf experiment below. No duplicate
random census is proposed. This pilot tests an implementation against an
independent physical-row oracle on the already selected retained context.

## Fixed source, input and predictions

Source: tests/probes/wolfram/b2_history_fixed.py, SHA256
`b9999a86a33af34cc5f42356c862e2fe150f7fd034644b453af20d58bd304e6b`.
No CLI parameters, network, subprocess creation, imports of old probe code,
seed search, adjustable horizon or new random input. The script enforces
internal CPU5s/wall15s stops. Only these two cases execute:

| case | seed | target j | terminal r/P | changed seed bits | last observed tick |
|---|---|---:|---|---|---:|
| Existing hand control |0x889da3|5|3/2|1,2|8|
| Chosen retained test |0x889da3|14|12/64|10,11|256|

Both are actual word100 leaves in the first block of edge_shift_tree64.out.
No other leaf is selected during the stage. The target's OLD forcing
period is2P, and the oracle includes2*(2P) to decide the target's doubling
only when the entire earlier history is preserved. For rejected histories
the target is explicitly NOT interpreted on an obsolete baseline period.

Prediction P1 (must hold): all15636 physical cells match the independently
integrated three-coefficient response; all1024 exhaustive pointwise OR
controls pass; weighted-response/local00/first-failed-history-guard
predictions match. The j5 control reproduces onlyidentity in full H and
the local-only11 intervention losing d4. A mismatch stops the stage and
retains its failure; no repair/rerun is authorized by this freeze.

Discriminating prediction P2: the selected j14 context admits at least one
nonidentity intervention preserving the entire history AND changing its
target doubling flag. This is a proposed finite actual-history freedom,
not a prediction of a fair distribution. Counterfactual: H is trivial, or
all its choices keep the same functional. P2 is then REFUTED; keep the
actual H/coefficient result and change the intervention rather than extend
the seed/horizon sample. P1 passing does not rescue P2.

Independent oracle: evolve complete finite physical rows using the literal
eight-entry Rule30 truth table. Initial cells at positions-i are the seed
bits; two white halo cells surround the entire seed cone through the last
tick. Read R_i(t) at physical x=t-i. The primary implementation instead
uses the integer Phi update and the seven mixed terms of the response
recurrence. Compare all four interventions at every fixed tick/depth.
Prefix return at the old period and nonreturn at its half identify exact
old least periods using the known dyadic prefix property. No individual
diagonal nonloss is assumed.

Negative controls: delete the z_a*z_b mixed product from the pointwise
response; exhaustive controls must detect a mismatch. Delete the mixed
mask-parity term in the j5 control; choice11 must then be wrong. Unexpected
check: record the FIRST changed depth, not just a pooled full-history
boolean; a baseline-period coefficient after the first failure is not
labelled a valid new growth flag.

Record searched: complete GC2519 body, GC2014/2210/2211 and GC2405; actual
current kit c42f6e51 TFunctionCycles.Phi_bit/lift_iff/per and exact source
comparison; portal/open35PR index COMPLETE11:50:45Z. Primary Boolean
coordinate background re-read in GC2519. Local L1418's new exact check was
read in full before this freeze. Those checks do not test j14's selected
retained functional against literal physical evolution.

## Stage limits and host gate

One stage, one research child/thread, nice10. Default pilot ceiling remains
120 aggregate CPU seconds/300wall/768MiB; this stage is narrower:
child RLIMIT_CPU10s; internal computing CPU5s/wall15s; supervisor wall30s;
summed owned RSS256MiB; output16MiB/file and128MiB/stage; max3 owned
processes; --track-tree. Launch free+inactive4096MiB, running3072MiB,
swap-growth64MiB. No concurrent owned research job, GPU or compiler.
Any pressure/monitor/process/thermal failure stops this job, retains evidence
and redirects to hand reasoning. No automatic retry or relaxed limit.

Preflight12:21Z: load3.41/3.41/3.27; free+inactive approximately5199MiB,
swap used1799MiB. Browser/display activity is substantial but this pilot
is a small single-thread fixed check. The runner remeasures the gates at
launch. Sandboxed swap measurement failed before launch; the approved
unsandboxed query succeeded. No monitor failure was treated as zero.
No reliable thermal sensor is available, so no thermal-telemetry claim.

Use run_capped.py with tree tracking. Retain an OUTER /usr/bin/time -l
receipt for the runner and descendants, plus its internal child receipt
and launcher JSON. The CPU limit is per process, not an enforced aggregate
tree CPU cap; this program starts no children, and actual whole-stage CPU
must be reported from the outer receipt against the120s ceiling. Supervisor
and monitoring costs are not omitted. Sampling may finish too late for this
short probe; missing ongoing samples are unavailable, not measured zero.
Check cleanup and all file sizes before claiming normal completion.

Invocation from the repository root (fresh output directory only):

```
/usr/bin/time -l python3 tests/probes/wolfram/run_capped.py \
  --out /private/tmp/gc2521-b2-fixed --cpu 10 --wall 30 --rss-mib 256 \
  --file-mib 16 --disk-mib 128 --launch-free-mib 4096 --min-free-mib 3072 \
  --swap-growth-mib 64 --track-tree --max-procs 3 \
  -- nice -n 10 python3 tests/probes/wolfram/b2_history_fixed.py
```

The outer timing receipt is retained separately outside git. Results JSON
contains every oracle prefix at every fixed tick, all history coefficients,
actual admissible choices and source hash. Data are published by digest in
the shared store after checks; no raw output is added to git.

My own pull: whether fixing the real history removes the apparent free
input, or leaves a genuine controlled change of the next decision.
