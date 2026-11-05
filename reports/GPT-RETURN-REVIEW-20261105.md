# Review of Local and Cloud and suggested continuations

5 November 2026. GC2683, reviewing main `e168c800`: Local L1540–L1547 and Cloud CL743–CL745. The owner reserves GPT for review. This is a carrying read, source inspection and arithmetic on saved outputs, with a convergence-diagnostic repair; no new simulation, build, submission or schedule restart. The GPT subagent's Local source check is a self-check, not another independent worker's read.

## Local

**Three hand results carry, with explicit hypotheses.** In [genealogy §64.5a–c](rule30-genealogy.md), the deviation rise table, triangular fair zone and entry change of measure are **PROVED hand/two-party** in the following scope.

Let `F(y)_k = y_(k+3) XOR (y_(k+4) OR y_(k+5))`. The rise table requires D>=5, agreement at every offset below D and a mismatch at D; it follows by comparing outputs at D−5, D−4 and D−3. Its two exceptional cancellations must remain. The numerical mean 4.25 additionally assumes a law for the encountered colours and damage bits; a half-white background alone does not imply that mean.

The fair-zone identity is `F^s(y)_k = y_(k+3s) XOR G(deeper initial cells)`. For a finite set of offsets `k>=K−3s`, eliminate its distinct fair pivot bits from deepest to shallowest. The output bits are jointly fair and independent of the initial top K. This is **before conditioning** on exit, letter survival, the selected edge or the evolved prefix. It does not justify fair boundary inputs under those conditions.

For the entry formula, choose the two initial letters uniformly, with independent fair cells below. Let U consist of distinct K-cell windows reading letters, closed under the backward dynamics, and let μ_U choose its windows uniformly with fair tail. For `m>=1`,

`e_m = |U| 2^(10−K) 8^m μ_U{F(y) outside U; F^j(y) reads a letter for every 1<=j<=m}`.

Separately, `e_0=|U|2^(10−K)`. The four-to-one lifting count in §64.1 gives density factor 8 per backward step: each lift adds five cells but only two free bits. Closure of U makes the immediately preceding row being outside U sufficient to exclude all earlier entries. The formula concerns **unconditional first entry at age m from this specified initial law**. Its event is not simply the tail of first-disagreement arrival; that replacement is a separate approximation.

**The direct observation stands; its rate interpretation needs correction.** [The saved M5 output](../tests/probes/wall_floor/capture_run.out) records 121,534,152,704 new ticks across four trajectories, zero detected third-lock captures, and 2,609 sampled ticks with agreement depth 145, none deeper. These are not 2,609 certified independent excursions. [The source](../tests/probes/wall_floor/wall_capture2.c) starts each trajectory from letter A and checks exact lock membership from tick 300; closure makes an earlier third-lock entry persistent and hence detectable. Its quiet flag tests period-three letters over twenty million ticks, and its other detector tests long AB alternation. Neither excludes every unknown lock or removes terminal censoring of the quiet test.

A bound such as `−log(0.05)/T` is a **conditional Poisson/constant-hazard conversion**, not a distribution-free consequence of four dependent paths. More fundamentally, finite-age e_m near m=60–87 does not predict twelve entries in this long run. A persistent hazard of that size would do so under an additional model. The observation does not itself refute those finite-age probabilities. Even if the extrapolated `8^m P(arrival>m)` eventually grows impossibly, that rejects the combined extrapolation; it does not isolate whether the fair automaton, the arrival-tail replacement, or both failed.

**Two further evidence repairs.** The resampling retraction is accepted: ancestor collapse invalidates the claimed end near K/3.4. Ancestor counts alone do not certify accuracy before a chosen earlier cutoff. The free-graph program labels any exhausted iteration budget “a cycle”; its saved 50 rounds on a much larger graph certify an unresolved long-path calculation, not a closed walk. The diagnostic is corrected, while historical output is preserved. A repeated-state path or SCC certificate would settle the graph claim. Competing periodic patches remain interesting; matching their branch offsets to plateaus is not yet a cell-by-cell identification.

**Warmest continuation for Local: explain the obstruction at 145 using the successful route.** Recover one existing specimen behind [arrive_track.py](../tests/probes/wall_floor/arrive_track.py), whose `arrive145.txt` input is not committed, and compare it with the already verified entry witness. Align the six strip phases and inspect six ticks around offsets 119–150, retaining every cell in the dependency cones. The saved witness crosses 143→148; it need not visit exactly 145. Aim for one explicit local/history condition obeyed by the plateau route and violated by the witness, then certify that condition on the actual rows. Prediction: an inherited competing branch explains the failed extension. Counterfactual: the inspected prefixes coincide, forcing the distinction deeper or earlier. First executable step is recovery and digesting of the existing specimen, not another rare-event run. If it is lost, use the saved top-word constraints to seek a finite compatible witness and distinguish that reconstruction from a recovered observation.

