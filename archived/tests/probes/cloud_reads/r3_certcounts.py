"""R3 assignment stage with the certified plank counts. Usage: python3 r3_certcounts.py CERTDIR 24 25 (CERTDIR holds E<m>.json certificate files, kept outside git)."""
import json, sys
sys.path.insert(0, 'tests/probes/cloud_reads')
from mechanism import planks, count_ok, B, R3
def R3_assign(m, town, cnt):
    """R3's assignment stage with a given count vector (largest plank to the street with the largest remaining average need)."""
    P = planks(m); rem = list(town); cnt = list(cnt)
    for i, p in enumerate(P):
        best = None
        order = sorted((b for b in range(8) if cnt[b] > 0), key=lambda b: -(rem[b] / cnt[b]))
        for b in order:
            if rem[b] < p: continue
            c = cnt[b] - 1; r = rem[b] - p; suf = P[i+1:]
            if c == 0 and r != 0: continue
            if c > 0 and (sum(suf[-c:]) > r or sum(suf[:c]) < r): continue
            rem[b] -= p; cnt[b] -= 1
            if count_ok(rem, suf): best = b; break
            rem[b] += p; cnt[b] += 1
        if best is None: return False
    return all(r == 0 for r in rem)
def R3_counts(m, town):
    rem = list(town); cnt = [B(m, l) for l in town]; spare = m - sum(cnt)
    while spare > 0:
        b = max(range(8), key=lambda b: rem[b] / cnt[b]); cnt[b] += 2; spare -= 2
    return cnt
for lvl in sys.argv[2:]:
    certs = json.load(open(f"{sys.argv[1]}/E{lvl}.json"))
    n = len(certs); ok_cert = 0; same_profile = 0; ok_r3 = 0; ex = []
    for c in certs:
        m, town, til = c['m'], c['town'], c['tiling']
        assert [sum(t) for t in til] == town
        cnt = [len(t) for t in til]
        a = R3_assign(m, town, cnt); ok_cert += a
        r3c = R3_counts(m, town)
        same_profile += (sorted(zip(town, r3c)) == sorted(zip(town, cnt)))
        ok_r3 += R3(m, town)
        if not a and len(ex) < 3: ex.append((town, cnt))
    print(f'E{lvl}: towns {n}; R3 full {ok_r3}; R3 assignment with the CERTIFIED count vector {ok_cert} ({100*ok_cert/n:.1f}%); R3 count profile equals certified profile (as multiset of (street,count)) {same_profile} ({100*same_profile/n:.1f}%); assign-stage failures e.g. {ex}', flush=True)
