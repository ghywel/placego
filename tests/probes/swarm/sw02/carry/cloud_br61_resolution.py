#!/usr/bin/env python3
"""Cloud CL767: the resolution-size statements of BR-6.1, own generator and own checks.

Formula phi_h(W, T): variables x(k, t), k >= 1, t >= 0, k + t <= T + 1 (depth k, tick t).
  rule    x(k, t+1) = x(k+1, t) xor h(x(k, t), x(k-1, t)),  x(0, t) = 0   (white wall)
  units   x(1, 2s) = 1 for 2s <= T          (column 1 black at even ticks)
          x(k, 0) = 0 for W < k <= T + 1    (the row has width W)
h(b, c) = c is rule 90, b xor c is rule 150, b or c is rule 30.
Encoding P: each rule constraint by its prime implicates.
"""
import itertools, random, signal, sys, time

H = {90: lambda b, c: c, 150: lambda b, c: b ^ c, 30: lambda b, c: b | c}


def prime_implicates(nv, fn):
    """Clauses over variables 0..nv-1 implied by fn (a set of satisfying tuples), minimal ones."""
    sat = fn
    imps = []
    for size in range(1, nv + 1):
        for vs in itertools.combinations(range(nv), size):
            for signs in itertools.product((0, 1), repeat=size):
                # clause: OR of (x_v == signs_j); violated iff all x_v != signs_j
                if all(any(a[v] == s for v, s in zip(vs, signs)) for a in sat):
                    cl = frozenset(zip(vs, signs))
                    if not any(c <= cl for c in imps):
                        imps.append(cl)
    return imps


