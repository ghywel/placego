#!/usr/bin/env python3
"""CQ01 collisions of R -> Psi R, revision 2 (Local, 2026-10-24, L909; GPT's GC1821: the seeded whole-line selection is bound in producer
and gate from the retained labels, exactly the selected pairs, every selected attempt retained with its prefix, a stage-scope count of
twelve; the depth-2 truth table as an exact check; the largest class's least lane defined globally; the mechanism worded as front healing,
not invisibility). Revision 1 (L908; L907's next job, with GPT's GC1820 reading). NOT an agreed job
until GPT accepts this exact file; nothing runs on import; `--controls` runs the small CPU controls only.

If this holds, it changes the CQ01 row: L907 found R -> Psi R 1..800 far from injective on the 65,536 right halves R supported in
1..16 (31,478 classes). GC1820: by the kit's recon_local and recon_aff (Rule30ZeroBoundary, pin 2f63afda, lines 564-610) and Psi_col
(trace a(2s) = black, a(2s + 1) = not u R s), a first visible difference at index s gives the first Psi difference at depth 2s + 2,
so equality of Psi R 1..K is exactly equality of the first floor(K / 2) visible bits u R s (column 1 at time 2s + 1). The collisions are
in the driven right-visible map, not in reconstruction. This job asks where the right half's information is lost, cell by cell, and
tests one mechanism from the record: RULE30-PRIZE.md section 8.66's front identity (a difference never reaches a lower diagonal; the
damage heals on its left exactly when the undamaged diagonal below it is black). Near the wall, position 0 is overwritten by the wall,
so a cell 1 flip loses its lowest damaged diagonal at the next step. That is front healing, NOT invisibility (GC1821): directly,
u R 0 = 1 xor (R1 or R2) and Psi R 2 = u R 0, so a cell 1 flip first differs at depth 2 exactly when R2 is white, a cell 2 flip exactly
when R1 is white, and no other cell's flip differs at depth 2; f_1 and f_2 are at most 1/2. The gate checks this truth table pair by pair.

Measured (B = 16, K = 800, all R supported in 1..B, lane r is R p = bit p - 1 of r). Weighting: per right half (uniform R) unless a
quantity is a class count (unique classes); the two are kept separate (GC1820).
  - the class counts of Psi R 1..k at each k in PREFIX_DEPTHS (bound to L907's retained counts); at depth K the per-lane class labels
    (retained), the class-size histogram, the largest class (size, least lane, right half), and the class counts among the R supported
    in 1..B' for B' = 0..B (restricted supports: how many classes each added cell adds; GC1820 asks for these about L904's stall);
  - the number of classes of u R 0..K/2 - 1 and whether the two partitions are equal (the kit consequence above, checked numerically);
  - for each cell p = 1..B, over the 2^(B-1) pairs (r, r + 2^(p-1)), r ascending with bit p - 1 clear: the first depth at which Psi
    differs, 0 if equal through depth K (retained per pair). Equal through K is RIGHT-CENSORED at K/2 visible bits, never eternal
    equality (GC1820). Every first difference must be even and at least p (kit consequence and light cone). Summaries: the number equal
    through K, the first-difference histogram, its minimum and lower median, and the neighbour groups at time 0 (cell p - 1, cell p + 1;
    the wall black at time 0 for p = 1, cell B + 1 white for p = B) with [pairs, equal through K]. A single-cell flip finds edges inside
    classes, not all equal pairs: two members may differ in several cells (GC1820);
  - an independent whole-line check: select_pairs, from the retained labels alone, takes the classes of size >= 2 in label order, lets
    numpy PCG64 seed 20261024 choose min(12, eligible) of them without replacement, sorted, and gives each class's two least lanes R, R'.
    Both run on the whole line by cq01_census.whole_line from glue(truncate(Psi R, 400), R) and glue(truncate(Psi R, 400), R'); both
    must fail at d, the first black depth of Psi R beyond 400, with equal visible words while alternating. Every selected attempt is
    retained with Psi R 1..d (1..K if there is no black beyond 400), including a failure; the gate recomputes the selection and requires
    exactly it, and twelve pairs at the stage scope. d is checked against the retained prefix, not against an independent Psi.
Bindings to the retained per-R result (cited/cq01-per-r-20261024-2125/, result c4d37470...), at the stage scope: the class counts at the
eight depths equal PREFIX_L907; the extremal lane 29394's Psi R 1..800 has the sha256 MAX_LANE_SHA256 of its retained bits (both read from
that result by script).

Controls (`--controls`, CPU only, small; all must pass before a stage):
  - a single-lane Psi, cell by cell from the kit's definitions (not lane words), equals the lane bits for every R with B <= 4, K = 24;
  - the u-word partition equals the Psi partition for B <= 6, K = 40, and for B = 16, K = 16 (still splitting there: L907's 36);
  - the vectorized flip statistics equal direct pairwise comparison of single-lane Psi for B = 5, K = 40;
  - three mutants, each of which must fail a control: 'ulast' (the last visible bit dropped), 'flipbit' (the flip pairs r with
    r + 2^p), 'firstoff' (first-difference depths one too deep).
The result gate (GC1813, GC1818): strict reading, then one explicit schema in the order types, exact key sets, domains, cross-field
bindings, arithmetic, completion, fail-closed, on bounded bytes. Every summary is recomputed from the retained labels and first
differences: the class count, size histogram, largest class (the least lane among all classes of maximum size) and restricted counts from
the labels; each flip's equal count, histogram, minimum, median and neighbour groups from its first-difference list; first difference 0
exactly when the pair's labels agree; exact group pair counts; even depths and the light cone; the depth-2 truth table; the whole-line
selection and each retained prefix. The valid synthetic packet is assembled by the run's own code from a real tiny
computation (B = 3, K = 420); every negative fixture states its exact diagnostic.

Proposed stage: B = 16, K = 800 (the only admitted stage scope); W1A caps: stage, step wall and CPU 600 s, group RSS 4 GiB, artifacts
50 MiB, log 10 MiB. `run` also admits 3 <= B <= 16, 402 <= K <= 800, K even, for disclosed tiny development runs.
DISCLOSED before these predictions: while checking that the gate's synthetic packet is feasible, the class counts 5 of 8 (B = 3) and
9 of 16 (B = 4) at K = 420 were read. With L907's 31,478 at B = 16, the mean growth from B = 4 to 16 is about 1.97 per added cell. A first
draft (never committed or run) predicted collisions rising with p; this exposure and the wall's first-step healing reversed it.
Predictions (written before any run of this file):
  - the u-word partition equals the Psi partition at depth 800 (a failure is a bug; the run is then incomplete);
  - the restricted class count grows by a factor of at least 1.8 per added cell for every B' from 8 to 16;
  - the fraction equal through K, f_p, is largest at p = 1, and its rank correlation with p is at most -0.8;
  - for every p in 2..16 the fraction equal through K is higher when cell p - 1 is black at time 0 than when it is white (section
    8.66: first-step healing exactly when the diagonal below, cell p - 1, is black);
  - the largest class at depth 800 has at most 32 right halves;
  - all 12 whole-line pairs agree.
The rank correlation uses average ranks for ties and is undefined if f_p is constant (GC1821).
Counterfactual: f_1 not the largest, or a rank correlation of f_p with p at or above 0, rejects that prediction; the left-neighbour
prediction failing for most p rejects that one; a factor below 1.5 per cell at high B' says the high cells are hidden too. A failure
rejects these exploratory statistical predictions, not section 8.66's identity or every role for healing; a success is consistent with
first-step front healing but does not establish it as the cause (GC1821). Results between the margins are inconclusive. No finite run settles infinite
injectivity: a pair equal at depth 800 may differ deeper (GC1818, GC1820).
Usage: python3 cq01_collisions.py --controls | run OUT B K | stage OUT B K
OUTCOME (the one GC1822-accepted stage at revision 2, af4b7a7c, 2026-10-24 21:57:30 to 21:57:40 BST, L910): W1A pass, the strict gate
PASS, both stage bindings held; child wall 7.21 s, sampled group RSS 358,891,520 bytes. The u partition equals the Psi partition (31,478
classes): HELD. Restricted class counts 1, 2, 3, 5, 9, 17, 33, 65, 129, 256, 511, 1,010, 2,005, 3,984, 7,921, 15,781, 31,478 for
B' = 0..16, growth 1.977 to 1.996 per cell from B' = 8: HELD. f_p rises with p, from f_1 = f_2 = 0 to f_16 = 0.381 (rank correlation
+0.999): PREDICTION FAILED, counterfactual met (my first draft's direction was right; the B = 3, 4 exposure misled me). Left-black above
left-white for p = 3..16, a tie at zero for p = 2: INCONCLUSIVE. Largest class 236 (least lane 31): PREDICTION FAILED. All 12 whole-line
pairs agree: HELD. The depth-2 truth table exact (16,384, 16,384, 0). Read afterwards from the retained labels: two right-end moves
generate the partition exactly for B' <= 8 and hold for every applicable right half (L910).
"""
import hashlib, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PER_R_SHA256 = 'b46f509fb6052dec5dc026a895edddad1c6c2fe40b52ca59fe2ad70d8472b6fe'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_SCOPE = (16, 800)
STAGE_S = 600
SEED = 20261024
PREFIX_DEPTHS = (8, 16, 32, 64, 128, 256, 512, 800)
PREFIX_L907 = {"8": 8, "16": 36, "32": 296, "64": 2683, "128": 9505, "256": 24819, "512": 30996, "800": 31478}
MAX_LANE, MAX_LANE_SHA256 = 29394, 'cf90a3f34b0159a6f249d2a4175533959c953710c973369445c4ad8539a30813'
WL_PAIRS, WL_L = 12, 400
MUTANTS = ('ulast', 'flipbit', 'firstoff')
BASE_KEYS = ('single_lane_psi_equals_lane_bits_B_le_4_K24', 'u_partition_equals_psi_partition_B_le_6_K40_and_B16_K16',
             'flip_stats_equal_pairwise_single_lane_B5_K40')
