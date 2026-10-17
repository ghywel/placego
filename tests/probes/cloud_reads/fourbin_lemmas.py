# Independent statement checks for GPT's four-bin SS3 candidate (MI333, MI336, MI337, MI339) on small parameters.
import itertools, sys, time
def L(r): return r*(r-1)//2
def spectrum(P, r): return {sum(c) for c in itertools.combinations(P, r)}
def gaps(P, r):
    S = spectrum(P, r); lo, hi = min(S), max(S); return sorted(set(range(lo, hi+1)) - S), lo, hi
if __name__ == "__main__":
    t0 = time.time()
    # S1 (MI333): one-hole pool {0..M}\{q}; r-subset spectrum misses at most min+1 (iff q == r) and max-1 (iff q == M-r), 2<=r<=M-2
    bad = []; cnt = 0
    for M in range(4, 15):
        for q in range(0, M+1):
            P = [x for x in range(M+1) if x != q]
            for r in range(2, M-1):
                g, lo, hi = gaps(P, r); cnt += 1
                allowed = set(); 
                if q == r: allowed.add(lo+1)
                if q == M-r: allowed.add(hi-1)
                if set(g) - allowed or (q == r and lo+1 not in g and r >= 2) : bad.append((M, q, r, g))
    print("S1 one-hole spectra:", cnt, "checks; violations", bad[:4], f"({time.time()-t0:.0f}s)")
    # S2 (MI336): two deleted values, r and complement size c >= 3: omissions only among min+1,min+2,max-1,max-2
    bad = []; cnt = 0
    for V in range(7, 14):
        for q1, q2 in itertools.combinations(range(V+1), 2):
            P = [x for x in range(V+1) if x not in (q1, q2)]
            for r in range(3, len(P)-2):
                g, lo, hi = gaps(P, r); cnt += 1
                if set(g) - {lo+1, lo+2, hi-1, hi-2}: bad.append((V, q1, q2, r, g))
    print("S2 two-hole spectra:", cnt, "checks; violations", bad[:4])
    # S3 (MI337): R = {0..V}\{p,p+1,V-1}, u = V-p-2, r+c = p+u, r,c>=3: gaps only min+1/+2 if r==p, max-1/-2 if r==u, min+3 if (u==4,c==3), max-3 if (u==4,r==3)
    bad = []; cnt = 0
    for V in range(8, 16):
        for p in range(1, V-2):
            R = [x for x in range(V+1) if x not in (p, p+1, V-1)]; u = V-p-2
            if u < 1: continue
            for r in range(3, len(R)-2):
                c = len(R) - r
                if c < 3: continue
                g, lo, hi = gaps(R, r); cnt += 1
                allowed = set()
                if r == p: allowed |= {lo+1, lo+2}
                if r == u: allowed |= {hi-1, hi-2}
                if u == 4 and c == 3: allowed.add(lo+3)
                if u == 4 and r == 3: allowed.add(hi-3)
                if set(g) - allowed: bad.append((V, p, r, g, sorted(allowed)))
    print("S3 structured three-hole spectra:", cnt, "checks; violations", bad[:4])
    # S4 (MI337 theorem): one-hole pool, three bins sizes>=3, targets totaling sum(P): partition exists iff each target in its own singleton spectrum
    def exists3(P, sizes, targets):
        P = sorted(P); k = 3; rem_c = list(sizes); rem_s = list(targets)
        def rec(i):
            if i == len(P): return all(x == 0 for x in rem_c)
            x = P[i]; tried = set()
            for b in range(k):
                key = (rem_c[b], rem_s[b])
                if rem_c[b] == 0 or rem_s[b] < x or key in tried: continue
                tried.add(key); rem_c[b] -= 1; rem_s[b] -= x
                if rec(i+1): return True
                rem_c[b] += 1; rem_s[b] += x
            return False
        return rec(0)
    bad = []; cnt = 0; feas = 0
    for M in range(9, 13):
        for q in range(0, M+1):
            P = [x for x in range(M+1) if x != q]; tot = sum(P)
            specs = {r: spectrum(P, r) for r in range(3, M-5)}
            for sizes in itertools.combinations_with_replacement(range(3, M-5), 3):
                if sum(sizes) != M: continue
                for ta in specs[sizes[0]]:
                    for tb in specs[sizes[1]]:
                        tc = tot - ta - tb
                        if tc not in specs[sizes[2]]: continue
                        if sizes[0] == sizes[1] and ta > tb: continue
                        if sizes[1] == sizes[2] and tb > tc: continue
                        cnt += 1
                        if not exists3(P, sizes, (ta, tb, tc)): bad.append((M, q, sizes, (ta, tb, tc)))
    print("S4 one-hole three-bin theorem: individually-feasible targets", cnt, "; no partition", len(bad), bad[:4], f"({time.time()-t0:.0f}s)")
    # S5 (MI339): staircase boundary. sizes a,b,c,d>=3, N=a+b+c+d, 0<=h<min(ab,cd): P = {0..p-1} u {p+2j+1+[j>=s-t]}, s,t from h=T_s+t (0<=t<=s), p=m-s, m=a+b.
    # check sum(P)=L(m)+h, a-spectrum of P contains [L(a)+h, L(a)+ab], and the reflected complement Q' has c-spectrum containing [L(c)+h, L(c)+cd].
    def staircase(m, h):
        s = 0
        while (s+1)*(s+2)//2 <= h: s += 1
        t = h - s*(s+1)//2; assert 0 <= t <= s
        p = m - s
        return sorted(list(range(p)) + [p + 2*j + 1 + (1 if j >= s - t else 0) for j in range(s)])
    bad = []; cnt = 0
    for N in range(12, 19):
        for a, b, c, d in itertools.product(range(3, N), repeat=4):
            if a + b + c + d != N or a > b or c > d: continue
            m = a + b
            for h in range(0, min(a*b, c*d)):
                P = staircase(m, h); cnt += 1
                if len(P) != m or len(set(P)) != m or max(P) > N - 1 or sum(P) != L(m) + h: bad.append(("shape", N, (a,b,c,d), h, P)); continue
                Q = [x for x in range(N) if x not in set(P)]; Qr = sorted(N - 1 - x for x in Q)
                SA = spectrum(P, a); SC = spectrum(Qr, c)
                if not set(range(L(a)+h, L(a)+a*b+1)) <= SA: bad.append(("A", N, (a,b,c,d), h))
                if not set(range(L(c)+h, L(c)+c*d+1)) <= SC: bad.append(("C", N, (a,b,c,d), h))
    print("S5 staircase boundary:", cnt, "(sizes,h) cases; violations", len(bad), bad[:4], f"({time.time()-t0:.0f}s)")