class Formula:
    def __init__(self, rule, W, T, target=None, extra=False):
        self.rule, self.W, self.T = rule, W, T
        self.var = {}
        for k in range(1, T + 2):
            for t in range(0, T + 2 - k):
                self.var[(k, t)] = len(self.var) + 1
        self.n = len(self.var)
        self.clauses = []
        h = H[rule]
        # generic constraint on (new, left, centre, right) and the wall version (right = 0)
        gen = {(n, l, c, r) for n in (0, 1) for l in (0, 1) for c in (0, 1) for r in (0, 1) if n == l ^ h(c, r)}
        wall = {(n, l, c) for n in (0, 1) for l in (0, 1) for c in (0, 1) if n == l ^ h(c, 0)}
        self.pi_gen = prime_implicates(4, gen)
        self.pi_wall = prime_implicates(3, wall)
        for (k, t), _ in list(self.var.items()):
            if (k, t + 1) not in self.var or (k + 1, t) not in self.var:
                continue
            if k == 1:
                cells = [(1, t + 1), (2, t), (1, t)]
                pis = self.pi_wall
            else:
                cells = [(k, t + 1), (k + 1, t), (k, t), (k - 1, t)]
                pis = self.pi_gen
            for cl in pis:
                self.clauses.append([self.var[cells[v]] if s else -self.var[cells[v]] for v, s in cl])
        self.n_axiom_clauses = len(self.clauses)
        for s in range(0, T // 2 + 1):
            bit = 1 if target is None else target[s]
            self.clauses.append([self.var[(1, 2 * s)] if bit else -self.var[(1, 2 * s)]])
        for k in range(W + 1, T + 2):
            self.clauses.append([-self.var[(k, 0)]])
        if extra:   # rule 150 only: the four-cell identity, as xor clauses
            assert rule == 150
            for (k, t) in list(self.var):
                if (k + 2, t) not in self.var:
                    continue
                if k == 1:
                    cells = [(3, t), (1, t + 2)]
                elif k == 2:
                    cells = [(4, t), (2, t + 2), (2, t)]
                else:
                    cells = [(k + 2, t), (k, t + 2), (k, t), (k - 2, t)]
                vs = [self.var[c] for c in cells]
                for signs in itertools.product((0, 1), repeat=len(vs)):
                    if sum(signs) % 2 == 1:      # forbid odd-parity assignments
                        self.clauses.append([-v if s else v for v, s in zip(vs, signs)])
        self.occ = {}
        for i, cl in enumerate(self.clauses):
            for l in cl:
                self.occ.setdefault(l, []).append(i)
        self.val = [0] * (self.n + 1)      # 0 unassigned, +1 true, -1 false
        self.trail = []
        self.props = 0

    def assign(self, lit):
        """Assign lit and propagate. False on conflict."""
        queue = [lit]
        while queue:
            l = queue.pop()
            v = abs(l); s = 1 if l > 0 else -1
            if self.val[v] == s:
                continue
            if self.val[v] == -s:
                return False
            self.val[v] = s; self.trail.append(v); self.props += 1
            for ci in self.occ.get(-l, ()):
                un = None; satisfied = False; cnt = 0
                for m in self.clauses[ci]:
                    vm = self.val[abs(m)]
                    if vm == 0:
                        un = m; cnt += 1
                    elif (vm > 0) == (m > 0):
                        satisfied = True; break
                if satisfied:
                    continue
                if cnt == 0:
                    return False
                if cnt == 1:
                    queue.append(un)
        return True

    def undo(self, mark):
        while len(self.trail) > mark:
            self.val[self.trail.pop()] = 0

    def root(self):
        for cl in self.clauses:
            if len(cl) == 1:
                if not self.assign(cl[0]):
                    return False
        return True

    def rk(self, k):
        """Generalised unit propagation of level k under the current assignment. False on conflict."""
        if k == 0:
            return True
        changed = True
        while changed:
            changed = False
            for v in range(1, self.n + 1):
                if self.val[v] != 0:
                    continue
                for lit in (v, -v):
                    mark = len(self.trail)
                    ok = self.assign(lit) and self.rk(k - 1)
                    self.undo(mark)
                    if not ok:
                        if not self.assign(-lit):
                            return False
                        changed = True
                        break
        return True

    def hardness(self, kmax):
        if not self.root():
            return 0
        for k in range(1, kmax + 1):
            mark = len(self.trail)
            ok = self.rk(k)
            self.undo(mark)
            if not ok:
                return k
        return None


def evolve(rule, row, T):
    """Run the wall rule from depths 1..T+1; return column 1 at ticks 0..T and the triangle."""
    h = H[rule]
    x = {(k, 0): row[k - 1] if k - 1 < len(row) else 0 for k in range(1, T + 2)}
    for t in range(0, T):
        for k in range(1, T + 1 - t):
            x[(k, t + 1)] = x[(k + 1, t)] ^ h(x[(k, t)], x[(k - 1, t)] if k > 1 else 0)
    return x


def alive(rule, row, T):
    x = evolve(rule, row, T)
    return all(x[(1, 2 * s)] == 1 for s in range(0, T // 2 + 1))


def D_brute(rule, W, cap=400):
    """max over rows of the first even tick with depth 1 white (zero boundary frame)."""
    h = H[rule]
    best = 0
    for Y in range(1 << W):
        cur = [(Y >> i) & 1 for i in range(W)]
        t = 0
        while True:
            if cur[0] == 0 and t % 2 == 0:
                break
            cur = cur + [0, 0]
            cur = [cur[i + 1] ^ h(cur[i], cur[i - 1] if i > 0 else 0) for i in range(len(cur) - 1)]
            while cur and cur[-1] == 0:
                cur.pop()
            if not cur:
                cur = [0]
            t += 1
            assert t < cap
        best = max(best, t)
    return best


def kstar(W):
    k = W + 1
    while k % 2 == 0 or k % 3 == 0:
        k += 1
    return k


def main():
    t0 = time.time()
    print("prime implicates per constraint (generic cell, wall cell):",
          {r: (len(Formula(r, 2, 2).pi_gen), len(Formula(r, 2, 2).pi_wall)) for r in (90, 150, 30)})
    print("brute-force D for W = 2..12:", {r: [D_brute(r, W) for W in range(2, 13)] for r in (90, 150, 30)})

    # Q1 rule 90
    phi = [0, 1]
    for k in range(2, 200):
        phi.append(phi[-1] ^ phi[-2])
    ok1 = True; rows = []
    for W in range(2, 41):
        D = kstar(W) - 1
        res = {}
        for T in (D - 2, D - 1, D, D + 1, D + 6):
            f = Formula(90, W, T)
            res[T] = not f.root()
            if T == D:
                props, nvars, ncl = f.props, f.n, len(f.clauses)
        row = [phi[k] if k % 2 == 1 else 0 for k in range(1, W + 1)]
        wit = alive(90, row, D - 1)
        dead = not alive(90, row, D)
        good = (res == {D - 2: False, D - 1: False, D: True, D + 1: True, D + 6: True}) and wit and dead
        ok1 &= good
        rows.append((W, D, props, nvars, ncl))
        if not good:
            print("   Q1 FAIL at W", W, res, wit, dead)
    print("Q1 rule 90, W = 2..40: unit propagation refutes exactly when T >= k* - 1, and the Fibonacci row "
          "satisfies T = k* - 2:", ok1)
    print("   (W, D, literals propagated before the conflict at T = D, variables, clauses):",
          [rows[i] for i in (0, 4, 9, 19, 29, 38)])
    print("   propagated / (T+2)^2 at T = D:", [round(r[2] / (r[1] + 2) ** 2, 3) for r in rows[::6]])

    # Q2 rule 150
    ok2 = True; up_alone = {}
    for W in range(2, 41):
        D = 2 * ((W + 1) // 2)
        up_alone[W] = not Formula(150, W, D).root()
        res = {}
        for T in (D - 2, D - 1, D, D + 1, D + 6):
            if T < 1:
                continue
            f = Formula(150, W, T, extra=True)
            res[T] = not f.root()
            if T == D:
                props150 = f.props
        want = {T: (T >= D) for T in res}
        # a satisfying row at T = D - 1, built sideways (free odd-tick bits of column 1)
        T = D - 1
        def build(free):
            C = {0: [0] * (T + 3), 1: [1 if t % 2 == 0 else free.get(t, 0) for t in range(T + 3)]}
            for k in range(1, T + 1):
                C[k + 1] = [C[k][t + 1] ^ C[k][t] ^ C[k - 1][t] for t in range(len(C[k]) - 1)]
            return [C[k][0] for k in range(1, T + 2)]
        row = build({})
        if any(row[k - 1] for k in range(W + 1, T + 2)):
            for t in range(1, T + 1, 2):
                row = build({t: 1})
                if not any(row[k - 1] for k in range(W + 1, T + 2)):
                    break
        wit = (not any(row[k - 1] for k in range(W + 1, T + 2))) and alive(150, row[:W], T)
        good = res == want and wit
        ok2 &= good
        if not good:
            print("   Q2 FAIL at W", W, res, wit)
    print("Q2 rule 150, W = 2..40: with the four-cell identity added, unit propagation refutes exactly when "
          "T >= 2*ceil(W/2), and a row satisfies T = D - 1:", ok2)
    print("   unit propagation alone refutes at T = D for W in:", [W for W in up_alone if up_alone[W]])

    # the identity from its axioms: semantic check and least resolution width
    def saturate(clauses, nv, width, targets):
        """Resolution closure with clause width <= width. Clauses are (pos, neg) bitmask pairs."""
        seen = {}
        order = []
        def add(c, par):
            if c in seen:
                return
            seen[c] = par; order.append(c)
        for c in clauses:
            add(c, None)
        i = 0
        while i < len(order):
            a = order[i]; i += 1
            for j in range(i):
                b = order[j]
                x1 = a[0] & b[1]; x2 = a[1] & b[0]
                cl = x1 | x2
                if cl == 0 or cl & (cl - 1):
                    continue          # resolve on exactly one clashing variable
                p = (a[0] | b[0]) & ~cl; n = (a[1] | b[1]) & ~cl
                if p & n:
                    continue
                if bin(p | n).count("1") > width:
                    continue
                add((p, n), (a, b))
            if all(tg in seen for tg in targets):
                break
        if not all(tg in seen for tg in targets):
            return None
        anc = set(); work = list(targets)
        while work:
            c = work.pop()
            if c in anc:
                continue
            anc.add(c)
            if seen[c]:
                work.extend(seen[c])
        return len([c for c in anc if seen[c] is not None])

    def xor_clauses(vs, rhs):
        out = []
        for signs in itertools.product((0, 1), repeat=len(vs)):
            if sum(signs) % 2 != rhs:      # assignment violating the xor: forbid it
                p = sum(1 << v for v, s in zip(vs, signs) if not s)
                n = sum(1 << v for v, s in zip(vs, signs) if s)
                out.append((p, n))
        return out
    # generic case k >= 3: cells indexed 0..8
    names = ["k+2,t", "k+1,t+1", "k+1,t", "k,t", "k,t+2", "k,t+1", "k-1,t+1", "k-1,t", "k-2,t"]
    ax = [[0, 1, 2, 3], [1, 4, 5, 6], [2, 5, 3, 7], [3, 6, 7, 8]]   # new = left + centre + right, as xor = 0
    target = [0, 4, 3, 8]
    cls = [c for a in ax for c in xor_clauses(a, 0)]
    sem = all((sum(b[i] for i in target) % 2 == 0)
              for b in itertools.product((0, 1), repeat=9)
              if all(sum(b[i] for i in a) % 2 == 0 for a in ax))
    widths = {}
    for w in range(4, 10):
        widths[w] = saturate(cls, 9, w, xor_clauses(target, 0))
        if widths[w] is not None:
            break
    print("   generic identity (k >= 3): implied by its four axioms:", sem,
          "| axiom clauses", len(cls), "| derived clauses used, by width bound:", widths)
    # k = 1: cells 3,t ; 2,t+1 ; 2,t ; 1,t ; 1,t+2 ; 1,t+1
    ax1 = [[0, 1, 2, 3], [1, 4, 5], [2, 5, 3]]
    cls1 = [c for a in ax1 for c in xor_clauses(a, 0)]
    sem1 = all(b[0] == b[4] for b in itertools.product((0, 1), repeat=6)
               if all(sum(b[i] for i in a) % 2 == 0 for a in ax1))
    widths1 = {}
    for w in range(2, 7):
        widths1[w] = saturate(cls1, 6, w, xor_clauses([0, 4], 0))
        if widths1[w] is not None:
            break
    print("   wall identity (k = 1), x(3,t) = x(1,t+2): implied:", sem1,
          "| derived clauses used, by width bound:", widths1)

    # Q3 control and Q4 hardness
    Dtab = {r: {W: D_brute(r, W) for W in (2, 4, 6, 8, 10)} for r in (90, 150, 30)}
    print("Q3 rule 30: unit propagation alone refutes at T = D(W) for W in:",
          [W for W in range(2, 13) if not Formula(30, W, D_brute(30, W)).root()])

    class Timeout(Exception):
        pass
    def handler(sig, frm):
        raise Timeout()
    signal.signal(signal.SIGALRM, handler)
    hd = {}
    for rule, Ws in ((90, (2, 4, 6, 8, 10)), (150, (2, 4, 6, 8)), (30, (2, 4, 6, 8))):
        hd[rule] = {}
        for W in Ws:
            f = Formula(rule, W, Dtab[rule][W])
            signal.alarm(150)
            try:
                hd[rule][W] = f.hardness(3)
            except Timeout:
                hd[rule][W] = "time cap"
            signal.alarm(0)
    print("Q4 hardness at T = D(W), prime encoding (None = above 3):", hd)
    print("   source's table: rule 30: 0, 1, 2, 2 (W = 2, 4, 6, 8); rule 150: 1, 2, 3, 3; rule 90: 0 throughout")

    # Added after the first run (kept as cloud_br61_resolution_run1.out): local hardness of one
    # identity step for rule 150.  Nine cells, four axioms, the three known black cells as units and
    # the conclusion negated; and the wall case k = 1.  If this is j - 1, then level-j propagation
    # forces every odd-column cell in turn, so hd(phi_150(W, T)) <= j for every W and T >= D.
    def raw(clauses, n):
        f = Formula.__new__(Formula)
        f.n = n; f.clauses = [list(c) for c in clauses]; f.occ = {}
        for i, cl in enumerate(f.clauses):
            for l in cl:
                f.occ.setdefault(l, []).append(i)
        f.val = [0] * (n + 1); f.trail = []; f.props = 0
        return f
    def lits(cs):
        return [[(v + 1) for v in range(16) if (p >> v) & 1] + [-(v + 1) for v in range(16) if (n >> v) & 1]
                for p, n in cs]
    gen_local = lits(cls) + [[5], [4], [9], [-1]]          # x(k,t+2), x(k,t), x(k-2,t) black; x(k+2,t) white
    wall_local = lits(cls1) + [[5], [-1]]                  # x(1,t+2) black; x(3,t) white
    print("   local hardness of one identity step (conclusion negated): generic", raw(gen_local, 9).hardness(5),
          "| wall", raw(wall_local, 6).hardness(5))

    # Q5 rule 90, arbitrary target word
    rng = random.Random(20261110)
    ok5 = True; tested = 0; real_n = 0
    for W in (4, 7, 10):
        T = 2 * W + 4
        realised = set()
        for Y in range(1 << W):
            x = evolve(90, [(Y >> i) & 1 for i in range(W)], T)
            realised.add(tuple(x[(1, 2 * s)] for s in range(T // 2 + 1)))
        targets = list(realised) + [tuple(rng.randrange(2) for _ in range(T // 2 + 1)) for _ in range(300)]
        for g in targets:
            f = Formula(90, W, T, target=g)
            refuted = not f.root()
            tested += 1; real_n += g in realised
            if refuted != (g not in realised):
                ok5 = False
    print("Q5 rule 90, arbitrary target words: unit propagation refutes exactly the unrealised targets:",
          ok5, "| targets tested", tested, "of which realised", real_n)
    print("seconds", round(time.time() - t0, 1))


if __name__ == "__main__":
    main()
