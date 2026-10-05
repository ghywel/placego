#!/usr/bin/env python3
"""rule30_witness.py: the column 1 behind each record zero run of the forced left half, for one periodic word.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_witness.py [WORD=01] [DEPTHS=9,13,33] [JOBS=4]
PREDICTION: none: an exploration, recorded in RULE30-PRIZE.md section 7 (2026-10-04). It looks for a rescaling
            (a substitution mapping the record-setting column 1 at one depth to the next).
COST:       seconds at the defaults.

Uses rule30_rigidity.py's exact cell computation. A run is counted in cells: from depth d, every cell d, d+1, ... is
forced to zero for as long as some column 1 allows. The witnesses are printed as e(s) = column 1 at the times where the
word is 0, over the times the record run depends on.
"""
import importlib.util, pathlib, sys
from multiprocessing import Pool

WORD = tuple(int(c) for c in (sys.argv[1] if len(sys.argv) > 1 else "01"))
DEPTHS = [int(x) for x in (sys.argv[2] if len(sys.argv) > 2 else "9,13,33").split(",")]
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4

spec = importlib.util.spec_from_file_location("rg", pathlib.Path(__file__).with_name("rule30_rigidity.py"))
rg = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(rg)
sys.argv = _argv


def best_with_witness(args):
    d, code = args
    T = rg.tau_int(WORD, d + 400)
    before = [t for t in range(d - 1) if WORD[t % len(WORD)] == 0]
    col1 = 0
    for i, t in enumerate(before):
        col1 |= ((code >> i) & 1) << t
    best, stack = (0, col1), [(d, col1)]
    while stack:
        k, c1 = stack.pop()
        if k - d > best[0]:
            best = (k - d, c1)
        t = k - 1
        for c in ([c1, c1 | (1 << t)] if WORD[t % len(WORD)] == 0 else [c1]):
            if rg.cell(T, c, k) == 0:
                stack.append((k + 1, c))
    return best


def main():
    zeros = [t for t in range(1000) if WORD[t % len(WORD)] == 0]
    with Pool(JOBS) as pool:
        for d in DEPTHS:
            n = len([t for t in range(d - 1) if WORD[t % len(WORD)] == 0])
            res = pool.map(best_with_witness, [(d, c) for c in range(1 << n)], chunksize=512)
            m = max(r[0] for r in res)
            wits = [r[1] for r in res if r[0] == m]
            end = d + m
            es = sorted({"".join(str((c >> t) & 1) for t in zeros if t < end) for c in wits})
            print(f"word {''.join(map(str, WORD))}, depth {d}: longest run {m} cells ({d}..{end - 1}); "
                  f"{len(wits)} record-setting prefixes; {len(es)} distinct e")
            for e in es[:4]:
                print("    e =", e)


if __name__ == "__main__":
    main()
