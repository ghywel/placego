# Exact channel certificates at layer widths 16 and 20

2026-10-23. GPT, CL587 job 2. **Result: both exact integer certificates PASS, with 2,260 and 12,749 states. The ordinary Core Lean array encoding did not normalize, so no successful kernel timing or four-minute verifier verdict is claimed.** This is a bounded certificate-generation and kernel-cost job, not a new entropy theorem. The existing PROOFS 19 hand squeeze remains separate from the finite arithmetic and the automaton's formal connection to the physical layer.

## Frozen scope before execution

Record searched: `entropy2|Collatz.Wielandt` and the exact PROOFS 19 / RULE30-PRIZE 8.20 and 8.33 / `rule30_squeeze.py` sources. The existing counts are 2,260 states at m=16 and 12,749 at m=20. `entropy2.c` builds the actual reachable subset automaton, comparing complete sorted row sets after hashing, and proposes weights by floating iteration. The new instrument will retain its algorithm, add a bounded allocator wrapper, then check a newly rounded vector and its rational inequality entirely in Python integers. Floats propose data; the resulting inequality does not use a floating tolerance.

Prediction: both state counts match, and a positive integer vector with denominator 10^9 certifies rates near the recorded 0.2130 and 0.1533 bits per visible bit. The certificate contains labelled successors, every weight, the exact numerator/denominator and a reproducible file digest. It counts two labelled edges twice even when they have the same destination; a dead edge contributes zero. The integer ceiling of w_start/min(w) is included for the word-count prefactor.

Independent controls before relying on those results: construct the entire DFA by literal scalar row evolution and Python sets for every m=1..8, comparing every labelled transition to the C output; verify the arithmetic checker on one-state two-loop and one-loop/dead examples, including failing bounds; check 256 actual clamped-right evolutions per requested width for accepted 32-symbol traces. Reject lambda=1 and a deliberately corrupted start weight for each nontrivial certificate. Unexpected check: duplicate successors must contribute multiplicity 2; filtering them as a set would produce a false certificate on the two-loop example.

Caps: one unchanged-source instrument run, m=16 and m=20 only, no wider census or tuning loop. Every C child has CPU240s/wall300s, an instrumented 1 GiB live-heap cap, and retained stdout/stderr; stop the whole job on a failed construction/control. Total data output <=20 MiB. Python memory is small relative to the C pool and checked against a 512 MiB sampled peak; total job wall <=720s. A timeout kills only the owned child, retains partial receipts and is not a pass. No machine-wide process operations.

The local installed Lean is 4.33.1, not the verifier's 4.35.0. If available, the same run emits a Core-only Lean module and checks every chunk of 256 rows with ordinary `by decide`, standard axioms only, CPU100s/wall120s per width. A compile error or cap is retained as an inconclusive timing result, with no automatic patch/retry. This benchmark measures the full local elaboration/kernel-check time for the finite inequality, not a Rule30PrizeKit pass. It cannot alone certify the complete Wolfram notebook under four minutes. No new toolchain/package download is planned.

The formal bridge still needed: Lean must prove that these labelled DFA transitions overapproximate every physical layer trace. A successful integer or Core check of A*w <= lambda*w does not certify that connection. The graph size alone does not estimate the cost of checking full subset transitions, whose start set already has 2^20 layer rows.

Instrument: `tests/probes/channel_certificate_m20.py`. Predictions and source are published before the one bounded execution. Certificate data and raw receipts remain outside git and are sent through the authorized shared store with committed digests; the report receives the complete result afterwards.


## Exact results

The unchanged frozen instrument at `6feeaa9c`, SHA256 `f75a31d0ea3de65bf779769570a9edd874a8cb23518cbe4a6a0cd9ace8dcda4c`, completed in 67.187 s on the Intel host. The original C source SHA256 is `37b8496a4fbddaa90e1d79feb5b95f85ca23801a12e1ba3f3d61207ec163341b`; the allocator-wrapped source is `a548110061602775869fb618f7ec6c4455fb0bf3f7274b8d3c6a357f795ff524`. C generation took 0.126 s and 1.928 s; its guarded live-heap peaks were 5,703,680 and 101,302,272 bytes, both below the cap.

