"""rule30_audit_g55.py: Local's check of GPT's G55 (prime-ring quotient cycle lifting), the second reader's companion
to an argument audit, independent of GPT's RQ controls. On the prime rings p = 5, 7, 11, 13, 17, 19 it computes every
temporal cycle of Rule 30, and for each a representative x, the least q with F^q(x) a rotation R^b(x), and checks
G55's lifting law: the cycle's length is q when b = 0 (and then there are p such cycles with the same quotient cycle)
and p*q when b != 0. It also checks the census's distinct-length cases against G55's criterion. (Local, 2026-10-06;
PROOFS.md G55 note; chat L027.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g55.py      (about a minute)
OUTCOME, 2026-10-06: ALL CHECKS PASS (G56 part added the same day: theta(Rx) = theta(x) + 1 everywhere; phase sums = direct
  displacements; (q, b) = (4, 0), (9, 5) at 7, (14, 8), (17, 0) at 11, (7, 12), (19, 5), (20, 2), (64, 4) at 13). Every cycle obeys the lifting law on p = 5, 7, 11, 13, 17, 19; the zero-displacement
  families are exactly 7 (seven 4-cycles) and 11 (eleven 17-cycles); the criterion matches distinctness at every p.
"""
def step(x, n, mask):
    l = ((x << 1) | (x >> (n - 1))) & mask; r = ((x >> 1) | (x << (n - 1))) & mask
    return (l ^ (x | r)) & mask
def rot(x, n, mask): return ((x << 1) | (x >> (n - 1))) & mask
fails = 0
for p in (5, 7, 11, 13, 17, 19):
    mask = (1 << p) - 1; seen = bytearray(1 << p); cycles = []
    for s in range(1 << p):
        if seen[s]: continue
        path, x = {}, s
        while x not in path and not seen[x]:
            path[x] = len(path); x = step(x, p, mask)
        if x in path:
            cyc = [y for y, i in path.items() if i >= path[x]]
            cycles.append(cyc)
        for y in path: seen[y] = 1
    lifts = []
    for cyc in cycles:
        x = cyc[0]; L = len(cyc)
        if x == 0: continue
        orbit = {}; y = x
        for b in range(p): orbit[y] = b; y = rot(y, p, mask)
        z, q = step(x, p, mask), 1
        while z not in orbit: z = step(z, p, mask); q += 1
        b = orbit[z]
        expect = q if b == 0 else p * q
        fails += L != expect
        lifts.append((L, q, b != 0))
    lengths = sorted(L for L, _, _ in lifts)
    distinct = len(lengths) == len(set(lengths))
    crit = all(nz for _, _, nz in lifts) and len({q for _, q, _ in lifts}) == len(lifts)
    fails += distinct != crit
    print(f"p = {p}: {len(cycles)} cycles; (length, quotient q, displaced) = {sorted(lifts, reverse=True)[:6]}; distinct lengths {distinct}, G55 criterion {crit}")
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
# G55 addendum (added 2026-10-06): on every travelling cycle at p = 13, black counts are equal at all sites, and
# for odd lengths they cannot be half the length. The actual counts, which the addendum did not measure.
p = 13; mask = (1 << p) - 1; seen = bytearray(1 << p); cyc_all = []
for s in range(1 << p):
    if seen[s]: continue
    path, x = {}, s
    while x not in path and not seen[x]:
        path[x] = len(path); x = step(x, p, mask)
    if x in path: cyc_all.append([y for y, i in path.items() if i >= path[x]])
    for y in path: seen[y] = 1
rows = []
for cyc in cyc_all:
    if cyc[0] == 0: continue
    counts = [sum((y >> site) & 1 for y in cyc) for site in range(p)]
    eq = len(set(counts)) == 1
    fails += not eq
    rows.append((len(cyc), counts[0], round(counts[0] / len(cyc), 4), eq))
