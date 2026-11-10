# S06: complete source and release read

GPT GC2815 (review GC2814), 10 November 2026. **Mathematical and formal-source read PASS. Corrected wording accepted; routine corrected-source Check/nb2/pin gates below complete posting clearance.** Local retains Wolfram and posting. No new Intel Lean run or numerical census was needed: GC2807's independently carried induction and fixed controls remain the baseline.

## The four L1630 questions

1. **Derivative and constants: correct.** Read the complete original 622-line kit module, its generated 1174-line portal form and generator. In `diag`, the histories differ at time `d - 1`; `recon_aff` flips the preceding anti-diagonal, while `recon_local` identifies the earlier cells. The Boolean identity for the changed OR gives the negation in `zs_two`. The zero-depth term is retained, so no boundary constant disappears without an argument. `check_flip` splits the derivative into the part at times at least 2, the time-1 `bcell` and the time-0 previous check. `hc_cons`/`xs_head` kill precisely the first part. Both uses of `xs_not` in `top_succ` sum over `m + 1` variables, hence at least one: constant cancellation is valid. `bsum` has its separate one-variable base. For the coefficient omitting `f 1`, `rsum` at index 0 is the check at n=2, and `tsum` there is B3 in GC2807's notation. Thus the exceptional bases are not silently included in a recurrence that needs another newest variable.
2. **Degree: correct.** `coeff` is the exclusive-or over the subcube below its mask. `anf_expansion` proves that this transform is its own inverse over GF(2), so these are the usual multilinear ANF coefficients. `IsDegree` says that every mask of greater weight has zero coefficient and that a mask of exactly the claimed weight has coefficient one. The odd case uses the full mask; in the even case the only possible greater-weight mask is the full mask, whose coefficient vanishes. The witness `true :: false :: replicate (n - 2) true` has exactly n-1 ones and omits the second free bit, as required. Guards n>=1 and n>=2 are present. This proves two coefficient laws and the exact degree; it does not list every ANF coefficient.
3. **Other phase and credit: correct.** Read the entire `altO`/`otherCheck`/`other_flip`/`other_phase_odd` proof. Here the first free bit is at time 0; `ho_cons` kills all the later terms, leaving only the previous check. The one-variable base and positive-dimensional cancellation are explicit. This carries Local's implementation of the optional one-slice argument in GC2807. The theorem is a top-coefficient statement; odd weight and full degree follow from the already-read cube-parity/ANF definitions. Berzai's alternating physical wall is compared through the masking argument only in the essay, explicitly outside the formal theorem. The comparison is valid: at the black wall ticks the adjacent cell is forced black, so replacing the wall by white changes no OR. The exact phase and width distinction, Berzai's prior assertion, cochon123's code and rule30-open's finite table are credited. General degree invariance under nonlinear triangular substitution is not claimed.
4. **Scope and text: accepted after one clarification.** Replaced “fixes the algebraic normal form” by “proves two ANF coefficient laws and the exact degree” in the comments, abstract, essay, PR body and catalogue row. The corrected abstract remains exactly 200 words. No theorem or proof changed. The survivor claim remains a congruence, using the known `first_check_count`; the Walsh theorem requires n>=2 and has a separate n=1 result. No single-seed, spectral or forgetting claim is included.

## Source identity, checks and actual nb1

The portal generator exactly reproduces the original source and copies the actual main `Rule30FirstChecks` body byte for byte: body SHA256 `6f0a94e8a6449b3492621da6b9b8c9c164de664b35d91b75b66434a83a0590ca`. Its full source equals the GC2807 carrying source, SHA256 `18a01ef281d8dda99d5a4358bcaa1e770b00cdada803a250ba688697b8c9f95b`. New module body SHA256 `9733249222209d4edc5967cad943374fd3a711ed0338e7cd4ef9fc68137a9d0c` is unchanged after the wording edit. The complete kit declaration/proof token stream, removing nested comments and normalizing whitespace, remains SHA256 `5e58f08fe7b86ca481a9a6e99e339318fd223f720c73e04f18904ac34d0326c1`.

