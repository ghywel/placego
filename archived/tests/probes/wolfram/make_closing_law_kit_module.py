#!/usr/bin/env python3
"""L1417 (Local, 2026-11-03): build the kit-PR module lean/Ruliology/CellularAutomata/Rule30ClosingLaw.lean from
tests/probes/lean/ClosingLaw.lean (the reviewed cdf38552 source). Run: python3 tests/probes/wolfram/make_closing_law_kit_module.py KITDIR
Same declarations and proofs, in the kit's module form (module / public import / @[expose] public section) and the namespace
Ruliology.CellularAutomata.Rule30ClosingLaw; the #print lines are dropped.
"""
import hashlib
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[3]
src = (root / 'tests/probes/lean/ClosingLaw.lean').read_text()
want = 'cdf38552686f5a5ebc1c5b96d4016da100600b4bf26c76db2e988091d9c68548'
got = hashlib.sha256(src.encode()).hexdigest()
if got != want:
    raise SystemExit('REFUSED: source digest %s, pinned %s' % (got, want))
body = src.split('open Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks\n', 1)[1]
body = body.split('end Ruliology.CellularAutomata.Rule30ClosingLaw', 1)[0]
header = '''module
public import Ruliology.CellularAutomata.Rule30GateClocks

/-!
# The closing law of prefix doublings, for every gate with a quadratic term

In `Rule30GateClocks`, bit `j` of a seed evolves by `x_j(t+1) = x_j(t) xor g j (x_(j-1)(t)) (x_(j-2)(t))`; with
`g j = (· || ·)` this is Rule 30's right edge in the frame moving with it. `prefixExp g x n` is the exponent of the least
period of the first `n` bits, and column `n + 1` doubles when `prefixExp g x (n + 1) = prefixExp g x n + 1`. A gate is
`Quadratic` when its derivative in the newer input, `g true s xor g false s`, depends on `s`; OR is (`quadratic_or`).

* `order_countdown_exact`: for a pair "double, keep" (`s` with period `M = 2 ^ v ≥ 2`, `b` antiperiodic at `M`,
  `h (t + 1) = h t xor g (b t) (s t)` with period `2 M`), a quadratic gate and `order s M + 1 < M`, the order drops by
  exactly one: `order h (2 M) + 1 = order s M`. `order_countdown_gate` is the inequality; the guard excludes the capped
  order `M - 1` of a constant stream.
* `closing_law`: after a doubling at exponent `E` (`q0 = 2 ^ E` is the period before it), `m ≥ 0` pairs `10` and a
  doubling, `m + 1 ≤ q0`, and the next column doubles iff `m + 1 = q0`; `closing_law_or` is the OR case.
* `no_1101011`: `1 (10)^2 1 1` never occurs among the doubling letters; a closing run has length one less than a power
  of two.
* `no_three_at` (`E ≥ 1`), `no_11011_at` (`E ≥ 2`) and `five_letter`: once `prefixExp g x n ≥ 2`, five consecutive
  columns raise the exponent by at most `3`.

Past the `M`-th difference, `h` differs exactly like `s` (`difs_past_gate`): the difference-order mechanism of
`order_countdown`, made an equality. Nothing here concerns the centre column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30ClosingLaw

open Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks
'''
out = header + body.rstrip() + '\n\nend Ruliology.CellularAutomata.Rule30ClosingLaw\n'
dst = pathlib.Path(sys.argv[1]) / 'lean/Ruliology/CellularAutomata/Rule30ClosingLaw.lean'
dst.write_text(out)
print('wrote %s: %d lines, SHA256 %s' % (dst.name, out.count('\n'), hashlib.sha256(out.encode()).hexdigest()))
