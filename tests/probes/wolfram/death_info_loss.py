#!/usr/bin/env python3
"""Exact free-bit information-loss baselines on CL632's per-lane death tables, revision 2 (Local, 2026-10-25, L941; GPT's GC1870 gate
repairs, made before any stage). NOT an agreed job until GPT accepts this exact file; nothing runs on import; `--controls` runs the small
CPU controls only, with no data.
Revision 2 (GC1870; the mathematics, orientations, labels, predictions and caps of revision 1 unchanged):
  - every control report is checked as a dict with exactly BASE_KEYS and Boolean values, and base_all_pass, each mutant's caught flag and
    ok are recomputed from those details: a roll-up can no longer stand in for missing or contrary evidence; gate_controls likewise;
  - every comparison in the gate is type-strict (same(): 1 is not True); replay and binding subfields have exact keys and types;
  - each permutation digest is a 64-hex string bound to a frozen pin (PERM_SHA256, computed from the seed and width alone, no data), and
    the run refuses a permutation whose digest is not the pin. The digest binds the permutation's identity only; the permuted statistics
    are checked by the same domains, endpoints and equivalences as the real table, not recomputed by the gate;
  - each row's intrinsic equivalences: mixed = 0 iff e01 = 0 (and, for a nondegenerate label, iff ber = 0) for A and for B; dmixed = 0
    iff ssw = 0; in the real and the permuted table;
  - every metadata file is parsed from the same bounded buffer whose digest was checked (arrays already were), in the run and the stage;
  - prose: the counts of mixed classes are NOT monotone (the XOR fixture goes 1, 2, 0); what is nonincreasing is each error, the residual,
    and the lanes in mixed classes; B is named for what its rule is, the conservative ten-percent upper tail; R^2 = 1 for constant data
    is a convention; predictions are scored from the exact integers, the floats being for display only.
Revision 1 (0b531db1, L940) was reviewed in GC1870: mathematics carried, seven gate false passes, launch not accepted.

If this holds, it changes the all-width D(W) row (CL631 item 5): it measures exactly, on each finite constrained class, how much of the
death time and of two survival labels ANY function of k end free bits can know, before any model is fitted. These are finite descriptive
oracles per width (GC1867): no generalization to a withheld width and no all-width locality theorem; a mixed class is an exact
counterexample to that width's k-bit sufficiency, nothing more.

The population (CL632; death_tables.py a578883c, read): width W in STAGE_WIDTHS = 8, 12, ..., 40; n = W/2; lane l in [0, 2^n) carries the
odd trace bits b_i = a(2i + 1) = bit i of l, all even trace bits below W black; death d(l) = the first even time with depth 1 white,
W <= d <= 4W, none censored at these widths (GC1869's table). Inputs: deaths_W.npy from the shared store's cited/deaths/, each byte-checked
against manifest-v2 AND the digest pinned below (manifest-v3's array entries are the same bytes; its corrected source naming does not
touch these pins, GC1870); the histogram, D, maximizers, minimum and censor count must equal GPT's file-audit.json; GPT's label-check.json
lanes 47284, 180, 47104 at W = 40 must read 66, 40, 42, and its file digest must be the pinned W = 40 array's.
Widths 44, 48 and 52 are SEALED: never opened here, so their bit-label relationship stays unseen for a later frozen model test (their
aggregate histograms are already known; W = 40 is exploratory).

Frozen conventions (GC1869):
  - labels: A = 1[d > 3W/2] (strict; GC1869's death > 60 at W = 40). B = the conservative ten-percent upper tail: d* = the least even d0
    in [W, 4W + 2] with #{d >= d0} <= floor(N/10), B = 1[d >= d*], the largest upper tail of whole death values holding at most a tenth of
    the lanes; it can underfill far below N/10, or be empty (its positive count is reported). The regression target is d itself.
  - orientation: 'early' = (b_0 .. b_(k-1)) = l mod 2^k, trace times 1, 3, .., 2k - 1; 'late' = (b_(n-k) .. b_(n-1)) = l >> (n - k),
    trace times W - 2k + 1, .., W - 1, the last trace samples before the first unconstrained even time W. Every k = 0, 1, .., n.
  - every class has exactly m = 2^(n-k) lanes (the lanes are the full product of the n bits), so every quantity is an exact integer.
Quantities, for each W, orientation and k; N1(z), N0(z) = m - N1(z) are a class's label counts, P and Q = N - P the totals:
  - mixed: classes holding both labels; the label is exactly determined by these k bits iff it is 0;
  - e01 = sum_z min(N0, N1): N times the least 0-1 error of ANY deterministic predictor from these bits (GC1867);
  - ber = sum_z min(N1 Q, N0 P): 2PQ times the least class-balanced error (1/2)(FN/P + FP/Q), attained by predicting 1 iff N1 Q > N0 P
    (ties to 0); null when P = 0 or Q = 0 (W = 8 has no A-positive: its maximum is 12 = 3W/2);
  - ssw = m sum d^2 - sum_z S(z)^2, S(z) a class's death sum: m N times the least mean squared error of any death prediction from these
    bits (GC1867's within-class variance); R^2(k) = 1 - (ssw_k / m_k) / (ssw_0 / N), and 1 by convention for constant data;
  - dmixed: classes holding more than one death value; d is exactly determined by these bits iff it is 0.
  Each partition refines the last, so e01, ber, the residual ssw/m and the lanes in mixed classes (mixed times m, likewise dmixed) are
  nonincreasing in k; the COUNTS mixed and dmixed can at most double from k to k + 1, and need not fall. The two orientations agree at
  k = 0 and k = n, and at k = n everything is 0.
The negative control on the real data: the same table for d composed with one fixed permutation per width (numpy PCG64, seed
PERM_SEED + W, its digest pinned in PERM_SHA256). Over a uniformly random permutation of nonconstant data, R^2(k) has expectation exactly
(2^k - 1)/(N - 1); one fixed draw is a control, not a confidence interval.
The unexpected check, an independent replay of the data's semantics (GC1869 notes none was executed): for W = 8, 12, 16 every width-W
start (cells 1..W free, the wall at depth 0 white, everything else white) is evolved forward directly, with no trace reconstruction, by
new[k] = row[k+1] XOR (row[k] OR row[k-1]); a(t) is depth 1. The constrained starts (a black at every even t < W) must number 2^(W/2),
map bijectively onto the lanes by l = sum a(2i+1) 2^i, and have the table's deaths lane by lane.

Controls (`--controls`, CPU, no data; all must pass before a stage):
  - the integer table against first principles on 24 pseudo-random populations with n <= 6, every k and both orientations: class
    membership by integer division, exact fractions for the within-class error, and for k <= 3 the least 0-1 and balanced errors found by
    enumerating every deterministic rule;
  - orientation fixtures at n = 6: A = b0 XOR b1 is determined early at k = 2 and late only at k = 6; d = W + 2 b5 has R^2 = 1 late from
    k = 1 and exactly 0 early below k = 6; the label edge d = 3W/2 is A-negative;
  - the replay engine against GC1867's width-2 hand deaths: the starts (1,1), (1,0), (0,1), (0,0) die at 6, 2, 0, 0, and the two
    constrained ones are lanes 0 and 1;
  - the bounded reader: a file one byte over its bound is refused, and the parsed object comes from the digested buffer;
  - six mutants, each of which must fail a control: 'orient' (early and late swapped), 'shift' (late reads l >> (n - k + 1)), 'berswap'
    (min(N1 P, N0 Q)), 'sswdenom' (the class size 2^k in place of 2^(n - k)), 'labelge' (A = d >= 3W/2), 'traceeven' (replay lanes read
    a(2i)).
The result gate (GC1813's method): bounded bytes, strict reading (no NaN, Infinity or overflowing exponent), then one explicit schema in the
order types, exact key sets, domains, input bindings, arithmetic, completion, inside one fail-closed matcher; every comparison type-strict.
The valid full synthetic packet is assembled by the run's own assembly code from a replay-generated table at W = 4 and a hand-made one at
W = 8 (HAND_8, with A-positives); every negative fixture, including GC1870's nine literal JSON cases, names its exact diagnostic. The gate's
added work is string and integer comparison only (no permutation is regenerated in the parent).

Proposed stage: `stage OUT INDIR`, all of STAGE_WIDTHS (the only scope); W1A caps: stage, step wall and CPU 300 s, group RSS 2 GiB,
artifacts 10 MiB, log 5 MiB; W1A's inherited pressure, swap-growth, free-disk and monitor-failure stops in force (sampled operational
guards, not OS ceilings); launched only with fresh host headroom and no other research stage on the M5. `run OUT INDIR` is the stage's
child.
Predictions (written before any bit-label statistic was computed, unchanged from revision 1 but for B's name; seen: GPT's GC1869
histograms, survival table, its 537 A-positives at W = 40 and its three-lane countercontrol; scored from the exact integers):
  P1 at W = 40, e01_A(k) = P_A for every k <= 16 in both orientations (no class of 16 or more lanes has an A-positive majority);
     counterfactual: some k <= 12 has e01_A < P_A.
  P2 at W = 40, the balanced error ber_A / 2PQ at k = 10 is >= 0.10 in both orientations; counterfactual (CL631's): <= 0.05 in one.
  P3 (low confidence) at W = 40, k = 10: late beats early, ber_A late < early and R^2 late > early; counterfactual: both reversed.
  P4 at W = 40, R^2(10) <= 0.5 in both orientations; counterfactual: >= 0.8 in one.
  P5 for every W in 12..40, dmixed(n - 1) > 0 in both orientations (the omitted end bit changes SOME death); counterfactual: a zero, an
     exact irrelevance of that bit at that width.
  P6 R^2(8) at W = 40 is below R^2(8) at W = 24 in each orientation; counterfactual: higher at W = 40 in both.
  P7 at W = 40, for every k from 6 to n - 1 and both orientations, the real R^2(k) exceeds the permuted R^2(k) by >= 0.02, and the permuted
     R^2(k) is within a factor 2 of (2^k - 1)/(N - 1) for 6 <= k <= n - 2.
  P8 at W = 40, k = 10, ber_B / 2PQ < ber_A / 2PQ in both orientations (B the conservative ten-percent upper tail).
  Replay: every lane agrees at 8, 12 and 16; counterfactual: any disagreement voids this stage's reading of the data.
Usage: python3 death_info_loss.py --controls | run OUT INDIR | stage OUT INDIR
"""
import hashlib, io, json, math, os, random, re, sys, tempfile, time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
W1A_SHA256 = '3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883'
MANIFEST_V2_SHA256 = '0913be6442cecfaac1d6be52b98bbf260bae8d608868237e82aaaa94ef90b65d'
FILE_AUDIT_SHA256 = '6ee0978f90db553859ee92c4a0dea56a3f056b429d6045eb0eb5f99d2ed5c899'
LABEL_CHECK_SHA256 = '1dbc210a79f161c508e54461bde2d1c92cc81b47522d9b3d4504630c761b9b4e'
ARRAY_SHA256 = {8: 'ebe5395971c0c9a2673726b625f4ff3698e42221ea3c87bf803ec6b17998b9a5',
                12: '5a44a77a035131c423048596622f5fbb42b852620f9a5ddd67c6b05f262781f9',
                16: '15610eaf680595fe6347454ce4b13ddb92d758250bb5d28092504ab40cc1e7f1',
                20: 'e04e9912364ee4380e1b3abeda4d4a4885a5adedb4e093f99532f1a642f0dcb9',
                24: '74d30d9f198da88d3f5a65afc8bf383bf2fd790cfc026bf630c958159b3f64e2',
                28: 'bc08cb56a6a078a0d7ea021d2488e3b8c7c7202ab4a929cfd634404ef1f76b93',
                32: '97be06aaa0f5590c210c6627b50528a0f0573b38602d5b64133996056ff9e7a9',
                36: 'b481d03751b19c7b23cb0963817a1b472669bab145cc3996dd248c788536b712',
                40: '7fe7cfbc6200e52ec749c53d20950539364a3cf283d387b38e2befde44a395b8'}   # copied from manifest-v2 by script