Read both original official Check receipts in full: 63 kit /120 portal declarations, 145/243 replayed constants, eleven found/type-matching headlines, standard axioms, no new axioms/reasons. The seven mutation source changes and their compiler rejections were read. Rejection of an unchanged proof after mutation is a regression control, not by itself a refutation of the altered theorem. No redundant mutant run was performed.

The actual main/verifier `Jen` and `Prize` inputs are byte-identical. `ZeroBoundary` differs only by the later appended integer top-bit/time-injectivity section; the reconstruction, affine and locality definitions used here are unchanged. The copied `FirstChecks` supplies the verifier-missing dependency explicitly, rather than importing unavailable statements.

Fetched and verified `cited/local/first-check-degree-nb1-20261110.tar.gz`, 70235 bytes, SHA256 `2d5068a86fdc7be301e625f95f522cdbc398ed5f2081e7ba58fa27f7b2cab652`. Actual nb1 is 214078 bytes, SHA256 `2a904097144b2f81b4fc5f7bd57a14cf69d1cff9f0d56e11728126d31e90ecbf`. Independent serialized-notebook inspection passes exact original source/abstract/title, six evaluated outputs, zero Message cells, the full expected numerical tuple, eleven actual axiom sets and KernelChecked243. Each saved output digest and the unchanged driver match. This is PASS **against the original text**, now superseded. Parser support was extended for Wolfram's named ö and six-hex-digit Unicode escapes; no artifact or builder changed.

The complete assembler, Python replay, Wolfram driver, receipt helper, wrapper and integration patch were read. No Wolfram was run on Intel. The original seven pins and fresh verifier environment pass an independent dry guard replay. The stale wrapper correctly refuses the corrected portal source before network/submission. Outward notebook/source/text privacy checks pass. Local reports an uncapped full `lake build Ruliology` attempt stopped before completion; it carries no validation, and the PR now states this explicitly. Targeted builds and Check receipts are separate successful evidence.

## Routine gates completing clearance

Local may proceed under standing owner consent, without another mathematical or owner approval round, once these gates pass:

1. Regenerate both source forms and essay exactly. Rerun official Check on both comment-only-corrected forms: expect 145/243 constants, eleven headlines and the same standard axioms/declaration counts.
2. Build nb2 with the **unchanged driver**. Require corrected source/abstract/title, six outputs, zero Message cells/$Failed, the unchanged numerical tuple, eleven exact axiom sets and KernelChecked243. Preserve immutable evidence/readback. Old nb1 is superseded.
3. Change exactly four wrapper pins: notebook, portal source, abstract and essay. Title, headlines, driver, helper and wrapper logic remain unchanged. Pass a fresh verifier dry guard and pre-post known_find. Source/proof/driver/verifier changes reopen the affected read.
4. Refresh the local kit branch with the corrected comment/row, post once, open its kit PR and record the actual public outcome. No repost or pre-emptive Lean Verified/Human Verified claim.

Corrected SHA256 pins:

```text
kit       33d6150b37afa804b1822a0cd399905a1a90e4175cec1f8c2cedfa9caf08c13c
portal    b03196f456a96286d891a66383308ecf54b799ea17d5068c48f1da0f8aaf1180
abstract  e98fef66a8c3f99b82aeb4c830a877e7a456daaaa4780583d261c7aeea2df40c
essay     534a8f4ec42635aa9c215d212fa4f3c2fa0dc56a84c4ef71ec6dac6df4fb8fe3
driver    a559d6bce7b9eb155b6f4e8269d23bc8e33cef019b59c1b1a910e5581b513a52
headlines 157bcaaeaf5bcb187fd45b1374d3962a5134deed4fdc6f98e2ad03a27db3d0e6
title     7b6b369f130bca714d9e879acea0f0e6d21e1f5e73830963d30d535f3308e5ae
```

Prior-art carrying read: GC2807, including actual kit lean/equivalents/catalogues, PR77/95 discussions/heads and the pinned primary sources. Fresh COMPLETE known_find 2026-11-10T13:44:43.356828+00:00: kit03a19bf6, portal13:44:35Z, 28 PRs, four additions, all third-party PR261/R30-20261110-f49f6a. Read its actual new guarded statements and discussion/review channels: backward projective inversion and guarded NOR phase synchronization, not the S06 coefficient/degree law or S09 five-column bound. No carrying read of that entire proof, no universal-capture inference and no research excursion.
