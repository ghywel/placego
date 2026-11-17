#!/usr/bin/env python3
"""Cloud CL771/CL772: the doubling link, checked against the record.

Frame: a vertex is a pair (c, d) of P-tick profiles at sites i+1, i+2; its children are (u, c)
with u(t+1) = u(t) xor (c(t) or d(t)) cyclically; bit t of a word is tick t.  Leftward is forward.

Usage: cloud_doubling_links.py DIR   (DIR holds core1.txt .. core15.txt from cloud_core_census.c)
"""
import sys, itertools
from collections import deque

RING = ('###..#.#.#####....#...##.##.######..#.###.#.##.##..##.##...####.#.....##..###.#.#..#......####...#.#..#..'
        '###.#..##.#...#.##...#.')        # G16 at time 0, from reports/rule30-genealogy.md 29.7
pc = lambda x: bin(x).count("1")


class G:
    def __init__(s, P):
        s.P = P; s.FULL = (1 << P) - 1

    def rot(s, w, k):
        k %= s.P
        return ((w >> k) | (w << (s.P - k))) & s.FULL

    def prefix(s, m):
        w = 0; bit = 0
        for t in range(s.P - 1):
            bit ^= (m >> t) & 1; w |= bit << (t + 1)
        return w

    def children(s, v):
        c, d = v; m = c | d
        if pc(m) & 1:
            return []
        w = s.prefix(m)
        return [(w, c), (w ^ s.FULL, c)]

    def valid(s, u, c, d):
        return (u ^ s.rot(u, 1)) == (c | d)        # rot(u,1) bit t = u(t+1)

    def lift(s, w, p):                              # a p-tick word repeated to P ticks
        out = 0
        for k in range(s.P // p):
            out |= w << (k * p)
        return out

    def period(s, w):
        return min(k for k in range(1, s.P + 1) if s.P % k == 0 and s.rot(w, k) == w)

    def closure(s, start, cap=2_000_000):
        adj = {}; work = deque(start); seen = set(start)
        while work:
            v = work.popleft(); adj[v] = s.children(v)
            for x in adj[v]:
                if x not in seen:
                    seen.add(x); assert len(seen) <= cap, "NODE CAP"; work.append(x)
        return adj


def sccs(adj):
    index = {}; low = {}; onst = set(); st = []; comps = []; cnt = 0
    for root in adj:
        if root in index:
            continue
        work = [(root, 0)]; index[root] = low[root] = cnt; cnt += 1; st.append(root); onst.add(root)
        while work:
            v, i = work[-1]
            if i < len(adj[v]):
                work[-1] = (v, i + 1); x = adj[v][i]
                if x not in adj:
                    continue
                if x not in index:
                    index[x] = low[x] = cnt; cnt += 1; st.append(x); onst.add(x); work.append((x, 0))
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
    return [set(c) for c in comps if len(c) > 1 or c[0] in adj[c[0]]]


def alive_set(adj):
    """Vertices of the closure with an infinite leftward path."""
    alive = {v for v in adj if adj[v]}
    changed = True
    while changed:
        changed = False
        for v in list(alive):
            if not any(x in alive for x in adj[v]):
                alive.discard(v); changed = True
    return alive


def depth_below(adj, v, memo):
    """Longest leftward path from v inside the closure (None if it reaches a cycle)."""
    stack = [v]
    while stack:
        x = stack[-1]
        if x in memo:
            stack.pop(); continue
        pend = [y for y in adj[x] if y not in memo]
        if pend:
            stack.extend(pend); continue
        vals = [memo[y] for y in adj[x]]
        memo[x] = None if any(z is None for z in vals) else (1 + max(vals) if vals else 0)
        stack.pop()
    return memo[v]


def links_report(g, adj, p, alive, cyc, label):
    """Doubling links p -> 2p inside a closure at P = 2p: pairs of period dividing p whose drive has odd weight over p."""
    assert g.P == 2 * p
    half = (1 << p) - 1
    links = [v for v in adj if g.rot(v[0], p) == v[0] and g.rot(v[1], p) == v[1] and pc((v[0] | v[1]) & half) & 1]
    lemma = True; step2 = True; surv = 0
    memo = {v: None for v in alive}
    depths = []
    for v in links:
        ch = adj[v]
        lemma &= len(ch) == 2 and g.rot(ch[0][0], p) == ch[1][0] and ch[0][0] ^ ch[1][0] == g.FULL
        # Corrected after run 1 (kept as cloud_doubling_links_run1.out): the condition is an even number
        # of WHITE cells of the adjacent column over p, which is "even weight" only when p is even.
        even_c = (p - pc(v[0] & half)) % 2 == 0
        step2 &= all((len(adj[x]) == 2) == even_c for x in ch)
        if v in alive:
            surv += 1
        else:
            depths.append(depth_below(adj, v, memo))
    hist = {}
    for dd in depths:
        hist[dd] = hist.get(dd, 0) + 1
    print(f"   {label}: doubling links {len(links)} | children are half-shifts and complements: {lemma} | "
          f"a grandchild exists exactly when the adjacent column has an even number of white cells: {step2}")
    print(f"      links with an infinite leftward continuation: {surv} | the others die after at most "
          f"{max(depths) if depths else 0} further pairs | survival-length counts (length: links): "
          f"{dict(sorted(hist.items())[:8])}{' ...' if len(hist) > 8 else ''}")
    return links, surv


def read_core(d, P):
    out = []
    for line in open(f"{d}/core{P}.txt"):
        n = int(line); out.append((n >> P, n & ((1 << P) - 1)))
    return out


def main(d):
    # ---- the core table, P = 1..15
    print("== cores by full census (second code on LN-12's table)")
    cores = {}
    for P in range(1, 16):
        g = G(P); core = set(read_core(d, P)); cores[P] = core
        adj = {v: [x for x in g.children(v) if x in core] for v in core}
        cyc = sccs(adj)
        shape = {}
        for cm in cyc:
            e = sum(1 for v in cm for x in adj[v] if x in cm)
            shape[(len(cm), e)] = shape.get((len(cm), e), 0) + 1
        print(f"   P {P}: states {len(core)} edges {sum(len(a) for a in adj.values())} | cyclic components "
              f"(vertices, edges): count {sorted(shape.items())} | branching: {sum(1 for (n, e) in shape if e > n) > 0}")

    # ---- D6: the period-15 core
    print("== D6 the period-15 core")
    P = 15; g = G(P); core = cores[P]
    adj = {v: [x for x in g.children(v) if x in core] for v in core}
    cyc = sccs(adj); compof = {v: i for i, cm in enumerate(cyc) for v in cm}
    trans = core - set(compof)
    def reach(src):
        seen = set(src); work = list(src)
        while work:
            v = work.pop()
            for x in adj[v]:
                if x not in seen:
                    seen.add(x); work.append(x)
        return {compof[x] for x in seen if x in compof}
    info = []
    for i, cm in enumerate(cyc):
        e = sum(1 for v in cm for x in adj[v] if x in cm)
        pers = sorted({max(g.period(v[0]), g.period(v[1])) if g.period(v[0]) % g.period(v[1]) == 0 or
                       g.period(v[1]) % g.period(v[0]) == 0 else g.period(v[0]) * g.period(v[1]) for v in cm})
        out = reach(cm) - {i}
        leaves = sum(1 for v in cm for x in adj[v] if x not in cm)
        info.append((i, len(cm), e, pers, sorted(out), leaves))
    feeds = {i: [j for j, *_r in info if i in info[j][4]] for i, *_ in info}
    for i, n, e, pers, out, leaves in info:
        print(f"   component {i}: vertices {n} edges {e} branching {e > n} | pair periods {pers} | "
              f"core edges leaving it {leaves} | reaches components {out} | reached from components {feeds[i]}")
    br = [r for r in info if r[2] > r[1]]
    print(f"   transient core pairs {len(trans)} | branching components {len(br)} | all terminal: "
          f"{all(r[5] == 0 for r in br)} | each entered from another component: {all(feeds[r[0]] for r in br)}")
    R = lambda v, k: (g.rot(v[0], k), g.rot(v[1], k))
    if br:
        orb = []
        for k in range(15):
            img = {R(v, k) for v in cyc[br[0][0]]}
            orb.append([i for i, cm in enumerate(cyc) if cm == img][0])
        print("   rotation by 0..14 ticks carries the first branching component to components", orb)
        bv = sorted(v for v in cyc[br[0][0]] if sum(1 for x in adj[v] if x in cyc[br[0][0]]) > 1)
        print("   its branch vertices:", bv[:6], "count", len(bv))

    # ---- D1: T23 replay
    print("== D1 G16's exits at periods 16 and 32 (T23, genealogy 29.11)")
    y = [1 if ch == "#" else 0 for ch in RING]; m = len(y)
    mine = [y[(-i) % m] for i in range(m)]                 # mirror: my drivers sit to the right
    for P in (16, 32):
        g = G(P)
        rows = [mine]
        for _ in range(P):
            z = rows[-1]; rows.append([z[i] ^ (z[(i + 1) % m] | z[(i + 2) % m]) for i in range(m)])
        back16 = rows[16] == rows[0]; back8 = rows[8] == rows[0]
        prof = [sum(rows[t][i] << t for t in range(P)) for i in range(m)]
        g16 = {(prof[(i + 1) % m], prof[(i + 2) % m]) for i in range(m)}
        okc = all((prof[i], prof[(i + 1) % m]) in g.children((prof[(i + 1) % m], prof[(i + 2) % m])) for i in range(m))
        A = sum(1 << t for t in range(1, P, 2)); rain = {(A, A ^ g.FULL), (A ^ g.FULL, A)}
        adj = g.closure(g16)
        tree = set(adj) - g16 - rain
        entries = sum(1 for v in adj if v not in rain for x in adj[v] if x in rain)
        cyc = sccs(adj); alive = alive_set(adj)
        indeg = {}
        for v in adj:
            for x in adj[v]:
                indeg[x] = indeg.get(x, 0) + 1
        merges = sum(1 for v in tree if indeg.get(v, 0) > 1)
        memo = {v: None for v in alive}
        longest = max((depth_below(adj, v, memo) for v in tree if v not in alive), default=-1) + 1
        # longest path from the cycle through tree states, the wall into the rain included
        memo2 = {}
        def from_cycle(v):
            stack = [v]
            while stack:
                x = stack[-1]
                if x in memo2:
                    stack.pop(); continue
                kids = [z for z in adj[x] if z in tree]
                pend = [z for z in kids if z not in memo2]
                if pend:
                    stack.extend(pend); continue
                memo2[x] = 1 + max((memo2[z] for z in kids), default=0); stack.pop()
            return memo2[v]
        deep_all = max(from_cycle(x) for v in g16 for x in adj[v] if x in tree)
        print(f"   P {P}: longest path from the cycle through tree states, wall included: {deep_all} pairs")
        print(f"   P {P}: ring returns after 16 ticks {back16}, after 8 {back8} | G16 states {len(g16)} on a cycle {okc} | "
              f"tree states {len(tree)} | longest dying path {longest} pairs | edges into the rain {entries} | "
              f"cyclic components (sizes) {sorted(len(c) for c in cyc)} | tree states with two parents {merges} | "
              f"tree states with an infinite continuation {len(tree & alive)}")
        if P == 32:
            links_report(g, adj, 16, alive, cyc, "16 -> 32 from G16")

    # ---- D3: all doubling links out of the lower cores
    print("== D3 doubling links out of the complete lower core")
    for p in (1, 2, 3, 4, 5, 6, 7, 8):
        g = G(2 * p)
        start = {(g.lift(c, p), g.lift(dd, p)) for (c, dd) in cores[p]}
        adj = g.closure(start)
        cyc = sccs(adj); alive = alive_set(adj)
        newc = [cm for cm in cyc if not cm <= start]
        links, surv = links_report(g, adj, p, alive, cyc, f"{p} -> {2 * p}")
        tgt = sorted((len(cm), sum(1 for v in cm for x in adj[v] if x in cm)) for cm in newc)
        print(f"      closure {len(adj)} pairs | cyclic components not inside the period-{p} core (vertices, edges): {tgt}")
    # 16 -> 32 from the cycles of the 16 core: white, rain, G8 (lifted from the 8 core) and G16
    g = G(32)
    start = {(g.lift(c, 8), g.lift(dd, 8)) for (c, dd) in cores[8]}
    rows = [mine]
    for _ in range(32):
        z = rows[-1]; rows.append([z[i] ^ (z[(i + 1) % m] | z[(i + 2) % m]) for i in range(m)])
    prof = [sum(rows[t][i] << t for t in range(32)) for i in range(m)]
    start |= {(prof[(i + 1) % m], prof[(i + 2) % m]) for i in range(m)}
    adj = g.closure(start); cyc = sccs(adj); alive = alive_set(adj)
    links, surv = links_report(g, adj, 16, alive, cyc, "16 -> 32 from white, rain, G8 and G16")
    print(f"      closure {len(adj)} pairs | cyclic components (vertices): {sorted(len(c) for c in cyc)}")

    # ---- D4, D5: half-shift spins
    print("== D4 the period-12 branch vertices and exhaustive half-shift search")
    g = G(12); L = 6
    H = lambda z, gg=g, LL=L: z ^ gg.rot(z, LL)
    U = (1323, 2868); V = (2772, 3372)
    core = cores[12]; adj = {v: [x for x in g.children(v) if x in core] for v in core}
    cyc = sccs(adj); CU = next(cm for cm in cyc if U in cm)
    for nm, B in (("U", U), ("V", V)):
        ch = [x for x in adj[B] if x in CU]
        print(f"   {nm}: half-differences of its two columns {H(B[0])}, {H(B[1])} (overlap {H(B[0]) & H(B[1])}) | "
              f"continuing children {[x[0] for x in ch]} with weights {[pc(x[0]) for x in ch]}")

    def site_profiles(walk):                 # closed leftward walk -> profiles by site, cyclic
        q = [v[0] for v in walk[1:]]         # sites -1, -2, ..., -n
        return q[::-1]                       # increasing site order

    def first_return(b, child, comp, stops):
        path = [b, child]
        while path[-1] not in stops:
            path.append([x for x in adj[path[-1]] if x in comp][0])
        return path
    ret = {}
    for B in (U, V):
        for chd in adj[B]:
            if chd in CU:
                pth = first_return(B, chd, CU, (U, V)); ret[(B, pth[-1])] = pth

    def walk(word):
        cur = U; path = [U]
        for e in word:
            tgt = cur if e == 0 else (V if cur == U else U)
            path += ret[(cur, tgt)][1:]; cur = tgt
        assert cur == U
        return path

    def spin_analysis(gg, LL, prof):
        n = len(prof)
        Hh = lambda z: z ^ gg.rot(z, LL)
        sh = lambda z, e: gg.rot(z, LL) if e else z
        tab = []
        for s in range(n):
            u, c, dd = prof[s], prof[(s + 1) % n], prof[(s + 2) % n]
            tab.append({(a, b, e): gg.valid(sh(u, a), sh(c, b), sh(dd, e)) for a in (0, 1) for b in (0, 1) for e in (0, 1)})
        dummy = [Hh(z) == 0 for z in prof]
        # exact count of valid spin assignments with dummy spins fixed at 0 (cyclic transfer)
        total = 0
        for e0 in (0, 1):
            for e1 in (0, 1):
                if (dummy[0] and e0) or (dummy[1 % n] and e1):
                    continue
                vec = {(e0, e1): 1}
                for s in range(n):
                    nv = {}
                    for (a, b), w in vec.items():
                        for e in (0, 1):
                            if dummy[(s + 2) % n] and e:
                                continue
                            if tab[s][(a, b, e)]:
                                nv[(b, e)] = nv.get((b, e), 0) + w
                    vec = nv
                total += vec.get((e0, e1), 0)
        # the equality graph from the local classification
        edges = []
        for s in range(n):
            u, c, dd = prof[s], prof[(s + 1) % n], prof[(s + 2) % n]
            A_ = Hh(c) & ~dd & gg.FULL; B_ = Hh(dd) & ~c & gg.FULL; C_ = Hh(c) & Hh(dd); D_ = A_ ^ B_ ^ C_
            if C_:
                edges.append((s + 1, s + 2))
                if D_:
                    edges.append((s, s + 1))
            else:
                if A_:
                    edges.append((s, s + 1))
                if B_:
                    edges.append((s, s + 2))
        # check the classification against the literal table at every site
        okcls = True
        for s in range(n):
            u, c, dd = prof[s], prof[(s + 1) % n], prof[(s + 2) % n]
            A_ = Hh(c) & ~dd & gg.FULL; B_ = Hh(dd) & ~c & gg.FULL; C_ = Hh(c) & Hh(dd)
            for (a, b, e), ok in tab[s].items():
                okcls &= ok == ((((a ^ b) * A_) ^ ((a ^ e) * B_) ^ ((a ^ (b & e)) * C_)) == 0)
        # lifted components by potentials: (site residue, offset)
        nb = {}
        for (i, j) in edges:
            nb.setdefault(i % n, []).append((j % n, (j - i)))
            nb.setdefault(j % n, []).append((i % n, (i - j)))
        seenq = {}; comps = []
        for s in range(n):
            if dummy[s] or s in seenq:
                continue
            pot = {s: 0}; work = [s]; infinite = False
            while work:
                v = work.pop()
                for (x, dlt) in nb.get(v, []):
                    val = pot[v] + dlt
                    if x not in pot:
                        pot[x] = val; work.append(x)
                    elif pot[x] != val:
                        infinite = True
            for v in pot:
                seenq[v] = len(comps)
            comps.append((len(pot), infinite))
        return total, comps, sum(dummy), okcls

    for word in ((0,), (1, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)):
        prof = site_profiles(walk(word))
        total, comps, nd, okcls = spin_analysis(g, 6, prof)
        line = f"   background {''.join(map(str, word))}: period {len(prof)} cells | valid half-shift fields {total} | " \
               f"equality components (sites, infinite lift) {comps} | columns with zero half-difference {nd} | " \
               f"classification equals the literal rule at every site: {okcls}"
        if len(prof) <= 14:
            n = len(prof); cnt = 0; fields = set()
            for bits in itertools.product((0, 1), repeat=n):
                z = [g.rot(prof[s], 6) if bits[s] else prof[s] for s in range(n)]
                if all(g.valid(z[s], z[(s + 1) % n], z[(s + 2) % n]) for s in range(n)):
                    fields.add(tuple(z))
            line += f" | brute force over 2^{n} assignments: distinct valid fields {len(fields)}"
        print(line)

    print("== D5 equality graphs of every simple cycle in the cores at even periods")
    worst = []
    for P in (2, 4, 6, 8, 10, 12, 14):
        gg = G(P); core = cores[P]
        adjc = {v: [x for x in gg.children(v) if x in core] for v in core}
        tot_c = 0; finite_nd = 0; okall = True; summ = {}
        for cm in sccs(adjc):
            e = sum(1 for v in cm for x in adjc[v] if x in cm)
            if e != len(cm):
                continue                                  # branching components are handled above
            v0 = next(iter(cm)); pth = [v0]
            while True:
                nx = [x for x in adjc[pth[-1]] if x in cm][0]
                pth.append(nx)
                if nx == v0:
                    break
            prof = site_profiles(pth)
            total, comps, nd, okcls = spin_analysis(gg, P // 2, prof)
            okall &= okcls; tot_c += 1
            fin = [c for c in comps if not c[1]]
            finite_nd += len(fin)
            key = (len(cm), total, tuple(sorted(comps)))
            summ[key] = summ.get(key, 0) + 1
        print(f"   P {P}: simple cycles {tot_c} | classification equals the literal rule: {okall} | "
              f"finite field-changing components: {finite_nd} | (cycle length, valid fields, components): count "
              f"{sorted(summ.items())}")


if __name__ == "__main__":
    main(sys.argv[1])
