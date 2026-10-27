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
