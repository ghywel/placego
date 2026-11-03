# The universal healing bound for rule 30 (NIGHT-TASKS A2)

Local, 3 November 2026 (L1348–L1350). **Status: theorem kernel-checked and portal form checked on the M5; not submitted.**
Posting waits for GPT's read (statement and prior art) and then the owner's word.

## Statement

For every rule-30 evolution `E` of the whole line (any background orbit, periodic or not) and every rule-30 evolution `G`
agreeing with `E` at time 0 on `x ≤ −1`, let `K(0) = −1` and `K(t + 1) = K(t) + 1` exactly when `E(t, K(t) − t)` is black.
Then `G = E` on every diagonal `x + t ≤ K(t)`. Damage therefore moves left at most at speed one minus the frontier's
climb rate.

| Headline | Says |
|---|---|
| `healing_bound` | agreement on the diagonals `x + t ≤ K(t)` |
| `front_ge` | the leftmost disagreement at time `t` lies at `x ≥ K(t) − t + 1` |
| `K_succ_bounds` | the frontier never falls and climbs at most one diagonal per tick |

## Files

| File | sha256 | What it is |
|---|---|---|
| `Rule30Submission.lean` | `f444ae69…25b8` | the portal form, generated from `tests/probes/lean/HealingBound.lean` (`90118b62…e7d9`) |
| `RUN-SPEC.md` | | the check, with its prediction and receipts |

Still to come: GPT's read, an essay with the per-background rates (a replay of the finite walk), and the notebook.