GROUPS = ('00', '01', '10', '11')
GATE_B, GATE_K = 3, 420


def deps():
    import cq01_per_r_stats as M
    if hashlib.sha256(open(M.__file__, 'rb').read()).hexdigest() != PER_R_SHA256:
        raise SystemExit('REFUSED: cq01_per_r_stats.py is not the pinned bytes')
    return M, M.census()


def psi_single(R, K):
    """Psi R 1..K for one right half (R[p - 1] = cell p), cell by cell from the kit's definitions: the alternating wall drives positions
    1..B + T + 1; u_s = cell 1 at time 2s + 1; the trace a(2s) = 1, a(2s + 1) = 1 - u_s; Psi k = recon a k 0 with the whole triangle."""
    S = (K + 1) // 2; T = 2 * S; P = len(R) + T + 1
    w = [0] * (P + 2)
    for i, b in enumerate(R): w[i + 1] = b
    u = []
    for t in range(T):
        nw = [0] * (P + 2); prev = 1 if t % 2 == 0 else 0
        for x in range(1, P + 1):
            nw[x] = prev ^ (w[x] | w[x + 1]); prev = w[x]
        w = nw
        if t % 2 == 0: u.append(w[1])
    a = []
    for s in range(S): a += [1, 1 - u[s]]
    rows = [[0] * (len(a) + 1), a + [0]]
    for _ in range(K - 1):
        r1, r0 = rows[-1], rows[-2]
        rows.append([r1[t + 1] ^ (r1[t] | r0[t]) for t in range(len(r1) - 1)] + [0])
    return [rows[k][0] for k in range(1, K + 1)]


def labels(rows):
    """Class labels of the lanes by their bits in rows (shape (k, n)), and the class sizes."""
    import numpy as np
    packed = np.packbits(np.ascontiguousarray(rows.T), axis=1)
    _, inv, cnt = np.unique(packed, axis=0, return_inverse=True, return_counts=True)
    return inv.reshape(-1), cnt


def partition_equal(la, lb):
    import numpy as np
    pairs = la.astype(np.int64) * (int(lb.max()) + 1) + lb
    return int(np.unique(pairs).size) == int(la.max()) + 1 == int(lb.max()) + 1


