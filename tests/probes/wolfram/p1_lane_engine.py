#!/usr/bin/env python3
"""P1, revision 2 (Local, 2026-10-24; revision 1 passed as run p1-pilot-20261024-1330, L863; revision 2 adds the GPU-side
reduction to the engine and the control R below): the exact lane engine for Q01 death times on the M5's GPU (GPU-METAL-JOBS.md §J.1
revision 2, with GPT's GC1775/GC1776 corrections and the owner's memory clarification GC1777). The engine is
`p1_engine/lanes.metal` (two compute kernels: `build_start`, the kit's trace reconstruction; `simulate`, the forward
evolution with even-time death detection) driven by `p1_engine/main.swift` (built with swiftc at run time into the output
folder; the Metal source is compiled by the driver at run time). This harness builds it, runs the controls against
independent scalar code, measures throughput on one batch validated lane by lane against the exact CPU engine
(d1_engine, the kit's lane check), and writes one result JSON. Nothing runs on import.

Mathematics (checked on the CPU before any GPU code was written, L863): index bit i is the odd trace bit a(2i+1) (depth 1
at time 2i+1), the even trace bits are 1; the class of starts of width <= W surviving every even time < W is in bijection
with the floor(W/2) index bits (round trip verified W = 2..16); every maximizer of D(W) lies in the class (verified
W = 2..16); L(2) = not f(0). The kit's lane engine (d1_engine.run_lanes, one chunk n = W/2) uses the SAME convention,
lane for lane: its lane p reconstructs to recon(W, p) and its elimination level equals the physical death (verified at
W = 16, 20, 24, every lane); chunk c, lane p of n bits is index (c << n) | p.

Controls (all must pass; the first failure stops the pilot):
  C0  hand fixture: the literal index-to-start tables at W = 4 and 6 (computed once by forward simulation only and written
      here as constants) equal the reconstruction, and the GPU's deaths on them equal the scalar engine's.
  C1  exhaustive W = 10..14 (both parities), both lane widths: the GPU class census against a brute-force scalar census of
      all 2^W starts: equal D(W), equal maximizer starts, class size 2^floor(W/2), every lane's death equal to the scalar.
  C2  frozen fixtures: the known maximizers at 52, 56, 60 (d = 96, 100, 114) reproduced; a seeded sample of 256 lanes in
      each of chunks 0 and last at each width, with their exact levels from d1_engine, reproduced (an evaluator check on
      known inputs, not a census and not a statement about multiplicities); 32 of them re-simulated by the scalar engine.
  C3  edge cases: the zero start (d = 0); the singleton (d = 2); starts with their last black cell at depth W, compared cell
      by cell for ten steps (the whole row, the wall and the halo included) against the scalar engine; the censoring logic
      by a stripe halo (the reconstructed eternal trace on initial depths 1..T+1, censored at T; recorded as a test of
      censoring, not as an infinite support); the truncated stripe in the class; death exactly at T and censoring at T-2;
      census ranges whose first and last groups are partial, crossing lane positions 31/32 and 63/64; odd width 21.
  C4  Sparse16 (negative control, exact statement): every lane alive at all even times 0..110 has an initial row with at
      least 17 black cells among depths 1..111; a violation is an engine bug.
  C5  two engines: every census batch's 64 sampled lanes re-simulated by the scalar engine; one disagreement stops.
  R   the GPU reduction (revision 2: a threadgroup histogram with one atomic add per death event, per-group maxima, the
      maximizers found from the groups whose maximum attains) equals the CPU reduction (revision 1's per-lane loop) on every
      C1 census and on the W = 60 measurement batch: histogram, maximum, its count, censored lanes, lanes, maximizer set.
  N   the mutant (compile-time MUTANT_DROP_EDGE, the first draft's bug: the new edge cell not computed) must be DETECTED by
      the C3 edge trace and by a C1 census; a mutant that passes means the controls are blind, and the pilot fails.
Measurement (not a census): one batch at W = 60, T = 240, lanes [0, 2^24) (d1 chunks 0..63), on 32-lane words (G = 2^19)
and on 64-lane words (G = 2^18), every lane's death compared with d1's exact level; prep, build, simulate (GPU time and
wall) and reduce reported separately, with the GPU and the CPU reduction, and a dump-free timing run (the engine as a census would
run it); a short threadgroup-size comparison on [0, 2^22);
and d1 on the same 64 chunks across 10 worker processes (the CPU engine on all cores) for the comparison. Only timing and
agreement counts are reported from these runs: no maximum, histogram or multiplicity claim.

Caps (§J.1 revision 2): GPU budget 2 GiB (enforced by the driver from the live allocations); process-group RSS stop 6 GiB,
pressure, swap growth 256 MiB (the W1A supervisor in `stage`); 120 s per engine call; pilot wall <= 1,800 s; outputs <=
100 MB (death dumps are compared and deleted, their digests kept); no census above width 14; nothing else on the M5.

Usage: python3 p1_lane_engine.py --controls        (CPU-only self-tests of this harness: seconds)
       python3 p1_lane_engine.py pilot OUT_DIR      (the pilot, unsupervised: development)
       python3 p1_lane_engine.py stage OUT_DIR      (the pilot as one step under the W1A supervisor: the agreed run)
OUTCOME, revision 2 (run p1r2-pilot-20261024-1335 under the W1A supervisor, at this file ad548e35..., lanes.metal 17a81e66...,
main.swift 8649a598..., binary 4bdc578e...; this docstring is the only change since): PASS, 71 of 71 checks, step wall 9.37 s,
group RSS peak 1.0 GB (the ten-worker d1 pool), clean cleanup. Every revision-1 control passes again (N: 1,875 cell and 5 lane
mismatches for the mutant; C4: 1,584 lanes, no violation; C5: 1,063 samples); R: the GPU reduction equals the CPU reduction
on all ten C1 censuses and on both W = 60 batches (14 checks). Measurement (not a census), W = 60, T = 240, lanes [0, 2^24):
every lane equals d1's exact level on both lane widths; dump-free timing run: build 0.058 s + simulate 0.126 s GPU, reduce
0.002 s, engine wall 0.212 s = 79 M lanes/s end to end (64-lane words 80 M); with revision 1's CPU reduction 0.47 s.
d1 on all ten cores: 22.8 M lanes/s on the same lanes (0.74 s wall including pool start-up; 5.7 s of chunk work). The GPU
engine is about 3.5x the whole CPU at W = 60 end to end.

OUTCOME, revision 1 (run p1-pilot-20261024-1330, at 0b24a5ba..., lanes.metal f6d598a3..., main.swift 9645f6df...): PASS, 57 of
57 checks; GPU kernels 89 M lanes/s, end to end 27 M lanes/s with the CPU reduction (0.40 s per 2^24 lanes)."""
import hashlib, json, os, random, shutil, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d1_engine as E

