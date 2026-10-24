#!/usr/bin/env python3
"""P2, revision 2 (Local, 2026-10-24, L879; revision 1 was L876's, reviewed by GPT in GC1787: "Source/design review COMPLETE WITH
CORRECTIONS; not launch-accepted"): the survivor search at equal budgets (GPU-METAL-JOBS.md §J.2; the allocation of L872 with GPT's
GC1785 accounting). NOT an agreed job until GPT accepts this exact file; nothing runs on import.

Question: how cheaply can a search that does not know the answer find a start attaining D(W), or near it, at W = 64 and 72? The census
answers (D(64) = 116 with 40 maximizers; D(72) = 130 with 252) are read by the search process ONLY in the scoring step after every
search has finished.

Methods, budgets and RNG (UNCHANGED from revision 1; the code of rng_for, m_random, m_hill, m_beam, m_cem is byte-identical): per case
(method, width, seed) floor(2^22 / 5) = 838,860 GROSS lanes (duplicates counted; unique counted beside); a method checks the remaining
budget before every request and stops when its next unit does not fit; the remainder is reported, never spent. 1 uniform random
(batches of 2^16, a final partial batch); 2 hill climbing (a random start charged one evaluation; each step evaluates all W/2 single-bit
neighbours; move to the best if strictly better; if equal, move (ties by the lowest index) at most 2 consecutive times; else restart,
charged one evaluation); 3 deep-first and 4 shallow-first beam (one empty initial prefix; 2 free bits per round, a single last bit when
the count is odd; each child scored by the MAXIMUM death over R random completions, ties by the mean, then the lowest prefix; B = 192
kept; the last round exact; R = 72 at W = 64, cost 633,504, and R = 64 at W = 72, cost 661,504); 5 cross-entropy (Bernoulli
probabilities from 0.5; population 2^14; elite 164, ties by the lowest index; p <- 0.7 x elite frequency + 0.3 x p, clipped to
[0.02, 0.98]; the final partial population scored, not used). numpy PCG64, seed = 1000003 x W + 101 x method + seed, seeds 1..5.

Revision 2, GPT's GC1787 fixes, each with controls:
 1. Correctness failures FAIL the stage, after the failing candidate is saved: a best whose scalar death differs from the recorded one; a
    best or candidate above the census maximum D; a claim of D by an index outside the census maximizer set; a census maximizer recorded
    with a different death; a near candidate (death >= D - 4) whose scalar death differs; a truncated near-candidate record. Nonmaximal
    near candidates need not be census maximizers. The census inputs are pinned by digest and validated in full (width and horizon,
    lanes = 2^(W/2), complete, zero censored, a complete maximizer list matching the count and the histogram, every census check
    passed); their bytes are re-hashed after the searches against the hashes recorded before them. The supervising stage validates
    them before launch; the search process opens them only after the searches.
 2. First reach is ORDERED: prior gross + lane offset + 1, the position in the method's own evaluation order. Separately labelled:
    the gross count at the end of the batch that held it and that batch's completion time, the moment the result existed. The curve's
    columns are named (CURVE_COLUMNS).
 3. A censored lane (-1) is a stop-and-investigate: the request's indices and deaths are retained (censor_event.json and the result),
    nothing continues, T is never widened. No method ever ranks a -1.
 4. One evaluator path, bound to the accepted, successful S0 stage: S0 (s0_serve_controls.py) and the P1 helper are imported only at
    their pinned digests; the S0 stage's receipt and result must be the exact retained files (digests pinned) and say what they should
    (complete, the pinned sources, one clean pass of exactly S0's required checks, zero live servers); the binary built here must equal
    the binary S0 passed. Every request goes through S0's transport (Server.exchange) and response check (check_response), then a
    zero-wait silence poll (poll_quiet, below); S0's own 0.2 s silence check runs before each server is closed. A run-wide finally
    closes every live server through S0's close_all. Progress is appended per request (p2_progress.jsonl), so an interrupted case keeps
    its charged requests; the interrupted case's record and the failure are saved before cleanup.
 5. The terminal gate (gate) requires the exact 50 (width, method, seed) cases, each with its budget invariants (gross + unused =
    budget; random and cross-entropy spend it all; beams cost exactly 633,504 / 661,504; hill climbing leaves fewer than W/2), valid
    counts, an exact scored set, zero correctness failures, no censor event, no interruption, the S0 and census bindings, and zero live
    servers. `complete` alone is not enough.
Also new: poll_quiet, a zero-wait poll after each response (S0's accepted quiet() waits 0.2 s, which after each of the 32,045 small hill-
climbing requests of the W = 64, seed 1 case (counted against a stub) would cost about 1.8 hours for that case; a stray byte arriving after the poll still fails the next exchange as
an unparsable line or a wrong id). The near-candidate record per case keeps each index once with death >= W + 32, capped at 65,536 by
death (ties by the lowest index) when it passes twice that; the largest pruned death is recorded and must be below D - 4 (the whole
census class holds 246 starts with death >= 112 at W = 64 and 496 with death >= 126 at W = 72, so the cap cannot bind on them). Each
case's full record is its own file (cases/case_NN.json, digest in the result).

Controls (`--controls`, CPU only: mocks, fakes and Python protocol stubs, no GPU): revision 1's 17, and for revision 2 the ordered first
reach, censoring (direct and inside a method), short, non-integer, odd and inconsistent evaluator results, every scoring failure kind and
the non-failures, census validation, S0 receipt validation, the terminal gate's mutations, the evaluator path against S0's stubs
(valid, trailing, malformed, bool echo, end of stream), and six end-to-end runs of the real search loop (guarded_search) against a stub server
through S0's transport at a small budget: a clean run that passes the case gate with the small budget's exact costs, a censor at a
known request (stopped, retained, servers closed), a server that dies mid-case (stopped, interrupted case saved, servers closed),
and GPT's GC1789 polling cases: a partial tail and a whole extra line arriving 50 ms after a response (after the zero-wait poll saw
silence) fail the next exchange, as unparsable and as a wrong id; a tail arriving after a width's last response fails S0's final
silence check before the close.

Stage (`stage`): 50 cases sequential, one server per width; then the scoring step. Caps (W1A): wall 5,400 s, CPU 5,400 s, group RSS
6 GiB (it covers the servers), GPU budget 2 GiB, artifacts 200 MiB, nothing else on the M5, no retry.
Usage: python3 p2_search.py --controls
       python3 p2_search.py inputs S0_STAGE_DIR CENSUS64_RESULT.json CENSUS72_RESULT.json   (validates the bindings only; no search)
       python3 p2_search.py stage OUT_DIR S0_STAGE_DIR CENSUS64_RESULT.json CENSUS72_RESULT.json
OUTCOME: (to be filled after the run)
"""
import copy, json, os, select, sys, tempfile, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_lane_engine as P
import s0_serve_controls as S0