def lower_median(h):
    items = sorted((int(k), v) for k, v in h.items()); need = (sum(v for _, v in items) - 1) // 2; acc = 0
    for x, v in items:
        acc += v
        if acc > need: return x


def pair_lanes(p, B):
    """The lanes r with bit p - 1 clear, ascending: pair i is (r_i, r_i + 2^(p - 1))."""
    return [r for r in range(1 << B) if not (r >> (p - 1)) & 1]


def neighbours(r, p, B):
    left = 1 if p == 1 else (r >> (p - 2)) & 1
    right = 0 if p == B else (r >> p) & 1
    return '%d%d' % (left, right)


def summarize_flip(first, p, B):
    """Summaries of one cell's first-difference list (0 = equal through K), in pure Python: the gate recomputes them the same way."""
    fh = {}
    for f in first:
        if f: fh[str(f)] = fh.get(str(f), 0) + 1
    g = {k: [0, 0] for k in GROUPS}
    for r, f in zip(pair_lanes(p, B), first):
        key = neighbours(r, p, B); g[key][0] += 1; g[key][1] += (f == 0)
    vis = [f for f in first if f]
    return {'pairs': len(first), 'equal_through_K': len(first) - len(vis), 'first_hist': fh, 'min_first': min(vis) if vis else None,
            'median_first': lower_median(fh) if fh else None, 'groups': g}


def flip_firsts(bits, lab, B, K, mutant=''):
    """Per cell p, the first depth at which Psi differs across each pair, 0 if equal through K (vectorized)."""
    import numpy as np
    n = 1 << B; ar = np.arange(n); out = {}
    for p in range(1, B + 1):
        bit = 1 << (p if mutant == 'flipbit' and p < B else p - 1)
        r = ar[(ar & (1 << (p - 1))) == 0]; r2 = r ^ bit
        eq = lab[r] == lab[r2]
        first = (bits[1:, r] != bits[1:, r2]).argmax(axis=0) + 1 + (1 if mutant == 'firstoff' else 0)
        first[eq] = 0
        out[str(p)] = [int(x) for x in first]
    return out


def compute(B, K, mutant=''):
    """Psi lane bits and u lane bits (u_0..u_(K/2 - 1))."""
    M, C = deps()
    psi, U, ALL = C.lane_psi(B, K)
    S = K // 2
    Uw = (U[:S - 1] + [0] + U[S:]) if mutant == 'ulast' else U          # 'ulast': the last visible bit dropped
    return M.lane_bits(psi, B, K), M.lane_bits([0] + Uw[:S], B, S)


def select_pairs(lab):
    """The seeded whole-line selection from the labels alone, used by producer and gate (GC1821): the classes of size >= 2 in label order,
    numpy PCG64 seed SEED chooses min(WL_PAIRS, eligible) without replacement, sorted; each gives its two least lanes."""
    import numpy as np
    lab = np.asarray(lab, dtype=np.int64); sizes = np.bincount(lab)
    elig = np.flatnonzero(sizes >= 2)
    if elig.size == 0: return []
    rng = np.random.Generator(np.random.PCG64(SEED))
    pick = sorted(int(x) for x in rng.choice(elig, size=min(WL_PAIRS, elig.size), replace=False))
    return [[int(x) for x in np.flatnonzero(lab == c)[:2]] for c in pick]


def whole_line_checks(bits, lab, B, K):
    """Every selected pair is attempted and retained, with Psi R 1..d of its first lane (1..K if no black beyond WL_L): no silent skip."""
    _, C = deps()
    out = []
    for lanes in select_pairs(lab):
        d = next((k for k in range(WL_L + 1, K + 1) if bits[k, lanes[0]]), None)
        prefix = [int(x) for x in bits[1:(d or K) + 1, lanes[0]]]
        if d is None:
            out.append({'lanes': lanes, 'L': WL_L, 'd_expected': None, 'f': [None, None], 'words_equal': False, 'prefix': prefix}); continue
        res = [C.whole_line(prefix[:WL_L], [(r >> j) & 1 for j in range(B)], d + 2) for r in lanes]
        out.append({'lanes': lanes, 'L': WL_L, 'd_expected': d, 'f': [res[0][0], res[1][0]], 'words_equal': res[0][1] == res[1][1], 'prefix': prefix})
    return out


def assemble(bits, ubits, B, K, mutant=''):
    import numpy as np
    n = 1 << B; t = time.monotonic()
    counts = {str(k): int(labels(bits[1:k + 1])[1].size) for k in PREFIX_DEPTHS if k <= K}
    lab, cnt = labels(bits[1:K + 1]); ulab, ucnt = labels(ubits[1:])
    sh = {str(int(k)): int(v) for k, v in zip(*np.unique(cnt, return_counts=True))}
    least = int(np.flatnonzero(cnt[lab] == cnt.max()).min())                 # the least lane among all classes of maximum size (GC1821)
    classes = {'counts': counts, 'count_K': int(cnt.size), 'labels': [int(x) for x in lab], 'size_hist': sh, 'largest_size': int(cnt.max()), 'largest_least_lane': least,
               'largest_right': [(least >> j) & 1 for j in range(B)],
               'by_support': {str(b): int(np.unique(lab[:1 << b]).size) for b in range(B + 1)}}
    visible = {'u_classes': int(ucnt.size), 'partition_equal': partition_equal(lab, ulab)}
    classes_s = time.monotonic() - t; t = time.monotonic()
    firsts = flip_firsts(bits, lab, B, K, mutant)
    flips = {p: dict(summarize_flip(f, int(p), B), first=f) for p, f in firsts.items()}
    flips_s = time.monotonic() - t; t = time.monotonic()
    wl = whole_line_checks(bits, lab, B, K)
    wl_s = time.monotonic() - t
    if (B, K) == STAGE_SCOPE:
        lane_sha = hashlib.sha256(''.join(str(int(x)) for x in bits[1:, MAX_LANE]).encode()).hexdigest()
        bindings = {'prefix_counts_equal': counts == PREFIX_L907, 'max_lane_sha256': lane_sha, 'max_lane_equal': lane_sha == MAX_LANE_SHA256}
    else:
        bindings = {'prefix_counts_equal': None, 'max_lane_sha256': None, 'max_lane_equal': None}
    return ({'classes': classes, 'visible': visible, 'flips': flips, 'whole_line': wl, 'bindings': bindings},
            {'classes_s': round(classes_s, 2), 'flips_s': round(flips_s, 2), 'whole_line_s': round(wl_s, 2)})


