#!/usr/bin/env python3
"""Cloud CL767: independent replay of the period-12 return machine (GC2830).

Built from the local rule alone: no kit tile, no graph of GPT's is read.
Frame: a vertex is a pair (c, d) of 12-tick profiles at sites i+1, i+2 of a
configuration x with tau^12 x = x, where (tau x)_i = x_i xor (x_{i+1} or x_{i+2}).
Its children are (u, c) with u(t+1) = u(t) xor (c(t) or d(t)), cyclically in t.
Bit t of a profile word is the cell at tick t.

Stage 1: all 2^24 pairs; keep the pairs on a two-sided infinite path (the core).
Stage 2: strongly connected components of the core; the component of U.
Stage 3: return structure, temporal rotation, isolation of the six components.
Stage 4: period law on every primitive event word of length <= 6, by running the
         ordinary rule on a ring.  Stage 5: the three 34-cell return tiles.
"""
import sys, itertools, math
import numpy as np

P = 12
FULL = (1 << P) - 1
N = 1 << (2 * P)
U = (1323, 2868)
V = (2772, 3372)


def rot(w, k):
    k %= P
    return ((w >> k) | (w << (P - k))) & FULL


def prefix(m):
    word = 0; bit = 0
    for t in range(P - 1):
        bit ^= (m >> t) & 1
        word |= bit << (t + 1)
    return word


def children(v):
    c, d = v
    m = c | d
    if bin(m).count("1") % 2:
        return []
    w = prefix(m)
    return [(w, c), (w ^ FULL, c)]


def valid(u, c, d):
    return all(((u >> ((t + 1) % P)) & 1) == (((u >> t) & 1) ^ (((c >> t) & 1) | ((d >> t) & 1)))
               for t in range(P))


