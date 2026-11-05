"""front_law.py: the actual front against the forced one, to wheel 894,235 (CL739). From the rows of tree16_data.py: the
single black cell evolved with the lag-32 band edge every tick, hence its settling tick tau_j for every wheel; the forced
front F_j on its strip (the recursion of CL730 on A0's words); the slope in windows of 100,000 wheels, the cumulative
ratios, the increments at the doublings, the increment histogram; the local coincidence statistics of CL695/CL730 over all
wheels (violations, share, slack); the lag F_j - tau_j. Then each other row of the tree, evolved from its parent's row with
the fork's child bit complemented, with its own tau above its fork: slope, windows, histogram. Predictions P-C1 … P-C4 in CL739.
Usage: python3 front_law.py STATEDIR seed | sib NAME | report"""
import sys, os, json, time
import numpy as np
K = 894236; MASK = (1 << K) - 1; P = 32; LAG = 32
STATE, CMD = sys.argv[1], sys.argv[2]
st = json.load(open(f"{STATE}/state.json"))
def step(v): return ((v << 2) ^ ((v << 1) | v)) & MASK
def lowbit(x): return (x & -x).bit_length() - 1 if x else K
def load_row(name): return int.from_bytes(open(f"{STATE}/rows/{name}.bin", 'rb').read(), 'little')
def evolve_edge(x0, t_max=3_000_000):
    """the lag-32 band edge E[t] for t = LAG .. until it has been K for 64 ticks; returns the array E (index t)."""
    ring = [x0]; E = np.zeros(t_max + 1, dtype=np.int32); t = 0; full = 0
    while True:
        x = step(ring[-1]); t += 1; ring.append(x)
        if len(ring) > LAG + 1: ring.pop(0)
        if t >= LAG:
            e = lowbit(x ^ ring[0]); E[t] = e
            full = full + 1 if e == K else 0
            if full >= 64: return E[:t + 1]
        if t > t_max: raise RuntimeError("no settling by the horizon")
def tau_of(E):
    """tau_j = first tick from which the edge stays above j for ever (the lag-32 wheel j and all below agree with their eventual period)."""
    Emin = np.minimum.accumulate(E[::-1])[::-1]              # Emin[t] = min_{u >= t} E[u]
    Emin[:LAG] = 0
    tau = np.searchsorted(Emin, np.arange(1, K + 1), side='left')   # first t with Emin[t] >= j + 1
    return tau.astype(np.int64)
