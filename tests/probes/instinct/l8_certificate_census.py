#!/usr/bin/env python3
"""Read the output of CL454's L8 certificate job (tests/probes/cloud_reads/l8_certificates.py) and summarise it (L742).

Usage:  python3 l8_certificate_census.py OUTDIR [--workers N] [--top K]

What it reports, per level m = 24..32:
- towns read, against an independent count of the level (nondecreasing 8-tuples in [68, 2m+66] summing to m^2, by a
  bounded-partition DP, not the job's enumerator), and per chunk against the same DP with the smallest street fixed;
- tiled / impossible (X) / unknown (U), and duplicate or misplaced towns;
- node counts: n = m + 1 means the solver never backtracked into its recursion (its largest-remaining-first choice,
  filtered by the feasibility test, succeeded at every plank); quantiles and the share at n = m + 1 (L742's L4);
- the strict greedy flag g (cleared by any pruned branch, so expected near 0; L742's niggle);
- the towns with the largest node counts, overall and per level (CL454: "the interesting ones").
It does not re-verify tilings; the job's own `check` mode does that. Output is text for the record; data stays outside git.

OUTCOME (2026-10-19 01:46 BST, M5; run 23:59 to 01:46 BST, 6,385 s, 8 workers; certificates, 6.9 GB, in Local's
scratch outside git). Every level matches its independent count, chunk by chunk, with no duplicate or misplaced town:
    m      towns        X  U   n = m+1 (share)       strict g   largest node count
    24         3,319    0  0         121 (3.65%)          0      1,028
    25       425,632    0  0      28,444 (6.68%)         18      2,699
    26     5,523,890    0  0     493,758 (8.94%)        325      3,102
    27    19,382,158    0  0   1,895,813 (9.78%)      2,941      4,321
    28    24,688,633    0  0   1,881,055 (7.62%)      2,916      4,829
    29    12,385,850    0  0     906,216 (7.32%)      1,978      4,916
    30     2,271,658    0  0     157,828 (6.95%)        548      4,427
    31       106,518    0  0       3,862 (3.63%)         50        686
    32           186    0  0           5 (2.69%)          2        429
    all   64,787,844    0  0   5,367,102 (8.28%)      8,778
  Every town tiles. The hardest town took 4,916 nodes (m = 29, e.g. 87, 88, 98, 111, 112, 112, 112, 121), and no town
  came near the 120 s cap. The hardest towns at each level come in families of 16 with equal node counts that share
  their smallest streets. The shared prefix alone does not set the difficulty: of the 2,842 towns at m = 29 that start
  87, 88, 98, most take 30 to 70 nodes. L742's predictions: L1 HELD, L2 HELD (1 h 46 min), L3 HELD (the job's `check`:
  64,787,844 valid, 0 invalid; stream sha256 90fea878...), L4 REFUTED (the share peaks at m = 27).
"""
import sys, os, json, heapq, argparse
from collections import Counter
from multiprocessing import Pool

def count_bounded(total, parts, lo, hi):
    s = total - parts * lo; W = hi - lo
    if s < 0: return 0
    dp = [[0] * (s + 1) for _ in range(parts + 1)]; dp[0][0] = 1
    for v in range(1, W + 1):
        for j in range(1, parts + 1):
            row = dp[j]; prev = dp[j - 1]
            for n in range(v, s + 1): row[n] += prev[n - v]
    return sum(dp[j][s] for j in range(parts + 1))

def read_file(args):
    path, top = args
    st = {'towns': 0, 'tiled': 0, 'X': 0, 'U': 0, 'g': 0, 'nfree': 0, 'bad_min': 0, 'dups': 0, 'done': False}
    hist = Counter(); heap = []; seen = set(); m = l1 = None
    name = os.path.basename(path)                       # E<m>_l<l1>.jsonl
    fm, fl = name[1:-6].split('_l'); fm, fl = int(fm), int(fl)
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            if 'end' in r: st['done'] = True; st['declared'] = r['towns']; continue
            m = r['m']; t = tuple(r['town']); st['towns'] += 1
            if m != fm or t[0] != fl or list(t) != sorted(t): st['bad_min'] += 1
            if t in seen: st['dups'] += 1
            seen.add(t)
            if r.get('r') == 'X': st['X'] += 1; heapq.heappush(heap, (10**12, t, 'X')); continue
            if r.get('r') == 'U': st['U'] += 1; heapq.heappush(heap, (10**12, t, 'U')); continue
            n = r['n']; st['tiled'] += 1; st['g'] += r['g']
            if n == fm + 1: st['nfree'] += 1
            b = n if n <= fm + 40 else (1 << (n.bit_length() - 1)) + 10**9   # exact near the floor, log2 buckets above
            hist[b] += 1
            if len(heap) < top: heapq.heappush(heap, (n, t, 'T'))
            elif n > heap[0][0]: heapq.heapreplace(heap, (n, t, 'T'))
    return fm, fl, st, hist, heap

