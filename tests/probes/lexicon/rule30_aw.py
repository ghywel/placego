#!/usr/bin/env python3
"""rule30_aw.py: AW, are Theorem B's bounds attained by admissible periodic walls? (Local's run, after GPT's GC309;
claimed in CLOUD-LOCAL.md, with these predictions pushed before the script was run.)

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_aw.py
COST:       under a minute expected; caps 600 CPU s, 1 GiB peak RSS.

Question. S106 found that entry 06's odd-run bound 2P - 5 (GPT's GC307 refinement) and the general bound 2P - 2 are
attained at some P, by formal pairs of P-periodic columns 0 and 1. GPT's GC309 notes that such a pair need not come
from an actual configuration: column 1 must have a right continuation. For P-periodic columns that is decidable.
Columns k - 1, k, k + 1 must satisfy x(k, t + 1) = x(k - 1, t) XOR (x(k, t) OR x(k + 1, t)); a pair (u, v) of
P-periodic words is ADMISSIBLE when an infinite chain (u, v), (v, w), (w, z), ... of such P-periodic columns exists
to its right. On the finite graph of pairs this means: some path from (u, v) reaches a cycle. Prune nodes with no
successor until none is removed; the survivors are the admissible pairs. Then rerun S106's census of the forced left
half (inverse rule, 40 columns deep, runs in row 0 bounded by black cells, strictly in x < 0) on admissible pairs only.

PREDICTIONS, Local's, published before the run:
  AW-P1 (blind, uncertain): the odd bound 2P - 5 is attained by an admissible pair for at least one P in 4..7.
  AW-P2 (blind, uncertain): the general bound 2P - 2 is attained by an admissible pair for at least one P in 3..7.
  AW-C1 (control): every pair counted by S106 is either admissible or not, and the admissible census never exceeds the
        formal one (longest admissible runs <= the formal maxima 3, 5, 5, 9 odd at P = 4..7; 4, 6, 4, 6, 6 even at
        P = 3..7).
  AW-C2 (control): GPT's GC309 hand check at P = 2: every admissible pair gives only singleton white runs in row 0, and
        the formal pair tau = 01 (column 0), sigma = 11 (column 1) is not admissible.
  AW-U (the unexpected check): admissibility computed by pruning agrees with an explicit chain of 3P further columns
        for every surviving pair (a constructive witness), and fails to extend for a pruned pair.
OUTCOME, 2026-10-07 16:43 (M5, one run at commit d189991; CPU 0.1 s, peak RSS 20.7 MiB). Pairs with a periodic right
continuation: 3 of 16 at P = 2, 15/64, 31/256, 48/1,024, 99/4,096, 108/16,384 at P = 3..7. Longest bounded row-0 runs
on those pairs: P = 2 odd 1; P = 3 even 4, odd 1; P = 4 even 6, odd 1; P = 5 odd 5, even 2; P = 6 odd 5, even 4;
P = 7 odd 5, even 6. AW-P1 HELD: 2P - 5 is attained at P = 5 (odd 5). AW-P2 HELD: 2P - 2 is attained at P = 3 (4)
and P = 4 (6). AW-C1 PASS (never above the formal maxima). AW-C2 PASS (P = 2: singletons only; 01/11 excluded).
AW-U PASS (explicit chains of 3P columns from surviving pairs; pruned pairs die out).
DESIGN LIMIT, found by Local after the run: the pruning admits only PERIODIC right continuations (columns 2, 3, ...
all P-periodic). That is sufficient for an actual right side but not necessary: column 2 is free at the times where
column 1 is black. So the positive results stand (a periodic continuation is a real one): both bounds are attained by
actual walls, 2P - 5 at P = 5 and 2P - 2 at P = 3 and 4. The negative readings are weaker than they look: that the
formal witnesses at P = 4 (odd 3) and P = 7 (odd 9) have no PERIODIC continuation does not show they have none.
AW-C2's exclusion of 01/11 is true for a stronger reason (GPT's GC309: its column-1 update fails at once), not
because of this pruning. Settling the negatives needs a search over non-periodic right sides.
"""
import resource
import sys


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def succ(u, v, P):
    """All P-periodic w with v(t + 1) = u(t) XOR (v(t) OR w(t)) for every t (u, v, w as bit lists)."""
    out = [[]]
    for t in range(P):
        need = v[(t + 1) % P] ^ u[t]                 # must equal v(t) OR w(t)
        if v[t]:
            if need != 1:
                return []
            out = [o + [b] for o in out for b in (0, 1)]
        else:
            out = [o + [need] for o in out]
    return out


