#!/usr/bin/env python3
"""Local's carrying read of GC2753 (independent code; GPT's scripts read as text, not imported or run).

Usage: python3 -I local_carry_gc2753.py EVIDENCE_DIR
EVIDENCE_DIR holds data files extracted from cited/gpt/gc2753-row119-ancestry-20261108.tar.gz (SHA256 b4ee30af...0763):
the original 359-tick CNF, the triple and word case CNFs, the RUP prefix, the eight-bit collision record and the saved
full-E histories. Only data is read.

Conventions. Physical tick t, column p >= 1; column 0 is the drive, black at even t. One tick:
x(t+1,p) = x(t,p-1) xor (x(t,p) or x(t,p+1)). Rows as naturals with bit p-1 = column p. The source frame of the 45-tick
cone and of the saved histories is physical minus 108 (even). The cone CNF of height H has root cells 1..H+1 at t = 0,
cells 1..H+1-t at time t (exactly the cells determined by the root, whatever lies beyond it), variable v(t,x) = off[t] + x
with off[0] = 1, off[t+1] = off[t] + (H+1-t), and variable 1 the constant true.

Prediction, written 8 November 2026 19:24 UTC before the run:
A. Dictionary.
   (1) In the original (H = 359) formula: v(119,6..8) = 35826..35828 and v(121,8) = 36309; every cell (t+1,x) with
       x <= 359-t carries clauses whose models over its four variables are exactly y = l xor (c or r), the left input at
       x = 1 being the constant true at even t and false at odd t; the unit clauses on column 1 are exactly the head word
       E A^4 E A^7 E (E = 33535555, A = 25) from tick 1, black at the cumulative positions, white elsewhere, ticks 1..359.
   (2) The triple and word CNFs are the same construction at H = 193 (heads E A^4 E through 193) plus, respectively,
       the three white units at (119, 6..8), and the units row 109 cells 1..7 = 64 with column 8 at ticks 109..119 = the
       bits of 93, least significant first. The past heads agree with the original's through 193, and the short common S
       (word 253353 at source 3..45) is the original's heads 111..153 under the shift 108.
   (3) Light cone: on 200 random 360-cell roots, changing cells 195..360 never changes the heads through 193 or row 119
       cells 6..10, and changing cells 130..360 never changes row 119 cells 6..10; changing cell 194 does change head 193
       for some root (the 194 bound is tight).
B. Trunk. The low seven cells obey q' = (((q << 1) | drive) xor (q | q >> 1 | u << 6)) mod 128 with u = column 8 (checked
   on 20000 random rows). From q = 64 at 109 with inputs 93 the trunk is 64 96 49 27 104 44 103 57 78 115 28, so cells
   6, 7 at 119 are white, and the eleventh input makes cell 8 white. Saved history 14429 has row-1 low seven 64, and its
   column-8 word at source ticks 1..14 is 14429 (low eleven bits 93).
C. Collision. Root 55973280461853 (source frame, the 45-tick cone) and the saved 4522 root both satisfy S (heads at
   source 5..45 by 253353), have white col8(10) and Q = col8(13) = 1, P = head 3 = 0 and 1 respectively, register
   (x11,10, x11,11, x12,11, x12,12) = 1001, top word (x13,11..8) = 1111, patch cells 6..10 at 11 = 11011; their seam
   rows at source 85 give bands (cells 80..102, bit 0 = cell 80) 6145448 and 755656.
D. RUP. My own unit-propagation checker accepts all 1045 lemmas of the prefix against the original CNF, the last being
   35826 35827 35828. Against only the original's past clauses (variables of cells t <= 193, x <= 194 - t, and heads
   through 193) it accepts them too, so the clause follows from the past alone.
Counterfactual: a mismatch in A stops the dictionary; in B the class interpretation; in C the collision conclusion; a
rejected lemma in D's first run means my checker or the prefix is wrong (to be settled before any status); acceptance
against the full formula but rejection against the past alone means the clause's scope includes future heads.
"""
import json, random, sys
from pathlib import Path

E = Path(sys.argv[1])
fails = []
def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if not ok: fails.append(name)

def offs(H):
    W = H + 1; off = [1]
    for t in range(H + 1): off.append(off[-1] + W - t)
    return off
def heads(word, start):
    pos, ones = 0, {0}
    for c in word: pos += int(c); ones.add(pos)
    return {start + 2 * s: int(s in ones) for s in range(pos + 1)}
