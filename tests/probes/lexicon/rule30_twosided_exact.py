#!/usr/bin/env python3
"""rule30_twosided_exact.py: both sides exactly. For every finite right half of a given width, column 1 is what the
right side really produces (column 0 clamped to a periodic word), and the left half is forced from columns 0 and 1.
How long can a run of zeros in that left half be?

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_twosided_exact.py [WMAX=24] [K=384] [JOBS=4] [WORDS=01,0001]
COST:       about 2 minutes at WMAX 20, K 192; each step of 2 in WMAX costs about four times as much.

The owner's suggestion (2026-10-04): use the right side as a complement to the left. With column 1 free, the left
side allows zero runs about as long as the depth they start at (rule30_rigidity.py). With column 1 produced by a real
right half, the first measurement (recorded before the predictions below, not predicted) gave:
  longest zero run, depth <= 192, over every right half of exact width W:
    word 01:   W =  8: 14, 10: 15, 12: 15, 14: 20, 16: 20, 18: 20, 20: 20
    word 0001: W =  8: 13, 10: 13, 12: 17, 14: 17, 16: 17, 18: 17, 20: 17
  and, over every right half up to 16 cells and depth <= 256, the longest run by starting band showed no trend.
If a bound B holds for every finite right half at every depth, the forced left half has a one in every B+1 cells, so it
is never eventually zero, and no finite configuration has a column periodic with that word.

PREDICTIONS, written 2026-10-04 before this script's first run:
  X1 (control): the search reproduces the recorded values above for W <= 20 at depth 192 (01: 20, 0001: 17).
  X2 (control): with the right half replaced by a free column 1 (the left side alone), the exhaustive search of
     rule30_rigidity.py finds runs well past the two-sided bound inside the same window: at least 30 cells for 01 (from
     depth 33) and at least 40 for 0001 (from depth 18). So long runs fit in the window and can be seen. (A greedy
     random search was tried first as this control and rejected in a dry run: it found only 19 and 14, which proves
     nothing.)
  X3 (the plateau, uncertain): the bound holds further. For W = 22 and 24, the longest run is still 20 (01) and 17
     (0001), at depth up to K = 384.
REFUTED-BY: X1 or X2 failing (the instrument is wrong); for X3, a longer run at W = 22 or 24, or deeper than 192.
"""
import pathlib, sys
from multiprocessing import Pool

WMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 24
K = int(sys.argv[2]) if len(sys.argv) > 2 else 384
JOBS = int(sys.argv[3]) if len(sys.argv) > 3 else 4
WORDS = [tuple(int(c) for c in w) for w in (sys.argv[4] if len(sys.argv) > 4 else "01,0001").split(",")]
RECORDED = {(0, 1): 20, (0, 0, 0, 1): 17}
FAILS = 0

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
_argv, sys.argv = sys.argv, sys.argv[:1]          # the helpers read their own arguments at import
import rule30_periodic as r30                     # noqa: E402  (imported by name so the process pool can pickle)
import rule30_rigidity as rg                      # noqa: E402
sys.argv = _argv


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""), flush=True)


def verdict(name, held, detail=""):
    print(f"{'HELD' if held else 'REFUTED'}  prediction {name}" + (f"  ({detail})" if detail else ""), flush=True)


def longest_run(L, upto):
    run = m = 0
    for b in L[:upto]:
        run = run + 1 if b == 0 else 0
        m = max(m, run)
    return m


def chunk(args):
    word, lo, hi, k = args
    tau = [word[t % len(word)] for t in range(k + 1)]
    m192 = mk = 0
    for R in range(lo, hi):
        if R == 0 and not any(word):
            continue
        L = r30.forced_left(R, tau, k)
        m192 = max(m192, longest_run(L, 192))
        mk = max(mk, longest_run(L, k))
    return m192, mk


def free_window(word):
    """X2: the left side alone, searched exhaustively (rule30_rigidity.py), from a depth where it is known to allow a
    long run: 01 from depth 33, 0001 from depth 18."""
    d = {(0, 1): 33, (0, 0, 0, 1): 18}[word]
    n = len([u for u in range(d - 1) if word[u % len(word)] == 0])
    with Pool(JOBS) as pool:
        return d, max(r[2] for r in pool.map(rg.search, [(word, d, c) for c in range(1 << n)], chunksize=512))


def main():
    with Pool(JOBS) as pool:
        for word in WORDS:
            name = "".join(map(str, word))
            rows = []
            for W in range(8, WMAX + 1, 2):
                lo0 = 1 << (W - 1)
                step = max(1, (1 << (W - 1)) // (16 * JOBS))
                res = pool.map(chunk, [(word, lo, min(lo + step, 1 << W), K) for lo in range(lo0, 1 << W, step)])
                rows.append((W, max(r[0] for r in res), max(r[1] for r in res)))
                print(f"   word {name}, exact width {W}: longest run depth<=192: {rows[-1][1]}, depth<={K}: {rows[-1][2]}",
                      flush=True)
            if word in RECORDED:
                upto20 = max(r[1] for r in rows if r[0] <= 20)
                report(f"X1 word {name}: reproduces the recorded bound for W <= 20 at depth 192", upto20 == RECORDED[word],
                       f"{upto20} (recorded {RECORDED[word]})")
                d, free = free_window(word)
                need = {(0, 1): 30, (0, 0, 0, 1): 40}[word]
                report(f"X2 word {name}: a free column 1 allows runs past the two-sided bound (from depth {d})",
                       free >= need and d + free <= 192, f"longest {free} cells, ending at depth {d + free - 1}")
                beyond = [r for r in rows if r[0] > 20]
                if beyond:
                    worst = max(max(r[1], r[2]) for r in beyond)
                    verdict(f"X3 word {name}: still {RECORDED[word]} at W = 22..{WMAX}, depth <= {K}",
                            worst <= RECORDED[word], f"longest {worst}")
    print(f"\n{'ALL CONTROLS PASS' if FAILS == 0 else f'{FAILS} CONTROL FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
