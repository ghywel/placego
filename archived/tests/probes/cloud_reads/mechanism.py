# Cloud, CL457 (owner: "continue with the recommendation"). The one mechanism experiment: does a CANONICAL construction,
# a deterministic rule with no search, tile the real towns? Three rules, scored on every town of levels 24, 25, 31, 32 and
# on a seeded random sample of 60,000 towns at each of levels 26..30 (the towns are enumerated here; no certificate data).
#   R1 greedy:   largest plank first, to the street with the largest remaining sum that can still finish (count test), no backtracking.
#   R2 tightest: largest plank first, to the street whose remaining sum is smallest among those where the plank still fits
#                and the count test survives (fill tight streets early).
#   R3 counts:   fix each street's plank count first (its Tan-Teh minimum, then hand the spare counts two at a time to the
#                streets with the most room), then largest plank first to the street with the largest remaining
#                average need (remaining sum / remaining count) among those still needing planks, with a parity-aware
#                feasibility test; no backtracking.
import sys, random, time, json
sys.path.insert(0, 'tests/probes/cloud_reads')
from e_slice import B
from l8_certificates import towns_with_min
def planks(m): return list(range(2*m-1, 0, -2))
def count_ok(rem, suf):
    # the dynamic Tan-Teh test used by the solver: every remaining sum reachable with a parity-consistent count, counts add up
    left = len(suf); tmin_total = tmax_total = 0; small = suf[::-1]
    for r in rem:
        if r < 0: return False
        if r == 0: continue
        par = r & 1; s = t = 0; tmin = None
        for p in suf:
            s += p; t += 1
            if s >= r and (t & 1) == par: tmin = t; break
        if tmin is None: return False
        s = t = tmax = 0
        for p in small:
            if s + p > r: break
            s += p; t += 1
            if (t & 1) == par: tmax = t
        if tmax < tmin: return False
        tmin_total += tmin; tmax_total += tmax
    return tmin_total <= left <= tmax_total
def R1(m, town):
    P = planks(m); rem = list(town)
    for i, p in enumerate(P):
        best = None
        for b in sorted(range(8), key=lambda b: -rem[b]):
            if rem[b] < p: continue
            rem[b] -= p
            if count_ok(rem, P[i+1:]): best = b; break
            rem[b] += p
        if best is None: return False
    return all(r == 0 for r in rem)
def R2(m, town):
    P = planks(m); rem = list(town)
    for i, p in enumerate(P):
        best = None
        for b in sorted(range(8), key=lambda b: rem[b]):
            if rem[b] < p: continue
            rem[b] -= p
            if count_ok(rem, P[i+1:]): best = b; break
            rem[b] += p
        if best is None: return False
    return all(r == 0 for r in rem)
def R3(m, town):
    P = planks(m); rem = list(town); cnt = [B(m, l) for l in town]; spare = m - sum(cnt)
    while spare > 0:   # give two more planks to the street with the most room per plank
        b = max(range(8), key=lambda b: rem[b] / cnt[b]); cnt[b] += 2; spare -= 2
    for i, p in enumerate(P):
        best = None
        order = sorted((b for b in range(8) if cnt[b] > 0), key=lambda b: -(rem[b] / cnt[b]))
        for b in order:
            if rem[b] < p: continue
            # parity-aware local test: after taking p, the remaining cnt-1 planks must be able to make rem-p
            c = cnt[b] - 1; r = rem[b] - p; suf = P[i+1:]
            if c == 0 and r != 0: continue
            if c > 0 and (sum(suf[-c:]) > r or sum(suf[:c]) < r): continue
            rem[b] -= p; cnt[b] -= 1
            if count_ok(rem, suf): best = b; break
            rem[b] += p; cnt[b] += 1
        if best is None: return False
    return all(r == 0 for r in rem)
if __name__ == '__main__':
    random.seed(20261019); T0 = time.time(); out = {}
    for m in range(24, 33):
        alltowns = [t for l1 in range(68, 2*m+67) if 8*l1 <= m*m for t in towns_with_min(m, l1)]
        sample = alltowns if len(alltowns) <= 450000 else random.sample(alltowns, 60000)
        st = {'n': len(sample), 'R1': 0, 'R2': 0, 'R3': 0, 'any': 0}; fails3 = []
        for t in sample:
            a, b, c = R1(m, t), R2(m, t), R3(m, t)
            st['R1'] += a; st['R2'] += b; st['R3'] += c; st['any'] += (a or b or c)
            if not c and len(fails3) < 3: fails3.append(t)
        out[m] = st
        print(f"m={m}: sample {st['n']} of {len(alltowns)}: R1 greedy {st['R1']}, R2 tightest {st['R2']}, R3 counts {st['R3']}, any {st['any']}; R3 failures e.g. {fails3} ({time.time()-T0:.0f}s)", flush=True)
    json.dump(out, open(sys.argv[1], 'w')) if len(sys.argv) > 1 else None
