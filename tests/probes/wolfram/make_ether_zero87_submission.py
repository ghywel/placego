#!/usr/bin/env python3
"""make_ether_zero87_submission.py (Local, L1370): a DRAFT portal form of A1 with the cutoff 87, for the owner's choice.
Run: python3 tests/probes/wolfram/make_ether_zero87_submission.py A1_PORTAL ROOTED_CATALOG OUT

Mechanical: A1's portal file (reports/wolfram-agents/submissions/ether-zero/Rule30Submission.lean) is kept byte for
byte except its module docstring, which gains one bullet for `edge_pinned_tail87`; the body of
tests/probes/lean/RootedFront.lean (between its `open` line and `end`) is appended before `end Rule30Submission`, with
its internal docstring references removed. The script refuses internal references left in the code.
For the verifier's time limit (L1390), A1's 28 entry checks `set_option maxRecDepth 100000 in theorem entry_.. := by decide`
become `theorem entry_.. := by decide +kernel` (the kernel evaluates directly; statements unchanged; standard axioms):
compile 114 s -> 81 s on the M5.
"""
import sys
a1 = open(sys.argv[1]).read()
rf = open(sys.argv[2]).read().split('\n')
start = rf.index('open Rule30Jen Rule30StripCertificates Rule30Ether Ruliology.CellularAutomata.EtherEdgeZero') + 1
end = rf.index('end Ruliology.CellularAutomata.RootedFront')
body = '\n'.join(rf[start:end])
body = body.replace('(A2\'s backward thresholds, GC2423, for the entry window) ', '(backward thresholds of the recruitment frontier for the entry window) ')
body = body.replace("/-- A2's recruitment step for a half-line state. -/", "/-- The recruitment step of a half-line state (a black newest known cell masks its unknown right neighbour). -/")
body = body.replace('/-! ### A1 with cutoff 87 -/', '/-! ### The inserted edge with cutoff 87 -/')
body = body.replace("pinned (A1's `pinned_of_check_tail`, with the agreement supplied directly). -/", "pinned (`pinned_of_check_tail`, with the agreement supplied directly). -/")
body = body.replace("A1's `edge_pinned_tail` with cutoff `87` in place of `198`", "`edge_pinned_tail` with cutoff `87` in place of `198`")
for bad in ('L13', 'CL6', 'GC2', 'NIGHT', 'placego', 'Lowry', 'PR65', 'T53', 'T54', 'A1', 'A2', 'GPT'):
    assert bad not in body, ('internal reference left', bad, [l for l in body.split('\n') if bad in l][:2])
old_bullet = """* `edge_pinned_tail`: the same for every rule-30 evolution whose initial row agrees with the inserted edge's on
  `x ≤ 198`, whatever its right tail (radius-one locality, `agree_cone`, and the trap's closure under every right input).
"""
new_bullet = old_bullet + """* `edge_pinned_tail87`: the same with `87` in place of `198`. A rooted-front observer follows the leftmost difference
  with a three-valued window of two cells (`HoldsR`), half-line states evolve by the recruitment step (`HoldsH`,
  `succH`), and one tick is sound for every choice of the untrusted expansion thresholds (`tick_sound`); the background
  rows are bit masks, so the kernel runs each entry's check (`check_sound`, `decide +kernel`). A single flipped cell at
  `87` changes the entry window at `(4, 3)` (a computation, not part of this module), so `87` is the least cutoff for
  these entries.
"""
assert old_bullet in a1
a1 = a1.replace(old_bullet, new_bullet, 1)
tail = '\nend Rule30Submission\n'
assert a1.endswith(tail)
import re
a1, nent = re.subn(r'set_option maxRecDepth 100000 in\n(theorem entry_\d_\d : checkEntry [^\n]*) := by decide\n', r'\1 := by decide +kernel\n', a1)
assert nent == 28, nent
out = a1[:-len(tail)] + '\n' + body.rstrip('\n') + '\n' + tail
open(sys.argv[3], 'w').write(out)
print('written', sys.argv[3], len(out.split('\n')), 'lines')
