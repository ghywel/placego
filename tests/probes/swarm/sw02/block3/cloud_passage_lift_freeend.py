# The single passage E A^4 E A^7 E lifted width by width (Cloud, CL755). Own code. The finite-trace sets at width W project
# into those at W-1, so lift(sets[W-1]) contains sets[W]; a forward pass from the lifted start restricted to the lifted
# candidates and one backward prune give sets[W] exactly. Free row at tick 1 (phase -34), nothing after tick 359 (phase 145).
# uint64: exact to width 62. Usage: python3 -I passage_lift.py WMAX OUTDIR
import sys, os, time, json
import numpy as np
A = [2, 5]; E = [3, 3, 5, 3, 5, 5, 5, 5]
WORD = A * 4 + E + A * 7 + E; P = sum(WORD); assert P == 145
u = np.zeros(P, dtype=np.uint8); t = 0
for g in WORD: u[t % P] = 1; t += g
def tr(phase): return int(u[phase % P])
a0, b0 = -34, 145
PH = list(range(a0, b0 + 1))
MASK = lambda w: (np.uint64(1) << np.uint64(w)) - np.uint64(1)
def Bstep(x, b, w):
    one = np.uint64(1); left = (x << one) | np.uint64(b)
    return (left ^ (x | (x >> one))) & MASK(w)
def move(x, e, W):
    y = x | (np.uint64(e) << np.uint64(W)); y = Bstep(y, 0, W + 2) & MASK(W + 1); return Bstep(y, 1, W + 1) & MASK(W)
def isin_sorted(a, b):
    if b.size == 0: return np.zeros(a.shape, dtype=bool)
    idx = np.searchsorted(b, a); idx[idx == b.size] = 0
    return b[idx] == a
def label_words(a, W):
    out = np.zeros(a.shape, dtype=np.int64); x = a.copy(); w = W
    for k in range(14):
        out |= ((x >> np.uint64(7)) & np.uint64(1)).astype(np.int64) << k
        x = Bstep(x, 0 if k % 2 == 0 else 1, w); w -= 1; x &= MASK(w)
    return out
def prune(cands, W):
    """forward pass restricted to the candidates, then backward prune; cands: dict phase -> sorted unique array."""
    F = {a0: cands[a0]}
    for s in PH[1:]:
        prev = F[s - 1]
        if prev.size == 0: F[s] = prev; continue
        img = np.unique(np.concatenate([move(prev, e, W) for e in range(4)]))
        F[s] = img[isin_sorted(img, cands[s])]
    B = {b0: F[b0]}
    for s in reversed(PH[:-1]):
        a_ = F[s]; nxt = B[s + 1]; keep = np.zeros(a_.shape, dtype=bool)
        for e in range(4): keep |= isin_sorted(move(a_, e, W), nxt)
        B[s] = a_[keep]
    return B
def main():
    Wmax, out = int(sys.argv[1]), sys.argv[2]; assert Wmax <= 62
    os.makedirs(out, exist_ok=True); t0 = time.time()
    # width 1: candidates = the prescribed bit at each phase
    sets = {s: np.array([tr(s)], dtype=np.uint64) for s in PH}
    sets = prune(sets, 1)
    prof = {}
    for W in range(2, Wmax + 1):
        tw = time.time(); hi = np.uint64(1) << np.uint64(W - 1)
        cands = {s: np.unique(np.concatenate([sets[s], sets[s] | hi])) for s in PH}
        sets = prune(cands, W)
        sizes = {s: int(sets[s].size) for s in PH}; tot = sum(sizes.values())
        line = f"W={W} total {tot} | source109 {sizes[20]} source275 {sizes[103]} seam69 {sizes[0]} seam193 {sizes[62]} end {sizes[145]} min {min(sizes.values())} | {time.time()-tw:.1f}s"
        notes = []
        if W >= 21 and sizes[20] and sizes[103]:
            l1 = np.unique(label_words(sets[20], W)).tolist(); l2 = np.unique(label_words(sets[103], W)).tolist()
            notes.append(f"labels {l1} / {l2}")
        prof[W] = sizes
        if tot == 0:
            print(line + "  EMPTY: no right half beside the alternating centre realises the passage E A^4 E A^7 E (width %d)" % W, flush=True)
            break
        print(line + ("  " + "; ".join(notes) if notes else ""), flush=True)
        np.savez_compressed(os.path.join(out, f"passage_W{W}.npz"), **{f"p{s+34}": sets[s] for s in PH})
    json.dump(prof, open(os.path.join(out, "profile.json"), "w"))
    print(f"done; wall {time.time()-t0:.1f}s", flush=True)
main()
