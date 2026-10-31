# The longest ether-pair episode behind a black right edge — delivery record

Local, 31 October 2026 (L1262–L1271). **Status: built and checked at the verifier's kit e5e1728e (image 14); not
submitted.** GPT passed the content (GC2338). It waits for the owner's explicit yes.

## Statement

For every k ≥ 1, two adjacent depths k, k + 1 behind a black right edge of rule 30 follow the ether of kit PR #69
for at most L(k) = floor(2k/3) + 4 − [k ≡ 0, 2 (mod 6)] consecutive ticks. This holds over every edge code, phase and
onset, and an explicit code with no black bit beyond k + 1 attains it. At the witness's phase class the optimal prefix
is unique.

| Headline | Says |
|---|---|
| `episode_max` | the longest episode is exactly `Lw k` |
| `episode_bound` | no episode has `Lw k + 1` ticks, for every code, phase and onset |
| `wit_episode` | the explicit witness `wit` attains `Lw k` |
| `episode_witness_finite` | a code with no black bit beyond `k + 1` attains it |
| `witness_unique` | at class `(s + q + 2i + 6k) % 8 = 7`, an optimal episode fixes bits `0 .. k + 1` at its onset |

**Status.**
- **The hand proof** is two-party: GC2333.
- **The Lean source:**
  - GPT passed its fidelity and source review: GC2336.
  - It builds on the verifier's kit and passes `Check.lean` (this folder's RUN-SPEC).
  - The release notebook is gated: `KernelChecked`, 483 declarations.
- **Prior art:** GPT compared Phillips 2004 in GC2337.

## Files

| File | sha256 | What it is |
|---|---|---|
| `Rule30Submission.lean` | `bd9ade95…` | the portal form, made from the kit PR #71 form; it imports `Rule30EtherGrounding` (the verifier is at e5e1728e) |
| `essay-prose.md` | pinned in the assembler | the essay to read |
| `essay.md` | `9bdc8480…` | the prose with the source embedded, built into the notebook |
| `abstract.txt` | `2a3e4e4f…` | the abstract parameter (247 words) |
| `kit-pr/` | | the catalog form, opened as [kit PR #71](https://github.com/WolframInstitute/Rule30PrizeKit/pull/71) |
| `RUN-SPEC.md` | | every check, with predictions and receipts |

The notebook `essay.nb` (`a1d48b66…`) is kept outside git, and is in the shared store's `cited/l1271-ether-episode-release.tar.gz`.

## Submission parameters (for the owner's yes)

- **notebook:** the release `essay.nb`, `a1d48b66…`, built at e5e1728e.
- **problem:** `1`. **claim:** `partial`.
- **title:** The longest ether-pair episode behind a black right edge of rule 30.
- **authors:** Gareth Herbert; Claude (Anthropic); GPT (OpenAI).
- **agent:** Claude Code with Claude Opus 5.5.
- **headlines:** `Rule30Submission.episode_max`, `Rule30Submission.episode_bound`, `Rule30Submission.wit_episode`,
  `Rule30Submission.episode_witness_finite`, `Rule30Submission.witness_unique`.
- **abstract:** `abstract.txt`.
- **repository:** https://github.com/WolframInstitute/Rule30PrizeKit/pull/71. The portal asks for the kit pull request
  here; the maintainer then tags the entry Kit Contribution.
- **consent:** `true`, only after the owner's yes.
