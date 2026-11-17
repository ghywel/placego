#!/usr/bin/env python3
"""Per-lane death times of the constrained width-W starts (the kit's class: 2^(W/2) starts whose column -1 is black at
every even time below W), by lanes of one big integer (Cloud, CL632). Lane l carries the odd trace bits a(2i+1) = bit i of l
(the convention of submissions 16 and the edge-sep module); the start is the sideways reconstruction of the trace to depth W,
truncated there; death = first even time t with depth 1 white; cutoff 4W (censored lanes reported).
Output: deaths_W.npy (uint16 per lane) + a JSON summary. Kill test: D(W) against the known exact values."""
import sys, json, time, hashlib
import numpy as np

def pat(n, s):  # bit l of pat(n,s) is bit s of l, for l < 2^n
    blk = ((1 << (1 << s)) - 1) << (1 << s)        # 2^s zeros then 2^s ones (bits 2^s .. 2^(s+1)-1)
    out, length = blk, 1 << (s + 1)
    for _ in range(n - s - 1):
        out |= out << length; length <<= 1
    return out

def run(W, cutoff_mult=4):
    n = W // 2; L = 1 << n; ALL = (1 << L) - 1
    # trace words a(t): even t -> ALL (black), odd t = 2i+1 -> pat(n, i) for i < n, else 0 (the free bits beyond W are
    # irrelevant for the truncated start: the reconstruction to depth W uses a(0..W-1) only)
    def a(t):
        if t % 2 == 0: return ALL
        i = (t - 1) // 2
        return pat(n, i) if i < n else 0
    # sideways reconstruction: cell(t,k+1) = cell(t+1,k) ^ (cell(t,k) | cell(t,k-1)); column 0 is the wall (0), column 1 = a(t)
    T = W  # need times 0..W-1 for depths up to W
    col_prev = [0] * (T + 1)            # depth 0
    col = [a(t) for t in range(T + 1)]  # depth 1
    row0 = [0, col[0]]                  # start cells at depth 0, 1
    for k in range(1, W):
        new = [0] * (T + 1)
        for t in range(T - k):
            new[t] = col[t + 1] ^ (col[t] | col_prev[t])
        row0.append(new[0]); col_prev, col = col, new
    # row0[k] = lane word at depth k, k = 0..W; forward simulation on depths 0..W+cutoff
    cutoff = cutoff_mult * W
    width = W + cutoff + 2
    row = row0 + [0] * (width - len(row0))
    dead = 0; death = np.full(L, 0xFFFF, dtype=np.uint16)
    t0 = time.time()
    for t in range(cutoff + 1):
        if t % 2 == 0:
            newly = (~row[1]) & ~dead & ALL
            if newly:
                # record death times for newly dead lanes: bits of `newly` via numpy (linear, not quadratic)
                nbytes = (L + 7) // 8
                bits = np.unpackbits(np.frombuffer(newly.to_bytes(nbytes, 'little'), dtype=np.uint8), bitorder='little')[:L]
                death[bits.astype(bool)] = t
                dead |= newly
                if dead == ALL: break
        new = [0] * width
        for k in range(1, width - 1):
            new[k] = row[k + 1] ^ (row[k] | row[k - 1])
        row = new
    alive = L - int((death != 0xFFFF).sum())
    D = int(death[death != 0xFFFF].max()) if alive < L else None
    cnt = int((death == D).sum()) if D is not None else 0
    return death, {"W": W, "lanes": L, "D": D, "maximizers": cnt, "censored": alive, "cutoff": cutoff, "seconds": round(time.time() - t0, 2)}

if __name__ == "__main__":
    Ws = [int(x) for x in sys.argv[1].split(',')]
    summ = {}
    for W in Ws:
        death, s = run(W)
        np.save(f"deaths_{W}.npy", death)
        s["sha256"] = hashlib.sha256(open(f"deaths_{W}.npy", "rb").read()).hexdigest()
        summ[W] = s; print(json.dumps(s), flush=True)
    json.dump(summ, open("summary_" + sys.argv[1].replace(',', '_') + ".json", "w"), indent=1)
