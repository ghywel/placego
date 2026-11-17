#!/usr/bin/env python3
"""mutate_ternary_waves.py: must-fail mutants of the S-22 module Rule30TernaryWaves (Cloud's K-04 with K-09a).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
statement or data it touches does not carry the claim. Record searched: GPT's GC2830/GC2846 (period 12) and GC2848
(period 15) literal tile reviews; Cloud's CL768/CL775; the kit's Rule30MovingWaves and Rule30RingOrbits.
Data and parameters: M1 one bit of the new period-12 tile flipped; M2 one bit of a period-15 tile flipped;
M3 tile length 33 at period 12; M4 period 14 for the 31-cell tiles. Decoders: M5 the period-12 reader with tiles 0
and 1 swapped; M6 the period-15 decoder read at offset 7 instead of 6.

Run from the kit's lean/ directory: python3 -I PATH/mutate_ternary_waves.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "2986,1131,2644,3674,2406,2389,1493,1327,2864,3240,2728,2772,", "2986,1131,2644,3674,2406,2389,1493,1326,2864,3240,2728,2772,"),
    ('M2', "[5461,23930,21125,13126,10949,10917,21926,10837,30069,2890,3277,2731,",
     "[5461,23930,21125,13126,10949,10917,21926,10837,30069,2890,3276,2731,"),
    ('M3', "def tiles12 : Tiles := { L := 34, P := 12, profiles := profiles12 }",
     "def tiles12 : Tiles := { L := 33, P := 12, profiles := profiles12 }"),
    ('M4', "def tiles15 : Tiles := { L := 31, P := 15, profiles := profiles15 }",
     "def tiles15 : Tiles := { L := 31, P := 14, profiles := profiles15 }"),
    ('M5', "def read12 (u v : Bool) : Fin 3 := if u then 2 else if v then 0 else 1",
     "def read12 (u v : Bool) : Fin 3 := if u then 2 else if v then 1 else 0"),
    ('M6', "theorem reads15 : ∀ a : Fin 3, read15 (profile tiles15 a 6 0) (profile tiles15 a 23 0) = a := by",
     "theorem reads15 : ∀ a : Fin 3, read15 (profile tiles15 a 7 0) (profile tiles15 a 23 0) = a := by"),
]
os.makedirs(out, exist_ok=True)
lake = os.path.expanduser('~/.elan/bin/lake')
ok = True
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lake, 'env', 'lean', f], capture_output=True, text=True, timeout=900)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    v = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    ok = ok and v == 'REJECTED'
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-',
          (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
