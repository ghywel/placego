#!/usr/bin/env python3
"""CQ01 kernel test, revision 2 (Local, 2026-10-24, L912; GPT's GC1823: the gate requires every move pair equal at every depth, with
GPT's self-consistent split packet as a negative fixture; persistence through depth 3,200 is worded as unresolved candidate pairs, not
a larger infinite kernel; the depth-800 partition is bound to L910's retained labels by a canonical-label digest; memory accounting
from GPT). Revision 1 (L911; L910's next job). NOT an agreed job until GPT accepts this exact file; nothing
runs on import; `--controls` runs the small CPU controls only.

If this holds, it changes the CQ01 row: L910's move lemma (PROOFS.md waiting room) says Psi R is unchanged by two right-end moves,
'...0 1' ~ '...0 1 1' and '...1 1' ~ '...1 0 1' (the wall black at time 0). The moves generate the depth-800 partition exactly for the
right halves supported in 1..B' with B' <= 8, but the depth-800 partition is coarser for B' >= 9 (256 classes against 257 move classes;
31,478 against 32,769 at B' = 16). Finite depth can only merge (a pair equal through depth K may differ deeper: GC1818, GC1820). This
job asks whether those extra merges split at depths 1,600 and 3,200. If they do, the kernel conjecture (the moves generate the whole
kernel of R -> u R) gains support on this domain; if they persist, they are UNRESOLVED through depth 3,200, candidate pairs for
explanation: only a proof of permanent equality outside the move relation refutes the kernel conjecture, and splitting every extra merge
would settle this finite-support domain at that depth, not the conjecture for all B (GC1823). The move lemma is HAND/PROVED (GC1823), and
GPT's hand observation there, that move components are paths, gives 2^(B - 1) + 1 move classes for every B, each of at most B lanes.

Measured (B = 16, all 65,536 right halves R supported in 1..16, lane r is R p = bit p - 1 of r; one lane pass at K = 3,200, so the
partitions at K = 800, 1,600 and 3,200 are prefix partitions of the same bits and nested by construction):
  - the move partition: union-find over the two moves, applied wherever the moved cell stays inside 1..16 (move_labels); its class count
    and its restricted counts among the R supported in 1..B' for B' = 0..16;
  - at each K: the per-lane class labels (retained), the class count, the restricted counts, whether every move pair has equal labels
    (the lemma's consequence, numerically), and the number of extra merges (move classes minus observed classes);
  - at K = 3,200: every observed class that contains more than one move class, as the sorted list of the least lanes of its move
    classes (retained, capped at 4,096 groups with the total count kept).
Bindings at the stage scope to L910's retained result (cited/cq01-collisions-20261024-2157/, result d74395a5...): the K = 800 class count
31,478, the restricted counts BY_SUPPORT_L910, and the sha256 of its canonical labels (each lane labelled by the least lane of its class,
written as comma-separated decimals), LABELS_SHA256_L910, so the whole partition is bound, not only its counts (all read from that
result by script).

Controls (`--controls`, CPU only, small; all must pass before a stage):
  - move_labels reproduces L910's small classes literally: for B' = 3, {100, 010, 011} and {110, 101} (cell 1 first), the rest singletons;
    and for B' <= 10 the move class count is 2^(B' - 1) + 1, as L910's union-find found;
  - the lemma's consequence on real data: every move pair has equal Psi at every depth up to 400 for every R supported in 1..8;
  - the nested labels: labels_at(bits, K) equals a direct prefix partition for B = 16 at K = 16 and 32 (still splitting there), and the
    K = 32 partition refines the K = 16 one;
  - three mutants, each of which must fail a control: 'movea' (move (a)'s partner is R + {m + 2}, which is itself move-equivalent, two
    moves away, so only the literal small classes catch it), 'm2b' (move (b)'s partner is R + {m + 2}, not move-equivalent: the Psi check
    catches it), 'kcut' (labels at depth K are computed from depth K/2).
The result gate (GC1813, GC1818, GC1821): strict reading, one explicit schema in the order types, exact key sets, domains, cross-field
bindings, arithmetic, completion, fail-closed, on bounded bytes; every count, refinement and merged group is recomputed from the retained
labels and from move_labels, the same helper the producer uses; the merged groups are required exactly, in order; nesting (labels at a
larger K refine those at a smaller K) is checked pair-free by label-pair counting; every depth's moves_refine must be true, so a
self-consistent packet that reports a move pair splitting fails the gate (GC1823's fixture is kept). The valid synthetic packet is assembled by the run's
own code from a real tiny computation (B = 6, K = 400, at depths 100, 200, 400); every negative fixture states its exact diagnostic.

Proposed stage: B = 16, depths (800, 1,600, 3,200) (the only admitted stage scope); W1A caps: stage, step wall and CPU 600 s, group RSS
4 GiB, artifacts 50 MiB, log 10 MiB. Cost ESTIMATE: the lane pass alone is quadratic in K: 0.85 s at K = 800 (L910), so about 14 s at
3,200 (controls, assembly, JSON and supervision are extra). Memory (GC1823's accounting): the bit matrix is 209,780,736 bytes; labels_at
at depth 3,200 materializes a 209,715,200-byte transpose and a 26,214,400-byte packed array, with unique/sort copies and indices on top;
the lane words overlap the matrix until deleted. Under 1 GB is an estimate, not a measured peak; the 4 GiB stop is the bound. `run` also admits 6 <= B <= 16 with depths K1 < K2 < K3 <= 3,200,
even, for disclosed tiny development runs.
Predictions (written before any run of this file, after L910's tables):
  - every move pair has equal labels at every K (the lemma);
  - the extra merges strictly decrease from K = 800 to 1,600 and from 1,600 to 3,200;
  - at K = 3,200 the restricted counts equal 2^(B' - 1) + 1 for every B' <= 12;
  - at K = 3,200 the full count is at least 32,500 (of the move partition's 32,769).
Counterfactual: restricted counts for B' = 9..12 unchanged from K = 800 to 3,200 says the extra merges persist through these depths:
unresolved candidate pairs, named by the retained groups, not a refutation; a move pair with unequal labels contradicts the proved lemma
and means a bug. Results between are inconclusive. No finite depth proves or refutes the kernel conjecture.
Usage: python3 cq01_kernel.py --controls | run OUT B K1 K2 K3 | stage OUT B K1 K2 K3
OUTCOME (the one GC1824-accepted stage at revision 2, a541847f, 2026-10-24 22:24:12 to 22:24:26 BST, L913): W1A pass, the strict gate
PASS, all three bindings held (L910's count, restricted counts and canonical-label digest); child wall 12.48 s, sampled group RSS
906,674,176 bytes. Every move pair equal at every depth: HELD. Extra merges 1,291, 949, 908 at depths 800, 1,600, 3,200: strictly
decreasing, HELD, but plateauing. Restricted counts at 3,200 short of 2^(b - 1) + 1 by 1, 2, 12, 33 at b = 9..12 (b = 9 and 10 unchanged
since depth 800): PREDICTION FAILED. Count at 3,200 is 31,861, not >= 32,500: PREDICTION FAILED. 82 merged groups persist through 1,600
visible bits: unresolved candidate pairs (e.g. 11111 and 111101111). Local's afterwards check: none of their least pairs becomes
move-related within 600 steps (the checker certifies all 511 true move pairs at B = 10 at t = 1).
"""
import hashlib, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
COLL_SHA256 = 'dd943133c1eb806706b0d01ac3c0545e71047f50d6b416b560ffb3be159fde16'
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
STAGE_SCOPE = (16, 800, 1600, 3200)
STAGE_S = 600
GROUP_CAP = 4096
COUNT_L910 = 31478
BY_SUPPORT_L910 = [1, 2, 3, 5, 9, 17, 33, 65, 129, 256, 511, 1010, 2005, 3984, 7921, 15781, 31478]
LABELS_SHA256_L910 = '35b013a093fb5f4c065a23c904bbd0291714f61f08d37d374b82c71733bb79ed'
MUTANTS = ('movea', 'm2b', 'kcut')
BASE_KEYS = ('move_labels_reproduce_L910_small_classes', 'move_pairs_equal_psi_B8_K400', 'nested_labels_B16_K16_K32')
PARSE_FAIL = 'parse: nonfinite or invalid JSON'