ENGINE_DIR = os.path.join(HERE, 'p1_engine')
METAL = os.path.join(ENGINE_DIR, 'lanes.metal')
SWIFT = os.path.join(ENGINE_DIR, 'main.swift')
D1_SHA256 = 'e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
CALL_TIMEOUT_S = 120
GPU_BUDGET = 2 << 30
CENS = 0xFFFF

HAND_FIXTURE = {   # index -> start (depth j+1 = bit j), from forward simulation only (L863); literal
    4: {0: 0b1011, 1: 0b1101, 2: 0b11, 3: 0b101},
    6: {0: 0b101011, 1: 0b11101, 2: 0b11, 3: 0b110101, 4: 0b1011, 5: 0b111101, 6: 0b100011, 7: 0b10101},
}
WITNESSES = {52: (0x7dc2ff6fcc4fd, 96), 56: (0x93d4b223f5b9b5, 100), 60: (0xe77a4e77b8f99b5, 114)}


# ---- the scalar reference (independent of the GPU code) --------------------------------------------------------------

def pstep(r):
    return (r >> 1) ^ (r | (r << 1))


def death(r, T):
    """First even t <= T with depth 1 white, or -1 (censored, d > T)."""
    for t in range(T + 1):
        if t % 2 == 0 and (r & 1) == 0:
            return t
        r = pstep(r)
    return -1


def trace_bits(r, n):
    out = []
    for _ in range(n):
        out.append(r & 1); r = pstep(r)
    return out