def words_of(x):
    c = [x]
    for _ in range(P): c.append(step(c[-1]))
    assert c[P] == x
    w = np.zeros(K, dtype=np.int64)
    for r in range(P):
        bits = np.unpackbits(np.frombuffer(c[r].to_bytes((K + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:K]
        w += bits.astype(np.int64) << r
    return w
def forced(w):
    F = np.zeros(K, dtype=np.int64); F[0] = 0; F[1] = 1
    for j in range(1, K - 1):
        word = int(w[j]); m = int(F[j])
        if word == 0: F[j + 1] = m
        else:
            r = 0
            while not (word >> ((m + r) % P)) & 1: r += 1
            F[j + 1] = m + r + 1
    return F
def hist(inc):
    h = {str(k): float(np.mean(inc == k)) for k in range(0, 8)}; h['>=8'] = float(np.mean(inc >= 8)); return h
WIN = 100000
if CMD == 'seed':
    t0 = time.time(); E = evolve_edge(1); tau = tau_of(E)
    retreats = int(np.sum(np.diff(E[LAG:]) < 0))
    np.save(f"{STATE}/tau_seed.npy", tau)
    w = words_of(load_row('A0')); F = forced(w); np.save(f"{STATE}/F_A0.npy", F)
    out = {'name': 'seed', 'settle_tick': int(tau[K - 1]), 'edge_retreats': retreats, 'ticks': int(len(E) - 1), 'seconds': round(time.time() - t0)}
    bounds = list(range(0, K - 1, WIN)) + [K - 1]
    out['windows'] = [[int(a), int(b), round(float(tau[b] - tau[a]) / (b - a), 4)] for a, b in zip(bounds[:-1], bounds[1:])]
    out['cumulative'] = [[int(b), round(float(tau[b]) / b, 4)] for b in bounds[1:]]
    inc = np.diff(tau)
    out['increments_all'] = hist(inc); out['increment_mean'] = round(float(inc.mean()), 4)
    out['increments_after_100k'] = hist(inc[100000:])
    out['doublings'] = {str(d): [int(tau[d]), int(tau[d] - tau[d - 1])] for d in (3, 8, 29, 400, 87867)}
    out['increment_max'] = int(inc.max()); out['increment_p999'] = int(np.quantile(inc, 0.999))
    # coincidences (CL695 local form): G_k = 1 + first black of wheel k-1 at or after max(tau_{k-2}, tau_{k-1}); or that max if white
    G = np.zeros(K, dtype=np.int64)
    for k in range(2, K):
        m = int(max(tau[k - 2], tau[k - 1])); word = int(w[k - 1])
        if word == 0: G[k] = m
        else:
            r = 0
            while not (word >> ((m + r) % P)) & 1: r += 1
            G[k] = m + r + 1
    slack = G[2:] - tau[2:]
    def stats(lo, hi):
        s = slack[lo - 2:hi - 1]
        return {'wheels': int(len(s)), 'violations': int(np.sum(s < 0)), 'coincidence_share': round(float(np.mean(s > 0)), 4),
                'mean_slack': round(float(s.mean()), 4), 'slack_dist': {str(k): round(float(np.mean(s == k)), 4) for k in range(0, 6)}}
    out['coincidences'] = {'2..53207': stats(2, 53207), '53208..165749': stats(53208, 165749), '165750..894235': stats(165750, K - 1), 'all': stats(2, K - 1)}
    lag = F - tau
    out['lag'] = [[int(b), int(lag[b])] for b in bounds[1:]]
    out['lag_slope_100k_end'] = round(float(lag[K - 1] - lag[100000]) / (K - 1 - 100000), 4)
    out['forced_front_end'] = int(F[K - 1]); out['forced_slope_100k_end'] = round(float(F[K - 1] - F[100000]) / (K - 1 - 100000), 4)
    json.dump(out, open(f"{STATE}/front_seed.json", 'w'), indent=1); print(json.dumps(out)[:600])
elif CMD == 'sib':
    name = sys.argv[3]; s = st['strips'][name]; par = s['parent']; wf = s['fork']
    t0 = time.time(); x0 = load_row(par) ^ (1 << (wf + 1)); E = evolve_edge(x0); tau = tau_of(E)
    lo = wf + 1 + 10000; hi = K - 1
    out = {'name': name, 'fork': wf, 'settle_tick': int(tau[K - 1]), 'edge_retreats': int(np.sum(np.diff(E[LAG:]) < 0)), 'seconds': round(time.time() - t0)}
    out['slope_stretch'] = round(float(tau[hi] - tau[lo]) / (hi - lo), 4) if hi > lo else None
    bounds = list(range(lo, hi, WIN)) + [hi]
    out['windows'] = [[int(a), int(b), round(float(tau[b] - tau[a]) / (b - a), 4)] for a, b in zip(bounds[:-1], bounds[1:]) if b > a]
    out['increments_stretch'] = hist(np.diff(tau[lo:hi + 1])) if hi > lo else None
    json.dump(out, open(f"{STATE}/front_{name}.json", 'w'), indent=1); print(json.dumps(out)[:400])
elif CMD == 'report':
    seed = json.load(open(f"{STATE}/front_seed.json"))
    print(f"single cell: settled through {K-1} at tick {seed['settle_tick']}, edge retreats {seed['edge_retreats']}, {seed['seconds']} s")
    print("windows (lo, hi, slope):", seed['windows'])
    print("cumulative ratios:", seed['cumulative'])
    ws = [w[2] for w in seed['windows'] if w[0] >= 100000]
    print(f"P-C1 windows from 100,000 within [1.30, 1.335]: {all(1.30 <= x <= 1.335 for x in ws)}; spread {max(ws)-min(ws):.4f}; first-to-last {ws[-1]-ws[0]:+.4f}; all below 4/3: {all(x < 4/3 for x in ws)}")
    print("doublings (tau, increment):", seed['doublings'])
    print(f"P-C2 increment at 87,867 at most 8: {seed['doublings']['87867'][1] <= 8}; slope after 100,000 = {ws and round(sum(ws)/len(ws),4)}")
    print("increments all:", seed['increments_all'], "mean", seed['increment_mean'], "max", seed['increment_max'], "p99.9", seed['increment_p999'])
    print("coincidences:", json.dumps(seed['coincidences']))
    c = seed['coincidences']['all']
    print(f"P-C3 violations {c['violations']}, share {c['coincidence_share']} (within 0.01 of 0.454: {abs(c['coincidence_share']-0.454) <= 0.01}), slack0 {c['slack_dist']['0']}, lag slope {seed['lag_slope_100k_end']} (0.686 ± 0.01: {abs(seed['lag_slope_100k_end']-0.686) <= 0.01}), forced slope {seed['forced_slope_100k_end']}")
    print("lag at window ends:", seed['lag'])
    sl = []
    for name in st['order'][1:]:
        try: o = json.load(open(f"{STATE}/front_{name}.json"))
        except FileNotFoundError: print("missing", name); continue
        print(f"{name}: fork {o['fork']}, settled at {o['settle_tick']}, slope over the stretch {o['slope_stretch']}, windows {[w[2] for w in o['windows']]}, inc0 {o['increments_stretch']['0'] if o['increments_stretch'] else None}, inc1 {o['increments_stretch']['1'] if o['increments_stretch'] else None}, {o['seconds']} s")
        if o['slope_stretch'] is not None: sl.append((name, o['slope_stretch'], o['increments_stretch']))
    ok = all(1.30 <= s <= 1.34 for _, s, _ in sl)
    h0 = seed['increments_after_100k']
    agree = all(all(abs(h[k] - h0[k]) <= 0.02 for k in ('0', '1', '2', '3')) for _, _, h in sl)
    print(f"P-C4 all fifteen slopes within [1.30, 1.34]: {ok} (min {min(s for _,s,_ in sl):.4f}, max {max(s for _,s,_ in sl):.4f}); histograms within 0.02 of the single cell's: {agree}")
