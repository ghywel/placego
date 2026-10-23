#!/usr/bin/env python3
"""D1, revision 1: a CPU word engine for the kit's lane computation (`Rule30ZeroBoundaryLanes.check`), exact to the
pinned source, with the kit's packed physical evaluator (`Rule30ZeroBoundarySmall.pstep`) beside it, for the lane
"D-exact": the exact death time D(W) of every width, kernel-checked above (the chunk certificate at K = D(W) + 1) and
below (an explicit witness start evolved by the kit's `prun`, bridged to `zrow` by `run_toFun`). Lane chosen by Local
on the owner's word (2026-10-23 20:4x BST: "it is up to you local to pick the next lane if the current has reached
its end - instinct method applies"). Design block; nothing beyond the tiny-width instrument tests runs before GPT's
design read (heartbeat rule), except as the rule's two-silent-ticks clause allows.

If this holds, it changes the kit's death-time table from "tightness observed, not proved" to proved at each width
reached (the kit's `Rule30ZeroBoundaryWidth52.lean`: "the bound 96, which is D(52) of the death-time table (its
tightness is observed, not proved)"), and gives the law of D(W) its first kernel-checked exact points: the record's
observed values are D(52) = 96 and D(56) <= 100, so the "2W - 8" law written in GPU-METAL-JOBS.md already fails at 56
(104 > 100) and the true law is open. D(W) is on the critical path as the finite shadow of Q01 (LR): a proof of a
linear bound for every W is Q01 itself.

The computation, exact to the kit (`Rule30ZeroBoundaryLanes.lean`, sha256 e34541fa…, cc1e0e0), lanes as bits of
Python integers (one lane per bit, 2^n lanes per chunk, exactly the kit's `Nat` words):
  ALL = 2^(2^n) - 1; pat(n, s): bit p is bit s of p; yFree(s) = pat(n, s) if s < n else (ALL if bit (s - n) of c
  else 0); scanN(acc, as, bs): v = acc; for each a: v = v xor (a or headD bs); emit v; bs = tail bs; returns (list,
  v); stepR at level k: k even: scan with ALL, Rnew = ALL :: list; k odd and k + 1 <= W: y = yFree(k / 2), scan with
  y, Rnew = y :: list; k odd and k + 1 > W: scan with 0, t = last, Rnew = t :: mapX t list; `last` is the scan's
  final value; alive &= ALL xor last when k is even and W < k + 1; run K levels from k = 0, R = Rm = [], alive = ALL;
  check = (alive == 0). The engine also records each lane's elimination level (the first level at which its alive bit
  cleared) and reconstructs a lane's start row as the `last` values of levels 0 .. W - 1 read as depths 1 .. W (a
  reading to be CONFIRMED by the exhaustive test below, not assumed).

Physical side (the kit's `Rule30ZeroBoundarySmall`): pstep r = (r >>> 1) xor (r ||| (r <<< 1)), bit j is depth j + 1,
the wall at depth 0 white; the first even time t with bit 0 clear is the start's death time; W1A's engines control
already matched this to the list engine for W <= 4 and the literal orbits from 1 and 3.

Instrument tests (tiny widths, exhaustive, seconds; predictions first):
  T1 agreement with the kit's own numbers: check(2, 7, 1, 0) true, check(2, 6, 1, 0) false (W1A's controls);
     check(16, 34, n, c) true for every chunk at n = 8 (the kit's `check_16`-style bound 34 at width 16: the kit's
     `checkBelow 34 (2^16)` is the physical form; the lane form at K = 34 is predicted true).
  T2 for W = 2 .. 12 (n = W / 2, one chunk): every lane's reconstructed start r < 2^W, the map lane -> start is
     injective, and the physical death time t(r) (first even time with depth 1 white) relates to the lane's
     elimination level e by ONE affine rule across all lanes and widths (predicted: t = e - W + something fixed, or
     t = e; the test finds and records it; counterfactual: no single rule fits, and then the reconstruction reading
     is wrong and is fixed before anything else);
  T3 D_phys(W) = max over ALL 2^W starts of t(r) (exhaustive, W <= 12) equals the lanes engine's D_lane(W) under T2's
     rule (the lanes cover the extremal starts; counterfactual: a start outside the lane images survives longer, which
     would contradict the kit's `q01_of_checks` soundness and must be a bug here);
  T4 negative: flipping the parity branch (treating k odd as even) or reversing lane order must break T2/T3.
The kit's death-time table for W <= 16 is predicted to be recovered exactly: D(W) for W = 2, 4, 6, 8 = 6, ?, 10, 12
(from W1A's K(W) = 7, 7, 11, 13 = D + 1) and D(16) <= 33.

OUTCOME of the instrument tests (MEASURED, 2026-10-23 20:47 BST, M5, 0.03 s): T1 true (check(2,7) true, check(2,6)
false, check(16,34) true); T2 every reconstructed start in range and the map injective at W = 2 .. 12, and the rule is
t = e exactly (offset 0 at every lane and width: a lane's elimination level IS the physical first even white time of
its reconstructed start); T3 D_lane = D_phys at every W <= 12: D(2..12) = 6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30;
T4 both negatives differ. A first revision had the death mask inverted (died = alive & ~last) and T2 reported a
constant offset of -2 with lanes missing: the test caught it; fixed to alive & last (the kit keeps alive ∧ (ALL xor
last)). Calibration (instrument, seconds): D(13..24) = 30, 32, 32, 32, 32, 32, 38, 38, 38, 40, 40, 42 (witness starts
recorded by the engine; each witness's physical death equals the level); one width-60 chunk at K = 129 takes 1.2 s
here (the Lean kernel: 0.36 s), chunk 0's latest lane dies at level 86 (lane 93695, start 0x2652039467d5555, physical
death 86).

D(W) run (block D1, after GPT's read): `python3 d1_engine.py D W [WORKERS] OUT.json` computes D(W) over every chunk at
n = min(W/2, 18) with WORKERS processes, recording per chunk the maximal elimination level and one lane there, and at
the end the witness start (hex), its physical death time by pstep (must equal D(W)), the chunk and lane, and timings.
Predictions: D(52) = 96 (the kit's observed value; counterfactual: anything else means this engine or the kit's table
is wrong, stop); D(56) = 100 (the author's bound; counterfactual: 98 or lower is possible and would be new); D(60) in
[102, 116] (counterfactual: outside; the K = 129 of W3 was 2W + 9 and no chunk failed, so D(60) <= 128 is known);
cost about 1.2 s per chunk per process: W = 52 about 1.5 min, 56 about 5 min, 60 about 25 min at 4 workers (nice 5,
6 GiB total stop by the caller's ulimit, each chunk's state is a few MB).
"""
import sys, time