def controls(mutant=''):
    res = {}
    ok = True
    for B in range(5):
        bits, _ = compute(B, 24, mutant)
        for r in range(1 << B):
            if psi_single([(r >> j) & 1 for j in range(B)], 24) != [int(x) for x in bits[1:, r]]: ok = False
    res['single_lane_psi_equals_lane_bits_B_le_4_K24'] = ok
    ok = True
    for B, K in [(b, 40) for b in range(1, 7)] + [(16, 16)]:              # at B = 16 the classes are still splitting at depth 16 (L907: 36)
        bits, ubits = compute(B, K, mutant)
        if not partition_equal(labels(bits[1:])[0], labels(ubits[1:])[0]): ok = False
    res['u_partition_equals_psi_partition_B_le_6_K40_and_B16_K16'] = ok
    B, K = 5, 40
    bits, _ = compute(B, K)
    lab, _ = labels(bits[1:])
    got = flip_firsts(bits, lab, B, K, mutant)
    single = {r: psi_single([(r >> j) & 1 for j in range(B)], K) for r in range(1 << B)}
    ok = True
    for p in range(1, B + 1):
        want = []
        for r in pair_lanes(p, B):
            a, b = single[r], single[r | (1 << (p - 1))]
            want.append(0 if a == b else next(i for i in range(K) if a[i] != b[i]) + 1)
        if got[str(p)] != want or any(f and (f % 2 or f < p) for f in want) or truth_table_problem(want, p, B): ok = False
    res['flip_stats_equal_pairwise_single_lane_B5_K40'] = ok
    return res


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 COLLISIONS CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, B, K):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic(); deps()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'per_r_sha256': PER_R_SHA256, 'scope': {'B': B, 'K': K}, 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_collisions_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'cq01_collisions_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    t = time.monotonic(); bits, ubits = compute(B, K); lane_s = round(time.monotonic() - t, 2)
    sections, timing = assemble(bits, ubits, B, K)
    R.update(sections); R['timing'] = {'lane_psi_s': lane_s, **timing}
    b = R['bindings']; wl = R['whole_line']
    R['complete'] = (R['visible']['partition_equal'] is True and len(wl) >= 1 and [w['lanes'] for w in wl] == select_pairs(R['classes']['labels'])
                     and all(w['d_expected'] is not None and w['words_equal'] is True and w['f'] == [w['d_expected']] * 2 for w in wl)
                     and stage_pairs_problem(len(wl), B, K) is None
                     and ((b['prefix_counts_equal'] is True and b['max_lane_equal'] is True) if (B, K) == STAGE_SCOPE else b['prefix_counts_equal'] is None))
    if not R['complete']: R['stopped'] = 'incomplete: the partition check, a whole-line pair or a binding failed (no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 16 << 20
PARSE_FAIL = 'parse: nonfinite or invalid JSON'
TOP_KEYS = {'started', 'finished', 'elapsed_s', 'this_sha256', 'per_r_sha256', 'scope', 'controls', 'gate_controls', 'classes', 'visible',
            'flips', 'whole_line', 'bindings', 'timing', 'complete'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}
SECTION_KEYS = {'classes': {'counts', 'count_K', 'labels', 'size_hist', 'largest_size', 'largest_least_lane', 'largest_right', 'by_support'},
                'visible': {'u_classes', 'partition_equal'},
                'bindings': {'prefix_counts_equal', 'max_lane_sha256', 'max_lane_equal'},
                'timing': {'lane_psi_s', 'classes_s', 'flips_s', 'whole_line_s'}}
FLIP_KEYS = {'pairs', 'equal_through_K', 'first_hist', 'min_first', 'median_first', 'groups', 'first'}
WL_KEYS = {'lanes', 'L', 'd_expected', 'f', 'words_equal', 'prefix'}
STAGE_BIND_FAIL = "bindings: the stage scope does not match L907's retained result"
OFF_SCOPE_FAIL = 'bindings: a stage binding outside the stage scope'
STAGE_PAIRS_FAIL = 'bindings: the stage scope needs twelve whole-line pairs'


def stage_pairs_problem(npairs, B, K):
    """At the stage scope the promised twelve pairs must all be present (GC1821); separately callable for literal fixtures."""
    return STAGE_PAIRS_FAIL if (B, K) == STAGE_SCOPE and npairs != WL_PAIRS else None


def truth_table_problem(first, p, B):
    """GC1821's depth-2 truth table: u R 0 = 1 xor (R1 or R2) = Psi R 2, so a cell 1 flip first differs at depth 2 exactly when R2 is white,
    a cell 2 flip exactly when R1 is white, and no other flip differs at depth 2."""
    for r, f in zip(pair_lanes(p, B), first):
        if p == 1: want = ((r >> 1) & 1) == 0 if B >= 2 else True
        elif p == 2: want = (r & 1) == 0
        else: want = False
        if (f == 2) != want: return 'arithmetic: depth-2 truth table (p = %d)' % p
    return None


def stage_binding_problem(b, B, K):
    """The stage-scope bindings, separately callable so the gate controls exercise the stage scope without running the stage."""
    if (B, K) == STAGE_SCOPE:
        if b.get('prefix_counts_equal') is not True or b.get('max_lane_equal') is not True or b.get('max_lane_sha256') != MAX_LANE_SHA256: return STAGE_BIND_FAIL
    elif any(b.get(k) is not None for k in ('prefix_counts_equal', 'max_lane_sha256', 'max_lane_equal')): return OFF_SCOPE_FAIL
    return None


