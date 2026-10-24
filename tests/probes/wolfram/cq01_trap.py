#!/usr/bin/env python3
"""CQ01 trap census, revision 1 (Local, 2026-10-24, L920; L919's next job (a)). NOT an agreed job until GPT accepts this exact file;
nothing runs on import; `--controls` runs the small CPU controls only.

If this holds, it changes the CQ01 row: L919 found that 11111 and 111101111 enter the kit's ether-and-wall trap (public kit 3eca23c,
Rule30Ether: etherTable, wallStates, trap_invariant), which makes column 1 of the driven right half eventually periodic; the kit's
not_finSupp_Psi_of_eventuallyPeriodic (Rule30PeriodTwoSideways) then gives CQ01 for that R. This job finds, for every right half R
supported in 1..16, the first time t1 < T at which the driven run (drv altCol R) is in the trap, and its phase s:
  - column 0 is altCol t = ether 3 (t + s) for every t exactly when s is odd (ether column B4 is 0, 1, 0, 1), so s is 1 or 3, j0 = 3;
  - at t1, columns 1..6 equal ether (3 + p) (t1 + s) (column 6 is a B3: (3 + 6) % 7 = 2), and columns 7..19 are a wall state at phase
    (t1 + s) % 4, one of the kit's 109 wallStates (transcribed below as WALL_STATES from Rule30Ether.lean, sha256 KIT_ETHER_SHA256).
By trap_invariant (any IsR30 F, here drv altCol R by drv_isR30) the run stays in the trap at every later time, so each entry is a finite
certificate of CQ01 for R, composed with the kit's Lean theorems (the composition is L919's, under GPT's carrying read). Two right halves
that enter with the same phase and have equal column 1 at every odd time before the later entry have equal u, hence equal Psi.
Measured (B = 16, T = 2,000): per lane, the first entry time (-1 if none before T) and phase (0 if none), retained; the counts by phase
and an entry-time histogram; for L913's 82 kernel groups (input: the retained kernel result, sha256 KERNEL_RESULT_SHA256, read with a size
bound before hashing), each member's entry and, against the group's first member, whether the pair is trap-certified equal (both entered,
one phase, equal column 1 at every odd time before the later entry); the visible words (column 1 at odd times, T/2 bits) of every group
lane, retained as hex, so the gate recomputes every certificate and checks every post-entry bit against the trap (column 1 is ether
column 4 at phase t + s after entry).
Controls (`--controls`, and inside the run before the stage's work):
  - the kit's own trap configurations: for every wall state ws at phase s % 4 with s odd, the kit's config 3 s 6 ws (ether columns 1..6
    at phase s, ws on 7..19, white beyond) is detected in the trap at t = 0 with phase s;
  - the lane-word detector equals an independent per-row detector (one Python int per row) on every R supported in 1..10 at T = 200;
  - after entry, every entered lane of the previous control keeps columns 1..6 equal to the ether through T (trap_invariant's claim,
    checked numerically; a failure would mean a transcription or indexing error);
  - three mutants, each of which must fail a control: 'phase2' (even phases s = 0, 2), 'k5' (the B3 at column 5), 'wallrev' (wall states
    read right to left).
In the run, after the census: an independent per-row re-check of 200 seeded entered lanes (entry state recomputed, post-entry column 1
equal to ether 4 (t + s) through T), required all true.
The result gate (GC1813, GC1818, GC1821, GC1823, GC1825): strict reading, one explicit schema in the order types, exact key sets, domains,
cross-field bindings, arithmetic, completion, fail-closed, on bounded bytes; counts and histogram recomputed from the per-lane arrays;
the groups bound to the input; every group certificate recomputed from the retained words and entries; the 200-lane re-check selection
recomputed by the same seeded helper. Every negative fixture states its exact diagnostic.
Proposed stage: B = 16, T = 2,000 (the only admitted stage scope); W1A caps: stage, step wall and CPU 600 s, group RSS 4 GiB, artifacts
50 MiB, log 10 MiB. Cost ESTIMATE: the exact lane evolution is about T^2 / 2 updates of 65,536-bit words (L913's lane pass did 3,200 in
7.6 s, so about 3 s); the trap test adds about 720 word operations per step; the result about 1.5 MB. `run` also admits 10 <= B <= 16,
200 <= T <= 2,000, even, for disclosed tiny development runs.
Predictions (written before any run of this file, after L919's two-lane certificate):
  - every one of the 970 members of L913's 81 stable groups enters before T with one phase per group, and all 81 groups are fully
    trap-certified (every member certified equal to the group's first);
  - the member that left the 82nd group at visible bit 1,677 is not certified equal to that group's first member;
  - at least 25% of the 65,536 right halves enter before T;
  - R = {} and R = {1} do not enter before T.
Counterfactual: a stable-group member that never enters, or a stable group with two phases, says the trap is not the whole second
mechanism; fewer than 5% entering says absorption is rare at this size. Results between are inconclusive. Entry certifies CQ01 only for
the entering R; no finite census decides CQ01 or the empty milestone.
Usage: python3 cq01_trap.py --controls | run OUT KERNEL_RESULT B T | stage OUT KERNEL_RESULT B T
"""
import hashlib, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
KERNEL_SHA256 = 'de6c178d37c1a78fc17a35c92b0b8ba7f5388c661e3eb3054c931adb5a7bc83b'
KERNEL_RESULT_SHA256 = '16c70bf3832a2aca776f02405020ec964610a2db02df100bab9a2ae3e2f3488e'
KIT_ETHER_SHA256 = 'dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_SCOPE = (16, 2000)
STAGE_S = 600
SEED = 20261024
N_RECHECK = 200
MAX_INPUT_BYTES = 16 << 20
J0, K = 3, 6
ETHER = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]   # etherTable: B1 B2 B3 B4 B5 c c
WALL_STATES = [(0, '0001010100000'), (0, '0001010100001'), (0, '0001010100010'), (0, '0001010100011'), (0, '0001010100100'), (0, '0001010100101'), (0, '0001010100111'), (0, '0001010110000'), (0, '0001010110001'), (0, '0001010110011'), (0, '0001010110110'), (0, '0100000100000'), (0, '0100000100001'), (0, '0100000100100'), (0, '0100000100101'), (0, '0100000101000'), (0, '0100000101001'), (0, '0100000101010'), (0, '0100000101011'), (0, '0100000101100'), (0, '0100000101101'), (0, '0100000101110'), (0, '0100000101111'), (0, '0100000110000'), (0, '0100000110001'), (0, '0100000110011'), (1, '0110001101000'), (1, '0110001101001'), (1, '0110001101010'), (1, '0110001101011'), (1, '0110001101100'), (1, '0110001101101'), (1, '0110001101110'), (1, '0110001101111'), (1, '0110001110000'), (1, '0110001110001'), (1, '0110001110011'), (1, '0110001111101'), (1, '0110001111110'), (1, '0110001111111'), (1, '1011010100100'), (1, '1011010100101'), (1, '1011010101000'), (1, '1011010101001'), (1, '1011010101011'), (1, '1011010101110'), (1, '1011010110000'), (1, '1011010110001'), (1, '1011010110011'), (1, '1011010110110'), (1, '1011010110111'), (1, '1011010111100'), (1, '1011010111101'), (1, '1011010111110'), (1, '1011010111111'), (2, '0010010100000'), (2, '0010010100001'), (2, '0010010100010'), (2, '0010010100011'), (2, '0010010100100'), (2, '0010010100101'), (2, '0010010101000'), (2, '0010010101001'), (2, '0010010101010'), (2, '0010010101011'), (2, '0010010101100'), (2, '0010010101101'), (2, '0010010101110'), (2, '0010010101111'), (2, '0010010111101'), (2, '0010010111110'), (2, '0010010111111'), (2, '0101011000000'), (2, '0101011000001'), (2, '0101011001000'), (2, '0101011001001'), (2, '0101011001010'), (2, '0101011001011'), (2, '0101011001100'), (2, '0101011001101'), (2, '0101011001110'), (2, '0101011001111'), (3, '0111110100000'), (3, '0111110100001'), (3, '0111110101000'), (3, '0111110101001'), (3, '0111110101010'), (3, '0111110101011'), (3, '0111110101100'), (3, '0111110101101'), (3, '0111110101111'), (3, '0111110110000'), (3, '0111110110001'), (3, '0111110110011'), (3, '0111110110110'), (3, '0111110110111'), (3, '0111110111101'), (3, '0111110111110'), (3, '0111110111111'), (3, '1101010100000'), (3, '1101010100001'), (3, '1101010100011'), (3, '1101010111000'), (3, '1101010111001'), (3, '1101010111010'), (3, '1101010111011'), (3, '1101010111100'), (3, '1101010111101'), (3, '1101010111111')]
MUTANTS = ('phase2', 'k5', 'wallrev')
BASE_KEYS = ('kit_configs_detected_at_t0', 'lane_detector_equals_row_detector_B10_T200', 'post_entry_ether_kept_B10_T200')
PARSE_FAIL = 'parse: nonfinite or invalid JSON'


