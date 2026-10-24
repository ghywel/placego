#!/usr/bin/env python3
"""D5, revision 1 (2026-10-24, L850): the record-holders in free-bit coordinates. How much do the shallowest free bits
move a start's death time? NOT an agreed job until GPT reads L850; nothing runs on import; `--test` runs the
instrument's own controls at a small width only.

Coordinates (the kit's `Rule30ZeroBoundaryLanes`, d1_engine's `y_free`): a width-W start is its free bits y1, y3, ...,
y(W-1); lane bit s is y(2s+1); one chunk with n = W/2 holds every start. The death time of lane p is its elimination
level (equal to the physical first even white time at depth 1, verified exhaustively to width 12 in the record).

For each width W (one chunk, n = W/2, c = 0, K = D(W) + 1 so that every lane dies) and each k in (4, 6): group the lanes
by their deep prefix P = p >> k (free bits y(2k+1) and above); for each prefix record the k-th-power-of-two completions'
levels: spread = max - min, the prefix's own maximum, and the number of completions attaining it. Report the
distribution of spreads, the fraction of prefixes with spread 0, the record prefix (maximum level = D(W)): its spread
and attaining count, and the spread as a function of the prefix's maximum level (the unexpected check). The null:
the same statistic after a seeded random permutation of the levels across lanes (the spread a prefix would show if
the shallow bits were as decisive as everything else).

Predictions (L850): every lane dead at K and max level = D(W) from the table (known-value control); the record prefix's
attaining count equals the checkpoint's holder count (W = 30: 4; 32, 34, 36: 13); the median spread at k = 4 at most 4
levels; the fraction of spread-0 prefixes above one tenth; the permuted null's median spread comparable to the level
range. Counterfactual: a median spread comparable to the inter-prefix range refutes "the deep free bits determine".

Usage: python3 d5_spread.py W K OUT.json        (one width; W even, n = W/2 <= 18)
       python3 d5_spread.py --test              (W = 14, K = D(14) + 1 with D(14) from the physical engine: the engine
                                                 use, the grouping, the null and a wrong-K control, seconds)
OUTCOME: (to be filled after the agreed run)
"""
import json, os, random, statistics, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d1_engine as E

TABLE = {24: 42, 26: 44, 28: 48, 30: 52, 32: 66, 34: 66, 36: 66, 38: 72, 40: 76, 42: 78, 44: 78}   # D(W) from the record
HOLDERS = {30: 4, 32: 13, 34: 13, 36: 13, 38: 16, 40: 6, 42: 12, 44: 12}                                      # checkpoint holder counts


def levels_of(W, K):
    """Per-lane elimination level for the whole width (one chunk). Returns (levels list, alive mask)."""
    n = W // 2
    alive, elim, _ = E.run_lanes(W, n, 0, K, record=True)
    levels = [None] * (1 << n)
    for k, m in elim.items():
        while m:
            low = m & -m; p = low.bit_length() - 1; levels[p] = k; m ^= low
    return levels, alive


def spreads(levels, k):
    """Per deep prefix: (spread, prefix max, attaining count)."""
    size = 1 << k; out = {}
    for P in range(len(levels) >> k):
        block = levels[P << k:(P + 1) << k]
        mx = max(block); mn = min(block)
        out[P] = (mx - mn, mx, block.count(mx))
    return out


def summarise(per_prefix, D):
    sp = [v[0] for v in per_prefix.values()]
    hist = {}
    for s in sp: hist[s] = hist.get(s, 0) + 1
    rec = [(P, v) for P, v in per_prefix.items() if v[1] == D]
    by_max = {}
    for v in per_prefix.values():
        by_max.setdefault(v[1], []).append(v[0])
    return {'prefixes': len(sp), 'median_spread': statistics.median(sp), 'mean_spread': round(statistics.fmean(sp), 3),
            'max_spread': max(sp), 'fraction_spread_zero': round(sum(1 for s in sp if s == 0) / len(sp), 4),
            'spread_histogram': {str(k): hist[k] for k in sorted(hist)},
            'record_prefixes': [{'prefix_hex': hex(P), 'spread': v[0], 'attaining': v[2]} for P, v in rec],
            'median_spread_by_prefix_max': {str(m): statistics.median(v) for m, v in sorted(by_max.items())}}