def validate_result(d, src_sha, B, K):
    """One explicit schema, in order: types, exact key sets, domains, cross-field bindings, arithmetic, completion. Every summary is
    recomputed from the retained labels and first-difference lists."""
    isint = lambda x: type(x) is int
    fin = lambda x: (type(x) is int or (type(x) is float and math.isfinite(x)))
    n = 1 << B
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('this_sha256', str), ('per_r_sha256', str), ('started', str), ('finished', str), ('scope', dict), ('controls', dict),
                   ('gate_controls', dict), ('classes', dict), ('visible', dict), ('flips', dict), ('whole_line', list), ('bindings', dict),
                   ('timing', dict), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float): return 'types: elapsed_s'
    c = d['controls']
    if not isinstance(c.get('base'), dict) or not all(isinstance(c.get(m), dict) for m in MUTANTS): return 'types: control reports'
    cl, fl, wl = d['classes'], d['flips'], d['whole_line']
    if not (isinstance(cl.get('counts'), dict) and isinstance(cl.get('size_hist'), dict) and isinstance(cl.get('largest_right'), list)
            and isinstance(cl.get('labels'), list) and isinstance(cl.get('by_support'), dict)): return 'types: classes'
    if not all(isinstance(v, dict) and isinstance(v.get('first_hist'), dict) and isinstance(v.get('groups'), dict) and isinstance(v.get('first'), list)
               for v in fl.values()): return 'types: flips'
    if not all(isinstance(w, dict) and isinstance(w.get('lanes'), list) and isinstance(w.get('f'), list) and isinstance(w.get('prefix'), list) for w in wl): return 'types: whole line'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['scope']) != {'B', 'K'}: return 'keys: scope'
    if set(c) != CONTROL_KEYS: return 'keys: controls'
    if set(c['base']) != set(BASE_KEYS) or not all(set(c[m]) == set(BASE_KEYS) for m in MUTANTS): return 'keys: base or mutant reports'
    if set(d['gate_controls']) != set(GATE_KEYS): return 'keys: gate controls'
    for name, keys in SECTION_KEYS.items():
        if set(d[name]) != keys: return 'keys: %s' % name
    if set(cl['counts']) != {str(k) for k in PREFIX_DEPTHS if k <= K}: return 'keys: class counts'
    if set(cl['by_support']) != {str(b) for b in range(B + 1)}: return 'keys: restricted supports'
    if set(fl) != {str(p) for p in range(1, B + 1)} or not all(set(v) == FLIP_KEYS and set(v['groups']) == set(GROUPS) for v in fl.values()): return 'keys: flips'
    if not all(set(w) == WL_KEYS for w in wl): return 'keys: whole line'
    # 3. domains
    if d['this_sha256'] != src_sha: return 'domains: source digest'
    if d['per_r_sha256'] != PER_R_SHA256: return 'domains: dependency digest'
    if d['scope'] != {'B': B, 'K': K}: return 'domains: scope'
    if not all(type(v) is bool for v in list(c['base'].values()) + [x for m in MUTANTS for x in c[m].values()] + [c[m + '_caught'] for m in MUTANTS] + [c['base_all_pass'], c['ok']]):
        return 'domains: control values not Boolean'
    if not all(v is True for v in d['gate_controls'].values()): return 'domains: a gate control is not true'
    if not all(fin(x) and x >= 0 for x in [d['elapsed_s']] + list(d['timing'].values())): return 'domains: timing'
    if not all(isint(v) and 1 <= v <= n for v in list(cl['counts'].values()) + list(cl['by_support'].values()) + [cl['count_K']]): return 'domains: class counts'
    if not (len(cl['labels']) == n and all(isint(x) and 0 <= x < n for x in cl['labels'])): return 'domains: labels'
    if not all(isinstance(k, str) and k.isdigit() and 1 <= int(k) <= n and isint(v) and v >= 1 for k, v in cl['size_hist'].items()): return 'domains: size histogram'
    if not (isint(cl['largest_size']) and 1 <= cl['largest_size'] <= n and isint(cl['largest_least_lane']) and 0 <= cl['largest_least_lane'] < n
            and len(cl['largest_right']) == B and all(isint(x) and x in (0, 1) for x in cl['largest_right'])): return 'domains: largest class'
    v = d['visible']
    if not (isint(v['u_classes']) and 1 <= v['u_classes'] <= n and type(v['partition_equal']) is bool): return 'domains: visible'
    for p, f in fl.items():
        if not (isint(f['pairs']) and isint(f['equal_through_K']) and 0 <= f['equal_through_K'] <= f['pairs'] <= n
                and len(f['first']) == n // 2 and all(isint(x) and 0 <= x <= K for x in f['first'])
                and all(isinstance(k, str) and k.isdigit() and 1 <= int(k) <= K and isint(x) and x >= 1 for k, x in f['first_hist'].items())
                and all(x is None or isint(x) for x in (f['min_first'], f['median_first']))
                and all(isinstance(g, list) and len(g) == 2 and all(isint(y) and y >= 0 for y in g) for g in f['groups'].values())):
            return 'domains: flips'
    for w in wl:
        dd = w['d_expected']
        if not (len(w['lanes']) == 2 and all(isint(x) and 0 <= x < n for x in w['lanes']) and isint(w['L'])
                and (dd is None or (isint(dd) and w['L'] < dd <= K)) and len(w['f']) == 2 and all(x is None or isint(x) for x in w['f'])
                and type(w['words_equal']) is bool and len(w['prefix']) == (dd or K) and all(isint(x) and x in (0, 1) for x in w['prefix'])):
            return 'domains: whole line'
    b = d['bindings']
    if not (b['prefix_counts_equal'] in (None, True, False) and b['max_lane_equal'] in (None, True, False) and (b['max_lane_sha256'] is None or isinstance(b['max_lane_sha256'], str))):
        return 'domains: bindings'
    # 4. cross-field bindings
    if not all(c['base'][k] is True for k in BASE_KEYS) or c['base_all_pass'] is not True: return 'bindings: base controls'
    for m in MUTANTS:
        if c[m + '_caught'] is not True or all(c[m][k] for k in BASE_KEYS): return 'bindings: mutant %s not caught by its own outcomes' % m
    if c['ok'] is not True: return 'bindings: controls ok flag'
    sp = stage_binding_problem(b, B, K)
    if sp: return sp
    if (B, K) == STAGE_SCOPE and cl['counts'] != PREFIX_L907: return STAGE_BIND_FAIL
    lab = cl['labels']; ncl = len(set(lab))
    if cl['count_K'] != ncl or (str(K) in cl['counts'] and cl['counts'][str(K)] != ncl): return 'bindings: the depth-K class count vs the labels'
    if cl['largest_right'] != [(cl['largest_least_lane'] >> j) & 1 for j in range(B)]: return 'bindings: largest right half vs its lane'
    if v['partition_equal'] is not True or v['u_classes'] != ncl: return 'bindings: the visible-word partition is not the Psi partition'
    spp = stage_pairs_problem(len(wl), B, K)
    if spp: return spp
    for p in range(1, B + 1):
        if any((f == 0) != (lab[r] == lab[r | (1 << (p - 1))]) for r, f in zip(pair_lanes(p, B), fl[str(p)]['first'])):
            return 'bindings: first differences vs labels (p = %d)' % p
    # 5. arithmetic
    ks = sorted(int(k) for k in cl['counts'])
    if any(cl['counts'][str(a)] > cl['counts'][str(c2)] for a, c2 in zip(ks, ks[1:])): return 'arithmetic: class counts decrease'
    sizes = {}
    for x in lab: sizes[x] = sizes.get(x, 0) + 1
    shw = {}
    for s_ in sizes.values(): shw[str(s_)] = shw.get(str(s_), 0) + 1
    if cl['size_hist'] != shw: return 'arithmetic: size histogram vs labels'
    big = max(sizes.values())
    if cl['largest_size'] != big or sizes[lab[cl['largest_least_lane']]] != big or any(sizes[lab[r]] == big for r in range(cl['largest_least_lane'])):
        return 'arithmetic: largest class vs labels'
    if cl['by_support'] != {str(bb): len(set(lab[:1 << bb])) for bb in range(B + 1)}: return 'arithmetic: restricted supports vs labels'
    for p in range(1, B + 1):
        f = fl[str(p)]
        if {k: f[k] for k in ('pairs', 'equal_through_K', 'first_hist', 'min_first', 'median_first', 'groups')} != summarize_flip(f['first'], p, B):
            return 'arithmetic: flip summaries vs first differences (p = %d)' % p
        if any(x and (x % 2 or x < p) for x in f['first']): return 'arithmetic: odd depth or light cone (p = %d)' % p
        tt = truth_table_problem(f['first'], p, B)
        if tt: return tt
    if [w['lanes'] for w in wl] != select_pairs(lab) or len(wl) == 0: return 'arithmetic: whole line selection'
    for w in wl:
        pre, dd = w['prefix'], w['d_expected']
        if w['L'] != WL_L or (dd is not None and (pre[dd - 1] != 1 or any(pre[WL_L:dd - 1]))) or (dd is None and any(pre[WL_L:])):
            return 'arithmetic: whole line prefix vs d'
    for w in wl:
        if w['d_expected'] is None or w['f'] != [w['d_expected']] * 2 or w['words_equal'] is not True: return 'arithmetic: whole line pair'
    # 6. completion
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, B, K):
    M, _ = deps()
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = M.strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate_result(d, src_sha, B, K)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'CQ01 collisions complete, the partition check and every binding held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


