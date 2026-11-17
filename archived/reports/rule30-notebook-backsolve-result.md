# GC1986: retained-row extension fails; short prefixes explain why

One owner-authorized Intel execution of GC1985, frozen at commit257283af0ae1e21d5ea1e29fbf1f9c38621f5824. Source SHA25624cef54728a424f4155946333cc564fa0c6e1570e25371300f6f7dc83022fea5; inputs and dependencies match the freeze. No rerun, SAT, sampling, further ancestry level or schedule restart.

## Actual result

All512 width8 target/phase checks matched exhaustive forward enumeration. The guaranteed constructed positive returned16 candidates and recovered its original row. These instrument checks pass.

The fixed00001000@100 witness had zero two-step predecessors: Local's fixed-delay prediction failed. P/Q's saved row also had zero predecessors, so no P99/Q100 witness was obtained; its second-delay stage was not entered. R's saved row had zero predecessors, so no R100 witness was obtained. B_B failed and the short-word gate remains open. The JSON false values mean no extension found for these exact rows, not proof that the words are absent.

No successful target candidate existed to replay independently. I read the actual result, stdout and resource receipt, verified the source/input hashes, and independently checked the two target failures by the following hand obstruction. This is stronger than repeating the same solver: no solver was used.

## The failure can be seen in four cells

Write x1,x2,... for a parent row to the right of the wall, and y for its next row. A wall1 step has

    y1 = 1 XOR (x1 OR x2).

If y1=1, then x1=x2=0. The subsequent equations are

    y2=x3, y3=x3 OR x4, y4=x3 XOR(x4 OR x5).

P/Q's retained row starts1010. Thus y2=0 forces x3=0, y3=1 forces x4=1, and then y4 must be1, contradicting0. It has no predecessor even for the last wall1 update, regardless of all cells farther right.

R's row starts1111. The same equations force x1=x2=0, x3=1 and x4=x5=0. Every last-step parent would therefore start0010. But that prefix cannot follow a wall0 update: output0010 forces its parent's first two bits0, then third bit0 and fourth bit1, which forces output bit4=1 instead of0. Hence R cannot have a two-step predecessor. Its first four cells suffice for this conclusion too.

The optional fixed control begins011010. It likewise has no wall1 predecessor: possible starting pairs01,10,11 exhaust the requirement x1 OR x2=1. Pair11 contradicts y2=1. Pair10 forces x3=0,x4=1, contradicting y4=0. Pair01 forces x3=x4=x5=0,x6=1, contradicting y6=0. Thus its failure is also an exact local incompatibility, not evidence of a broken back-solver.

These are elementary hand consequences awaiting Local's read, not novelty claims. The original source's empty-control handling and top-four pruning were corrected before execution; neither explains away the mathematical failure.

## What changed and the next dependency

The prediction confused two different spaces: an arbitrary starting right row is allowed in the witness search, but only some such rows lie in the image of two earlier clamped updates. A late word can occur in a row whose very early boundary context makes that row impossible to extend backwards. Our full-line possible-pasts discussion did not include this imposed wall restriction.

We now know that directly delaying these retained rows cannot settle P99/P100/R100. We do not know their word membership. Changing just a near-wall prefix is not automatically safe for a late word: its causal cone includes that region. A further test must seek a compatible different row, not rerun these failures. GC1983's proposed small exact membership stage is still an option, but its driver and bounds have not been frozen. Ask Local to read the hand failures and choose whether a justified witness-preserving alteration exists or direct membership is the appropriate next step. No automatic next computation.

The owner's Ouroboros question remains DQ023: repeated output versus changing support; this finite clamped-row obstruction does not decide a natural eternal centre clock.

## Resources and retained evidence

Child exit0,0.36s real and0.35s user+system CPU; supervisor wall1.05s, CPU0.105s. Process maximum RSS from time16,330,752bytes. The child finished before the supervisor's first live sample: sampled group maxima of0 are missing live samples, not zero memory, zero pressure, or measured zero swap growth. Launch free+inactive4869MiB, swap106.25MiB; cleanup found no remaining process. Per-child CPU/file limits and final disk check applied; sampled RSS/pressure stops were armed but saw no live sample. Final pre-receipt output2048bytes. Hard child limits60CPU seconds/4MiB per file; sampled wall120s/RSS256MiB/disk16MiB and stated pressure gates as frozen.

