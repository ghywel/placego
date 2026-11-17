# Moving walls: exact front speeds 5/19 and 2/9 (NIGHT-TASKS A4) — delivery record

Local, 3 November 2026 (L1420, L1423, L1424, L1426, L1428, L1429). **Status: POSTED, Lean Verified** as
[R30-20261103-87ba7a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-87ba7a) (L1462),
superseding R30-20261103-37281a (L1445). The repaired text scopes the 2/9 law to its alignment and names the ring-orbit
period convention, at the owner's word after GPT's reads (GC2552, GC2557, GC2560). Kit PR
[#115](https://github.com/WolframInstitute/Rule30PrizeKit/pull/115) is open (`Rule30MovingWall`, branch `moving-wall`,
head f35a150).

## Statement

The inserted black edge (background left of 0, black at 0, white right of 0) on two ring backgrounds of Rule 30, in the
namespaces of `Rule30Submission.lean`:

| Headline | Says |
|---|---|
| `Ring57.edge_law` | ring 100100000 (period 57), alignment (0, 0): for t ≥ 300 there is A with the background intact on x ≤ A, a difference in (A, A + 24], and −14 ≤ 19(A + 72) + 5(t − 300) ≤ 22 |
| `Ring63.edge_law` | ring 1010000 (period 63), alignment (0, 4): the same with (A, A + 16] and −20 ≤ 9(A + 55) + 2(t − 300) ≤ 4 |
| `Ring57.edge_law_tail`, `Ring63.edge_law_tail` | the same laws for every rule-30 evolution agreeing with the inserted edge at time 0 on x ≤ 252 (respectively 261) |
| `Ring57.step_sound`, `Ring63.step_sound` | one tick of the anchored window is sound on every rule-30 evolution of the whole line, whatever the cell beyond the window |

**Corollaries for the front F.** 5 ≤ 19(F + 72) + 5(t − 300) ≤ 478 and −11 ≤ 9(F + 55) + 2(t − 300) ≤ 148 (GC2528,
L1427). The front stays within 26 cells (respectively 17) of the lines with slopes −5/19 and −2/9.

## Checks

- **Source.** `Rule30Submission.lean`, 1,504 lines, SHA256 `095e3800341d85e14990390c5b1871f9dcafb42dd62a154dd2f76b36b4a50e14`.
  - `make_moving_wall_submission.py` builds it from the kit module (`a4_kit_module.py`).
  - That module is assembled from the two generated modules, `tests/probes/lean/MovingWall.lean` (the pinned template)
    and `MovingWall63.lean`, made by `a4_lean_module.py` with `--selftest`.
- **The kit's unchanged `Check.lean`.**
  - On the verifier kit 93d98bbe: **pass**, replay OK over 338 constants, six headlines, standard axioms only, no new
    axioms, statements imported.
  - The kit-form module on a local branch from main c42f6e5 also passes, with eight headlines (adding `anchored`).
- **Release notebook.** `moving_wall_notebook.wl` gives **RESULT OK** in 107 s: seven outputs, no message cells, the
  source in an icon, KernelChecked 338, no local paths. Notebook SHA256
  `692cdd6171d78e563df93895006da1244a374d799e23efd370cdf18c644fb40a`.
  - Essay `b5fb854f71fb11f6…`; prose `dfb8e9c38ff5a067…`; abstract 281 words.
  - The picture cell's ranges are [5, 55] and [−11, 20] to t = 1200, so both lower bounds are attained.
- **Direct replays.** `a4_anchor_replay.py`: both anchor identities attain their bounds exactly to t = 4,000.
- **Receipts in the shared store, write-once:** `cited/l1429-moving-wall/a4-receipts-l1429.tar.gz`, 79,245 bytes,
  SHA256 `b21a98107c93f822c1f1182d760425ae75b5ed0012987265f82e9cbec6297395`, readback verified. It holds both Check
  outputs, the notebook and receipts, and the two closure exports.

## Repairs after GPT's packet read (GC2535, L1432)

- The abstract now says the classic front "remains in a bounded window" (not "stands still"). It states alignment (0, 0)
  for 100100000 and that the speed is leftward and asymptotic (289 words).
- The related work adds Phillips (Wolfram Science Conference 2004, growth from finite perturbations of periodic
  backgrounds) and the kit's `Rule30EtherThreeErosion` (Perez Morales and Claude: a finite-state front potential
  inequality, speed at least 2/5). "New here" is marked as a scoped comparison.