def gate_fixtures():
    nan = float('nan')
    good_stage = {'prefix_counts_equal': True, 'max_lane_sha256': MAX_LANE_SHA256, 'max_lane_equal': True}
    def f2(d): return d['flips']['2']
    def first_nonzero(d):
        return next(i for i, x in enumerate(f2(d)['first']) if x)
    def first_zero(d):
        return next(i for i, x in enumerate(f2(d)['first']) if x == 0)
    def zero_a_visible(d):                      # breaks the label binding: a visible pair reported equal
        f2(d)['first'][first_nonzero(d)] = 0
    def odd_depth(d):                           # an odd depth, labels and summaries kept consistent so only arithmetic catches it
        f = f2(d); i = first_nonzero(d); f['first'][i] += 1
        d['flips']['2'] = dict(summarize_flip(f['first'], 2, GATE_B), first=f['first'])
    def stale_summary(d):
        f = f2(d); f['first_hist'] = dict(f['first_hist']); k = sorted(f['first_hist'], key=int)[0]; f['first_hist'][k] += 1
    def relabel(d):                             # merge two classes in the labels only
        lab = d['classes']['labels']; a = lab[0]; b = next(x for x in lab if x != a)
        d['classes']['labels'] = [a if x == b else x for x in lab]
    def wrong_support(d):
        d['classes']['by_support']['2'] += 1 if d['classes']['by_support']['2'] < 4 else -1
    def keep_one(d):
        d['whole_line'][:] = d['whole_line'][:1]
    def same_lane(d):
        w = d['whole_line'][0]; w['lanes'] = [w['lanes'][0], w['lanes'][0]]
    def reversed_pair(d):
        w = d['whole_line'][0]; w['lanes'] = w['lanes'][::-1]
    def unselected(d):
        sel = [w['lanes'] for w in d['whole_line']]
        d['whole_line'][0]['lanes'] = next(x for x in ([0, 7], [1, 7], [2, 7]) if x not in sel)
    def repeated_class(d):
        d['whole_line'][1] = dict(d['whole_line'][0], lanes=d['whole_line'][0]['lanes'][::-1])
    def bad_prefix(d):
        w = d['whole_line'][0]; w['prefix'][w['d_expected'] - 1] = 0
    def failed_attempt(d):
        d['whole_line'][0]['f'][1] = None
    def truth_table(d):
        f = d['flips']['1']; i = next(j for j, x in enumerate(f['first']) if x == 2); f['first'][i] = 4
        d['flips']['1'] = dict(summarize_flip(f['first'], 1, GATE_B), first=f['first'])
    def largest_tie(d):
        cl = d['classes']; lab = cl['labels']; l0 = cl['largest_least_lane']
        later = next(r for r in range(l0 + 1, len(lab)) if lab[r] == lab[l0])
        cl['largest_least_lane'] = later; cl['largest_right'] = [(later >> j) & 1 for j in range(GATE_B)]
    return [
        ('good_full_packet_passes', 'file', lambda d: None, None),
        ('good_stage_binding_passes', 'stage', dict(good_stage), None),
        ('types_classes_null', 'file', lambda d: d.__setitem__('classes', None), 'types: classes'),
        ('types_labels_dict', 'file', lambda d: d['classes'].__setitem__('labels', {}), 'types: classes'),
        ('types_whole_line_dict', 'file', lambda d: d.__setitem__('whole_line', {}), 'types: whole_line'),
        ('types_started_dict', 'file', lambda d: d.__setitem__('started', {}), 'types: started'),
        ('types_elapsed_string', 'file', lambda d: d.__setitem__('elapsed_s', '1'), 'types: elapsed_s'),
        ('types_flip_first_dict', 'file', lambda d: f2(d).__setitem__('first', {}), 'types: flips'),
        ('keys_extra_top_key', 'file', lambda d: d.__setitem__('extra', 1), "keys: top level ['extra']"),
        ('keys_stopped_present', 'file', lambda d: d.__setitem__('stopped', 'x'), "keys: top level ['stopped']"),
        ('keys_flip_missing_cell', 'file', lambda d: d['flips'].pop('3'), 'keys: flips'),
        ('keys_class_depth_missing', 'file', lambda d: d['classes']['counts'].pop('8'), 'keys: class counts'),
        ('keys_support_missing', 'file', lambda d: d['classes']['by_support'].pop('0'), 'keys: restricted supports'),
        ('keys_whole_line_extra', 'file', lambda d: d['whole_line'][0].__setitem__('x', 1), 'keys: whole line'),
        ('domains_wrong_digest', 'file', lambda d: d.__setitem__('this_sha256', '0' * 64), 'domains: source digest'),
        ('domains_wrong_dependency', 'file', lambda d: d.__setitem__('per_r_sha256', '0' * 64), 'domains: dependency digest'),
        ('domains_wrong_scope', 'file', lambda d: d['scope'].__setitem__('K', 418), 'domains: scope'),
        ('domains_negative_timing', 'file', lambda d: d['timing'].__setitem__('flips_s', -1.0), 'domains: timing'),
        ('domains_nan_elapsed', 'memory', lambda d: d.__setitem__('elapsed_s', nan), 'domains: timing'),
        ('domains_inf_timing', 'memory', lambda d: d['timing'].__setitem__('classes_s', float('inf')), 'domains: timing'),
        ('domains_class_count_zero', 'file', lambda d: d['classes']['counts'].__setitem__('8', 0), 'domains: class counts'),
        ('domains_label_out_of_range', 'file', lambda d: d['classes']['labels'].__setitem__(0, 8), 'domains: labels'),
        ('domains_largest_right_nonbinary', 'file', lambda d: d['classes']['largest_right'].__setitem__(0, 2), 'domains: largest class'),
        ('domains_first_beyond_K', 'file', lambda d: f2(d)['first'].__setitem__(0, 421), 'domains: flips'),
        ('domains_first_list_short', 'file', lambda d: f2(d)['first'].pop(), 'domains: flips'),
        ('domains_whole_line_lane_range', 'file', lambda d: d['whole_line'][0]['lanes'].__setitem__(0, 8), 'domains: whole line'),
        ('parse_nan_token', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": NaN, "x_": ', 1), PARSE_FAIL),
        ('parse_exponent_overflow', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": 1e999, "x_": ', 1), PARSE_FAIL),
        ('bindings_explicit_false_base', 'file', lambda d: d['controls']['base'].__setitem__(BASE_KEYS[0], False), 'bindings: base controls'),
        ('bindings_mutant_all_true', 'file', lambda d: [d['controls'].__setitem__(m, {k: True for k in BASE_KEYS}) for m in MUTANTS],
         'bindings: mutant %s not caught by its own outcomes' % MUTANTS[0]),
        ('bindings_stage_values_off_scope', 'file', lambda d: d['bindings'].update(good_stage), OFF_SCOPE_FAIL),
        ('bindings_stage_prefix_false', 'stage', dict(good_stage, prefix_counts_equal=False), STAGE_BIND_FAIL),
        ('bindings_stage_lane_sha_wrong', 'stage', dict(good_stage, max_lane_sha256='0' * 64), STAGE_BIND_FAIL),
        ('bindings_stage_missing', 'stage', {'prefix_counts_equal': None, 'max_lane_sha256': None, 'max_lane_equal': None}, STAGE_BIND_FAIL),
        ('bindings_count_not_labels', 'file', lambda d: d['classes'].__setitem__('count_K', d['classes']['count_K'] + 1 if d['classes']['count_K'] < 8 else 1),
         'bindings: the depth-K class count vs the labels'),
        ('bindings_largest_right_not_lane', 'file', lambda d: d['classes'].__setitem__('largest_right', [1 - x for x in d['classes']['largest_right']]),
         'bindings: largest right half vs its lane'),
        ('bindings_partition_false', 'file', lambda d: d['visible'].__setitem__('partition_equal', False), 'bindings: the visible-word partition is not the Psi partition'),
        ('bindings_first_vs_labels', 'file', zero_a_visible, 'bindings: first differences vs labels (p = 2)'),
        ('arithmetic_class_counts_decrease', 'file', lambda d: d['classes']['counts'].__setitem__('16', 1), 'arithmetic: class counts decrease'),
        ('arithmetic_size_histogram', 'file', lambda d: d['classes'].__setitem__('size_hist', {'8': 1}), 'arithmetic: size histogram vs labels'),
        ('arithmetic_largest_size', 'file', lambda d: d['classes'].__setitem__('largest_size', d['classes']['largest_size'] + 1), 'arithmetic: largest class vs labels'),
        ('arithmetic_restricted_support', 'file', wrong_support, 'arithmetic: restricted supports vs labels'),
        ('arithmetic_stale_flip_summary', 'file', stale_summary, 'arithmetic: flip summaries vs first differences (p = 2)'),
        ('arithmetic_odd_depth', 'file', odd_depth, 'arithmetic: odd depth or light cone (p = 2)'),
        ('arithmetic_whole_line_f', 'file', lambda d: d['whole_line'][0].__setitem__('f', [d['whole_line'][0]['d_expected'], d['whole_line'][0]['d_expected'] + 1]),
         'arithmetic: whole line pair'),
        ('arithmetic_whole_line_one_row', 'file', keep_one, 'arithmetic: whole line selection'),
        ('arithmetic_whole_line_same_lane', 'file', same_lane, 'arithmetic: whole line selection'),
        ('arithmetic_whole_line_reversed', 'file', reversed_pair, 'arithmetic: whole line selection'),
        ('arithmetic_whole_line_unselected', 'file', unselected, 'arithmetic: whole line selection'),
        ('arithmetic_whole_line_repeated_class', 'file', repeated_class, 'arithmetic: whole line selection'),
        ('arithmetic_whole_line_prefix', 'file', bad_prefix, 'arithmetic: whole line prefix vs d'),
        ('arithmetic_whole_line_failed_attempt', 'file', failed_attempt, 'arithmetic: whole line pair'),
        ('arithmetic_depth2_truth_table', 'file', truth_table, 'arithmetic: depth-2 truth table (p = 1)'),
        ('arithmetic_largest_tie', 'file', largest_tie, 'arithmetic: largest class vs labels'),
        ('good_stage_twelve_pairs_passes', 'stagepairs', 12, None),
        ('bindings_stage_fewer_than_twelve', 'stagepairs', 11, STAGE_PAIRS_FAIL),
        ('completion_flag_false', 'file', lambda d: d.__setitem__('complete', False), 'completion: complete flag'),
    ]


GATE_KEYS = ('good_full_packet_passes', 'good_stage_binding_passes', 'types_classes_null', 'types_labels_dict', 'types_whole_line_dict',
             'types_started_dict', 'types_elapsed_string', 'types_flip_first_dict', 'keys_extra_top_key', 'keys_stopped_present',
             'keys_flip_missing_cell', 'keys_class_depth_missing', 'keys_support_missing', 'keys_whole_line_extra', 'domains_wrong_digest',
             'domains_wrong_dependency', 'domains_wrong_scope', 'domains_negative_timing', 'domains_nan_elapsed', 'domains_inf_timing',
             'domains_class_count_zero', 'domains_label_out_of_range', 'domains_largest_right_nonbinary', 'domains_first_beyond_K',
             'domains_first_list_short', 'domains_whole_line_lane_range', 'parse_nan_token', 'parse_exponent_overflow',
             'bindings_explicit_false_base', 'bindings_mutant_all_true', 'bindings_stage_values_off_scope', 'bindings_stage_prefix_false',
             'bindings_stage_lane_sha_wrong', 'bindings_stage_missing', 'bindings_count_not_labels', 'bindings_largest_right_not_lane',
             'bindings_partition_false', 'bindings_first_vs_labels', 'arithmetic_class_counts_decrease', 'arithmetic_size_histogram',
             'arithmetic_largest_size', 'arithmetic_restricted_support', 'arithmetic_stale_flip_summary', 'arithmetic_odd_depth',
             'arithmetic_whole_line_f', 'arithmetic_whole_line_one_row', 'arithmetic_whole_line_same_lane', 'arithmetic_whole_line_reversed',
             'arithmetic_whole_line_unselected', 'arithmetic_whole_line_repeated_class', 'arithmetic_whole_line_prefix',
             'arithmetic_whole_line_failed_attempt', 'arithmetic_depth2_truth_table', 'arithmetic_largest_tie', 'good_stage_twelve_pairs_passes',
             'bindings_stage_fewer_than_twelve', 'completion_flag_false')


def gate_controls():
    """A valid full synthetic packet from a real tiny computation (B = 3, K = 420), assembled by the run's own code; every fixture must
    produce EXACTLY its stated diagnostic, the positive ones a pass."""
    import copy, tempfile
    bits, ubits = compute(GATE_B, GATE_K)
    sections, timing = assemble(bits, ubits, GATE_B, GATE_K)
    sections = json.loads(json.dumps(sections, allow_nan=False))
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'finished': 'f', 'elapsed_s': 0.1, 'this_sha256': 'S', 'per_r_sha256': PER_R_SHA256, 'scope': {'B': GATE_B, 'K': GATE_K},
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'timing': {'lane_psi_s': 0.0, **timing}, 'complete': True, **sections}
    res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', GATE_B, GATE_K)
        for name, kind, f, want in gate_fixtures():
            if kind == 'stage':
                res[name] = stage_binding_problem(f, *STAGE_SCOPE) == want; continue
            if kind == 'stagepairs':
                res[name] = stage_pairs_problem(f, *STAGE_SCOPE) == want; continue
            bad = copy.deepcopy(good)
            if kind == 'memory':
                f(bad); res[name] = validate_result(bad, 'S', GATE_B, GATE_K) == want; continue
            if kind == 'text':
                open(rp, 'w').write(f(json.dumps(bad, allow_nan=False)))
            else:
                f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            verdict, note = m(0, '')
            res[name] = (verdict == 'pass') if want is None else (verdict == 'FAIL' and note == (want if kind == 'text' else 'rc 0: ' + want))
    assert set(res) == set(GATE_KEYS) and len(res) == len(GATE_KEYS)
    return res


def stage(out, B, K):
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if (B, K) != STAGE_SCOPE:
        print('REFUSED: the only admitted stage scope is B = 16, K = 800'); return 3
    deps()
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01_collisions'] = {'this_sha256': src_sha, 'per_r_sha256': PER_R_SHA256, 'w1a_sha256': W1A_SHA256, 'scope': {'B': B, 'K': K},
                             'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_collisions_result.json'), src_sha, B, K)
    rec = sup.run_step('cq01_collisions', [sys.executable, os.path.abspath(__file__), 'run', rdir, str(B), str(K)], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 4 and a[0] == 'run':
        B, K = int(a[2]), int(a[3])
        if not (3 <= B <= 16 and WL_L + 2 <= K <= 800 and K % 2 == 0): print('REFUSED: run admits 3 <= B <= 16, 402 <= K <= 800, K even'); sys.exit(3)
        R = run(a[1], B, K); print('CQ01 COLLISIONS RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 4 and a[0] == 'stage':
        sys.exit(stage(a[1], int(a[2]), int(a[3])))
    print(__doc__); sys.exit(2)
