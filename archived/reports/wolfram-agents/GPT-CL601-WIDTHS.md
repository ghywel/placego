# Larger channel certificates: design read for CL601

2026-10-23, GPT, GC1708 / MI659. **Design/source review only; no new certificate run, kernel build or timing claim.**

**Recommendation:** use separately checked closure declarations over explicitly named state bitsets, then assemble the existing physical-language and weight proof. This is a refinement of candidate 1. Prefer direct membership checks to rebuilding a growing image accumulator. Keep the current width-12 submission frozen. Do not start with a dense all-images table, a different `Nat` recursor, or an unmeasured width-13 run.

Cloud's cache explanation has strong source support, but the 53-minute observation does not establish that swapping, garbage collection, or one particular cache caused the slowdown. Separate declarations give a real cache-lifetime boundary in the pinned kernel and in the prize-kit replay. They do not guarantee four minutes, one hour, or a particular peak RSS. The unresolved question is implementation performance, not a new mathematical obstruction.

## 1. What is now established, and what was read

CL598's corrections at `1443dcc8` change only the module's explanatory text, not its proof terms; the current source SHA256 is `99806d1c0bca8ab1a651e6737860c75a45b5150cf98b74ee7a229e2e3b07ef4f`. The setup cell and asymptotic/exterior-input/growth corrections are present. L776/L777 and CL599 report submission `R30-20261023-4767e0` Lean Verified on the first automatic attempt. I read the committed records; I did not rerun the submission or independently query its current public status. The JSON itself has no source-digest field: the digest association is in Cloud's dated provenance, corroborated by Local's reported final build, not an embedded JSON binding.

CL600/601 distinguish a completed width-12 check from two incomplete width-14 attempts. Neither timeout is a negative certificate. Widths 14 and 16 remain unverified in the present encoding. The draft wider modules retain width-12 explanatory text; regenerate their descriptions and constants together if they become submissions.

Read: the current checker, `Width14.lean`/`Width16.lean` interfaces, CL598–601, Local L775–777, and the official **Lean v4.35.0** sources listed below. The kernel source was read at that tag, not inferred from current master. The kit replay driver was read at full commit `cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554`. Record searched: `kernel.cache|whnf|chunked|cache limit`; relevant prior result was Cloud's present measurement, not an earlier cache solution. Both prescribed startup checks completed ALL CHECKS PASS, preserving their old blind failures and qualifications.

## 2. The cache question has a source-level answer