def main():
    px = np.array([prefix(m) for m in range(1 << P)], dtype=np.int64)
    par = np.array([bin(m).count("1") & 1 for m in range(1 << P)], dtype=bool)
    idx = np.arange(N, dtype=np.int64)
    c = idx >> P
    d = idx & FULL
    m = c | d
    ok = ~par[m]
    w = px[m]
    ch0 = ((w << P) | c).astype(np.int32)
    ch1 = (((w ^ FULL) << P) | c).astype(np.int32)
    del idx, d, m, w
    print("pairs", N, "with an even drive (two children)", int(ok.sum()))

    # forward-infinite
    A = ok.copy(); rounds = 0
    while True:
        B = ok & (A[ch0] | A[ch1]); rounds += 1
        if (B == A).all():
            break
        A = B
    print("forward-infinite pairs", int(A.sum()), "rounds", rounds)
    # backward-infinite inside the forward-infinite set
    C = A.copy(); rounds = 0
    while True:
        hit = np.zeros(N, dtype=bool)
        src = np.nonzero(C)[0]
        hit[ch0[src]] = True
        hit[ch1[src]] = True
        B = C & hit
        # a forward step must also stay inside
        B = B & (B[ch0] | B[ch1])
        rounds += 1
        if (B == C).all():
            break
        C = B
    core = np.nonzero(C)[0]
    print("core (pairs on a two-sided infinite path)", len(core), "rounds", rounds)
    coreset = set(int(v) for v in core)
    adj = {}
    for v in coreset:
        adj[v] = [int(x) for x in (ch0[v], ch1[v]) if int(x) in coreset]
    edges = sum(len(a) for a in adj.values())
    print("core edges", edges)

    # Tarjan, iterative
    index = {}; low = {}; onst = set(); st = []; comps = []; counter = [0]
    for root in adj:
        if root in index:
            continue
        work = [(root, 0)]
        index[root] = low[root] = counter[0]; counter[0] += 1; st.append(root); onst.add(root)
        while work:
            v, i = work[-1]
            if i < len(adj[v]):
                work[-1] = (v, i + 1)
                x = adj[v][i]
                if x not in index:
                    index[x] = low[x] = counter[0]; counter[0] += 1; st.append(x); onst.add(x)
                    work.append((x, 0))
                elif x in onst:
                    low[v] = min(low[v], index[x])
            else:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[v])
                if low[v] == index[v]:
                    comp = []
                    while True:
                        x = st.pop(); onst.discard(x); comp.append(x)
                        if x == v:
                            break
                    comps.append(comp)
    cyc = [set(cm) for cm in comps if len(cm) > 1 or cm[0] in adj[cm[0]]]
    triv = sum(1 for cm in comps if not (len(cm) > 1 or cm[0] in adj[cm[0]]))
    print("strongly connected components with a cycle:", len(cyc), "; transient core pairs:", triv)
    shape = {}
    for cm in cyc:
        e = sum(1 for v in cm for x in adj[v] if x in cm)
        shape[(len(cm), e)] = shape.get((len(cm), e), 0) + 1
    print("component shapes (vertices, edges): count ->", sorted(shape.items()))
    branching = [cm for cm in cyc if sum(1 for v in cm for x in adj[v] if x in cm) > len(cm)]
    print("components with more edges than vertices:", len(branching))

    key = lambda v: (v[0] << P) | v[1]
    unkey = lambda n: (n >> P, n & FULL)
    assert key(U) in coreset and key(V) in coreset, "U or V is not in the core"
    CU = next(cm for cm in cyc if key(U) in cm)
    eU = sum(1 for v in CU for x in adj[v] if x in CU)
    br = sorted(unkey(v) for v in CU if sum(1 for x in adj[v] if x in CU) > 1)
    print("P1: component of U: vertices", len(CU), "edges", eU, "branch vertices", br)
    assert all(valid(unkey(x)[0], *unkey(v)) for v in CU for x in adj[v])

    def first_return(b, child):
        path = [b, child]
        while path[-1] not in (key(U), key(V)):
            nx = [x for x in adj[path[-1]] if x in CU]
            assert len(nx) == 1
            path.append(nx[0])
        return path
    ret = {}
    for b, name in ((key(U), "U"), (key(V), "V")):
        for ch in adj[b]:
            assert ch in CU
            p = first_return(b, ch)
            end = "U" if p[-1] == key(U) else "V"
            ret[(name, end)] = p
            print("   first return", name, "->", end, "cells", len(p) - 1)
    lens = {k: len(p) - 1 for k, p in ret.items()}
    print("P1 verdict:", "PASS" if (len(CU), eU) == (30, 32) and br == sorted([U, V]) and
          lens == {("U", "U"): 14, ("U", "V"): 10, ("V", "V"): 14, ("V", "U"): 10} else "FAIL")

    # P2: temporal rotation
    R = lambda v, k=1: key(tuple(rot(x, k) for x in unkey(v)))
    orbit = []
    cur = CU
    for k in range(P):
        img = {R(v, k) for v in CU}
        which = [i for i, cm in enumerate(cyc) if cm == img]
        assert len(which) == 1, "rotated component is not a component"
        orbit.append(which[0])
    print("P2: component index under rotation by 0..11 ticks:", orbit)
    six = len(set(orbit)) == 6 and orbit[6:] == orbit[:6] and len(set(orbit[:6])) == 6
    swap = R(key(U), 6) == key(V) and R(key(V), 6) == key(U)
    nofix = all(R(v, 6) != v for v in CU)
    lp = all(min(k for k in range(1, 13) if R(v, k) == v) == 12 for v in CU)
    print("P2 verdict:", "PASS" if six and swap and nofix and lp else "FAIL",
          "| 6-cycle", six, "| six ticks swap U,V", swap, "| no fixed pair", nofix,
          "| every pair has least temporal period 12", lp)

    # P4: isolation in the full core, and the other components
    fam = set()
    for i in set(orbit):
        fam |= cyc[i]
    out_e = [(v, x) for v in fam for x in adj[v] if x not in fam]
    in_e = [(v, x) for v in coreset - fam for x in adj[v] if x in fam]
    print("P4: family pairs", len(fam), "| core edges leaving the family", len(out_e),
          "| core edges entering the family", len(in_e))
    for v, x in (in_e[:3] + out_e[:3]):
        print("     edge", unkey(v), "->", unkey(x))
    others = [cm for i, cm in enumerate(cyc) if i not in set(orbit)]
    oshape = {}
    for cm in others:
        e = sum(1 for v in cm for x in adj[v] if x in cm)
        oshape[(len(cm), e)] = oshape.get((len(cm), e), 0) + 1
    print("    other cyclic components (vertices, edges): count ->", sorted(oshape.items()))
    other_branch = [cm for cm in others if sum(1 for v in cm for x in adj[v] if x in cm) > len(cm)]
    print("    other components with branching:", len(other_branch))
    cross = sum(1 for v in coreset for x in adj[v]
                if not any(v in cm and x in cm for cm in cyc))
    print("    core edges not inside one cyclic component (links and transients):", cross)
    # least temporal periods present in the core
    per = {}
    for v in coreset:
        k = min(k for k in range(1, 13) if R(v, k) == v)
        per[k] = per.get(k, 0) + 1
    print("    least temporal period of core pairs: count ->", sorted(per.items()))
    print("P4 verdict:", "PASS" if not out_e and not in_e and not other_branch else "FAIL (see counts)")

    # P3: period law
    def path_for(word, start):
        cur = start; path = [key(start)]
        for e in word:
            nm = "U" if cur == U else "V"
            tgt = nm if e == 0 else ("V" if nm == "U" else "U")
            p = ret[(nm, tgt)]
            path += p[1:]
            cur = U if tgt == "U" else V
        return path, cur

    def row_of(path):  # leftward path: path[j] = (profile at site -j, profile at site -j+1)
        cells = [unkey(v)[0] & 1 for v in path[1:]]      # sites -1, -2, ... (tick 0)
        return cells[::-1]                               # increasing site order

    def F(x):
        n = len(x)
        return [x[(j - 1) % n] ^ (x[j] | x[(j + 1) % n]) for j in range(n)]

    def least_spatial(x):
        n = len(x)
        return min(p for p in range(1, n + 1) if n % p == 0 and all(x[j] == x[(j + p) % n] for j in range(n)))

    def primitive(wd):
        n = len(wd)
        return not any(n % p == 0 and wd == wd[:p] * (n // p) for p in range(1, n))

    tested = 0; bad = []
    for mlen in range(1, 7):
        for wd in itertools.product((0, 1), repeat=mlen):
            if not primitive(wd):
                continue
            r = sum(wd); L = 14 * mlen - 4 * r
            reps = 1 if r % 2 == 0 else 2
            path, end = path_for(wd * reps, U)
            assert end == U and len(path) - 1 == L * reps
            x = row_of(path)
            sp = least_spatial(x)
            pred_sp = L if r % 2 == 0 else 2 * L
            pred_t = (12 * L // math.gcd(12, L)) if r % 2 == 0 else 12 * L // math.gcd(2 * L, L + 6)
            y = x; n = 0
            while True:
                y = F(y); n += 1
                if y == x or n > 20000:
                    break
            tested += 1
            if sp != pred_sp or n != pred_t:
                bad.append((wd, sp, pred_sp, n, pred_t))
            if wd in ((0,), (1,), (0, 1), (0, 1, 1), (0, 0, 1, 1)):
                print("   word", "".join(map(str, wd)), "L", L, "spatial", sp, "ordinary period", n)
    print("P3: primitive words tested", tested, "mismatches", len(bad), bad[:3])
    print("P3 verdict:", "PASS" if not bad and tested == 106 else "FAIL")

    # P5: the three 34-cell return tiles
    gpt = {"011": "0001111110000100011100011111100001",
           "101": "0001111110000100011100000001000111",
           "110": "0001111110000100011111100001000111"}
    okk = True; tiles = {}
    for name in ("011", "101", "110"):
        path, end = path_for(tuple(int(ch) for ch in name), U)
        s = "".join(map(str, row_of(path)))
        tiles[name] = s
        print("   tile", name, s, "cells", len(s), "matches GPT's string:", s == gpt[name])
        okk &= (end == U and len(s) == 34 and s == gpt[name])
    dec = {name: tiles[name][20] + tiles[name][23] for name in tiles}
    print("   bits at offsets 20, 23:", dec)
    # shortest lengths with more than one closed walk at U
    cnt = {}
    for mlen in range(1, 5):
        for wd in itertools.product((0, 1), repeat=mlen):
            if sum(wd) % 2 == 0:
                cnt.setdefault(14 * mlen - 4 * sum(wd), []).append("".join(map(str, wd)))
    small = {L: ws for L, ws in sorted(cnt.items()) if L <= 40}
    print("   closed walks at U by cell length (<= 40):", small)
    print("P5 verdict:", "PASS" if okk and len(set(tiles.values())) == 3 and len(set(dec.values())) == 3 else "FAIL")
    # Added after run 1 (kept as cloud_period12_replay_run1.out): my window holds the 34 new
    # profiles of the walk (sites -34..-1); GPT's holds sites -33..0.  Both walks close at U,
    # so the two windows are one cyclic shift apart.  Compare after that shift.
    al = {n: tiles[n][1:] + tiles[n][0] for n in tiles}
    print("   after a one-cell shift of the window:", {n: al[n] == gpt[n] for n in al},
          "| bits at offsets 20, 23:", {n: al[n][20] + al[n][23] for n in al})
    print("P5 after alignment:", "PASS" if all(al[n] == gpt[n] for n in al)
          and len({al[n][20] + al[n][23] for n in al}) == 3 else "FAIL")

    # Stage 6 (after run 1's P4 result): how the core outside the family feeds the family.
    names = {}
    for i, cm in enumerate(cyc):
        e = sum(1 for v in cm for x in adj[v] if x in cm)
        tp = sorted({min(k for k in range(1, 13) if R(v, k) == v) for v in cm})
        names[i] = (len(cm), e, tp)
    compof = {}
    for i, cm in enumerate(cyc):
        for v in cm:
            compof[v] = i
    between = [(compof[v], compof[x]) for v in coreset for x in adj[v]
               if v in compof and x in compof and compof[v] != compof[x]]
    print("S6: edges directly between two different cyclic components:", len(between))
    trans = coreset - set(compof)
    tper = {}
    for v in trans:
        k = min(k for k in range(1, 13) if R(v, k) == v)
        tper[k] = tper.get(k, 0) + 1
    print("S6: transient core pairs", len(trans), "by least temporal period", sorted(tper.items()))
    # reachability from each non-family cyclic component
    famidx = set(orbit)
    for i, cm in enumerate(cyc):
        if i in famidx:
            continue
        seen = set(cm); work = list(cm); depth = {v: 0 for v in cm}
        hits = {}
        while work:
            v = work.pop(0)
            for x in adj[v]:
                if x not in seen:
                    seen.add(x); depth[x] = depth[v] + (0 if x in cm else 1); work.append(x)
                    if x in compof and compof[x] != i:
                        hits.setdefault(compof[x], depth[x])
        fam_hit = sorted((orbit.index(j), dd) for j, dd in hits.items() if j in famidx)
        oth_hit = sorted((names[j][0], dd) for j, dd in hits.items() if j not in famidx)
        cells = [unkey(v)[0] & 1 for v in cm]
        print("   component", names[i], "black cells at tick 0 on its cycle:", sum(cells),
              "| reaches family phases (rotation index, link length):", fam_hit,
              "| reaches other cycles (size, link length):", oth_hit)
    # rotation by one tick on the cycles outside the family
    low = [i for i in range(len(cyc)) if i not in famidx]
    for i in low:
        img = {R(v, 1) for v in cyc[i]}
        j = [k for k in low if cyc[k] == img]
        print("   rotation by one tick sends component", names[i], "black", sum(unkey(v)[0] & 1 for v in cyc[i]),
              "to component", names[j[0]] if j else None, "black", sum(unkey(v)[0] & 1 for v in cyc[j[0]]) if j else None,
              "| same component:", bool(j) and j[0] == i)
    # one explicit entering configuration, checked by running the moving rule on a window
    src_cm = next(cm for i, cm in enumerate(cyc) if i not in famidx and len(cm) == 10
                  and any(x in trans for v in cm for x in adj[v]))
    v0 = next(v for v in src_cm if any(x in trans for x in adj[v]))
    # walk back around the source cycle (it is a plain cycle), then forward into the family
    cyc_order = [v0]
    while True:
        nx = [x for x in adj[cyc_order[-1]] if x in src_cm][0]
        if nx == v0:
            break
        cyc_order.append(nx)
    pos = cyc_order.index(v0)
    right = [cyc_order[(pos + 1 + j) % len(cyc_order)] for j in range(6 * len(cyc_order))]  # ends at v0
    path = right[:]
    cur = [x for x in adj[v0] if x in trans][0]
    path.append(cur); link = 1
    while cur not in fam:
        nxt = [x for x in adj[cur] if x in trans or x in fam]
        cur = nxt[0]; path.append(cur); link += 1
    entered = orbit.index(compof[cur])
    for _ in range(120):
        nxt = [x for x in adj[cur] if x in fam]
        cur = nxt[0]; path.append(cur)
    prof = [unkey(v)[0] for v in path]            # profiles, sites decreasing
    for j in range(len(path) - 1):
        assert valid(unkey(path[j + 1])[0], *unkey(path[j]))
    row = [w & 1 for w in prof][::-1]              # increasing site order
    def tau(x):                                    # (tau x)_i = x_i xor (x_{i+1} or x_{i+2}); loses two cells on the right
        return [x[i] ^ (x[i + 1] | x[i + 2]) for i in range(len(x) - 2)]
    y = row
    hist = [row]
    for t in range(12):
        y = tau(y); hist.append(y)
    n12 = len(hist[12])
    same12 = hist[12] == row[:n12]
    same6 = hist[6] == row[:len(hist[6])]
    fam_part = len(path) - len(right) - link
    left6 = hist[6][:fam_part - 14] == row[:fam_part - 14]
    print("S6: explicit entering configuration: right tail = 6 turns of a 10-cycle, link of", link,
          "pairs, then", fam_part, "family pairs entered at rotation index", entered)
    print("    window of", len(row), "cells: tau^12 x = x on the", n12, "checkable cells:", same12,
          "| tau^6 x = x on the whole checkable window:", same6, "| on the family part alone:", left6)
    print("    row (increasing site; the family is on the left):", "".join(map(str, row)))


if __name__ == "__main__":
    main()
