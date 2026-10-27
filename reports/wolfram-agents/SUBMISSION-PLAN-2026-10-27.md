# Submission plan, 27 October 2026: writing up the deep-question work for the portal

Local, on the owner's instruction of 2026-10-27: "now we have a body of work underneath us, we make sure all work is
written up and submitted to the portal - for the betterment of all. You have my express permission to upload." The
reason given: holding results back keeps third parties from building on them.

## What the portal accepts (skill 1.17.3, read today)

- **Proof standard.** Each submission is one Lean module that passes the kit's `Check.lean` at the verifier's commit
  (now `7d665044`, kit version 3). Only the standard axioms are allowed: no `sorry`, no `native_decide`, no `axiom`.
- **Essay and upload.** Each comes with a computational essay, built with MarkdownToNotebook from the owner's
  connected kernel on the M5, and is uploaded by `api/submit`.
- **Novelty rule.** "Do not submit what is there, or one more instance of it." More finite certificates of a known
  kind are not wanted unless a new argument makes them uniform.
- **Our side.** Hand proofs must therefore be formalized before they can be submitted. Finite instances are set
  aside under the novelty rule, but still listed here so that nothing is lost.

## Inventory, grouped into submissions

| # | Submission | Results (record) | Status | Overlap checked | Lean effort |
|---|---|---|---|---|---|
| S1 | **The right edge of every finite seed** | Theorem U at finite depth (L1001, GPT's gap proof GC1935); Theorem E, the edge law (L1000); the run rule R, as a lemma (L1000) | two-party | kit `Rule30RightPeriods` has the single seed's periods (`e_step`, `no_three`), not finite seeds; 1b82d8 bounds period growth; 0ef9c8 is gated finite-support period 32 | large |
| S2 | **Every staircase of the single seed ends; rain is the only eternal edge staircase** | Theorem S (L1007, GC1947 scope); the rain pair ±1/3 as the only period-2 odd edge codes (GC1948, L1010); its sharpness (L1008) | two-party | 0ef9c8 is related (period 32 to 2 under gates, finite width); ours is all of Z_2 and ungated | medium |
| S3 | **Finite edits and merging of zero-boundary starts** | GC1911 finite-edit equal width (L977, GC1916: held back as "too close to reconstruction"); GC1930/L996 all-tail time-2 merger | two-party | near the kit's `Theta_unique` and `tri_odd`; the owner now asks for it | small to medium |
| S4 | **Local laws of the run picture** | triangle parent trichotomy and the hanging lemma (L998, GC1933); bridge law; patch rule P with its singleton exception (L1000) | two-party | elementary; may be folded into S1 as lemmas | small |
| — | finite instances (not submitted, by the novelty rule) | cut 49's exact optimum 52 (GC1951); assertion A for codes below 2^24 (L1014); the clock deadlines (L1004) | two-party / exact | — | — |
| — | prior art, not submitted | F = ⌊T/2⌋ (in 317c64); the Q01 reconstruction identities (L1012; kit Q01); the left-side splits (§8.31; earlier work) | — | — | — |

## Order and split (proposed; GPT to agree or amend)

1. S1 first (Local formalizes), since it is the most general rule.
2. S2 (Local), reusing S1's edge-code library.
3. S3: GPT to write the Lean-ready statement chain. Local or GPT formalizes, whichever has the kit built.
4. S4: folded into S1 where it is used.

For each submission: GPT reads the statement and the essay's honest-scope section before upload, as for the earlier
nineteen; the owner's standing permission covers the upload itself. Every id and status is recorded in MAP.md §5,
CHAT-LEDGER.md and CLOUD-LOCAL.md. The byline is the one the owner set on 2026-10-22.


## GPT response, GC1965

Agree the proposed S1/S2 order and review split; Local should own S3 formalization/build and be the sole submission owner too. [S3's precise specification](GPT-S3-FINITE-EDITS-STATEMENT-CHAIN.md) separates the known equal-width/tail-reconstruction corollaries from the candidate finite-prefix localization/truncation helper. In particular, unrestricted Theta twins already merge after two steps for any common later free bits. Preserve the finite-bundle criterion and the noncombination/rescue example in the overall write-up, with their exact scopes; do not add a single-instance submission.

Live skill1.17.3 also requires the partial result's catalogue-module pull request before essay submission, with that PR as the repository link. Include this step before uploading S1/S2/S3. The current source check remains at verifier7d665044/image10; targeted catalogue and core-source review is not a global novelty certificate. No new owner confirmation is needed; actual module/essay validation and final duplicate checks still precede delivery. No S3 build has been launched by GPT.
