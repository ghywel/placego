#!/usr/bin/env python3
"""L8 <= 68 certificates for the exceptional levels E_24..E_32 (MI044's reduction), as a parallel, resumable job.

A town is eight street lengths in [68, 2m+66] summing to m^2; the planks are the odd lengths 1..2m-1. A certificate is an
exact tiling. For every town the job records the tiling (as the bin index of each plank, largest plank first), the number
of search nodes, and whether the FIRST branch of the search succeeded with no backtracking (the "greedy" flag): a town the
greedy rule fails is interesting mathematics, a town the solver cannot finish within the cap is reported as unknown.

Usage:  python3 l8_certificates.py run  OUTDIR [--levels 24,25,...] [--workers N] [--cap SECONDS]
        python3 l8_certificates.py check OUTDIR          # independent re-verification of every certificate
Work is split into chunks (level, smallest street length); each chunk writes OUTDIR/E<m>_l<l1>.jsonl and is skipped on
resume if its file ends with the DONE line. No network, no git: run it outside the repository's data rules.
"""
import sys, os, json, time, hashlib, argparse
from multiprocessing import Pool

def planks(m): return list(range(2*m-1, 0, -2))

def solve(m, targets, cap):
    P = planks(m); k = len(targets); rem = list(targets); n = len(P); t0 = time.time(); nodes = [0]
    if sum(targets) != m*m: return None, 0, False
    assign = [-1]*n; suf = [P[i:] for i in range(n+1)]; dead = set(); backtracked = [False]
    def feasible(i):
        left = n - i; big = suf[i]; small = big[::-1]; tmin_total = 0; tmax_total = 0
        for r in rem:
            if r < 0: return False
            if r == 0: continue
            par = r & 1; s = 0; t = 0; tmin = None
            for p in big:
                s += p; t += 1
                if s >= r and (t & 1) == par: tmin = t; break
            if tmin is None: return False
            s = 0; t = 0; tmax = 0
            for p in small:
                if s + p > r: break
                s += p; t += 1
                if (t & 1) == par: tmax = t
            if tmax < tmin: return False
            tmin_total += tmin; tmax_total += tmax
        return tmin_total <= left <= tmax_total
    def rec(i):
        nodes[0] += 1
        if nodes[0] & 1023 == 0 and time.time() - t0 > cap: raise TimeoutError
        if i == n: return all(r == 0 for r in rem)
        key = (i, tuple(sorted(rem)))
        if key in dead: return False
        p = P[i]; tried = set(); first = True
        for b in sorted(range(k), key=lambda b: -rem[b]):
            if rem[b] < p or rem[b] in tried: continue
            tried.add(rem[b]); rem[b] -= p; assign[i] = b
            if feasible(i+1) and rec(i+1): return True
            rem[b] += p; assign[i] = -1; backtracked[0] = True
        dead.add(key); return False
    try:
        ok = rec(0)
    except TimeoutError:
        return 'unknown', nodes[0], False
    return (assign[:] if ok else 'impossible'), nodes[0], (ok and not backtracked[0])

def towns_with_min(m, l1):
    """Nondecreasing 8-tuples with smallest street exactly l1."""
    hi = 2*m + 66; out = []
    def rec(i, start, remaining, acc):
        if i == 8:
            if remaining == 0: out.append(tuple(acc))
            return
        left = 8 - i
        for l in range(start, hi + 1):
            if l * left > remaining: break
            if l + hi * (left - 1) < remaining: continue
            rec(i + 1, l, remaining - l, acc + [l])
    rec(1, l1, m*m - l1, [l1]); return out

def chunk(args):
    m, l1, outdir, cap = args
    path = os.path.join(outdir, f"E{m}_l{l1}.jsonl")
    if os.path.exists(path):
        with open(path, 'rb') as f:
            f.seek(0, 2); size = f.tell(); f.seek(max(0, size - 64)); tail = f.read().decode(errors='ignore')
        if tail.strip().endswith('"DONE"'): return (m, l1, 'skipped')
    towns = towns_with_min(m, l1); t0 = time.time(); st = {'tiled': 0, 'greedy': 0, 'impossible': 0, 'unknown': 0}
    with open(path, 'w') as f:
        for t in towns:
            res, nodes, greedy = solve(m, list(t), cap)
            if res == 'unknown': st['unknown'] += 1; f.write(json.dumps({'m': m, 'town': t, 'r': 'U', 'nodes': nodes}) + "\n")
            elif res == 'impossible': st['impossible'] += 1; f.write(json.dumps({'m': m, 'town': t, 'r': 'X', 'nodes': nodes}) + "\n")
            else:
                st['tiled'] += 1; st['greedy'] += greedy
                f.write(json.dumps({'m': m, 'town': t, 'a': ''.join(str(b) for b in res), 'n': nodes, 'g': int(greedy)}) + "\n")
        f.write(json.dumps({'m': m, 'l1': l1, 'towns': len(towns), 'stats': st, 'seconds': round(time.time() - t0, 1), 'end': "DONE"}) + "\n")
    return (m, l1, st)

def run(a):
    os.makedirs(a.outdir, exist_ok=True)
    jobs = [(m, l1, a.outdir, a.cap) for m in a.levels for l1 in range(68, 2*m + 67) if 8*l1 <= m*m]
    print(f"{len(jobs)} chunks, {a.workers} workers, cap {a.cap}s", flush=True); t0 = time.time(); tot = {}
    with Pool(a.workers) as pool:
        for (m, l1, st) in pool.imap_unordered(chunk, jobs):
            if st == 'skipped': continue
            for k, v in st.items(): tot[k] = tot.get(k, 0) + v
            if st['impossible'] or st['unknown']: print(f"  E{m} l1={l1}: {st}", flush=True)
            if (m, l1) == (m, 68): print(f"  E{m} started; running totals {tot} ({time.time()-t0:.0f}s)", flush=True)
    print(f"finished: {tot} in {time.time()-t0:.0f}s", flush=True)

def check(a):
    files = sorted(f for f in os.listdir(a.outdir) if f.endswith('.jsonl')); tot = {'valid': 0, 'invalid': 0, 'X': 0, 'U': 0}; h = hashlib.sha256()
    for fn in files:
        done = False
        for line in open(os.path.join(a.outdir, fn)):
            h.update(line.encode()); r = json.loads(line)
            if 'end' in r: done = True; continue
            m = r['m']; town = r['town']
            if r.get('r') in ('X', 'U'): tot[r['r']] += 1; continue
            P = planks(m); sums = [0]*8
            for p, b in zip(P, r['a']): sums[int(b)] += p
            ok = sorted(sums) == sorted(town) and len(r['a']) == len(P) and sum(town) == m*m and all(68 <= l <= 2*m+66 for l in town)
            tot['valid' if ok else 'invalid'] += 1
        if not done: print("INCOMPLETE", fn)
    print(f"{len(files)} chunk files: {tot}; stream sha256 {h.hexdigest()}")

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('mode', choices=['run', 'check']); ap.add_argument('outdir')
    ap.add_argument('--levels', default='24,25,26,27,28,29,30,31,32'); ap.add_argument('--workers', type=int, default=max(1, os.cpu_count() - 2)); ap.add_argument('--cap', type=float, default=120.0)
    a = ap.parse_args(); a.levels = [int(x) for x in a.levels.split(',')]
    run(a) if a.mode == 'run' else check(a)