def recon(W, idx):
    """The start of width <= W whose depth-1 trace is a(even) = 1, a(2i+1) = bit i of idx, for t < W."""
    col1 = 0
    for t in range(W):
        col1 |= (1 if t % 2 == 0 else (idx >> ((t - 1) // 2)) & 1) << t
    prev, cur = 0, col1
    r = cur & 1
    for k in range(1, W):
        nxt = ((cur >> 1) ^ (cur | prev)) & ((1 << (W - k)) - 1)
        r |= (nxt & 1) << k
        prev, cur = cur, nxt
    return r


def index_of(W, r):
    a = trace_bits(r, W); idx = 0
    for i in range(W // 2):
        idx |= a[2 * i + 1] << i
    return idx


def sparse16_ok(start, d, T):
    """False only for a lane alive at all even t <= 110 whose initial row has fewer than 17 black cells in depths 1..111."""
    alive_110 = (d > 110) or (d == -1 and T >= 110)
    return (not alive_110) or bin(start & ((1 << 111) - 1)).count('1') >= 17


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def d1_levels(W, c, K, n=18):
    """Exact levels of the 2^n lanes of d1 chunk c (index (c << n) | p), as a list (-1 never: all must die by K)."""
    import numpy as np
    alive, elim, _ = E.run_lanes(W, n, c, K, record=True)
    if alive != 0:
        raise RuntimeError('d1 chunk %d at W=%d not all dead by K=%d' % (c, W, K))
    N = 1 << n; lv = np.full(N, -1, dtype=np.int32)
    for k, m in elim.items():
        bits = np.unpackbits(np.frombuffer(m.to_bytes(N // 8, 'little'), dtype=np.uint8), bitorder='little')[:N].astype(bool)
        lv[bits] = k
    if (lv < 0).any():
        raise RuntimeError('a d1 lane without a level')
    return lv


# ---- the engine --------------------------------------------------------------------------------------------------------

class Engine:
    def __init__(self, out):
        self.out = out; self.bin = os.path.join(out, 'bin', 'p1engine'); self.calls = 0; self.log = []
        os.makedirs(os.path.dirname(self.bin), exist_ok=True)

    def build(self):
        t = time.monotonic()
        r = subprocess.run(['swiftc', '-O', '-o', self.bin, SWIFT], capture_output=True, text=True, timeout=600)
        if r.returncode != 0:
            raise RuntimeError('swiftc failed: ' + r.stderr[-2000:])
        v = subprocess.run(['swiftc', '--version'], capture_output=True, text=True).stdout.strip().splitlines()[0]
        return {'swift_sha256': digest(SWIFT), 'metal_sha256': digest(METAL), 'binary_sha256': digest(self.bin),
                'swiftc': v, 'build_s': round(time.monotonic() - t, 2)}

    def run(self, job, name):
        self.calls += 1
        jp = os.path.join(self.out, 'jobs', '%03d_%s.json' % (self.calls, name)); op = jp.replace('.json', '.out.json')
        os.makedirs(os.path.dirname(jp), exist_ok=True)
        job = dict(job); job.setdefault('metal', METAL); job.setdefault('gpu_budget_bytes', GPU_BUDGET)
        json.dump(job, open(jp, 'w'))
        t = time.monotonic()
        try:
            r = subprocess.run([self.bin, jp, op], capture_output=True, text=True, timeout=CALL_TIMEOUT_S)
        except subprocess.TimeoutExpired:
            raise RuntimeError('engine call %s exceeded %d s' % (name, CALL_TIMEOUT_S))
        wall = time.monotonic() - t
        if r.returncode != 0 or not os.path.exists(op):
            raise RuntimeError('engine call %s failed rc=%d: %s' % (name, r.returncode, r.stderr[-1000:]))
        res = json.load(open(op))
        if res.get('status') != 'ok':
            raise RuntimeError('engine call %s status %s' % (name, res.get('status')))
        self.log.append({'name': name, 'wall_s': round(wall, 3), 'lanes': res.get('lanes_total')})
        return res


def read_dump(path):
    import numpy as np
    a = np.fromfile(path, dtype='<u2').astype(np.int32)
    a[a == CENS] = -1
    return a


# ---- the pilot -----------------------------------------------------------------------------------------------------------

class Stop(Exception):
    pass


def same_reduction(a, b):
    return all(a[k] == b[k] for k in ('histogram', 'max', 'max_count', 'censored', 'lanes_total')) and sorted(a['maximizers']) == sorted(b['maximizers'])


def _d1_chunk(args):
    W, c, K = args
    t = time.perf_counter(); E.run_lanes(W, 18, c, K, record=True); return time.perf_counter() - t


def pilot(out):
    import numpy as np
    t_start = time.monotonic()
    os.makedirs(out, exist_ok=True)
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': digest(os.path.abspath(__file__)), 'd1_sha256': digest(E.__file__),
         'checks': {}, 'measurement': {}, 'sparse16_lanes_checked': 0, 'two_engine_samples': 0}
    if R['d1_sha256'] != D1_SHA256:
        raise Stop('d1_engine is not the pinned bytes')
    eng = Engine(out)
    R['build'] = eng.build()
    sparse = []           # (start, death, T)

    def save():
        R['elapsed_s'] = round(time.monotonic() - t_start, 1); R['engine_calls'] = eng.log
        tmp = os.path.join(out, 'p1_result.json.tmp'); json.dump(R, open(tmp, 'w'), indent=1); os.replace(tmp, os.path.join(out, 'p1_result.json'))

    def check(name, ok, **detail):
        R['checks'][name] = {'pass': bool(ok), **detail}; save()
        if not ok:
            raise Stop('control failed: %s %s' % (name, json.dumps(detail)[:500]))

    def two_engine(res, W, T):
        bad = []
        for b in res['batches']:
            for n, d in b['samples']:
                n, d = int(n), int(d); s = recon(W, n); R['two_engine_samples'] += 1
                if death(s, T) != d: bad.append((n, d, death(s, T)))
                sparse.append((s, d, T))
        return bad

    R['device'] = None
    # C0 hand fixture
    for W, tab in HAND_FIXTURE.items():
        check('C0_recon_W%d' % W, all(recon(W, i) == s for i, s in tab.items()))
        for LB in (32, 64):
            res = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': 4 * W, 'indices': [str(i) for i in tab]}, 'C0_W%d_L%d' % (W, LB))
            R['device'] = R['device'] or {'device': res['device'], 'pipeline': res['pipeline']}
            got = {int(x['index']): x['death'] for x in res['deaths']}
            check('C0_gpu_W%d_L%d' % (W, LB), all(got[i] == death(s, 4 * W) for i, s in tab.items()), got=got)
    check('C0_L2_is_not_f0', all(((recon(6, i) >> 1) & 1) == 1 - (i & 1) for i in range(8)))

    # C1 exhaustive tiny widths against brute force over all 2^W starts
    for W in range(10, 15):
        T = 4 * W; nb = W // 2
        bf = {r: death(r, T) for r in range(1 << W)}
        D = max(bf.values()); bf_max = sorted(r for r, d in bf.items() if d == D)
        cls = sorted(r for r in range(1 << W) if all(x for x in trace_bits(r, W)[0::2]))
        check('C1_bijection_W%d' % W, len(cls) == (1 << nb) and sorted(index_of(W, r) for r in cls) == list(range(1 << nb)))
        for LB in (32, 64):
            dp = os.path.join(out, 'dump_C1.u16')
            res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << nb), 'deaths_out': dp}, 'C1_W%d_L%d' % (W, LB))
            rc = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << nb), 'reduce': 'cpu'}, 'C1_W%d_L%d_cpu_reduce' % (W, LB))
            check('R_C1_W%d_L%d' % (W, LB), res['reduce'] == 'gpu' and rc['reduce'] == 'cpu' and same_reduction(res, rc))
            dump = read_dump(dp); os.remove(dp)
            lane_ok = len(dump) == (1 << nb) and all(int(dump[n]) == bf[recon(W, n)] for n in range(1 << nb))
            gpu_max = sorted(recon(W, int(x)) for x in res['maximizers'])
            bad = two_engine(res, W, T)
            check('C1_W%d_L%d' % (W, LB), lane_ok and res['max'] == D and gpu_max == bf_max and res['lanes_total'] == (1 << nb)
                  and res['censored'] == 0 and not bad, D=D, gpu_max=res['max'], maximizers=[hex(x) for x in bf_max], lanes=res['lanes_total'])
            for n in range(1 << nb):
                sparse.append((recon(W, n), int(dump[n]), T))

    # C2 frozen fixtures at 52, 56, 60
    for W, (r, d) in WITNESSES.items():
        idx = index_of(W, r)
        check('C2_witness_roundtrip_W%d' % W, recon(W, idx) == r and death(r, 4 * W) == d, index=hex(idx))
        rng = random.Random(1000003 * W)
        K = d + 1; last = (1 << (W // 2 - 18)) - 1
        sample = {}
        for c in (0, last):
            lv = d1_levels(W, c, K)
            for p in rng.sample(range(1 << 18), 256):
                sample[(c << 18) | p] = int(lv[p])
        fx = {'W': W, 'K': K, 'witness_index': str(idx), 'witness_death': d, 'sample': {str(k): v for k, v in sorted(sample.items())}}
        fp = os.path.join(out, 'fixture_W%d.json' % W); json.dump(fx, open(fp, 'w'))
        R['checks'].setdefault('fixture_digests', {})['W%d' % W] = digest(fp)
        idxs = [idx] + sorted(sample)
        for LB in (32, 64):
            res = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': 4 * W, 'indices': [str(i) for i in idxs]}, 'C2_W%d_L%d' % (W, LB))
            got = {int(x['index']): x['death'] for x in res['deaths']}
            ok = got[idx] == d and all(got[i] == v for i, v in sample.items())
            check('C2_W%d_L%d' % (W, LB), ok, witness=got[idx], sample_mismatches=sum(1 for i, v in sample.items() if got[i] != v))
        resim = sorted(sample)[:32]
        check('C2_scalar_resim_W%d' % W, all(death(recon(W, i), 4 * W) == sample[i] for i in resim))
        sparse.append((r, d, 4 * W))
        for i in resim:
            sparse.append((recon(W, i), sample[i], 4 * W))

    # C3 edge cases
    for LB in (32, 64):
        res = eng.run({'lane_bits': LB, 'mode': 'rows', 'T': 16, 'Wsup': 8, 'starts': ['0', '1']}, 'C3_zero_singleton_L%d' % LB)
        check('C3_zero_singleton_L%d' % LB, res['deaths'] == [0, 2], deaths=res['deaths'])

    def edge_trace(LB, mutant=''):
        W = 20; T = 40; steps = 10; rng = random.Random(77 + LB)
        starts = [(1 << (W - 1)) | rng.getrandbits(W - 1) for _ in range(LB)]
        job = {'lane_bits': LB, 'mode': 'rows', 'T': T, 'Wsup': W, 'starts': [hex(s) for s in starts], 'trace_steps': steps}
        if mutant: job['mutant'] = mutant
        res = eng.run(job, 'C3_edge_trace_L%d%s' % (LB, '_' + mutant if mutant else ''))
        L = res['L']; mism = 0
        for t in range(steps + 1):
            rows = [int(h, 16) for h in res['trace'][t]]
            for l, s in enumerate(starts):
                st = s
                for _ in range(t): st = pstep(st)
                for k in range(L):
                    want = 0 if k == 0 else (st >> (k - 1)) & 1
                    if ((rows[k] >> l) & 1) != want: mism += 1
        dmis = sum(1 for l, s in enumerate(starts) if res['deaths'][l] != death(s, T))
        return mism, dmis, starts, res, T

    for LB in (32, 64):
        mism, dmis, starts, res, T = edge_trace(LB)
        check('C3_edge_trace_L%d' % LB, mism == 0 and dmis == 0, cell_mismatches=mism, death_mismatches=dmis)
        sparse.extend((s, res['deaths'][l], T) for l, s in enumerate(starts))

    T = 120
    halo = [recon(T + 1, f) for f in (0, int('01' * 30, 2), (1 << 60) - 1)]
    check('C3_halo_scalar_alive', all(death(s, T) == -1 for s in halo))
    for LB in (32, 64):
        res = eng.run({'lane_bits': LB, 'mode': 'rows', 'T': T, 'Wsup': T + 1, 'starts': [hex(s) for s in halo]}, 'C3_halo_L%d' % LB)
        check('C3_halo_censored_L%d' % LB, res['deaths'] == [-1, -1, -1] and res['censored'] == 3, deaths=res['deaths'])
        sparse.extend((s, -1, T) for s in halo)

    W = 24; stripe = [0, int('01' * 6, 2), int('10' * 6, 2), (1 << 12) - 1]
    for LB in (32, 64):
        res = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': 4 * W, 'indices': [str(i) for i in stripe]}, 'C3_truncated_stripe_L%d' % LB)
        got = {int(x['index']): x['death'] for x in res['deaths']}
        check('C3_truncated_stripe_L%d' % LB, all(got[i] == death(recon(W, i), 4 * W) for i in stripe), got=got)

    i60 = index_of(60, WITNESSES[60][0]); i12 = index_of(12, 0x5d5)
    for (W, idx, d) in ((60, i60, 114), (12, i12, 30)):
        for LB in (32, 64):
            a = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': d, 'indices': [str(idx)]}, 'C3_at_T_W%d_L%d' % (W, LB))
            b = eng.run({'lane_bits': LB, 'mode': 'list', 'W': W, 'T': d - 2, 'indices': [str(idx)]}, 'C3_before_T_W%d_L%d' % (W, LB))
            check('C3_death_at_T_W%d_L%d' % (W, LB), a['deaths'][0]['death'] == d and b['deaths'][0]['death'] == -1 and b['censored'] == 1,
                  at_T=a['deaths'][0]['death'], at_T_minus_2=b['deaths'][0]['death'])

    for LB, (lo, hi) in ((32, (31, 97)), (64, (63, 193))):
        for W in (20, 21):
            dp = os.path.join(out, 'dump_C3.u16')
            res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': 4 * W, 'lo': str(lo), 'hi': str(hi), 'deaths_out': dp, 'G_max': 2}, 'C3_boundary_W%d_L%d' % (W, LB))
            dump = read_dump(dp); os.remove(dp)
            ok = len(dump) == hi - lo and all(int(dump[n - lo]) == death(recon(W, n), 4 * W) for n in range(lo, hi))
            bad = two_engine(res, W, 4 * W)
            check('C3_boundary_W%d_L%d' % (W, LB), ok and not bad and res['lanes_total'] == hi - lo and len(res['batches']) >= 2,
                  lanes=res['lanes_total'], batches=len(res['batches']))
    for LB in (32, 64):
        dp = os.path.join(out, 'dump_C3.u16'); W = 21
        res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': 4 * W, 'lo': '0', 'hi': str(1 << 10), 'deaths_out': dp}, 'C3_odd21_L%d' % LB)
        dump = read_dump(dp); os.remove(dp)
        check('C3_odd_W21_L%d' % LB, all(int(dump[n]) == death(recon(W, n), 4 * W) for n in range(1 << 10)) and not two_engine(res, W, 4 * W))

    # N: the mutant must be detected
    mism, dmis, _, _, _ = edge_trace(32, mutant='drop_edge')
    dp = os.path.join(out, 'dump_N.u16')
    res = eng.run({'lane_bits': 32, 'mode': 'census', 'W': 12, 'T': 48, 'lo': '0', 'hi': '64', 'deaths_out': dp, 'mutant': 'drop_edge'}, 'N_mutant_C1_W12')
    dump = read_dump(dp); os.remove(dp)
    c1_mis = sum(1 for n in range(64) if int(dump[n]) != death(recon(12, n), 48))
    check('N_mutant_detected', mism > 0 and c1_mis > 0, edge_cell_mismatches=mism, edge_death_mismatches=dmis, c1_lane_mismatches=c1_mis, c1_max=res['max'])

    # C4 Sparse16 over every lane with a known start
    R['sparse16_lanes_checked'] = len(sparse)
    viol = [(hex(s), d, T) for s, d, T in sparse if not sparse16_ok(s, d, T)]
    check('C4_sparse16', not viol, lanes=len(sparse), alive_through_110=sum(1 for s, d, T in sparse if (d > 110) or (d == -1 and T >= 110)), violations=viol[:5])

    # Measurement at W = 60 (not a census): timing, and every lane against d1's exact level
    W, T = 60, 240
    lv = np.concatenate([d1_levels(W, c, 115) for c in range(64)])
    R['measurement']['d1_reference'] = {'chunks': '0..63', 'lanes': int(len(lv))}
    for LB, G in ((32, 1 << 19), (64, 1 << 18)):
        dp = os.path.join(out, 'dump_M.u16')
        res = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << 24), 'deaths_out': dp, 'G_max': G}, 'M_W60_L%d' % LB)
        dump = read_dump(dp); dd = digest(dp); os.remove(dp)
        agree = int((dump == lv).sum()); bad = two_engine(res, W, T)
        b = res['batches'][0]
        R['measurement']['W60_L%d' % LB] = {'lanes': res['lanes_total'], 'groups': res['groups_total'], 'G_batch': res['G_batch'], 'live_bytes': res['live_bytes'],
                                            'threadgroup': res['threadgroup_sim'], 't_prep_s': b['t_prep_s'], 't_build_gpu_s': b['t_build_gpu_s'],
                                            't_build_wall_s': b['t_build_wall_s'], 't_sim_gpu_s': b['t_sim_gpu_s'], 't_sim_wall_s': b['t_sim_wall_s'],
                                            't_reduce_s': b['t_reduce_s'], 'engine_wall_s': res['wall_total_s'], 'agree_with_d1': agree, 'dump_sha256': dd}
        check('M_W60_L%d_agrees_with_d1' % LB, agree == len(lv) and not bad, agree=agree, lanes=int(len(lv)))
        rc = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << 24), 'G_max': G, 'reduce': 'cpu'}, 'M_W60_L%d_cpu_reduce' % LB)
        bc = rc['batches'][0]
        R['measurement']['W60_L%d' % LB].update({'cpu_reduce_t_reduce_s': bc['t_reduce_s'], 'cpu_reduce_engine_wall_s': rc['wall_total_s']})
        check('R_W60_L%d' % LB, same_reduction(res, rc))
        rt = eng.run({'lane_bits': LB, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << 24), 'G_max': G}, 'M_W60_L%d_timing' % LB)   # no dump: the engine as a census would run it
        bt = rt['batches'][0]
        R['measurement']['W60_L%d' % LB].update({'timing_run': {'t_build_gpu_s': bt['t_build_gpu_s'], 't_sim_gpu_s': bt['t_sim_gpu_s'], 't_reduce_s': bt['t_reduce_s'],
                                                  'engine_wall_s': rt['wall_total_s'], 'lanes_per_s': round((1 << 24) / rt['wall_total_s'])}})
        check('R_W60_L%d_timing_run_same' % LB, same_reduction(res, rt))
    import multiprocessing as mp
    t = time.perf_counter()
    with mp.get_context('spawn').Pool(10) as pool:
        per = pool.map(_d1_chunk, [(W, c, 115) for c in range(64)])
    wall = time.perf_counter() - t
    R['measurement']['d1_all_cores'] = {'workers': 10, 'chunks': 64, 'lanes': 1 << 24, 'wall_s': round(wall, 3), 'sum_chunk_s': round(sum(per), 3),
                                        'lanes_per_s': round((1 << 24) / wall), 'note': 'includes pool start-up; record=True (per-lane levels), the same output as the engine'}
    R['measurement']['threadgroup_scan'] = {}
    for tg in (64, 256, 1024):
        res = eng.run({'lane_bits': 32, 'mode': 'census', 'W': W, 'T': T, 'lo': '0', 'hi': str(1 << 22), 'G_max': 1 << 17, 'tg': tg}, 'M_tg%d' % tg)
        b = res['batches'][0]
        R['measurement']['threadgroup_scan'][str(tg)] = {'t_build_gpu_s': b['t_build_gpu_s'], 't_sim_gpu_s': b['t_sim_gpu_s'], 'two_engine_bad': len(two_engine(res, W, T))}
        if R['measurement']['threadgroup_scan'][str(tg)]['two_engine_bad']:
            raise Stop('two-engine disagreement in the threadgroup scan')
    R['complete'] = True; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


