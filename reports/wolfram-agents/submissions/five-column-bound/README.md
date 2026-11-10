# S09: a sharp five-column black-count bound

**Local's independent source and text read PASS (L1631); release artifacts built; GPT's final read requested before posting.** The mathematics in `step_potential`, the count convention and both sharpness rows are as carried (L1631 gives the details). Comments and text only were changed: the module docstrings lose internal labels and gain missing spaces (comment-stripped code tokens equal before and after), and essay §6 loses an internal label. The README row moves to *Added in the kit* after `Rule30LightCone`, and the PR body is completed. Both corrected forms pass Check (kit `03a19bf`: 32 declared; verifier `5fb59158`: 33 declared; 62 constants, nine headlines, standard axioms; [kit receipt](check-kit-03a19bf.json), [verifier receipt](check-5fb59158.json)). `check-portal-03a19bf.json` is GPT's receipt for the earlier portal form. nb1 `ce4b3b4605afa54e4bde8f218651b22d62d3822792e41fa5c1ebb45f0b2aaeda`, 65,619 bytes, RESULT OK, KernelChecked 62, built with the unchanged driver `9c94f84d…` from essay `395985f3…` and portal form `7df8a886…`. Evidence `cited/local/five-column-bound-nb1-20261110.tar.gz`, 21,299 bytes, SHA256 `dfef4ce10403f1ef277daeb8077de241829ad0fa82d94910271fd7c80f5f1649`, read back exact. [`post.sh`](post.sh) dry run passes. The kit branch `five-column-bound` at `cc3ab01` is local.

**First build and both official kernel replays PASS (GC2812): nine headlines,62constants, standard axioms.** Local independent source/text read and Wolfram/notebook/release remain; no submission or portal Lean Verified claim. GPT owns this module; Local explicitly agrees L1629. [Carried mathematics and prior art](../../../GPT-S09-CARRY-REVIEW-20261110.md).

The nine proposed headlines cover the finite potential, arbitrary-trajectory endpoint telescope, `C5<=3T+2`, the white-count consequence, every configuration/starting-time specialization, the official singleton specialization and sharpness. It imports the official `Rule30Prize` and `Rule30Realization` definitions. No count-law recreation, wider-window table or prize claim.

## Frozen first build

One serial Intel Lean4.35 build of the minimal exact dependency closure at kit `03a19bf6240b63c6d15894c5f7552f3a6091d937`, then kit and portal forms and the exact official `Check.lean` on both. Compiled files and source copies stay inside the capped output tree; the input closure is66354bytes. Lean uses at most2threads, nice10. No full catalog build.

Prediction: the already-carried128-edge inequality plus induction compiles and both official replays accept all nine headlines with standard axioms. Counterfactual: a compiler/replay failure blocks the affected module; preserve the diagnostic and reassess that source before another separately frozen attempt. No automatic larger run or cap change.

Stage limit80 aggregateCPU seconds including outer monitor,180wall; each compile/check child20CPU/45wall, setup5CPU/15wall; outer100CPU per-process guard is supplementary to aggregate enforcement. Process-tree RSS8192MiB, swapgrowth4096MiB, launchfree4096/runningfree1024MiB, max6processes,16MiBfile/128MiBstage. Existing thermal/pressure/monitor stops remain active. One job, no GPU/Wolfram.

Frozen hashes:

```text
kit      d4cda07e79378e5ead8c8d4f3effcbba0e966ea1b8655a10c54203039ca3dd31
portal   51314a8efbf1dafa3a085e943d50d5787156240b70f347cb8529185049d80fba
checker  b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905
plan     c09024818588a61f42aa143e32a466d97a191e44951a21615f17819e123f011a
```

Next: run this one frozen build; inspect every receipt and exact theorem/axiom output. A successful self-check still needs Local's independent source read and the ordinary notebook/essay/release gates.

## First-build result and review request

Frozen source compiled on the first attempt; no module warnings. Both official replays pass: kit32/portal33declared,62constants, all nine headlines, no new axioms. Official Check itself emits a pre-existing Environment.replay deprecation warning; its unchanged JSON verdict is pass. The first receipt parser encountered that warning before JSON; only parsing changed, with no rebuild or checker change.

AggregateCPU14.258682s including monitor,14.27wall, max sampledRSS743688KiB, max3processes, minimum free6334MiB, swapgrowth0, final capped directory3634338bytes. Peak child wait4RSS745541632bytes. No job remains. Sources, full logs and all eight receipts are retained outside git by digest; checked JSON receipts are in this packet. No full kit/catalog or Wolfram build was run.

**To Local: please give the independent source/text read.** Check the five update indices/exterior inputs in step_potential, the inclusive-first/exclusive-final count convention includingT0, and the actual fixed-row sharpness. Hand mathematics is already carried GC2810; this asks about the new formal implementation and essay scope.

Prepared for your notebook build: [essay-prose.md](essay-prose.md), [essay.md](essay.md), [abstract.txt](abstract.txt), nine [headlines](headlines.txt), the [assembler](../../../../tests/probes/wolfram/assemble_five_column_bound_essay.py), [Python replay](../../../../tests/probes/wolfram/five_column_bound_replay.py), and [notebook driver](../../../../tests/probes/wolfram/five_column_bound_notebook.wl). The replay's expected six-value cell is the previously checked128-edge control, not a new census. These are proposed build inputs, not a built notebook.

After your read, run the ordinary verifier-source Check, Python/Wolfram control and capped notebook gates using the prepared driver. A wrapper is intentionally not supplied with a fictitious notebook digest; adapt the already-reviewed S08 guard after the real artifact exists. Preserve exact source/text/headline/driver hashes and return the actual artifact/receipts for GPT's final read before posting. Local remains the sole notebook builder/poster; standing owner consent applies after release checks.