## Cloud

**The finite bookkeeping carries; the measurements remain useful.** Cloud's CL743 read completes the two-party proof of `B−A=H_T−H_0` and the corresponding finite heal/stay identity, with positive denominators. [edge_windows.py](../tests/probes/wolfram/edge_windows.py) uses the matching transition convention. Identifying the damaged row's terminal strip and phase after settling is the correct comparison: the fourth initial strip settles on its parent `A0.53207.165748`, phase zero. The four selected strip runs weaken the proposed common excess hazard. They do not establish a common probability law, absence of strip dependence, or an asymptotic speed equality.

**“One walk per strip” is not established by these outputs.** [The seed](../tests/probes/wolfram/edge_windows.out) and [damaged A0](../tests/probes/wolfram/edge_strip_A0r.out) have equal printed aggregates in several middle windows; aggregates alone cannot prove tickwise equality. In the claimed matching 800,000–894,235 window, both durations are 123,967 but their healing fractions are 0.412279 and 0.412327, with different jump statistics too. That window cannot be an identical tickwise walk. Earlier finite alignment observations and guarded packet certificates in atlas §20 remain valid in their original scope.

The same saved durations expose a more specific pattern. With Δ equal to damaged-row minus seed cumulative time at window exits:

| Window just completed | Δ | Change in Δ |
|---|---:|---:|
| 400,000–499,999 | −168 | 0 |
| 500,000–599,999 | −200 | −32 |
| 600,000–699,999 | 152 | 352 |
| 700,000–799,999 | 216 | 64 |
| 800,000–894,235 | 216 | 0 |

All these offsets are 24 modulo 32, consistent with the damaged reference's phase 8; the three nonzero changes are −1, +11 and +2 whole periods. This is exact arithmetic on the saved finite durations, **not a proof of synchronization or quantization at every intermediate crossing**.

**The reset explanation needs the actual-parent guard.** At child k the rule uses actual parents `a_(k−2),a_(k−1)`. The known reset applies when they equal the reference parents and `a_(k−1)=C_(k−1)=1`; then the child's old error is erased. A black reference parent alone does not suffice. For example, triples `(C_(k−2),C_(k−1),C_k)=(0,1,0)` and `(a_(k−2),a_(k−1),a_k)=(0,0,0)` give next child bits 1 and 0. This is a direct rule substitution illustrating the missing guard, not a claim that this triple occurs in the reported A0 run. Permanent white-parent pinning likewise requires aligned earlier parents and a fixed reference phase. On odd initial rows wheel 2 becomes permanently white from tick 2, not tick 1 (`1→7→19` is the small boundary case).

**Hazard scope.** The three fair-row samples do not show exact memorylessness from n=2. Their n=7 values are 0.4902, 0.5017 and 0.5128, contradicting the stated ±0.002 range. Phase bins use n>=2, not all stalls; final bins pool n>=12 and preceding jumps d>=7. The new jump-four/five/six implications are Cloud-reported exhaustive computations; the inline enumerator is not supplied for a carrying source read, so this review does not independently certify them. Preserve a replayable enumerator or a short hand proof before using them as proof premises. The explicitly withdrawn smoke-test sentence is excluded from this review's evidence.

**Warmest continuation for Cloud: explain one loss and recovery of phase-aligned front agreement.** Use this existing seed/A0 pair, first checking actual alignment rather than assuming it from aggregates. Locate a concrete divergence in the 500,000–600,000 interval and a subsequent alignment, if present, and follow the pairwise difference together with each row's difference from the common phase-aligned strip. Which actual parent ceases to agree, and what guarded reset restores agreement? The target is one finite transfer statement accounting for a whole-period clock slip, or a counterexample to that picture. Prediction: agreement recovers only after a specific parent-aligned reset. Counterfactual: equal later durations conceal continuing distinct walks. This would connect the observed clock offsets to the existing §20 packet/phase mathematics without another speed or hazard census.

## Handover

Validation: ledger and document-link checks pass; `git diff --check` passes; the changed C source passes `clang -fsyntax-only`. The repaired diagnostic was source-reviewed without rerunning the graph.

The current kit/portal receipt remains the preceding complete GC2682 check at 12:50:50 UTC, kit `a5c28dbb537c92373be689b0304aed293377229a`. No new novelty or submission clearance is claimed. This review builds on the named record and sources, rather than proposing an additional theorem or reopening a closed census. Local and Cloud own any continuations the owner chooses; GPT has no run queued and both schedules remain paused.

My own pull: for Local, the physical distinction between the plateau and witness routes; for Cloud, a guarded explanation of a whole-period clock slip. Both are warmer than another bulk rate estimate.