PER_CASE = (1 << 22) // 5          # 838,860
WIDTHS = {64: 256, 72: 288}
SEEDS = (1, 2, 3, 4, 5)
METHODS = {1: 'random', 2: 'hill', 3: 'beam_deep', 4: 'beam_shallow', 5: 'cem'}
BEAM_B = 192
BEAM_R = {64: 72, 72: 64, 14: 8}
BEAM_COST = {64: 633504, 72: 661504}
MAX_REQ = 1 << 17
HIGH_CAP = 1 << 16
CURVE_COLUMNS = ['ordered_count', 'batch_end_gross', 'batch_completion_s', 'death']
PROGRESS_COLUMNS = ['case', 'request', 'lanes', 'gross_after', 'batch_completion_s', 'best_after']

METAL_SHA256 = '17a81e6621185098f3132ea199f41530de699f56030c9ac6c4c6392a7b1e5ec9'
SWIFT_SHA256 = '6b76fe740856c3e01c5bc2baffe68de6b9022bf8dfafb1ce8241ce4c0c3bd1ec'      # driver revision 6
P1_HELPER_SHA256 = 'ea9b7cc23d32373c270997cb8420b5ff1ce339eb5588813dd1ad1e859295738f'
S0_SHA256 = '9953969f97eed66c372db1c19cee008579dcb5bf2f36ccebeeda2df02cd422ad'          # S0 revision 2, the bytes GC1788 accepted and L878 ran
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
S0_RECEIPT_SHA256 = '225aa8df4306a3f4e8e4fc02ad119c28790e66b3b832099c76c6fec3b641cca7'  # L878's stage receipt (store cited/s0-stage-20261024-1548/)
S0_RESULT_SHA256 = '457a58c22e240984f8665fcd6c286d74b38cf351c8c5c008854a844486090667'   # L878's stage result
CENSUS_SHA256 = {64: '2b35f2e841e0a98553faaab632645a82849291fba76c470173de56a9c13a5d4f',   # P1b W = 64 (store cited/p1-packet/p1b-W64/)
                 72: '31df72e199ff1e63692bd79bffff1a1a1721a809e783a7ef0028d43c8d43293d'}   # P1c W = 72 (store cited/p1-packet/p1c-W72/)
STAGE_S = 5400


class Stop(Exception):
    pass


class Censored(Stop):
    pass


def atomic_json(path, obj, indent=None):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(obj, f, indent=indent)
    os.replace(tmp, path)


def rng_for(W, method, seed):
    import numpy as np
    return np.random.Generator(np.random.PCG64(1000003 * W + 101 * method + seed))


class Budgeted:
    """Wraps evaluate(list_of_indices) -> list_of_deaths with gross/unique accounting, ordered first reach, the censor stop and the
    near-candidate record. A charged request always writes its progress line (on_request), even when a check on its result then stops."""

    def __init__(self, evaluate, W, budget, on_request=None):
        self.evaluate, self.W, self.budget, self.on_request = evaluate, W, budget, on_request
        self.gross = 0; self.requests = 0; self.unique = set(); self.best = -2; self.best_index = None
        self.first_reach = None; self.first_batch_gross = None; self.first_batch_s = None
        self.curve = []; self.high = {}; self.high_pruned = 0; self.high_pruned_max = None; self.censor = None; self.t0 = time.monotonic()

    def remaining(self):
        return self.budget - self.gross

    def _keep_high(self, i, d):
        old = self.high.get(i)
        if old is not None and old != d:
            raise Stop('index %d returned deaths %d and %d' % (i, old, d))
        self.high[i] = d
        if len(self.high) > 2 * HIGH_CAP:
            ranked = sorted(self.high.items(), key=lambda kv: (-kv[1], kv[0]))
            self.high_pruned += len(ranked) - HIGH_CAP
            self.high_pruned_max = max(ranked[HIGH_CAP][1], -1 if self.high_pruned_max is None else self.high_pruned_max)
            self.high = dict(ranked[:HIGH_CAP])

    def __call__(self, idx):
        idx = [int(i) for i in idx]
        if not idx:
            raise Stop('an empty request')
        if len(idx) > self.remaining():
            raise Stop('request of %d exceeds the remaining budget %d' % (len(idx), self.remaining()))
        out = []
        for k in range(0, len(idx), MAX_REQ):
            part = idx[k:k + MAX_REQ]; got = self.evaluate(part)
            if type(got) is not list or len(got) != len(part):
                raise Stop('the evaluator returned %s results for %d lanes' % (len(got) if type(got) is list else type(got).__name__, len(part)))
            out += got
        prior = self.gross; self.gross += len(idx); self.requests += 1; self.unique.update(idx)
        t = round(time.monotonic() - self.t0, 3)
        try:
            bad = [d for d in out if type(d) is not int or not (d == -1 or (d >= 0 and d % 2 == 0))]
            if bad:
                raise Stop('the evaluator returned deaths outside the domain: %r' % bad[:3])
            if -1 in out:
                j = out.index(-1)
                self.censor = {'request': self.requests, 'prior_gross': prior, 'ordered_count': prior + j + 1,
                               'indices': [str(i) for i in idx], 'deaths': out}
                raise Censored('a censored lane (-1) at ordered count %d: stop and investigate; T is not widened' % (prior + j + 1))
            for j, (i, d) in enumerate(zip(idx, out)):
                if d >= self.W + 32: self._keep_high(i, d)
                if d > self.best:                              # ordered: the first lane, in the method's order, to reach a new best
                    self.best, self.best_index = d, i
                    self.first_reach, self.first_batch_gross, self.first_batch_s = prior + j + 1, self.gross, t
                    self.curve.append([prior + j + 1, self.gross, t, d])
        finally:
            if self.on_request: self.on_request(self, len(idx), t)
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


