# Exactly four left sides through wheel 87,866: follow-up packet

Local, 4 November 2026 (L1512 to L1514). **Status: prepared, not posted, awaiting GPT's carrying read and then the owner's word.** It extends [R30-20261104-309041](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261104-309041), which needs no change. This would be a new portal entry.

| File | SHA256 |
|---|---|
| [`Rule30Submission.lean`](Rule30Submission.lean), portal form | `a34875ab40879d33573bcc476e0ae6f431c2d3f7717695622aa356e7d7a00bea` |
| `essay.md`, assembled | `c3fd02c921f0d1d515952161d34a0f8b8c0128052ce3445cb051d047f2ffed55` |
| [`abstract.txt`](abstract.txt), 246 words | `5417036a91ccaad5c7748c46bf40be26f0a63c2577237b636423d2ea5914bb20` |
| Dry-build notebook, outside git (`cited/l1514-four-left/nb1-receipts.tar.gz`, 103097 bytes, 2b4824c229b99f5d…) | `a8c17164eb7667f9a8940cc6134deafb35f73e00489d3506bbf4456be2c70671` |

Texts: [`title.txt`](title.txt), [`essay-prose.md`](essay-prose.md). Assembler: [`assemble_four_left_essay.py`](../../../../tests/probes/wolfram/assemble_four_left_essay.py). Driver: [`four_left_notebook.wl`](../../../../tests/probes/wolfram/four_left_notebook.wl) (00777aa1ef8ce927…). Generator and replay: [`four_left_sides_leaves.py`](../../../../tests/probes/wolfram/four_left_sides_leaves.py), [`four_left_sides_crosscheck.py`](../../../../tests/probes/wolfram/four_left_sides_crosscheck.py), [output](../../../../tests/probes/wolfram/four_left_sides_crosscheck.out). Hand proof: the PROOFS waiting room, entry L1514.

**Checks so far (M5, Lean 4.35.0, verifier kit 722a0c51).** `Check.lean --claim partial`: pass, nine headlines (`universal_of_strip`, `left_side_classification`, `exactly_four_left_sides`, `on_exactly_one`, `odd_reaches_one_of_four`, `least_period_16`, `seed_classified`, `four_distinct`, `fork_weights`), 272 constants, no new axioms, no build warnings. Notebook: RESULT OK in 21 s, eight outputs, no messages, exact source icon, Abstract cell exact, `KernelChecked` 272, no local paths; the printed digest of the replayed row equals the digest of the literal `A0`.

**Who edits what.** GPT may change the texts and the comments of the Lean, with reasons in the ledger, as on 309041. Local rebuilds the notebook on any change, because the pins above then move. Local alone posts, on the owner's word.

**Kit PR.** Not prepared yet. Once #141 lands, the kit form should import `Rule30UniversalLeftSide` rather than repeat its induction. Until then the portal entry stands alone.

## Questions for GPT

1. **Carrying read:** `extend`, `branch` and `classification`, in particular that the alignment is carried across each fork with one shift, and that `extend` needs both parents aligned (its induction starts at wheel `j0 ≥ 1`).
2. **`side_unique` and `on_exactly_one`:** the shift bookkeeping `s' + 15 s`, and that "exactly one" says what the prose says.
3. **`reaches`:** the uniform threshold, the choice of a tick that is a multiple of 16 and at least 16, and the passage from wheels to numbers.
4. **Essay §6, the cycle-count corollary** (1, 2, 3, 4 with thresholds at 53,209, 58,288, 72,577). It is a hand argument and is not in the Lean. Does it carry, including lifting a periodic point and the need for `n > 400` in "reductions coincide"? If it needs a Lean statement before posting, say so, and I will add it or cut it.
5. **Prior art:** anything on cycle counts of non-invertible T-functions, in particular Anashin's work or 1-Lipschitz maps of the 2-adic integers, that would change how §6 reads. My search found nothing on this map, and the record of what was searched is in L1514.
6. **Scope:** the abstract's and essay's statements against Rowland §5, as you did for 309041; and whether "exactly four" reads correctly given that the cut is where the rows stop.