def deps():
    import cq01_collisions as X
    if hashlib.sha256(open(X.__file__, 'rb').read()).hexdigest() != COLL_SHA256:
        raise SystemExit('REFUSED: cq01_collisions.py is not the pinned bytes')
    M, C = X.deps()
    return X, M, C


def move_partner(r, B, mutant=''):
    """The move partner of right half r (lane), or None if the moved cell leaves 1..B: move (a) when cell m - 1 is white, move (b) when it
    is black or m = 1 (the wall black at time 0)."""
    if r == 0: return None
    m = r.bit_length()
    if m >= B: return None
    left = 1 if m == 1 else (r >> (m - 2)) & 1
    if left == 0: q = r | (1 << (m + 1 if mutant == 'movea' else m))
    else: q = (r | (1 << (m + 1))) if mutant == 'm2b' else ((r & ~(1 << (m - 1))) | (1 << m))
    return q if q < (1 << B) else None


def move_labels(B, mutant=''):
    """Union-find labels of the move partition on the lanes 0..2^B - 1, canonical: each lane labelled by the least lane of its class."""
    n = 1 << B; parent = list(range(n))
    def f(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for r in range(1, n):
        q = move_partner(r, B, mutant)
        if q is not None:
            a, b = f(r), f(q)
            if a != b: parent[max(a, b)] = min(a, b)
    return [f(x) for x in range(n)]


def labels_at(bits, K, mutant=''):
    """Canonical class labels of the lanes by Psi 1..K (each lane labelled by the least lane with the same prefix)."""
    import numpy as np
    k = K // 2 if mutant == 'kcut' else K
    packed = np.packbits(np.ascontiguousarray(bits[1:k + 1].T), axis=1)
    _, first, inv = np.unique(packed, axis=0, return_index=True, return_inverse=True)
    return [int(x) for x in first[inv.reshape(-1)]]


def labels_digest(lab):
    return hashlib.sha256(','.join(map(str, lab)).encode()).hexdigest()


def by_support(lab, B):
    return [len(set(lab[:1 << b])) for b in range(B + 1)]


def refines(fine, coarse):
    """True if equal labels in fine imply equal labels in coarse (pair-free: each fine class meets one coarse class)."""
    seen = {}
    for a, b in zip(fine, coarse):
        if seen.setdefault(a, b) != b: return False
    return True


def merged_groups(mv, lab):
    """Observed classes containing more than one move class: sorted lists of the move classes' least lanes, sorted by first element."""
    g = {}
    for r, (a, b) in enumerate(zip(mv, lab)):
        g.setdefault(b, set()).add(a)
    return sorted(sorted(v) for v in g.values() if len(v) > 1)


def assemble(bits, B, depths, mutant=''):
    t = time.monotonic()
    mv = move_labels(B, mutant)
    moves = {'count': len(set(mv)), 'by_support': by_support(mv, B)}
    per_k = {}
    for K in depths:
        lab = labels_at(bits, K, mutant)
        per_k[str(K)] = {'labels': lab, 'count': len(set(lab)), 'by_support': by_support(lab, B), 'moves_refine': refines(mv, lab),
                         'extra_merges': moves['count'] - len(set(lab))}
    groups = merged_groups(mv, per_k[str(depths[-1])]['labels'])
    merged = {'total': len(groups), 'groups': groups[:GROUP_CAP]}
    if (B,) + tuple(depths) == STAGE_SCOPE:
        k0 = per_k[str(depths[0])]
        bindings = {'count_equal': k0['count'] == COUNT_L910, 'by_support_equal': k0['by_support'] == BY_SUPPORT_L910,
                    'labels_equal': labels_digest(k0['labels']) == LABELS_SHA256_L910}
    else:
        bindings = {'count_equal': None, 'by_support_equal': None, 'labels_equal': None}
    return {'moves': moves, 'per_k': per_k, 'merged': merged, 'bindings': bindings}, {'assemble_s': round(time.monotonic() - t, 2)}


def controls(mutant=''):
    X, M, C = deps(); res = {}
    lab3 = move_labels(3, mutant)
    def cls(lab, B):
        g = {}
        for r, a in enumerate(lab): g.setdefault(a, []).append(''.join(str((r >> j) & 1) for j in range(B)))
        return sorted(sorted(v) for v in g.values() if len(v) > 1)
    res['move_labels_reproduce_L910_small_classes'] = (cls(lab3, 3) == [['010', '011', '100'], ['101', '110']]
                                                      and all(len(set(move_labels(b, mutant))) == (1 << (b - 1)) + 1 for b in range(1, 11)))
    bits, _ = X.compute(8, 400)
    ok = True
    for r in range(1, 1 << 8):
        q = move_partner(r, 8, mutant)
        if q is not None and (bits[1:, r] != bits[1:, q]).any(): ok = False
    res['move_pairs_equal_psi_B8_K400'] = ok
    bits16, _ = X.compute(16, 32)                 # at B = 16 the classes still split between depths 16 and 32 (L907: 36 at 16)
    ok = True
    for K in (16, 32):
        got = labels_at(bits16, K, mutant)
        direct = {}
        want = [direct.setdefault(bits16[1:K + 1, r].tobytes(), r) for r in range(1 << 16)]
        if got != want: ok = False
    ok = ok and refines(labels_at(bits16, 32, mutant), labels_at(bits16, 16, mutant))
    res['nested_labels_B16_K16_K32'] = ok
    return res


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('CQ01 KERNEL CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def run(out, B, depths):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic(); X, M, C = deps()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'coll_sha256': COLL_SHA256, 'scope': {'B': B, 'depths': list(depths)}, 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'cq01_kernel_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'cq01_kernel_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    t = time.monotonic(); psi, _, _ = C.lane_psi(B, depths[-1]); bits = M.lane_bits(psi, B, depths[-1]); del psi
    lane_s = round(time.monotonic() - t, 2)
    sections, timing = assemble(bits, B, depths)
    R.update(sections); R['timing'] = {'lane_psi_s': lane_s, **timing}
    b = R['bindings']
    R['complete'] = (all(v['moves_refine'] is True for v in R['per_k'].values())
                     and (all(v is True for v in b.values()) if (B,) + tuple(depths) == STAGE_SCOPE else all(v is None for v in b.values())))
    if not R['complete']: R['stopped'] = 'incomplete: a move pair differs, or a binding failed (no retry)'
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S'); save()
    return R


MAX_RESULT_BYTES = 16 << 20
TOP_KEYS = {'started', 'finished', 'elapsed_s', 'this_sha256', 'coll_sha256', 'scope', 'controls', 'gate_controls', 'moves', 'per_k', 'merged',
            'bindings', 'timing', 'complete'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}
K_KEYS = {'labels', 'count', 'by_support', 'moves_refine', 'extra_merges'}
STAGE_BIND_FAIL = "bindings: the K = 800 partition does not match L910's retained result"
OFF_SCOPE_FAIL = 'bindings: a stage binding outside the stage scope'


BIND_KEYS = ('count_equal', 'by_support_equal', 'labels_equal')
MOVE_SPLIT_FAIL = 'bindings: a move pair differs (K = %s)'


def stage_binding_problem(b, scope):
    if tuple(scope) == STAGE_SCOPE:
        if any(b.get(k) is not True for k in BIND_KEYS): return STAGE_BIND_FAIL
    elif any(b.get(k) is not None for k in BIND_KEYS): return OFF_SCOPE_FAIL
    return None


def validate_result(d, src_sha, B, depths):
    isint = lambda x: type(x) is int
    fin = lambda x: (type(x) is int or (type(x) is float and math.isfinite(x)))
    n = 1 << B; ks = [str(k) for k in depths]
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('this_sha256', str), ('coll_sha256', str), ('started', str), ('finished', str), ('scope', dict), ('controls', dict),
                   ('gate_controls', dict), ('moves', dict), ('per_k', dict), ('merged', dict), ('bindings', dict), ('timing', dict), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float): return 'types: elapsed_s'
    c = d['controls']
    if not isinstance(c.get('base'), dict) or not all(isinstance(c.get(m), dict) for m in MUTANTS): return 'types: control reports'
    if not (isinstance(d['moves'].get('by_support'), list) and isinstance(d['merged'].get('groups'), list)): return 'types: moves or merged'
    if not all(isinstance(v, dict) and isinstance(v.get('labels'), list) and isinstance(v.get('by_support'), list) for v in d['per_k'].values()): return 'types: per depth'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['scope']) != {'B', 'depths'}: return 'keys: scope'
    if set(c) != CONTROL_KEYS: return 'keys: controls'
    if set(c['base']) != set(BASE_KEYS) or not all(set(c[m]) == set(BASE_KEYS) for m in MUTANTS): return 'keys: base or mutant reports'
    if set(d['gate_controls']) != set(GATE_KEYS): return 'keys: gate controls'
    if set(d['moves']) != {'count', 'by_support'} or set(d['merged']) != {'total', 'groups'} or set(d['bindings']) != set(BIND_KEYS):
        return 'keys: sections'
    if set(d['timing']) != {'lane_psi_s', 'assemble_s'}: return 'keys: timing'
    if set(d['per_k']) != set(ks) or not all(set(v) == K_KEYS for v in d['per_k'].values()): return 'keys: per depth'
    # 3. domains
    if d['this_sha256'] != src_sha: return 'domains: source digest'
    if d['coll_sha256'] != COLL_SHA256: return 'domains: dependency digest'
    if d['scope'] != {'B': B, 'depths': list(depths)}: return 'domains: scope'
    if not all(type(v) is bool for v in list(c['base'].values()) + [x for m in MUTANTS for x in c[m].values()] + [c[m + '_caught'] for m in MUTANTS] + [c['base_all_pass'], c['ok']]):
        return 'domains: control values not Boolean'
    if not all(v is True for v in d['gate_controls'].values()): return 'domains: a gate control is not true'
    if not all(fin(x) and x >= 0 for x in [d['elapsed_s']] + list(d['timing'].values())): return 'domains: timing'
    for v in d['per_k'].values():
        if not (len(v['labels']) == n and all(isint(x) and 0 <= x < n for x in v['labels']) and isint(v['count']) and 1 <= v['count'] <= n
                and len(v['by_support']) == B + 1 and all(isint(x) for x in v['by_support']) and type(v['moves_refine']) is bool and isint(v['extra_merges'])):
            return 'domains: per depth'
    mo, me = d['moves'], d['merged']
    if not (isint(mo['count']) and len(mo['by_support']) == B + 1 and isint(me['total']) and me['total'] >= 0 and len(me['groups']) <= GROUP_CAP
            and all(isinstance(g, list) and len(g) >= 2 and all(isint(x) and 0 <= x < n for x in g) for g in me['groups'])):
        return 'domains: moves or merged'
    b = d['bindings']
    if not all(v in (None, True, False) for v in b.values()): return 'domains: bindings'
    # 4. cross-field bindings
    if not all(c['base'][k] is True for k in BASE_KEYS) or c['base_all_pass'] is not True: return 'bindings: base controls'
    for m in MUTANTS:
        if c[m + '_caught'] is not True or all(c[m][k] for k in BASE_KEYS): return 'bindings: mutant %s not caught by its own outcomes' % m
    if c['ok'] is not True: return 'bindings: controls ok flag'
    sp = stage_binding_problem(b, (B,) + tuple(depths))
    if sp: return sp
    k0 = d['per_k'][ks[0]]
    if (B,) + tuple(depths) == STAGE_SCOPE and (k0['count'] != COUNT_L910 or k0['by_support'] != BY_SUPPORT_L910
                                               or labels_digest(k0['labels']) != LABELS_SHA256_L910): return STAGE_BIND_FAIL
    mv = move_labels(B)
    if mo['count'] != len(set(mv)) or mo['by_support'] != by_support(mv, B): return 'bindings: move partition'
    for k in ks:                       # the proved lemma: every move pair equal at every depth (GC1823)
        if d['per_k'][k]['moves_refine'] is not True: return MOVE_SPLIT_FAIL % k
    # 5. arithmetic
    for k in ks:
        v = d['per_k'][k]; lab = v['labels']
        if any(lab[x] > x or lab[lab[x]] != lab[x] for x in range(n)): return 'arithmetic: labels not canonical (K = %s)' % k
        if v['count'] != len(set(lab)) or v['by_support'] != by_support(lab, B): return 'arithmetic: counts vs labels (K = %s)' % k
        if v['moves_refine'] != refines(mv, lab) or v['extra_merges'] != mo['count'] - v['count']: return 'arithmetic: refinement or merges (K = %s)' % k
    for a, b2 in zip(ks, ks[1:]):
        if not refines(d['per_k'][b2]['labels'], d['per_k'][a]['labels']): return 'arithmetic: nesting (%s within %s)' % (b2, a)
    groups = merged_groups(mv, d['per_k'][ks[-1]]['labels'])
    if me['total'] != len(groups) or me['groups'] != groups[:GROUP_CAP]: return 'arithmetic: merged groups'
    # 6. completion
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, B, depths):
    X, M, C = deps()
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = M.strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate_result(d, src_sha, B, depths)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'CQ01 kernel complete, every move pair equal and every binding held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


