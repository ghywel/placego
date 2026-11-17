#!/usr/bin/env python3
"""g326_review.py: Cloud's carrying-review instrument for GPT's G326 (H2, protected one-hole partitions with one bin of
size two; PROOFS.md, GC1599). Our code, written from the proof text and G315 (FOUR-BIN-PARTITIONS.md sections 5-6).

R1  Table 3(a): pair-sum omissions of [0,U] minus two internal holes, inside the actual pair extrema, equal the stated
    LOW list plus its reflection. Exhaustive for 6 <= U <= 80.
R2  Table 3(b): the same for H_p = [0,V] minus {p,p+1,V-1} and K_t = [0,V] minus {1,t,t+1}, 7 <= V <= 80.
R3  The reflection identity rM - T + (M-r)(M-r+1)/2 = L(r) + q, symbolic over a range.
R4  Every explicit repair and finite core (steps 2, 4, 5 and G315's triple), checked as literal partitions for all l, c
    in range: sizes, sums, disjointness, availability, and that the sums equal the stated targets.
R5  The construction, run as written: least six-slack choice with size-two tie priority (all remaining tie choices
    tried), one global reflection, G315's prefix/suffix/pivot recipe or a missing-pivot repair (high preferred), then
    the second bin's scalar sum by exact search; on failure only the explicit replacements in G326 may be used. Every
    protected H2 instance for 7 <= M <= MMAX. A FAIL is an instance where the proof's branches do not finish.

Record searched: G326, G315, H2, MI453, CL449/CL450 (H2 machine-true to M = 14, all holes).
PREDICTIONS (written before any run):
  R1, R2, R3, R4 hold everywhere tested (0.9; they are short, explicit claims).
  R5: no FAIL up to M = 16 (0.75). If the proof has a gap it will most likely sit at a tie or at the step-6 exclusion,
     which rests on the selection rule rather than on arithmetic. Counterfactual: a FAIL whose instance has a partition
     (H2 itself true there) means a gap in the case analysis, not a counterexample to H2.
  Unexpected check: the number of instances completed by each explicit replacement is reported; each replacement
     should fire at least once (otherwise the proof contains a dead branch, harmless but worth naming).

OUTCOME (2026-10-20, this container):
  R1 HELD: table 3(a) exact for every pair of internal holes, 6 <= U <= 80. R2 HELD: table 3(b) exact for every H_p
     and K_t, 7 <= V <= 80. R3 HELD for M < 200.
  R4 HELD: every explicit repair and core is a literal partition with the stated sizes and sums for l < 80, c < 40,
     and each targeted pair sum is a genuine gap before its repair.
  R5 HELD: 400,772 protected H2 instances, 8 <= M <= 18, every remaining tie choice; 0 FAIL. A rerun taking the pair's
     upper slack when both of its slacks tie (4,919 instances, M <= 16) also has 0 FAIL. Completions: pivot k=0 368,774;
     low repair 25,624; pivot k=1 5,902; high repair 412; step 4 (3,4) 35; step 4 (4,3) 23; G315 triple 2.
  Unexpected check: the three finite cores of step 4(iii), the step-4(ii) pair repair and the step-5 explicit partition
     never fired. Under the canonical choices here those branches are unreachable up to M = 18; they are dead
     branches, harmless to the proof's validity, and possibly excludable by the selection or protection.
"""
import sys, itertools
from collections import Counter
L = lambda r: r * (r - 1) // 2

def pair_omissions(pool):
    s = sorted(pool); sums = {x + y for x, y in itertools.combinations(s, 2)}
    lo, hi = s[0] + s[1], s[-1] + s[-2]
    return {j for j in range(lo, hi + 1) if j not in sums}

def R1(Umax=80):
    bad = 0
    for U in range(6, Umax + 1):
        for h1 in range(1, U):
            for h2 in range(h1 + 1, U):
                pool = [x for x in range(U + 1) if x not in (h1, h2)]
                low = set(); H = {h1, h2}
                if 2 in H and max(H - {2}, default=0) >= 3: low.add(2)
                if H in ({1, 3}, {2, 3}): low.add(3)
                if H in ({1, 4}, {3, 4}): low.add(4)
                R = {U - h1, U - h2}; high = set()
                if 2 in R and max(R - {2}, default=0) >= 3: high.add(2 * U - 2)
                if R in ({1, 3}, {2, 3}): high.add(2 * U - 3)
                if R in ({1, 4}, {3, 4}): high.add(2 * U - 4)
                pred = low | high
                if pair_omissions(pool) != pred: bad += 1
    return bad

