# The classic ether absorbs a black edge: front speed exactly zero (NIGHT-TASKS A1)

Local, 3 November 2026 (L1344–L1354). **Status: package complete and checked on the M5; not submitted.** The Lean source
is carried by GPT (GC2412, GC2416). The checker passes on the verifier's kit, and the release notebook passes every gate
(RESULT OK). Waiting for GPT's final packet read, and then the owner's word to post.

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
| `Rule30Submission.lean` | `4a2688b0…7018` | the portal form, generated from `tests/probes/lean/EtherEdgeZero.lean` (`47870927…3773`; the first versions `dc9ea874…`/`005f5e3e…` are superseded) |
| `RUN-SPEC.md` | | the check, with its prediction and receipts |
| `essay-prose.md` | `86068b39…f831` | the essay prose (corrected per GC2413 and GC2416) |
| `abstract.txt` | | the abstract parameter (247 words) |

| `essay.md` | `ee7aefd3…7144` | the prose with the source embedded, built into the notebook |
| `essay.nb` | `c50e21cb…0c63` | the release notebook (shared store, `cited/local/l1354-ether-zero-release.tar.gz`; outside git) |

## Submission parameters (for the owner's yes)

- **notebook:** the release `essay.nb`, `c50e21cb…`, built at kit 93d98bbe.
- **problem:** `1`. **claim:** `partial`.
- **title:** The classic ether of rule 30 absorbs a black edge: front speed exactly zero.
- **authors:** Gareth Herbert; Claude (Anthropic); GPT (OpenAI).
- **agent:** Claude Code with Claude Opus 5.5.
- **headlines:** `Rule30Submission.edge_pinned`, `Rule30Submission.edge_pinned_tail`, `Rule30Submission.trap_two_sided`,
  `Rule30Submission.wall_ne_ref_all`.
- **abstract:** `abstract.txt` (247 words).
- **repository:** none yet. A kit pull request needs the owner's word.
- **consent:** `true`, only after the owner's yes.
