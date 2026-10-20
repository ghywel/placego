"""CL475 bounded test: does core row 7 need the absent bin's protection?

Row 7 on labels a, c, d:  rho_a + rho_cd <= hi_ac + hi_d   (bin b does not appear).
Relaxed domain: sizes >= 3, every K_J nonempty for the four groups used, and the baseline lower cut
t_J >= T(C_J) imposed ONLY for J inside {a, c, d}; nothing on groups containing b.
Prediction: violations exist in the relaxed domain (so b's protection is load-bearing).
Counterfactual: none, which would make row 7 a three-group scalar inequality.

OUTCOME: M = 12: 148,150 relaxed instances, 0 violations; M = 12..14: 5,275,244, 0 violations.
Prediction FAILED: b's protection is not load-bearing for row 7 in this range.  Control: dropping the
three-label cuts too (targets from L(c)) gives 34 violations at M = 12 (e.g. q3, 3333, t_a 5, t_d 3).
"""
import itertools, sys
L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2

def run(MMAX):
    viol = n = 0; ex = []
    for M in range(12, MMAX + 1):
        for ca, cc, cd in itertools.product(range(3, M), repeat=3):
            cb = M - ca - cc - cd
            if cb < 3: continue
            for q in range(1, M):
                H = M - q; S = T(M) - q
                def K(c, t):
                    v = [r for r in range(max(0, c - q), min(c, H) + 1)
                         if L(c - r) + (q + 1) * r + L(r) <= t <= (c - r) * (q - 1) - L(c - r) + M * r - L(r)]
                    return (min(v), max(v)) if v else None
                for ta in range(T(ca), S):
                    for tc in range(T(cc), S - ta):
                        for td in range(T(cd), S - ta - tc):
                            if ta + tc < T(ca + cc) or ta + td < T(ca + cd) or tc + td < T(cc + cd) \
                               or ta + tc + td < T(ca + cc + cd): continue
                            Ka, Kcd, Kac, Kd = K(ca, ta), K(cc + cd, tc + td), K(ca + cc, ta + tc), K(cd, td)
                            if None in (Ka, Kcd, Kac, Kd): continue
                            n += 1
                            if Ka[0] + Kcd[0] > Kac[1] + Kd[1]:
                                viol += 1
                                tb = S - ta - tc - td
                                if len(ex) < 3: ex.append((M, q, (ca, cb, cc, cd), (ta, tb, tc, td)))
    print('relaxed instances', n, 'row-7 violations', viol, ex)

if __name__ == '__main__':
    run(int(sys.argv[1]))
