#!/usr/bin/env python3
"""E2: does enlarging the right support expose longer different-edge center-trace agreement at fixed edges?
(Design CL619 after GPT's GC1782/GC1785; Cloud run at the owner's word, CL620.)

Edge pairs (a, b) = (-2, -1) and (-3, -2); right support [a, R] for R in 6, 8, 10, 12 (rows per edge 2^(R - a));
H = 256 fixed, horizon hits reported as censored; OFF = R + H + 8 computed from the parameters.
Predeclared prediction: m(a, b, R + 2) >= m(a, b, R) + 2 at every step, from the E1 anchors m(-2,-1,6) = 8, m(-3,-2,6) = 14.
Engine A: integer bitsets. Engine B (independent): lists with the literal eight-case table.
Caps enforced in-process: RLIMIT_CPU 600 s, RLIMIT_AS 1 GiB; the launcher adds timeout 900. Output: one JSON, plus a
checkpoint JSON rewritten after every (edge pair, R) so a cap termination retains partial results (GC1785).
"""
import sys, json, time, resource, hashlib, itertools, bisect

CAP_CPU_S = 600; CAP_AS_BYTES = 1024 * 2**20
resource.setrlimit(resource.RLIMIT_CPU, (CAP_CPU_S, CAP_CPU_S))
resource.setrlimit(resource.RLIMIT_AS, (CAP_AS_BYTES, CAP_AS_BYTES))

H = 256
EDGE_PAIRS = [(-2, -1), (-3, -2)]
RS = [6, 8, 10, 12]
ANCHORS = {(-2, -1): 8, (-3, -2): 14}  # E1 at R = 6

def stepA(x): return (x << 1) ^ (x | (x >> 1))
def traceA(x, OFF, H=H):
    out = 0
    for t in range(H):
        out = (out << 1) | ((x >> OFF) & 1); x = stepA(x)
    return out
TABLE = {(1,1,1):0,(1,1,0):0,(1,0,1):0,(1,0,0):1,(0,1,1):1,(0,1,0):1,(0,0,1):1,(0,0,0):0}
def stepB(cells, lo):
    ext = [0, 0] + cells + [0, 0]
    return [TABLE[(ext[i-1], ext[i], ext[i+1])] for i in range(1, len(ext) - 1)], lo - 1
def traceB(cells, lo, H=H):
    out = []
    for t in range(H):
        i = 0 - lo; out.append(cells[i] if 0 <= i < len(cells) else 0); cells, lo = stepB(cells, lo)
    return out
def row_int(a, bits, OFF):  # bits over positions a..R
    x = 0
    for i, b in enumerate(bits):
        if b: x |= 1 << (a + i + OFF)
    return x
def lcp(a, b, H=H):
    d = a ^ b
    return H if d == 0 else H - d.bit_length()

def rows_for(a, R, OFF):
    out = []
    for bits in itertools.product((0, 1), repeat=R - a):
        full = (1,) + bits
        out.append((full, row_int(a, full, OFF)))
    return out