def read_cnf(path):
    cls = []; nv = None
    with open(path) as fh:
        for line in fh:
            if line.startswith('p'): nv = int(line.split()[2]); continue
            if line.startswith('c') or not line.strip(): continue
            lits = list(map(int, line.split()))
            assert lits[-1] == 0; cls.append(lits[:-1])
    return nv, cls
EA = '33535555' + '25' * 4 + '33535555'
FULLW = EA + '25' * 7 + '33535555'

def semantics(cls, H, wanted, label):
    """Group clauses by cell; check each cell's clause set is exactly the Rule 30 gate, and list the remaining units."""
    off = offs(H); W = H + 1
    var_tx = {}
    for t in range(H + 1):
        for x in range(1, W - t + 1): var_tx[off[t] + x] = (t, x)
    out_var = {}
    for t in range(H):
        for x in range(1, W - t): out_var[off[t + 1] + x] = (t, x)
    gate = {}; units = []
    for c in cls:
        vs = {abs(l) for l in c}
        if len(c) == 1 and abs(c[0]) != 1 and not any(abs(l) in out_var and len(vs) > 1 for l in c):
            units.append(c[0]); continue
        if c == [1]: continue
        # the output is the variable of largest time
        o = max((v for v in vs if v != 1), key=lambda v: var_tx[v][0])
        gate.setdefault(o, []).append(c)
    ok = True
    for o, (t, x) in out_var.items():
        l = off[t] + x - 1 if x > 1 else None
        c_, r = off[t] + x, off[t] + x + 1
        cs = gate.get(o, [])
        for lv in (0, 1):
            if l is None and lv != (1 if t % 2 == 0 else 0): continue
            for cv in (0, 1):
                for rv in (0, 1):
                    for yv in (0, 1):
                        val = {1: 1, c_: cv, r: rv, o: yv}
                        if l is not None: val[l] = lv
                        sat = all(any((val[abs(q)] == 1) == (q > 0) for q in cl) for cl in cs)
                        if sat != (yv == lv ^ (cv | rv)): ok = False
    extra = set(gate) - set(out_var)
    check(f'{label}: every cell is the Rule 30 gate with the drive at column 0 ({len(out_var)} cells)', ok and not extra)
    rest = [(var_tx[abs(u)], int(u > 0)) for u in units]
    ok_heads = True
    for t, b in wanted.items():
        if ((t, 1), b) in rest: rest.remove(((t, 1), b))
        else: ok_heads = False
    if any(tx[1] == 1 and tx[0] in wanted for tx, _ in rest if (tx, 1 - wanted.get(tx[0], 0)) in rest): ok_heads = False
    check(f'{label}: column-1 units include exactly the head word through {max(wanted)}', ok_heads)
    return sorted(rest), off

# ---------- A ----------
nv, full = read_cnf(E / 'gc2749-branches/artifacts/full-target-original.cnf')
off359 = offs(359)
check('A1: v(119,6..8) = 35826..35828 and v(121,8) = 36309',
      [off359[119] + p for p in (6, 7, 8)] == [35826, 35827, 35828] and off359[121] + 8 == 36309)
wfull = heads(FULLW, 1)
check('A1: the full head word ends at tick 359', max(wfull) == 359)
other, _ = semantics(full, 359, wfull, 'A1 original')
check('A1: the original has no other units', other == [])
wpast = heads(EA, 1)
check('A2: past heads end at 193 and agree with the original there', max(wpast) == 193 and all(wfull[t] == b for t, b in wpast.items()))
S = heads('253353', 3)
check('A2: S (253353 at source 3..45) is the original heads 111..153 under +108', all(wfull[t + 108] == b for t, b in S.items()))
_, tr = read_cnf(E / 'gc2751-export/artifacts/triple.cnf')
o3, off193 = semantics(tr, 193, wpast, 'A2 triple')
check('A2 triple: extra units are the three whites at (119, 6..8)', o3 == [((119, 6), 0), ((119, 7), 0), ((119, 8), 0)])
_, wd = read_cnf(E / 'gc2751-export/artifacts/word.cnf')
ow, _ = semantics(wd, 193, wpast, 'A2 word')
want_w = sorted([((109, p), (64 >> (p - 1)) & 1) for p in range(1, 8)] + [((109 + k, 8), (93 >> k) & 1) for k in range(11)])
check('A2 word: extra units are row 109 cells 1..7 = 64 and column 8 at 109..119 = bits of 93', ow == want_w)
def evolve(root, n, start_t=0):
    rows = [root]
    for t in range(start_t, start_t + n): x = rows[-1]; rows.append(((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1)))
    return rows
