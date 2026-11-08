# The periodic word (A^4 E A^7 E)^inf and other short cycles lifted alone on the xx window graph (Cloud, CL754). Own code. Usage: python3 -I cloud_cycle_lift.py WMAX CHECKPOINT_DIR BUDGET_SECONDS [WORD] ; WORD like A4EA7E; env PQ=1 for rule30-open move rule.
# Windows: columns 1..W at odd ticks, cell i <-> bit i-1. A move: double step, centre white then black, columns W+1, W+2 free.
# Live windows: on a bi-infinite path whose column-1 sampled word is the periodic gap word. Lift width by width.
import sys, time, os
import numpy as np
A = [2,5]; E = [3,3,5,3,5,5,5,5]
def parse_word(spec):
    out = []
    for m in re.finditer(r'(A|E)(\d*)', spec):
        n = int(m.group(2)) if m.group(2) else 1
        out += (A if m.group(1) == 'A' else E) * n
    return out
import re
SPEC = sys.argv[4] if len(sys.argv) > 4 else 'A4EA7E'
WORD = parse_word(SPEC)
P = sum(WORD); DEFAULT = (SPEC == 'A4EA7E')
if DEFAULT: assert P == 145
# sampled trace u(s): black at the partial sums (black at s=0, then after each gap)
u = np.zeros(P, dtype=np.uint8); t = 0
for g in WORD:
    u[t % P] = 1; t += g
assert t == P and u.sum() == len(WORD)
print(f'word {SPEC}: {len(WORD)} gaps, period {P} sampled steps', flush=True)
# phases of interest within the passage E A^4 E A^7 E (sampled steps from the first E's black at s=0 <-> tick 1):
# the periodic word here starts with A^4; align: passage word = E A^4 E A^7 E; our period = A^4 E A^7 E starting after the first E.
# tick t = 2s+1 for sampled step s. In the passage, sampled step s_p has tick 2 s_p + 1. The first E occupies s_p = 0..33 (34 gaps), A^4 is s_p = 34..61, ...
# Our phase s = s_p - 34 (mod 145). Source rows 109, 275 (ticks) -> s_p = 54, 137 -> s = 20, 103. Gate rows 119, 285 -> s_p = 59, 142 -> s = 25, 108. Seam 193 -> s_p = 96 -> s = 62.
PH = {'source109': 20, 'source275': 103, 'gate119': 25, 'gate285': 108, 'seam193': 62, 'E125launch': (62-34) % P, 'E291launch': (145-34) % P}
MASK = lambda w: (np.uint64(1) << np.uint64(w)) - np.uint64(1)
def Bstep(x, b, w):
    """one Rule 30 tick on cells 1..w (bits 0..w-1), centre bit b; valid result bits 0..w-2 (cell w needs cell w+1)."""
    one = np.uint64(1)
    left = (x << one) | np.uint64(b)
    return (left ^ (x | (x >> one))) & MASK(w)
PQ = os.environ.get("PQ", "0") == "1"
def move(x, e, W):
    """double step from a W-window x with exterior pair e in 0..3; xx: (cell W+1, cell W+2) at the tick; pq: cell W+1 at each of the two ticks. Exact low W bits."""
    if PQ:
        y = x | (np.uint64(e & 1) << np.uint64(W))                 # W+1 cells known at the odd tick
        y = Bstep(y, 0, W + 1) & MASK(W)                            # cells 1..W exact after the white-centre tick
        y = y | (np.uint64(e >> 1) << np.uint64(W))                 # column W+1 free again at the even tick
        return Bstep(y, 1, W + 1) & MASK(W)
    y = x | (np.uint64(e) << np.uint64(W))          # W+2 cells known (xx)
    y = Bstep(y, 0, W + 2) & MASK(W + 1)            # cells 1..W+1 exact after the white-centre tick
    y = Bstep(y, 1, W + 1) & MASK(W)                # cells 1..W exact after the black-centre tick
    return y
def isin_sorted(a, b):
    if b.size == 0: return np.zeros(a.shape, dtype=bool)
    idx = np.searchsorted(b, a); idx[idx == b.size] = 0
    return b[idx] == a
