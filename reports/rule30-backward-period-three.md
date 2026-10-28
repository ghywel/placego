# Period-three traces in valid root pasts

GC2023, owner question, 28 October 2026. Interpret "instead of period 2" as the moving diagonal x=t through
the root, not a spatially period-three row or a new update rule. Read bits backwards, starting at the root 1.
The proper period-three words are 100,101,110; 111 is the existing constant A control. The first two start
through B, the last through A. Keeping a branch only if its next bit matches is valid ancestry selection;
forcing a cell after reconstructing it would change the problem and is forbidden.

Record searched: GC2016–2022; root_past_tails.py; backward_diagonal_b.py; record_find period-three; G122's
spatial-tail result. No recorded conclusion for these three moving period-three traces. No novelty claim.
Hand observation: a spatial 001 background maps to all 1 then all 0, so its spatial period alone is no
reason to expect a temporal period-three diagonal. The two questions must be separated.

Prediction: at least one of the three prefixes may close through a finite compatibility obstruction;
none is presumed infinite. Counterfactual: survivors at depth 128 are only a finite prefix, and any node,
period or resource cap means inconclusive. Compare complete parent sets at every visited node using the
GC2016 constructor and Local's earlier ray generator plus literal truth-table back-solving. Reproduce
first-generation counts 1,2,5,8 and the period-two closure at 38. Sharing the Row container and least-period
normalization does not make this an independent-worker read.

Frozen source: tests/probes/wolfram/backward_period_three.py, existing two dependency sources. One worker,
128 past steps maximum per new word, 2,000 live branches, 20,000 total generated nodes over the whole stage,
right-tail period 4,096; left window -130..0 is sufficient because inverse extension propagates right to left.
Every right ray is symbolically periodic to infinity. Under run_capped.py: 60 CPU/90 wall seconds, 256 MiB
sampled group RSS, 8 MiB/file, 16 MiB output, launch free+inactive 1024 MiB, ongoing 512 MiB, swap growth
128 MiB. No automatic rerun or widening. Retain exact levels, failed parents and implementation comparisons.