# ---- harness self-tests (CPU only) ----------------------------------------------------------------------------------------

def controls():
    res = {}
    ok = True
    for W in range(2, 13):
        cls = [r for r in range(1 << W) if all(x for x in trace_bits(r, W)[0::2])]
        ok = ok and len(cls) == (1 << (W // 2)) and all(recon(W, index_of(W, r)) == r for r in cls)
    res['recon_bijection_W2_12'] = ok
    res['hand_fixture_matches_recon'] = all(recon(W, i) == s for W, t in HAND_FIXTURE.items() for i, s in t.items())
    res['witness_deaths'] = all(death(r, 4 * W) == d for W, (r, d) in WITNESSES.items())
    res['sparse16_flags_planted_violation'] = sparse16_ok((1 << 16) - 1, 112, 240) is False and sparse16_ok((1 << 17) - 1, 112, 240) is True
    res['sparse16_ignores_early_death'] = sparse16_ok(1, 2, 240) is True
    res['censored_alive_flagged'] = sparse16_ok(1, -1, 120) is False and sparse16_ok(1, -1, 100) is True
    import numpy as np, tempfile
    p = os.path.join(tempfile.mkdtemp(), 'd.u16'); np.array([0, 2, 0xFFFF, 114], dtype='<u2').tofile(p)
    res['dump_reader'] = read_dump(p).tolist() == [0, 2, -1, 114]
    lv = d1_levels(24, 0, 43, n=12)
    res['d1_levels_match_physical_W24'] = all(int(lv[p]) == death(recon(24, p), 43) for p in range(1 << 12))
    allok = all(v is True for v in res.values())
    print(json.dumps(res, indent=1)); print('P1 HARNESS CONTROLS', 'PASS' if allok else 'FAIL', len(res)); return allok


def stage(out):
    import w1a_harness as H
    if digest(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    os.makedirs(out, exist_ok=True)
    H.CAPS['stage_s'] = 1800; H.CAPS['rss_stop_bytes'] = 6 << 30; H.CAPS['artifacts_max_bytes'] = 100 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['p1'] = {'this_sha256': digest(os.path.abspath(__file__)), 'metal_sha256': digest(METAL), 'swift_sha256': digest(SWIFT), 'd1_sha256': D1_SHA256,
                'w1a_sha256': W1A_SHA256, 'caps': {'stage_s': 1800, 'step_wall_s': 1800, 'step_cpu_s': 1800, 'group_rss_stop_bytes': 6 << 30,
                'gpu_budget_bytes': GPU_BUDGET, 'call_timeout_s': CALL_TIMEOUT_S, 'artifacts_max_bytes': 100 << 20}, 'nice_inherited': os.nice(0)}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    pdir = os.path.join(out, 'pilot')

    def matcher(rc, text):
        try:
            d = json.load(open(os.path.join(pdir, 'p1_result.json')))
        except Exception as e:
            return 'FAIL', 'no result: %r' % e
        if rc != 0 or not d.get('complete') or not all(v.get('pass') for k, v in d['checks'].items() if isinstance(v, dict) and 'pass' in v):
            return 'FAIL', 'rc %s complete %s' % (rc, d.get('complete'))
        return 'pass', 'all controls pass; %d checks; W60 L32 sim %.3f s GPU' % (len(d['checks']), d['measurement']['W60_L32']['t_sim_gpu_s'])
    rec = sup.run_step('p1_pilot', [sys.executable, os.path.abspath(__file__), 'pilot', pdir], out, 1800, 1800, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; Rc['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if controls() else 1)
    if len(a) == 2 and a[0] == 'pilot':
        try:
            R = pilot(a[1]); print('P1 PILOT COMPLETE', len(R['checks']), 'checks'); sys.exit(0)
        except Stop as e:
            print('P1 PILOT STOPPED:', e); sys.exit(1)
    if len(a) == 2 and a[0] == 'stage':
        sys.exit(stage(a[1]))
    print(__doc__); sys.exit(2)
