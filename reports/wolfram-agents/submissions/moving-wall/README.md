# Moving walls: exact front speeds 5/19 and 2/9 (NIGHT-TASKS A4) — delivery record

Local, 3 November 2026 (L1420, L1423, L1424, L1426, L1428, L1429). **Status: PREPARED, not posted.** Posting, and any
kit PR, wait for GPT's packet read and the owner's word.

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

## Prior art and credit

- **The method.** The closed-set method with a moving anchor is Cloud's (CL682). GPT supplied the phase repair (GC2394)
  and the start guard (GC2402). GPT carried the source mathematics (GC2528) and proposed the tail transfer (GC2531).
- **The kit.** `Rule30Ether`'s stationary trap (109 wall states, `trap_invariant`).
- **Our own entries.** A1, R30-20261103-3742dc (speed 0 on the classic ether), and A2, R30-20261103-e660e4 (the healing
  bound; attained on 1010000).
- **Search.** `known_find` finds no moving wall or exact nonzero front speed in the kit main, the portal or the open
  PRs (L1426). That is a scoped search, not a priority clearance.
