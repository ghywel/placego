"""CL508: MI368's form for bottom-tight facets: does EVERY realization of the least-slack bottom-tight singleton or
pair leave a child in H(h') (lower family, child re-indexed to its own interval)?  Samples from kholek DUMPEVERY.
"""
import sys
from collections import Counter
from itertools import combinations
_argv_every = sys.argv; sys.argv = ["x"]
exec(open('tests/probes/cloud_reads/descent_pair.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv_every

def every(M, h, files, C=(3, 3, 3, 3, 3), stride=3):
    cnt = Counter(); ex = []; i = 0
    for f in files:
        for line in open(f):
            if not line.startswith('V'): continue
            i += 1
            if i % stride: continue
            hs, ts = line[len('V holes'):].split('|')
            H = list(map(int, hs.split())); t = list(map(int, ts.split()))
            S = [x for x in range(M + 1) if x not in H]; k = len(C)
            facets = sorted((sum(t[j] for j in J) - sum(C[j] for j in J) * (sum(C[j] for j in J) - 1) // 2
                             - h * sum(C[j] for j in J), s, J) for s in range(1, k) for J in combinations(range(k), s))
            sl, s, J = facets[0]
            if s not in (1, 2): continue
            tag = 'single' if s == 1 else 'pair'
            m = sum(C[j] for j in J); tot = sum(t[j] for j in J); good = bad = 0
            for R in combinations(S, m):
                if sum(R) != tot: continue
                if s == 2 and not splits(R, C[J[0]], t[J[0]]): continue
                rest = [x for x in S if x not in R]; a, b = rest[0], rest[-1]; hh = (b - a + 1) - len(rest)
                oth = [j for j in range(k) if j not in J]; sz = [C[j] for j in oth]; tt = [t[j] for j in oth]
                if key([u - a * c for u, c in zip(tt, sz)], sz) >= hh: good += 1
                else:
                    bad += 1
                    if len(ex) < 4: ex.append((H, t, J, R, hh))
            cnt[tag] += 1; cnt[tag + '_all_good'] += bad == 0; cnt[tag + '_realizations'] += good + bad; cnt[tag + '_bad'] += bad
    return cnt, ex

if __name__ == '__main__':
    M, h = int(sys.argv[1]), int(sys.argv[2])
    cnt, ex = every(M, h, sys.argv[3:])
    print(M, h, dict(sorted(cnt.items())), 'examples of a bad realization:', ex, flush=True)