GATE_B, GATE_DEPTHS = 6, (100, 200, 400)


def gate_fixtures():
    nan = float('nan'); k1, k2, k3 = (str(k) for k in GATE_DEPTHS)
    good_stage = {'count_equal': True, 'by_support_equal': True, 'labels_equal': True}
    def move_split(d):                # GC1823: split lane 2 from its move partner lane 1 at the two deeper depths, every field recomputed
        mv = move_labels(GATE_B)
        for k in (k2, k3):
            lab = list(d['per_k'][k]['labels']); assert lab[2] == lab[1] == 1; lab[2] = 2
            d['per_k'][k].update(labels=lab, count=len(set(lab)), by_support=by_support(lab, GATE_B), moves_refine=refines(mv, lab),
                                 extra_merges=d['moves']['count'] - len(set(lab)))
        g = merged_groups(mv, d['per_k'][k3]['labels']); d['merged'].update(total=len(g), groups=g[:GROUP_CAP])
    def merge_two(d):                 # merge two classes at the deepest K, so nesting against the shallower K stays possible to break
        lab = d['per_k'][k3]['labels']; a = lab[1]; b = next(x for x in sorted(set(lab)) if x != a and x != lab[0])
        lo = min(a, b); d['per_k'][k3]['labels'] = [lo if x in (a, b) else x for x in lab]
    def split_deep(d):                # merge two K2 classes that are distinct at K1, keeping K2's own fields consistent: only nesting fails
        lab, lab1 = d['per_k'][k2]['labels'], d['per_k'][k1]['labels']
        roots = [r for r in range(64) if lab[r] == r]
        i, j = next((a, b) for a in roots for b in roots if a < b and lab1[a] != lab1[b])
        new = [i if x == j else x for x in lab]; v = d['per_k'][k2]; mv = move_labels(GATE_B)
        v.update(labels=new, count=len(set(new)), by_support=by_support(new, GATE_B), moves_refine=refines(mv, new),
                 extra_merges=d['moves']['count'] - len(set(new)))
    def dishonest_flag(d):            # a move pair split at the deepest depth while its flag still claims refinement
        mv = move_labels(GATE_B); lab = list(d['per_k'][k3]['labels']); lab[2] = 2
        d['per_k'][k3].update(labels=lab, count=len(set(lab)), by_support=by_support(lab, GATE_B), moves_refine=True,
                              extra_merges=d['moves']['count'] - len(set(lab)))
        g = merged_groups(mv, lab); d['merged'].update(total=len(g), groups=g[:GROUP_CAP])
    def stale_count(d):
        d['per_k'][k1]['count'] += 1; d['per_k'][k1]['extra_merges'] -= 1
    def noncanonical(d):              # a class root labelled by a larger member
        lab = d['per_k'][k1]['labels']; b = next(x for x in range(64) if lab[x] != x); d['per_k'][k1]['labels'][lab[b]] = b
    return [
        ('good_full_packet_passes', 'file', lambda d: None, None),
        ('good_stage_binding_passes', 'stage', dict(good_stage), None),
        ('types_per_k_null', 'file', lambda d: d.__setitem__('per_k', None), 'types: per_k'),
        ('types_labels_dict', 'file', lambda d: d['per_k'][k1].__setitem__('labels', {}), 'types: per depth'),
        ('types_started_dict', 'file', lambda d: d.__setitem__('started', {}), 'types: started'),
        ('types_elapsed_string', 'file', lambda d: d.__setitem__('elapsed_s', '1'), 'types: elapsed_s'),
        ('keys_extra_top_key', 'file', lambda d: d.__setitem__('extra', 1), "keys: top level ['extra']"),
        ('keys_stopped_present', 'file', lambda d: d.__setitem__('stopped', 'x'), "keys: top level ['stopped']"),
        ('keys_depth_missing', 'file', lambda d: d['per_k'].pop(k2), 'keys: per depth'),
        ('keys_merged_extra', 'file', lambda d: d['merged'].__setitem__('x', 1), 'keys: sections'),
        ('domains_wrong_digest', 'file', lambda d: d.__setitem__('this_sha256', '0' * 64), 'domains: source digest'),
        ('domains_wrong_dependency', 'file', lambda d: d.__setitem__('coll_sha256', '0' * 64), 'domains: dependency digest'),
        ('domains_wrong_scope', 'file', lambda d: d['scope'].__setitem__('depths', [100, 200, 402]), 'domains: scope'),
        ('domains_negative_timing', 'file', lambda d: d['timing'].__setitem__('assemble_s', -1.0), 'domains: timing'),
        ('domains_nan_elapsed', 'memory', lambda d: d.__setitem__('elapsed_s', nan), 'domains: timing'),
        ('domains_inf_timing', 'memory', lambda d: d['timing'].__setitem__('lane_psi_s', float('inf')), 'domains: timing'),
        ('domains_label_out_of_range', 'file', lambda d: d['per_k'][k1]['labels'].__setitem__(0, 64), 'domains: per depth'),
        ('domains_group_singleton', 'file', lambda d: d['merged']['groups'].append([0]), 'domains: moves or merged'),
        ('parse_nan_token', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": NaN, "x_": ', 1), PARSE_FAIL),
        ('parse_exponent_overflow', 'text', lambda t: t.replace('"elapsed_s": ', '"elapsed_s": 1e999, "x_": ', 1), PARSE_FAIL),
        ('bindings_explicit_false_base', 'file', lambda d: d['controls']['base'].__setitem__(BASE_KEYS[0], False), 'bindings: base controls'),
        ('bindings_mutant_all_true', 'file', lambda d: [d['controls'].__setitem__(m, {k: True for k in BASE_KEYS}) for m in MUTANTS],
         'bindings: mutant %s not caught by its own outcomes' % MUTANTS[0]),
        ('bindings_stage_values_off_scope', 'file', lambda d: d['bindings'].update(good_stage), OFF_SCOPE_FAIL),
        ('bindings_stage_count_false', 'stage', dict(good_stage, count_equal=False), STAGE_BIND_FAIL),
        ('bindings_stage_missing', 'stage', {'count_equal': None, 'by_support_equal': None, 'labels_equal': None}, STAGE_BIND_FAIL),
        ('bindings_stage_labels_false', 'stage', dict(good_stage, labels_equal=False), STAGE_BIND_FAIL),
        ('bindings_move_pair_split', 'file', move_split, MOVE_SPLIT_FAIL % k2),
        ('bindings_move_count', 'file', lambda d: d['moves'].__setitem__('count', d['moves']['count'] + 1), 'bindings: move partition'),
        ('arithmetic_noncanonical_label', 'file', noncanonical, 'arithmetic: labels not canonical (K = %s)' % k1),
        ('arithmetic_stale_count', 'file', stale_count, 'arithmetic: counts vs labels (K = %s)' % k1),
        ('arithmetic_refine_flag', 'file', dishonest_flag, 'arithmetic: refinement or merges (K = %s)' % k3),
        ('arithmetic_nesting', 'file', split_deep, None),          # its exact diagnostic is set below, after one evaluation
        ('arithmetic_merged_groups', 'file', lambda d: d['merged'].__setitem__('total', d['merged']['total'] + 1), 'arithmetic: merged groups'),
        ('completion_flag_false', 'file', lambda d: d.__setitem__('complete', False), 'completion: complete flag'),
    ]


GATE_KEYS = ('good_full_packet_passes', 'good_stage_binding_passes', 'types_per_k_null', 'types_labels_dict', 'types_started_dict',
             'types_elapsed_string', 'keys_extra_top_key', 'keys_stopped_present', 'keys_depth_missing', 'keys_merged_extra',
             'domains_wrong_digest', 'domains_wrong_dependency', 'domains_wrong_scope', 'domains_negative_timing', 'domains_nan_elapsed',
             'domains_inf_timing', 'domains_label_out_of_range', 'domains_group_singleton', 'parse_nan_token', 'parse_exponent_overflow',
             'bindings_explicit_false_base', 'bindings_mutant_all_true', 'bindings_stage_values_off_scope', 'bindings_stage_count_false',
             'bindings_stage_missing', 'bindings_stage_labels_false', 'bindings_move_pair_split', 'bindings_move_count', 'arithmetic_noncanonical_label', 'arithmetic_stale_count', 'arithmetic_refine_flag',
             'arithmetic_nesting', 'arithmetic_merged_groups', 'completion_flag_false')


def gate_controls():
    import copy, tempfile
    X, M, C = deps()
    bits, _ = X.compute(GATE_B, GATE_DEPTHS[-1])
    sections, timing = assemble(bits, GATE_B, GATE_DEPTHS)
    sections = json.loads(json.dumps(sections, allow_nan=False))
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'finished': 'f', 'elapsed_s': 0.1, 'this_sha256': 'S', 'coll_sha256': COLL_SHA256,
            'scope': {'B': GATE_B, 'depths': list(GATE_DEPTHS)},
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'timing': {'lane_psi_s': 0.0, **timing}, 'complete': True, **sections}
    res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', GATE_B, GATE_DEPTHS)
        for name, kind, f, want in gate_fixtures():
            if name == 'arithmetic_nesting': want = 'arithmetic: nesting (%d within %d)' % (GATE_DEPTHS[1], GATE_DEPTHS[0])
            if kind == 'stage':
                res[name] = stage_binding_problem(f, STAGE_SCOPE) == want; continue
            bad = copy.deepcopy(good)
            if kind == 'memory':
                f(bad); res[name] = validate_result(bad, 'S', GATE_B, GATE_DEPTHS) == want; continue
            if kind == 'text':
                open(rp, 'w').write(f(json.dumps(bad, allow_nan=False)))
            else:
                f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            verdict, note = m(0, '')
            res[name] = (verdict == 'pass') if want is None else (verdict == 'FAIL' and note == (want if kind == 'text' else 'rc 0: ' + want))
    assert set(res) == set(GATE_KEYS) and len(res) == len(GATE_KEYS)
    return res