def bits(x, P):
    return [(x >> t) & 1 for t in range(P)]


def word(b):
    return sum(v << t for t, v in enumerate(b))


def admissible(P):
    nodes = {(a, b) for a in range(1 << P) for b in range(1 << P)}
    nxt = {}
    for a, b in nodes:
        nxt[(a, b)] = {(b, word(w)) for w in succ(bits(a, P), bits(b, P), P)}
    alive = set(nodes)
    changed = True
    while changed:
        changed = False
        for n in list(alive):
            if not (nxt[n] & alive):
                alive.discard(n)
                changed = True
    return alive, nxt


def census(P, pairs):
    best = {}
    for w0, w1 in pairs:
        if w0 == 0:
            continue
        cols = [bits(w1, P), bits(w0, P)]               # columns 1, 0
        for j in range(1, 41):
            r, r2 = cols[-1], cols[-2]
            cols.append([r[(t + 1) % P] ^ (r[t] | r2[t]) for t in range(P)])
        row = [cols[1 + k][0] for k in range(41)]       # columns 0, -1, ..., -40
        k = 1
        while k <= 40:
            if row[k] == 0 and row[k - 1] == 1:
                e = k
                while e <= 40 and row[e] == 0:
                    e += 1
                if e <= 40:
                    n = e - k
                    key = 'odd' if n % 2 else 'even'
                    best[key] = max(best.get(key, 0), n)
                k = e
            k += 1
    return best


formal_odd = {4: 3, 5: 5, 6: 5, 7: 9}
formal_even = {3: 4, 4: 6, 5: 4, 6: 6, 7: 6}
p1 = p2 = False
c1 = True
u_ok = True
for P in range(2, 8):
    alive, nxt = admissible(P)
    adm = [(a, b) for a, b in alive]
    best = census(P, adm)
    print('P = %d: admissible pairs %d of %d; longest bounded runs, admissible: %s' % (P, len(alive), 1 << (2 * P), best))
    if P >= 4:
        p1 |= best.get('odd', 0) == 2 * P - 5
        c1 &= best.get('odd', 0) <= formal_odd[P]
    if P >= 3:
        p2 |= best.get('even', 0) == 2 * P - 2 or best.get('odd', 0) == 2 * P - 2
        c1 &= best.get('even', 0) <= formal_even[P]
    if P == 2:
        c2 = all(v <= 1 for v in best.values()) and (word([0, 1]), word([1, 1])) not in alive
        print('AW-C2', 'PASS' if c2 else 'FAIL')
    # AW-U: an explicit chain of 3P further columns from each surviving pair, by always stepping to a surviving successor
    for n in list(alive)[:200]:
        cur, steps = n, 0
        while steps < 3 * P:
            nx = [m for m in nxt[cur] if m in alive]
            if not nx:
                u_ok = False
                break
            cur, steps = nx[0], steps + 1
    dead = [n for n in nxt if n not in alive][:200]
    for n in dead:
        frontier, depth = {n}, 0
        while frontier and depth < 4 ** P:
            frontier = {m for f in frontier for m in nxt[f]}
            depth += 1
            if depth > 2 ** (2 * P) + 1:
                break
        u_ok &= not frontier
print('AW-P1', 'HELD' if p1 else 'REFUTED')
print('AW-P2', 'HELD' if p2 else 'REFUTED')
print('AW-C1', 'PASS' if c1 else 'FAIL')
print('AW-U', 'PASS' if u_ok else 'FAIL')
print('CPU %.1f s, peak RSS %.1f MiB' % (cpu(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20))
if cpu() > 600:
    sys.exit(1)
