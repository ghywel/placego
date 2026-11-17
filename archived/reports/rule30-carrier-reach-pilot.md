# One bounded carrier-origin period-sixteen reachability pilot

GC2252,30 October2026. **GC2253 outcome: FAILED in a positive control;
reachability was never attempted. No rerun.** The original freeze below is
retained, including its erroneous proposed rain extension. This changes representation
after the first-tail-merger argument recovered the already-known G13 obstruction.

## Question and discriminating outcome

Can a primitive16 temporal profile have an infinite newer continuation after
an older spatial tail on one of the named white, rain or period8 carrier cycles?
Use Phi(x)_j=x_j XOR(x_(j-1) OR x_(j-2)). A pair(a,b) of16-bit temporal words
has successor(b,c) exactly when Delta c=a OR b cyclically. A forcing of odd
weight has no successor; an even forcing has exactly two, distinguished by
c(0). This follows by summing the Boolean difference and then integrating.

Roots are(0,0), the two rain pairs, and all four spatial/eight temporal phases
of the exact PR48 carrier86,149,101,89, repeated to16ticks. These are actual
infinite older tails. No claim that they exhaust all possible older tails.

**Prediction:** the forward reachable set closes within4096pairs and no
primitive16 pair has an infinite continuation. **Counterfactual:** a surviving
primitive16 pair gives a finite path from a named older cycle through that
pair to a newer cycle, hence a genuine full-line16-return of least period16.
Such a witness would refute the proposed dyadic-background bound. A state,
CPU, memory, pressure or wall stop is inconclusive; no automatic extension.

Breadth-first traversal stops before adding pair4097. If it closes, delete
vertices of outdegree zero and retain a decreasing rank on every deleted
vertex. The surviving vertices are exactly those with infinite forward
continuations, because the graph is finite. A separate scalar recurrence
checks every successor list and every rank inequality. This decides only
the named-tail problem. Even a negative complete answer is not a full
period16 classification, nor an all-clock or centre-column result.

## Searches and controls

Record searched: GC2231's finite-graph pumping distinction, GC2233, PR48's
carried cycle/exit, PR58's exact profile-core source/results and preregistered
ring/SAT scopes; targeted carrier/bridge and transient/homoclinic searches.
Fresh actual kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0 matches the
06:21:50Z complete portal/23open-PR index. Existing q8 core count46 remains
external evidence, not an input or rerun. The author's failed16x32 torus SAT
and finite ring17–24 tests do not test this specified-tail reachability
problem. This is a different algorithm and boundary question, not a retry
with larger limits. No full pair graph or ring census is proposed.

