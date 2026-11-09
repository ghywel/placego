#!/usr/bin/env python3
"""mutate_trap_words.py (Local, 9 November 2026): mutants of the portal form of `Rule30GateTrapWords`, each of which
must be REJECTED by Lean (any error). Usage: python3 mutate_trap_words.py SOURCE KIT_REPO OUTDIR [MUTANT ...]

M1 drop one window from a middle layer of 3353 (step check fails)
M2 claim the allowed word 3355 with the layers of 3353 (the last letter differs, the step check fails)
M3 start from the white windows instead of the black ones (start check fails)
M4 flip the first column-17 value in the path witness of 353. Not a must-fail mutant after all: column 17 reaches
   column 1 only after about eight double steps, and this path still reads 353 (first run: ACCEPTED, kept as found)
M4a flip column 1 of the start window of the path of 353 (its first sample is then white: minimal_paths fails)
M4b replace the start window of the path of 553 by 0, which is not in the trap (minimal_paths fails)
M5 remove the final empty layer of 333 (the check no longer types: readCheck runs out of layers)
M6 drop one window from the shared first layer lay1 (start check fails)
M7 shift every code of one layer of 5533 by one bit (step check fails)
"""
import re
import subprocess
import sys
import time
from pathlib import Path

src = Path(sys.argv[1]).read_text()
KIT = Path(sys.argv[2])
OUT = Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)


def layer_span(name):
    m = re.search(r'def ' + name + r' : List Nat := \[(.*?)\]', src, re.S)
    return m.start(1), m.end(1), [int(x) for x in m.group(1).replace('\n', ' ').split(',')]


def drop_one(name):
    a, b, c = layer_span(name)
    return src[:a] + ', '.join(str(x) for x in c[1:]) + src[b:]


def shift(name):
    a, b, c = layer_span(name)
    return src[:a] + ', '.join(str((x << 1) & 0xFFFF) for x in c) + src[b:]


def once(old, new):
    assert src.count(old) == 1, old
    return src.replace(old, new)


m4 = re.search(r'def path353 : Nat × List \(Bool × Bool\) :=\n  \((\d+), \[\((true|false),', src)
MUT = {
    'M1': drop_one('lay10010010000'),
    'M2': once('theorem check3353 : wordCheck (gapWord [3, 3, 5, 3]) layers3353 = true := by\n  rw [show gapWord [3, 3, 5, 3] =',
               'theorem check3353 : wordCheck (gapWord [3, 3, 5, 5]) layers3353 = true := by\n  rw [show gapWord [3, 3, 5, 5] ='),
    'M3': once('theorem start1 : startOK true lay1 = true', 'theorem start1 : startOK false lay1 = true'),
    'M4': src[:m4.start(2)] + ('false' if m4.group(2) == 'true' else 'true') + src[m4.end(2):],
    'M4a': src[:m4.start(1)] + str(int(m4.group(1)) ^ 1) + src[m4.end(1):],
    'M4b': re.sub(r'(def path553 : Nat × List \(Bool × Bool\) :=\n  \()\d+', r'\g<1>0', src, count=1),
    'M5': re.sub(r'(def layers333 : List \(List Nat\) := \[.*?), \[\]\]', r'\1]', src, count=1, flags=re.S),
    'M6': drop_one('lay1'),
    'M7': shift('lay10000100001'),
}
assert MUT['M5'] != src and MUT['M4b'] != src
only = sys.argv[4:]
res = {}
for k, text in MUT.items():
    if only and k not in only:
        continue
    f = KIT / f'MutTrap{k}.lean'
    f.write_text(text)
    t = time.time()
    r = subprocess.run([str(Path.home() / '.elan/bin/lake'), 'env', 'lean', f.name], cwd=KIT, capture_output=True, text=True,
                       timeout=600)
    f.unlink()
    errs = [l for l in (r.stdout + r.stderr).splitlines() if 'error' in l]
    (OUT / f'{k}.txt').write_text(r.stdout + r.stderr)
    res[k] = ('REJECTED' if r.returncode != 0 and errs else 'ACCEPTED', round(time.time() - t, 1), errs[:1])
    print(k, *res[k], flush=True)
print('ALL REJECTED' if all(v[0] == 'REJECTED' for v in res.values()) else 'SOME MUTANT ACCEPTED')