def core(sets, W):
    """greatest fixed point: keep windows with column 1 = u(s), some successor in sets[s+1] and some predecessor in sets[s-1]."""
    sets = [np.unique(s_) for s_ in sets]
    changed = True; rounds = 0
    while changed:
        changed = False; rounds += 1
        new = []
        for s in range(P):
            a = sets[s]
            if a.size == 0: new.append(a); continue
            a = a[((a & np.uint64(1)) == np.uint64(u[s]))]
            nxt = sets[(s + 1) % P]; prv = sets[(s - 1) % P]
            fwd = np.zeros(a.shape, dtype=bool)
            for e in range(4): fwd |= isin_sorted(move(a, e, W), nxt)
            a = a[fwd]
            if prv.size:
                preds = np.unique(np.concatenate([move(prv, e, W) for e in range(4)]))
                a = a[isin_sorted(a, preds)]
            else:
                a = a[:0]
            if a.size != sets[s].size: changed = True
            new.append(a)
        sets = new
    return sets, rounds
def lift(sets, W):
    hi = np.uint64(1) << np.uint64(W)
    return [np.concatenate([s_, s_ | hi]) for s_ in sets]
def label_words(a, Wrow, W):
    """for source windows a (at the source odd tick), the 14 column-8 bits over the next 14 ticks (odd then even), low bit first."""
    out = np.zeros(a.shape, dtype=np.int64); x = a.copy(); w = W
    for k in range(14):
        out |= ((x >> np.uint64(7)) & np.uint64(1)).astype(np.int64) << k
        b = 0 if k % 2 == 0 else 1          # odd tick: centre white; even tick: centre black
        x = Bstep(x, b, w) ; w -= 1          # one tick, one fewer exact cell
        x &= MASK(w)
    return out
def main(Wmax, ckdir, budget_s):
    t0 = time.time()
    assert Wmax <= 62, "uint64 words are exact only to width 62 (the exterior pair needs bits W, W+1); use cloud_cycle_lift_big.py beyond (CL755)"
    os.makedirs(ckdir, exist_ok=True)
    # resume
    W0 = 1; sets = None
    for W in range(Wmax, 0, -1):
        f = os.path.join(ckdir, f"core_W{W}.npz")
        if os.path.exists(f):
            z = np.load(f); sets = [z[f"s{s}"] for s in range(P)]; W0 = W + 1; break
    if sets is None:
        sets = [np.arange(2, dtype=np.uint64) for _ in range(P)]
        sets, r = core(sets, 1); W0 = 2
        print(f"W=1 core sizes min/max/total {min(x.size for x in sets)}/{max(x.size for x in sets)}/{sum(x.size for x in sets)} rounds {r}", flush=True)
        np.savez_compressed(os.path.join(ckdir, "core_W1.npz"), **{f"s{s}": sets[s] for s in range(P)})
    for W in range(W0, Wmax + 1):
        if time.time() - t0 > budget_s: print("budget reached before W", W, flush=True); break
        tw = time.time()
        sets, r = core(lift(sets, W - 1), W)
        sizes = [x.size for x in sets]
        tot = sum(sizes)
        line = f"W={W} core sizes min/max/total {min(sizes)}/{max(sizes)}/{tot} rounds {r} time {time.time()-tw:.1f}s"
        if tot == 0:
            print(line + "  EMPTY: this periodic word has no bi-infinite window path at this width", flush=True); 
            np.savez_compressed(os.path.join(ckdir, f"core_W{W}.npz"), **{f"s{s}": sets[s] for s in range(P)}); break
        # readings at the phases of interest (4,7 word only)
        notes = []
        for name in (('source109', 'source275') if DEFAULT else ()):
            a = sets[PH[name]]
            low7 = np.unique((a & np.uint64(127)).astype(np.int64)).tolist()
            notes.append(f"{name}: n={a.size} low7={low7[:8]}{'...' if len(low7)>8 else ''}")
            if W >= 21:
                labs = np.unique(label_words(a, None, W)).tolist()
                notes.append(f"  labels(14-bit col8 words)={labs if len(labs)<=12 else str(labs[:12])+'...('+str(len(labs))+')'}")
        for name in (('gate119', 'gate285') if DEFAULT else ()):
            a = sets[PH[name]]
            q = np.unique(((a >> np.uint64(5)) & np.uint64(15)).astype(np.int64)).tolist()   # cells 6..9, cell 6 = low bit
            notes.append(f"{name}: n={a.size} cells6..9 (cell6 low bit) patterns={q}")
        if DEFAULT: a = sets[PH['seam193']]; notes.append(f"seam193: n={a.size}")
        print(line + ("\n   " + "\n   ".join(notes) if notes else ''), flush=True)
        np.savez_compressed(os.path.join(ckdir, f"core_W{W}.npz"), **{f"s{s}": sets[s] for s in range(P)})
    print(f"done; wall {time.time()-t0:.1f}s", flush=True)
if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2], float(sys.argv[3]))