def run(W, K, seed=1000003):
    t0 = time.time()
    levels, alive = levels_of(W, K)
    res = {'W': W, 'K': K, 'n': W // 2, 'lanes': len(levels), 'all_dead': alive == 0, 'undefined_levels': levels.count(None),
           'max_level': max(l for l in levels if l is not None), 'min_level': min(l for l in levels if l is not None),
           'table_D': TABLE.get(W), 'engine_s': round(time.time() - t0, 2)}
    res['known_value_control'] = res['all_dead'] and res['undefined_levels'] == 0 and res['max_level'] == TABLE.get(W)
    D = res['max_level']
    res['by_k'] = {}
    if not (res['all_dead'] and res['undefined_levels'] == 0):          # a lane without a level: no statistics, the control has already failed
        res['elapsed_s'] = round(time.time() - t0, 2); return res
    rnd = random.Random(seed * W)
    perm = levels[:]; rnd.shuffle(perm)
    for k in (4, 6):
        if k >= W // 2: continue
        real = summarise(spreads(levels, k), D)
        null = summarise(spreads(perm, k), D)
        res['by_k'][str(k)] = {'measured': real, 'permuted_null': {kk: null[kk] for kk in ('median_spread', 'mean_spread', 'fraction_spread_zero', 'max_spread')}}
    hold = HOLDERS.get(W)
    if hold is not None and '4' in res['by_k']:
        att = sum(r['attaining'] for r in res['by_k']['4']['measured']['record_prefixes'])
        res['holder_count_control'] = {'checkpoint': hold, 'measured_attaining_at_record': att, 'equal': att == hold}
    res['elapsed_s'] = round(time.time() - t0, 2)
    return res


def test():
    W = 14; D14 = E.D_phys(W, 200)[0]; TABLE[W] = D14; K = D14 + 1          # the small width's D from the physical engine, not from memory
    r = run(W, K)
    ok = r['known_value_control'] and r['by_k']['4']['measured']['prefixes'] == (1 << (W // 2 - 4))
    # the null must spread more than the measured, and a constant-level array must have spread 0 everywhere
    ok = ok and r['by_k']['4']['permuted_null']['median_spread'] >= r['by_k']['4']['measured']['median_spread']
    const = summarise(spreads([5] * (1 << 7), 4), 5)
    ok = ok and const['median_spread'] == 0 and const['fraction_spread_zero'] == 1.0
    # a wrong K (too small) must fail the known-value control: not every lane dead
    r2 = run(W, D14 - 10)
    ok = ok and not r2['known_value_control']
    print(json.dumps({'W14': r, 'wrongK_known_value_control': r2['known_value_control'], 'const_control': const['median_spread']}, indent=1)[:3000])
    print('D5 TEST', 'PASS' if ok else 'FAIL'); return ok


if __name__ == '__main__':
    if sys.argv[1:] == ['--test']:
        sys.exit(0 if test() else 1)
    if len(sys.argv) != 4:
        print(__doc__); sys.exit(2)
    W, K, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    if W % 2 or W // 2 > 18:
        print('REFUSED: W even and W/2 <= 18'); sys.exit(3)
    if os.path.exists(out):
        print('REFUSED: output exists'); sys.exit(3)
    r = run(W, K)
    json.dump(r, open(out, 'w'), indent=1)
    print(json.dumps({k: r[k] for k in ('W', 'K', 'lanes', 'all_dead', 'max_level', 'table_D', 'known_value_control', 'holder_count_control', 'elapsed_s') if k in r}))
    for k, v in r['by_k'].items():
        m = v['measured']; print('k =', k, '| prefixes', m['prefixes'], '| median spread', m['median_spread'], '| spread-0 fraction', m['fraction_spread_zero'], '| record', m['record_prefixes'], '| null median', v['permuted_null']['median_spread'])