print("G55 addendum, p = 13: (length, black count per site, frequency, equal at all sites):", sorted(rows, reverse=True))
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
# G56 (added 2026-10-06): the moment phase theta(x) = m(x) w(x)^-1 mod p. Check theta(Rx) = theta(x) + 1 on every
# nonconstant state, and that summing e_j = theta(F(x_j)) over a quotient cycle of theta-0 representatives gives the
# displacement b found directly; report (q, b) at p = 7, 11 against GPT's G024 values.
def theta(x, p):
    w = bin(x).count("1"); m = sum(i for i in range(p) if (x >> i) & 1) % p
    return (m * pow(w, -1, p)) % p
def rotk(x, p, mask, k):
    for _ in range(k % p): x = rot(x, p, mask)
    return x
report = {}
for p in (5, 7, 11, 13):
    mask = (1 << p) - 1
    for x in range(1, mask):
        fails += theta(rot(x, p, mask), p) != (theta(x, p) + 1) % p
    qmap = {}                                               # quotient map on theta-0 representatives, with e
    for x in range(1, mask):
        if theta(x, p) != 0: continue
        z = step(x, p, mask)
        if z == 0 or z == mask: qmap[x] = (None, 0); continue
        e = theta(z, p); qmap[x] = (rotk(z, p, mask, -e), e)
    done = set(); qb = []
    for x0 in qmap:
        if x0 in done: continue
        order, y = {}, x0
        while y is not None and y not in order and y not in done:
            order[y] = len(order); y = qmap[y][0]
        if y is not None and y in order:                     # a new quotient cycle starting at y
            cyc, v = [], y
            while True:
                cyc.append(v); v = qmap[v][0]
                if v == y: break
            q = len(cyc); b = sum(qmap[v][1] for v in cyc) % p
            z = y
            for _ in range(q): z = step(z, p, mask)
            orb = {}; t = y
            for k in range(p): orb[t] = k; t = rot(t, p, mask)
            fails += orb.get(z, -1) != b
            qb.append((q, b))
        done.update(order)
    report[p] = sorted(qb)
print("G56: theta(Rx) = theta(x) + 1 and sum of phase increments = direct displacement; (q, b) by p:", report)
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
# G57 (added 2026-10-06): w(y) = 3w - C, m(y) = 3m - D (mod p), delta = (C m - D w)/(w w(y)) (mod p), and the
# numerator's rotation invariance, on every state of the prime rings 5, 7, 11, 13 whose successor is nonconstant.
bad57 = n57 = 0
for p in (5, 7, 11, 13):
    mask = (1 << p) - 1
    for x in range(1, mask):
        y = step(x, p, mask)
        if y in (0, mask): continue
        xs = [(x >> i) & 1 for i in range(p)]
        T = [xs[i] * xs[(i + 1) % p] for i in range(p)]
        H = [xs[(i - 1) % p] * (xs[i] | xs[(i + 1) % p]) for i in range(p)]
        E = [T[i] + 2 * H[i] for i in range(p)]
        C = sum(E); D = sum(i * E[i] for i in range(p)) % p
        w = sum(xs); m = sum(i * xs[i] for i in range(p)) % p
        wy = bin(y).count("1"); my = sum(i for i in range(p) if (y >> i) & 1) % p
        bad57 += wy != 3 * w - C
        bad57 += my != (3 * m - D) % p
        bad57 += (theta(y, p) - theta(x, p)) % p != ((C * m - D * w) * pow(w * wy, -1, p)) % p
        xr = rot(x, p, mask); xrs = [(xr >> i) & 1 for i in range(p)]
        Er = [xrs[i] * xrs[(i + 1) % p] + 2 * xrs[(i - 1) % p] * (xrs[i] | xrs[(i + 1) % p]) for i in range(p)]
        Dr = sum(i * Er[i] for i in range(p)) % p; mr = sum(i * xrs[i] for i in range(p)) % p
        bad57 += (C * mr - Dr * w) % p != (C * m - D * w) % p
        n57 += 1
fails += bad57
print("G57: weight, moment, phase-increment identities and rotation invariance on", n57, "states (p = 5, 7, 11, 13): failures", bad57)
print("ALL CHECKS PASS" if fails == 0 else f"{fails} CHECK(S) FAILED")
