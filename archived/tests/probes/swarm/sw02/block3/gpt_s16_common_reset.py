"""GC2797: test one common-endpoint reset candidate, no new width.
Prediction: intersection of B-images need not reset its own A-orbit; expect
a failed B-cover by28. Counterfactual: a certified A-orbit/B-reset family.
At most20 A images per width; no enlargement on timeout/nonclosure.
"""
import json, pathlib, sys
import numpy as np
from gpt_s16_cover import read

folder, covers, out = map(pathlib.Path, sys.argv[1:])
for w in (16, 24, 26, 28):
    n, ss, tr = read(folder, w)
    selected = json.loads((covers / f"code-cover-{w}.json").read_text())["chosen"]
    common = (1 << n) - 1
    for i in selected:
        common &= ss[tr[i][1]]
    assert common
    allcore = np.array(list(map(int, (folder / f"code-core-{w}.txt").read_text().split())), dtype=np.uint64)
    bits = np.unpackbits(np.frombuffer(common.to_bytes((n+7)//8, "little"), dtype=np.uint8), bitorder="little")[:n]
    root = allcore[np.flatnonzero(bits)]
    mask = np.uint64((1 << w) - 1)

    def tick(a, centre, exterior):
        b = a | (np.uint64(exterior) << np.uint64(w))
        return (((b << np.uint64(1)) | np.uint64(centre)) ^ (b | (b >> np.uint64(1)))) & mask

    def gap(a, g):
        for k in range(1, g + 1):
            a = np.unique(np.concatenate([tick(tick(a, 0, x), 1, y) for x in (0, 1) for y in (0, 1)]))
            a = a[(a & np.uint64(1)) == np.uint64(k == g)]
        return a

    def B(a):
        for g in (3, 5, 5, 5):
            a = gap(a, g)
        return a

    orbit, seen, sizes = [], {}, []
    a = root
    result = {"width":w, "root_cardinality":int(root.size), "status":"BOUNDED_UNKNOWN"}
    for t in range(20):
        key = a.tobytes()
        if key in seen:
            result.update(status="RESET_COVER_PASS", preperiod=seen[key], period=t-seen[key])
            break
        seen[key] = t
        orbit.append(a)
        sizes.append(int(a.size))
        b = B(a)
        missing = np.setdiff1d(root, b, assume_unique=True)
        if missing.size:
            result.update(status="RESET_COVER_BROKEN", failing_A_phase=t,
                          missing_count=int(missing.size), missing_examples=list(map(int, missing[:4])))
            break
        a = gap(a, 5)
    result["A_orbit_sizes"] = sizes
    (out / f"common-reset-{w}.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result), flush=True)
print("S16_COMMON_RESET_FINISHED", flush=True)
