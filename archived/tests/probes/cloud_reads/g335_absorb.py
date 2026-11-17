"""Cloud's carrying-read instrument for GPT's G335, and a bounded absorption test (CL477).

Score-vector model.  A tournament on [0, M] (M+1 vertices) is described by its score vector; by Landau, the strong
components are the blocks of the sorted scores cut where the prefix sum equals L(k).  Colours 0..3 (bins) and the
distinguished vertex * (colour 4, score q).  Colour totals t_i are invariants of every move below.

Part A (G335 checks, random tournaments): Phi = sum d^2 = sum j^2 - 2 * (#cyclic triangles); a same-colour path
reversal inside a block changes (d_u, d_v) by (-1, +1); after hill-climbing on that move every block is rainbow and
there are at most 11 nontrivial blocks with at most 45 vertices.

Part B (absorption): from random starting tournaments with protected totals (sizes >= 3, t_J >= T(C_J)), climb with
  move 1: same-colour transfer inside a block (G335 step 2);
  move 2: straighten one nontrivial block that avoids * (assign its scores s..e in some order), then repair the
          colour-total change by colour swaps of adjacent-score singleton vertices (neither is *);
  move 3: the same for the block containing *, keeping * at score q.
Record whether the climb reaches a transitive tournament (= a partition), and the shape of what is left when stuck.
Predictions: Part A all identities hold.  Part B: moves 1+2+3 reach transitive in most runs; stuck runs keep a
cyclic block containing * or on a side where some colour has <= 2 vertices (G335's thin case).
Counterfactual: stuck runs with all colours >= 3 on both sides and * alone would mean thick cycles survive these moves.
Move 4 (added): G335 step 3 itself, replacing any consecutive region of blocks avoiding * by an exact partition
found by capped backtracking.

OUTCOME (python3 g335_absorb.py 400; 2.5 s).  Part A: 0 failures (Phi identity; Landau blocks = strong components,
3,000 random tournaments).  Part B, random protected targets, M = 12..20, six size patterns: 2,332 of 2,340 starts
reach a transitive tournament (one start failed to build).  The 7 stuck runs are ALL explained: each cyclic block
is the block of * or lies on a side where some colour has <= 2 vertices; every stuck run has both sides thin, and 4
of 7 keep only the block of *.  None stuck at M = 18 or 20.  Prediction held.  Caveat: the move set is capped and
not complete, so a stuck run is a local stop of THESE moves, not a G335 maximiser.
"""
import itertools, random, sys
from collections import Counter

L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2

def random_tournament(n, rnd):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rnd.random() < 0.5: A[i][j] = 1
            else: A[j][i] = 1
    return A

def blocks(d):
    """Landau blocks: list of lists of vertex indices, in increasing score order."""
    order = sorted(range(len(d)), key=lambda v: d[v]); out = []; cur = []; s = 0
    for k, v in enumerate(order):
        cur.append(v); s += d[v]
        if s == L(k + 1) + k + 1 - (k + 1) and s == (k + 1) * k // 2:  # prefix sum equals C(k+1, 2)
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def part_A(trials=3000, seed=3):
    rnd = random.Random(seed); bad = 0
    for _ in range(trials):
        n = rnd.randint(3, 14); A = random_tournament(n, rnd)
        d = [sum(r) for r in A]
        tau = sum(1 for a, b, c in itertools.combinations(range(n), 3)
                  if (A[a][b] and A[b][c] and A[c][a]) or (A[b][a] and A[c][b] and A[a][c]))
        if sum(x * x for x in d) != sum(j * j for j in range(n)) - 2 * tau: bad += 1
        # Landau blocks vs strong components (Floyd reachability)
        R = [row[:] for row in A]
        for k in range(n):
            for i in range(n):
                if R[i][k]:
                    for j in range(n):
                        if R[k][j]: R[i][j] = 1
        comp = {frozenset(j for j in range(n) if j == i or (R[i][j] and R[j][i])) for i in range(n)}
        if comp != {frozenset(b) for b in blocks(d)}: bad += 1
    return bad

