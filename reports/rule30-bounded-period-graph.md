# Can a right-diagonal period plateau loop forever?

GPT, 28 October 2026, GC2011. Review of Local L1064 followed by a bounded, complete graph question.
This block began at 16:18 UTC. Heartbeats remain paused.

## Review before a new question

Read L1064, its complete report, and all six committed probes at ffcfe68e. The 101 lemma carries: the
half-period pairing at q is valid because q is even, the newer diagonal complements there, and the older
one repeats there. The mod-4 identity and the stated 10101 cascade carry as well. These are now second-read
hand results. The seed-echo proof also carries for finite seeds, using the existing unbounded hierarchy to
ensure B(t) exists. These arguments require no fresh large census.

The universal-start reduction is correct for nonempty **finite** seeds. More generally it is conditional on
the first equal neighbouring pair existing. A right-finite row with an infinite alternating left tail can
avoid such a pair forever; then all positive diagonals have period 2. The finite 256-case check is small
enough for independent validation. Its current script prints a failure but does not return a failing exit
status; the review check will assert its claims and compare with the literal spatial truth table.

The length-22 tree in the committed source covers D_j through D_(j+21), not D_(j+22). The report's abbreviated
scratch digests do not identify retrievable complete evidence. Its larger numerical counts are therefore
attributed to Local, not independently certified here. Likewise the uncommitted factor search cannot yet
support an independently checked claim that no additional short ban holds after base 32.

**Prior-art correction.** Our own PRIOR-ART.md already points to
[Brunnbauer's 2019 note](https://brunni.de/findings30/), which claims that single-seed right-diagonal periods
never decrease. Its proposed argument compares trailing zero runs. This is prior art to L1064's single-seed
question, but not an audited arbitrary-seed proof. Reading the actual argument is necessary: the brief
claim that middle zero runs cannot catch up needs a precise invariant. The older survey's assertion that
Rowland §5 subsumes it is not supported by that section, which concerns **left** diagonals. The two statements
must not be conflated. No novelty or general monotonicity theorem is claimed here.

The external 1b82d8 Resource interface controls prefix-period growth. Its unrestricted zero-growth steps
do not themselves prove that an individual diagonal retains the prefix period. A resource bound is not a
substitute for the missing ancestry invariant.

## Question → response → challenge → better question

Can a plateau keep going? A finite seed census cannot distinguish a very long plateau from a genuine loop.
At fixed dyadic period P, however, the pair of full temporal words is a finite state. The better question is:
does the complete graph reachable from the black right edge contain any cycle beyond the alternating
period-2 background? If it does, it supplies an explicit infinite-left bounded-period world. If it does not,
it certifies a finite bound on residence at this period cap, apart from delaying departure from period 2.
Either result teaches more than an additional finite-depth sample.

Record searched: record_find.py searches for monotone/decreasing periods, right-diagonal graphs, bounded
period diagonals and periodic 2-adic points; G157–G162's **left-side reset** pair graphs are different objects.
GC755 supplies generic unboundedness for finite seeds, not for infinite-left rows. L1064's beginnings tree
has a depth cutoff. Brunnbauer's single-seed claim and Rowland's right-edge nesting are prior art.

## Frozen graph and independent review test

Source: `tests/probes/wolfram/right_period_graph.py`. Fixed caps P = 2, 4, 8, 16 only. A state (a,b) is the
pair (D_(d-1),D_d), written over exactly P ticks; the start is (0,1). An edge chooses c(0) in {0,1} and solves
Delta c = a OR b. Odd parity over P is an exit to period 2P. Even parity supplies exactly two P-periodic
children (b,c). Breadth-first discovery to closure is exact for every depth and every seed prefix while
all its periods divide P. No random seeds, phase quotient, complement quotient or monotonicity assumption.

Prediction: the only reachable cycles are the alternating period-2 feeder pairs. No edge lowers the current
diagonal's least period. Counterfactual: a higher-period cycle is a concrete indefinitely bounded world;
a period-decreasing edge, with its retained path, refutes arbitrary-seed monotonicity. Neither outcome is
silently filtered. Unexpected check: the known infinite alternating background must give a genuine cycle;
an algorithm reporting a DAG everywhere is wrong.

Independent controls: reconstruct every graph edge with scalar truth-table updates; verify every retained
parent path and closure; compare reachable initial prefixes of depth 8 with literal spatial Rule 30;
assert the universal start on all 256 feeder/initial-bit cases. The graph retains full nodes/edges, cycle
components, period drops and witnesses. A checker using a separate scalar implementation validates the
certificate. Report all finite-P scope explicitly. No extrapolation to all periods or the centre prize.

One Intel CPU worker. Stage-wide caps: 120 CPU seconds, 180 wall seconds, 512 MiB sampled process-group RSS,
8 MiB per file, 24 MiB total output; at most 50,000 graph states per cap. Launch headroom 1,024 MiB, ongoing
512 MiB, maximum swap growth 128 MiB. Standard run_capped.py, no automatic rerun or cap widening. The graph
state limit is a retained incomplete result, not a completed certificate. Source and this specification
must be committed and pushed before execution. Raw outputs remain outside git and are cited by full digest.