def cellv(rows, t, p, t0=0): return (rows[t - t0] >> (p - 1)) & 1
rng = random.Random(2753)
ok_cone = True; tight = False
for _ in range(200):
    r = rng.getrandbits(360)
    base = evolve(r, 193)
    h = [cellv(base, t, 1) for t in range(1, 194)]; g = [cellv(base, 119, p) for p in range(6, 11)]
    r2 = (r & ((1 << 194) - 1)) | (rng.getrandbits(166) << 194)
    b2 = evolve(r2, 193)
    if [cellv(b2, t, 1) for t in range(1, 194)] != h or [cellv(b2, 119, p) for p in range(6, 11)] != g: ok_cone = False
    r3 = (r & ((1 << 129) - 1)) | (rng.getrandbits(231) << 129)
    if [cellv(evolve(r3, 119), 119, p) for p in range(6, 11)] != g: ok_cone = False
    r4 = r ^ (1 << 193)   # cell 194
    if cellv(evolve(r4, 193), 193, 1) != h[-1]: tight = True
check('A3: cells > 194 never move heads <= 193 or row-119 cells 6..10; cells > 129 never move the patch', ok_cone)
check('A3: cell 194 moves head 193 for some root (tight)', tight)

# ---------- B ----------
def low7(q, d, u): return (((q << 1) | d) ^ (q | (q >> 1) | (u << 6))) & 127
ok_rec = True
for _ in range(20000):
    x = rng.getrandbits(30); t = rng.randrange(2)
    nx = ((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1))
    if nx & 127 != low7(x & 127, 1 if t % 2 == 0 else 0, (x >> 7) & 1): ok_rec = False
check('B: low-seven recurrence equals the true step (20000 random rows)', ok_rec)
q = 64; trunk = [q]
for k in range(10):
    t = 109 + k
    q = low7(q, 1 if t % 2 == 0 else 0, (93 >> k) & 1); trunk.append(q)
print('trunk', trunk)
check('B: trunk 64 96 49 27 104 44 103 57 78 115 28; cells 6, 7 white at 119 and the eleventh input white',
      trunk == [64, 96, 49, 27, 104, 44, 103, 57, 78, 115, 28] and (trunk[-1] >> 5) & 1 == 0 and (trunk[-1] >> 6) & 1 == 0 and (93 >> 10) & 1 == 0)
hist = {r['word']: r for r in json.loads((E / 'inputs/old-full-E-histories.json').read_text()) if r.get('answer') is True}
r14 = hist[14429]['witness']; root14 = int(r14['root']); rows14 = evolve(root14, 85)
col8 = sum(cellv(rows14, t, 8) << (t - 1) for t in range(1, 15))
check('B: saved 14429 replays its rows; row-1 low seven 64; column-8 word at source 1..14 = 14429 (low eleven 93); cells 6..8 white at 11',
      rows14 == [int(h_, 16) for h_ in r14['rows_hex']] and rows14[1] & 127 == 64 and col8 == 14429 and col8 & 2047 == 93
      and [cellv(rows14, 11, p) for p in (6, 7, 8)] == [0, 0, 0])
print('saved labels and their column-8 words:', {w: sum(cellv(evolve(int(hist[w]['witness']['root']), 14), t, 8) << (t - 1) for t in range(1, 15)) for w in sorted(hist)})

# ---------- C ----------
def summary(root):
    rows = evolve(root, 85)
    c = lambda t, p: cellv(rows, t, p)
    return {'S': all(c(t, 1) == b for t, b in S.items() if t != 3), 'P': c(3, 1), 'white10': c(10, 8) == 0, 'Q': c(13, 8),
            'register': [c(11, 10), c(11, 11), c(12, 11), c(12, 12)], 'top': [c(13, j) for j in (11, 10, 9, 8)],
            'patch': [c(11, p) for p in range(6, 11)], 'band': sum(c(85, 80 + i) << i for i in range(23))}