def protected_instances(M, C, rnd, k):
    out = []
    for q in range(1, M):
        S = T(M) - q
        for _ in range(200):
            t = [rnd.randint(T(c), 4 * M) for c in C[:3]]; t.append(S - sum(t))
            ok = all(sum(t[i] for i in J) >= T(sum(C[i] for i in J))
                     for r in (1, 2, 3) for J in itertools.combinations(range(4), r))
            if ok: out.append((q, tuple(t)))
    rnd.shuffle(out); return out[:k]

def start_scores(M, C, q, t, rnd):
    """A random tournament with colour totals t and * score q: random orientation, then fix totals by
    reversing directed paths between colours (each reversal moves one win along the path)."""
    n = M + 1; col = [4] + [i for i in range(4) for _ in range(C[i])]
    rnd.shuffle(col)
    A = random_tournament(n, rnd)
    target = {i: t[i] for i in range(4)}; target[4] = q
    def tot():
        d = [sum(r) for r in A]; s = Counter()
        for v in range(n): s[col[v]] += d[v]
        return s
    for _ in range(20000):
        s = tot(); need = [c for c in range(5) if s[c] < target[c]]; extra = [c for c in range(5) if s[c] > target[c]]
        if not need: break
        # BFS from a vertex of an 'extra' colour to a vertex of a 'need' colour along arcs; reversing the path
        # moves one win from the start to the end
        src = [v for v in range(n) if col[v] in extra]; rnd.shuffle(src)
        prev = {v: None for v in src}; fr = list(src); hit = None
        while fr and hit is None:
            nf = []
            for u in fr:
                for w in range(n):
                    if A[u][w] and w not in prev:
                        prev[w] = u; nf.append(w)
                        if col[w] in need: hit = w; break
                if hit is not None: break
            fr = nf
        if hit is None: return None, None
        w = hit
        while prev[w] is not None:
            u = prev[w]; A[u][w] = 0; A[w][u] = 1; w = u
    d = [sum(r) for r in A]
    return d, col