def deps():
    import cq01_kernel as KX
    if hashlib.sha256(open(KX.__file__, 'rb').read()).hexdigest() != KERNEL_SHA256:
        raise SystemExit('REFUSED: cq01_kernel.py is not the pinned bytes')
    X, M, C = KX.deps()
    return KX, M


def ether(j, ph):
    return ETHER[j % 7][ph % 4]


def phases(mutant=''):
    return (0, 2) if mutant == 'phase2' else (1, 3)


def kk(mutant=''):
    return 5 if mutant == 'k5' else K


def walls(mutant=''):
    """Wall states by phase, as tuples of 13 bits (column k + 1 first)."""
    out = {}
    for ph, bits in WALL_STATES:
        b = tuple(int(c) for c in bits)
        out.setdefault(ph, set()).add(b[::-1] if mutant == 'wallrev' else b)
    return out


def row_in_trap(cells, t, s, mutant=''):
    """cells: a list with cells[p] the value of column p (p >= 1); True if in the trap at time t with phase s."""
    k = kk(mutant)
    return (all(cells[p] == ether(J0 + p, t + s) for p in range(1, k + 1))
            and tuple(cells[k + 1:k + 14]) in walls(mutant).get((t + s) % 4, set()))


def row_census(r, B, T, mutant=''):
    """Independent per-row engine on one Python int (bit x is cell x, bit 0 the wall): first (t, s) in the trap, column 1 at every time,
    and whether columns 1..k stay the ether after entry."""
    k = kk(mutant); wl = walls(mutant)
    eth = {(ph, s): sum(ether(J0 + p, ph + s) << (p - 1) for p in range(1, k + 1)) for ph in range(4) for s in (0, 1, 2, 3)}
    wint = {ph: {sum(b << i for i, b in enumerate(st)) for st in sts} for ph, sts in wl.items()}
    mk, m13 = (1 << k) - 1, (1 << 13) - 1
    w = r << 1; entry = None; col1 = []; kept = True
    for t in range(T):
        w = (w & ~1) | (1 if t % 2 == 0 else 0)
        col1.append((w >> 1) & 1)
        low = (w >> 1) & mk
        if entry is None:
            for s in phases(mutant):
                if low == eth[(t % 4, s)] and ((w >> (k + 1)) & m13) in wint.get((t + s) % 4, ()): entry = (t, s); break
        elif low != eth[(t % 4, entry[1])]: kept = False
        w = ((w << 1) ^ (w | (w >> 1))) & ~1
    return entry, col1, kept