`type_checker::state` owns ordinary expression maps for `m_whnf_core`, `m_whnf`, inferred types and unfolding, plus successful/failed definitional-equality pairs. `expr_map` is an unordered map keyed by structural expression equality. In the inspected implementation there is no entry cap or eviction policy on those maps. `whnf` looks up its argument and inserts its result; `whnf_core` inserts results on its non-cheap paths. Easy cases, including an already literal `Nat`, return without a new entry. Thus “every reduced term is retained” is too broad, but a long closed reduction can retain a large number of expression keys, values and the subterms they reference. [Kernel state](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/type_checker.h#L25-L44), [map definition](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/expr_maps.h#L13-L16), [normalization](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/type_checker.cpp#L465-L550), [full whnf](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/type_checker.cpp#L706-L744).

The normal constructor allocates a fresh state; the owning destructor deletes it. `environment::add_theorem` creates a local owning checker for one theorem declaration. Separate theorem declarations therefore discard these checker caches between checks. Stored expressions/proof terms remain in the environment, and the allocator may retain memory, so this is not a promise that the operating system's RSS falls to baseline. Avoid checking many expensive chunks concurrently if peak memory is the concern. [Lifetime](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/type_checker.cpp#L1239-L1260), [declaration checking](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/environment.cpp#L192-L211).

Crucially, `decide +kernel` creates an auxiliary lemma with `mkAuxLemma`; it returns a reference to that lemma. Its own source explains that the checked proof is then reusable. A local `have ... := by decide +kernel` can therefore create a genuine auxiliary declaration too; an ordinary local `let`, `force`, or syntactic split of one decision procedure does not by itself create a cache boundary. Prefer explicitly named chunk theorems so their domains and replay costs are auditable. [Decide implementation](https://github.com/leanprover/lean4/blob/v4.35.0/src/Lean/Elab/Tactic/Decide.lean#L117-L136).

**The verifier preserves this separation.** Its `replayModule` collects the module's constants and calls `env.replay`. Lean's replay traverses dependencies and sends each theorem to `addDeclCore` separately, which reaches the declaration checker above. It does not inline all proved chunk bodies into one giant boolean evaluation. The final proof must actually use the chunk theorems, however: a final `by decide +kernel` of the original whole `check` simply recreates the problem. [Pinned kit driver](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/Check.lean#L100-L125), [Lean replay](https://github.com/leanprover/lean4/blob/v4.35.0/src/Lean/Replay.lean#L59-L101).

I found no user-facing kernel option here that caps those caches. `maxHeartbeats` and `maxRecDepth` bound execution/recursion; they do not evict cache entries. `LEAN_NAT_MAX_SIZE` caps an individual numeral (128 MiB by default), not aggregate retained reductions. `eagerReduce` changes conversion behavior, not cache capacity. Changing `Nat.casesOn` to `Nat.rec` offers no source-backed cache reset; it can change term formation and work, possibly adversely. The cheap internal `whnf_core` paths are not a general user-selectable no-cache evaluator. A bounded-cache kernel patch would require a maintainer-side change and revalidation, outside a portable submission. [Kernel entry point](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/environment.cpp#L287-L295), [numeral limit](https://github.com/leanprover/lean4/blob/v4.35.0/src/kernel/type_checker.cpp#L31-L36).

## 3. Preferred architecture: explicit sets, local closure, opaque proofs

The new certificate should name one bitset `B_i` for each graph state, once. These are **untrusted certificate data** until checked. They need not equal the original BFS sets: any sets with full root coverage and all required transition inclusions suffice for an upper bound. That flexibility is already present in the reviewed `EdgeOK` contract. No generator assertion, hash, or external computation substitutes for the checks.

For H = 2^M, N states, and successor j = succ(i,b), prove these obligations:

1. The root is the full H-bit set (or explicitly prove full root coverage).
2. For every i < N and every row s < H with bit s present in `B_i`, take b = s mod 2. Then j < N and each of the four actual `step2(s,u,v)` lies in `B_j`.
3. The existing weight inequalities, positive minimum and root-weight bound use exactly those successor IDs, including the established dead-sentinel convention.

Obligation 2 naturally detects a false dead edge: a source row with that label would require its successor to be live. It does not need exact image reconstruction or exact BFS equality. An empty source label is permitted.

Split the source-row domain into intervals aligned with 64-bit words. A chunk checks the **actual masked words of `B_i` in its interval**, then iterates their set bits. Reuse the current `pos64`/clear-highest-bit reasoning, but accumulate a Boolean conjunction of four target-membership tests rather than a growing image bitset. A target test can use the accelerated `Nat.land (Nat.shiftRight Bdst outputRow) 1`, with its equivalence to `testBit` proved once. This can still retain shifted big integers within a chunk; it is not a constant-memory claim. Prove the generic chunk-soundness lemma once. Prove coverage of all intervals and all live state IDs separately; an externally supplied list of members without an exhaustiveness proof is insufficient. The last interval must cover H exactly, and source parity is the pre-transition label.

Each closed chunk becomes its own theorem, for example the schematic statement `chunkCheck M Bsrc Bdst0 Bdst1 j0 j1 N lo hi = true`. Its semantic conclusion is restricted to `lo <= s < hi`. Merge semantic conclusions by an ordinary coverage proof, not by reducing the conjunction of every chunk again. Name each bitset once and reference it; use bounded-depth lookup or explicit per-state references, rather than placing repeated large literals and long list traversals inside the member loop.

Balance declarations by work, not just number of states. The root alone has 65,536 rows at width 16, exceeding the entire width-12 row-occurrence count. Dense states need multiple chunks; groups of sparse states can share a declaration. Bound both visited words and set-bit occurrences. Chunk size is an engineering parameter to measure later, not a theorem or a predicted runtime.

**Exact reuse point:** `st_inv` and `visFrom_mem` already take `Bset`, root coverage and `hE` as explicit arguments. `weight_bound` is separate. Extract the body of `Cert.bound` after its `check_sound` call into a semantic theorem accepting those obligations. The existing `Cert.bound` becomes one wrapper; the explicit-set checker becomes another. Trying to fit unrelated local certificates directly into `Cert.Valid.hcheck` would unnecessarily require reconstructing the original whole-run Boolean proof. Retain the ncard finiteness proof and the even-time rebase unchanged.

This does add certificate data. It does not add trusted assumptions. The gain is eliminating the dynamic discovery list and, with the direct-check variant, the long sequence of ever-growing packed image accumulators whose reductions can remain cached. Whether that gain suffices at width 16 remains unmeasured.

## 4. If retaining minimal data is the priority

A checkpointed version of the existing reconstruction is the lower-change alternative: store literal state bitsets needed at a checkpoint, prove a bounded reconstruction block reaches the next specified checkpoint, and compose by a proved transition invariant. Intermediate states can still be reconstructed within a block. Reuse named literals instead of duplicating the whole discovered-state list at every checkpoint; otherwise source size grows with the number of snapshots.

A further optimization can retain only the live frontier of earlier sets that later blocks access. That requires an explicit dependency/liveness argument, and a single global interpretation or consistent reconstruction of removed states. It is not free merely because a set is no longer the current source. I would first implement the simpler explicit-set checker, then compress the data if source size proves to be the limiting resource.

**The tempting no-data split is not automatically effective.** Naming `def checkpoint := computePrefix ...` does not store its evaluated value in the kernel environment. A later declaration may unfold and recompute that prefix with a fresh cache. Likewise a chain of symbolic state definitions derived from parent paths can repeatedly expand the same ancestors. This can trade a memory wall for repeated work. No measured feasibility claim follows without evaluating the dependency graph and the actual conversion path. A symbolic decision-diagram representation is another possible long-term route, but would require a new verified representation/operation layer; it is not a cheap repair to the present module.

## 5. Size arithmetic and the other candidates

These are storage formulas, not newly generated data or measurements. One set needs at most H bits. Two labelled image sets packed together need 2H bits; do not confuse the two.

| Quantity | Width 14 | Width 16 |
|---|---:|---:|
| One full-width state bitset, binary | 2 KiB | 8 KiB |
| All state bitsets, at the reported state counts | 1,882,112 bytes (919 states) | 18,513,920 bytes (2,260 states) |
| Max decimal digits per full-width state literal | 4,933 | 19,729 |
| Max digits across those literals, excluding syntax | 4,533,427 | 44,587,540 |
| Dense row-to-image-bitset table, H by H bits | 32 MiB | 512 MiB |
| Four M-bit successor indices per row | 112 KiB | 512 KiB |

Actual state literals can be shorter; binary payload size is not decimal source size, parsed expression memory, or peak kernel RSS. At width 14 the proposed 4 KiB figure is a **packed pair of images**, not one state set. Sparse row lists or mixed encodings may shrink the payload substantially, but would introduce another decoding/exhaustiveness cost; no compression ratio is assumed here.

**Candidate 2, dense image table:** not my first choice. It replaces repeated arithmetic with a much larger retained object and still leaves aggregate ORs, extraction and closure to prove. At width 16 its nominal 512 MiB single-Nat representation exceeds the pinned kernel's default 128 MiB numeral cap. Splitting the table does not remove the semantic certification or cache problem. A four-successor-index table is vastly smaller than a one-bit-per-destination table, if precomputation later becomes useful, but its outputs must first be kernel-checked against `step2`, in bounded declarations; never trust an external lookup table.

**Candidate 2, bit slicing:** it may reduce arithmetic on many rows, but the scatter from lanes to destination positions is the nontrivial operation. The pinned fast `Nat` operations include shifts and bitwise operations, not a general gather/scatter primitive. A faster row transformer does not itself bound cache growth over the whole run. Treat it as a later local optimization with a proved lane/scatter specification, after establishing a bounded checking unit.

**Candidate 3, cap the cache:** the inspected stock interface has no such setting. No `force`/recursor rewrite supplies it. Do not modify the submitted proof to depend on a locally patched kernel, and do not replace the computation by `native_decide`: the pinned kit's axiom filter explicitly excludes that trust route.

**Candidate 4, width 13:** legitimate smaller target, not a solution to scaling. Its reported 94,993 occurrences are roughly twice width 12, but the failed width-14 extrapolation shows that interpolation cannot guarantee a fit. Keep it as a fallback if the smallest useful partial improvement is the owner's priority, not as the next automatic run.

Ranking: **(1) explicit-set local closure declarations; (2) checkpoint reconstruction if minimum source data outweighs implementation simplicity; (3) local arithmetic/table optimizations inside either design; (4) width 13 as a separate fallback.** A cache-option search has now yielded a negative source answer, not a recommended experimental branch.

## 6. What would justify implementation, without starting it here

The first implementation task should be the generic chunk-soundness and coverage interface, not another full width-14 attempt. A future pilot should include a dense root chunk and a representative nontrivial/dead-edge chunk, and compare final semantic statements against the existing width-12 bridge. Freeze independent literal checks, a dropped-input negative, a label-swap negative, a deliberately missing interval and a false dead edge before running. Preserve all four exterior inputs and the source/target/weight indexing. Check the assembled theorem uses already-proved facts without re-executing the monolithic `check`.

Measure one declaration, then the real kit replay of several declarations: elapsed time, CPU, peak memory, per-chunk work, generated source and object sizes, and whether work is repeated. Declare resource caps and a single pilot decision in advance. Passing a small pilot is not a width-16 receipt; a plateau in RSS is not a proof about all allocations. Parallel checking and the combined notebook/verifier overhead also matter. No prediction of an automatic four-minute pass is justified today.

**Unexpected check:** the prize verifier's replay was inspected, rather than assuming that source-level splitting survives replay. It does use separate declaration checks. **Countercheck to the cache diagnosis:** fresh-literal forcing already occurs in the failing code, so merely adding more forcing does not distinguish the proposed cause. The source supports lifetime-based splitting; it does not prove which part of Cloud's 10.2 GB was responsible.

No new experiment or implementation was run. The source downloads used verified HTTPS; Python's local CA-store failure was handled with the system TLS-verified client, never by disabling verification. The owner's paused heartbeat remains paused. Cloud has the requested design decision, not a new carrying-review queue or a promised runtime.
