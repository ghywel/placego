#!/usr/bin/env python3
"""Local's carrying read of GC2748 (independent code; GPT's scripts not imported or run).

Usage: python3 -I local_carry_gc2748.py EVIDENCE_DIR
EVIDENCE_DIR holds four data files extracted from the cited archive cited/gpt/gc2748-lock-widths-row119-20261108.tar.gz
(SHA256 ab3a2791...75b0): gc2746-main/Bseed.bin, gc2746-main/B/scc_xx.jsonl, inputs/gc2724-saved-histories.json and
gc2747-permitted-replay/artifacts/result.json. Only data is read; no code from the archive runs.

Conventions. A window of width W is a natural with bit i = column i + 1 of a right half driven by column 0, which is
black at even ticks; windows are read at odd ticks. The xx model: from an odd tick, columns W + 1 and W + 2 are free
and the double step is computed (BN-13's closure; Rule30SidewaysLocks.winW_dstep proves every actual right half obeys
it). A history row is a natural with bit p - 1 = column p, in the source frame (tick 0 = physical 108, even shift).

Prediction, written before the run (8 November 2026, 18:16 UTC):
A. Lineage. Bseed holds 78 distinct windows below 2^40, least 5522065728. In the xx model at W = 40 their induced
   graph is one strongly connected component with 112 edges and phase gcd 21; the column-1 bit is constant on phase
   classes and the 21-letter word has primitive period 7, a rotation of 0101000; 30 moves leave the set. Lift and peel
   with no window deleted for being a target: cores of 78, 77, 29, 0 windows at W = 41..44, each nonempty core one SCC
   with 101, 98, 36 edges, least windows 5522065728, 5522065728, 30352548404. Every xx move at width W + 1 projects
   to an xx move at width W (all candidate moves at 41..44, plus 20000 random windows per width).
B. Row 119. The five-cell identity f(f(a,b,c), f(b,c,d), f(c,d,e)) = a xor ([b = c] and (d or e)) holds in all 32
   cases for f(l,c,r) = l xor (c or r), l the column nearer the drive. The six saved histories (4482, 4498, 4520,
   4521, 4522, 14429) replay from their roots through all 86 saved rows; row 1 has low seven bits 64; the heads at odd
   ticks 5..45 follow S (the word 253353 used in L1592: black at 7, 17, 23, 29, 39, 45, white otherwise); head 3 is
   black (the older pulse P); col8(10) is white; col8(13) = Q is black; the telescoped parities at seam m = 85 give
   P = 1 and Q = 1. Row 11 cells 6..10 are 11010 (first four), 11011 (4522), 00011 (14429). The four-register
   recurrence reconstructs them from (A,B,C,D) = (x11,10, x11,11, x12,11, x12,12) and the actual row-13 cells
   11, 10, 9, 8, its intermediate values equal row-12 cells 10, 9, 8, 7, and it is an identity on 20000 random rows.
   14429 has register 1100, incoming word 0101, and Q-term at s = 11 (the OR of row-11 cells 7, 8) equal to 0, while
   the other five have that term 1. Our results agree with GPT's result.json field by field.
C. Addendum, written after A and B passed and before C ran (18:17 UTC). 14429's Q terms 01110101 equal those of
   GC2741's P = 0, Q = 1 control root 54421244276371. Prediction: that control has row-11 cells 7, 8 both white and
   reaches Q = 1 by the right-OR branch (a = 0, d or e = 1), so that branch needs no older pulse; the P = 0, Q = 0
   control 52777231658405 has an unequal pair 7/8 and copies a = 0; the P = 1 fixture 57931849600863 copies a = 1
   through an unequal pair. Counterfactual: if the 01 control copies a = 1 instead, right-OR is not shown to be
   pulse-free and the remark is dropped.
Counterfactual: any mismatch means a datum, index or model in GC2748 (or in my reading of it) is off; the carry of
that item stops there.
"""
import json, random, struct, sys
from math import gcd
from pathlib import Path

