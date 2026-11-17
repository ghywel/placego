# The single passage E A^4 E A^7 E lifted width by width with the exact end cone (Cloud, CL755). Own code.
# Only cells 1..2(b0-s)+1 of the window at phase s can reach the samples up to the last constrained phase b0, so the window
# width at phase s is w(s) = min(W, 2(b0-s)+1): exact for consistency with the passage's samples, and it keeps the sets at the
# free end small. Free row at tick 1 (phase -34). uint64: exact to width 62. Usage: python3 -I passage_lift2.py WMAX OUTDIR [CONTROL_DIR]
import sys, os, time, json
import numpy as np
A = [2, 5]; E = [3, 3, 5, 3, 5, 5, 5, 5]
WORD = A * 4 + E + A * 7 + E; P = sum(WORD); assert P == 145
u = np.zeros(P, dtype=np.uint8); t = 0
for g in WORD: u[t % P] = 1; t += g
def tr(phase): return int(u[phase % P])
a0, b0 = -34, 145
PH = list(range(a0, b0 + 1))
def wid(W, s): return min(W, 2 * (b0 - s) + 1)
MASK = lambda w: (np.uint64(1) << np.uint64(w)) - np.uint64(1)
def Bstep(x, b, w):
    one = np.uint64(1); left = (x << one) | np.uint64(b)
    return (left ^ (x | (x >> one))) & MASK(w)
def move(x, e, W):
    y = x | (np.uint64(e) << np.uint64(W)); y = Bstep(y, 0, W + 2) & MASK(W + 1); return Bstep(y, 1, W + 1) & MASK(W)
def step(prev, w_prev, w_next):
    """images of the width-w_prev windows at the next phase, as width-w_next windows (w_next <= w_prev)."""
    if w_next <= w_prev - 2:
        return np.unique(move(prev, 0, w_prev) & MASK(w_next))          # exteriors never reach the kept cells
    return np.unique(np.concatenate([move(prev, e, w_prev) for e in range(4)]) & MASK(w_next))
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
    F = {a0: cands[a0]}
    for s in PH[1:]:
        prev = F[s - 1]
        if prev.size == 0: F[s] = prev; continue
        img = step(prev, wid(W, s - 1), wid(W, s))
        F[s] = img[isin_sorted(img, cands[s])]
    B = {b0: F[b0]}
    for s in reversed(PH[:-1]):
        a_ = F[s]; nxt = B[s + 1]; wp, wn = wid(W, s), wid(W, s + 1)
        if a_.size == 0: B[s] = a_; continue
        if wn <= wp - 2:
            keep = isin_sorted(move(a_, 0, wp) & MASK(wn), nxt)
        else:
            keep = np.zeros(a_.shape, dtype=bool)
            for e in range(4): keep |= isin_sorted(move(a_, e, wp) & MASK(wn), nxt)
        B[s] = a_[keep]
    return B
def main():
    Wmax, out = int(sys.argv[1]), sys.argv[2]; ctrl = sys.argv[3] if len(sys.argv) > 3 else None
    assert Wmax <= 62
    os.makedirs(out, exist_ok=True); t0 = time.time()
    sets = {s: np.array([tr(s)], dtype=np.uint64) for s in PH}
    sets = prune(sets, 1); prof = {}
    for W in range(2, Wmax + 1):
        tw = time.time()
        cands = {}
        for s in PH:
            if wid(W, s) > wid(W - 1, s):
                hi = np.uint64(1) << np.uint64(wid(W, s) - 1)
                cands[s] = np.unique(np.concatenate([sets[s], sets[s] | hi]))
            else: cands[s] = sets[s]
        sets = prune(cands, W)
        sizes = {s: int(sets[s].size) for s in PH}; tot = sum(sizes.values()); prof[W] = sizes
        line = f"W={W} total {tot} | start {sizes[a0]} seam69 {sizes[0]} source109 {sizes[20]} seam193 {sizes[62]} source275 {sizes[103]} gate285 {sizes[108]} min {min(sizes.values())} max {max(sizes.values())} | {time.time()-tw:.1f}s"
        notes = []
        if W >= 21 and sizes[20] and sizes[103]:
            notes.append(f"labels {np.unique(label_words(sets[20], W)).tolist()} / {np.unique(label_words(sets[103], W)).tolist()}")
        if ctrl and os.path.exists(os.path.join(ctrl, f"passage_W{W}.npz")):
            try:
                z = np.load(os.path.join(ctrl, f"passage_W{W}.npz")); mism = 0
                for s in PH:
                    if wid(W, s) == W and not np.array_equal(z[f"p{s+34}"], sets[s]): mism += 1
                notes.append(f"control vs free-end run: {mism} mismatching full-width phases")
            except Exception as ex:
                notes.append(f"control file unreadable ({type(ex).__name__}), skipped")
        if tot == 0:
            print(line + f"  EMPTY: no right half beside the alternating centre realises the passage E A^4 E A^7 E (width {W})", flush=True); break
        print(line + ("  " + "; ".join(notes) if notes else ""), flush=True)
        np.savez_compressed(os.path.join(out, f"passage_W{W}.npz"), **{f"p{s+34}": sets[s] for s in PH})
    json.dump(prof, open(os.path.join(out, "profile.json"), "w"))
    print(f"done; wall {time.time()-t0:.1f}s", flush=True)
main()