| Quantity | m = 16 | m = 20 |
|---|---:|---:|
| Exact reachable DFA states | 2,260 | 12,749 |
| Labelled nondead edges | 2,897 | 15,677 |
| Rational lambda numerator R | 1,159,107,281 | 1,112,115,481 |
| Rational lambda denominator D | 1,000,000,000 | 1,000,000,000 |
| Minimum positive weight | 9,004,527 | 10,401,158 |
| Start and maximum weight | 92,830,470,123 | 1,202,033,291,690 |
| Minimum exact margin R w_i minus D (A w)_i | 9,222,265,563 | 67,837,652,890 |
| Integer prefactor ceil(w_start/min w) | 10,310 | 115,568 |
| Largest product bit length in the inequality | 67 | 71 |
| Approximate log2(R/D), for description only | 0.213014100947 | 0.153306603903 |

The matrix acts by `(A w)_i = sum of w_j over the two labelled nondead successors`. Every vector entry is a positive integer. The inequalities `D*(A w)_i <= R*w_i` hold at every state, after independently re-reading the dumped JSON and computing both sides directly. This is an exact certificate even though floating power/resolvent iteration proposed the vector. The integer prefactors differ by one from the old report's rounded certificate because this run uses its own rounded vector; the old certificate is not refuted.

For accepted visible-word counts `N_m(n)`, the exact certified bound is

```math
D^n N_m(n)\le C R^n,
\qquad (C_{16},C_{20})=(10310,115568).
```

To avoid relying on decimal logarithms, exact post-run integer comparisons also give `R16^500 < 2^107 D^500` and `R20^500 < 2^77 D^500`, hence coarse rigorous entropy ceilings 0.214 and 0.154 bits per visible bit. In particular do not call the rounded descriptive 0.1533 an upward-rounded rigorous decimal bound.

The path-count proof needs no irreducibility or Perron eigenvector theorem. Start with one path at the root. Induct on n to bound the total endpoint weight of labelled n-step paths by `(R/D)^n*w_start`. Every endpoint has weight at least `min w`; divide by it and round the root/minimum ratio upward. Determinism makes labelled paths and accepted words correspond. Transient states, including the all-layer-rows root, remain included.

All eight independent literal DFA controls passed, with counts `2,2,3,6,13,31,42,56` at m=1 through 8. Every labelled edge matched the independently built Python-set graph. All 512 physical-trace checks passed (256 per requested width); each trace has 32 visible observations, with a sufficient physical light cone. Both exact certificates reject lambda=1 and a corrupted root weight. The one-state two-loop control rejects the false deduplicated-edge interpretation; the one-loop/dead control checks the sentinel. These controls do not independently kernel-verify the large DFA construction.

## Complete data for Cloud

The fixed shared-store bundle is `cited/gpt/cl587-channel-ca4cc38ded5fa750.json`, 1,366,119 bytes, SHA256 **`ca4cc38ded5fa750ab186745f350b84dac6ba3237307385964c7263e616253b6`**. Uploaded once, recovered by stat/read after the old flag client's response-size limit, then byte-verified; the shared manifest has the path/digest/source commit. The transport and TLS verification were unchanged, with only an in-memory extension of the obsolete flags-only path/read guards for this owner-authorized cited artifact. The permanent private client was not changed.

It contains 56 named UTF-8 files, each with its own SHA256 and exact text, including `channel-m16.json`, `channel-m20.json`, generated Lean literals, all retained run receipts/errors, the original C and its guarded wrapper. Load the bundle with JSON, then load `bundle["files"]["channel-m20.json"]["text"]` as JSON. The certificate's fields are `width`, `states`, `start`, `dead`, `numerator`, `denominator`, `successors` and `weights`; state IDs are zero-based, dead is -1, and `successors[i]` has exactly two labelled entries. This supplies the entire matrix and vector, not merely their digest or a floating summary.

| Artifact | Bytes | SHA256 |
|---|---:|---|
| channel-m16.json | 46,794 | `8e7ec5a267c9b67945f8a5ecdaedf9110eb2ae6334dfed9ab826ad88adc1087f` |
| channel-m20.json | 271,136 | `89e15eb018c275be74d30ed470bd723207dfdfb901e27d361e3f745e29ce1605` |
| ChannelM16.lean, failed benchmark encoding | 70,788 | `a8910b5822a5d0430d8857589241f060f323d714b03877b2967c8d54399f2789` |
| ChannelM20.lean, failed benchmark encoding | 403,909 | `b79dbead181e05c829cdf11580ae79790e081200d9cd402fa5a3389ecc27eb61` |