- The essay is re-pinned; the release notebook is rebuilt with **RESULT OK** in 102.5 s: seven outputs, KernelChecked
  338, no local paths. Notebook SHA256 `751049eed588fa45c523601dbcb5ae4bb3bff0591b1ed100c7883b75a28fef00`.
- Receipts: `cited/l1429-moving-wall/a4-receipts-l1432.tar.gz`. It supersedes the L1429 archive for the notebook.

## Repair after posting: scope to the alignment (owner, L1450)

The census of L1449 ran the inserted edge at every alignment. On `1010000` it runs at 2/9 at only 91 of 441 alignments,
at 11/81 at 336, and 14 were not yet periodic by t = 3000. Three lines of the posted text read as if 2/9 belonged to
the background. The repair narrows them; the Lean source and its theorems are unchanged.
- The **Description** names both alignments.
- The **abstract** replaces "the speed belongs to the front and the background" with "the law holds for every front
  whose state enters the closure". It says the bound is attained at this alignment, and that finite-window computations
  at other alignments show slower displacement rates (GC2552's wording). It is 296 words.
- The **essay** has the same correction in its closure paragraph. "On 1010000 the inserted edge attains that bound" now
  names the alignment (0, 4). The Scope bullet now carries the census as finite-window lag observations over
  t = 1500 … 3000, with no all-future claim for the slow class (GC2552).
- Pins after GC2552's three finite-window wording repairs: prose `7d765b2a…`, essay `327cae3b…`, abstract `57f080b2…`
  (296 words), source unchanged at `095e3800…`. The rebuilt notebook (nb4) gives **RESULT OK**: seven outputs, no
  message cells, KernelChecked 338, standard axioms, no local paths. Notebook SHA256
  `5847f90ba58f626dcba07d350c31f6d2d0a698bda084ade827c69ef7439fb792`. Receipts:
  `cited/l1450-a4-repair/a4-repair-nb4-receipts.tar.gz` (`7d5f338e…`). nb3 (`c0714438…`) is superseded.
- **Second repair (GC2557):** "temporal period 57" was wrong. 57 is the ring orbit's period in the diagonal
  coordinate j = t − x, while at a fixed column the 100100000 background repeats every 171 ticks: E(0, 3) = 0 but
  E(57, 3) = 1. For 1010000 the two periods coincide (63).
  - The table now gives both periods. The Description, the abstract and the Lean docstrings say "ring orbit of
    period".
  - The fix runs through the template (`MovingWall.lean`, TEMPLATE_SHA re-pinned, selftest True), `MovingWall63.lean`,
    the kit module and the portal source.
  - Declarations and proofs are unchanged. The portal source (now `ed9c69bf…`) also carries L1445's scoped docstring.
  - Checks: the portal form on kit 93d98bbe passes (338 constants, six headlines, no new axioms). The kit module on
    c42f6e5 passes (338 constants, eight headlines).
- Final pins after the second repair: prose `a75bcbef…`, essay `35678a11…`, source `ed9c69bf…`. The notebook (nb5)
  gives **RESULT OK**: seven outputs, no message cells, KernelChecked 338, standard axioms, no local paths. Notebook
  `be8d260adb5efa418fa161c5cfdc1c0e8daf3379519abce960dfa2fb19721ca8`. Receipts, with both Check JSONs:
  `cited/l1450-a4-repair/a4-repair-nb5-receipts.tar.gz` (`305b4342…`). nb4 is superseded.
- Posted as a superseding submission of R30-20261103-37281a only on the owner's word, after GPT's read of the final
  notebook ("After GPT reads nb4", L1460).

## Prior art and credit

- **The method.** The closed-set method with a moving anchor is Cloud's (CL682). GPT supplied the phase repair (GC2394)
  and the start guard (GC2402). GPT carried the source mathematics (GC2528) and proposed the tail transfer (GC2531).
- **The kit.** `Rule30Ether`'s stationary trap (109 wall states, `trap_invariant`).
- **Our own entries.** A1, R30-20261103-3742dc (speed 0 on the classic ether), and A2, R30-20261103-e660e4 (the healing
  bound; attained on 1010000).
- **Search.** `known_find` finds no moving wall or exact nonzero front speed in the kit main, the portal or the open
  PRs (L1426). That is a scoped search, not a priority clearance.
