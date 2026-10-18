# Cloud, CL452 (owner-authorized cheap search, 2026-10-18 late). Direct certificates for real towns.
#  Town = eight street lengths l_i in [68, 2m+66] summing to m^2; planks = odd lengths 1..2m-1; a certificate is an exact
#  tiling. Solver: largest-plank-first backtracking with parity and bound pruning; per-town time cap; unknowns recorded.
#  E24: every town at m=24 (the base level of the reduction). SLICE: at every level m=24..32, the most constrained towns,
#  every street within DELTA of the minimum 68 or of the maximum 2m+66. Certificates are written outside git.
import itertools, sys, time, json, hashlib, os
def planks(m): return list(range(2*m-1, 0, -2))
def solve(m, targets, cap=60.0):
    P = planks(m); k = len(targets); rem = list(targets); bins = [[] for _ in range(k)]
    if sum(targets) != m*m: return False, 0.0, 0
    # suffix min/max sums for t planks from P[i:] (smallest t / largest t)
    n = len(P); t0 = time.time(); nodes = [0]
    suf = [P[i:] for i in range(n+1)]; dead = set()
    def feasible(i):
        # each bin: remaining sum r with parity constraint (odd planks): need some t>=0 with t = r mod 2 and achievable range
        for r in rem:
            if r < 0: return False
            if r == 0: continue
            # minimal number of planks: largest first
            s = 0; t = 0
            for p in suf[i]:
                if s >= r: break
                s += p; t += 1
            if s < r: return False
        return True
    def rec(i):
        nodes[0] += 1
        if nodes[0] & 1023 == 0 and time.time() - t0 > cap: raise TimeoutError
        if i == n: return all(r == 0 for r in rem)
        key = (i, tuple(sorted(rem)))
        if key in dead: return False
        p = P[i]; tried = set()
        order = sorted(range(k), key=lambda b: -rem[b])
        for b in order:
            if rem[b] < p or rem[b] in tried: continue
            tried.add(rem[b]); rem[b] -= p; bins[b].append(p)
            if feasible(i+1) and rec(i+1): return True
            rem[b] += p; bins[b].pop()
        dead.add(key)
        return False
    try:
        ok = rec(0)
    except TimeoutError:
        return None, time.time() - t0, nodes[0]
    return (bins if ok else False), time.time() - t0, nodes[0]
def B(m, l):  # Tan-Teh minimal plank count with parity
    t = 1 if l % 2 else 2
    while 2*m*t - t*t < l: t += 2
    return t
def towns(m, lo, hi):
    for c in itertools.combinations_with_replacement(range(lo, hi+1), 8):
        if sum(c) == m*m: yield c
def slice_towns(m, delta):
    vals = sorted(set(list(range(68, 68+delta+1)) + list(range(2*m+66-delta, 2*m+67))))
    for c in itertools.combinations_with_replacement(vals, 8):
        if sum(c) == m*m: yield c
if __name__ == '__main__':
    mode = sys.argv[1]; out = sys.argv[2]; T0 = time.time(); results = []
    if mode == 'E24':
        gen = [(24, t) for t in towns(24, 68, 2*24+66)]
    else:
        delta = int(sys.argv[3]); gen = [(m, t) for m in range(24, 33) for t in slice_towns(m, delta)]
    print(f"{mode}: {len(gen)} towns", flush=True)
    stats = {'tiled': 0, 'impossible': 0, 'unknown': 0, 'count_test_fail': 0}; worst = 0
    for (m, t) in gen:
        if sum(B(m, l) for l in t) > m: stats['count_test_fail'] += 1
        bins, dt, nodes = solve(m, list(t))
        worst = max(worst, dt)
        if bins is None: stats['unknown'] += 1; results.append({'m': m, 'town': t, 'result': 'unknown', 'seconds': round(dt, 2)})
        elif bins is False: stats['impossible'] += 1; results.append({'m': m, 'town': t, 'result': 'impossible', 'seconds': round(dt, 2), 'nodes': nodes}); print("IMPOSSIBLE", m, t, flush=True)
        else: stats['tiled'] += 1; results.append({'m': m, 'town': t, 'tiling': bins, 'seconds': round(dt, 3)})
    json.dump(results, open(out, 'w'))
    h = hashlib.sha256(open(out, 'rb').read()).hexdigest()
    print(f"{mode} done: {stats}, worst town {worst:.1f}s, total {time.time()-T0:.0f}s, certificates sha256 {h[:16]} ({len(results)} records)", flush=True)
