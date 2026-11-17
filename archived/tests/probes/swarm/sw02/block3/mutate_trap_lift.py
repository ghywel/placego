#!/usr/bin/env python3
"""mutate_trap_lift.py (Local, 9 November 2026; S-16): mutants of the portal form of `Rule30GateTrapLift`, each of
which must be REJECTED by Lean (any error). Usage: python3 mutate_trap_lift.py SOURCE KIT_REPO OUTDIR [MUTANT ...]

L1 drop one window from a chunk of the first layer (a step check fails)
L2 drop one window from a middle layer, lift12 (a step check fails)
L3 start from the white lift windows instead of the black ones (the start check fails)
L4 remove the final empty layer (the word check no longer reduces)
L5 shift every code of lift20 by one bit (a step check fails)
L6 flip column 1 of the start window of the 16-column path of 3535353 (trap_reads_3535353 fails)
L7 replace the start window of the lift path of 535353 by one whose low sixteen bits are not in the trap
"""
import re
import subprocess
import sys
import time
from pathlib import Path

src = Path(sys.argv[1]).read_text()
KIT = Path(sys.argv[2])
OUT = Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)
ONLY = sys.argv[4:]


def span(name):
    m = re.search(r'def ' + name + r' : List Nat := \[(.*?)\]', src, re.S)
    return m.start(1), m.end(1), [int(x) for x in re.findall(r'\d+', m.group(1))]


def drop_one(name):
    a, b, c = span(name)
    return src[:a] + ', '.join(str(x) for x in c[1:]) + src[b:]


def shift(name):
    a, b, c = span(name)
    return src[:a] + ', '.join(str((x << 1) & 0x3FFFF) for x in c) + src[b:]


def once(old, new):
    assert src.count(old) == 1, old
    return src.replace(old, new)


m6 = re.search(r'def path16_3535353 : Nat × List \(Bool × Bool\) :=\n  \((\d+), ', src)
MUT = {
    'L1': drop_one('lift0_1'),
    'L2': drop_one('lift12'),
    'L3': once('theorem liftStart : startOK18 true lift0 = true', 'theorem liftStart : startOK18 false lift0 = true'),
    'L4': re.sub(r'(def liftLayers : List \(List Nat\) := \[.*?), \[\]\]', r'\1]', src, count=1, flags=re.S),
    'L5': shift('lift20'),
    'L6': src[:m6.start(1)] + str(int(m6.group(1)) ^ 1) + src[m6.end(1):],
    'L7': re.sub(r'(def path18_535353 : Nat × List \(Bool × Bool\) :=\n  \()\d+', r'\g<1>1', src, count=1),
}
assert MUT['L4'] != src and MUT['L7'] != src
res = {}
for k, text in MUT.items():
    if ONLY and k not in ONLY:
        continue
    f = KIT / f'MutLift{k}.lean'
    f.write_text(text)
    t = time.time()
    r = subprocess.run([str(Path.home() / '.elan/bin/lake'), 'env', 'lean', f.name], cwd=KIT, capture_output=True, text=True,
                       timeout=900)
    f.unlink()
    errs = [l for l in (r.stdout + r.stderr).splitlines() if 'error' in l]
    (OUT / f'{k}.txt').write_text(r.stdout + r.stderr)
    res[k] = ('REJECTED' if r.returncode != 0 and errs else 'ACCEPTED', round(time.time() - t, 1), errs[:1])
    print(k, *res[k], flush=True)
print('ALL REJECTED' if all(v[0] == 'REJECTED' for v in res.values()) else 'SOME MUTANT ACCEPTED')
