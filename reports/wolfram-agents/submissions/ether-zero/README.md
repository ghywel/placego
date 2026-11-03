# The classic ether absorbs a black edge: front speed exactly zero (NIGHT-TASKS A1)

Local, 3 November 2026 (L1344–L1346). **Status: package built and checked on the M5; not submitted.** Posting waits for
GPT's source and prior-art read, and then the owner's standing permission (AGENTS §9; the owner's word for anything
outward).

## Statement

Insert one black cell, with white to its right, into the kit's ether (`Rule30Ether`: spatial period 7, temporal period 4)
at any of its 28 alignments, and evolve by rule 30 on the whole line. From a finite time t1 ≤ 222 on, the ether at and
left of a fixed column x_B is never disturbed, and some cell of the next 13 always differs from it. The leftmost
mismatch is pinned in (x_B, x_B + 13], so its speed is exactly zero.

| Headline | Says |
|---|---|
| `edge_pinned` | the statement above, for every alignment `c0 < 7`, `c1 < 4` |
| `trap_two_sided` | the ether-wall trap on the whole line: ether up to a B3 column plus a wall state stays so for ever |
| `wall_ne_ref_all` | no wall state is the ether's own 13 cells after a B3, so the disturbance never heals |
| `edge_pinned_tail` | the same for every row agreeing with the inserted edge's on x ≤ 198, whatever its right tail |

**Status.**
- The theorem is kernel-checked: standard axioms, on kit 93d98bbe, which equals c42f6e5 for every module used.
- The hand argument for the two-sided step is two-party (L1320 with Cloud's CL681).
- GPT's read of the source passed (GC2412). Its packet read of this version is requested (L1351).
- Prior art: the ether, its wall states and `trap_invariant` are the kit's `Rule30Ether` (a catalog module of the kit's
  first commit); kit PR 65 later added `Lock` and `Rule30EtherWallWitness`. GPT's source comparison (GC2412) found no
  inserted-edge entry or pinning theorem there.

## Files

| File | sha256 | What it is |
|---|---|---|
| `Rule30Submission.lean` | `dc9ea874…99b3` | the portal form, generated from `tests/probes/lean/EtherEdgeZero.lean` (`005f5e3e…dfe2`) |
| `RUN-SPEC.md` | | the check, with its prediction and receipts |
| `essay-prose.md` | draft | the essay (first draft, L1347) |
| `abstract.txt` | draft | the abstract parameter (245 words) |

Still to come: GPT's read of the source and the essay, the release notebook (LeanLink, Local's host) with its gate, and
the submission parameters for the owner's yes.
