#!/usr/bin/env python3
"""rule30_rings.py: which temporal column periods Rule 30's spatially periodic orbits allow, and what the periodic
tails of rule30_periodic.py's forced left halves are.

RUN-ON:     cpu (pure Python 3, standard library; exact)
COMMAND:    python3 tests/probes/lexicon/rule30_rings.py [N_MAX=18] [W_TAILS=12] [K=256]
PREDICTION: none for the table, which is a measurement (written after rule30_periodic.py's first run showed 7-, 14-
            and 28-periodic tails for periods 2 and 4 only, 2026-10-04). Its controls must pass: the 7-ring's cycle
            lengths are 1, 4 (seven times) and 63; every one of the 2^1 + ... + 2^N_MAX states is visited exactly once.
REFUTED-BY: a control failing.
COST:       about a second for the rings; seconds for the tails and the deep tails.

A spatially n-periodic Rule 30 configuration is Rule 30 on a ring of n cells: a finite program, whose loops are its
spectrum (LEXICON.md 3.6). A column of such an orbit is periodic with a period dividing the cycle length. Recorded in
RULE30-PRIZE.md section 5.
"""
import importlib.util, pathlib, sys
from collections import Counter

N_MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 18
W_TAILS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
K = int(sys.argv[3]) if len(sys.argv) > 3 else 256
FAILS = 0


def report(name, ok, detail=""):
    global FAILS
    FAILS += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))


def ring_map(n):
    m = (1 << n) - 1
    return [(((x << 1) | (x >> (n - 1))) & m) ^ (x | (((x >> 1) | ((x & 1) << (n - 1))) & m)) for x in range(1 << n)]


def ring_cycles(n):
    """Every cycle of Rule 30 on the n-ring, and the number of states visited."""
    f = ring_map(n)
    state, cycles, visited = bytearray(1 << n), [], 0
    for s in range(1 << n):
        if state[s]:
            continue
        path, x = [], s
        while state[x] == 0:
            state[x] = 1
            path.append(x)
            x = f[x]
        if state[x] == 1:
            cycles.append(path[path.index(x):])
        for y in path:
            state[y] = 2
        visited += len(path)
    return cycles, visited


def column_period(cyc, c):
    col = [(y >> c) & 1 for y in cyc]
    L = len(cyc)
    return next(p for p in range(1, L + 1) if L % p == 0 and all(col[k] == col[(k + p) % L] for k in range(L)))


def main():
    c7, v7 = ring_cycles(7)
    lens7 = Counter(len(c) for c in c7)
    report("control: the 7-ring's cycle lengths are 1, 4 (x7), 63", dict(lens7) == {1: 1, 4: 7, 63: 1}, str(dict(lens7)))
    realised, total = {}, 0
    for n in range(1, N_MAX + 1):
        cycles, v = ring_cycles(n)
        total += v
        for cyc in cycles:
            for c in range(n):
                realised.setdefault(column_period(cyc, c), set()).add(n)
    expect = sum(1 << n for n in range(1, N_MAX + 1))
    report(f"control: every state of rings 1..{N_MAX} visited exactly once", total == expect, f"{total} of {expect}")
    print(f"\ncolumn periods <= 12 realised by spatially periodic Rule 30 orbits, rings 1..{N_MAX}:")
    for p in range(1, 13):
        print(f"   period {p:>2}: " + (", ".join(map(str, sorted(realised[p]))) if p in realised else "none"))

    spec = importlib.util.spec_from_file_location("r30", pathlib.Path(__file__).with_name("rule30_periodic.py"))
    r30 = importlib.util.module_from_spec(spec)
    sys.argv = sys.argv[:1]
    spec.loader.exec_module(r30)
    print(f"\nperiodic tails of the forced left halves, right halves up to {W_TAILS} cells, depth {K}:")
    for word in [(0, 1), (1, 0)]:
        tau = [word[t % 2] for t in range(K + 1)]
        tails, onset = Counter(), Counter()
        for R in range(1 << W_TAILS):
            L = r30.forced_left(R, tau, K)
            kind = r30.tail_kind(L)
            if not kind.startswith("period"):
                continue
            q = int(kind.split()[1])
            tail = L[-q:]
            tails[(q, min(tuple(tail[i:] + tail[:i]) for i in range(q)))] += 1
            onset[next(s for s in range(len(L)) if all(L[i] == L[i + q] for i in range(s, len(L) - q)))] += 1
        print(f"   trace {''.join(map(str, word)) * 3}...: {sum(tails.values())} periodic tails; "
              f"from the first cell: {onset.get(0, 0)}")
        for (q, w), n in sorted(tails.items(), key=lambda kv: -kv[1])[:4]:
            print(f"      period {q:>2}: {''.join(map(str, w))}  x{n}")
    # Deep tails: are the "aperiodic over 64 cells" left halves long transients into a ring orbit? A period q is
    # accepted only with at least 128 comparisons (window 256, q <= 128), so a short window cannot fake one.
    KD, WD, n, qmax = 768, 10, 256, 128
    print(f"\ndeep tails, right halves up to {WD} cells, depth {KD}, period <= {qmax} over the last {n} cells:")
    for word in [(0, 1), (1, 0)]:
        tau = [word[t % 2] for t in range(KD + 1)]
        per, zero, aper, qs = 0, 0, 0, set()
        for R in range(1 << WD):
            tail = r30.forced_left(R, tau, KD)[-n:]
            if not any(tail):
                zero += 1
                continue
            q = next((q for q in range(1, qmax + 1) if all(tail[i] == tail[i + q] for i in range(n - q))), None)
            if q:
                per += 1
                qs.add(q)
            else:
                aper += 1
        print(f"   trace {''.join(map(str, word)) * 3}...: periodic {per} (periods {sorted(qs)}), zero {zero}, "
              f"no period: {aper}")
    print(f"\n{'ALL CHECKS PASS' if FAILS == 0 else f'{FAILS} FAILURE(S)'}")
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
