# Shortening a beginning: what may the replacement forget?

GPT, 26 October 2026, GC1892 / MI820. Owner-requested continuation after the morning portal check. Hand reasoning and inspection of the already retained GC1891 output; no new dynamics run. Same zero-wall half-line and black-even-time test as the [conductor review](rule30-tock-conductor-review.md).

**Outcome:** shortening can repair a particular failed check, and an exact hand calculation distinguishes one helpful deletion from a harmful one. Preserving the entire previous trace would forbid such a repair at the same width; preserving just the required ticks permits it. No deletion has been proved to preserve eternal survival, and no all-width reduction follows.

## Two opposite effects of the same operation

Write initial cells from the wall outward; all omitted cells are white. The operation in both examples is deletion of the outermost black cell, at depth 6 (turning it white, not shifting the other cells).

| Original | First failed even update | Shortened beginning | First failed even update |
|---|---:|---|---:|
| 101111 | 6 | 10111 | 8 |
| 110101 | 10 | 11010 | 6 |

All four cases were included in GC1891's 32-case audit; the raw output's SHA-256 was checked before rereading these four values. Nothing was rerun. The first line is a finite example supporting the owner's original compression question: removing a cell can preserve every earlier required tick and repair the next one. The second is an essential countercontrol: removal is not uniformly helpful.

Here is why the effects differ, without relying on those numerical death times. Let the first three tocks be u, v, w. The reviewed reconstruction through depth seven is

    F_1..F_7 = (1, NOT u, u, NOT v, u,
                NOT(u XOR v XOR w), w OR ((NOT u) AND v)).

Consider first-five-cell prefixes of the form (1, NOT u, u, 1, u), so v = 0. They already satisfy the required checks at times 0, 2 and 4. Let the sixth cell be q and the seventh be white. If the next check at time 6 is also to pass, the seventh-cell formula forces w = 0; the sixth-cell formula then forces

    q = NOT u.

This is also sufficient for that one check: the triangular reconstruction realizes the desired full trace through time 6 exactly when the first seven initial cells match. It says nothing about later checks.

- Prefix 10111 has u = 1. The sixth cell must be white. Deleting its black sixth cell repairs time 6.
- Prefix 11010 has u = 0. The sixth cell must be black. Deleting it destroys time 6.

Equivalently, within this specified family the watched colour at time 6 is u XOR q. Both alternatives have identical required earlier ticks; their tock at time 5 changes when q changes. No monotonicity in width or black-cell count is available from this move.

This is a small consequence of the already reviewed table, not a novel universal deletion criterion. The fact that 10111 eventually fails at 8 does not diminish its role as a counterexample to “shortening cannot repair a failure”; it does prevent calling the operation survival-preserving forever.

## A general price for keeping the whole past

The first-arrival / triangular rule in these coordinates is

    a(t) = x(0,t+1) XOR G_t(x(0,1),...,x(0,t)),

where a(t) is the watched cell. Induction on t gives it directly: the farthest input reaches the watched cell along the all-XOR path, and every other input is nearer. This is the established left-permutive reconstruction principle (G130, with the fixed-zero-boundary convention), not a new theorem about Rule 30.

Suppose a finite beginning has support at most W, passes every checked even time before T, and fails at the even time T, with T >= W. Compare alternative beginnings; no change is made to a running automaton.

**If an alternative keeps every watched colour before T unchanged, including the tocks, and repairs time T, it must have a black cell at depth T+1.**

Proof: equal traces at times 0 through T-1 force equal initial cells at depths 1 through T, by successive inversion. The wanted opposite value at T then forces the initial cell at T+1 to flip. It was white because T >= W, so it becomes black. Conversely, adding just that black cell preserves every earlier watched colour and repairs time T. Thus T+1 is the exact minimum support endpoint for this particular full-history-preserving repair. Later failure is not controlled.

**Consequently, any repair that keeps width at most W while preserving the earlier required ticks must change at least one earlier tock.** Its first changed initial cell is at an even depth: if it is at depth j <= W <= T, the first watched difference is at j-1 < T; that cannot be an even checked time. This conclusion only concerns a first difference and a finite horizon. It does not classify which changes succeed.

Last night's 110101 example failed at T = 10 with W = 6. A full-history-preserving repair therefore needs a black cell at depth 11—the very cell the hand argument demanded. In today's first example, shortening 101111 avoids the price by changing the unrequired tock at time 5. It keeps the promise, not the entire old diary.

A process that repeatedly repairs failures this way may demand ever larger support. That observation is not an extinction proof: one has not shown that every repaired start fails again, and other repairs are allowed to rewrite tocks. Arbitrarily long finite successes also do not supply one fixed finite beginning that works forever.

## What the record already knew, and the next question

Read the actual G130 proof and its finite-prefix/finite-support countercontrol, DQ-011's first-arrival statement, and RULE30-PRIZE.md sections 8.88–8.89. The conductor/check split is already present in the old forced-only work, which became a closed main-line approach after its measurements reduced it to the missing language characterization. The old visible-language restrictions cannot simply be imposed on the arbitrary tocks of this auxiliary zero-wall problem. This work neither revives that census nor claims its split is newly discovered.

The new value here is a precise answer to the owner's question about what can be removed or forgotten. A replacement can sometimes be shorter **because it is allowed a different tock history**. Requiring it to match the whole history would rule out the repair before it began.

**Refined question:** can we recognize a part that can be removed while allowing the tocks to change, and prove that any endless sequence of successful ticks would survive that removal? If every sufficiently large hypothetical survivor admitted such a shorter representative, repeated shortening could reach finitely many small cases. The missing step is a uniform, future-valid replacement rule, not more examples of temporary improvement. For a proposed rule, the harmful deletion above is an immediate countercontrol.

No candidate uniform removal rule is established in this block. The next substantive step must specify what a proposed replacement preserves at its boundary and why that suffices for all future checked ticks. Equality of whole histories is unnecessarily strong; mere improvement of a finite death time is too weak. The relevant result is preservation of the eternal-tick property, conditional on the original having it.

Reasoned verdict: the two toy cases are explained exactly, and the general full-history repair cost is an elementary consequence of known reconstruction. Gut verdict: warm on allowing the replacement to forget tocks, cooler on any argument that treats a fixed past as mandatory. No new all-width theorem, computation, proof-status promotion or schedule restart.

Evidence retained: GC1891 source `tests/probes/wolfram/tock_conductor_audit.py`; raw JSON digest `25a71172bdca3ecdb43d901db1911daf94aca4326bb424b821b1d9efd58ec740`. Source search `record_find.py trace triangular` returned G130 and the related earlier prefix/factor distinctions. Legacy startup checks remain incomplete from the previous monitoring-blocked attempts; no startup PASS or new run is claimed.
