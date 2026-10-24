#!/usr/bin/env python3
"""E1: finite different-edge agreement test for the kit's EdgeObservable (GPT's design, GC1780 section 3; Cloud run, CL618).

Revision 2 (CL619, after GC1782): explicit control roll-up with a failed exit; the replayed pairs named as the fifteen
edge-pair representatives; the attaining pair is the exact lexicographic minimum over the attaining prefix blocks;
resource caps enforced in-process (RLIMIT_CPU, RLIMIT_AS) and recorded; output file name taken from the command line.
The retained CL618 results (e1_results.json, revision 1) stand; this revision reproduces their values.

Rows supported in [-6, 6] with leftmost black a in {-6, ..., -1} (8064 rows); center traces for t = 0..255 under the full
expanding zero-background rule 30 update; for every pair of edges a < b the longest common trace prefix over different-edge
pairs, with a canonical attaining pair; the predeclared target "first disagreement <= -a + 8"; and the controls of the design.
Engine A: Python integers as bitsets. Engine B (independent): lists with a literal eight-case table.
"""
import sys, json, time, resource, hashlib, itertools, bisect

CAP_CPU_S = 180; CAP_AS_BYTES = 512 * 2**20
resource.setrlimit(resource.RLIMIT_CPU, (CAP_CPU_S, CAP_CPU_S))
resource.setrlimit(resource.RLIMIT_AS, (CAP_AS_BYTES, CAP_AS_BYTES))

H = 256; LO, HI = -6, 6
OFF = 300  # bit index = position + OFF; positions in [-6-256, 6+256] fit

# ---------- engine A: integer bitsets ----------
def stepA(x):
    # new(p) = x(p-1) xor (x(p) or x(p+1)); bit p+OFF holds x(p): x(p-1) is bit (p-1)+OFF = (x << 1) at p, x(p+1) is (x >> 1)
    return (x << 1) ^ (x | (x >> 1))
def traceA(x, H=H):
    out = 0
    for t in range(H):
        out = (out << 1) | ((x >> OFF) & 1)
        x = stepA(x)
    return out  # bit (H-1-t) holds center at time t; lexicographic order of bit strings from t = 0

# ---------- engine B: dict table on lists, written independently ----------
TABLE = {(1,1,1):0,(1,1,0):0,(1,0,1):0,(1,0,0):1,(0,1,1):1,(0,1,0):1,(0,0,1):1,(0,0,0):0}  # rule 30 by Wolfram code
def stepB(cells, lo):
    # cells[i] = x(lo + i); returns (new cells, new lo) with one zero of padding each side
    ext = [0, 0] + cells + [0, 0]
    new = [TABLE[(ext[i-1], ext[i], ext[i+1])] for i in range(1, len(ext) - 1)]
    return new, lo - 1
def traceB(cells, lo, H=H):
    out = []
    for t in range(H):
        i = 0 - lo
        out.append(cells[i] if 0 <= i < len(cells) else 0)
        cells, lo = stepB(cells, lo)
    return out

def row_int(bits_by_pos):  # dict pos -> bit
    x = 0
    for p, b in bits_by_pos.items():
        if b: x |= 1 << (p + OFF)
    return x
def lcp(a, b, H=H):
    d = a ^ b
    if d == 0: return H
    return H - d.bit_length()  # number of equal leading bits (from t = 0)