def main():
    t0 = time.time(); c0 = time.process_time()
    results = {}; ctrl = {"anchors_reproduced": True, "replay_attaining_agree": True, "monotone_nondecreasing": True,
                          "prediction_strict_growth_2": True, "kit_1_vs_12_equal_256": None, "orient_m1_0_gives_0": None,
                          "orient_0_1_gives_1": None, "counts_ok": True, "distinct_ok": True}
    OFF0 = 12 + H + 8
    ctrl["kit_1_vs_12_equal_256"] = traceA(row_int(1, (1,), OFF0), OFF0) == traceA(row_int(1, (1, 1), OFF0), OFF0)
    ctrl["orient_m1_0_gives_0"] = ((stepA(row_int(-1, (1, 1), OFF0)) >> OFF0) & 1) == 0
    ctrl["orient_0_1_gives_1"] = ((stepA(row_int(0, (1, 1), OFF0)) >> OFF0) & 1) == 1
    for (a, b) in EDGE_PAIRS:
        prev = None
        for R in RS:
            OFF = R + H + 8
            A = rows_for(a, R, OFF); B = rows_for(b, R, OFF)
            ctrl["counts_ok"] &= (len(A) == 2 ** (R - a) and len(B) == 2 ** (R - b))
            ctrl["distinct_ok"] &= (len({x for _, x in A}) == len(A) and len({x for _, x in B}) == len(B))
            TA = sorted((traceA(x, OFF), bits) for bits, x in A); TB = [(traceA(x, OFF), bits) for bits, x in B]
            keys = [t for t, _ in TA]
            best = -1
            for tb, _ in TB:
                i = bisect.bisect_left(keys, tb)
                for j in (i - 1, i):
                    if 0 <= j < len(TA): best = max(best, lcp(keys[j], tb))
            m = best
            censored = m >= H
            # exact lexicographic minimum attaining pair (if not censored); for censored, any colliding pair
            shift = H - min(m, H - 1) if not censored else 0
            blocks = {}
            for ta, bits in TA: blocks.setdefault(ta >> (H - m) if not censored else ta, []).append(bits)
            cands = []
            for tb, bits in TB:
                blk = blocks.get(tb >> (H - m) if not censored else tb)
                if blk: cands.append((min(blk), bits))
            wa, wb = min(cands)
            # engine B replay of the attaining pair
            tA_ = traceB(list(wa), a); tB_ = traceB(list(wb), b)
            first = next((t for t in range(H) if tA_[t] != tB_[t]), None)
            ctrl["replay_attaining_agree"] &= ((first if first is not None else H) == m)
            if R == 6: ctrl["anchors_reproduced"] &= (m == ANCHORS[(a, b)])
            if prev is not None:
                ctrl["monotone_nondecreasing"] &= (m >= prev)
                if not censored: ctrl["prediction_strict_growth_2"] &= (m >= prev + 2)
            results[f"{a},{b},R={R}"] = {"rows_a": len(A), "rows_b": len(B), "max_common_prefix": m,
                                          "first_disagreement": (None if censored else m), "censored": censored,
                                          "witness_a": "".join(map(str, wa)), "witness_b": "".join(map(str, wb)),
                                          "engineB_first_disagreement": first,
                                          "cpu_s_so_far": round(time.process_time() - c0, 2)}
            print(f"progress edges ({a},{b}) R={R}: m={m} censored={censored} witness {''.join(map(str,wa))} / {''.join(map(str,wb))} cpu={time.process_time()-c0:.1f}s", flush=True)
            prev = m
            json.dump({"checkpoint": True, "results_so_far": results, "controls_so_far": ctrl, "cpu_s": round(time.process_time() - c0, 2),
                       "source_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()},
                      open((sys.argv[1] if len(sys.argv) > 1 else "e2_results.json") + ".checkpoint", "w"), indent=1)
    REQUIRED = ["anchors_reproduced", "replay_attaining_agree", "monotone_nondecreasing", "kit_1_vs_12_equal_256",
                "orient_m1_0_gives_0", "orient_0_1_gives_1", "counts_ok", "distinct_ok"]
    for k in REQUIRED:
        if k not in ctrl or not isinstance(ctrl[k], bool): raise SystemExit(f"control {k} missing or non-Boolean")
    controls_ok = all(ctrl[k] for k in REQUIRED)
    summary = {"H": H, "edge_pairs": EDGE_PAIRS, "R": RS, "results": results, "controls": ctrl, "controls_all_ok": controls_ok,
               "prediction_strict_growth_2_holds": ctrl["prediction_strict_growth_2"],
               "cpu_s": round(time.process_time() - c0, 3), "wall_s": round(time.time() - t0, 3),
               "maxrss_MiB": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1),
               "caps_enforced": {"RLIMIT_CPU_s": CAP_CPU_S, "RLIMIT_AS_MiB": CAP_AS_BYTES // 2**20},
               "python": sys.version.split()[0], "source_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    out = sys.argv[1] if len(sys.argv) > 1 else "e2_results.json"
    json.dump(summary, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=1))
    for k, v in results.items(): print(k, v["max_common_prefix"], "censored" if v["censored"] else "", v["witness_a"], v["witness_b"])
    if not controls_ok: raise SystemExit("E2 CONTROL FAILURE")
if __name__ == "__main__": main()