def climb(d, col, q, M):
    n = len(d); star = col.index(4)
    def move1():
        for b in blocks(d):
            seen = {}
            for v in b:
                c = col[v]
                if c in seen:
                    u = seen[c]; lo, hi = (u, v) if d[u] <= d[v] else (v, u)
                    d[lo] -= 1; d[hi] += 1; return True
                seen[c] = v
        return False
    def swap_repair(delta, frozen):
        """Move colour totals by delta using colour swaps of singleton-block vertices with scores x, x+1."""
        for _ in range(200):
            if all(x == 0 for x in delta.values()): return True
            sing = {}
            for b in blocks(d):
                if len(b) == 1 and b[0] != star and b[0] not in frozen: sing[d[b[0]]] = b[0]
            # graph: colour B -> colour A if some x in A and x+1 in B (swap gives A +1, B -1)
            edges = {}
            for x, v in sing.items():
                w = sing.get(x + 1)
                if w is not None and col[v] != col[w]: edges.setdefault(col[w], []).append((col[v], v, w))
            srcs = [c for c in range(4) if delta.get(c, 0) < 0]; dsts = [c for c in range(4) if delta.get(c, 0) > 0]
            prev = {c: None for c in srcs}; fr = list(srcs); found = None
            while fr and found is None:
                nf = []
                for B in fr:
                    for (Acol, v, w) in edges.get(B, []):
                        if Acol not in prev:
                            prev[Acol] = (B, v, w); nf.append(Acol)
                            if Acol in dsts: found = Acol; break
                    if found is not None: break
                fr = nf
            if found is None: return False
            # perform the last swap only (into 'found'), then re-plan
            B, v, w = prev[found]
            col[v], col[w] = col[w], col[v]
            delta[found] -= 1; delta[B] += 1
        return False
    def move23():
        for b in blocks(d):
            if len(b) < 3: continue
            lo = sorted(d[v] for v in b)[0]
            s0 = min(d[v] for v in b); start = sum(1 for v in range(n) if d[v] < s0)
            vals = list(range(start, start + len(b)))
            for perm in itertools.permutations(vals):
                if star in b and perm[b.index(star)] != q: continue
                newd = dict(zip(b, perm)); delta = Counter()
                for v in b:
                    if v != star: delta[col[v]] -= newd[v] - d[v]
                save_d, save_c = d[:], col[:]
                for v in b: d[v] = newd[v]
                if swap_repair(Counter(delta), set(b)):
                    return True
                d[:] = save_d; col[:] = save_c
        return False
    def partition(vals, counts, sums):
        """Backtracking: split sorted vals into colour classes with given counts and sums (dicts by colour)."""
        vals = sorted(vals, reverse=True); cols = list(counts); rc = dict(counts); rs = dict(sums); owner = {}
        steps = [0]
        def go(i):
            steps[0] += 1
            if steps[0] > 200000: return False
            if i == len(vals): return all(rs[c] == 0 for c in cols)
            rest = vals[i:]
            for c in cols:
                if rc[c] == 0: continue
                if rs[c] - vals[i] < 0: continue
                rc[c] -= 1; rs[c] -= vals[i]; owner[vals[i]] = c
                okk = True
                for c2 in cols:
                    k = rc[c2]; r2 = rest[1:]
                    if k > len(r2) or (k and not (sum(r2[len(r2) - k:]) <= rs[c2] <= sum(r2[:k]))) or (not k and rs[c2]): okk = False; break
                if okk and go(i + 1): return True
                rc[c] += 1; rs[c] += vals[i]
            return False
        return owner if go(0) else None
    def move4():
        allb = blocks(d); sb = next(i for i, b in enumerate(allb) if star in b)
        for lo_i in range(len(allb)):
            for hi_i in range(lo_i, len(allb)):
                if lo_i <= sb <= hi_i: break
                R = [v for b in allb[lo_i:hi_i + 1] for v in b]
                if all(len(b) == 1 for b in allb[lo_i:hi_i + 1]): continue
                start = sum(len(b) for b in allb[:lo_i])
                counts = Counter(col[v] for v in R); sums = Counter()
                for v in R: sums[col[v]] += d[v]
                own = partition(range(start, start + len(R)), counts, sums)
                if own is None: continue
                byc = {}
                for val, c in own.items(): byc.setdefault(c, []).append(val)
                for c in byc:
                    for v, val in zip([v for v in R if col[v] == c], sorted(byc[c])): d[v] = val
                return True
        return False
    for _ in range(5000):
        if move1(): continue
        if move4(): continue
        if all(len(b) == 1 for b in blocks(d)): return 'transitive', None
        if move23(): continue
        bl = [b for b in blocks(d) if len(b) > 1]
        sb = next(i for i, b in enumerate(blocks(d)) if star in b)
        shape = []
        allb = blocks(d)
        for b in bl:
            i = allb.index(b)
            side = 'star' if star in b else ('low' if i < sb else 'high')
            shape.append((side, len(b)))
        low = Counter(col[v] for i, b in enumerate(allb) if i < sb for v in b)
        high = Counter(col[v] for i, b in enumerate(allb) if i > sb for v in b)
        thin = (min(low.get(c, 0) for c in range(4)) <= 2, min(high.get(c, 0) for c in range(4)) <= 2)
        unexplained = sum(1 for side, _ in shape if (side == 'low' and not thin[0]) or (side == 'high' and not thin[1]))
        return 'stuck', (tuple(shape), thin, unexplained)
    return 'limit', None

def part_B(M, C, runs, seed):
    rnd = random.Random(seed); res = Counter(); shapes = Counter()
    for q, t in protected_instances(M, C, rnd, runs):
        d, col = start_scores(M, C, q, t, rnd)
        if d is None: res['nostart'] += 1; continue
        r, info = climb(d, col, q, M)
        res[r] += 1
        if info: shapes[info] += 1
    unexpl = sum(n for k, n in shapes.items() if k[2] > 0)
    star_only = sum(n for k, n in shapes.items() if all(side == 'star' for side, _ in k[0]))
    return dict(res), dict(unexplained_runs=unexpl, star_block_only=star_only), shapes.most_common(5)

if __name__ == '__main__':
    print('Part A failures:', part_A())
    runs = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    for M, C in ((12, (3, 3, 3, 3)), (14, (3, 4, 3, 4)), (16, (4, 4, 4, 4)), (16, (3, 3, 4, 6)), (18, (3, 5, 4, 6)), (20, (5, 5, 5, 5))):
        print('Part B', M, C, part_B(M, C, runs, M), flush=True)
