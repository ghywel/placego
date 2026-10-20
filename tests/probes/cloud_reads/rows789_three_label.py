"""CL475 bounded test: core rows 7-9 written on three labels, under protection inside those labels only.

With hi_J = H - rho_(J^c), each crossing row has a form that omits one label:
  row 7:  rho_x + rho_yz        <= hi_xy + hi_z
  row 8:  rho_xy + rho_xz       <= 2 hi_x + hi_yz
  row 9:  2 rho_x + rho_yz      <= hi_xy + hi_xz      (GPT's corrected row 9, rho_24 = H - hi_13)
Domain: sizes >= 3 for x, y, z and the absent bin, every hole, baseline cuts t_J >= T(C_J) only for J
inside {x, y, z}, all seven K_J nonempty.  Every labelling is covered by looping over ordered sizes and
targets.  Prediction: 0 violations of each row.  Counterfactual: a violation means the absent bin's
protection is needed for that row.

OUTCOME (M = 12..13): 974,909 instances, violations 0 / 0 / 0.  Tight in 10,026 / 10,910 / 11,976.
(A pattern seen in tight cases, some bin with a pure end, has a 97% base rate: no signal.)
"""
import itertools, sys
L = lambda n: n * (n - 1) // 2
T = lambda n: n * (n + 1) // 2

def run(MMAX):
    n = 0; viol = [0, 0, 0]; ex = []
    for M in range(12, MMAX + 1):
        for cx, cy, cz in itertools.product(range(3, M), repeat=3):
            if M - cx - cy - cz < 3: continue
            for q in range(1, M):
                H = M - q; S = T(M) - q; memo = {}
                def K(c, t):
                    if (c, t) not in memo:
                        v = [r for r in range(max(0, c - q), min(c, H) + 1)
                             if L(c - r) + (q + 1) * r + L(r) <= t <= (c - r) * (q - 1) - L(c - r) + M * r - L(r)]
                        memo[(c, t)] = (min(v), max(v)) if v else None
                    return memo[(c, t)]
                for tx in range(T(cx), S):
                    for ty in range(T(cy), S - tx):
                        for tz in range(T(cz), S - tx - ty):
                            if tx + ty < T(cx + cy) or tx + tz < T(cx + cz) or ty + tz < T(cy + cz) \
                               or tx + ty + tz < T(cx + cy + cz): continue
                            G = {'x': K(cx, tx), 'y': K(cy, ty), 'z': K(cz, tz), 'xy': K(cx + cy, tx + ty),
                                 'xz': K(cx + cz, tx + tz), 'yz': K(cy + cz, ty + tz), 'xyz': K(cx + cy + cz, tx + ty + tz)}
                            if None in G.values(): continue
                            n += 1
                            r = lambda k: G[k][0]; h = lambda k: G[k][1]
                            rows = (r('x') + r('yz') - h('xy') - h('z'),
                                    r('xy') + r('xz') - 2 * h('x') - h('yz'),
                                    2 * r('x') + r('yz') - h('xy') - h('xz'))
                            for i, v in enumerate(rows):
                                if v > 0:
                                    viol[i] += 1
                                    if len(ex) < 6: ex.append((i + 7, M, q, (cx, cy, cz), (tx, ty, tz)))
    print('instances', n, 'violations row7/row8/row9', viol, ex)

if __name__ == '__main__':
    run(int(sys.argv[1]))
