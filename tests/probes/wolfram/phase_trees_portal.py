#!/usr/bin/env python3
"""L1493 (Local, 2026-11-03): the A6 portal form from the pinned probe tests/probes/lean/PhaseTrees.lean.
Run: python3 tests/probes/wolfram/phase_trees_portal.py
Writes reports/wolfram-agents/submissions/phase-trees/Rule30Submission.lean: namespace Rule30Submission, the statement import
added, the #print lines dropped, and the module docstring's first lines in public wording. Declarations and proofs are unchanged.
"""
import hashlib
import pathlib

root = pathlib.Path(__file__).resolve().parents[3]
src = (root / 'tests/probes/lean/PhaseTrees.lean').read_bytes()
want = '7e2590f14fcdc152'
got = hashlib.sha256(src).hexdigest()
if not got.startswith(want):
    raise SystemExit('REFUSED: probe digest %s, pinned %s' % (got, want))
s = src.decode()


def once(text, old, new):
    assert text.count(old) == 1, old[:50]
    return text.replace(old, new)


s = once(s, 'import Ruliology.CellularAutomata.Rule30FrozenRuler\n',
         'import Ruliology.CellularAutomata.Rule30Prize\nimport Ruliology.CellularAutomata.Rule30FrozenRuler\n')
s = once(s, '# Three phases at bounded depth: G16 to depth 14, P1024 to depth 8, the 480-phase to depth 10 (Local, L1488–L1489)\n',
         '# Three phases at bounded depth: G16 to depth 14, P1024 to depth 8, the 480-phase to depth 10\n')
s = once(s, "L1484's certificate made generic in the depth `k` and the phase `E` (Cloud's top-word tree, CL706; GC2596's soundness and\n"
            'alignment contract), then applied to three phases of the record, each at every alignment:\n',
         'A certificate generic in the depth `k` and the phase `E` (the top-word tree, proposed in the contributors\' record by Claude\n'
         '(Anthropic), with its soundness and alignment contract read by GPT (OpenAI)), applied to three phases of the record, each at\n'
         'every alignment:\n')
s = once(s, 'namespace Ruliology.CellularAutomata.Rule30PhaseTrees\n', 'namespace Rule30Submission\n\nopen Ruliology.CellularAutomata\n')
s = s[:s.index('end Ruliology.CellularAutomata.Rule30PhaseTrees\n')] + 'end Rule30Submission\n'
assert '"' not in s and '\\' not in s, 'the source must embed as a plain string literal'
out = root / 'reports/wolfram-agents/submissions/phase-trees/Rule30Submission.lean'
out.write_text(s)
print('wrote %s: %d lines, SHA256 %s' % (out.name, s.count('\n'), hashlib.sha256(s.encode()).hexdigest()))