def lane_census(B, T, mutant=''):
    """Lane-word engine over all 2^B right halves: first entry time and phase per lane, and column 1 at odd times as lane words."""
    import numpy as np
    KX, M = deps()
    n = 1 << B; ALL = (1 << n) - 1; P = B + T + 2
    w = [0] * (P + 2)
    for p in range(1, B + 1): w[p] = sum(1 << r for r in range(n) if (r >> (p - 1)) & 1)
    entered = 0; entry_t = np.full(n, -1, dtype=np.int64); entry_s = np.zeros(n, dtype=np.int64); U = []
    k = kk(mutant); wl = walls(mutant)
    def lanes_of(x):
        return np.flatnonzero(np.unpackbits(np.frombuffer(x.to_bytes((n + 7) // 8, 'little'), dtype=np.uint8), bitorder='little')[:n])
    for t in range(T):
        w[0] = ALL if t % 2 == 0 else 0
        for s in phases(mutant):
            m = ALL & ~entered
            for p in range(1, k + 1):
                m &= w[p] if ether(J0 + p, t + s) else ~w[p]
                if not m: break
            if m:
                inw = 0
                for st in wl.get((t + s) % 4, ()):
                    x = m
                    for i, bit in enumerate(st):
                        x &= w[k + 1 + i] if bit else ~w[k + 1 + i]
                        if not x: break
                    inw |= x
                m &= inw
            if m:
                idx = lanes_of(m); entry_t[idx] = t; entry_s[idx] = s; entered |= m
        nw = [0] * (P + 2); prev = w[0]
        for x in range(1, P + 1):
            nw[x] = prev ^ (w[x] | w[x + 1]); prev = w[x]
        nw[0] = 0; w = nw
        if t % 2 == 0: U.append(w[1])
    return entry_t, entry_s, U


def load_kernel(path):
    with open(path, 'rb') as f:
        raw = f.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES: raise SystemExit('REFUSED: the kernel result exceeds the input bound')
    if hashlib.sha256(raw).hexdigest() != KERNEL_RESULT_SHA256: raise SystemExit('REFUSED: the kernel result is not the pinned bytes')
    return json.loads(raw)['merged']['groups']


def word_of(U, r, V):
    return sum(((U[s] >> r) & 1) << s for s in range(V))


def certified(ea, sa, eb, sb, wa, wb):
    """Two lanes are trap-certified equal: both entered, one phase, and equal column 1 at every odd time before the later entry."""
    if ea < 0 or eb < 0 or sa != sb: return False
    tmax = max(ea, eb); V = (tmax + 1) // 2          # the visible bits s with 2s + 1 <= tmax (one more than needed, harmless)
    mask = (1 << V) - 1
    return (wa & mask) == (wb & mask)


def recheck_lanes(entry_t, n):
    """The seeded re-check selection among entered lanes (producer and gate)."""
    import numpy as np
    ent = [r for r in range(n) if entry_t[r] >= 0]
    if not ent: return []
    rng = np.random.Generator(np.random.PCG64(SEED))
    return sorted(int(x) for x in rng.choice(ent, size=min(N_RECHECK, len(ent)), replace=False))


def group_section(groups, entry_t, entry_s, words):
    out = []
    for g in groups:
        f = g[0]
        out.append({'entries': [[int(entry_t[r]), int(entry_s[r])] for r in g],
                    'certified': [certified(int(entry_t[f]), int(entry_s[f]), int(entry_t[r]), int(entry_s[r]), words[f], words[r]) for r in g[1:]]})
    return out


def assemble(B, T, groups, mutant=''):
    import numpy as np
    n = 1 << B; V = T // 2; t0 = time.monotonic()
    entry_t, entry_s, U = lane_census(B, T, mutant)
    census_s = time.monotonic() - t0
    glanes = sorted({r for g in groups for r in g})
    words = {r: word_of(U, r, V) for r in glanes}
    hexlen = (V + 3) // 4
    gs = group_section(groups, entry_t, entry_s, words)
    rc = recheck_lanes(entry_t, n); rres = []
    for r in rc:
        e, col1, kept = row_census(r, B, T, mutant)
        rres.append(bool(e == (int(entry_t[r]), int(entry_s[r])) and kept and all(col1[t] == ether(J0 + 1, t + e[1]) for t in range(e[0], T))))
    et = [int(x) for x in entry_t]; es = [int(x) for x in entry_s]
    hist = {}
    for x in et:
        if x >= 0: hist[str(x // 100)] = hist.get(str(x // 100), 0) + 1
    return ({'entry_t': et, 'entry_s': es, 'counts': {'entered': sum(1 for x in et if x >= 0), 'phase1': es.count(1), 'phase3': es.count(3), 'lanes': n},
             'hist100': hist, 'words': {str(r): format(words[r], 'x').rjust(hexlen, '0') for r in glanes}, 'groups': groups, 'group_certs': gs,
             'recheck': {'lanes': rc, 'ok': rres}},
            {'census_s': round(census_s, 2), 'total_s': round(time.monotonic() - t0, 2)})


def controls(mutant=''):
    res = {}
    ok = True
    for ph, bits in WALL_STATES:
        for s in (1, 3):
            if s % 4 != ph: continue
            cells = [0] * 40
            for p in range(1, K + 1): cells[p] = ether(J0 + p, s)
            for i, c in enumerate(bits): cells[K + 1 + i] = int(c)
            r = sum(cells[p] << (p - 1) for p in range(1, 20))
            e, _, _ = row_census(r, 19, 1, mutant)
            if e != (0, s): ok = False
    res['kit_configs_detected_at_t0'] = ok
    import numpy as np
    et, es, U = lane_census(10, 200, mutant)
    ok = True; kept_all = True
    for r in range(1 << 10):
        e, col1, kept = row_census(r, 10, 200)
        if (e or (-1, 0)) != (int(et[r]), int(es[r])): ok = False
        if e is not None and not kept: kept_all = False
    res['lane_detector_equals_row_detector_B10_T200'] = ok
    res['post_entry_ether_kept_B10_T200'] = kept_all and any(int(x) >= 0 for x in et)
    return res


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 TRAP CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, kpath, B, T):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic(); deps()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'kernel_result_sha256': KERNEL_RESULT_SHA256, 'kit_ether_sha256': KIT_ETHER_SHA256, 'scope': {'B': B, 'T': T}, 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_trap_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'cq01_trap_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    groups = [g for g in load_kernel(kpath) if max(g) < (1 << B)]
    sections, timing = assemble(B, T, groups)
    R.update(sections); R['timing'] = timing
    R['complete'] = all(R['recheck']['ok']) and len(R['recheck']['ok']) == len(R['recheck']['lanes'])
    if not R['complete']: R['stopped'] = 'incomplete: an independent re-check failed (no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 16 << 20
TOP_KEYS = {'started', 'finished', 'elapsed_s', 'this_sha256', 'kernel_result_sha256', 'kit_ether_sha256', 'scope', 'controls', 'gate_controls',
            'entry_t', 'entry_s', 'counts', 'hist100', 'words', 'groups', 'group_certs', 'recheck', 'timing', 'complete'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}
RECHECK_FAIL = 'bindings: an independent re-check failed'


def validate_result(d, src_sha, B, T, groups_in):
    isint = lambda x: type(x) is int
    fin = lambda x: (type(x) is int or (type(x) is float and math.isfinite(x)))
    n = 1 << B; V = T // 2; hexlen = (V + 3) // 4
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('this_sha256', str), ('kernel_result_sha256', str), ('kit_ether_sha256', str), ('started', str), ('finished', str),
                   ('scope', dict), ('controls', dict), ('gate_controls', dict), ('entry_t', list), ('entry_s', list), ('counts', dict),
                   ('hist100', dict), ('words', dict), ('groups', list), ('group_certs', list), ('recheck', dict), ('timing', dict), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float): return 'types: elapsed_s'
    c = d['controls']
    if not isinstance(c.get('base'), dict) or not all(isinstance(c.get(m), dict) for m in MUTANTS): return 'types: control reports'
    if not all(isinstance(g, dict) and isinstance(g.get('entries'), list) and isinstance(g.get('certified'), list) for g in d['group_certs']): return 'types: group certificates'
    if not (isinstance(d['recheck'].get('lanes'), list) and isinstance(d['recheck'].get('ok'), list)): return 'types: recheck'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['scope']) != {'B', 'T'}: return 'keys: scope'
    if set(c) != CONTROL_KEYS: return 'keys: controls'
    if set(c['base']) != set(BASE_KEYS) or not all(set(c[m]) == set(BASE_KEYS) for m in MUTANTS): return 'keys: base or mutant reports'
    if set(d['gate_controls']) != set(GATE_KEYS): return 'keys: gate controls'
    if set(d['counts']) != {'entered', 'phase1', 'phase3', 'lanes'} or set(d['recheck']) != {'lanes', 'ok'} or set(d['timing']) != {'census_s', 'total_s'}:
        return 'keys: sections'
    glanes = sorted({r for g in groups_in for r in g})
    if set(d['words']) != {str(r) for r in glanes}: return 'keys: words'
    if not all(set(g) == {'entries', 'certified'} for g in d['group_certs']): return 'keys: group certificates'
    # 3. domains
    if d['this_sha256'] != src_sha: return 'domains: source digest'
    if d['kernel_result_sha256'] != KERNEL_RESULT_SHA256 or d['kit_ether_sha256'] != KIT_ETHER_SHA256: return 'domains: input digests'
    if d['scope'] != {'B': B, 'T': T}: return 'domains: scope'
    if not all(type(v) is bool for v in list(c['base'].values()) + [x for m in MUTANTS for x in c[m].values()] + [c[m + '_caught'] for m in MUTANTS] + [c['base_all_pass'], c['ok']]):
        return 'domains: control values not Boolean'
    if not all(v is True for v in d['gate_controls'].values()): return 'domains: a gate control is not true'
    if not all(fin(x) and x >= 0 for x in [d['elapsed_s']] + list(d['timing'].values())): return 'domains: timing'
    et, es = d['entry_t'], d['entry_s']
    if not (len(et) == n and len(es) == n and all(isint(x) and -1 <= x < T for x in et) and all(isint(x) and x in (0, 1, 3) for x in es)
            and all((a < 0) == (b == 0) for a, b in zip(et, es))): return 'domains: entries'
    if not all(isinstance(v, str) and len(v) == hexlen and all(ch in '0123456789abcdef' for ch in v) and int(v, 16) < (1 << V) for v in d['words'].values()):
        return 'domains: words'
    if not all(isinstance(k, str) and k.isdigit() and isint(v) and v >= 1 for k, v in d['hist100'].items()): return 'domains: histogram'
    if not (all(isint(x) and 0 <= x < n for x in d['recheck']['lanes']) and all(type(x) is bool for x in d['recheck']['ok'])
            and len(d['recheck']['ok']) == len(d['recheck']['lanes'])): return 'domains: recheck'
    # 4. cross-field bindings
    if not all(c['base'][k] is True for k in BASE_KEYS) or c['base_all_pass'] is not True: return 'bindings: base controls'
    for m in MUTANTS:
        if c[m + '_caught'] is not True or all(c[m][k] for k in BASE_KEYS): return 'bindings: mutant %s not caught by its own outcomes' % m
    if c['ok'] is not True: return 'bindings: controls ok flag'
    if d['groups'] != groups_in: return 'bindings: groups are not the retained kernel groups'
    if d['recheck']['lanes'] != recheck_lanes(et, n): return 'bindings: re-check lanes are not the seeded selection'
    if not all(d['recheck']['ok']): return RECHECK_FAIL
    # 5. arithmetic
    if d['counts'] != {'entered': sum(1 for x in et if x >= 0), 'phase1': es.count(1), 'phase3': es.count(3), 'lanes': n}: return 'arithmetic: counts'
    hist = {}
    for x in et:
        if x >= 0: hist[str(x // 100)] = hist.get(str(x // 100), 0) + 1
    if d['hist100'] != hist: return 'arithmetic: histogram'
    words = {int(k): int(v, 16) for k, v in d['words'].items()}
    for r, w in words.items():                       # trap_invariant: after entry, column 1 is ether column 4 at phase t + s
        if et[r] >= 0 and any(((w >> v) & 1) != ether(J0 + 1, 2 * v + 1 + es[r]) for v in range(V) if 2 * v + 1 >= et[r]):
            return 'arithmetic: a word disagrees with its trap after entry'
    if d['group_certs'] != group_section(groups_in, et, es, words): return 'arithmetic: group certificates'
    # 6. completion
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, B, T, groups_in):
    KX, M = deps()
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = M.strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate_result(d, src_sha, B, T, groups_in)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'CQ01 trap census complete, every re-check held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


GATE_B, GATE_T = 10, 200
GATE_GROUPS = [[31, 495], [112, 944], [37, 39, 41]]      # synthetic: real lanes in 1..10, not required to be merged


def gate_fixtures():
    nan = float('nan')
    def first_entered(d): return next(r for r, x in enumerate(d['entry_t']) if x >= 0)
    def flip_cert(d):
        g = d['group_certs'][0]; g['certified'][0] = not g['certified'][0]
    def word_change(d):                  # a visible bit before entry (time 1) of lane 31, which enters at t = 9
        v = int(d['words']['31'], 16) ^ 1; d['words']['31'] = format(v, 'x').rjust(len(d['words']['31']), '0')
    def word_after_entry(d):             # the last visible bit of lane 31, long after its entry
        V = GATE_T // 2; v = int(d['words']['31'], 16) ^ (1 << (V - 1)); d['words']['31'] = format(v, 'x').rjust(len(d['words']['31']), '0')
    return [
        ('good_full_packet_passes', 'file', lambda d: None, None),
        ('types_entry_t_dict', 'file', lambda d: d.__setitem__('entry_t', {}), 'types: entry_t'),
        ('types_started_dict', 'file', lambda d: d.__setitem__('started', {}), 'types: started'),
        ('types_elapsed_string', 'file', lambda d: d.__setitem__('elapsed_s', '1'), 'types: elapsed_s'),
        ('keys_extra_top_key', 'file', lambda d: d.__setitem__('extra', 1), "keys: top level ['extra']"),
        ('keys_stopped_present', 'file', lambda d: d.__setitem__('stopped', 'x'), "keys: top level ['stopped']"),
        ('keys_word_missing', 'file', lambda d: d['words'].pop(sorted(d['words'], key=int)[0]), 'keys: words'),
        ('domains_wrong_digest', 'file', lambda d: d.__setitem__('this_sha256', '0' * 64), 'domains: source digest'),
        ('domains_wrong_kit_digest', 'file', lambda d: d.__setitem__('kit_ether_sha256', '0' * 64), 'domains: input digests'),
        ('domains_wrong_scope', 'file', lambda d: d['scope'].__setitem__('T', 202), 'domains: scope'),
        ('domains_negative_timing', 'file', lambda d: d['timing'].__setitem__('census_s', -1.0), 'domains: timing'),
        ('domains_nan_elapsed', 'memory', lambda d: d.__setitem__('elapsed_s', nan), 'domains: timing'),
        ('domains_inf_timing', 'memory', lambda d: d['timing'].__setitem__('total_s', float('inf')), 'domains: timing'),
        ('domains_entry_phase_even', 'file', lambda d: d['entry_s'].__setitem__(first_entered(d), 2), 'domains: entries'),
        ('domains_entry_without_phase', 'file', lambda d: d['entry_s'].__setitem__(first_entered(d), 0), 'domains: entries'),
        ('domains_entry_beyond_T', 'file', lambda d: d['entry_t'].__setitem__(first_entered(d), GATE_T), 'domains: entries'),
        ('domains_word_not_hex', 'file', lambda d: d['words'].__setitem__(sorted(d['words'], key=int)[0], 'z' * len(d['words'][sorted(d['words'], key=int)[0]])), 'domains: words'),
        ('parse_nan_token', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": NaN, "x_": ', 1), PARSE_FAIL),
        ('parse_exponent_overflow', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": 1e999, "x_": ', 1), PARSE_FAIL),
        ('bindings_explicit_false_base', 'file', lambda d: d['controls']['base'].__setitem__(BASE_KEYS[0], False), 'bindings: base controls'),
        ('bindings_mutant_all_true', 'file', lambda d: [d['controls'].__setitem__(m, {k: True for k in BASE_KEYS}) for m in MUTANTS],
         'bindings: mutant %s not caught by its own outcomes' % MUTANTS[0]),
        ('bindings_group_dropped', 'file', lambda d: d['groups'].pop(), 'bindings: groups are not the retained kernel groups'),
        ('bindings_recheck_lanes_changed', 'file', lambda d: d['recheck']['lanes'].__setitem__(0, (d['recheck']['lanes'][0] + 1) % (1 << GATE_B)),
         'bindings: re-check lanes are not the seeded selection'),
        ('bindings_recheck_failed', 'file', lambda d: d['recheck']['ok'].__setitem__(0, False), RECHECK_FAIL),
        ('arithmetic_counts', 'file', lambda d: d['counts'].__setitem__('entered', d['counts']['entered'] + 1), 'arithmetic: counts'),
        ('arithmetic_histogram', 'file', lambda d: d['hist100'].__setitem__('0', d['hist100'].get('0', 0) + 1), 'arithmetic: histogram'),
        ('arithmetic_cert_flipped', 'file', flip_cert, 'arithmetic: group certificates'),
        ('arithmetic_word_changed', 'file', word_change, 'arithmetic: group certificates'),
        ('arithmetic_word_after_entry', 'file', word_after_entry, 'arithmetic: a word disagrees with its trap after entry'),
        ('completion_flag_false', 'file', lambda d: d.__setitem__('complete', False), 'completion: complete flag'),
    ]


GATE_KEYS = ('good_full_packet_passes', 'types_entry_t_dict', 'types_started_dict', 'types_elapsed_string', 'keys_extra_top_key',
             'keys_stopped_present', 'keys_word_missing', 'domains_wrong_digest', 'domains_wrong_kit_digest', 'domains_wrong_scope',
             'domains_negative_timing', 'domains_nan_elapsed', 'domains_inf_timing', 'domains_entry_phase_even', 'domains_entry_without_phase',
             'domains_entry_beyond_T', 'domains_word_not_hex', 'parse_nan_token', 'parse_exponent_overflow', 'bindings_explicit_false_base',
             'bindings_mutant_all_true', 'bindings_group_dropped', 'bindings_recheck_lanes_changed', 'bindings_recheck_failed',
             'arithmetic_counts', 'arithmetic_histogram', 'arithmetic_cert_flipped', 'arithmetic_word_changed', 'arithmetic_word_after_entry',
             'completion_flag_false')


def gate_controls():
    import copy, tempfile
    sections, timing = assemble(GATE_B, GATE_T, GATE_GROUPS)
    sections = json.loads(json.dumps(sections, allow_nan=False))
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'finished': 'f', 'elapsed_s': 0.1, 'this_sha256': 'S', 'kernel_result_sha256': KERNEL_RESULT_SHA256,
            'kit_ether_sha256': KIT_ETHER_SHA256, 'scope': {'B': GATE_B, 'T': GATE_T},
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'timing': timing, 'complete': True, **sections}
    res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', GATE_B, GATE_T, GATE_GROUPS)
        for name, kind, f, want in gate_fixtures():
            bad = copy.deepcopy(good)
            if kind == 'memory':
                f(bad); res[name] = validate_result(bad, 'S', GATE_B, GATE_T, GATE_GROUPS) == want; continue
            if kind == 'text':
                open(rp, 'w').write(f(json.dumps(bad, allow_nan=False)))
            else:
                f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            verdict, note = m(0, '')
            res[name] = (verdict == 'pass') if want is None else (verdict == 'FAIL' and note == (want if kind == 'text' else 'rc 0: ' + want))
    assert set(res) == set(GATE_KEYS) and len(res) == len(GATE_KEYS)
    return res


def stage(out, kpath, B, T):
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if (B, T) != STAGE_SCOPE:
        print('REFUSED: the only admitted stage scope is B = 16, T = 2000'); return 3
    groups = load_kernel(kpath); deps()
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01_trap'] = {'this_sha256': src_sha, 'kernel_sha256': KERNEL_SHA256, 'kernel_result_sha256': KERNEL_RESULT_SHA256, 'kit_ether_sha256': KIT_ETHER_SHA256,
                       'w1a_sha256': W1A_SHA256, 'scope': {'B': B, 'T': T},
                       'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_trap_result.json'), src_sha, B, T, groups)
    rec = sup.run_step('cq01_trap', [sys.executable, os.path.abspath(__file__), 'run', rdir, os.path.abspath(kpath), str(B), str(T)], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 5 and a[0] in ('run', 'stage'):
        B, T = int(a[3]), int(a[4])
        if a[0] == 'run':
            if not (10 <= B <= 16 and 200 <= T <= 2000 and T % 2 == 0): print('REFUSED: run admits 10 <= B <= 16, 200 <= T <= 2000, T even'); sys.exit(3)
            R = run(a[1], a[2], B, T); print('CQ01 TRAP RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
        sys.exit(stage(a[1], a[2], B, T))
    print(__doc__); sys.exit(2)
