#!/usr/bin/env python3
"""not_absorption_replay.py (Local, 10 November 2026; S-05): the plain-Python replay of the worked-numbers cell of the
AbsorptionT t001 essay. Usage: python3 not_absorption_replay.py KIT_DIR

Prediction (written before the first run): driven by 001 from phase 0, the module's witness (cells 1..48 the number
266113541000008) and the half that lhallee/rule30-open names (196676618523018) never have cells 1..47 equal to a state
of the kit's t001 at a label of the same phase within 3,000 steps, and each shows at most 153 distinct 52-cell
windows (the size of trap001fifteen); the empty half, the control, enters t001 by step 1270 (the kit's
`absorbed_empty`). Counterfactual: an entry for either witness contradicts `not_absorptionT_t001` and means the
encoding is misread; no entry for the empty half means the test cannot see entries.

A right half is an integer X whose bit k is column k + 1; one step driven by c is ((X << 1) | c) ^ (X | (X >> 1)).
It prints {first entry of the witness, of rule30-open's half, of the empty half (-1 for none), distinct 52-cell
windows of the witness, of rule30-open's half}. The notebook's first Output cell must equal this list."""
import re
import sys
from pathlib import Path

sys.set_int_max_str_digits(100000)

src = (Path(sys.argv[1]) / 'lean/Ruliology/CellularAutomata/Rule30EtherThreeTrap.lean').read_text()
R = int(re.search(r'def t001_R : Nat := (\d+)', src).group(1))
L = int(re.search(r'def t001_L : Nat := (\d+)', src).group(1))
n, b, lb = 815, 47, 5
states = {}
for i in range(n):
    s, l = (R >> (b * i)) % (1 << b), (L >> (lb * i)) % (1 << lb)
    states.setdefault(l % 3, set()).add(s)
word = [0, 0, 1]


def run(x, T=3000):
    first, seen = -1, set()
    for t in range(T + 1):
        if first < 0 and (x % (1 << b)) in states.get(t % 3, ()):
            first = t
        seen.add(x % (1 << 52))
        x = ((x << 1) | word[t % 3]) ^ (x | (x >> 1))
    return first, len(seen)


a, b1, c = run(266113541000008), run(196676618523018), run(0)
out = [a[0], b1[0], c[0], a[1], b1[1]]
print('{' + ', '.join(map(str, out)) + '}')
assert a[0] == -1 and b1[0] == -1 and 0 <= c[0] <= 1270 and a[1] <= 153 and b1[1] <= 153
