#!/usr/bin/env python3
"""L1411 (Local, 2026-11-03): build the portal form of NIGHT-TASKS A3 from tests/probes/lean/ClosingLaw.lean.
Run: python3 tests/probes/wolfram/make_closing_law_submission.py
Writes reports/wolfram-agents/submissions/closing-law/Rule30Submission.lean: the same declarations and proofs, in namespace
Rule30Submission, importing the kit's statement module and Rule30GateClocks, with the #print lines dropped.
"""
import hashlib
import pathlib

root = pathlib.Path(__file__).resolve().parents[3]
src = (root / 'tests/probes/lean/ClosingLaw.lean').read_text()
body = src.split('open Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks\n', 1)[1]
body = body.split('end Ruliology.CellularAutomata.Rule30ClosingLaw', 1)[0]
header = '''import Ruliology.CellularAutomata.Rule30Prize
import Ruliology.CellularAutomata.Rule30GateClocks

/-!
# The closing law of prefix doublings, for every gate with a quadratic term

The kit's gate clocks (`Rule30GateClocks`) evolve bit `j` by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`; with
`g j = (· || ·)` this is Rule 30's right edge in the frame moving with it. `prefixExp g x n` is the exponent of the least
period of the first `n` bits, and the column `n + 1` doubles when `prefixExp g x (n + 1) = prefixExp g x n + 1`.
A gate is `Quadratic` when its derivative in the newer input, `g true s xor g false s`, depends on `s`; OR is quadratic
(`quadratic_or`).

* `order_countdown_exact`: if `s` has period `M = 2 ^ v ≥ 2`, `b` is antiperiodic at `M`,
  `h (t + 1) = h t xor g (b t) (s t)` with `g` quadratic, `h` has period `2 M` and `order s M + 1 < M`, then
  `order h (2 M) + 1 = order s M`. The kit's `order_countdown_gate` gives `≤`; this is the equality.
* `closing_law`: after a doubling at exponent `E` (period `q0 = 2 ^ E`), `m ≥ 0` pairs `10` and a doubling,
  `m + 1 ≤ q0`, and the next column doubles iff `m + 1 = q0`. Every quadratic gate family and every seed;
  `closing_law_or` is the OR case.
* `no_1101011`: the doubling word `1 (10)^2 1 1` never occurs, since `3` is not a power of two. In general a closing
  run has length one less than a power of two.
* `no_three_at` (`E ≥ 1`), `no_11011_at` (`E ≥ 2`; `11011` closes with `1` only when `q0 = 2`) and `five_letter`:
  once `prefixExp g x n ≥ 2`, five consecutive columns raise the exponent by at most `3`.

The countdown is the difference-order argument behind the kit's `order_countdown`: past the `M`-th difference,
`h` differs exactly like `s`. Nothing here concerns the centre column of the single-cell pattern or the Prize problems
themselves.
-/

namespace Rule30Submission

open Ruliology.CellularAutomata Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks
'''
out = header + body.rstrip() + '\n\nend Rule30Submission\n'
dst = root / 'reports/wolfram-agents/submissions/closing-law/Rule30Submission.lean'
dst.write_text(out)
print('wrote %s, %d lines, SHA256 %s' % (dst.relative_to(root), out.count('\n'), hashlib.sha256(out.encode()).hexdigest()))
