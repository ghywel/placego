# Independent re-check of certificate files written by e_slice.py / tight_run.py: every record with a tiling must use
# exactly the odd planks 1..2m-1 once each, with bin sums equal to the town; counts of impossible/unknown reported.
import json, sys, hashlib
for path in sys.argv[1:]:
    recs = json.load(open(path)); ok = bad = 0; other = {}
    for r in recs:
        m = r['m']; town = tuple(r['town'])
        if 'tiling' not in r: other[r['result']] = other.get(r['result'], 0) + 1; continue
        planks = sorted(p for b in r['tiling'] for p in b)
        if planks == list(range(1, 2*m, 2)) and sorted(sum(b) for b in r['tiling']) == sorted(town) and sum(town) == m*m and all(68 <= l <= 2*m+66 for l in town): ok += 1
        else: bad += 1
    print(f"{path.split('/')[-1]}: {len(recs)} records, valid tilings {ok}, invalid {bad}, other {other}, sha256 {hashlib.sha256(open(path,'rb').read()).hexdigest()[:16]}")
