#!/usr/bin/env python3
"""Block 9 step 2 (Local): bad-class certificates in the kit's `Cert` format for a period-3 center, with the kit's
checks and the period-3 path check re-implemented here, and Lean output.

Usage: gen_cert3.py WORD B R NAME FORBIDDEN... [--allow ALLOWED...]
  WORD       center word, phases 0..2 (001 or 011)
  B          strip width
  R          reading phase (the free white phase)
  NAME       Lean name prefix for the certificate
  FORBIDDEN  column-1 words read at phase R on consecutive periods, each to be certified absent from the bad class
  ALLOWED    words expected present (positive controls: the bad class has real paths)

The kit's `Cert` (Rule30StripCertificates): node index phi * 2^B + encList s (bit i = column i + 1); 16-bit rank,
8-bit position per node; 8-bit counter period and 64-bit word per rank. `Cert.checkb C bad`: ranks never rise along an
edge; inside a rank other than `bad`, positions advance by `nextPos` and column 1 at white phases equals the rank's
word at the position. `Cert.checkGb`: every node outside `bad` has position below its rank's period. With them,
`Cert.sound_bad` (masked Jen, the seed) puts the seed's strip in the bad class eventually.

Construction: Tarjan SCCs in emission order (sinks first); ranks by longest path to a sink, bumped so that each cyclic
SCC has a rank of its own; each labelled SCC (column 1 at every white phase a function of level mod gcd) gets its
counter; the single unlabelled SCC is the bad class.
"""
import sys
sys.set_int_max_str_digits(0)
from math import gcd

args = [a for a in sys.argv[1:] if a != '--no-lean']
word, B, R, name = args[0], int(args[1]), int(args[2]), args[3]
rest = args[4:]
allow = []
if '--allow' in rest:
    i = rest.index('--allow'); allow = rest[i + 1:]; rest = rest[:i]
forbid = rest
P = len(word); w = [int(c) for c in word]; NS = 1 << B; N = P * NS; MASK = NS - 1
assert P == 3

def step(s, c, x): e = s | (x << B); return (((e << 1) | c) ^ (e | (e >> 1))) & MASK
def succ(i, x): ph, s = divmod(i, NS); return ((ph + 1) % P) * NS + step(s, w[ph], x)

# Tarjan, iterative
index = [-1] * N; low = [0] * N; onst = [False] * N; comp = [-1] * N; stk = []; ncomp = 0; counter = 0
for root in range(N):
    if index[root] != -1: continue
    cs = [(root, 0)]; index[root] = low[root] = counter; counter += 1; stk.append(root); onst[root] = True
    while cs:
        v, e = cs[-1]
        if e < 2:
            cs[-1] = (v, e + 1); u = succ(v, e)
            if index[u] == -1:
                index[u] = low[u] = counter; counter += 1; stk.append(u); onst[u] = True; cs.append((u, 0))
            elif onst[u]: low[v] = min(low[v], index[u])
        else:
            cs.pop()
            if low[v] == index[v]:
                while True:
                    x = stk.pop(); onst[x] = False; comp[x] = ncomp
                    if x == v: break
                ncomp += 1
            if cs: p = cs[-1][0]; low[p] = min(low[p], low[v])
members = [[] for _ in range(ncomp)]
for i in range(N): members[comp[i]].append(i)
cyclic = [len(m) > 1 for m in members]
# labelling
level = {}; info = {}
for c in range(ncomp):
    if not cyclic[c]: continue
    r0 = members[c][0]; lv = {r0: 0}; q = [r0]
    for u in q:
        for x in (0, 1):
            v = succ(u, x)
            if comp[v] == c and v not in lv: lv[v] = lv[u] + 1; q.append(v)
    g = 0
    for u in members[c]:
        for x in (0, 1):
            v = succ(u, x)
            if comp[v] == c: g = gcd(g, lv[u] + 1 - lv[v])
    lab = {}; ok = True
    for u in members[c]:
        ph, s = divmod(u, NS)
        if w[ph]: continue
        k = lv[u] % g
        if lab.setdefault(k, s & 1) != (s & 1): ok = False
    level.update(lv); info[c] = (g, ok, r0)
unl = [c for c in info if not info[c][1]]
assert len(unl) == 1, f'expected one unlabelled SCC, got {len(unl)}'
badc = unl[0]
# ranks: emission order is reverse topological
rank = [0] * ncomp; used = set(); reserved = set()
for c in range(ncomp):
    r = -1
    for u in members[c]:
        for x in (0, 1):
            d = comp[succ(u, x)]
            if d != c: r = max(r, rank[d])
    r += 1
    if cyclic[c]:
        while r in used: r += 1
        reserved.add(r)
    else:
        while r in reserved: r += 1
    rank[c] = r; used.add(r)
