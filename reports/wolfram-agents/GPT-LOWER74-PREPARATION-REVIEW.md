# Width74 submission preparation: source review before the result

GPT, 2026-10-24; GC1797 / MI730. Reviewed commit `c171c3cd86bb67f64e4cf12ca98c1729e55222ad`, received directly from git while W74 runs. **Mathematical generator architecture carries; two preparation corrections below. Final witness, result digest, generated module/checker and actual notebook outputs remain pending.** This is not a new research-job agreement or a replay.

| Source | SHA256 |
|---|---|
| d6_lower74_submission.py | 704c2e09d31ad4c3ac17ac51eda887c6d7e5864e146c7484b1b8ee480da537ac |
| reused d5_lower_submission.py | 34c9d99a3f33e03d616d949080127389e5136b4823d7f2fa474b1e6662d2c7a3 |
| nb_gate_lower74.py | cbac06ac4bd4dc89d020ab5d87d2e44fce6cf2896d60fe166cf1ae41565b71e0 |
| essay-template.md | ce126e3b2c59e793330752188e68657c207046ad86463345f6aa0f283f6eda7f |

## What carries

D6 replaces only D5's opening imports/comment. Its generated theorem body is exactly D5's for the same witness tuple, verified by pure string comparison. The carrying chain remains: support from `w < 2^74`; all packed even observations below D black; packed observation at D white; `run_toFun` transports them to zrow; `width74_lower` asserts existence and survival, not a maximum. D5's parity bridge requires even D, so an odd candidate cannot silently acquire the claimed theorem. The additional death declaration is separate from the lower-bound headline and is displayed in cell9.

All Python sources parse. The gate's `esc`, `lst`, `expected` and `gate` function ASTs are unchanged from revision4; only witness import and parameterized mutations differ. The 11-cell template still matches those roles and puts KernelCheck last. No retained-output pass is claimed before outputs exist. The gate continues to check plot presence, not its pixel content, and environment counts, not every displayed declaration name. Carry forward GC1795's actual-source/actual-output binding review (including exact names/kinds), or strengthen the gate; do not describe the present count check as complete environment identity. The inherited “five headlines” text is merely stale wording; the executable HEAD list derives from the one-width witness list.

A text-only fixture used the existing width72 witness at width74 and bound130 to compare emitted bodies. It is only a generator fixture, not the unknown width74 census maximizer, not a new physical evaluation and not a result for this submission.

## Corrections before finalizing

1. **The write path must validate the census's completion, not just its digest and one witness.** `pick` checks `complete is True`, scope W74, zero censoring and `maximizer_list_complete is True`; `write` never calls those checks. It instead pins whatever file was selected, checks its maximum against a valid witness, and then emits “complete census,” maximum and count claims. A retained stopped/partial result can contain a perfectly valid witness; the witness proves a lower bound but does not certify those numerical claims. Factor the structural checks into a shared validator called by both paths. Also check nonempty unique in-range maximizer indices, `max_count == len(maximizers)`, the selected retained witness entry, and the expected horizon/coverage fields. Keep the selected supervisor/result review separate: a result digest alone is not a stage PASS. An even D above74 should be explicit for the essay's domain-reduction sentence. This does not threaten the eventual Lean lower theorem; it protects the surrounding numerical account.

2. **Make the ratio range approximate or round outward.** The template says D(W)/W “stays between” two values formatted with nearest two-decimal rounding. That is not guaranteed to enclose the exact values. As an adversarial *hypothetical* allowed even input, D74=146 would give 73/37≈1.972973 but print an upper endpoint1.97. A prediction miss is allowed, so do not rely on the predicted≤140 range to rescue this. Use “approximately …” or floor the lower endpoint and ceil the upper endpoint with exact rational arithmetic. No actual D74 value is inferred by this check.

The prose should also preserve the established distinction between scalar sample checks and d1 chunk checks: each sampled scalar observation was not separately replayed through the kit's chunk evaluator. The long essay paragraph already separates them better than the short Lean header; align that header when filling final provenance.

## Closure condition

The unfilled template review is complete with the above corrections. The remaining work is narrowly named: final census/supervisor evidence, frozen witness and digest, amended generator output, checker JSON, then actual notebook source/output binding. Existing owner authority for submission preparation/builds is not revoked by this review. No duplicate computation, W76, census retry or new research scope is authorized here. W74's accepted attempt remains running as reported in L888 until its retained terminal evidence arrives.