PERM_SHA256 = {8: '08d71f31add5dba4899805a876a2cfe1fa28ac4cba1f0988c2171c80ce7eeffa',
                12: '1693c594dbdf8fbaf5b1ceed16d3dfbe5566e69042f94f7fbc23187e74efe2fc',
                16: '4fbe3933ac25fdc8dc5d33404b18bf91db1f56807d65c1918bae747f37013318',
                20: '3939387994a2ebcd90db5802673ee8c27e9a0d479c4b8557c1fc80e80cac87f1',
                24: '8cb42cd06678da960c48d95f706e6db8bd2a4f04db3682e97526f83caa967267',
                28: '535532a833650d71b08d1b66dbb0df9d164bb3b06c61fe35c69427c4b3772f17',
                32: '00fc49857765ecf4b9ef8ff0f6163bbc9ffe2adc23312fa0875e8afbe851e93c',
                36: '605aa02d1e36520ca6c1ac3f4dc63f7b99cd7a56e688f7d412327fdda883d934',
                40: '7b37c71682b86b01ee174aea5993ebcbceb495ba1c3113ed966e02daa3b4155e'}   # perm_digest(perm_of(W, 2^(W/2))), computed by script from the seed alone
STAGE_WIDTHS = (8, 12, 16, 20, 24, 28, 32, 36, 40)
SEALED_WIDTHS = (44, 48, 52)
REPLAY_WIDTHS = (8, 12, 16)
SYNTH_WIDTHS = (4, 8)
HAND_8 = (8, 14, 10, 8, 16, 8, 12, 20, 8, 10, 14, 8, 18, 8, 10, 24)   # the synthetic W = 8 table: six A-positives, d* = 22
PERM_SEED = 20261025
LABEL_LANES = {'47284': 66, '180': 40, '47104': 42}
POS_A_40 = 537
STAGE_S = 300
JSON_MAX_BYTES = 64 << 10
ORIENTS = ('early', 'late')
MUTANTS = ('orient', 'shift', 'berswap', 'sswdenom', 'labelge', 'traceeven')
BASE_KEYS = ('table_equals_first_principles_n_le_6', 'orientation_fixtures_n6', 'label_edge_A_negative', 'replay_equals_gc1867_width2',
             'bounded_reader')