def quantile(hist, q, total):
    acc = 0
    for b in sorted(hist):
        acc += hist[b]
        if acc >= q * total: return b if b < 10**9 else f"~{b - 10**9}"
    return None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('outdir'); ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--top', type=int, default=12); a = ap.parse_args()
    files = sorted(os.path.join(a.outdir, f) for f in os.listdir(a.outdir) if f.endswith('.jsonl'))
    with Pool(a.workers) as pool:
        res = pool.map(read_file, [(p, a.top) for p in files], chunksize=1)
    levels = {}
    for fm, fl, st, hist, heap in res:
        L = levels.setdefault(fm, {'st': Counter(), 'hist': Counter(), 'heap': [], 'chunks': 0, 'chunk_bad': [], 'undone': 0})
        L['chunks'] += 1
        want = count_bounded(fm * fm - fl, 7, fl, 2 * fm + 66)
        if st['towns'] != want or st.get('declared') != want: L['chunk_bad'].append((fl, st['towns'], want))
        if not st['done']: L['undone'] += 1
        for k, v in st.items():
            if k not in ('done', 'declared'): L['st'][k] += v
        L['hist'].update(hist); L['heap'].extend(heap)
    all_top = []; grand = Counter(); ok = True
    for m in sorted(levels):
        L = levels[m]; st = L['st']; want = count_bounded(m * m, 8, 68, 2 * m + 66)
        nchunks = sum(1 for l1 in range(68, 2 * m + 67) if 8 * l1 <= m * m)
        tiled = st['tiled']; good = (st['towns'] == want and L['chunks'] == nchunks and not L['chunk_bad'] and not L['undone']
                                     and st['dups'] == 0 and st['bad_min'] == 0)
        ok &= good; grand.update(st)
        q = [quantile(L['hist'], x, tiled) for x in (0.5, 0.9, 0.99, 0.9999)] if tiled else []
        top = sorted(L['heap'], reverse=True)[:3]; all_top.extend((n, m, t, k) for n, t, k in L['heap'])
        flag = '' if good else f"; MISMATCH {L['chunk_bad'][:3]} undone {L['undone']}"
        print(f"E{m}: towns {st['towns']:,} (independent count {want:,}; chunks {L['chunks']}/{nchunks}{flag})"
              f"; tiled {tiled:,}, X {st['X']}, U {st['U']}, dups {st['dups']}, misplaced {st['bad_min']}")
        if tiled:
            print(f"     n = m+1 (no backtracking) {st['nfree']:,} = {100 * st['nfree'] / tiled:.2f}%; strict greedy g {st['g']:,};"
                  f" node quantiles 50/90/99/99.99%: {q}")
            print(f"     largest node counts: " + "; ".join(f"{n:,} {list(t)}" if k == 'T' else f"{k} {list(t)}" for n, t, k in top))
    print(f"ALL: towns {grand['towns']:,}, tiled {grand['tiled']:,}, X {grand['X']}, U {grand['U']},"
          f" n = m+1 {grand['nfree']:,} ({100 * grand['nfree'] / max(1, grand['tiled']):.2f}%), g {grand['g']:,}; "
          f"{'COMPLETE: every level matches its independent count' if ok and len(levels) == 9 else 'NOT COMPLETE'}")
    print("overall largest node counts:")
    for n, m, t, k in sorted(all_top, reverse=True)[:a.top]:
        print(f"  E{m} {list(t)}: {'%s' % k if k != 'T' else f'{n:,} nodes'}")

if __name__ == '__main__':
    main()