E = Path(sys.argv[1])
fails = []
def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok: fails.append(name)

# ---------- A. the lineage ----------
def st(e, c): return ((e << 1) | c) ^ (e | (e >> 1))
def succ(w, W):
    m = (1 << W) - 1
    return {st(st(w | (e << W), 0), 1) & m for e in range(4)}

def peel(S, W):
    S = set(S)
    out = {x: succ(x, W) & S for x in S}
    while True:
        inn = {x: 0 for x in S}
        for x in S:
            for y in out[x] & S: inn[y] += 1
        gone = {x for x in S if not inn[x] or not (out[x] & S)}
        if not gone: return S, {x: out[x] & S for x in S}
        S -= gone

def sccs(S, adj):
    rev = {x: set() for x in S}
    for x in S:
        for y in adj[x]: rev[y].add(x)
    def reach(x, g):
        seen = {x}; todo = [x]
        while todo:
            u = todo.pop()
            for v in g[u]:
                if v not in seen: seen.add(v); todo.append(v)
        return seen
    left = set(S); comps = []
    while left:
        x = min(left); c = reach(x, adj) & reach(x, rev); comps.append(c); left -= c
    return comps

def phase(comp, adj):
    first = min(comp); lab = {first: 0}; todo = [first]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v in comp and v not in lab: lab[v] = lab[u] + 1; todo.append(v)
    g = 0
    for u in comp:
        for v in adj[u]:
            if v in comp: g = gcd(g, lab[u] + 1 - lab[v])
    word = {}; consistent = True
    for u, l in lab.items():
        if word.setdefault(l % g, u & 1) != (u & 1): consistent = False
    wd = ''.join(str(word[k]) for k in range(g))
    prim = next(p for p in range(1, g + 1) if g % p == 0 and wd == wd[:p] * (g // p))
    return g, wd, consistent, prim, wd[:prim]

def rotations(s): return {s[k:] + s[:k] for k in range(len(s))}

data = (E / 'gc2746-main/Bseed.bin').read_bytes()
seed = list(struct.unpack('<' + 'Q' * (len(data) // 8), data))
check('Bseed: 78 distinct windows below 2^40, least 5522065728',
      len(seed) == 78 and len(set(seed)) == 78 and max(seed) < 1 << 40 and min(seed) == 5522065728)
core, adj = peel(seed, 40)
comps = sccs(core, adj)
nedges = sum(len(adj[x]) for x in core)
g, wd, cons, prim, pw = phase(core, adj)
leaks = sum(1 for x in seed for y in succ(x, 40) if y not in set(seed))
print(f'W40: core {len(core)}, SCCs {len(comps)}, edges {nedges}, gcd {g}, word {wd}, consistent {cons}, '
      f'primitive {prim} {pw}, leaking moves {leaks}')
check('W40 parent: one SCC of 78, 112 edges, gcd 21, primitive word a rotation of 0101000, 30 leaks',
      len(core) == 78 and len(comps) == 1 and nedges == 112 and g == 21 and cons and prim == 7
      and pw in rotations('0101000') and leaks == 30)
pred = {41: (78, 101, 5522065728), 42: (77, 98, 5522065728), 43: (29, 36, 30352548404), 44: (0, 0, None)}
sizes = {40: len(core)}
rng = random.Random(2748)
proj_ok = True; proj_n = 0
for W in range(41, 45):
    cand = {x | (b << (W - 1)) for x in core for b in (0, 1)}
    # projection lemma on every candidate and on random windows
    for x in list(cand) + [rng.getrandbits(W) for _ in range(20000)]:
        lo = succ(x & ((1 << (W - 1)) - 1), W - 1)
        for y in succ(x, W):
            proj_n += 1
            if y & ((1 << (W - 1)) - 1) not in lo: proj_ok = False
    core, adj = peel(cand, W)
    sizes[W] = len(core)
    if core:
        comps = sccs(core, adj); nedges = sum(len(adj[x]) for x in core)
        g, wd, cons, prim, pw = phase(core, adj)
        print(f'W{W}: candidates {len(cand)}, core {len(core)}, SCCs {len(comps)}, edges {nedges}, least {min(core)}, '
              f'gcd {g}, primitive {prim} {pw}, consistent {cons}')
        n, e, lst = pred[W]
        check(f'W{W}: core {n}, one SCC, {e} edges, least {lst}, primitive period 7',
              len(core) == n and len(comps) == 1 and nedges == e and min(core) == lst and prim == 7
              and pw in rotations('0101000'))
    else:
        print(f'W{W}: candidates {len(cand)}, core empty')
        check(f'W{W}: core empty', pred[W][0] == 0)
check(f'projection lemma: {proj_n} moves at widths 41..44 all project to moves', proj_ok)
gpt_rows = [json.loads(l) for l in (E / 'gc2746-main/B/scc_xx.jsonl').read_text().splitlines()]
gpt_sizes = {r['W']: r['nodes'] for r in gpt_rows if r['stage'] == 'CORE'}
check(f'core sizes {sizes} agree with GPT C rows {gpt_sizes} (absent width = empty)',
      all(sizes[W] == gpt_sizes.get(W, 0) for W in range(40, 45)))

# ---------- B. row 119 ----------
f = lambda l, c, r: l ^ (c | r)
check('five-cell identity, 32 cases', all(
    f(f(a, b, c), f(b, c, d), f(c, d, e)) == a ^ (int(b == c) & (d | e))
    for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1) for e in (0, 1)))

def step(x, t): return ((x << 1) | (1 if t % 2 == 0 else 0)) ^ (x | (x >> 1))
def cell(rows, t, p): return (1 if t % 2 == 0 else 0) if p == 0 else (rows[t] >> (p - 1)) & 1
WORD = {}
s, ones = 0, {0}
for ch in '253353': s += int(ch); ones.add(s)
for k in range(s + 1): WORD[3 + 2 * k] = int(k in ones)

def register(state, incoming):
    A, B, C, D = state; lowers = []; uppers = []
    for r in incoming:
        up = r ^ (C | D); lo = up ^ (A | B)
        uppers.append(up); lowers.append(lo)
        A, B, C, D = lo, A, up, C
    return lowers, uppers

# the recurrence as an identity on random rows (any rows obeying the rule, interior columns)
ok_id = True
for _ in range(20000):
    r0 = rng.getrandbits(40); r1 = step(r0, 1); r2 = step(r1, 0)
    rows = {11: r0, 12: r1, 13: r2}
    c = lambda t, p: (rows[t] >> (p - 1)) & 1
    lowers, uppers = register([c(11, 10), c(11, 11), c(12, 11), c(12, 12)], [c(13, j) for j in (11, 10, 9, 8)])
    if lowers != [c(11, j) for j in (9, 8, 7, 6)] or uppers != [c(12, j) for j in (10, 9, 8, 7)]: ok_id = False
check('four-register recurrence is an identity on 20000 random rows', ok_id)

hist = json.loads((E / 'inputs/gc2724-saved-histories.json').read_text())
cases = [r for r in hist if r['answer'] is True]
check('six positive histories with the stated labels',
      sorted(r['word'] for r in cases) == [4482, 4498, 4520, 4521, 4522, 14429])
gpt_res = {r['word']: r for r in json.loads((E / 'gc2747-permitted-replay/artifacts/result.json').read_text())
           ['saved_histories']}
m = 85
PRED_WIN = {4482: '11010', 4498: '11010', 4520: '11010', 4521: '11010', 4522: '11011', 14429: '00011'}
for r in sorted(cases, key=lambda r: r['word']):
    w = r['word']; root = int(r['witness']['root'])
    saved = [int(x, 16) for x in r['witness']['rows_hex']]
    rows = [root]
    for t in range(len(saved) - 1): rows.append(step(rows[-1], t))
    z = lambda s_, j: cell(rows, s_, j - m + s_)
    P = sum(z(s_, 84) | z(s_, 85) for s_ in range(3, 10)) % 2
    Qt = [z(s_, 81) | z(s_, 82) for s_ in range(5, 13)]
    Q = sum(Qt) % 2
    win = [cell(rows, 11, p) for p in range(6, 11)]
    state = [cell(rows, 11, 10), cell(rows, 11, 11), cell(rows, 12, 11), cell(rows, 12, 12)]
    inc = [cell(rows, 13, j) for j in (11, 10, 9, 8)]
    lowers, uppers = register(state, inc)
    a, b, c_, d, e = win
    mech = 'left copy' if b != c_ else 'right OR'
    print(f'{w}: rows {len(saved)}, row1&127 {rows[1] & 127}, S heads {all(cell(rows, t, 1) == v for t, v in WORD.items() if t != 3)}, '
          f'P {cell(rows, 3, 1)}/{P}, col8(10) {cell(rows, 10, 8)}, Q {cell(rows, 13, 8)}/{Q}, Q terms {"".join(map(str, Qt))}, '
          f'row11 cells6..10 {"".join(map(str, win))}, register {"".join(map(str, state))}, incoming {"".join(map(str, inc))}, '
          f'mechanism {mech}, row11&127 {rows[11] & 127}')
    g_ = gpt_res[w]
    check(f'{w}: replay, S, P = Q = 1, white col8(10), window {PRED_WIN[w]}, register, gate, s=11 term, GPT fields',
          rows == saved and len(saved) == 86 and rows[1] & 127 == 64
          and all(cell(rows, t, 1) == v for t, v in WORD.items() if t != 3)
          and cell(rows, 3, 1) == 1 and P == 1 and cell(rows, 10, 8) == 0 and cell(rows, 13, 8) == 1 and Q == 1
          and ''.join(map(str, win)) == PRED_WIN[w]
          and lowers == [win[3], win[2], win[1], win[0]] and uppers == [cell(rows, 12, j) for j in (10, 9, 8, 7)]
          and cell(rows, 13, 8) == a ^ (int(b == c_) & (d | e))
          and Qt[6] == (b | c_) and Qt[6] == (0 if w == 14429 else 1)
          and (w != 14429 or (state == [1, 1, 0, 0] and inc == [0, 1, 0, 1] and str(root) == '77371252455336267063753023'))
          and g_['row11_cells6_to10'] == win and g_['state4'] == state and g_['actual_row13_cells11_10_9_8'] == inc
          and g_['pair_or'] == (b | c_) and g_['older_pulse'] == 1 and g_['later_input'] == 1)
print('ALL PASS' if not fails else f'{len(fails)} FAIL: {fails}')

# ---------- C. the three GC2741 roots on the same gate ----------
for R, pq, pred in ((52777231658405, '00', 'left copy'), (54421244276371, '01', 'right OR'),
                    (57931849600863, '11', 'left copy')):
    rows = [R]
    for t in range(m): rows.append(step(rows[-1], t))
    win = [cell(rows, 11, p) for p in range(6, 11)]
    a, b, c_, d, e = win
    mech = 'left copy' if b != c_ else 'right OR'
    q = cell(rows, 13, 8)
    print(f'root {R} (P,Q) = {pq}: row11 cells6..10 {"".join(map(str, win))}, mechanism {mech}, a {a}, d or e {d | e}, Q {q}')
    check(f'root {R}: mechanism {pred}' + (', b = c = 0, a = 0, d or e = 1' if pq == '01' else ''),
          mech == pred and q == a ^ (int(b == c_) & (d | e)) and q == int(pq[1])
          and (pq != '01' or (b == c_ == 0 and a == 0 and (d | e) == 1)))
print('ALL PASS (with C)' if not fails else f'{len(fails)} FAIL: {fails}')
