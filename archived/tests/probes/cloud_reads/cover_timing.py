# Size the "finite base certificate" route: unrestricted exact cover of the odds 1..55 into 8 bins with prescribed sums
# (no cardinality model, no anchors, no cycles), timed on B57's uniform 2,000-rank sample of ALL E28 (mixed parity).
import json, sys, time
rows = [r['targets'] for r in json.load(open(sys.argv[1]))['groups'][1]['rows']]
ODDS = list(range(55, 0, -2))   # descending
def solve(targets, cap_nodes=2_000_000):
    rem = list(targets); nodes = 0
    tot_after = [0]*(len(ODDS)+1)
    for i in range(len(ODDS)-1, -1, -1): tot_after[i] = tot_after[i+1] + ODDS[i]
    def rec(i):
        nonlocal nodes
        nodes += 1
        if nodes > cap_nodes: raise TimeoutError
        if i == len(ODDS): return all(r == 0 for r in rem)
        x = ODDS[i]
        # feasibility: every bin's remainder must be 0 or >= next smallest token... (odd tokens: remainder parity handled by sum)
        tried = set()
        for b in range(8):
            r = rem[b]
            if r < x or r in tried: continue
            tried.add(r)          # bins with equal remainders are interchangeable
            rem[b] = r - x
            # prune: total remaining must equal remaining tokens' sum (always true), and no bin may need exactly 2 or any even remainder?
            # remainder parity: an odd remainder needs an odd number of odd tokens; always satisfiable; keep simple
            if rem[b] != 2:   # 2 cannot be a sum of distinct odds; any other nonnegative remainder may still complete
                if rec(i + 1): return True
            rem[b] = r
        return False
    ok = rec(0); return ok, nodes
t0 = time.time(); done = 0; fail = []; unk = []; total_nodes = 0; worst = 0
for t in rows:
    try:
        ok, nodes = solve(t); total_nodes += nodes; worst = max(worst, nodes)
        if not ok: fail.append(t)
    except TimeoutError:
        unk.append(t)
    done += 1
    if time.time() - t0 > 230: break
el = time.time() - t0
print(f"targets tried {done}/{len(rows)}; certified {done-len(fail)-len(unk)}; no partition {len(fail)}; cap hit {len(unk)}; {el:.1f}s; mean {1000*el/done:.2f} ms/target; mean nodes {total_nodes/max(1,done-len(unk)):.0f}; worst nodes {worst}")
print("failures", fail[:3], "unknown", unk[:3])