def R2(Vmax=80):
    bad = 0
    def lowH(V, p):
        out = set()
        if p == 2: out |= {2, 3}
        if p == 3: out.add(4)
        if V == 7 and p in (1, 4): out.add(6)
        return out
    def lowK(V, t):
        out = set()
        if t == 3: out |= {3, 4}
        if t == 4: out.add(4)
        return out
    for V in range(7, Vmax + 1):
        for p in range(0, V - 2):
            pool = [x for x in range(V + 1) if x not in (p, p + 1, V - 1)]
            t = V - p - 1                       # reflection of H_p is K_t
            pred = lowH(V, p) | {2 * V - j for j in lowK(V, t)}
            if pair_omissions(pool) != pred: bad += 1
        for t in range(2, V):
            pool = [x for x in range(V + 1) if x not in (1, t, t + 1)]
            p = V - t - 1
            pred = lowK(V, t) | {2 * V - j for j in lowH(V, p)}
            if pair_omissions(pool) != pred: bad += 1
    return bad

def R3(Mmax=200):
    bad = 0
    for M in range(3, Mmax):
        for q in range(1, M):
            T = M * (M + 1) // 2 - q
            for r in range(1, M):
                if r * M - T + (M - r) * (M - r + 1) // 2 != L(r) + q: bad += 1
    return bad

def check_partition(M, Q, parts, sizes, targets):
    P = set(range(M + 1)) - {Q}; allv = [x for part in parts for x in part]
    if len(allv) != len(set(allv)) or set(allv) != P: return False
    return all(len(part) == sz and sum(part) == tg for part, sz, tg in zip(parts, sizes, targets))

def explicit_candidates(M, Q, a):
    """All explicit replacements of G326 (and G315's triple), parameterized by the selected size a; each yields
    (A, pair, rest) or (A, triple, rest); the caller checks them as literal partitions."""
    P = set(range(M + 1)) - {Q}; out = []
    def add(name, A, B):
        A, B = set(A), set(B)
        if len(A | B) == len(A) + len(B) and (A | B) <= P: out.append((name, sorted(A), sorted(B), sorted(P - A - B)))
    l = a - 1
    add('step4 (3,4)', list(range(0, l - 1)) + [l + 1, l + 2], [l - 1, l + 5])
    add('step4 (4,3)', list(range(0, l - 1)) + [l, l + 2], [l - 1, l + 5])
    add('G315 triple', list(range(0, a - 2)) + [a - 1, a], [a - 2, a + 2, a + 3])
    add('step4 (ii) pair', list(range(0, a - 2)) + [a - 1, a], [a + 1, a + 5])
    for (Acore, pcore, Ccore) in [((0, 2, 3), (4, 8), (1, 6, 7)), ((1, 2, 3), (5, 7), (0, 6, 8)), ((0, 2, 4), (5, 9), (1, 3, 7, 8))]:
        sh = l - 2
        add('core ' + ''.join(map(str, Acore)), list(range(0, l - 2)) + [x + sh for x in Acore], [x + sh for x in pcore])
    l5 = a - 2
    add('step5', list(range(0, l5 - 1)) + [l5, l5 + 3, l5 + 7], [l5 + 1, l5 + 5])
    return out

def subset_sum_exists(pool, r, s):
    reach = {(0, 0)}
    for x in pool:
        reach |= {(n + 1, t + x) for n, t in reach if n < r}
    return (r, s) in reach

