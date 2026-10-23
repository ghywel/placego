#!/usr/bin/env python3
"""D1, revision 6 (revision 5 with GC1742's corrections to the `maximizers` mode: a self-checking second pass, set-bit iteration with a first-mismatch stop and bounded rejection sample, atomic progress in both phases, exact lane and distinct-start counts with truncation reported, the deep-prefix statistic as a stated family rule with a baseline, and `maxtest`, the mode's own asserted controls; the census and witness modes and the executed revisions' code unchanged). Revision 5 was (revision 4, the executed version e61d1694… for the width-64 census, plus a `maximizers` mode and its `runmax` launcher: every lane at the maximal level, each start validated; nothing else changed). Revision 4 was (revision 3, the executed version 27eb852c…, with the stale MISS sentence corrected and the stage outcomes below; code unchanged): revision 3 was revision 2 (the executed a5f331d3…) plus a `census` mode and a `runcensus` launcher for the widths without a tight certified bound: a CPU word engine for the kit's lane computation (`Rule30ZeroBoundaryLanes.check`), exact to the
pinned source, with the kit's packed physical evaluator (`Rule30ZeroBoundarySmall.pstep`) beside it, for the lane
"D-exact": the exact death time D(W) of a width, kernel-checked above (a chunk certificate at K = D + 1) and below (an
explicit witness start evolved by the kit's `prun`, bridged to `zrow` by `run_toFun`). Lane chosen by Local on the
owner's word (2026-10-23 ~20:40 BST: Local picks the next lane when the current one ends; instinct method). Revision
2 follows GPT's review GC1730 / GPT-L805-D1-REVIEW.md: explicit mutual agreement governs every run (the two-silent-
ticks clause of revision 1 is withdrawn); witness-first at an already certified bound; terminal verdicts enforced;
tests assert and exit nonzero; negatives routed through the acceptance validator; atomic checkpoints with coverage and
binding; patterns built once per process by the kit's doubling; the supervised launcher below with frozen caps.
NOT an agreed job until GPT accepts this exact file; nothing runs on import; nothing is submitted.

If this holds, it changes the kit's death-time table from "tightness observed, not proved" to proved at each width
reached, and gives the law of D(W) its first kernel-checked exact points (the LR row; a linear bound for every width
would IMPLY Q01 and is stronger than Q01, which only asks that every finite start has some even white time).

Definitions (GPT's framing, adopted). D(W) is the largest, over starts r with 0 < r < 2^W (supported at depths 1 .. W),
of the first even time t at which the depth-1 cell is white, time 0 included. The kit's certificates give an upper
bound U(W) with t <= U: U(52) = 96 (the kit), U(56) = 100 (W2), U(60) = 128 (W3). A witness start black at depth 1 at
every even time strictly below U, together with the upper theorem, shows the bound is attained, so D(W) = U(W)
exactly, when U is even (every certified U is even); the direct physical check at U is retained too. So the first
useful job is WITNESS-FIRST: find one start attaining the certified bound, validate it physically, and later
kernel-check its lower statement; no second upper census is needed when the bound is attained. A miss (no lane
attains U after every chunk) is inconclusive for exactness: D(W) < U would then need a tighter upper bound, which is a
full certificate at a smaller K over ALL chunks (one chunk never establishes an upper bound).

The lane computation, exact to the kit (`Rule30ZeroBoundaryLanes.lean`, sha256 e34541fa…, cc1e0e0), lanes as bits of
Python integers (the kit's own `Nat` words): ALL = 2^(2^n) - 1; pat(n, s) by the kit's `dbl` doubling (bit p is bit s
of p, checked against the bitwise definition in T0); yFree(s) = pat(n, s) if s < n else (ALL if bit (s - n) of c else
0); scanN(acc, as, bs): v = acc; for each a: v = v xor (a or headD bs); emit v; bs = tail bs; stepR at level k: k even:
scan with ALL, Rnew = ALL :: list; k odd and k + 1 <= W: y = yFree(k / 2), Rnew = y :: list; k odd and k + 1 > W: scan
with 0, t = last, Rnew = t :: mapX t list; alive &= ALL xor last when k is even and W < k + 1 (a lane dies where last
is 1); run K levels from k = 0, R = Rm = [], alive = ALL; check = (alive == 0). The engine records each level's
elimination mask and the `last` values, and reconstructs a lane's start as the `last` values of levels 0 .. W - 1
read as depths 1 .. W (only the even and free branches feed those levels, so the forced-odd caveat of GPT's G1
interface does not touch the extraction). Finite tests that a lane's elimination level equals its start's physical
death time are finite evidence, used to find candidates; the lower bound is gated on the independent physical check
of the witness (pstep), never on the lane engine.

Tests (`python3 d1_engine.py test`; every outcome asserted, nonzero exit on any failure; predictions first):
  T0 pat by doubling equals pat by bits for n <= 12;
  T1 the kit's numbers: check(2,7) true, check(2,6) false, check(16,34) true;
  T2 W = 2 .. 12: every reconstructed start r satisfies 0 < r < 2^W, the lane-to-start map is injective, and the
     physical death time of every lane's start equals its elimination level (t = e), at every lane and width;
  T3 W = 2 .. 12: the lane engine's maximal elimination level equals the physical maximum over ALL 2^W starts, and the
     validator (validate_witness) accepts the engine's witness;
  T4 negatives through the validator: the flipped-parity mutant and the reversed-lane-order mutant each produce a
     candidate (level, start) that validate_witness REJECTS at W = 8 (or no candidate at all), and a start whose
     physical death is 2 short of the target is rejected.
Predicted (and measured in revision 1, 2026-10-23 20:4x BST, before the asserts existed): all pass; D(2 .. 12) = 6, 6,
6, 8, 10, 12, 12, 18, 18, 30, 30; D(13 .. 24) = 30, 32, 32, 32, 32, 32, 38, 38, 38, 40, 40, 42; D(30) = 52; one width-60
chunk 1.2 s of recurrence (setup and validation separate; the Lean kernel 0.36 s).

Witness-first run (`python3 d1_engine.py witness W U WORKERS OUT.json`; the proposal for GPT's acceptance): chunks
c = 0, 1, 2, ... at n = min(W/2, 18) and K = U + 1, WORKERS processes (proposed 2, the agreed pilot's count; never
more without agreement); each chunk reports whether all its lanes died by K (if not, the run STOPS: U would be
contradicted and that is a bug or a wrong U) and its maximal elimination level with one lane; the first chunk whose
maximum equals U gives the candidate; the parent reconstructs the start r, validates it physically (validate_witness:
0 < r < 2^W, depth-1 black at every even t < U, white at U) and stops with verdict ATTAINED; if every chunk is done
without one, verdict MISS (inconclusive); any validation failure is FAIL. Checkpoints are atomic (tmp + rename) after
every chunk, with the chunk list completed, duplicates refused, exact coverage checked at the end, monotonic elapsed,
start/finish times, this file's sha256, the Python version, and the terminal verdict; an interrupted run keeps its
completed chunk identifiers. Predictions: W = 52, U = 96: ATTAINED within the 256 chunks (D(52) = 96 is the kit's
observed value; counterfactual: MISS, which would mean the kit's table or this engine is wrong, stop); cost about
0.6 s per chunk at K = 97, so under 2 minutes at 2 workers even if the witness is in the last chunk. W = 56, U = 100:
ATTAINED or MISS both informative (a MISS is inconclusive for exactness: D(56) < 100 would need a tighter full certificate; corrected in revision 4 after GC1734);
about 0.9 s per chunk, 1,024 chunks, about 8 minutes at 2 workers. W = 60 is not proposed in this revision (4,096
chunks at 1.2 s is beyond a 30-minute stage at 2 workers; a C engine or a later agreement).

Supervised launcher (`python3 d1_engine.py run W U WORKERS OUT_DIR`): the W1A supervisor (`w1a_harness.Supervisor`,
unchanged, sha256 3f9089146c…) runs the witness-first command as one step with these frozen caps: stage 30 min, step
wall 25 min, cumulative CPU 50 min (two workers), process-group RSS stop 6 GiB (the workers are in the step's group,
so the sampled aggregate is the sum over them), pressure level >= 2, swap growth 256 MiB, disk 5 GiB, new artifacts
512 MiB, log 10 MiB, no retry; the supervisor's receipt plus the engine's checkpoint file are the run's record. No
Lean job runs beside it. The kit path is only used for the supervisor's disk and pressure metrics.

OUTCOME (MEASURED, run d1-w52-20261023-2103, launched 21:03 BST at GC1731's accepted versions, nice 5, two workers;
supervisor receipt sha256 86d8e1d1937f641be614d313d8a354c228ac3b1864ad28ca18a6fa2840d33dd2, checkpoint sha256 fa8883fe4069dbddc5e79bea7fae68bff5d179418907b16cf2893bec913542b8, both kept on the M5):
supervisor complete, step witness_W52 pass/completed, final problems [], groups clean after; engine verdict ATTAINED:
chunk 31, lane 127461, start 0x7dc2ff6fcc4fd (51 bits, width <= 52), physically validated (black at depth 1 at every
even t < 96, white at 96) by the packed validator inside the run and again by the list-of-bools engine of
w1a_harness afterwards; 32 chunks consumed of 256 (the first qualifying chunk in consumption order), per-chunk maxima
76 .. 88 before it. The cost prediction was wrong by two orders: the whole step took 1.04 s wall (0.51 s user) and the
recurrence 12 ms per chunk; revision 1's "1.2 s per width-60 chunk" was the bitwise pattern setup, which the kit's
doubling removes (a width-60 chunk's recurrence is 27 ms). So a full census at width 60 is minutes, not an hour.
Group RSS sampled at 1 MiB (the step lasted one sample). D(52) = 96 is now a physically validated candidate pending
the Lean lower proof (block D2, d2_witness.py); D2 then kernel-checked D(52) = 96 (L810).

OUTCOME of revision 3's two stages (MEASURED, GC1734's accepted versions, nice 5, two workers, L812): stage 1
d1-w56-20261023-2125, `run 56 100 2`: ATTAINED at chunk 820 of 1,024 (821 consumed), witness 0x93d4b223f5b9b5 (56
bits), physical death 100 (validator and, afterwards, the list-of-bools engine); step pass, final problems [], wall
6.25 s, user 12.47 s, sys 0.38 s, sampled group peak 155 MiB with 5 members, groups clean; per-chunk maxima 76 .. 100
(one chunk at 98, one at 100). Stage 2 d1-w60-20261023-2125, `runcensus 60 129 2`: CENSUS-ATTAINED, all 4,096
chunks covered, no lane alive at 129, maximum level 114 attained by exactly one chunk (1400, lane 1995), witness
0xe77a4e77b8f99b5 (60 bits), physical death 114 (validator and the list engine); step pass, final problems [], wall
50.0 s, user 98.7 s, sys 1.0 s, sampled group peak 190 MiB, groups clean; maxima histogram 78:1, 80:45, 82:386,
84:884, 86:1034, 88:737, 90:456, 92:254, 94:136, 96:87, 98:44, 100:17, 102:5, 104:3, 106:2, 108:1, 110:3, 114:1.
Against the predictions: 56 under a minute (6 s); 60 about two minutes with M in [102, 116] (50 s; M = 114).
So the candidates are D(56) = 100 (the W2 bound attained) and D(60) = 114 (the W3 bound 128 is loose by 14);
neither is a law of the form 2W - c (D - 2W = -8, -12, -6 at 52, 56, 60).
OUTCOME of revision 4's width-64 census (MEASURED, GC1740's accepted version e61d1694…, run d1-w64-20261023-2216,
`runcensus 64 137 2`, nice 5, two workers; receipt sha256 7b269d16895710fa6aa0fca17b665c3896b810cd3db7f25cfefab04a30e53162; checkpoint sha256
1dcd9f1ccc4dda5f4ce1ea6e81e0f63865696aed2177052027fb844fd8d79866): CENSUS-ATTAINED, all 16,384 chunks covered, no lane alive at 137, maximum level
116 attained by exactly one chunk (10686, lane 42727), witness 0x88b46d66afc2fbd5 (64 bits), physical death 116
(validator and the list engine); step pass, final problems [], wall 229.0 s, user 460.9 s, sys 4.4 s, max RSS 81
MiB, sampled group peak 204 MiB with 5 members, groups clean; recurrence sum 454 s (28 ms per chunk). Against the
predictions: about four minutes (3.8); group RSS under 1 GiB (0.2); M in [118, 134]: MISS, M = 116 is below the
range (D - 2W = -12 at 64). So the candidates are D(64) = 116 with the certified 96, 100, 114 before it.
"""
import hashlib, json, os, platform, sys, time