Packet cited/gc1986-backsolve/: result.json, out.txt, time_receipt.txt, launcher-sanitized.json, manifest.json. All uploaded raw with digest receipts and byte-exact readback. Manifest SHA256ce42dac38a3bfec01be711d14443bcde792978136e0f43ddcf4e789f8c02ecbb. Sanitized launcher changes only private input/output paths; original retained locally. Exact per-file digests are in the manifest.


## GC1987: L1033 review adopted; conditional rates do not justify a sampling retry

Local independently carried all three prefix arguments and read the actual result receipt. That closes GC1986's carrying review. L1033 also reports an exact width12 prefix experiment:58.7% one-step and41.4% two-step extendible. Its source/retained enumeration output was not provided in that commit, so those percentages are reported, not independently reproduced here.

Even if correct,41.4% is not the delay probability of our selected late-word witnesses. For a uniformly random full215-cell row Y, let D_n denote that its first n cells have a two-step clamped predecessor. Then D_215 implies D_12. Consequently the width12 rate is an upper bound for the unconditional full-row rate, not an estimate guaranteed to transfer. The required quantity is Pr(D_215 | Y exhibits P or R late), which can differ arbitrarily from Pr(D_12). The retained control/PQ/R rows are also not three independent uniform draws: one is solver-produced and the others selected for rare outputs. The calculation0.59^3 therefore does not calibrate their joint failure. Likewise zero successful delays in a further selected finite sample would not establish systematic unextendibility without a justified conditional model and sufficient sample evidence.

The algebraic distinction is exact: if W_a(w) is the set of right rows exhibiting w at visible age a, and D is the image of two clamped updates, then

    W_a(w) intersects D iff E_(a+1)(w),

interpreted on infinite right rows (or adequate finite cones with compatible extensions). Delaying random witnesses searches the same existential condition; it does not give an independent survival criterion. It may be a useful heuristic with evidence about its conditional success/cost, but such evidence is absent here. No larger/new-seed sampler is agreed.

### Next source requested from Local: direct membership, largest age first

Use GC1983's two already-reviewed encodings, literal replay, retained input bindings and small controls. P=00010101, Q=00101010, R=01010100.

1. Query P100 with both encodings. A clause-checked, physically replayed SAT model proves P100. By E100(P) implies E99(P), and E99(P) iff E100(Q), it also settles P99 and Q100 without those solver calls. Record these as hand-derived conclusions, not separate solver outcomes.
2. Query R100 with both encodings, independently of a P timeout.
3. Only if P100 has no accepted SAT witness, query P99 with both encodings, to locate the boundary or recover Q100. A verified SAT answer in either encoding suffices for existence; an opposite reported UNSAT triggers immediate disagreement review, never silent preference. UNKNOWN does not conflict with SAT.

At most6 external solver calls, one at a time,30s CPU/wall each; stage CPU admission guard210s (self plus completed children, also account after every call), wall300s, sampled group RSS512MiB, disk256MiB and file64MiB; launch free+inactive4096MiB, stop below1024MiB or swap growth256MiB. No bound increase, sampler fallback, wider words or next age. Keep supervisor limitations explicit. All CNFs, solver output, proof traces, resource receipts and positive full cones retained. UNSAT remains solver-reported unless a separately bounded, explicitly included checker actually validates its certificate; source freeze must state which validation is included. No certificate checker is silently added to the solver budget.

Controls include existing tiny exhaustive checks and direct clause/physical validation of the saved P98 and R99 positive fixtures without fresh solver searches. Unexpected check: conditional pruning of P99 must rely on an accepted P100 witness, never on a timeout or an unchecked exit code. On every SAT result verify each clause, every modeled physical cone cell and target word. Preserve a failure checkpoint if interrupted.

Prediction remains P100 andR100 both possible. Counterfactual: exact certified absence at a queried frontier supplies a late death; UNKNOWN says only that the bounded search did not decide it. The earlier exact-row failure did not test or refute this existential prediction.

This is a concrete source request, not a source freeze or launch agreement. Local should prepare the minimal driver; GPT reviews the carrying source/resources before the one execution owner is assigned. The dependency is that driver, not another owner confirmation. Schedules remain paused.
