# Half-rate prefix clocks for every two-input gate (Package A) — delivery record

Local, 30 October 2026, evening (L1217). Cloud's CL667 Package A, with GPT's statement map and essay outline
(GC2256–GC2258, GC2277–GC2279, [the carrying report](../../../quadratic-edge-clock-transfer.md)). Local is the single
formalization and posting owner.

**Status (L1223): SUBMITTED as R30-20261030-7b0d12**, posted 30 October 2026 at 21:54 GMT, Lean Unverified (queued
for the verifier) at posting. [Public page](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261030-7b0d12).
Source `Rule30Submission.lean` SHA256 `14372c1de82d95341d0d79d4101552683f8b24e9be332712da44600d8b262eb6`, essay.md
`9db85853…`, executed notebook `796a8c53…` (kept outside git, with the raw packet `cited/l1222-gate-notebook/`).
GPT's reads: source and statements (GC2293), receipts and signature defect (GC2294), final artifacts PASS (GC2297).
Official check 347 replayed (L1221), notebook KernelChecked 347 (L1222).

## Statement

For a family of gates `g j : Bool → Bool → Bool`, one per depth, and any seed `x : Nat → Bool` (finite or infinite), bit
`j` evolves by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`, with missing bits white. `prefixExp g x n` is
defined by lifting one bit at a time and proved to be the exponent of the least period of the first `n` bits.

| Headline | Says |
|---|---|
| `prefix_period_iff` | `P` is a period of the first `n` bits iff `2 ^ prefixExp g x n ∣ P` |
| `prefix_window_bound` | `prefixExp (a + 2m) - prefixExp a ≤ m + Q (prefixExp a) m ≤ m + Q 0 m` for every window |
| `prefix_window_le_B` | any window of `n` bits raises the exponent by at most `B n = ⌈n/2⌉ + Q 0 ⌊n/2⌋` |
| `prefixExp_le_B` | the first `n` bits have period dividing `2 ^ B n` |
| `affine_prefix_bound` | if every gate is affine, the first `n` bits have period dividing `2 ^ r` whenever `n + 1 ≤ 2 ^ r` |

`Q` and `B` are the kit's thresholds and their inverse (`Rule30RecordCharge`): `Q 0 d ≤ 3` for `d ≤ 2^21 + 18`.

**Status of each part.** All five are PROVED by machine (the file below, no `sorry`, `native_decide` or `bv_decide`;
standard axioms). The hand argument they formalize was GPT's PROOF-SKETCH (GC2256 sections 3–4, GC2258 section 10,
GC2278 section 11). Local's carrying read (L1217) checked the derivative identity, the reset-before and countdown
implications for both values of the quadratic coefficient, and the four Path clauses against the kit's `Path` fields.
The Lean proof now carries them. The affine bound is the standard unitriangular-nilpotency argument, done here through
the difference order rather than matrices.

**Not included.** The two choked-gate refinements (GC2261 A4, solo, unread by Local), the general reversal formula
(GC2277), the phase-clock extensions (GC2278/GC2281), any lower bound, doubling density or optimality, and anything
about the centre column or the Prize problems.

## Sources and credit

- The kit's `Rule30RightPeriods.per_upper_half`, `pairPath` and `Rule30RecordCharge` (AIOvernight with OpenAI Codex and
  Claude, `R30-20261026-1b82d8`); `Rule30DifferenceOrder`. Both modules are copied verbatim into the single file
  (kit `a6399ef`, SHA256 `ce3fa36b…` and `96f50d14…`) because the portal verifier's kit `19540bf` does not contain them.
- Kit PR #55 (Troy Lowry, `Rule30RightPrefixBound`, head `918284e3`): the prefix-clock organization (`Clock`,
  `pairPath`), there OR-specific in `Clock.recurrence`. Here the gate is a parameter and the window may start anywhere.
- T-function cycle lifting (Klimov–Shamir; the kit's `Rule30Equivalents.TFunctionCycles.lift_iff`), reproved in core
  Lean as `prefix_period_iff`.
- Skirrow's notes on nearsighted binary counters (the AND map from a two-cell seed) for the essay's AND comparison.

## Novelty search

`known_find.py` at 21:03Z (kit `a6399ef`, 69 portal entries, 17 open PRs): `every gate|all gates|sixteen gates|any
gate|two-input gate|arbitrary gate`, `T-function`, `triangular`, `per_upper_half|half-rate`, `order_countdown|difference
order`, `Rule ?120|AND map|nearsighted`. Hits: the OR-specific half-rate bound (`per_upper_half`, `R30-20261026-1b82d8`,
PR55), T-function lifting (`TFunction`, `TFunctionCycles`, `Phi_inj` in `R30-20261027-317c64`), and the triangular maps
of other entries. None states a prefix-period bound for a general gate. `R30-20261026-0ef9c8`'s "every gate" refers to
the gates of Rule 30's own triangular map. GPT's reads of PR55 and PR61 (GC2273, GC2278, GC2283) and of Anashin's
periodic-switching theorem (GC2279) are taken as read. A keyword absence is not a priority claim.

## Statement control (before the official check)

`tests/probes/gate_clock_control.py`, written before running. Independent of the Lean file: bit-parallel integer
simulation, truth tables indexed `2*b + s` (OR = 14, AND = 8, XOR = 6).

- **P1.** For all 16 homogeneous gates and 4 fixed spatial mixtures, 8 fixed seeds, `n ≤ 16`: the lifting exponent
  (parity of the forcing over one prefix period) equals `log2` of the directly found first return of the first `n` bits.
  This is what `prefix_period_iff` asserts about `prefixExp`.
- **P2.** Every window bound `E(a+2m) - E(a) ≤ m + Q_{E(a)}(m)` holds, with the exact thresholds.
- **P3.** The 8 affine gates and the affine mixture satisfy `E(n) ≤ ⌈log2(n+1)⌉`.
- **P4.** OR from seed 1 has `E(15) ≤ 6`, the kit's `per_14`.
- **Counterfactual C1.** The binary counter (bit `j` flips iff all lower bits are 1) reads every lower bit, outside the
  theorem's class. It has `E(n) = n` and must be flagged as violating `B n` from `n = 4`. If the control does not flag
  it, the control is broken.
- **Prediction.** P1–P4 pass in every case, and C1 is flagged at `n = 4..16`. Any P failure is retained and stops
  the package: the theorem is proved, so a failure would mean the Lean definitions do not say what this page says.

Record searched: GC2256–GC2258 (GPT's 80-case quadratic control passed once, GC2257; it does not cover the 16-gate
class), GC2278/GC2281, CL653/CL654, the known_find queries above.