PARSE_FAIL = 'parse: nonfinite or invalid JSON'
MAX_RESULT_BYTES = 16 << 20
TOL = 1e-9
HEX64 = re.compile(r'[0-9a-f]{64}')


def same(a, b):
    """Type-strict deep equality (GC1870): 1 is not True and 1.0 is not 1."""
    if type(a) is not type(b): return False
    if isinstance(a, dict): return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list): return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b


def read_bounded(path, limit):
    """The file's bytes, refused if longer than limit; callers digest and parse this one buffer."""
    with open(path, 'rb') as f:
        raw = f.read(limit + 1)
    if len(raw) > limit: raise SystemExit('REFUSED: %s exceeds %d bytes' % (os.path.basename(path), limit))
    return raw


def labels(d, W, mutant=''):
    """A, B as int64 0/1 arrays and B's threshold d*."""
    import numpy as np
    N = int(d.size); half = 3 * W // 2
    A = (d >= half) if mutant == 'labelge' else (d > half)
    dstar = next(d0 for d0 in range(W, 4 * W + 3, 2) if int((d >= d0).sum()) <= N // 10)
    return A.astype(np.int64), (d >= dstar).astype(np.int64), dstar


def class_view(x, n, k, orient, mutant=''):
    """x as a (classes, m) array, one row per class of the k end bits."""
    if mutant == 'orient':
        orient = 'late' if orient == 'early' else 'early'
    if orient == 'early':
        return x.reshape(1 << (n - k), 1 << k).T              # row z: the lanes with l mod 2^k = z
    j = k - 1 if (mutant == 'shift' and k >= 1) else k
    return x.reshape(1 << j, 1 << (n - j))                    # row z: the lanes with l >> (n - j) = z


def table(d, A, B, n, mutant=''):
    """{orient: rows k = 0..n of [mixedA, e01A, berA, mixedB, e01B, berB, ssw, dmixed]}."""
    import numpy as np
    N = 1 << n; sq = int((d * d).sum()); out = {}
    tot = ((A, int(A.sum())), (B, int(B.sum())))
    for o in ORIENTS:
        rows = []
        for k in range(n + 1):
            row = []
            for Y, P in tot:
                Q = N - P; c = class_view(Y, n, k, o, mutant); m = c.shape[1]
                N1 = c.sum(axis=1); N0 = m - N1
                if P == 0 or Q == 0: ber = None
                elif mutant == 'berswap': ber = int(np.minimum(N1 * P, N0 * Q).sum())
                else: ber = int(np.minimum(N1 * Q, N0 * P).sum())
                row += [int(((N1 > 0) & (N1 < m)).sum()), int(np.minimum(N0, N1).sum()), ber]
            c = class_view(d, n, k, o, mutant); m = c.shape[1]; S = c.sum(axis=1)
            mm = (1 << k) if mutant == 'sswdenom' else m
            row += [mm * sq - int((S * S).sum()), int((c.min(axis=1) != c.max(axis=1)).sum())]
            rows.append(row)
        out[o] = rows
    return out


def first_principles(dl, W, n, k, orient):
    """The same row from definitions, for the controls: class membership by integer division, exact fractions, and for k <= 3 the least
    errors found by enumerating every deterministic rule on the classes."""
    N = 1 << n; half = 3 * W // 2
    dstar = min(d0 for d0 in range(W, 4 * W + 3, 2) if sum(1 for x in dl if x >= d0) <= N // 10)
    cls = {}
    for l in range(N):
        cls.setdefault(l % (1 << k) if orient == 'early' else l // (1 << (n - k)), []).append(l)
    zs = sorted(cls); row = []
    for Y in ([int(x > half) for x in dl], [int(x >= dstar) for x in dl]):
        P = sum(Y); Q = N - P
        n1 = [sum(Y[l] for l in cls[z]) for z in zs]; n0 = [len(cls[z]) - a for z, a in zip(zs, n1)]
        mixed = sum(1 for a, b in zip(n1, n0) if a and b)
        if k <= 3:
            rules = [[(r >> i) & 1 for i in range(len(zs))] for r in range(1 << len(zs))]
            e01 = min(sum(b if y else a for a, b, y in zip(n1, n0, rule)) for rule in rules)
            if P and Q:
                best = min(Fraction(sum(a for a, y in zip(n1, rule) if not y), P) + Fraction(sum(b for b, y in zip(n0, rule) if y), Q) for rule in rules)
                ber = best * P * Q
                assert ber.denominator == 1; ber = int(ber)
            else:
                ber = None
        else:
            e01 = sum(min(a, b) for a, b in zip(n1, n0))
            ber = sum(min(a * Q, b * P) for a, b in zip(n1, n0)) if P and Q else None
        row += [mixed, e01, ber]
    sse = sum(sum((Fraction(dl[l]) - Fraction(sum(dl[x] for x in cls[z]), len(cls[z]))) ** 2 for l in cls[z]) for z in zs)
    row += [int(sse * (N >> k)), sum(1 for z in zs if len({dl[l] for l in cls[z]}) > 1)]
    return row


def replay(W, mutant=''):
    """Every width-W start evolved directly to time 4W: (constrained mask, lane of each start, first even white time or 0xFFFF)."""
    import numpy as np
    S = 1 << W; T = 4 * W; width = W + T + 2
    s = np.arange(S, dtype=np.int64)
    row = np.zeros((S, width), dtype=np.uint8)
    for c in range(1, W + 1):
        row[:, c] = (s >> (c - 1)) & 1
    a = np.zeros((T + 1, S), dtype=np.uint8)
    for t in range(T + 1):
        a[t] = row[:, 1]
        new = np.zeros_like(row)
        new[:, 1:width - 1] = row[:, 2:width] ^ (row[:, 1:width - 1] | row[:, 0:width - 2])
        row = new
    cons = np.all(a[0:W:2] == 1, axis=0)
    off = 0 if mutant == 'traceeven' else 1
    lanes = np.zeros(S, dtype=np.int64)
    for i in range(W // 2):
        lanes |= a[2 * i + off].astype(np.int64) << i
    white = a[0:T + 1:2] == 0
    first = np.where(white.any(axis=0), white.argmax(axis=0) * 2, 0xFFFF)
    return cons, lanes, first


def replay_table(W, mutant=''):
    """The lane -> death table a replay implies, or None if its constrained starts are not a bijection onto the lanes."""
    import numpy as np
    cons, lanes, first = replay(W, mutant)
    L = lanes[cons]
    if int(cons.sum()) != 1 << (W // 2) or not np.array_equal(np.sort(L), np.arange(1 << (W // 2))): return None
    d = np.zeros(1 << (W // 2), dtype=np.int64); d[L] = first[cons]
    return d


def replay_check(W, d, mutant=''):
    import numpy as np
    cons, lanes, first = replay(W, mutant)
    L = lanes[cons]; count = int(cons.sum())
    bij = count == (1 << (W // 2)) and bool(np.array_equal(np.sort(L), np.arange(1 << (W // 2))))
    return {'constrained': count, 'bijection': bool(bij), 'deaths_equal': bool(bij and np.array_equal(first[cons], d[L]))}


def hist(d):
    import numpy as np
    v, c = np.unique(d, return_counts=True)
    return {str(int(a)): int(b) for a, b in zip(v, c)}


def perm_of(W, N):
    import numpy as np
    return np.random.Generator(np.random.PCG64(PERM_SEED + W)).permutation(N)


def perm_digest(p):
    return hashlib.sha256(p.astype('<i8').tobytes()).hexdigest()


def reading(tab, P_A, P_B, n):
    """Floats for display, recomputed by the gate: per row [ber_A / 2PQ, ber_B / 2PQ, R^2]."""
    N = 1 << n; out = {}
    for o in ORIENTS:
        rows = tab[o]; s0 = rows[0][6]; r = []
        for k, row in enumerate(rows):
            fa = None if row[2] is None else round(row[2] / (2 * P_A * (N - P_A)), 12)
            fb = None if row[5] is None else round(row[5] / (2 * P_B * (N - P_B)), 12)
            r2 = 1.0 if s0 == 0 else round(float(1 - Fraction(row[6] * N, (N >> k) * s0)), 12)
            r.append([fa, fb, r2])
        out[o] = r
    return out


def assemble_width(W, d, perm_pin, mutant=''):
    """One width's section of the result, from its death table (int64 array indexed by lane); refuses a permutation off its pin."""
    n = W // 2; N = 1 << n
    A, B, dstar = labels(d, W, mutant)
    tab = table(d, A, B, n, mutant)
    p = perm_of(W, N); ph = perm_digest(p)
    if ph != perm_pin: raise SystemExit('REFUSED: permutation digest W=%d' % W)
    dp = d[p]; Ap, Bp, _ = labels(dp, W, mutant)
    ptab = table(dp, Ap, Bp, n, mutant)
    P_A, P_B = int(A.sum()), int(B.sum())
    return {'n': n, 'N': N, 'P_A': P_A, 'P_B': P_B, 'dstar': int(dstar), 'hist': hist(d), 'sum': int(d.sum()), 'sq': int((d * d).sum()),
            'table': tab, 'reading': reading(tab, P_A, P_B, n), 'perm_sha256': ph, 'perm_table': ptab, 'perm_reading': reading(ptab, P_A, P_B, n)}


def controls(mutant=''):
    import numpy as np
    R = {}
    rng = random.Random(20261025); ok = True
    for i in range(24):
        n = 2 + i % 5; W = 2 * n; N = 1 << n
        dl = [rng.randrange(W, 4 * W + 1, 2) for _ in range(N)]
        if i % 3 == 0: dl[rng.randrange(N)] = 3 * W // 2
        d = np.array(dl, dtype=np.int64); A, B, _ = labels(d, W, mutant); tab = table(d, A, B, n, mutant)
        for o in ORIENTS:
            for k in range(n + 1):
                ok = ok and tab[o][k] == first_principles(dl, W, n, k, o)
    R[BASE_KEYS[0]] = ok
    n = 6; W = 12; l = np.arange(64, dtype=np.int64)
    Y = (l & 1) ^ ((l >> 1) & 1); d = W + 2 * ((l >> 5) & 1); tab = table(d, Y, Y, n, mutant)
    e = [r[1] for r in tab['early']]; lt = [r[1] for r in tab['late']]
    s0 = tab['early'][0][6]
    R[BASE_KEYS[1]] = (e == [32, 32, 0, 0, 0, 0, 0] and lt == [32] * 6 + [0] and [r[0] for r in tab['early']] == [1, 2, 0, 0, 0, 0, 0]
                       and [r[6] for r in tab['late']] == [s0] + [0] * 6 and [r[6] * 2 ** k for k, r in enumerate(tab['early'])][:6] == [s0] * 6
                       and tab['early'][6][6] == 0 and s0 > 0)
    A, _, _ = labels(np.array([16, 18, 20, 22], dtype=np.int64), 12, mutant)
    R[BASE_KEYS[2]] = A.tolist() == [0, 0, 1, 1]
    cons, lanes, first = replay(2, mutant)
    R[BASE_KEYS[3]] = (first.tolist() == [0, 2, 0, 6] and cons.tolist() == [False, True, False, True] and lanes.tolist()[1] == 1 and lanes.tolist()[3] == 0)
    with tempfile.TemporaryDirectory() as t:
        p = os.path.join(t, 'x.json'); body = b'{"a": [1, 2]}'
        open(p, 'wb').write(body)
        good = read_bounded(p, len(body)) == body and json.loads(read_bounded(p, len(body))) == {'a': [1, 2]}
        try:
            read_bounded(p, len(body) - 1); refused = False
        except SystemExit:
            refused = True
    R[BASE_KEYS[4]] = good and refused
    return {k: bool(v) for k, v in R.items()}


def control_report():
    base = controls(); R = {'base': base, 'base_all_pass': all(base.values())}
    for m in MUTANTS:
        R[m] = controls(m); R[m + '_caught'] = not all(R[m].values())
    R['ok'] = R['base_all_pass'] and all(R[m + '_caught'] for m in MUTANTS)
    return R


def strict_loads(raw):
    """JSON with no NaN, no Infinity and no float that overflows to infinity (GC1818)."""
    def const(tok): raise ValueError('nonfinite constant')
    def flt(tok):
        x = float(tok)
        if not math.isfinite(x): raise ValueError('nonfinite number')
        return x
    return json.loads(raw, parse_constant=const, parse_float=flt)


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def verified_json(path, pin):
    """One bounded buffer, digested against its pin and parsed from the same bytes (GC1870)."""
    raw = read_bounded(path, JSON_MAX_BYTES)
    if hashlib.sha256(raw).hexdigest() != pin: raise SystemExit('REFUSED: %s digest' % os.path.basename(path))
    return json.loads(raw)


def load_inputs(indir):
    """Every input byte-checked before use; raises SystemExit naming the first refusal."""
    import numpy as np
    man = {f['name']: f for f in verified_json(os.path.join(indir, 'manifest-v2.json'), MANIFEST_V2_SHA256)['files']}
    audit = {f['W']: f for f in verified_json(os.path.join(indir, 'file-audit.json'), FILE_AUDIT_SHA256)['files']}
    lc = verified_json(os.path.join(indir, 'label-check.json'), LABEL_CHECK_SHA256)
    tables = {}
    for W in STAGE_WIDTHS:
        name = 'deaths_%d.npy' % W; raw = read_bounded(os.path.join(indir, name), man[name]['bytes']); h = hashlib.sha256(raw).hexdigest()
        if h != ARRAY_SHA256[W] or h != man[name]['sha256'] or len(raw) != man[name]['bytes']: raise SystemExit('REFUSED: %s digest' % name)
        a = np.load(io.BytesIO(raw), allow_pickle=False)
        if a.dtype != np.dtype('<u2') or a.shape != (1 << (W // 2),) or np.isfortran(a): raise SystemExit('REFUSED: %s format' % name)
        d = a.astype(np.int64)
        if bool((d % 2).any()) or int(d.min()) < W or int(d.max()) > 4 * W: raise SystemExit('REFUSED: %s values' % name)
        tables[W] = d
    return tables, audit, lc


def expect_real(audit):
    return {'widths': STAGE_WIDTHS, 'replay': REPLAY_WIDTHS, 'sha': {W: ARRAY_SHA256[W] for W in STAGE_WIDTHS},
            'perm': {W: PERM_SHA256[W] for W in STAGE_WIDTHS}, 'audit': {W: audit[W] for W in STAGE_WIDTHS},
            'inputs': {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256, 'label_check': LABEL_CHECK_SHA256},
            'label_lanes': LABEL_LANES, 'pos_A_40': POS_A_40}


def run(out, indir):
    os.makedirs(out, exist_ok=True); t0 = time.monotonic()
    R = {'started': time.strftime('%Y-%m-%dT%H:%M:%S'), 'this_sha256': sha(os.path.abspath(__file__)), 'complete': False}
    def save():
        R['elapsed_s'] = round(time.monotonic() - t0, 2); tmp = os.path.join(out, 'death_info_loss_result.json.tmp')
        json.dump(R, open(tmp, 'w'), allow_nan=False); os.replace(tmp, os.path.join(out, 'death_info_loss_result.json'))
    R['controls'] = control_report(); R['gate_controls'] = gate_controls(); save()
    if not (R['controls']['ok'] and all(R['gate_controls'].values())):
        R['stopped'] = 'a control or mutant check failed'; save(); raise SystemExit(1)
    try:
        tables, audit, lc = load_inputs(indir)
        R['inputs'] = {'manifest_v2': MANIFEST_V2_SHA256, 'file_audit': FILE_AUDIT_SHA256, 'label_check': LABEL_CHECK_SHA256,
                       'arrays': {str(W): ARRAY_SHA256[W] for W in STAGE_WIDTHS}}
        R['widths'] = {str(W): assemble_width(W, tables[W], PERM_SHA256[W]) for W in STAGE_WIDTHS}
    except SystemExit as e:
        R['stopped'] = str(e); save(); raise
    R['replay'] = {str(W): replay_check(W, tables[W]) for W in REPLAY_WIDTHS}
    lanes = {k: int(tables[40][int(k)]) for k in LABEL_LANES}
    R['bindings'] = {'label_lanes': lanes, 'label_lanes_equal': same(lanes, LABEL_LANES) and lc.get('file_sha256') == ARRAY_SHA256[40] and lc.get('W') == 40,
                     'pos_A_40': R['widths']['40']['P_A'], 'pos_A_40_equal': R['widths']['40']['P_A'] == POS_A_40}
    R['finished'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    prob = validate_result(R | {'complete': True, 'elapsed_s': 0.0}, R['this_sha256'], expect_real(audit))
    R['complete'] = prob is None
    if prob: R['stopped'] = 'incomplete: %s (no retry)' % prob
    save()
    return R


TOP_KEYS = {'started', 'this_sha256', 'controls', 'gate_controls', 'inputs', 'widths', 'replay', 'bindings', 'finished', 'complete', 'elapsed_s'}
WIDTH_KEYS = {'n', 'N', 'P_A', 'P_B', 'dstar', 'hist', 'sum', 'sq', 'table', 'reading', 'perm_sha256', 'perm_table', 'perm_reading'}
CONTROL_KEYS = {'base', 'base_all_pass', 'ok'} | set(MUTANTS) | {m + '_caught' for m in MUTANTS}
REPLAY_KEYS = {'constrained', 'bijection', 'deaths_equal'}
BINDING_KEYS = {'label_lanes', 'label_lanes_equal', 'pos_A_40', 'pos_A_40_equal'}


def table_domains(tab, rd, W, n, P_A, P_B, s, sq, tag):
    """The domain of every cell and reading float of one table; None or the first failure."""
    isint = lambda x: type(x) is int
    N = 1 << n; s0 = N * sq - s * s
    for o in ORIENTS:
        rows = tab[o]
        for k, r in enumerate(rows):
            if not all(isint(x) and x >= 0 for i, x in enumerate(r) if not (i in (2, 5) and x is None)): return 'domains: W=%d %s%s k=%d' % (W, o, tag, k)
            for P, (mx, e, b) in ((P_A, r[0:3]), (P_B, r[3:6])):
                if mx > (1 << k) or e > min(P, N - P) or ((b is None) != (P in (0, N))) or (b is not None and b > P * (N - P)):
                    return 'domains: W=%d %s%s k=%d' % (W, o, tag, k)
            if r[7] > (1 << k) or r[6] > s0 * (N >> k) // N: return 'domains: W=%d %s%s k=%d' % (W, o, tag, k)
        for k, (fa, fb, r2) in enumerate(rd[o]):
            if not all(x is None or (type(x) is float and math.isfinite(x) and -TOL <= x <= 1 + TOL) for x in (fa, fb, r2)):
                return 'domains: reading W=%d%s' % (W, tag)
    return None


def table_arithmetic(tab, rd, W, n, P_A, P_B, s, sq, nvals, tag):
    """Endpoints and orientation agreement at k = 0 and k = n, each row's zero equivalences, monotonicity and the display floats of one
    table; None or the first failure."""
    N = 1 << n; s0 = N * sq - s * s
    k0 = [int(0 < P_A < N), min(P_A, N - P_A), None if P_A in (0, N) else P_A * (N - P_A),
          int(0 < P_B < N), min(P_B, N - P_B), None if P_B in (0, N) else P_B * (N - P_B), s0, int(nvals > 1)]
    kn = [0, 0, None if P_A in (0, N) else 0, 0, 0, None if P_B in (0, N) else 0, 0, 0]
    for o in ORIENTS:
        if not same(tab[o][0], k0): return 'arithmetic: W=%d %s%s k=0 endpoint' % (W, o, tag)
        if not same(tab[o][n], kn): return 'arithmetic: W=%d %s%s k=n not zero' % (W, o, tag)
    for o in ORIENTS:
        for k, r in enumerate(tab[o]):
            if ((r[0] == 0) != (r[1] == 0) or (r[2] is not None and (r[1] == 0) != (r[2] == 0)) or (r[3] == 0) != (r[4] == 0)
                    or (r[5] is not None and (r[4] == 0) != (r[5] == 0)) or (r[7] == 0) != (r[6] == 0)):
                return 'arithmetic: W=%d %s%s k=%d zero equivalence' % (W, o, tag, k)
    for o in ORIENTS:
        for k in range(n):
            a, b = tab[o][k], tab[o][k + 1]
            if (b[0] > 2 * a[0] or b[1] > a[1] or (b[2] or 0) > (a[2] or 0) or b[3] > 2 * a[3] or b[4] > a[4] or (b[5] or 0) > (a[5] or 0)
                    or 2 * b[6] > a[6] or b[7] > 2 * a[7]):
                return 'arithmetic: W=%d %s%s not monotone' % (W, o, tag)
    if not same(reading(tab, P_A, P_B, n), rd): return 'arithmetic: reading W=%d%s' % (W, tag)
    return None


def control_problem(c, gc):
    """Types and keys of every control report (None or the failure); the roll-ups are recomputed in completion."""
    if not all(isinstance(c.get(k), dict) for k in ('base',) + MUTANTS): return 'types: control reports'
    if not all(set(c[k]) == set(BASE_KEYS) and all(type(v) is bool for v in c[k].values()) for k in ('base',) + MUTANTS):
        return 'types: control reports'
    if not all(type(c.get(k)) is bool for k in ('base_all_pass', 'ok') + tuple(m + '_caught' for m in MUTANTS)): return 'types: control roll-ups'
    if set(gc) != set(GATE_KEYS) or not all(type(v) is bool for v in gc.values()): return 'types: gate controls'
    return None


def validate_result(d, src_sha, ex):
    """One explicit schema (GC1813), in order: types, exact key sets, domains, input bindings, arithmetic, completion; every comparison
    type-strict (GC1870). Returns the first failed obligation as a string, or None."""
    isint = lambda x: type(x) is int
    # 1. types
    if not isinstance(d, dict): return 'types: result not an object'
    for k, typ in (('started', str), ('this_sha256', str), ('controls', dict), ('gate_controls', dict), ('inputs', dict), ('widths', dict),
                   ('replay', dict), ('bindings', dict), ('finished', str), ('complete', bool)):
        if type(d.get(k)) is not typ: return 'types: %s' % k
    if type(d.get('elapsed_s')) not in (int, float) or not math.isfinite(d['elapsed_s']) or d['elapsed_s'] < 0: return 'types: elapsed_s'
    if set(d['controls']) != CONTROL_KEYS: return 'keys: controls'
    p = control_problem(d['controls'], d['gate_controls'])
    if p: return p
    for W in ex['widths']:
        w = d['widths'].get(str(W))
        if not isinstance(w, dict): return 'keys: widths'
        for k, typ in (('hist', dict), ('table', dict), ('reading', dict), ('perm_table', dict), ('perm_reading', dict), ('perm_sha256', str)):
            if type(w.get(k)) is not typ: return 'types: W=%d %s' % (W, k)
        for k in ('n', 'N', 'P_A', 'P_B', 'dstar', 'sum', 'sq'):
            if not isint(w.get(k)): return 'types: W=%d %s' % (W, k)
    for W in ex['replay']:
        r = d['replay'].get(str(W))
        if not (isinstance(r, dict) and set(r) == REPLAY_KEYS and isint(r['constrained']) and type(r['bijection']) is bool
                and type(r['deaths_equal']) is bool):
            return 'types: replay W=%d' % W
    b = d['bindings']
    if not (set(b) == BINDING_KEYS and isinstance(b['label_lanes'], dict) and all(isinstance(k, str) and isint(v) for k, v in b['label_lanes'].items())
            and type(b['label_lanes_equal']) is bool and isint(b['pos_A_40']) and type(b['pos_A_40_equal']) is bool):
        return 'types: bindings'
    i = d['inputs']
    if not (set(i) == {'manifest_v2', 'file_audit', 'label_check', 'arrays'} and all(type(i[k]) is str for k in ('manifest_v2', 'file_audit', 'label_check'))
            and isinstance(i['arrays'], dict) and all(type(v) is str for v in i['arrays'].values())):
        return 'types: inputs'
    # 2. exact key sets
    if set(d) != TOP_KEYS: return 'keys: top level %s' % sorted(set(d) ^ TOP_KEYS)
    if set(d['widths']) != {str(W) for W in ex['widths']}: return 'keys: widths'
    if set(d['replay']) != {str(W) for W in ex['replay']}: return 'keys: replay'
    if set(d['inputs']['arrays']) != {str(W) for W in ex['widths']}: return 'keys: inputs'
    for W in ex['widths']:
        w = d['widths'][str(W)]; n = W // 2
        if set(w) != WIDTH_KEYS: return 'keys: W=%d' % W
        for sec in ('table', 'perm_table', 'reading', 'perm_reading'):
            if set(w[sec]) != set(ORIENTS): return 'keys: W=%d %s' % (W, sec)
            for o in ORIENTS:
                rows = w[sec][o]; width = 8 if 'table' in sec else 3
                if not isinstance(rows, list) or len(rows) != n + 1 or not all(isinstance(r, list) and len(r) == width for r in rows):
                    return 'keys: table rows W=%d %s' % (W, o)
    # 3. domains
    for W in ex['widths']:
        w = d['widths'][str(W)]; n = W // 2; N = 1 << n
        if w['n'] != n or w['N'] != N: return 'domains: W=%d n, N' % W
        h = w['hist']
        if not all(k.isdigit() and isint(v) and v > 0 and int(k) % 2 == 0 and W <= int(k) <= 4 * W for k, v in h.items()) or sum(h.values()) != N:
            return 'domains: W=%d histogram' % W
        if not (0 <= w['P_A'] <= N and 0 <= w['P_B'] <= N and w['dstar'] % 2 == 0 and W <= w['dstar'] <= 4 * W + 2):
            return 'domains: W=%d labels' % W
        if not HEX64.fullmatch(w['perm_sha256']): return 'domains: W=%d permutation digest' % W
        for tab, rd, tag in ((w['table'], w['reading'], ''), (w['perm_table'], w['perm_reading'], ' permuted')):
            p = table_domains(tab, rd, W, n, w['P_A'], w['P_B'], w['sum'], w['sq'], tag)
            if p: return p
    # 4. input bindings
    if not same(d['inputs'], {**ex['inputs'], 'arrays': {str(W): ex['sha'][W] for W in ex['widths']}}):
        bad = [W for W in ex['widths'] if d['inputs']['arrays'].get(str(W)) != ex['sha'][W]]
        return 'bindings: array sha256 W=%d' % bad[0] if bad else 'bindings: input digests'
    for W in ex['widths']:
        w = d['widths'][str(W)]; h = {int(k): v for k, v in w['hist'].items()}; a = ex['audit'][W]; N = 1 << (W // 2)
        if w['perm_sha256'] != ex['perm'][W]: return 'bindings: permutation digest W=%d' % W
        if not same(w['hist'], a['histogram']) or a['censored'] != 0 or a['lanes'] != N: return 'bindings: histogram W=%d' % W
        if max(h) != a['D'] or h[max(h)] != a['maximizers'] or min(h) != a['minimum']: return 'bindings: histogram W=%d' % W
        if w['P_A'] != sum(v for k, v in h.items() if k > 3 * W // 2): return 'bindings: P_A W=%d' % W
        dstar = min(d0 for d0 in range(W, 4 * W + 3, 2) if sum(v for k, v in h.items() if k >= d0) <= N // 10)
        if w['dstar'] != dstar or w['P_B'] != sum(v for k, v in h.items() if k >= dstar): return 'bindings: P_B W=%d' % W
        if w['sum'] != sum(k * v for k, v in h.items()) or w['sq'] != sum(k * k * v for k, v in h.items()): return 'bindings: moments W=%d' % W
    if ex['label_lanes'] is not None and (not same(b['label_lanes'], ex['label_lanes']) or b['label_lanes_equal'] is not True): return 'bindings: label lanes'
    if ex['pos_A_40'] is not None and (b['pos_A_40'] != ex['pos_A_40'] or b['pos_A_40_equal'] is not True): return 'bindings: P_A at W = 40'
    # 5. arithmetic
    for W in ex['widths']:
        w = d['widths'][str(W)]; n = W // 2; nv = len(w['hist'])
        for tab, rd, tag in ((w['table'], w['reading'], ''), (w['perm_table'], w['perm_reading'], ' permuted')):
            p = table_arithmetic(tab, rd, W, n, w['P_A'], w['P_B'], w['sum'], w['sq'], nv, tag)
            if p: return p
    # 6. completion: the roll-ups recomputed from the details, then required
    for W in ex['replay']:
        r = d['replay'][str(W)]
        if r['constrained'] != 1 << (W // 2) or r['bijection'] is not True or r['deaths_equal'] is not True: return 'completion: replay W=%d' % W
    c = d['controls']
    base_all = all(c['base'].values()); caught = {m: not all(c[m].values()) for m in MUTANTS}; ok = base_all and all(caught.values())
    if c['base_all_pass'] is not base_all or c['ok'] is not ok or any(c[m + '_caught'] is not caught[m] for m in MUTANTS): return 'completion: control roll-ups'
    if not ok: return 'completion: controls'
    if not all(v is True for v in d['gate_controls'].values()): return 'completion: gate controls'
    if d['this_sha256'] != src_sha: return 'completion: source digest'
    if d['complete'] is not True: return 'completion: complete flag'
    return None


def make_matcher(result_path, src_sha, ex):
    """The final gate: bounded bytes, strict reading, then validate_result, inside one fail-closed boundary."""
    def matcher(rc, text):
        try:
            with open(result_path, 'rb') as f:
                raw = f.read(MAX_RESULT_BYTES + 1)
            if len(raw) > MAX_RESULT_BYTES: return 'FAIL', 'result exceeds the byte bound'
            try:
                d = strict_loads(raw)
            except ValueError:
                return 'FAIL', PARSE_FAIL
            prob = validate_result(d, src_sha, ex)
            if rc != 0 or prob: return 'FAIL', 'rc %s: %s' % (rc, prob)
            return 'pass', 'death information-loss tables complete, every binding held; result sha256 %s' % hashlib.sha256(raw).hexdigest()
        except Exception as e:
            return 'FAIL', 'validator exception (fail closed): %r' % e
    return matcher


def synthetic():
    """A valid full packet from a replay-generated table at W = 4 and HAND_8 at W = 8, and its expectations."""
    import numpy as np
    tabs = {4: replay_table(4), 8: np.array(HAND_8, dtype=np.int64)}
    shas = {W: hashlib.sha256(tabs[W].astype('<u2').tobytes()).hexdigest() for W in SYNTH_WIDTHS}
    perms = {W: perm_digest(perm_of(W, 1 << (W // 2))) for W in SYNTH_WIDTHS}
    audit = {}
    for W in SYNTH_WIDTHS:
        h = hist(tabs[W]); hi = {int(k): v for k, v in h.items()}
        audit[W] = {'histogram': h, 'censored': 0, 'lanes': 1 << (W // 2), 'D': max(hi), 'maximizers': hi[max(hi)], 'minimum': min(hi)}
    ins = {'manifest_v2': 'M', 'file_audit': 'F', 'label_check': 'L'}
    ex = {'widths': SYNTH_WIDTHS, 'replay': (4,), 'sha': shas, 'perm': perms, 'audit': audit, 'inputs': ins, 'label_lanes': None, 'pos_A_40': None}
    base = {k: True for k in BASE_KEYS}; mut = dict(base); mut[BASE_KEYS[0]] = False
    good = {'started': 's', 'this_sha256': 'S', 'finished': 'f', 'complete': True, 'elapsed_s': 0.1,
            'controls': {'base': base, 'base_all_pass': True, 'ok': True, **{m: dict(mut) for m in MUTANTS}, **{m + '_caught': True for m in MUTANTS}},
            'gate_controls': {k: True for k in GATE_KEYS}, 'inputs': {**ins, 'arrays': {str(W): shas[W] for W in SYNTH_WIDTHS}},
            'widths': {str(W): assemble_width(W, tabs[W], perms[W]) for W in SYNTH_WIDTHS},
            'replay': {'4': replay_check(4, tabs[4])},
            'bindings': {'label_lanes': {}, 'label_lanes_equal': False, 'pos_A_40': 0, 'pos_A_40_equal': False}}
    return json.loads(json.dumps(good, allow_nan=False)), ex


def gate_fixtures():
    """(name, kind, mutation, expected diagnostic or None for a pass): 'file' goes through the JSON file and the matcher; 'memory' calls
    validate_result on the in-memory packet (non-JSON values such as NaN); 'text' edits the JSON text and expects the strict-reading
    refusal. The cases marked GC1870 are GPT's nine literal JSON cases (revision 1 passed seven of them)."""
    nan = float('nan')
    def put(path, val):
        def f(d):
            x = d
            for p in path[:-1]: x = x[p]
            x[path[-1]] = val
        return f
    def raise_row(W, o, k, i, delta, sec='table'):
        def f(d): d['widths'][str(W)][sec][o][k][i] += delta
        return f
    def mono(d):
        t = d['widths']['8']['table']['late']; t[3][2] = t[1][2]    # balanced error 44 at k = 2 rises to 60 at k = 3
    def honest_base_failure(d):
        c = d['controls']; c['base'][BASE_KEYS[1]] = False; c['base_all_pass'] = False; c['ok'] = False
    return [
        ('good_full_packet_passes', 'file', lambda d: None, None),
        ('gc1870_base_false_rollup_true', 'file', put(['controls', 'base', BASE_KEYS[0]], False), 'completion: control roll-ups'),
        ('gc1870_base_detail_null', 'file', put(['controls', 'base'], None), 'types: control reports'),
        ('gc1870_mutant_all_pass_caught_true', 'file', lambda d: d['controls'].__setitem__('orient', {k: True for k in BASE_KEYS}), 'completion: control roll-ups'),
        ('gc1870_permutation_digest_empty', 'file', put(['widths', '8', 'perm_sha256'], ''), 'domains: W=8 permutation digest'),
        ('gc1870_permutation_digest_wrong_64hex', 'file', put(['widths', '8', 'perm_sha256'], '0' * 64), 'bindings: permutation digest W=8'),
        ('gc1870_replay_integer_truth', 'file', lambda d: d['replay']['4'].update(bijection=1, deaths_equal=1), 'types: replay W=4'),
        ('gc1870_dmixed_zero_positive_ssw', 'file', put(['widths', '8', 'table', 'early', 3, 7], 0), 'arithmetic: W=8 early k=3 zero equivalence'),
        ('gc1870_complete_false', 'file', put(['complete'], False), 'completion: complete flag'),
        ('controls_honest_base_failure', 'file', honest_base_failure, 'completion: controls'),
        ('controls_base_extra_key', 'file', put(['controls', 'base', 'extra'], True), 'types: control reports'),
        ('controls_rollup_integer', 'file', put(['controls', 'ok'], 1), 'types: control roll-ups'),
        ('gate_controls_integer', 'file', put(['gate_controls', 'good_full_packet_passes'], 1), 'types: gate controls'),
        ('permuted_mixed_zero_positive_error', 'file', put(['widths', '8', 'perm_table', 'late', 1, 0], 0), 'arithmetic: W=8 late permuted k=1 zero equivalence'),
        ('bindings_flag_integer', 'file', put(['bindings', 'pos_A_40_equal'], 0), 'types: bindings'),
        ('types_widths_null', 'file', put(['widths'], None), 'types: widths'),
        ('types_controls_list', 'file', put(['controls'], []), 'types: controls'),
        ('types_elapsed_negative', 'file', put(['elapsed_s'], -1), 'types: elapsed_s'),
        ('types_width_table_list', 'file', put(['widths', '4', 'table'], []), 'types: W=4 table'),
        ('keys_extra_top', 'file', put(['extra'], 1), "keys: top level ['extra']"),
        ('keys_width_missing', 'file', lambda d: d['widths'].pop('8'), 'keys: widths'),
        ('keys_short_table', 'file', lambda d: d['widths']['8']['table']['early'].pop(), 'keys: table rows W=8 early'),
        ('domains_histogram_sum', 'file', put(['widths', '4', 'hist', '4'], 99), 'domains: W=4 histogram'),
        ('domains_negative_cell', 'file', raise_row(4, 'early', 1, 1, -100), 'domains: W=4 early k=1'),
        ('domains_reading_nan_memory', 'memory', lambda d: d['widths']['4']['reading']['late'].__setitem__(0, [nan, nan, nan]), 'domains: reading W=4'),
        ('bindings_array_sha', 'file', put(['inputs', 'arrays', '4'], '0' * 64), 'bindings: array sha256 W=4'),
        ('bindings_input_digest', 'file', put(['inputs', 'manifest_v2'], 'X'), 'bindings: input digests'),
        ('bindings_P_A', 'file', lambda d: d['widths']['8'].__setitem__('P_A', d['widths']['8']['P_A'] + 1), 'bindings: P_A W=8'),
        ('bindings_moments', 'file', lambda d: d['widths']['8'].__setitem__('sq', d['widths']['8']['sq'] + 2), 'bindings: moments W=8'),
        ('arithmetic_endpoint_k0', 'file', raise_row(8, 'early', 0, 6, -1), 'arithmetic: W=8 early k=0 endpoint'),
        ('arithmetic_kn_not_zero', 'file', raise_row(8, 'late', 4, 7, 1), 'arithmetic: W=8 late k=n not zero'),
        ('arithmetic_not_monotone', 'file', mono, 'arithmetic: W=8 late not monotone'),
        ('arithmetic_reading_off', 'file', lambda d: d['widths']['8']['reading']['early'][1].__setitem__(2, 0.123456), 'arithmetic: reading W=8'),
        ('arithmetic_permuted_endpoint', 'file', raise_row(8, 'late', 0, 6, -1, 'perm_table'), 'arithmetic: W=8 late permuted k=0 endpoint'),
        ('completion_replay', 'file', put(['replay', '4', 'bijection'], False), 'completion: replay W=4'),
        ('completion_source', 'file', put(['this_sha256'], 'T'), 'completion: source digest'),
        ('parse_nan_text', 'text', lambda s: s.replace('"elapsed_s": 0.1', '"elapsed_s": NaN'), PARSE_FAIL),
    ]


GATE_KEYS = tuple(f[0] for f in gate_fixtures())


def gate_controls():
    """Every fixture must produce EXACTLY its stated diagnostic, and the positive one a pass."""
    import copy
    good, ex = synthetic(); res = {}
    with tempfile.TemporaryDirectory() as t:
        rp = os.path.join(t, 'r.json'); m = make_matcher(rp, 'S', ex)
        for name, kind, f, want in gate_fixtures():
            bad = copy.deepcopy(good)
            if kind == 'memory':
                f(bad); res[name] = validate_result(bad, 'S', ex) == want; continue
            if kind == 'text':
                open(rp, 'w').write(f(json.dumps(bad, allow_nan=False)))
            else:
                f(bad); json.dump(bad, open(rp, 'w'), allow_nan=False)
            verdict, note = m(0, '')
            res[name] = (verdict == 'pass') if want is None else (verdict == 'FAIL' and note == (want if kind == 'text' else 'rc 0: ' + want))
    assert set(res) == set(GATE_KEYS) and len(res) == len(GATE_KEYS)
    return res


def all_controls():
    report = control_report(); report['gate_controls'] = gate_controls(); ok = report['ok'] and all(report['gate_controls'].values())
    print(json.dumps(report, indent=1)); print('DEATH INFO-LOSS CONTROLS', 'PASS' if ok else 'FAIL'); return ok


def stage(out, indir):
    import w1a_harness as H
    if sha(H.__file__) != W1A_SHA256:
        print('REFUSED: W1A is not the pinned bytes'); return 3
    if not os.path.isabs(out) or (os.path.exists(out) and os.listdir(out)) or not os.path.isabs(indir):
        print('REFUSED: OUT must be absolute and new or empty; INDIR absolute'); return 3
    os.makedirs(out, exist_ok=True)
    src_sha = sha(os.path.abspath(__file__))
    caps = {'stage_s': STAGE_S, 'step_wall_s': STAGE_S, 'step_cpu_s': STAGE_S, 'group_rss_stop_bytes': 2 << 30, 'artifacts_max_bytes': 10 << 20,
            'log_max_bytes': 5 << 20}
    H.CAPS['stage_s'] = STAGE_S; H.CAPS['rss_stop_bytes'] = 2 << 30; H.CAPS['artifacts_max_bytes'] = 10 << 20; H.CAPS['log_max_bytes'] = 5 << 20
    sup = H.Supervisor(out, out); Rc = sup.receipts
    Rc['death_info_loss'] = {'this_sha256': src_sha, 'w1a_sha256': W1A_SHA256, 'widths': list(STAGE_WIDTHS), 'sealed': list(SEALED_WIDTHS), 'caps': caps}
    sup.save()
    if H.pressure_bad(sup.baseline):
        Rc['stopped'] = 'pressure at launch'; sup.save(); print('STOP: pressure'); return 1
    r = sup.register(H.preflight())
    if r['verdict'] != 'pass':
        Rc['stopped'] = 'preflight'; sup.save(); print('STOP: preflight'); return 1
    try:
        audit = {f['W']: f for f in verified_json(os.path.join(indir, 'file-audit.json'), FILE_AUDIT_SHA256)['files']}
    except SystemExit as e:
        Rc['stopped'] = str(e); sup.save(); print('STOP:', e); return 1
    rdir = os.path.join(out, 'run')
    matcher = make_matcher(os.path.join(rdir, 'death_info_loss_result.json'), src_sha, expect_real(audit))
    rec = sup.run_step('death_info_loss', [sys.executable, os.path.abspath(__file__), 'run', rdir, indir], out, STAGE_S, STAGE_S, matcher)
    Rc['complete'] = rec['verdict'] == 'pass'; sup.save()
    print('DONE' if Rc['complete'] else 'STOP', rec['verdict'], rec['reason'], rec.get('match_note'))
    return 0 if Rc['complete'] else 1


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--controls']:
        sys.exit(0 if all_controls() else 1)
    if len(a) == 3 and a[0] == 'run':
        R = run(a[1], a[2]); print('DEATH INFO-LOSS RUN', 'COMPLETE' if R['complete'] else 'INCOMPLETE'); sys.exit(0 if R['complete'] else 1)
    if len(a) == 3 and a[0] == 'stage':
        sys.exit(stage(a[1], a[2]))
    print(__doc__); sys.exit(2)
