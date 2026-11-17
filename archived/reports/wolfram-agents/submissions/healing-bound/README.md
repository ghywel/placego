# The universal healing bound for rule 30 (NIGHT-TASKS A2)

Local, 3 November 2026 (L1348–L1355). **Status: POSTED 3 November 2026 at the owner's word (L1390): [R30-20261103-e660e4](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261103-e660e4), Lean Verified (kernel replay passed, standard axioms). Kit PR [#103](https://github.com/WolframInstitute/Rule30PrizeKit/pull/103) (`Rule30HealingBound`). The posted notebook adds one related-work citation (ea30e7) and is sha256 `4e8685f8…`.** The source is
carried (GC2413), the checker passes on kit 93d98bbe (L1350), the rates are replayed (L1352), and the release notebook
gets RESULT OK (L1355; rebuilt after GC2422's prose fixes, L1358). GPT's technical PASS of the first build is
GC2422; its scoped read of the changed artifacts and then the owner's word remain.

## Statement

For every rule-30 evolution `E` of the whole line (any background orbit, periodic or not) and every rule-30 evolution `G`
agreeing with `E` at time 0 on `x ≤ −1`, let `K(0) = −1` and `K(t + 1) = K(t) + 1` exactly when `E(t, K(t) − t)` is black.
Then `G = E` on every diagonal `x + t ≤ K(t)`. This finite-time statement needs no limiting rate.
If `K(t)/t` tends to `rho`, the upper limiting leftward damage speed is at most `1 - rho`.

| Headline | Says |
|---|---|
| `healing_bound` | agreement on the diagonals `x + t ≤ K(t)` |
| `front_ge` | the leftmost disagreement at time `t` lies at `x ≥ K(t) − t + 1` |
| `K_succ_bounds` | the frontier never falls and climbs at most one diagonal per tick |

## Files

| File | sha256 | What it is |
|---|---|---|
| `Rule30Submission.lean` | `c2f3d999…76b3` | the portal form, generated from `tests/probes/lean/HealingBound.lean` (`d2af29c9…f1da`; first versions `f444ae69…`/`90118b62…` superseded, docstrings only) |
| `RUN-SPEC.md` | | the check, with its prediction and receipts |

**Per-background rates (COMPUTED; independent replay, L1352, `tests/probes/healing_rate_replay.py`).** The frontier's
leftward rate is 1/2 for G8, 7/12 for the classic ether, 2/9 for 1010000, 1/2 for 100100000 and 7/17 for 100100000000.
Each is a single value over all phases, and each equals Cloud's corrected `healing_bound.py`. The classic ether gives 7/12
from the kit's own table at all 28 alignments. By `front_ge`, each rate bounds every perturbation's leftward damage speed
on that background. (For the inserted edge in the classic ether the actual speed is 0, by A1.)

| `essay-prose.md` | | the essay (cites Tisseur §3.1 and Bagnoli, Rechtman and Ruffo §2, GC2413) |
| `essay.md` | `9767957e…6fbe` | the prose with the source embedded |
| `abstract.txt` | | the abstract (248 words) |
| `essay.nb` | `8e333966…1293` | the release notebook (shared store, `cited/local/l1358-healing-release.tar.gz`; the first build `89dc5432…` superseded) |

## Submission parameters (for the owner's yes)

- **notebook:** `essay.nb`, `8e333966…`, built at kit 93d98bbe. **problem:** `1`. **claim:** `partial`.
- **title:** The universal healing bound for rule 30.
- **authors:** Gareth Herbert; Claude (Anthropic); GPT (OpenAI). **agent:** Claude Code with Claude Opus 5.5.
- **headlines:** `Rule30Submission.healing_bound`, `Rule30Submission.front_ge`, `Rule30Submission.K_succ_bounds`.
- **abstract:** `abstract.txt`. **repository:** none (a kit pull request needs the owner's word).
- **consent:** `true`, only after the owner's yes.
