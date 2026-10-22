# Projective plane PG(2,q) over GF(q) for q in {2,3,4,5,7,8,9,11,13,16,17,19}, and the polarity (Erdos-Renyi) graph ER_q.
import itertools

IRRED = {4: (2, [1, 1]), 8: (2, [1, 1, 0]), 9: (3, [2, 0]), 16: (2, [1, 1, 0, 0]), 25: (5, [2, 0])}
# IRRED[q] = (p, coeffs c) meaning x^k = c0 + c1 x + ... (mod p), k = len(c)

class GF:
    def __init__(self, q):
        self.q = q
        if q in IRRED:
            p, c = IRRED[q]
            k = len(c)
            self.p, self.k = p, k
            els = list(itertools.product(range(p), repeat=k))
            self.idx = {e: i for i, e in enumerate(els)}
            self.els = els
            n = len(els)
            self.addt = [[self.idx[tuple((a[i] + b[i]) % p for i in range(k))] for b in els] for a in els]
            def mul(a, b):
                r = [0] * (2 * k - 1)
                for i in range(k):
                    for j in range(k):
                        r[i + j] = (r[i + j] + a[i] * b[j]) % p
                for d in range(2 * k - 2, k - 1, -1):
                    co = r[d]
                    if co:
                        r[d] = 0
                        for i in range(k):
                            r[d - k + i] = (r[d - k + i] + co * c[i]) % p
                return tuple(r[:k])
            self.mult = [[self.idx[mul(a, b)] for b in els] for a in els]
        else:
            p = q
            self.p, self.k = p, 1
            self.addt = [[(a + b) % p for b in range(p)] for a in range(p)]
            self.mult = [[(a * b) % p for b in range(p)] for a in range(p)]
        # element 0 is the zero, element 1 is one (true for both constructions: idx of (1,0,..) is 1? check)
        if q in IRRED:
            self.zero = self.idx[tuple([0] * self.k)]
            self.one = self.idx[tuple([1] + [0] * (self.k - 1))]
        else:
            self.zero, self.one = 0, 1

def plane(q):
    F = GF(q)
    Z, O = F.zero, F.one
    els = list(range(q))
    pts = []
    for a in els:
        for b in els:
            pts.append((O, a, b))
    for a in els:
        pts.append((Z, O, a))
    pts.append((Z, Z, O))
    def dot(u, v):
        s = Z
        for i in range(3):
            s = F.addt[s][F.mult[u[i]][v[i]]]
        return s
    n = len(pts)
    adj = [[j for j in range(n) if dot(pts[i], pts[j]) == Z] for i in range(n)]  # includes i itself if absolute
    absolute = [i in adj[i] for i in range(n)]
    nbr = [[j for j in adj[i] if j != i] for i in range(n)]
    return pts, adj, absolute, nbr

if __name__ == '__main__':
    for q in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16]:
        pts, line, ab, nbr = plane(q)
        n = len(pts)
        # checks: each line has q+1 points; two points on exactly one common line; #absolute = q+1
        assert n == q * q + q + 1
        assert all(len(l) == q + 1 for l in line)
        cnt = sum(ab)
        # C4-free check of ER_q: any two vertices have <= 1 common neighbour
        S = [set(x) for x in nbr]
        bad = 0
        for i in range(n):
            for j in range(i + 1, n):
                if len(S[i] & S[j]) > 1:
                    bad += 1
        print(q, n, 'absolute', cnt, 'C4 violations', bad, 'degrees', sorted(set(len(x) for x in nbr)))