s0 = summary(55973280461853); s1 = summary(int(hist[4522]['witness']['root']))
print('P=0 root:', s0); print('4522 root:', s1)
col = json.loads((E / 'gc2750-continuation/artifacts/eight-bit-collision.json').read_text())
check('C: both satisfy S with white col8(10) and Q = 1; P = 0, 1; same register 1001, top 1111, patch 11011; bands as GPT',
      s0['S'] and s1['S'] and s0['white10'] and s1['white10'] and s0['Q'] == s1['Q'] == 1 and (s0['P'], s1['P']) == (0, 1)
      and s0['register'] == s1['register'] == [1, 0, 0, 1] and s0['top'] == s1['top'] == [1, 1, 1, 1]
      and s0['patch'] == s1['patch'] == [1, 1, 0, 1, 1] and [s0['band'], s1['band']] == col['seam85_band80_to102']
      and col['roots'][1] == hist[4522]['witness']['root'])

# ---------- D ----------
def rup_check(clauses, lemmas, nvars, label):
    val = [0] * (nvars + 1)
    watches = {}
    db = []
    trail = []
    def lit_val(l): v = val[abs(l)]; return v if l > 0 else -v
    def assign(l): val[abs(l)] = 1 if l > 0 else -1; trail.append(l)
    def add(c):
        idx = len(db); db.append(list(c))
        if len(c) >= 2:
            watches.setdefault(c[0], []).append(idx); watches.setdefault(c[1], []).append(idx)
        return idx
    def propagate(start):
        i = start
        while i < len(trail):
            l = trail[i]; i += 1
            fl = -l
            ws = watches.get(fl, [])
            j = 0; keep = []
            while j < len(ws):
                ci = ws[j]; j += 1
                c = db[ci]
                if c[0] == fl: c[0], c[1] = c[1], c[0]
                if lit_val(c[0]) == 1: keep.append(ci); continue
                moved = False
                for k in range(2, len(c)):
                    if lit_val(c[k]) != -1:
                        c[1], c[k] = c[k], c[1]
                        watches.setdefault(c[1], []).append(ci); moved = True; break
                if moved: continue
                keep.append(ci)
                if lit_val(c[0]) == -1:
                    keep.extend(ws[j:]); watches[fl] = keep; return False
                assign(c[0])
            watches[fl] = keep
        return True
    units = []
    for c in clauses:
        c = list(dict.fromkeys(c))
        if len(c) == 1: units.append(c[0])
        else: add(c)
    for u in units:
        if lit_val(u) == -1: print('formula unsat by units'); return False, 0
        if lit_val(u) == 0: assign(u)
    if not propagate(0): print('formula unsat'); return False, 0
    base = len(trail)
    for n, lem in enumerate(lemmas):
        mark = len(trail)
        conflict = False
        for l in lem:
            v = lit_val(l)
            if v == 1: conflict = True; break   # lemma already satisfied by the base: RUP trivially
            if v == 0: assign(-l)
        if not conflict: conflict = not propagate(mark)
        for l in trail[base:]: val[abs(l)] = 0
        del trail[base:]
        if not conflict:
            print(f'{label}: lemma {n + 1} not RUP: {lem[:8]}'); return False, n
        lem = list(dict.fromkeys(lem))
        if len(lem) == 1:
            if lit_val(lem[0]) == 0:
                assign(lem[0])
                if not propagate(base): print(f'{label}: unit lemma {n + 1} conflicts'); return True, n + 1
            base = len(trail)
        else:
            nonfalse = [l for l in lem if lit_val(l) != -1]
            if len(nonfalse) == 1 and lit_val(nonfalse[0]) == 0:
                assign(nonfalse[0]); propagate(base); base = len(trail)
            # watch two literals not false at the base if possible
            lem.sort(key=lambda l: lit_val(l) == -1)
            add(lem)
    return True, len(lemmas)
lem = []
for line in open(E / 'gc2751-export/artifacts/full-prefix.drup'):
    xs = line.split()
    if not xs or xs[0] == 'd': continue
    lem.append([int(v) for v in xs[:-1]])
okD, nD = rup_check(full, lem, nv, 'D full')
check(f'D: all {len(lem)} lemmas RUP against the original; last lemma 35826 35827 35828', okD and nD == len(lem) and lem[-1] == [35826, 35827, 35828] and len(lem) == 1045)
past_vars = {1} | {off359[t] + x for t in range(194) for x in range(1, 195 - t)}
past = [c for c in full if all(abs(l) in past_vars for l in c)]
print('past clauses kept from the original:', len(past))
okP, nP = rup_check(past, lem, nv, 'D past')
check(f'D: all lemmas RUP against the past clauses alone ({len(past)} clauses, GPT: 112424)', okP and nP == len(lem) and len(past) == 112424)
print('ALL PASS' if not fails else f'{len(fails)} FAIL: {fails}')
