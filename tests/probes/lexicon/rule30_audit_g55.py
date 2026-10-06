"""rule30_audit_g55.py: Local's check of GPT's G55 (prime-ring quotient cycle lifting), the second reader's companion
to an argument audit, independent of GPT's RQ controls. On the prime rings p = 5, 7, 11, 13, 17, 19 it computes every
temporal cycle of Rule 30, and for each a representative x, the least q with F^q(x) a rotation R^b(x), and checks
G55's lifting law: the cycle's length is q when b = 0 (and then there are p such cycles with the same quotient cycle)
and p*q when b != 0. It also checks the census's distinct-length cases against G55's criterion. (Local, 2026-10-06;
PROOFS.md G55 note; chat L027.)

COMMAND:    python3 tests/probes/lexicon/rule30_audit_g55.py      (about a minute)
OUTCOME, 2026-10-06: ALL CHECKS PASS. Every cycle obeys the lifting law on p = 5, 7, 11, 13, 17, 19; the zero-displacement
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
