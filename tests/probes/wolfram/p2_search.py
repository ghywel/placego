#!/usr/bin/env python3
"""P2, revision 1 (Local, 2026-10-24, L876): the survivor search at equal budgets (GPU-METAL-JOBS.md §J.2; the allocation of L872 with
GPT's GC1785 accounting). NOT an agreed job until GPT accepts this exact file and S0 has passed; nothing runs on import.

Question: how cheaply can a search that does not know the answer find a start attaining D(W), or near it, at W = 64 and 72? The census
answers (D(64) = 116 with 40 maximizers; D(72) = 130 with 252) are read ONLY by the scoring step after every search has finished.

Evaluator: S0's persistent server (driver revision 5; S0's client class), every requested lane counted as GROSS work (duplicates
included); unique lanes counted beside. Per case (method, width, seed) the budget is floor(2^22 / 5) = 838,860 gross lanes; a method
checks the remaining budget before every request and stops when its next unit does not fit; the unused remainder is reported, never
spent. Every evaluation with death >= W + 32 is recorded (index, death) for scoring; the incumbent curve records (gross, wall, death)
at every improvement. RNG: numpy PCG64, seed = 1000003 x W + 101 x method_id + seed, for seeds 1..5.

Methods (method_id): 1 uniform random (batches of 2^16, a final partial batch); 2 hill climbing (start at a random index, charged one
evaluation; each step evaluates all W/2 single-bit neighbours; move to the best if strictly better; if the best equals the current
value move to it (ties by the lowest index) at most 2 consecutive times; otherwise restart at a fresh random index, charged one
evaluation; a step needs W/2 remaining, a restart 1); 3 deep-first beam and 4 shallow-first beam (one empty initial prefix; 2 free bits
per round, from the deep end or the shallow end; each round expands every prefix to its 4 children; a child is scored by the MAXIMUM
death over R random completions of its unassigned bits (ties by the mean, then the lowest prefix value); the top B = 192 children are
kept; completions fresh each round; the last round's children are complete starts scored exactly; R = 72 at W = 64 (cost 633,504) and
R = 64 at W = 72 (cost 661,504); the best start seen in ANY completion batch is the incumbent); 5 cross-entropy (independent Bernoulli
probabilities per free bit from 0.5; population 2^14; elite the top 164 by death, ties by the lowest index; p <- 0.7 x elite frequency
+ 0.3 x p, clipped to [0.02, 0.98]; 51 full generations and a final partial population of 3,276 evaluated, not used to update).

Controls (`--controls`, CPU only, a mock evaluator): the beam's gross cost at W = 64 and 72 equals 633,504 and 661,504; the random,
cross-entropy and hill-climbing accounting never exceeds 838,860 and leaves the stated remainders; at W = 14 against the scalar engine
(the exact maximum known by brute force) every method finds a start whose recorded death equals the scalar death, and the deep-first
beam with a small budget reaches the W = 14 maximum; the RNG seeds are distinct per (method, width, seed).

Stage (`stage`): 5 methods x 2 widths x 5 seeds = 50 cases, sequential, one server per width; then the scoring step. Caps (W1A): wall
5,400 s, CPU 5,400 s, group RSS 6 GiB, GPU budget 2 GiB, artifacts 200 MiB, nothing else on the M5, no retry.
Usage: python3 p2_search.py --controls | stage OUT_DIR CENSUS64_RESULT.json CENSUS72_RESULT.json   (the census results are read only by the
       scoring step, after all 50 searches; their digests are recorded)
OUTCOME: (to be filled after the run)
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P

PER_CASE = (1 << 22) // 5          # 838,860
WIDTHS = {64: 256, 72: 288}
SEEDS = (1, 2, 3, 4, 5)
METHODS = {1: 'random', 2: 'hill', 3: 'beam_deep', 4: 'beam_shallow', 5: 'cem'}
BEAM_B = 192
BEAM_R = {64: 72, 72: 64, 14: 8}
MAX_REQ = 1 << 17


def rng_for(W, method, seed):
    import numpy as np
    return np.random.Generator(np.random.PCG64(1000003 * W + 101 * method + seed))


class Budgeted:
    """Wraps an evaluate(list_of_indices) -> list_of_deaths callable with gross/unique accounting and the incumbent record."""

    def __init__(self, evaluate, W, budget):
        self.evaluate, self.W, self.budget = evaluate, W, budget
        self.gross = 0; self.unique = set(); self.best = -2; self.best_index = None; self.first_reach = None
        self.curve = []; self.high = {}; self.t0 = time.monotonic()

    def remaining(self):
        return self.budget - self.gross

    def __call__(self, idx):
        idx = [int(i) for i in idx]
        if len(idx) > self.remaining():
            raise RuntimeError('request of %d exceeds the remaining budget %d' % (len(idx), self.remaining()))
        out = []
        for k in range(0, len(idx), MAX_REQ):
            out += self.evaluate(idx[k:k + MAX_REQ])
        self.gross += len(idx); self.unique.update(idx)
        for i, d in zip(idx, out):
            if d >= self.W + 32: self.high[i] = d
            if d > self.best:                                  # the first lane to reach a new best is the incumbent
                self.best, self.best_index, self.first_reach = d, i, self.gross
                self.curve.append((self.gross, round(time.monotonic() - self.t0, 3), d))
        return out


def m_random(ev, rng, W):
    n = W // 2
    while ev.remaining() > 0:
        k = min(1 << 16, ev.remaining())
        ev(rng.integers(0, 1 << n, size=k, dtype='uint64').tolist())


def m_hill(ev, rng, W):
    n = W // 2
    cur = cur_d = None; side = 0
    while True:
        if cur is None:
            if ev.remaining() < 1: return
            cur = int(rng.integers(0, 1 << n, dtype='uint64')); cur_d = ev([cur])[0]; side = 0
        if ev.remaining() < n: return
        nb = [cur ^ (1 << b) for b in range(n)]
        ds = ev(nb)
        best = max(ds); bi = min(i for i, d in zip(nb, ds) if d == best)
        if best > cur_d:
            cur, cur_d, side = bi, best, 0
        elif best == cur_d and side < 2:
            cur, side = bi, side + 1
        else:
            cur = None


def m_beam(ev, rng, W, order):
    import numpy as np
    n = W // 2; R = BEAM_R[W]
    seq = list(range(n - 1, -1, -1)) if order == 'deep' else list(range(n))
    groups = [seq[k:k + 2] for k in range(0, n, 2)]           # pairs of free bits; the last group is a single bit when n is odd
    beam = [(0, 0)]                                    # (assigned value, assigned mask)
    full = (1 << n) - 1
    import itertools
    for r, g in enumerate(groups):
        last = r == len(groups) - 1
        gm = sum(1 << b for b in g)
        children = [(v | sum(x << b for x, b in zip(xs, g)), m | gm) for v, m in beam for xs in itertools.product((0, 1), repeat=len(g))]
        reps = 1 if last else R
        if len(children) * reps > ev.remaining(): return
        idx = []
        for v, m in children:
            free = full & ~m
            if last:
                idx.append(v)
            else:
                rnd = rng.integers(0, 1 << n, size=reps, dtype='uint64')
                idx += [v | (int(x) & free) for x in rnd]
        ds = ev(idx)
        scored = []
        for c, (v, m) in enumerate(children):
            block = ds[c * reps:(c + 1) * reps]
            scored.append((-max(block), -sum(block) / len(block), v, m))
        scored.sort()
        beam = [(v, m) for _, _, v, m in scored[:BEAM_B]]


def m_cem(ev, rng, W):
    import numpy as np
    n = W // 2; p = np.full(n, 0.5); pop = 1 << 14; elite = 164
    weights = (1 << np.arange(n, dtype=np.uint64))
    while ev.remaining() > 0:
        k = min(pop, ev.remaining())
        bits = (rng.random((k, n)) < p)
        idx = (bits.astype(np.uint64) * weights).sum(axis=1).tolist()
        ds = ev(idx)
        if k < pop: return                              # the final partial population is scored, not used to update
        order = sorted(range(k), key=lambda i: (-ds[i], idx[i]))[:elite]
        freq = bits[order].mean(axis=0)
        p = np.clip(0.7 * freq + 0.3 * p, 0.02, 0.98)


RUN = {1: m_random, 2: m_hill, 3: lambda ev, rng, W: m_beam(ev, rng, W, 'deep'), 4: lambda ev, rng, W: m_beam(ev, rng, W, 'shallow'), 5: m_cem}


def run_case(evaluate, W, method, seed, budget=PER_CASE):
    ev = Budgeted(evaluate, W, budget)
    t = time.monotonic(); RUN[method](ev, rng_for(W, method, seed), W)
    return {'W': W, 'method': METHODS[method], 'seed': seed, 'budget': budget, 'gross': ev.gross, 'unused': ev.remaining(), 'unique': len(ev.unique),
            'best': ev.best, 'best_index': str(ev.best_index), 'first_reach_gross': ev.first_reach, 'wall_s': round(time.monotonic() - t, 3),
            'curve': ev.curve, 'high': {str(k): v for k, v in sorted(ev.high.items())}}


def controls():
    import random as pyr
    res = {}
    mock = lambda idx: [64 + (int(i) * 2654435761 >> 7) % 20 * 2 for i in idx]     # deterministic fake deaths, no GPU
    for W, want in ((64, 633504), (72, 661504)):
        r = run_case(mock, W, 3, 1); res['beam_deep_cost_W%d' % W] = r['gross'] == want
        r = run_case(mock, W, 4, 1); res['beam_shallow_cost_W%d' % W] = r['gross'] == want
        r = run_case(mock, W, 1, 1); res['random_spends_exactly_W%d' % W] = r['gross'] == PER_CASE and r['unused'] == 0
        r = run_case(mock, W, 5, 1); res['cem_spends_exactly_W%d' % W] = r['gross'] == PER_CASE
        r = run_case(mock, W, 2, 1); res['hill_within_budget_W%d' % W] = r['gross'] <= PER_CASE and r['unused'] < W // 2 + 1
    # W = 14 against the scalar engine, exact maximum by brute force
    W = 14; T = 4 * W
    scalar = lambda idx: [P.death(P.recon(W, int(i)), T) for i in idx]
    D = max(P.death(r, T) for r in range(1 << W))
    for m in METHODS:
        r = run_case(scalar, W, m, 1, budget=2000)
        res['W14_%s_record_matches_scalar' % METHODS[m]] = r['best'] == P.death(P.recon(W, int(r['best_index'])), T)
        if m == 3: res['W14_beam_deep_reaches_D'] = r['best'] == D
    seeds = {int(1000003 * W + 101 * m + s) for W in WIDTHS for m in METHODS for s in SEEDS}
    res['rng_seeds_distinct'] = len(seeds) == len(WIDTHS) * len(METHODS) * len(SEEDS)
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('P2 CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec'   # driver revision 6 (S0 revision 2, GC1786)
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_S = 5400


def score(cases, census):
    """After every search: each case against the census answer (read here for the first time). census[W] = (D, set of maximizer indices)."""
    out = []
    for c in cases:
        W, T = c['W'], WIDTHS[c['W']]; D, mx = census[W]
        near = {}
        for i, d in c['high'].items():
            if d >= D - 4:
                sd = P.death(P.recon(W, int(i)), T)
                near[i] = {'death': d, 'scalar_death': sd, 'scalar_agrees': sd == d, 'census_maximizer': int(i) in mx}
        out.append(dict({k: c[k] for k in ('W', 'method', 'seed', 'gross', 'unused', 'unique', 'best', 'first_reach_gross', 'wall_s')},
                        D=D, gap=D - c['best'], found_maximum=c['best'] == D, best_is_census_maximizer=int(c['best_index']) in mx, near=near))
    summary = {}
    for W in WIDTHS:
        for m in METHODS.values():
            rows = [o for o in out if o['W'] == W and o['method'] == m]
            if not rows: continue
            bests = sorted(o['best'] for o in rows)
            summary['W%d_%s' % (W, m)] = {'seeds_finding_D': sum(o['found_maximum'] for o in rows), 'best_per_seed': [o['best'] for o in rows],
                                           'median_best': bests[len(bests) // 2], 'first_reach_of_D': [o['first_reach_gross'] for o in rows if o['found_maximum']],
                                           'unused_per_seed': [o['unused'] for o in rows], 'scalar_disagreements': sum(1 for o in rows for v in o['near'].values() if not v['scalar_agrees'])}
    return out, summary


def run(out, census_paths):
    import s0_serve_controls as S0
    t0 = time.monotonic(); os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 's0_sha256': P.digest(S0.__file__), 'cases': [], 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 1)
        tmp = os.path.join(out, 'p2_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 'p2_result.json'))
    if P.digest(P.METAL) != METAL_SHA256 or P.digest(P.SWIFT) != SWIFT_SHA256:
        R['stopped'] = 'engine sources are not the pinned bytes'; save(); raise RuntimeError(R['stopped'])
    eng = P.Engine(out); R['build'] = eng.build(); save()
    for W, T in WIDTHS.items():
        srv = S0.Server(eng, out); rid = [0]

        def evaluate(idx, W=W, T=T, srv=srv, rid=rid):
            rid[0] += 1; req = {'id': rid[0], 'W': W, 'T': T, 'indices': [str(i) for i in idx]}
            res = srv.ask(req); probs = S0.check_response(req, res)
            if probs:
                srv.kill(); raise RuntimeError('evaluator response contract: %s' % probs)
            return res['deaths']
        for m in METHODS:
            for seed in SEEDS:
                R['cases'].append(run_case(evaluate, W, m, seed)); save()
        srv.kill()
    census = {}
    for W, pth in census_paths.items():
        c = json.load(open(pth))['census']; census[W] = (c['max'], {int(i) for i in c['maximizers']})
        R.setdefault('census_sha256', {})[str(W)] = P.digest(pth)
    R['scored'], R['summary'] = score(R['cases'], census)
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


def stage(out, census_paths):
    import w1a_harness as H
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 200 << 20; H.CAPS['log_max_bytes'] = 20 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['p2'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'metal_sha256': METAL_SHA256, 'swift_sha256': SWIFT_SHA256, 'w1a_sha256': W1A_SHA256,
                'census_sha256': {str(W): P.digest(p) for W, p in census_paths.items()}, 'per_case_budget': PER_CASE, 'cases': len(WIDTHS) * len(METHODS) * len(SEEDS),
                'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 200 << 20}, 'nice_inherited': os.nice(0)}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'p2_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        if rc != 0 or not d.get('complete'):
            return 'FAIL', 'rc %s complete %s' % (rc, d.get('complete'))
        return 'pass', 'P2 complete: %d cases scored' % len(d['scored'])
    cmd = [sys.executable, os.path.abspath(__file__), 'run', rdir, census_paths[64], census_paths[72]]
    rec = sup.run_step('p2_search', cmd, out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(a) == 4 and a[0] in ('run', 'stage'):
        cp = {64: a[2], 72: a[3]}
        if a[0] == 'stage':
            sys.exit(stage(a[1], cp))
        try:
            R = run(a[1], cp); print('P2 COMPLETE', len(R['scored']), 'cases'); sys.exit(0)
        except RuntimeError as e:
            print('P2 STOPPED:', e); sys.exit(1)
    print(__doc__); sys.exit(2)
