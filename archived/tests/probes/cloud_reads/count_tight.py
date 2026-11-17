# Count-tight towns: the sum of Tan-Teh minimal plank counts equals m (slack 0) or m-2 (slack 2). Enumerated through
# count vectors so that levels with millions of towns are never listed in full.
import sys, itertools
sys.path.insert(0, '/home/user/placego/tests/probes/cloud_reads')
from e_slice import B
def interval(m, t):
    lo = 2*m*(t-2) - (t-2)**2 + 1 if t >= 3 else 1; hi = 2*m*t - t*t
    return [l for l in range(max(lo, 68), min(hi, 2*m+66) + 1) if l % 2 == t % 2]
def tight_towns(m, slack):
    total = m - slack; tmin = B(m, 68); out = []
    for tv in itertools.combinations_with_replacement(range(tmin, total), 8):
        if sum(tv) != total: continue
        ivs = [interval(m, t) for t in tv]
        if any(not iv for iv in ivs): continue
        def rec(i, remaining, prev_t, prev_l, acc):
            if i == 8:
                if remaining == 0: out.append(tuple(acc))
                return
            for l in ivs[i]:
                if tv[i] == prev_t and l < prev_l: continue
                if l > remaining: break
                rec(i+1, remaining - l, tv[i], l, acc + [l])
        rec(0, m*m, None, None, [])
    return out
if __name__ == '__main__':
    for m in range(24, 33):
        a = tight_towns(m, 0); b = tight_towns(m, 2)
        print(f"m={m}: count-tight towns slack0 {len(a)}, slack2 {len(b)}", flush=True)