The complete run receipt SHA256 is `b0f4cb40084fe5dc7cf2ac173b1d13f7c54a146d3a8152d53b90a0a51c815878`.

## Kernel timing and the verifier decision

**Not established within four minutes.** The local Lean 4.33.1 benchmark exited 1 at both widths, after 20.651 s and 43.555 s. It did not time out. Ordinary `by decide` did not normalize the generated `chunk.all good = true` propositions to `isTrue` or `isFalse`; the errors show reduction stuck at the Boolean decision/inequality expression. Lean's error recovery printed `sorryAx` dependencies, so these files are expressly **not proofs**. No repair or retry was made. The combined child-process peak RSS was 1,809,399,808 bytes; it includes the failed Lean jobs and is not the C heap measurement.

There are only 2,260 or 12,749 row inequalities, with at most 67- or 71-bit products, split into 9 or 50 chunks of at most 256 rows. That is the finite arithmetic workload. But a failed elaboration's elapsed time is neither a successful kernel runtime nor an upper bound for another encoding. These measurements do not support multiplying 43.555 by a speed factor and declaring a verifier pass. Lean 4.35, Mathlib/kit import, notebook evaluation and verifier replay would add distinct costs even after the reduction issue is resolved.

The larger unresolved interface is DFA soundness. Each abstract state must contain its represented concrete layer rows, the root must contain all `2^m` rows, and for each current row of output label b and each of the four exterior-input pairs, the two-step image must lie in the claimed successor (or a dead edge must have no such current row). The current JSON supplies graph/vector data, not these full subset witnesses or a Lean proof of their construction. C reports mean nonroot subset sizes 334.0 at m16 and 1022.0 at m20; including the root, a literal membership certificate would contain about 0.82 million and 14.08 million row occurrences, respectively. Those are estimates from rounded means, not new exact counts. Verifying that relation may dominate the small CW arithmetic and cannot be priced from the 12,749-node count alone.

Recommended disposition: use the exact data now, but do not schedule an automatic four-minute submission on this evidence. First choose a kernel-normalizing checker representation and a sound layer-to-graph certificate, with the data-to-row/weight linkage explicit, then measure that actual candidate. That is a formalization choice for Cloud, not an automatic new run by GPT. Job 2's requested counts and exact certificates are complete; its timing feasibility answer is honestly unresolved rather than positive.


## Source audit of the failed decision step

2026-10-23, owner-directed follow-up to CL587, GC1704. No benchmark was rerun and the frozen source/data are unchanged. The exact failed messages were compared with the installed Lean 4.33.1 tactic implementation and the [official Lean 4.35.0 decision-tactic source](https://raw.githubusercontent.com/leanprover/lean4/v4.35.0/src/Lean/Elab/Tactic/Decide.lean), particularly `evalDecideCore`, `doElab` and `doKernel` (lines 78–139 in that pinned source).

This identifies the failure phase, not a proved cause of the stuck expression: ordinary `by decide` uses elaborator weak-head reduction before submitting the resulting proof. The retained 4.33 errors come from that normalization check, so the failed timings did **not** measure a kernel attempt at these row propositions. The explicit `decide +kernel` option instead builds the decision proof and submits it through `mkAuxLemma` to the kernel. It is a distinct route from native decision; the implementation expressly rejects combining `+kernel` with `+native`. This is not a recommendation to use `native_decide` or add a trusted-computation axiom.

The versions also differ: 4.33's ordinary branch reduces the Decidable instance to `isTrue`; 4.35's branch reduces the Boolean decision to `true`. Therefore even the failure cannot be transported unchanged to the verifier's version. A source-backed next test for Cloud is the existing encoding under **the pinned 4.35 kit**, with the ordinary path first, or `by decide +kernel` if elaborator reduction remains the issue. First establish one complete checked chunk with standard axioms, then time the actual representation. Neither path has been run by this follow-up; success, memory cost and the four-minute budget remain unknown. The independent layer-to-DFA soundness obligation remains regardless of decision mode. This changes the next formalization diagnostic, not the certificate's mathematical status or the completed finite receipt.
