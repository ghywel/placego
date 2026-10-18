# Solve every count-tight (slack 0) town at the given levels; write certificates outside git.
import sys, json, time, hashlib
sys.path.insert(0, '/home/user/placego/tests/probes/cloud_reads')
from e_slice import solve, B
from count_tight import tight_towns
levels = [int(x) for x in sys.argv[1].split(',')]; out = sys.argv[2]; cap = float(sys.argv[3]) if len(sys.argv) > 3 else 60.0
T0 = time.time(); results = []
for m in levels:
    towns = tight_towns(m, 0); st = {'tiled': 0, 'impossible': 0, 'unknown': 0}; worst = 0; slow = []
    for t in towns:
        bins, dt, nodes = solve(m, list(t), cap=cap); worst = max(worst, dt)
        if bins is None: st['unknown'] += 1; results.append({'m': m, 'town': t, 'result': 'unknown'}); slow.append(t)
        elif bins is False: st['impossible'] += 1; results.append({'m': m, 'town': t, 'result': 'impossible', 'nodes': nodes}); print("IMPOSSIBLE", m, t, flush=True)
        else: st['tiled'] += 1; results.append({'m': m, 'town': t, 'tiling': bins})
    print(f"m={m}: {len(towns)} count-tight towns: {st}; worst {worst:.1f}s; unknown {slow[:5]} ({time.time()-T0:.0f}s)", flush=True)
json.dump(results, open(out, 'w')); print("sha256", hashlib.sha256(open(out, 'rb').read()).hexdigest()[:16], len(results), "records")
