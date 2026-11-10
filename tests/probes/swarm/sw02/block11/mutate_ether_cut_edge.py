#!/usr/bin/env python3
"""mutate_ether_cut_edge.py: must-fail mutants of the S-11 kit module Rule30EtherCutEdge (L1625).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
check it touches does not carry the claim. Record searched: GC2803 (the carried scope and controls).
E1 129 claimed on the nine-bit cycle; E2 depth 9 instead of 8; E3 no flush ether word within twelve cells (false by
the sharp witness at 55); E4 the thirteen-bit cycle closing after 63 steps; E5 row 204's offset word at phase 3;
E6 the sharp witness at time 54.

Run from the kit's lean/ directory: python3 -I PATH/mutate_ether_cut_edge.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('E1', 'C9.all (fun x => C9.contains (Tm 9 x)) = true ∧ C9.contains 129 = false := by decide +kernel',
     'C9.all (fun x => C9.contains (Tm 9 x)) = true ∧ C9.contains 129 = true := by decide +kernel'),
    ('E2', 'theorem c7cut_depth (N : Nat) : HasDepth (code (c7cut N) (7 * (N : Int) + 6)) 8 16 := by',
     'theorem c7cut_depth (N : Nat) : HasDepth (code (c7cut N) (7 * (N : Int) + 6)) 9 16 := by'),
    ('E3', '    ∃ j, j < 13 ∧ code (cell s) s j ≠ evol c7 a (p - j) := by',
     '    ∃ j, j < 12 ∧ code (cell s) s j ≠ evol c7 a (p - j) := by'),
    ('E4', 'theorem cycle13 : itN (Tm 13) 64 1 = 1 ∧', 'theorem cycle13 : itN (Tm 13) 63 1 = 1 ∧'),
    ('E5', '∀ j, j < 13 → code (cell 204) ((204 : Nat) : Int) (7 + j) = evol c7 2 (1 - j) := by',
     '∀ j, j < 13 → code (cell 204) ((204 : Nat) : Int) (7 + j) = evol c7 3 (1 - j) := by'),
    ('E6', '    ∀ j, j < 12 → code (cell 55) ((55 : Nat) : Int) j = evol c7 3 (4 - j) := by',
     '    ∀ j, j < 12 → code (cell 54) ((54 : Nat) : Int) j = evol c7 3 (4 - j) := by'),
]
os.makedirs(out, exist_ok=True)
lake = os.path.expanduser('~/.elan/bin/lake')
ok = True
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lake, 'env', 'lean', f], capture_output=True, text=True, timeout=600)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    v = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    ok = ok and v == 'REJECTED'
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-', (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