bad = rank[badc]
nranks = max(rank) + 1
assert nranks < 65536
per = {}; wordbits = {}; pos = [0] * N
for c, (g, ok, r0) in info.items():
    if c == badc or not ok: continue
    ph0 = r0 // NS
    white = [1 - w[(ph0 + k) % P] for k in range(g)]
    Wc = [0]
    for k in range(g): Wc.append(Wc[-1] + white[k])
    m = Wc[g]
    assert 1 <= m <= 64, m
    for u in members[c]:
        k = level[u] % g; pos[u] = Wc[k] % m
        ph, s = divmod(u, NS)
        if not w[ph]: wordbits[(rank[c], pos[u])] = s & 1
    per[rank[c]] = m
for r in range(nranks): per.setdefault(r, 1)
rankP = sum(rank[comp[i]] << (16 * i) for i in range(N))
posP = sum(pos[i] << (8 * i) for i in range(N))
perP = sum(per[r] << (8 * r) for r in range(nranks))
wordP = sum(1 << (64 * r + p) for (r, p), b in wordbits.items() if b)

# the kit's checks, from the packed data
def rk(ph, s): return (rankP >> (16 * (ph * NS + s))) % 65536
def ps(ph, s): return (posP >> (8 * (ph * NS + s))) % 256
def mm(r): return (perP >> (8 * r)) % 256
def uu(r, p): return (wordP >> (64 * r + p)) % 2 == 1
def wAt(ph): return w[ph] == 1
def nextPos(r, p, ph): return p if wAt(ph) else (p + 1) % mm(r)
def edgeOKb(ph, s, s2):
    ph2 = (ph + 1) % P; r = rk(ph, s)
    return rk(ph2, s2) <= r and ((rk(ph2, s2) != r) or r == bad or
            (ps(ph2, s2) == nextPos(r, ps(ph, s), ph) and (wAt(ph) or ((s & 1) == 1) == uu(r, ps(ph, s)))))
checkb = all(edgeOKb(ph, s, step(s, w[ph], x)) for ph in range(P) for s in range(NS) for x in (0, 1))
checkGb = all(rk(ph, s) == bad or ps(ph, s) < mm(rk(ph, s)) for ph in range(P) for s in range(NS))
def inBad(ph, s): return rk(ph, s) == bad
def occurs3(pat):
    if not pat: return True
    S = {s for s in range(NS) if inBad(R, s) and (s & 1) == pat[0]}
    for y in pat[1:]:
        T = set()
        for s in S:
            for x1 in (0, 1):
                s1 = step(s, w[R], x1)
                if not inBad((R + 1) % 3, s1): continue
                for x2 in (0, 1):
                    s2 = step(s1, w[(R + 1) % 3], x2)
                    if not inBad((R + 2) % 3, s2): continue
                    for x3 in (0, 1):
                        s3 = step(s2, w[(R + 2) % 3], x3)
                        if inBad(R, s3) and (s3 & 1) == y: T.add(s3)
        S = T
    return len(S) > 0
badsize = len(members[badc])
print(f'word {word} B {B} R {R}: nodes {N}, SCCs {ncomp}, cyclic {sum(cyclic)}, labelled {sum(1 for c in info if info[c][1])}, '
      f'bad SCC {badsize} nodes at rank {bad}, nranks {nranks}')
print('checkb', checkb, 'checkGb', checkGb)
res_f = {p: occurs3([int(ch) for ch in p]) for p in forbid}
res_a = {p: occurs3([int(ch) for ch in p]) for p in allow}
print('occurs3 on forbidden words (want False):', res_f)
print('occurs3 on allowed words (want True):', res_a)
ok = checkb and checkGb and not any(res_f.values()) and all(res_a.values())
print('ALL CHECKS', 'PASS' if ok else 'FAIL')
if ok and '--no-lean' not in sys.argv:
    def lb(p): return '[' + ', '.join('true' if ch == '1' else 'false' for ch in p) + ']'
    out = [f'-- bad-class certificate for w = {word}, strip width {B}, reading phase {R} (generated by gen_cert3.py)',
           f'def {name}_rankP : Nat := {rankP}', f'def {name}_posP : Nat := {posP}', f'def {name}_perP : Nat := {perP}',
           f'def {name}_wordP : Nat := {wordP}',
           f'def {name} : Cert where\n  w := {lb(word)}\n  b := {B}\n  nranks := {nranks}\n  rankP := {name}_rankP\n'
           f'  posP := {name}_posP\n  perP := {name}_perP\n  wordP := {name}_wordP',
           f'def {name}_bad : Nat := {bad}',
           f'theorem {name}_checkb : Cert.checkb {name} {name}_bad = true := by decide +kernel',
           f'theorem {name}_checkGb : Cert.checkGb {name} {name}_bad = true := by decide +kernel']
    for p in forbid:
        out.append(f'theorem {name}_occ_{p} : occurs3 {name} {name}_bad {R} {lb(p)} = false := by decide +kernel')
    for p in allow:
        out.append(f'theorem {name}_occ_ctrl_{p} : occurs3 {name} {name}_bad {R} {lb(p)} = true := by decide +kernel')
    open(f'{name}.lean.txt', 'w').write('\n'.join(out) + '\n')
    print(f'wrote {name}.lean.txt ({sum(len(l) for l in out)} chars)')
