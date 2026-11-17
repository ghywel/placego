# edge_shift_model.py, Cloud, 2026-11-02 (Block 27, DQ-024): the fair-except-forced chain for the doubling letters, and the
# aggregation of edge_shift_tree.c outputs. Model: letters are fair coins except that the forward word 11(01)^k is always followed
# by 0 (the forced family of the descent calculus). Five states: F (forced 0 pending), H (just after the forced 0), Z (after 00 or at
# the start), A (a free 1 after a 0), B (a free 0 after A). Exact stationary weights by linear algebra, a replay by simulation, the
# conditional rates after given suffixes, and the aggregation of the tree outputs: identity failures, forced-word occurrences,
# free-leaf classes with their doubling frequencies. Usage: python3 edge_shift_model.py [tree.out ...]
import sys, random, collections
from fractions import Fraction as Fr
# exact stationary distribution: states F,H,Z,A,B; transitions (prob, next, emitted letter)
T = {'F': [(Fr(1), 'H', 0)],
     'H': [(Fr(1,2), 'F', 1), (Fr(1,2), 'Z', 0)],
     'Z': [(Fr(1,2), 'A', 1), (Fr(1,2), 'Z', 0)],
     'A': [(Fr(1,2), 'F', 1), (Fr(1,2), 'B', 0)],
     'B': [(Fr(1,2), 'A', 1), (Fr(1,2), 'Z', 0)]}
S = list(T)
# solve pi = pi P by power iteration in exact arithmetic (chain is aperiodic? F->H->F has period 2 risk; use averaging)
pi = {s: Fr(1, len(S)) for s in S}
for _ in range(400):
    new = {s: Fr(0) for s in S}
    for s in S:
        for p, t, _l in T[s]: new[t] += pi[s]*p
    pi = {s: (pi[s]+new[s])/2 for s in S}
dens = sum(pi[s]*p*l for s in S for p, t, l in T[s])
print("stationary (approx exact):", {s: float(pi[s]) for s in S}, " density", float(dens))
print("hand: weights F,H,Z,A,B = 2,2,3,2,1 over 10, density 2/5; no_three alone: 3/7 =", 3/7)
rng = random.Random(20261102)
n = 10_000_000
def simulate(forced_family=True):
    hist = ''; ones = 0; suffix_counts = collections.Counter(); suffix_ones = collections.Counter()
    watch = ['101', '0101', '10101', '00101', '1011', '110101', '11', '001', '0', '1', '01', '10', '00']
    seq = []
    state = 'Z'
    for i in range(n):
        if state == 'F': letter = 0
        else: letter = rng.getrandbits(1)
        # record conditionals on the suffix before this letter
        h = ''.join(map(str, seq[-8:]))
        for w in watch:
            if h.endswith(w): suffix_counts[w] += 1; suffix_ones[w] += letter
        seq.append(letter); ones += letter
        if len(seq) > 16: del seq[0]
        # transition
        if state == 'F': state = 'H'
        elif state == 'H': state = 'F' if letter else 'Z'
        elif state == 'Z': state = 'A' if letter else 'Z'
        elif state == 'A': state = 'F' if letter else 'B'
        elif state == 'B': state = 'A' if letter else 'Z'
    print(f"simulation n={n}: density {ones/n:.4f}")
    for w in watch:
        c = suffix_counts[w]; print(f"  P(1 | ...{w}) = {suffix_ones[w]/c:.4f}  (n={c})")
simulate()
# aggregation of tree outputs
if len(sys.argv) > 1:
    rows = []
    for fn in sys.argv[1:]:
        seed = None
        for line in open(fn):
            if line.startswith('# seed='): seed = line.split()[1][5:]; continue
            if line.startswith('#') or line.startswith('j ') or line.startswith('DONE') or not line.strip(): continue
            f = line.split(); rows.append((seed, int(f[0]), int(f[1]), int(f[2]), f[3], f[4], int(f[5]), int(f[6]), int(f[7]), int(f[8]), f[9]))
    print(f"\nrows {len(rows)} from {len(sys.argv)-1} file(s); seeds {len(set(r[0] for r in rows))}")
    checked = [r for r in rows if r[10] in ('ok', 'FAIL')]; fails = [r for r in checked if r[10] == 'FAIL']
    print(f"P1 identities checked {len(checked)} (j >= 3), failures {len(fails)}", fails[:5])
    leaves = collections.Counter(r[5] for r in rows); print("leaf types:", dict(leaves))
    # forced leaves: value always equals d_j (that is the identity); list forced words with their constants
    forced = collections.Counter((r[4], r[8]) for r in rows if r[5] == 'FORCED')
    print("forced (backward word, constant K): count")
    for (w, k), c in sorted(forced.items(), key=lambda x: (len(x[0][0]), x[0][0], x[0][1])): print(f"  {w:>12} K={k}: {c}")
    # P2: forward 110101 ending at j-1 with L_(j-4) >= 16 -> d_j = 0
    byseed = collections.defaultdict(dict)
    for r in rows: byseed[r[0]][r[1]] = r
    occ = 0; bad = []
    for s, dd in byseed.items():
        for j, r in dd.items():
            if all(k in dd for k in range(j-6, j)) and ''.join(str(dd[k][3]) for k in range(j-6, j)) == '110101' and dd[j-4][2] >= 4:
                occ += 1
                if r[3] != 0: bad.append((s, j))
    print(f"P2: forward 110101 with e_(j-4) >= 4: {occ} occurrences, followed by 1 in {len(bad)} {bad[:5]}")
    # P3: free leaves by (leaf, backward word), n >= 13 (past the universal start)
    cls = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        if r[5] in ('FREE_G', 'SMALL_G', 'SMALL_R', 'DEEP', 'BOTTOM') and r[1] >= 13:
            k = (r[5], r[4]); cls[k][0] += 1; cls[k][1] += r[3]
    print("P3 free-leaf classes (n >= 13): leaf, backward word, n, doubling frequency")
    viol = 0
    for k, (c, o) in sorted(cls.items(), key=lambda x: -x[1][0]):
        f = o/c; flag = ''
        if c >= 100 and abs(f-0.5) > 0.10: flag = ' <-- P3 FAIL'; viol += 1
        elif 30 <= c < 100 and abs(f-0.5) > 0.18: flag = ' <-- P3 FAIL'; viol += 1
        if c >= 10: print(f"  {k[0]:8} {k[1]:>12} n={c:5d} f={f:.3f}{flag}")
    print("P3 violations:", viol)
    # P4: pooled density n = 13..56 and the model's conditionals on the data
    sel = [r for r in rows if 13 <= r[1] <= 56]
    dsum = sum(r[3] for r in sel); print(f"P4 pooled density n=13..56: {dsum/len(sel):.4f} (n={len(sel)}, binomial se {(0.25/len(sel))**0.5:.4f}); model 2/5")
    for w in ['101', '0101', '10101', '00101', '1011', '110101', '11', '001', '01', '0']:
        c = o = 0
        for s, dd in byseed.items():
            for j, r in dd.items():
                if j < 13 or j > 56: continue
                L = len(w)
                if all(k in dd for k in range(j-L, j)) and ''.join(str(dd[k][3]) for k in range(j-L, j)) == w: c += 1; o += r[3]
        if c: print(f"  data P(1 | ...{w}) = {o/c:.3f} (n={c})")