def pat(n, s):
    """bit p of pat(n, s) is bit s of p, for p < 2^n (the kit's `pat` by its specification `pat_spec`)."""
    v = 0
    for p in range(1 << n):
        if (p >> s) & 1:
            v |= 1 << p
    return v


def pats_of(n):
    return [pat(n, s) for s in range(n)]


def y_free(n, c, ALL, pats, s):
    if s < n:
        return pats[s]
    return ALL if (c >> (s - n)) & 1 else 0


def scanN(acc, as_, bs):
    out = []; v = acc
    for i, a in enumerate(as_):
        b = bs[i] if i < len(bs) else 0
        v = v ^ (a | b); out.append(v)
    return out, v


def stepR(W, n, c, ALL, pats, k, R, Rm, flip_parity=False):
    even = (k % 2 == 0) != flip_parity
    bs = [0] + Rm
    if even:
        lst, last = scanN(ALL, R, bs); return [ALL] + lst, last
    if k + 1 <= W:
        y = y_free(n, c, ALL, pats, k // 2); lst, last = scanN(y, R, bs); return [y] + lst, last
    lst, t = scanN(0, R, bs); return [t] + [t ^ a for a in lst], t


def run_lanes(W, n, c, K, record=False, flip_parity=False):
    """The kit's `run` for K levels. Returns (alive, elim, lasts): elim[k] = the mask of lanes whose alive bit cleared
    at level k (when record); lasts = the `last` value per level (for reconstruction) when record."""
    ALL = (1 << (1 << n)) - 1; pats = pats_of(n)
    R, Rm, alive = [], [], ALL
    elim = {} if record else None; lasts = [] if record else None
    for k in range(K):
        Rnew, last = stepR(W, n, c, ALL, pats, k, R, Rm, flip_parity)
        if record: lasts.append(last)
        if k % 2 == 0 and W < k + 1:
            died = alive & last & ALL              # the kit keeps alive ∧ (ALL xor last): a lane dies where last is 1
            alive &= ALL ^ last
            if record and died:
                elim[k] = died                     # the mask of lanes eliminated at level k (bit p = lane p)
        R, Rm = Rnew, R
    return alive, elim, lasts


def check(W, K, n, c):
    return run_lanes(W, n, c, K)[0] == 0


def elim_of_lane(elim, p):
    for k, m in elim.items():
        if (m >> p) & 1: return k
    return None


def max_elim(elim):
    """(the largest elimination level, one lane eliminated there) or (None, None)."""
    if not elim: return None, None
    k = max(elim); return k, elim[k].bit_length() - 1


def reconstruct(W, lasts, p):
    """The start row of lane p from the recorded `last` values: depth j + 1 is bit p of lasts[j], j = 0 .. W - 1."""
    r = 0
    for j in range(W):
        if (lasts[j] >> p) & 1: r |= 1 << j
    return r


def pstep(r):
    return (r >> 1) ^ (r | (r << 1))


def death_phys(r, tmax):
    """First even time t with the depth-1 cell white, or None within tmax."""
    for t in range(tmax + 1):
        if t % 2 == 0 and (r & 1) == 0:
            return t
        r = pstep(r)
    return None


def D_phys(W, tmax):
    worst = -1; arg = None
    for r in range(1 << W):
        t = death_phys(r, tmax)
        if t is None: return None, r
        if t > worst: worst, arg = t, r
    return worst, arg


def tests():
    out = {}
    out['T1'] = {'check_2_7_true': check(2, 7, 1, 0), 'check_2_6_false': not check(2, 6, 1, 0)}
    t0 = time.time()
    out['T1']['check_16_34_all_chunks'] = all(check(16, 34, 8, c) for c in range(1 << (8 - 8)))
    out['T1']['seconds_16'] = round(time.time() - t0, 2)
    rules = {}; inj = True; inrange = True; dl = {}; dp = {}
    for W in range(2, 13):
        n = W // 2; K = 4 * W + 8
        alive, elim, lasts = run_lanes(W, n, 0, K, record=True)
        starts = {}
        for p in range(1 << n):
            r = reconstruct(W, lasts, p)
            if r >= (1 << W): inrange = False
            if r in starts: inj = False
            starts[r] = p
            e = elim_of_lane(elim, p); t = death_phys(r, 4 * W + 8)
            rules.setdefault(W, set()).add((None if e is None else e - (t if t is not None else -999)))
        dl[W] = max_elim(elim)[0] if elim and alive == 0 else None
        dp[W] = D_phys(W, 4 * W + 8)[0]
    out['T2'] = {'all_starts_in_range': inrange, 'injective': inj, 'offset_sets_e_minus_t': {W: sorted(x for x in s if x is not None) for W, s in rules.items()}, 'none_eliminated': any(None in s for s in rules.values())}
    out['T3'] = {'D_lane_by_W': dl, 'D_phys_by_W': dp}
    # T4 negatives: flipped parity and reversed lanes must not reproduce the lane deaths at W = 8
    W, n, K = 8, 4, 40
    alive_f, elim_f, _ = run_lanes(W, n, 0, K, record=True, flip_parity=True)
    alive_ok, elim_ok, lasts = run_lanes(W, n, 0, K, record=True)
    rev = {k: int(bin(m)[2:].zfill(1 << n)[::-1], 2) for k, m in elim_ok.items()}
    out['T4'] = {'flipped_parity_differs': (alive_f, elim_f) != (alive_ok, elim_ok), 'reversed_lanes_differ': rev != elim_ok}
    return out


def chunk_job(args):
    W, n, c, K = args
    alive, elim, lasts = run_lanes(W, n, c, K, record=True)
    k, p = max_elim(elim)
    return c, alive == 0, k, p


def D_run(W, workers, out_path, K=None):
    import json, multiprocessing as mp
    n = min(W // 2, 18); chunks = 1 << (W // 2 - n); K = K or (2 * W + 9)
    t0 = time.time(); res = {'W': W, 'n': n, 'K': K, 'chunks': chunks, 'workers': workers, 'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'per_chunk_max': {}}
    best = (-1, None, None); all_dead = True
    with mp.Pool(workers) as pool:
        for c, dead, k, p in pool.imap_unordered(chunk_job, [(W, n, c, K) for c in range(chunks)], chunksize=1):
            res['per_chunk_max'][c] = k; all_dead &= dead
            if k is not None and k > best[0]: best = (k, c, p)
            if len(res['per_chunk_max']) % 64 == 0:
                res['elapsed_s'] = round(time.time() - t0, 1); json.dump(res, open(out_path, 'w'))
    k, c, p = best
    _, _, lasts = run_lanes(W, n, c, K, record=True); r = reconstruct(W, lasts, p)
    res.update({'all_chunks_dead_at_K': all_dead, 'D': k, 'witness': {'chunk': c, 'lane': p, 'start_hex': hex(r), 'phys_death': death_phys(r, K + 2)},
                'witness_consistent': death_phys(r, K + 2) == k, 'elapsed_s': round(time.time() - t0, 1), 'finished': time.strftime('%Y-%m-%dT%H:%M:%S')})
    json.dump(res, open(out_path, 'w'), indent=1)
    return res


if __name__ == '__main__':
    import json
    if len(sys.argv) >= 4 and sys.argv[1] == 'D':
        W = int(sys.argv[2]); workers = int(sys.argv[3]) if len(sys.argv) > 4 else 4; out = sys.argv[-1]
        r = D_run(W, workers, out); print('W', W, 'D', r['D'], 'witness', r['witness'], 'consistent', r['witness_consistent'], 'all dead', r['all_chunks_dead_at_K'], r['elapsed_s'], 's')
    else:
        print(json.dumps(tests(), indent=1, default=str))