_PATS = {}


def pat_bits(n, s):
    v = 0
    for p in range(1 << n):
        if (p >> s) & 1:
            v |= 1 << p
    return v


def dbl(m, B, length):
    for _ in range(m):
        B = B | (B << length); length = length + length
    return B


def pat(n, s):
    """The kit's `pat n s = dbl (n - (s + 1)) ((2^(2^s) - 1) <<< 2^s) (2^(s + 1))`."""
    return dbl(n - (s + 1), ((1 << (1 << s)) - 1) << (1 << s), 1 << (s + 1))


def pats_of(n):
    if n not in _PATS:
        _PATS[n] = [pat(n, s) for s in range(n)]
    return _PATS[n]


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
    at level k (when record); lasts = the `last` value per level (when record)."""
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
                elim[k] = died
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
    """The start row of lane p: depth j + 1 is bit p of lasts[j], j = 0 .. W - 1 (a reversed-lane mutant reads the
    wrong bit here, which is what T4 exercises)."""
    r = 0
    for j in range(W):
        if (lasts[j] >> p) & 1: r |= 1 << j
    return r


# ---- the physical side (the kit's Rule30ZeroBoundarySmall) --------------------------------------------------------------

def pstep(r):
    return (r >> 1) ^ (r | (r << 1))


def death_phys(r, tmax):
    """First even time t <= tmax with the depth-1 cell white, or None."""
    for t in range(tmax + 1):
        if t % 2 == 0 and (r & 1) == 0:
            return t
        r = pstep(r)
    return None


def validate_witness(W, U, r):
    """The independent physical gate: 0 < r < 2^W, depth 1 black at every even t < U, white at U (U even).
    Returns (ok, reason)."""
    if not (0 < r < (1 << W)): return False, 'start-out-of-range'
    if U % 2: return False, 'U-odd'
    x = r
    for t in range(U + 1):
        if t % 2 == 0:
            if t < U and (x & 1) == 0: return False, 'white-early-at-%d' % t
            if t == U and (x & 1) == 1: return False, 'black-at-U'
        x = pstep(x)
    return True, 'attains-%d' % U


def D_phys(W, tmax):
    worst = -1; arg = None
    for r in range(1, 1 << W):
        t = death_phys(r, tmax)
        if t is None: return None, r
        if t > worst: worst, arg = t, r
    return worst, arg


# ---- tests ----------------------------------------------------------------------------------------------------------------

def tests():
    out = {}; fails = []

    def req(name, cond, **d):
        out[name] = {'ok': bool(cond), **d}
        if not cond: fails.append(name)

    req('T0_pat_dbl_eq_bits', all(pat(n, s) == pat_bits(n, s) for n in range(1, 13) for s in range(n)))
    req('T1_kit_numbers', check(2, 7, 1, 0) and not check(2, 6, 1, 0) and check(16, 34, 8, 0))
    inrange = True; inj = True; rule = True; eq = True; dl = {}; dp = {}; accepted = True
    for W in range(2, 13):
        n = W // 2; K = 4 * W + 8
        alive, elim, lasts = run_lanes(W, n, 0, K, record=True)
        starts = {}
        for p in range(1 << n):
            r = reconstruct(W, lasts, p)
            if not (0 < r < (1 << W)): inrange = False
            if r in starts: inj = False
            starts[r] = p
            e = elim_of_lane(elim, p); t = death_phys(r, K)
            if e is None or t is None or e != t: rule = False
        k, p = max_elim(elim); dl[W] = k if alive == 0 else None
        dp[W] = D_phys(W, K)[0]
        if dl[W] != dp[W]: eq = False
        if not validate_witness(W, k, reconstruct(W, lasts, p))[0]: accepted = False
    req('T2_reconstruction_and_t_eq_e', inrange and inj and rule, in_range=inrange, injective=inj, t_eq_e=rule)
    req('T3_lane_max_eq_phys_max_and_witness_accepted', eq and accepted, D_lane=dl, D_phys=dp)
    W, n, K = 8, 4, 40
    _, elim_f, lasts_f = run_lanes(W, n, 0, K, record=True, flip_parity=True)
    kf, pf = max_elim(elim_f)
    neg_flip = (kf is None) or not validate_witness(W, dp[8], reconstruct(W, lasts_f, pf))[0]
    _, elim_ok, lasts_ok = run_lanes(W, n, 0, K, record=True)
    ko, po = max_elim(elim_ok)
    pr = (1 << n) - 1 - po                                   # the reversed-lane mutant names the mirrored lane
    neg_rev = not validate_witness(W, dp[8], reconstruct(W, lasts_ok, pr))[0]
    r_ok = reconstruct(W, lasts_ok, po)
    neg_short = not validate_witness(W, dp[8] + 2, r_ok)[0]   # a target 2 beyond the start's real death is rejected
    pos_ok = validate_witness(W, dp[8], r_ok)[0]
    req('T4_negatives_rejected_by_validator', neg_flip and neg_rev and neg_short and pos_ok, flipped=neg_flip, reversed=neg_rev, short=neg_short, positive=pos_ok)
    out['fails'] = fails
    return out, not fails


# ---- witness-first run --------------------------------------------------------------------------------------------------------

def chunk_job(args):
    W, n, c, K = args
    t0 = time.monotonic()
    alive, elim, lasts = run_lanes(W, n, c, K, record=True)
    k, p = max_elim(elim)
    return {'c': c, 'all_dead': alive == 0, 'max_level': k, 'lane': p, 'seconds': round(time.monotonic() - t0, 3)}


def atomic_write(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f: json.dump(obj, f, indent=1)
    os.replace(tmp, path)


def witness_first(W, U, workers, out_path):
    import multiprocessing as mp
    n = min(W // 2, 18); chunks = 1 << (W // 2 - n); K = U + 1
    t0 = time.monotonic()
    res = {'mode': 'witness-first', 'W': W, 'U': U, 'K': K, 'n': n, 'chunks': chunks, 'workers': workers,
           'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'python': platform.python_version(),
           'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'verdict': 'RUNNING', 'reason': None, 'completed': [], 'per_chunk': {},
           'setup_s': None, 'elapsed_s': 0.0}
    ts = time.monotonic(); pats_of(n); res['setup_s'] = round(time.monotonic() - ts, 3)
    atomic_write(out_path, res)
    candidate = None; verdict = 'MISS'; reason = 'no chunk attains U'
    with mp.Pool(workers) as pool:
        it = pool.imap(chunk_job, [(W, n, c, K) for c in range(chunks)], chunksize=1)
        for job in it:
            c = job['c']
            if c in res['per_chunk']:
                verdict, reason = 'FAIL', 'duplicate chunk %d' % c; break
            res['per_chunk'][c] = job; res['completed'].append(c); res['elapsed_s'] = round(time.monotonic() - t0, 1)
            if not job['all_dead']:
                verdict, reason = 'FAIL', 'chunk %d has a lane alive at K = %d: U = %d contradicted (bug or wrong U)' % (c, K, U); atomic_write(out_path, res); break
            if job['max_level'] is not None and job['max_level'] > U:
                verdict, reason = 'FAIL', 'chunk %d max level %d above U' % (c, job['max_level']); atomic_write(out_path, res); break
            if job['max_level'] == U:
                candidate = (c, job['lane']); atomic_write(out_path, res); pool.terminate(); break
            atomic_write(out_path, res)
    if candidate:
        c, p = candidate
        tv = time.monotonic()
        _, _, lasts = run_lanes(W, n, c, K, record=True); r = reconstruct(W, lasts, p)
        ok, why = validate_witness(W, U, r)
        res['witness'] = {'chunk': c, 'lane': p, 'start_hex': hex(r), 'start_bits': W, 'validation': why, 'phys_death': death_phys(r, K + 2),
                          'validate_s': round(time.monotonic() - tv, 3)}
        verdict, reason = ('ATTAINED', 'physical witness validated at U = %d' % U) if ok else ('FAIL', 'witness rejected: %s' % why)
    if verdict == 'MISS':
        cov = sorted(res['completed']) == list(range(chunks))
        res['coverage_exact'] = cov
        if not cov: verdict, reason = 'FAIL', 'coverage incomplete'
        else: reason = 'no chunk attains U = %d over all %d chunks: inconclusive for exactness (D(W) < U would need a tighter upper certificate)' % (U, chunks)
    res.update({'verdict': verdict, 'reason': reason, 'elapsed_s': round(time.monotonic() - t0, 1), 'finished': time.strftime('%Y-%m-%dT%H:%M:%S'),
                'recurrence_s_total': round(sum(j['seconds'] for j in res['per_chunk'].values()), 2)})
    atomic_write(out_path, res)
    return res


def census(W, K, workers, out_path):
    """Revision 3 (for GPT's read): every chunk at K levels; the maximum elimination level M over all lanes is the
    candidate D(W) = M, with its witness reconstructed and validated at U = M. Verdicts: CENSUS-ATTAINED (every chunk
    covered, no lane alive at K, witness validated at M), FAIL (a lane alive at K: K too small for a census; a rejected
    witness; a duplicate; incomplete coverage). Same checkpointing as witness_first."""
    import multiprocessing as mp
    n = min(W // 2, 18); chunks = 1 << (W // 2 - n)
    t0 = time.monotonic()
    res = {'mode': 'census', 'W': W, 'U': None, 'K': K, 'n': n, 'chunks': chunks, 'workers': workers,
           'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'python': platform.python_version(),
           'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'verdict': 'RUNNING', 'reason': None, 'completed': [], 'per_chunk': {}, 'setup_s': None, 'elapsed_s': 0.0}
    ts = time.monotonic(); pats_of(n); res['setup_s'] = round(time.monotonic() - ts, 3)
    atomic_write(out_path, res)
    verdict, reason = 'RUNNING', None; best = (-1, None, None)
    with mp.Pool(workers) as pool:
        for job in pool.imap(chunk_job, [(W, n, c, K) for c in range(chunks)], chunksize=1):
            c = job['c']
            if c in res['per_chunk']:
                verdict, reason = 'FAIL', 'duplicate chunk %d' % c; break
            res['per_chunk'][c] = job; res['completed'].append(c); res['elapsed_s'] = round(time.monotonic() - t0, 1)
            if not job['all_dead']:
                verdict, reason = 'FAIL', 'chunk %d has a lane alive at K = %d: K too small for a census' % (c, K); atomic_write(out_path, res); break
            if job['max_level'] is not None and job['max_level'] > best[0]: best = (job['max_level'], c, job['lane'])
            if len(res['completed']) % 64 == 0 or len(res['completed']) == chunks: atomic_write(out_path, res)
    if verdict == 'RUNNING':
        cov = sorted(res['completed']) == list(range(chunks)); res['coverage_exact'] = cov
        if not cov: verdict, reason = 'FAIL', 'coverage incomplete'
        else:
            M, c, p = best
            tv = time.monotonic(); _, _, lasts = run_lanes(W, n, c, K, record=True); r = reconstruct(W, lasts, p)
            ok, why = validate_witness(W, M, r)
            res['witness'] = {'chunk': c, 'lane': p, 'start_hex': hex(r), 'start_bits': W, 'validation': why, 'phys_death': death_phys(r, K + 2), 'validate_s': round(time.monotonic() - tv, 3)}
            res['U'] = M; res['chunks_attaining_M'] = sum(1 for v in res['per_chunk'].values() if v['max_level'] == M)
            verdict, reason = ('CENSUS-ATTAINED', 'maximum level %d over all %d chunks, witness validated at %d' % (M, chunks, M)) if ok else ('FAIL', 'witness rejected at M = %d: %s' % (M, why))
    res.update({'verdict': verdict, 'reason': reason, 'elapsed_s': round(time.monotonic() - t0, 1), 'finished': time.strftime('%Y-%m-%dT%H:%M:%S'),
                'recurrence_s_total': round(sum(j['seconds'] for j in res['per_chunk'].values()), 2)})
    atomic_write(out_path, res)
    return res


def top_family(r, W, bits=8):
    """The membership rule of the deep-prefix statistic: a start's family is its top `bits` bits after zero-padding
    to W bits (depths W - bits + 1 .. W)."""
    return (r >> max(0, W - bits)) & ((1 << bits) - 1)


def maximizers(W, K, workers, out_path, max_list=4096, fault_empty_mask=False):
    """Revision 6 (GC1742's corrections): the census, then a self-checking second pass over every chunk attaining the
    maximal level M: the rerun must have no lane alive at K, the same maximum M, a nonempty elimination mask at M,
    and its popcount must equal the number of lanes validated; every maximizing lane's start is validated at M by
    the physical validator (set-bit iteration, the first mismatch stops the run as FAIL with a bounded rejection
    sample); progress is persisted atomically per chunk in both phases. Outputs: `maximizing_lane_count` (exact),
    `distinct_start_count` among the validated starts (identity of starts is not independently proved complete),
    the retained list (capped at max_list, with `list_truncated`), and the deep-prefix statistic: the family
    partition by `top_family` (top 8 bits after zero-padding to W), its family count and sizes, against the
    baseline of the same statistic over the first max(count, 32) starts of the maximizing chunks' lane 0 .. (a
    non-extremal sample of the same width). Verdicts MAXIMIZERS or FAIL."""
    import multiprocessing as mp
    n = min(W // 2, 18); chunks = 1 << (W // 2 - n)
    t0 = time.monotonic()
    res = {'mode': 'maximizers', 'W': W, 'U': None, 'K': K, 'n': n, 'chunks': chunks, 'workers': workers,
           'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'python': platform.python_version(),
           'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'verdict': 'RUNNING', 'phase': 'census', 'reason': None, 'completed': [], 'per_chunk': {},
           'setup_s': None, 'elapsed_s': 0.0, 'second_pass': {'chunks_total': None, 'chunks_done': 0, 'lanes_validated': 0, 'rejected_count': 0, 'rejected_sample': []}}
    ts = time.monotonic(); pats_of(n); res['setup_s'] = round(time.monotonic() - ts, 3); atomic_write(out_path, res)
    verdict, reason = 'RUNNING', None; M = -1
    with mp.Pool(workers) as pool:
        for job in pool.imap(chunk_job, [(W, n, c, K) for c in range(chunks)], chunksize=1):
            c = job['c']
            if c in res['per_chunk']: verdict, reason = 'FAIL', 'duplicate chunk %d' % c; break
            res['per_chunk'][c] = job; res['completed'].append(c); res['elapsed_s'] = round(time.monotonic() - t0, 1)
            if not job['all_dead']: verdict, reason = 'FAIL', 'chunk %d has a lane alive at K = %d' % (c, K); atomic_write(out_path, res); break
            if job['max_level'] is not None and job['max_level'] > M: M = job['max_level']
            if len(res['completed']) % 64 == 0 or len(res['completed']) == chunks: atomic_write(out_path, res)
    if verdict == 'RUNNING':
        cov = sorted(res['completed']) == list(range(chunks)); res['coverage_exact'] = cov
        if not cov: verdict, reason = 'FAIL', 'coverage incomplete'
        elif M < 0: verdict, reason = 'FAIL', 'no maximum level recorded'
    if verdict == 'RUNNING':
        top = sorted(c for c, v in res['per_chunk'].items() if v['max_level'] == M)
        res['U'] = M; res['phase'] = 'second-pass'; sp = res['second_pass']; sp['chunks_total'] = len(top); atomic_write(out_path, res)
        starts = []; seen = set(); count = 0; truncated = False; baseline = []
        for c in top:
            alive2, elim2, lasts = run_lanes(W, n, c, K, record=True)
            k2, _ = max_elim(elim2); mask = elim2.get(M, 0)
            if fault_empty_mask: mask = 0
            if alive2 != 0: verdict, reason = 'FAIL', 'second pass: chunk %d has a lane alive' % c; break
            if k2 != M: verdict, reason = 'FAIL', 'second pass: chunk %d maximum %s differs from M = %d' % (c, k2, M); break
            if mask == 0: verdict, reason = 'FAIL', 'second pass: chunk %d has an empty mask at M' % c; break
            pop = bin(mask).count('1'); validated = 0; m = mask
            while m:
                low = m & -m; p = low.bit_length() - 1; m ^= low
                r = reconstruct(W, lasts, p); ok, why = validate_witness(W, M, r)
                if not ok:
                    sp['rejected_count'] += 1
                    if len(sp['rejected_sample']) < 8: sp['rejected_sample'].append({'chunk': c, 'lane': p, 'start_hex': hex(r), 'why': why})
                    verdict, reason = 'FAIL', 'second pass: a maximizing lane rejected by the validator (chunk %d, lane %d)' % (c, p); break
                validated += 1; count += 1; seen.add(r)
                if len(starts) < max_list: starts.append({'chunk': c, 'lane': p, 'start_hex': hex(r), 'bits': r.bit_length(), 'family': top_family(r, W)})
                else: truncated = True
            if verdict == 'FAIL': break
            if validated != pop: verdict, reason = 'FAIL', 'second pass: chunk %d validated %d lanes against a mask popcount of %d' % (c, validated, pop); break
            for p in range(min(32, 1 << n)):                     # the baseline sample: the chunk's lanes 0 .. 31, non-extremal in general
                baseline.append(top_family(reconstruct(W, lasts, p), W))
            sp['chunks_done'] += 1; sp['lanes_validated'] = count; res['elapsed_s'] = round(time.monotonic() - t0, 1); atomic_write(out_path, res)
        if verdict == 'RUNNING':
            if count == 0: verdict, reason = 'FAIL', 'second pass: no maximizing lane found'
            else:
                fams = {}
                for st_ in starts: fams[st_['family']] = fams.get(st_['family'], 0) + 1
                bfams = {}
                for f in baseline[:max(count, 32)]: bfams[f] = bfams.get(f, 0) + 1
                res.update({'maximizing_lane_count': count, 'distinct_start_count': len(seen), 'maximizers': starts, 'list_truncated': truncated,
                            'chunks_attaining_M': len(top), 'family_rule': 'top 8 bits after zero-padding to W (depths W-7 .. W)',
                            'family_count': len(fams), 'family_sizes': sorted(fams.values(), reverse=True),
                            'baseline_sample_size': min(len(baseline), max(count, 32)), 'baseline_family_count': len(bfams),
                            'hypothesis': 'maximizers share deep bits: family_count <= maximizing_lane_count / 2 when the count is at least 4 (a pilot statistic, not a theorem)',
                            'hypothesis_holds': (count >= 4 and len(fams) * 2 <= count)})
                verdict, reason = 'MAXIMIZERS', 'M = %d, %d maximizing lanes (%d distinct starts) over %d chunks, all validated; families %d (baseline %d of %d)' % (M, count, len(seen), len(top), len(fams), len(bfams), min(len(baseline), max(count, 32)))
    res.update({'verdict': verdict, 'reason': reason, 'phase': 'done', 'elapsed_s': round(time.monotonic() - t0, 1), 'finished': time.strftime('%Y-%m-%dT%H:%M:%S'),
                'recurrence_s_total': round(sum(j['seconds'] for j in res['per_chunk'].values()), 2)})
    atomic_write(out_path, res)
    return res


def maximizer_tests():
    """The mode's controls (GC1742 item 5), asserted: (a) at W = 6 .. 12 the SET of validated maximizing starts equals the
    set of all starts attaining D_phys(W) by brute force; (b) insufficient K fails; (c) an empty second-pass mask fails;
    (d) a positive multi-maximizer case (W = 24: 6 lanes); (e) truncation is reported (max_list = 2 at W = 24)."""
    import tempfile
    out = {}; fails = []
    def req(name, cond, **d):
        out[name] = {'ok': bool(cond), **d}
        if not cond: fails.append(name)
    d = tempfile.mkdtemp()
    seteq = True; detail = {}
    for W in range(6, 13):
        r = maximizers(W, 4 * W + 8, 1, os.path.join(d, 'm%d.json' % W))
        Dp, _ = D_phys(W, 4 * W + 8)
        brute = {x for x in range(1, 1 << W) if death_phys(x, 4 * W + 8) == Dp}
        got = {int(m['start_hex'], 16) for m in r['maximizers']}
        detail[W] = {'D': r['U'], 'D_phys': Dp, 'lanes': r.get('maximizing_lane_count'), 'brute': len(brute), 'equal': got == brute}
        if r['verdict'] != 'MAXIMIZERS' or r['U'] != Dp or got != brute: seteq = False
    req('A_set_equals_brute_force', seteq, detail=detail)
    r = maximizers(24, 40, 1, os.path.join(d, 'k.json')); req('B_insufficient_K_fails', r['verdict'] == 'FAIL' and 'alive' in r['reason'], reason=r['reason'])
    r = maximizers(12, 56, 1, os.path.join(d, 'e.json'), fault_empty_mask=True); req('C_empty_mask_fails', r['verdict'] == 'FAIL' and 'empty mask' in r['reason'], reason=r['reason'])
    r = maximizers(24, 57, 1, os.path.join(d, 'p.json')); req('D_positive_multi', r['verdict'] == 'MAXIMIZERS' and r['maximizing_lane_count'] == 6 and r['U'] == 42, count=r.get('maximizing_lane_count'), families=r.get('family_count'), baseline=r.get('baseline_family_count'))
    r = maximizers(24, 57, 1, os.path.join(d, 't.json'), max_list=2); req('E_truncation_reported', r['verdict'] == 'MAXIMIZERS' and r['list_truncated'] and r['maximizing_lane_count'] == 6 and len(r['maximizers']) == 2)
    out['fails'] = fails
    return out, not fails


def supervised(W, U, workers, out_dir, kit=None, mode='witness'):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import w1a_harness as H
    H.CAPS['stage_s'] = 30 * 60
    if os.path.exists(out_dir) and os.listdir(out_dir):
        print('REFUSED: output folder exists and is not empty:', out_dir); sys.exit(3)
    os.makedirs(out_dir, exist_ok=True)
    kit = kit or out_dir
    sup = H.Supervisor(kit, out_dir); R = sup.receipts
    R['d1'] = {'W': W, 'U': U, 'workers': workers, 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), 'caps': {'step_wall_s': 25 * 60, 'step_cpu_s': 50 * 60}}
    if H.pressure_bad(sup.baseline):
        R['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); sys.exit(1)
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        R['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); sys.exit(1)
    outj = os.path.join(out_dir, '%s_W%d_%s%d.json' % (mode, W, 'U' if mode == 'witness' else 'K', U))
    R['d1']['mode'] = mode

    def m_witness(rc, text):
        try: d = json.load(open(outj))
        except Exception as e: return 'FAIL', 'no checkpoint: %r' % e
        return ('pass' if d.get('verdict') in ('ATTAINED', 'MISS', 'CENSUS-ATTAINED', 'MAXIMIZERS') and rc == 0 else 'FAIL'), '%s: %s' % (d.get('verdict'), d.get('reason'))
    r = sup.run_step('%s_W%d' % (mode, W), [sys.executable, os.path.abspath(__file__), mode, str(W), str(U), str(workers), outj], out_dir, 25 * 60, 50 * 60, m_witness)
    R['complete'] = r['verdict'] == 'pass'; R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); sup.save()
    print('DONE' if R['complete'] else 'STOP', r['verdict'], r['reason'], r.get('match_note'))
    sys.exit(0 if R['complete'] else 1)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'test':
        out, ok = tests(); print(json.dumps(out, indent=1, default=str)); print('TESTS', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
    if a[0] == 'maxtest':
        out, ok = maximizer_tests(); print(json.dumps(out, indent=1, default=str)); print('MAXTESTS', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
    if a[0] == 'witness' and len(a) == 5:
        r = witness_first(int(a[1]), int(a[2]), int(a[3]), a[4])
        print(r['verdict'], r['reason'], r.get('witness'), r['elapsed_s'], 's'); sys.exit(0 if r['verdict'] in ('ATTAINED', 'MISS') else 1)
    if a[0] == 'census' and len(a) == 5:
        r = census(int(a[1]), int(a[2]), int(a[3]), a[4])
        print(r['verdict'], r['reason'], r.get('witness'), r['elapsed_s'], 's'); sys.exit(0 if r['verdict'] == 'CENSUS-ATTAINED' else 1)
    if a[0] == 'maximizers' and len(a) == 5:
        r = maximizers(int(a[1]), int(a[2]), int(a[3]), a[4])
        print(r['verdict'], r['reason'], 'count', r.get('maximizer_count'), r['elapsed_s'], 's'); sys.exit(0 if r['verdict'] == 'MAXIMIZERS' else 1)
    if a[0] in ('run', 'runcensus', 'runmax') and len(a) in (5, 6):
        supervised(int(a[1]), int(a[2]), int(a[3]), a[4], a[5] if len(a) == 6 else None, mode={'run': 'witness', 'runcensus': 'census', 'runmax': 'maximizers'}[a[0]])
    print('usage: d1_engine.py test | witness W U WORKERS OUT.json | census W K WORKERS OUT.json | run W U WORKERS OUT_DIR [KIT] | runcensus W K WORKERS OUT_DIR [KIT]'); sys.exit(2)