Urías, Salazar-Anaya, Ugalde and Enciso1996, [Traveling patterns in cellular
automata](https://www.researchgate.net/publication/10731741_Traveling_patterns_in_cellular_automata),
is now accessible through the author's linked public full text. Section V,
Lemma5, its proof and the following theorem were read: spatial periodicity
uses a strict end-resolving velocity inequality, and the critical endpoint
is explicitly excluded. Our moving-edge frame is at that endpoint. This
credits the finite-automaton approach and removes an abstract-only reading
limitation; it supplies no period16 exclusion. No novelty claim from search.

Independent controls: all256pairs at q4 compare bit-prefix integration with
scalar decimal Rule30 integration, including cyclic closure; the exact PR48
four-cycle and six-step exit to rain must pass. One altered carrier bit must
fail. Unexpected check: odd forcing(1,0) at q4 must have no cyclic successor,
even though integrating without the final wrap equation would produce one.
Every reached q16 pair is independently checked by the scalar method. A
complete negative certificate is rechecked via strict rank descent, rather
than trusting the peeling counters. No universal conclusion from a cap stop.

## Frozen source and conservative envelope

One execution of [the pilot](../tests/probes/rule30_carrier_reach_pilot.py),
SHA256 bbba28dfd65ea17fdcacb88e3eaf16b8d75060cd89f5092c54d494f414ff6a55.
Syntax parsed, source self-reviewed, not executed before this freeze.
Single Python process/thread, nice10; no subprocesses, GPU, or concurrent
heavy job. This serial graph walk does not benefit from GPU dispatch.

Use unchanged run_capped.py with60CPU seconds for the sole worker,
300wall seconds,768MiB owned-tree RSS,max2processes(time plus Python),
16MiB/file,128MiB/stage,4096MiB launch and3072MiB running free+inactive,
64MiB swap growth, tree tracking and monitor-failure cleanup. Total CPU
budget is120seconds including supervisory work; retain worker, supervisor
and child-helper accounting separately. The runner enforces the worker's
per-process CPU cap, **not an aggregate tree CPU meter**. Any missing
enforcement is reported as such, never inferred from per-process limits.
The fixed4096state work bound is an additional algorithmic stop.

Intel06:56preflight: about6107MiB free+inactive,193.25MiB swap, load2.24;
no competing research computation. pmset reports no thermal/performance
warning and scheduler/speed100. This is warning evidence, not continuous
temperature instrumentation. Refresh headroom before launch; retain the
actual gate and completion thermal/process snapshot. Any warning or pressure
failure redirects work to light reasoning, without a rerun or relaxed cap.
Retain source, controls, graph/ranks or cap frontier, resource and cleanup
receipts outside git with digests. Publish the freeze before running.

## GC2253: the control caught an unjustified extension of the proved endpoint

The sole run at freeze fdc374984fb08ce701bd466b5f128e2c959e56ca stopped
with CHILD_FAILED, assertion line72. All256q4 local-oracle comparisons and
four carrier-cycle checks passed. The four exact PR48 exit triples also
pass; the next proposed triple(234,170,85) is false. Mutation controls,
q16 traversal and rank checks were not reached. No certificate or negative
period16 result exists. Sourcebbba28df remains unchanged, not repaired or rerun.

The source-scope mistake is GPT's: PR48 `carrier_exit` and
`arbitrary_older_context` prove a finite spatial walk ending in(234,170).
Both endpoint profiles are valid for all time; the theorem does **not** say
that the spatial walk continues at clock8. The failed control had added
85,170 without a supporting source equation. This does not invalidate any
of PR48's stated theorems or its earlier carrying review.

### Exact hand diagnosis and the other exit choice

Let D(w)=w XOR ROR_8(w). At the proved endpoint,

    234 OR 170 = EA(hex) = 11101010(binary), of odd weight5.
    D(85) = FF(hex).

The wrap equation therefore fails. For **either** initial bit, integrating
the forcing EA for8ticks complements the next profile; integrating the
same forcing for another8ticks returns it. Its least period is16: its
period divides16 but cannot divide8. This is the standard cyclic parity
rule, applied to this exact endpoint, not evidence of an infinitely
extendible16-clock spacetime.

One step earlier,21 OR234=FF. Both alternating choices170and85 are allowed.
Choosing85 instead gives234 OR85=FF and the genuine continuation

    ...,86,149,154,21,234,85,170,85,170,... .

All later alternating pairs have OR=FF. This is the actual carrier-to-rain
connection, already present up to time phase in PR58's retained q8 witness.
Rotate every temporal word right by5bits: the exit becomes
178,172,212,168,87,170,85,170, matching that witness exactly. The four older
carrier profiles rotate to178,172,43,202 and repeat consistently. Thus the
two choices at the apparent drop have sharply different next clocks: one
joins rain; the other forces a new16-clock column immediately. The finite
PR48 endpoint must not be substituted for the PR58 infinite extension.

These hand implications remain **PROOF-SKETCH** pending independent read;
the standard parity rule and the existing PR58 path are credited as known.
No new simulation or repeat was used for this diagnosis. GC2231's report
and GC2233's reference have been corrected; the ledger has an explicit
amendment preserving the original erroneous attribution.

### Actual enforcement and retained failure

Intel gate07:02:18Z:6266MiB free+inactive,193.25MiB swap; thermal/speed
normal before and after. The worker used0.05user+0.01system seconds,
0.06wall and16924672bytes peak RSS in the time receipt. Outer wall0.54s;
supervisor CPU0.094s. Kernel60workerCPU and16MiB/file limits were checked
by the worker. The run completed before a periodic pressure/tree sample,
so sampled RSS0 means **no sample**, not zero memory. There is no hard
aggregate-CPU receipt; worker/supervisor figures are separate and helper
CPU is not independently itemized. The stage did not approach its budget.
The completion process check found no pilot left running; no cleanup
signal or cap change was needed.

Raw failure/source/inputs/preflight/completion/diagnosis and runner retained
as10payloads31273bytes plus manifest,11verified raw-body uploads:
`cited/gc2253-carrier-control-failure/manifest.json`, SHA256
3707a92031ba6261a26a47cc486c4f45daf3eefbf58f2a214c43cfc0a90e269f.
No automatic corrected run, larger period, state cap or ring census is
queued. Any future stage requires a separately justified freeze, corrected
source-bound controls, and an explicit aggregate-CPU enforcement plan.

Next independent hand lead: return to DQ009's carried two-choice protection
condition and compare its restricted fresh-bit dependence with the later
actual kit degree theorem. First check the specialization and selected-front
hypotheses; an unrestricted-variable degree theorem need not survive the
black-even pins. The alternative is a third-choice protection identity from
the exact recurrence, with the abstract always-protecting policy as a scope
control. No probabilistic condition is promoted to a universal seed theorem.