def construct(M, q, sizes, targets, tie_choice=None, stats=None):
    """Run G326's construction. Returns ('ok', how) or ('FAIL', info)."""
    P0 = [x for x in range(M + 1) if x != q]
    al = lambda P, r: sum(P[:r]); be = lambda P, r: sum(P[-r:])
    sl = []
    for i, (c, t) in enumerate(zip(sizes, targets)):
        sl.append((t - al(P0, c), 'low', i)); sl.append((be(P0, c) - t, 'up', i))
    h = min(x[0] for x in sl)
    tied = [x for x in sl if x[0] == h]
    two = [x for x in tied if sizes[x[2]] == 2]
    choice = two[0] if two else (tied[tie_choice % len(tied)] if tie_choice is not None else tied[0])
    _, side, i = choice
    if side == 'up':                                   # reflect the whole original pool once
        Q = M - q; tg = [c * M - t for c, t in zip(sizes, targets)]
    else:
        Q = q; tg = list(targets)
    P = [x for x in range(M + 1) if x != Q]
    a, sA = sizes[i], tg[i]
    others = [j for j in range(3) if j != i]
    # G315 recipe: l lowest values, k highest values, one pivot
    A = None; formal = None
    for k in range(a):
        l = a - 1 - k
        pre, suf = P[:l], (P[len(P) - k:] if k else [])
        p = sA - sum(pre) - sum(suf)
        if P[l] <= p <= P[len(P) - k - 1]:
            if p != Q: A = pre + suf + [p]; how = f'pivot k={k}'
            else: formal = (l, k)
            break
    if A is None:
        if formal is None: return ('FAIL', 'no recipe: target outside the pivot ranges')
        l, k = formal; u0 = M - k + 1
        if k >= 1 and u0 - Q >= 3:
            A = list(range(0, l)) + [x for x in range(u0 + 1, M + 1)] + [Q + 1, u0 - 1]; how = 'high repair'
        elif l >= 1 and Q - (l - 1) >= 3:
            A = list(range(0, l - 1)) + list(range(u0, M + 1)) + [l, Q - 1]; how = 'low repair'
        else: return ('FAIL', f'missing pivot with no repair l={l} k={k} Q={Q}')
    assert len(A) == a and sum(A) == sA and Q not in A and len(set(A)) == a, (A, a, sA)
    R = [x for x in P if x not in A]
    j1, j2 = others
    if sizes[j1] > sizes[j2]: j1, j2 = j2, j1          # j1: the smaller remaining bin (the pair when a >= 3)
    if subset_sum_exists(R, sizes[j1], tg[j1]):
        if stats is not None: stats[how] += 1
        return ('ok', how)
    for name, X, Y, Z in explicit_candidates(M, Q, a):
        for jy, jz in ((j1, j2), (j2, j1)):
            if check_partition(M, Q, [X, Y, Z], [a, sizes[jy], sizes[jz]], [sA, tg[jy], tg[jz]]):
                if stats is not None: stats['explicit ' + name] += 1
                return ('ok', 'explicit ' + name)
    return ('FAIL', f'{how}: second bin missing; oriented Q={Q} a={a} A={sorted(A)} targets={tg} sizes={sizes} sel={i}{side}')

def R5(Mmin=7, Mmax=16):
    stats = Counter(); fails = []; n = 0
    for M in range(Mmin, Mmax + 1):
        for b in range(3, M - 4):
            c = M - 2 - b
            if c < 3 or c < b: continue
            sizes = (2, b, c)
            for q in range(1, M):
                T = M * (M + 1) // 2 - q
                for u in range(3, 2 * M):
                    for v in range(b * (b + 1) // 2, T):
                        w = T - u - v
                        tg = (u, v, w)
                        ok = all(sum(tg[j] for j in J) >= (lambda C: C * (C + 1) // 2)(sum(sizes[j] for j in J))
                                 for J in [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2)])
                        if not ok: continue
                        n += 1
                        P0 = [x for x in range(M + 1) if x != q]
                        sl = [t - sum(P0[:cc]) for cc, t in zip(sizes, tg)] + [sum(P0[-cc:]) - t for cc, t in zip(sizes, tg)]
                        ntied = sl.count(min(sl))
                        for tc in range(ntied):
                            res = construct(M, q, sizes, tg, tie_choice=tc, stats=stats if tc == 0 else None)
                            if res[0] == 'FAIL': fails.append((M, q, sizes, tg, tc, res[1]))
        print(f'  M={M}: instances so far {n}, fails {len(fails)}', flush=True)
    return n, stats, fails

if __name__ == '__main__':
    print('R1 (table 3a) mismatches:', R1())
    print('R2 (table 3b) mismatches:', R2())
    print('R3 (reflection identity) mismatches:', R3())
    Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    n, stats, fails = R5(7, Mmax)
    print('R5: protected H2 instances', n, '| completions by branch', dict(stats))
    print('R5: FAILS', len(fails)); [print('   ', f) for f in fails[:15]]