def case_record(ev, W, method, seed, budget, wall):
    return {'W': W, 'method': METHODS[method], 'seed': seed, 'budget': budget, 'gross': ev.gross, 'unused': ev.remaining(),
            'unique': len(ev.unique), 'requests': ev.requests, 'best': ev.best, 'best_index': None if ev.best_index is None else str(ev.best_index),
            'first_reach_ordered': ev.first_reach, 'first_reach_batch_end_gross': ev.first_batch_gross, 'first_reach_batch_s': ev.first_batch_s,
            'wall_s': round(wall, 3), 'curve_columns': CURVE_COLUMNS, 'curve': ev.curve,
            'high': {str(k): v for k, v in sorted(ev.high.items())}, 'high_pruned': ev.high_pruned, 'high_pruned_max_death': ev.high_pruned_max,
            'censor': ev.censor}


def run_case(evaluate, W, method, seed, budget=PER_CASE, on_request=None, holder=None):
    ev = Budgeted(evaluate, W, budget, on_request)
    if holder is not None: holder['ev'] = ev
    t = time.monotonic(); RUN[method](ev, rng_for(W, method, seed), W)
    return case_record(ev, W, method, seed, budget, time.monotonic() - t)


def score(cases, census):
    """After every search. census[W] = (D, set of maximizer indices). Returns (scored rows, summary, correctness failures)."""
    out, failures = [], []
    for c in cases:
        W = c['W']; T = WIDTHS[W]; D, mx = census[W]; key = [W, c['method'], c['seed']]

        def fail(kind, **kw):
            failures.append(dict(case=key, kind=kind, **kw))
        if c.get('best_index') is None:
            fail('no best index'); continue
        bi = int(c['best_index']); sb = P.death(P.recon(W, bi), T)
        if sb != c['best']: fail('best: scalar death differs', index=str(bi), recorded=c['best'], scalar=sb)
        if c['best'] > D: fail('best above the census maximum', index=str(bi), recorded=c['best'], D=D)
        if c['best'] == D and bi not in mx: fail('claimed D outside the census maximizer set', index=str(bi))
        if bi in mx and c['best'] != D: fail('census maximizer recorded with a different death', index=str(bi), recorded=c['best'], D=D)
        if c.get('high_pruned_max_death') is not None and c['high_pruned_max_death'] >= D - 4:
            fail('near-candidate record truncated', pruned_max_death=c['high_pruned_max_death'], D=D)
        near = {}
        for i, d in c['high'].items():
            ii = int(i)
            if d > D: fail('candidate above the census maximum', index=i, recorded=d, D=D)
            if ii in mx and d != D: fail('census maximizer recorded with a different death', index=i, recorded=d, D=D)
            if d == D and ii not in mx: fail('candidate at D outside the census maximizer set', index=i)
            if d >= D - 4:
                sd = P.death(P.recon(W, ii), T)
                if sd != d: fail('near candidate: scalar death differs', index=i, recorded=d, scalar=sd)
                near[i] = {'death': d, 'scalar_death': sd, 'census_maximizer': ii in mx}
        out.append(dict({k: c[k] for k in ('W', 'method', 'seed', 'gross', 'unused', 'unique', 'requests', 'best', 'best_index',
                                           'first_reach_ordered', 'first_reach_batch_end_gross', 'first_reach_batch_s', 'wall_s')},
                        D=D, gap=D - c['best'], found_maximum=c['best'] == D, best_is_census_maximizer=bi in mx, near=near))
    summary = {}
    for W in WIDTHS:
        for m in METHODS.values():
            rows = [o for o in out if o['W'] == W and o['method'] == m]
            if not rows: continue
            bests = sorted(o['best'] for o in rows)
            summary['W%d_%s' % (W, m)] = {
                'seeds_finding_D': sum(o['found_maximum'] for o in rows), 'best_per_seed': [o['best'] for o in rows], 'median_best': bests[len(bests) // 2],
                'first_reach_of_D_ordered': [o['first_reach_ordered'] for o in rows if o['found_maximum']],
                'first_reach_of_D_batch_end_gross': [o['first_reach_batch_end_gross'] for o in rows if o['found_maximum']],
                'unused_per_seed': [o['unused'] for o in rows], 'near_candidates_verified': sum(len(o['near']) for o in rows)}
    return out, summary, failures


def load_census(W, path, want='pinned'):
    """Validates a census result in full; returns (D, maximizer set, digest). want: 'pinned', a digest, or None (controls only)."""
    want = CENSUS_SHA256[W] if want == 'pinned' else want
    dg = P.digest(path)
    if want is not None and dg != want:
        raise Stop('census W = %d: digest %s is not the pinned %s' % (W, dg[:16], want[:16]))
    d = json.load(open(path)); c = d.get('census', {}); sc = d.get('scope', {}); n = 1 << (W // 2); probs = []
    if d.get('complete') is not True: probs.append('not complete')
    if sc.get('W') != W or sc.get('T') != WIDTHS.get(W): probs.append('scope width or horizon')
    if c.get('lanes') != n: probs.append('lanes != 2^(W/2)')
    if c.get('censored') != 0: probs.append('censored lanes')
    if c.get('maximizer_list_complete') is not True: probs.append('maximizer list incomplete')
    mx = [int(x) for x in c.get('maximizers', [])]
    if len(mx) != c.get('max_count') or len(set(mx)) != len(mx) or any(not 0 <= x < n for x in mx): probs.append('maximizer list')
    h = {int(k): int(v) for k, v in c.get('histogram', {}).items()}
    if sum(h.values()) + (c.get('censored') or 0) != n: probs.append('histogram total')
    if not h or c.get('max') != max(k for k, v in h.items() if v > 0) or h.get(c.get('max')) != c.get('max_count'): probs.append('maximum and histogram')
    chk = d.get('checks', {})
    if not chk or not all(type(v.get('pass')) is bool and v['pass'] for v in chk.values()): probs.append('a census check did not pass')
    if probs:
        raise Stop('census W = %d refused: %s' % (W, probs))
    return c['max'], set(mx), dg


def check_s0_receipt(s0_dir, want=(S0_RECEIPT_SHA256, S0_RESULT_SHA256)):
    """The accepted S0 stage must be the retained, successful one. Returns (problems, digests incl. the binary S0 passed)."""
    rp = os.path.join(s0_dir, 'receipts.json'); sp = os.path.join(s0_dir, 'run', 's0_result.json')
    try:
        rc = json.load(open(rp)); res = json.load(open(sp))
    except Exception as e:
        return ['S0 receipt or result unreadable: %r' % e], {}
    dig = {'receipt_sha256': P.digest(rp), 'result_sha256': P.digest(sp), 'binary_sha256': (res.get('build') or {}).get('binary_sha256')}
    probs = []
    if want[0] is not None and dig['receipt_sha256'] != want[0]: probs.append('receipt digest is not the pinned one')
    if want[1] is not None and dig['result_sha256'] != want[1]: probs.append('result digest is not the pinned one')
    s = rc.get('s0', {})
    if rc.get('complete') is not True: probs.append('receipt not complete')
    if rc.get('harness_sha256') != W1A_SHA256 or s.get('w1a_sha256') != W1A_SHA256: probs.append('W1A digest')
    for k, v in (('this_sha256', S0_SHA256), ('swift_sha256', SWIFT_SHA256), ('metal_sha256', METAL_SHA256), ('p1_helper_sha256', P1_HELPER_SHA256)):
        if s.get(k) != v: probs.append('receipt s0.%s' % k)
    steps = [x for x in rc.get('steps', []) if x.get('step') == 's0_serve_controls']
    if len(steps) != 1 or steps[0].get('verdict') != 'pass' or steps[0].get('proof_verdict') != 'pass' or steps[0].get('final_problems') != []:
        probs.append('the S0 step is not one clean pass')
    ch = res.get('checks', {})
    if res.get('complete') is not True or res.get('this_sha256') != S0_SHA256: probs.append('S0 result not complete at the pinned bytes')
    if sorted(ch) != sorted(S0.REQUIRED) or not all(type(v.get('pass')) is bool and v['pass'] for v in ch.values()):
        probs.append('S0 result checks are not exactly the required passes')
    if res.get('live_servers_at_finally') != 0: probs.append('S0 left a live server')
    if not dig['binary_sha256']: probs.append('S0 result names no binary')
    return probs, dig


def expected_cases():
    return {(W, METHODS[m], s) for W in WIDTHS for m in METHODS for s in SEEDS}


def gate_cases(cases, budget=PER_CASE, beam_cost=BEAM_COST):
    probs = []; want = expected_cases()
    keys = [(c.get('W'), c.get('method'), c.get('seed')) for c in cases]
    if len(keys) != len(want) or set(keys) != want: probs.append('the case set is not exactly the %d (width, method, seed) cases' % len(want))
    ints = ('W', 'seed', 'budget', 'gross', 'unused', 'unique', 'requests', 'best', 'first_reach_ordered', 'first_reach_batch_end_gross')
    for c in cases:
        k = (c.get('W'), c.get('method'), c.get('seed'))
        if any(type(c.get(f)) is not int for f in ints) or c.get('W') not in WIDTHS or c.get('method') not in METHODS.values():
            probs.append('%s: malformed case record' % (k,)); continue
        W, n, m = c['W'], c['W'] // 2, c['method']
        if c['budget'] != budget or c['gross'] + c['unused'] != budget or not 0 < c['gross'] <= budget: probs.append('%s: budget accounting' % (k,))
        if not 0 < c['unique'] <= c['gross'] or not 0 < c['requests'] <= c['gross']: probs.append('%s: unique or request counts' % (k,))
        if not 1 <= c['first_reach_ordered'] <= c['first_reach_batch_end_gross'] <= c['gross']: probs.append('%s: first-reach counts' % (k,))
        if not (0 <= c['best'] <= WIDTHS[W] and c['best'] % 2 == 0) or c.get('censor') is not None: probs.append('%s: best or censor' % (k,))
        if m in ('random', 'cem') and c['gross'] != budget: probs.append('%s: did not spend the budget' % (k,))
        if m.startswith('beam') and c['gross'] != beam_cost[W]: probs.append('%s: beam cost %d, not %d' % (k, c['gross'], beam_cost[W]))
        if m == 'hill' and not c['unused'] < n: probs.append('%s: hill climbing left %d >= W/2' % (k, c['unused']))
    return probs


def gate(d, budget=PER_CASE, beam_cost=BEAM_COST):
    """The terminal policy: exactly the 50 cases with their invariants, an exact scored set, zero correctness failures and the bindings."""
    probs = []
    if d.get('complete') is not True: probs.append('not complete')
    if d.get('failures') != []: probs.append('correctness failures: %s' % (len(d['failures']) if isinstance(d.get('failures'), list) else 'missing'))
    if d.get('censor_event') is not None: probs.append('a censor event')
    if d.get('interrupted_case') is not None or d.get('failure') is not None: probs.append('an interrupted case or a failure')
    if d.get('live_servers_at_finally') != 0: probs.append('live servers at the finally')
    if d.get('s0_receipt_ok') is not True or d.get('census_rehash_ok') is not True: probs.append('the S0 receipt or census binding')
    probs += gate_cases(d.get('cases', []), budget, beam_cost)
    sk = [(s.get('W'), s.get('method'), s.get('seed')) for s in d.get('scored', [])]
    if len(sk) != len(expected_cases()) or set(sk) != expected_cases(): probs.append('the scored set is not exactly the cases')
    return ('pass' if not probs else 'FAIL'), probs


def poll_quiet(srv):
    """After a response: 'silence' (nothing buffered or readable now), 'trailing' (any byte) or 'eof', polling S0's pipe once with zero
    wait (S0's accepted quiet() waits 0.2 s; it still runs before each server closes)."""
    if srv.buf: return 'trailing'
    r, _, _ = select.select([srv.p.stdout], [], [], 0)
    if not r: return 'silence'
    try:
        chunk = os.read(srv.p.stdout.fileno(), 1 << 16)
    except BlockingIOError:
        return 'silence'
    if not chunk:
        srv.eof = True; return 'eof'
    srv.buf += chunk
    return 'trailing'


def make_evaluator(srv, W, T):
    """The one evaluator path: S0's transport and response check, then the zero-wait silence poll."""
    rid = [0]

    def evaluate(idx):
        rid[0] += 1; req = {'id': rid[0], 'W': W, 'T': T, 'indices': [str(i) for i in idx]}
        st, res, raw = srv.exchange((json.dumps(req) + '\n').encode())
        if st != 'ok' or res is None or res == 'MALFORMED':
            raise Stop('evaluator transport: send %s, line %r' % (st, (raw or b'')[:200]))
        probs = S0.check_response(req, res)
        if probs: raise Stop('evaluator response contract: %s' % probs)
        q = poll_quiet(srv)
        if q != 'silence': raise Stop('evaluator stream after a response: %s' % q)
        return res['deaths']
    return evaluate


def guarded_search(out, R, save, server_for, budget=PER_CASE):
    """The 50 searches with per-request progress, per-case files, failure capture and the run-wide finally (S0.close_all)."""
    holder = {}; cdir = os.path.join(out, 'cases'); os.makedirs(cdir, exist_ok=True)
    prog = open(os.path.join(out, 'p2_progress.jsonl'), 'a', buffering=1); R['progress_columns'] = PROGRESS_COLUMNS
    try:
        for W, T in WIDTHS.items():
            srv = server_for(W); evaluate = make_evaluator(srv, W, T)
            for m in METHODS:
                for seed in SEEDS:
                    case_no = len(R['cases']) + 1; holder.clear(); holder['key'] = (W, m, seed)

                    def on_request(ev, n, t, case_no=case_no):
                        prog.write(json.dumps([case_no, ev.requests, n, ev.gross, t, ev.best]) + '\n')
                    rec = run_case(evaluate, W, m, seed, budget, on_request, holder); holder.clear()
                    cp = os.path.join(cdir, 'case_%02d.json' % case_no); atomic_json(cp, rec)
                    light = {k: v for k, v in rec.items() if k != 'high'}
                    light.update(case_file='cases/case_%02d.json' % case_no, case_sha256=P.digest(cp), high_count=len(rec['high']))
                    R['cases'].append(light); save()
            q = srv.quiet()
            if q != 'silence': raise Stop('the W = %d server was not live and silent before closing: %s' % (W, q))
            if not srv.close(): raise Stop('the W = %d server was not verified dead after closing' % W)
        return True
    except BaseException as e:
        ev = holder.get('ev')
        if ev is not None:
            W, m, seed = holder['key']
            R['interrupted_case'] = case_record(ev, W, m, seed, budget, time.monotonic() - ev.t0)
            if ev.censor is not None:
                R['censor_event'] = ev.censor; atomic_json(os.path.join(out, 'censor_event.json'), ev.censor)
        R['failure'] = {'type': type(e).__name__, 'message': str(e)[:1000], 'traceback': traceback.format_exc()[-3000:]}
        save(); raise
    finally:
        try: prog.close()
        except Exception: pass
        R['live_servers_at_finally'] = len(S0.LIVE)
        R['live_servers_closed_dead'] = S0.close_all()
        save()


STUB_SERVER = r'''
import json, os, sys, time
mode, n_at = sys.argv[1], int(sys.argv[2]); k = 0
while True:
    line = sys.stdin.readline()
    if not line: break
    req = json.loads(line); k += 1
    if mode == 'die' and k == n_at: os._exit(3)
    d = [64 + (int(i) * 2654435761 >> 7) % 20 * 2 for i in req['indices']]
    if mode == 'censor' and k == n_at: d[0] = -1
    sys.stdout.write(json.dumps({'id': req['id'], 'W': req['W'], 'T': req['T'], 'deaths': d}) + '\n'); sys.stdout.flush()
    if mode in ('tail', 'extra') and k == n_at:          # a DELAYED tail, after the client's zero-wait poll has seen silence
        time.sleep(0.05)
        sys.stdout.write('{"id"' if mode == 'tail' else json.dumps({'id': req['id'], 'W': req['W'], 'T': req['T'], 'deaths': d}) + '\n'); sys.stdout.flush()
'''


def _fake(responses):
    q = list(responses)
    return lambda idx: q.pop(0)


def _raises(f, exc):
    try:
        f()
    except exc:
        return True
    except Exception:
        return False
    return False


def controls():
    res = {}
    mock = lambda idx: [64 + (int(i) * 2654435761 >> 7) % 20 * 2 for i in idx]     # deterministic fake deaths, no GPU
    # --- revision 1's 17 (algorithms and accounting)
    for W, want in ((64, 633504), (72, 661504)):
        r = run_case(mock, W, 3, 1); res['beam_deep_cost_W%d' % W] = r['gross'] == want
        r = run_case(mock, W, 4, 1); res['beam_shallow_cost_W%d' % W] = r['gross'] == want
        r = run_case(mock, W, 1, 1); res['random_spends_exactly_W%d' % W] = r['gross'] == PER_CASE and r['unused'] == 0
        r = run_case(mock, W, 5, 1); res['cem_spends_exactly_W%d' % W] = r['gross'] == PER_CASE
        r = run_case(mock, W, 2, 1); res['hill_within_budget_W%d' % W] = r['gross'] <= PER_CASE and r['unused'] < W // 2 + 1
    W = 14; T = 4 * W
    scalar = lambda idx: [P.death(P.recon(W, int(i)), T) for i in idx]
    D = max(P.death(r, T) for r in range(1 << W))
    for m in METHODS:
        r = run_case(scalar, W, m, 1, budget=2000)
        res['W14_%s_record_matches_scalar' % METHODS[m]] = r['best'] == P.death(P.recon(W, int(r['best_index'])), T)
        if m == 3: res['W14_beam_deep_reaches_D'] = r['best'] == D
    seeds = {int(1000003 * W + 101 * m + s) for W in WIDTHS for m in METHODS for s in SEEDS}
    res['rng_seeds_distinct'] = len(seeds) == len(WIDTHS) * len(METHODS) * len(SEEDS)
    # --- fix 2: ordered first reach, batch-end counts labelled separately
    lines = []
    ev = Budgeted(_fake([[4, 10, 6], [12, 2]]), 64, 100, on_request=lambda e, n, t: lines.append((e.requests, n, e.gross)))
    ev([1, 2, 3]); a = (ev.first_reach, ev.first_batch_gross, [c[:2] + c[3:] for c in ev.curve])
    res['first_reach_ordered_within_batch'] = a == (2, 3, [[1, 3, 4], [2, 3, 10]])
    ev([4, 5]); res['first_reach_ordered_second_batch'] = (ev.first_reach, ev.first_batch_gross, ev.best) == (4, 5, 12) and lines == [(1, 3, 3), (2, 2, 5)]
    # --- fix 3: a censor is a stop, retained, never ranked
    lines = []
    ev = Budgeted(_fake([[-1, 100]]), 64, 100, on_request=lambda e, n, t: lines.append(e.gross))
    ok = _raises(lambda: ev([7, 8]), Censored)
    res['censored_lane_stops_retained_unranked'] = ok and ev.best == -2 and ev.gross == 2 and lines == [2] and ev.censor['deaths'] == [-1, 100] and ev.censor['ordered_count'] == 1
    calls = [0]

    def censor_third(idx):
        calls[0] += 1; d = mock(idx)
        if calls[0] == 3: d[0] = -1
        return d
    res['censored_lane_inside_a_method_stops'] = _raises(lambda: run_case(censor_third, 64, 2, 1), Censored) and calls[0] == 3
    # evaluator result faults
    ev = Budgeted(_fake([[100]]), 64, 100); res['short_result_stops'] = _raises(lambda: ev([1, 2]), Stop) and ev.gross == 0
    ev = Budgeted(_fake([[True]]), 64, 100); res['boolean_death_stops'] = _raises(lambda: ev([1]), Stop)
    ev = Budgeted(_fake([[101]]), 64, 100); res['odd_death_stops'] = _raises(lambda: ev([1]), Stop)
    ev = Budgeted(_fake([[100], [102]]), 64, 100); ev([7])
    res['inconsistent_repeated_index_stops'] = _raises(lambda: ev([7]), Stop)
    ev = Budgeted(mock, 64, 10); res['over_budget_request_stops'] = _raises(lambda: ev(list(range(11))), Stop) and ev.gross == 0
    # --- fix 1: scoring failures (W = 64, horizon 256, scalar engine)
    i0 = 12345; s0 = P.death(P.recon(64, i0), 256)

    def case(best, high=None, pruned=None):
        return {'W': 64, 'method': 'random', 'seed': 1, 'gross': 10, 'unused': 0, 'unique': 10, 'requests': 1, 'best': best, 'best_index': str(i0),
                'first_reach_ordered': 1, 'first_reach_batch_end_gross': 1, 'first_reach_batch_s': 0.0, 'wall_s': 0.0,
                'high': {str(i0): best} if high is None else high, 'high_pruned_max_death': pruned}

    def kinds(c, D, mx):
        return sorted({f['kind'] for f in score([c], {64: (D, mx)})[2]})
    res['score_correct_hit_no_failure'] = s0 >= 0 and kinds(case(s0), s0, {i0}) == []
    res['score_nonmaximal_near_candidate_outside_set_ok'] = kinds(case(s0), s0 + 4, set()) == []
    res['score_scalar_mismatch_fails'] = 'best: scalar death differs' in kinds(case(s0 + 2), s0 + 6, set()) and 'near candidate: scalar death differs' in kinds(case(s0 + 2), s0 + 6, set())
    res['score_best_above_D_fails'] = 'best above the census maximum' in kinds(case(s0), s0 - 2, set())
    res['score_claimed_D_without_membership_fails'] = kinds(case(s0), s0, set()) == ['candidate at D outside the census maximizer set', 'claimed D outside the census maximizer set']
    res['score_maximizer_with_other_death_fails'] = 'census maximizer recorded with a different death' in kinds(case(s0), s0 + 2, {i0})
    res['score_truncated_near_record_fails'] = 'near-candidate record truncated' in kinds(case(s0, pruned=s0), s0 + 4, set())
    with tempfile.TemporaryDirectory() as tmp:
        # --- census validation
        good = {'complete': True, 'scope': {'W': 64, 'T': 256}, 'checks': {'a': {'pass': True}},
                'census': {'lanes': 1 << 32, 'censored': 0, 'max': 116, 'max_count': 2, 'maximizers': ['5', '9'], 'maximizer_list_complete': True,
                           'histogram': {'60': (1 << 32) - 2, '116': 2}}}

        def census_ok(mut):
            g = copy.deepcopy(good); mut(g); p = os.path.join(tmp, 'census.json'); atomic_json(p, g)
            try:
                load_census(64, p, want=None); return True
            except Stop:
                return False
        res['census_fake_valid_accepted'] = census_ok(lambda g: None)
        res['census_censored_refused'] = not census_ok(lambda g: g['census'].update(censored=1))
        res['census_incomplete_maximizer_list_refused'] = not census_ok(lambda g: g['census'].update(maximizer_list_complete=False))
        res['census_wrong_width_refused'] = not census_ok(lambda g: g['scope'].update(W=66))
        res['census_count_mismatch_refused'] = not census_ok(lambda g: g['census'].update(maximizers=['5']))
        res['census_failed_check_refused'] = not census_ok(lambda g: g['checks'].update(b={'pass': False}))
        p = os.path.join(tmp, 'census.json'); atomic_json(p, good)
        res['census_unpinned_digest_refused'] = _raises(lambda: load_census(64, p), Stop)
        # --- S0 receipt validation
        rc = {'complete': True, 'harness_sha256': W1A_SHA256, 's0': {'this_sha256': S0_SHA256, 'swift_sha256': SWIFT_SHA256, 'metal_sha256': METAL_SHA256,
                                                                    'p1_helper_sha256': P1_HELPER_SHA256, 'w1a_sha256': W1A_SHA256},
              'steps': [{'step': 'preflight', 'verdict': 'pass'}, {'step': 's0_serve_controls', 'verdict': 'pass', 'proof_verdict': 'pass', 'final_problems': []}]}
        sr = {'complete': True, 'this_sha256': S0_SHA256, 'checks': {k: {'pass': True} for k in S0.REQUIRED}, 'live_servers_at_finally': 0, 'build': {'binary_sha256': 'b'}}

        def receipt_problems(mr=None, ms=None, want=(None, None)):
            r, s = copy.deepcopy(rc), copy.deepcopy(sr)
            if mr: mr(r)
            if ms: ms(s)
            d = os.path.join(tmp, 's0'); os.makedirs(os.path.join(d, 'run'), exist_ok=True)
            atomic_json(os.path.join(d, 'receipts.json'), r); atomic_json(os.path.join(d, 'run', 's0_result.json'), s)
            return check_s0_receipt(d, want)[0]
        res['s0_receipt_fake_good_accepted'] = receipt_problems() == []
        res['s0_receipt_wrong_s0_digest_refused'] = receipt_problems(mr=lambda r: r['s0'].update(this_sha256='0' * 64)) != []
        res['s0_receipt_failed_step_refused'] = receipt_problems(mr=lambda r: r['steps'][1].update(verdict='UNKNOWN')) != []
        res['s0_receipt_missing_check_refused'] = receipt_problems(ms=lambda s: s['checks'].pop(S0.REQUIRED[-1])) != []
        res['s0_receipt_live_server_refused'] = receipt_problems(ms=lambda s: s.update(live_servers_at_finally=1)) != []
        res['s0_receipt_unpinned_files_refused'] = receipt_problems(want=(S0_RECEIPT_SHA256, S0_RESULT_SHA256)) != []
        # --- fix 5: the terminal gate
        cases = []
        for W in WIDTHS:
            for m in METHODS.values():
                for s in SEEDS:
                    g = PER_CASE if m in ('random', 'cem') else BEAM_COST[W] if m.startswith('beam') else PER_CASE - 5
                    cases.append({'W': W, 'method': m, 'seed': s, 'budget': PER_CASE, 'gross': g, 'unused': PER_CASE - g, 'unique': g // 2, 'requests': 10,
                                  'best': 100, 'first_reach_ordered': 3, 'first_reach_batch_end_gross': 10, 'censor': None})
        dgood = {'complete': True, 'failures': [], 'censor_event': None, 'interrupted_case': None, 'live_servers_at_finally': 0, 's0_receipt_ok': True,
                 'census_rehash_ok': True, 'cases': cases, 'scored': [{'W': c['W'], 'method': c['method'], 'seed': c['seed']} for c in cases]}

        def gate_verdict(mut):
            d = copy.deepcopy(dgood); mut(d); return gate(d)[0]
        res['gate_good_synthetic_passes'] = gate_verdict(lambda d: None) == 'pass'
        res['gate_missing_case_fails'] = gate_verdict(lambda d: d['cases'].pop()) == 'FAIL'
        res['gate_duplicate_case_fails'] = gate_verdict(lambda d: d['cases'].__setitem__(0, copy.deepcopy(d['cases'][1]))) == 'FAIL'
        res['gate_budget_invariant_fails'] = gate_verdict(lambda d: d['cases'][0].update(unused=1)) == 'FAIL'
        res['gate_beam_cost_fails'] = gate_verdict(lambda d: [c.update(gross=c['gross'] - 1, unused=c['unused'] + 1) for c in d['cases'] if c['method'] == 'beam_deep'][:1]) == 'FAIL'
        res['gate_float_count_fails'] = gate_verdict(lambda d: d['cases'][0].update(best=100.0)) == 'FAIL'
        res['gate_correctness_failure_fails'] = gate_verdict(lambda d: d.update(failures=[{'kind': 'x'}])) == 'FAIL'
        res['gate_censor_event_fails'] = gate_verdict(lambda d: d.update(censor_event={'request': 1})) == 'FAIL'
        res['gate_incomplete_fails'] = gate_verdict(lambda d: d.update(complete=False)) == 'FAIL'
        res['gate_live_server_fails'] = gate_verdict(lambda d: d.update(live_servers_at_finally=1)) == 'FAIL'
        res['gate_missing_scored_row_fails'] = gate_verdict(lambda d: d['scored'].pop()) == 'FAIL'
        # --- fix 4: the evaluator path against S0's protocol stubs
        def stub_server(code, name, *args):
            p = os.path.join(tmp, name + '.py'); open(p, 'w').write(code)
            return S0.Server([sys.executable, p] + list(args), os.path.join(tmp, name + '.err'))
        srv = stub_server(S0.STUBS['slow_sink'], 'slow_sink'); r = None
        try:
            r = make_evaluator(srv, 12, 48)([5])
        except Stop:
            pass
        res['evaluator_valid_response_passes'] = r == [12]; srv.close()
        srv = stub_server(S0.STUBS['trailing'], 'trailing'); res['evaluator_trailing_bytes_stop'] = _raises(lambda: make_evaluator(srv, 12, 48)([5]), Stop); srv.close()
        srv = stub_server(S0.STUBS['malformed'], 'malformed'); res['evaluator_malformed_stops'] = _raises(lambda: make_evaluator(srv, 12, 48)([5]), Stop); srv.close()
        srv = stub_server(S0.STUBS['bool_echo'], 'bool_echo'); res['evaluator_bool_echo_stops'] = _raises(lambda: make_evaluator(srv, 12, 48)([5]), Stop); srv.close()
        eof = "import os,sys\nos.read(0,1<<20)\nsys.stdout.write('{\"id\": 1, \"W\": 12, \"T\": 48, \"deaths\": [12]}\\n'); sys.stdout.flush()\n"
        srv = stub_server(eof, 'eof'); srv.exchange(b'{"id": 1, "W": 12, "T": 48, "indices": ["5"]}\n'); srv.p.wait(timeout=5)
        res['poll_quiet_sees_end_of_stream'] = poll_quiet(srv) == 'eof'; srv.close()
        # --- end to end: the real search loop through S0's transport against a stub server, small budget
        small, small_beam = 3000, {64: 1440, 72: 1280}

        def e2e(mode, n_at):
            out = tempfile.mkdtemp(dir=tmp); R = {'cases': []}
            save = lambda: atomic_json(os.path.join(out, 'p2_result.json'), R)
            server_for = lambda W: stub_server(STUB_SERVER, 'stub_%s' % mode, mode, str(n_at))
            try:
                guarded_search(out, R, save, server_for, budget=small); err = None
            except Exception as e:
                err = e
            nprog = sum(1 for _ in open(os.path.join(out, 'p2_progress.jsonl')))
            return R, err, nprog, out
        R, err, nprog, out = e2e('ok', 0)
        files_ok = all(P.digest(os.path.join(out, c['case_file'])) == c['case_sha256'] for c in R['cases'])
        res['e2e_clean_run_passes_case_gate'] = (err is None and gate_cases(R['cases'], small, small_beam) == [] and nprog == sum(c['requests'] for c in R['cases'])
                                                 and files_ok and R['live_servers_at_finally'] == 0 and not S0.LIVE)
        n64 = sum(c['requests'] for c in R['cases'] if c['W'] == 64)
        R, err, nprog, out = e2e('tail', 1)
        res['e2e_delayed_partial_tail_fails_next_exchange'] = (isinstance(err, Stop) and 'transport' in str(err) and len(R['cases']) == 1
                                                               and (R.get('interrupted_case') or {}).get('seed') == 2 and not S0.LIVE)
        R, err, nprog, out = e2e('extra', 1)
        res['e2e_delayed_extra_line_fails_identity'] = isinstance(err, Stop) and 'contract' in str(err) and len(R['cases']) == 1 and not S0.LIVE
        R, err, nprog, out = e2e('tail', n64)
        res['e2e_final_tail_fails_close_check'] = (isinstance(err, Stop) and 'before closing' in str(err) and len(R['cases']) == 25
                                                   and R.get('interrupted_case') is None and not S0.LIVE)
        R, err, nprog, out = e2e('censor', 5)
        ic = R.get('interrupted_case') or {}
        res['e2e_censor_stops_retained_and_closed'] = (isinstance(err, Censored) and len(R['cases']) == 4 and ic.get('method') == 'random' and ic.get('seed') == 5
                                                       and ic.get('gross') == small and nprog == 5 and os.path.exists(os.path.join(out, 'censor_event.json'))
                                                       and len(R['censor_event']['indices']) == small and R['censor_event']['deaths'][0] == -1
                                                       and R['live_servers_at_finally'] == 1 and R['live_servers_closed_dead'] == [True] and not S0.LIVE)
        R, err, nprog, out = e2e('die', 3)
        ic = R.get('interrupted_case') or {}
        res['e2e_dead_server_stops_saved_and_closed'] = (isinstance(err, Stop) and 'transport' in str(err) and len(R['cases']) == 2 and ic.get('seed') == 3
                                                         and ic.get('gross') == 0 and R.get('failure', {}).get('type') == 'Stop' and nprog == 2 and not S0.LIVE)
    ok = all(res.values()); print(json.dumps(res, indent=1)); print('P2 CONTROLS', 'PASS' if ok else 'FAIL', len(res)); return ok


def run(out, s0_dir, census_paths):
    t0 = time.monotonic(); os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': P.digest(os.path.abspath(__file__)), 'cases': [], 'complete': False}

    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 1); atomic_json(os.path.join(out, 'p2_result.json'), R, indent=1)

    def failed(e):
        R['complete'] = False
        R.setdefault('failure', {'type': type(e).__name__, 'message': str(e)[:1000], 'traceback': traceback.format_exc()[-3000:]}); save()
    try:
        pins = {'metal': (P.digest(P.METAL), METAL_SHA256), 'swift': (P.digest(P.SWIFT), SWIFT_SHA256),
                'p1_helper': (P.digest(P.__file__), P1_HELPER_SHA256), 's0': (P.digest(S0.__file__), S0_SHA256)}
        R['pins'] = {k: v[0] for k, v in pins.items()}
        bad = [k for k, (a, b) in pins.items() if a != b]
        if bad: raise Stop('not the pinned bytes: %s' % bad)
        probs, dig = check_s0_receipt(s0_dir); R['s0_receipt'] = dig
        if probs: raise Stop('S0 receipt: %s' % probs)
        R['s0_receipt_ok'] = True
        R['census_sha256_before'] = {str(W): P.digest(p) for W, p in census_paths.items()}
        if any(R['census_sha256_before'].get(str(W)) != CENSUS_SHA256[W] for W in WIDTHS): raise Stop('the census files are not the pinned bytes')
        eng = P.Engine(out); R['build'] = eng.build(); save()
        if R['build'].get('binary_sha256') != dig['binary_sha256']: raise Stop('the built binary differs from the one S0 passed')
    except BaseException as e:
        failed(e); raise
    guarded_search(out, R, save, lambda W: S0.Server.engine(eng, out))
    try:
        after = {str(W): P.digest(p) for W, p in census_paths.items()}
        R['census_sha256_after'] = after; R['census_rehash_ok'] = after == R['census_sha256_before']
        if not R['census_rehash_ok']: raise Stop('the census bytes changed during the search')
        census = {}
        for W, pth in census_paths.items():
            D, mx, _ = load_census(W, pth); census[W] = (D, mx)
        full = []
        for c in R['cases']:
            cp = os.path.join(out, c['case_file'])
            if P.digest(cp) != c['case_sha256']: raise Stop('case file %s changed' % c['case_file'])
            full.append(json.load(open(cp)))
        R['scored'], R['summary'], R['failures'] = score(full, census); save()
        if R['failures']: raise Stop('%d correctness failures (saved in the result)' % len(R['failures']))
        R['complete'] = True; v, probs = gate(R); R['gate'] = {'verdict': v, 'problems': probs}
        if v != 'pass': raise Stop('terminal gate: %s' % probs[:5])
        R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
        return R
    except BaseException as e:
        failed(e); raise


def inputs(s0_dir, census_paths):
    """Validates the S0 binding and the census inputs only (no engine, no search)."""
    probs, dig = check_s0_receipt(s0_dir); out = {'s0_problems': probs, 's0_digests': dig, 'census': {}}
    for W, p in census_paths.items():
        try:
            D, mx, dg = load_census(W, p); out['census'][str(W)] = {'ok': True, 'D': D, 'maximizers': len(mx), 'sha256': dg}
        except Stop as e:
            out['census'][str(W)] = {'ok': False, 'why': str(e)}
    ok = not probs and all(v['ok'] for v in out['census'].values())
    print(json.dumps(out, indent=1)); print('P2 INPUTS', 'PASS' if ok else 'FAIL'); return ok


def stage(out, s0_dir, census_paths):
    import w1a_harness as H
    if P.digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    probs, dig = check_s0_receipt(s0_dir)
    if probs:
        print('REFUSED: S0 receipt', probs); return 3
    try:
        cen = {str(W): load_census(W, p)[2] for W, p in census_paths.items()}       # the supervising process, not the search process
    except Stop as e:
        print('REFUSED:', e); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 200 << 20; H.CAPS['log_max_bytes'] = 20 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['p2'] = {'this_sha256': P.digest(os.path.abspath(__file__)), 'metal_sha256': METAL_SHA256, 'swift_sha256': SWIFT_SHA256, 'p1_helper_sha256': P1_HELPER_SHA256,
                's0_sha256': S0_SHA256, 'w1a_sha256': W1A_SHA256, 's0_receipt': dig, 'census_sha256': cen, 'per_case_budget': PER_CASE,
                'cases': len(expected_cases()), 'high_cap': HIGH_CAP, 'nice_inherited': os.nice(0),
                'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 6 << 30, 'artifacts_max_bytes': 200 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(rdir, 'p2_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        v, probs = gate(d)
        if rc != 0 or v != 'pass':
            return 'FAIL', 'rc %s gate %s %s' % (rc, v, probs[:5])
        return 'pass', 'P2 complete: the terminal gate passes on exactly %d cases' % len(d['cases'])
    cmd = [sys.executable, os.path.abspath(__file__), 'run', rdir, s0_dir, census_paths[64], census_paths[72]]
    rec = sup.run_step('p2_search', cmd, out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(a) == 4 and a[0] == 'inputs':
        sys.exit(0 if inputs(a[1], {64: a[2], 72: a[3]}) else 1)
    if len(a) == 5 and a[0] in ('run', 'stage'):
        cp = {64: a[3], 72: a[4]}
        if a[0] == 'stage':
            sys.exit(stage(a[1], a[2], cp))
        try:
            R = run(a[1], a[2], cp); print('P2 COMPLETE', len(R['scored']), 'cases'); sys.exit(0)
        except (Stop, P.Stop, RuntimeError) as e:
            print('P2 STOPPED:', e); sys.exit(1)
    print(__doc__); sys.exit(2)
