#!/usr/bin/env python3
"""rule30_factorial_compare.py A.txt B.txt: F4 of rule30_factorial.py. Compare two runs' tail probabilities (one seeded
Mersenne Twister, one GEN=os) and print the largest disagreement in standard errors.

RUN-ON:  cpu
COMMAND: python3 tests/probes/lexicon/rule30_factorial.py > mt.txt; GEN=os python3 tests/probes/lexicon/rule30_factorial.py > os.txt;
         python3 tests/probes/lexicon/rule30_factorial_compare.py mt.txt os.txt [SAMPLES=100000]
First result (Cloud, 2026-10-04): 3.43 standard errors at most, over 152 comparisons, in the 'neither' arm (coin flips
against coin flips): F4 held. The OS run is not reproducible by design; the comparison is.
"""
import math, re, sys


def parse(f):
    out, word = {}, None
    for line in open(f):
        m = re.match(r"\s+word (\d+): probability", line)
        if m:
            word = m.group(1)
            continue
        m = re.match(r"\s+(\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", line)
        if m and word:
            out[(word, int(m.group(1)))] = [float(m.group(i)) for i in range(3, 7)]
    return out


a, b = parse(sys.argv[1]), parse(sys.argv[2])
N = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
arms = ["neither", "right alone", "left alone", "both"]
worst, where, n = 0.0, None, 0
for k in sorted(a):
    for i, (x, y) in enumerate(zip(a[k], b[k])):
        p = (x + y) / 2
        se = math.sqrt(max(p * (1 - p), 1e-12) * 2 / N)
        z = abs(x - y) / se
        n += 1
        if z > worst:
            worst, where = z, (k, arms[i], x, y)
print(f"{n} comparisons; largest disagreement {worst:.2f} standard errors at word {where[0][0]}, B = {where[0][1]}, "
      f"arm '{where[1]}' ({where[2]} against {where[3]})")
print(("HELD" if worst <= 4 else "REFUTED") + "  prediction F4: every tail probability within 4 standard errors")
sys.exit(0)