def stage(out, B, depths):
    import w1a_harness as H
    if hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest() != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)):
        print('REFUSED: OUT must be absolute and new or empty'); return 3
    if (B,) + tuple(depths) != STAGE_SCOPE:
        print('REFUSED: the only admitted stage scope is B = 16, depths 800, 1600, 3200'); return 3
    deps()
    os.makedirs(out, exist_ok=True)
    src_sha = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 4 << 30; H.CAPS['artifacts_max_bytes'] = 50 << 20; H.CAPS['log_max_bytes'] = 10 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['cq01_kernel'] = {'this_sha256': src_sha, 'coll_sha256': COLL_SHA256, 'w1a_sha256': W1A_SHA256, 'scope': {'B': B, 'depths': list(depths)},
                         'caps': {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 4 << 30, 'artifacts_max_bytes': 50 << 20}}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'cq01_kernel_result.json'), src_sha, B, depths)
    rec = sup.run_step('cq01_kernel', [sys.executable, os.path.abspath(__file__), 'run', rdir, str(B)] + [str(k) for k in depths], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 6 and a[0] in ('run', 'stage'):
        B, depths = int(a[2]), tuple(int(x) for x in a[3:])
        if a[0] == 'run':
            if not (6 <= B <= 16 and all(k % 2 == 0 for k in depths) and depths[0] < depths[1] < depths[2] <= 3200):
                print('REFUSED: run admits 6 <= B <= 16 and even depths K1 < K2 < K3 <= 3200'); sys.exit(3)
            R = run(a[1], B, depths); print('CQ01 KERNEL RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
        sys.exit(stage(a[1], B, depths))
    print(__doc__); sys.exit(2)