def main():
    t0 = time.time(); c0 = time.process_time()
    rows = []  # (edge a, bitstring tuple over positions a..6, int)
    for a in range(LO, 0):
        free = HI - a  # positions a+1..6
        for bits in itertools.product((0, 1), repeat=free):
            d = {a: 1}; d.update({a + 1 + i: bits[i] for i in range(free)})
            rows.append((a, (1,) + bits, row_int(d)))
    assert len(rows) == 8064, len(rows)
    ints = [r[2] for r in rows]; assert len(set(ints)) == 8064
    for a, bits, x in rows:
        assert (x >> (a + OFF)) & 1 == 1 and (x & ((1 << (a + OFF)) - 1)) == 0 and x < (1 << (HI + OFF + 1))
    traces = [traceA(x) for x in ints]
    byedge = {}
    for (a, bits, x), tr in zip(rows, traces):
        byedge.setdefault(a, []).append((tr, bits))
    for a in byedge: byedge[a].sort()
    results = {}; longest = []
    for a, b in itertools.combinations(sorted(byedge), 2):  # a < b
        A = byedge[a]; Akeys = [t for t, _ in A]
        best = (-1, None, None)
        for tb, bitsb in byedge[b]:
            i = bisect.bisect_left(Akeys, tb)
            for j in (i - 1, i):
                if 0 <= j < len(A):
                    l = lcp(Akeys[j], tb)
                    cand = (l, A[j][1], bitsb)
                    if l > best[0] or (l == best[0] and (cand[1], cand[2]) < (best[1], best[2])): best = cand
        l, ba, bb = best
        if l < H:  # exact lexicographic minimum over all pairs attaining l: same l-bit prefix, cross pairs
            shift = H - l
            blocksA = {}
            for ta, bitsa in A: blocksA.setdefault(ta >> shift, []).append(bitsa)
            cands = []
            for tb, bitsb in byedge[b]:
                blk = blocksA.get(tb >> shift)
                if blk: cands.append((min(blk), bitsb))
            ba, bb = min(cands)
        results[f"{a},{b}"] = {"max_common_prefix": l, "first_disagreement": (l if l < H else None), "censored": l >= H,
                               "target_le": -a + 8, "target_holds": l <= -a + 8,
                               "pair_a": "".join(map(str, ba)), "pair_b": "".join(map(str, bb))}
        longest.append((l, a, b, ba, bb))
    longest.sort(reverse=True)
    # --- controls ---
    ctrl = {}
    # 1. replay the fifteen edge-pair representatives (one attaining pair per pair of edges) with engine B
    ok = True; replay = []
    for l, a, b, ba, bb in longest:
        tA = traceB(list(ba), a); tB = traceB(list(bb), b)
        first = next((t for t in range(H) if tA[t] != tB[t]), None)
        ok &= ((first if first is not None else H) == l)
        replay.append({"edges": [a, b], "engineB_first_disagreement": first, "engineA": (l if l < H else None)})
    ctrl["replay_edge_pair_representatives_agree"] = ok; ctrl["replay_edge_pair_representatives"] = replay
    # 2. all configurations in [-2,2], 32 steps, both engines
    ok2 = True
    for bits in itertools.product((0, 1), repeat=5):
        d = {p: bits[p + 2] for p in range(-2, 3)}
        tA = traceA(row_int(d), 32); tB = traceB(list(bits), -2, 32)
        ok2 &= (tA == int("".join(map(str, tB)), 2) if any(tB) else tA == 0)
    ctrl["box22_two_engines_agree_32"] = ok2
    # 3. equal-right-half pairs against the -q lemma (rows agreeing at all p >= 0, different edges)
    byright = {}
    for a, bits, x in rows:
        byright.setdefault(x >> OFF, []).append((a, bits, x))
    ok3 = True; n3 = 0
    for key, group in byright.items():
        for (a, ba, xa), (b, bb, xb) in itertools.combinations(group, 2):
            if a == b: continue
            d = xa ^ xb; q = d.bit_length() - 1 - OFF  # rightmost disagreement position
            assert q < 0
            tA, tB = traceA(xa), traceA(xb); first = lcp(tA, tB)
            ok3 &= (first == -q); n3 += 1
    ctrl["minus_q_lemma_pairs"] = n3; ctrl["minus_q_lemma_holds"] = ok3
    # 4. kit's {1} vs {1,2}: identical traces (same edge, positive control)
    ctrl["kit_1_vs_12_equal_256"] = traceA(row_int({1: 1})) == traceA(row_int({1: 1, 2: 1}))
    # 5. orientation
    ctrl["orient_m1_0_gives_0"] = ((stepA(row_int({-1: 1, 0: 1})) >> OFF) & 1) == 0
    ctrl["orient_0_1_gives_1"] = ((stepA(row_int({0: 1, 1: 1})) >> OFF) & 1) == 1
    ctrl["count"] = len(rows); ctrl["distinct"] = len(set(ints)) == 8064
    REQUIRED = ["replay_edge_pair_representatives_agree", "box22_two_engines_agree_32", "minus_q_lemma_holds",
                "kit_1_vs_12_equal_256", "orient_m1_0_gives_0", "orient_0_1_gives_1", "distinct"]
    for k in REQUIRED:
        if k not in ctrl or not isinstance(ctrl[k], bool): raise SystemExit(f"control {k} missing or non-Boolean")
    all_ok = all(ctrl[k] for k in REQUIRED) and ctrl["count"] == 8064
    summary = {"H": H, "domain": "[-6,6], edges -6..-1", "rows": len(rows),
               "collision_at_256": any(v["censored"] for v in results.values()),
               "target_minus_a_plus_8_holds_all": all(v["target_holds"] for v in results.values()),
               "max_first_disagreement_overall": max(l for l, *_ in longest),
               "per_edge_pair": results, "controls": ctrl, "controls_all_ok": all_ok,
               "cpu_s": round(time.process_time() - c0, 3), "wall_s": round(time.time() - t0, 3),
               "maxrss_MiB": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1),
               "caps_enforced": {"RLIMIT_CPU_s": CAP_CPU_S, "RLIMIT_AS_MiB": CAP_AS_BYTES // 2**20},
               "python": sys.version.split()[0], "source_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    out = sys.argv[1] if len(sys.argv) > 1 else "e1_results.json"
    json.dump(summary, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "per_edge_pair"}, indent=1))
    print("per edge pair (a,b): max common prefix / target -a+8 / holds")
    for k, v in results.items(): print(k, v["max_common_prefix"], v["target_le"], v["target_holds"], v["pair_a"], v["pair_b"])
    if not all_ok: raise SystemExit("E1 CONTROL FAILURE")
if __name__ == "__main__": main()
