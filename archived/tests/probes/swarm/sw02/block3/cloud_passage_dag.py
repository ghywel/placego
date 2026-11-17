# The single passage E A^4 E A^7 E as a finite-trace DAG on xx windows (Cloud, CL755). Own code.
# Phases of the periodic 4,7 word (A^4 E A^7 E, period 145): phase 0 = the first black of A^4 after an E.
# The passage's sampled steps s_p = 0..179 (tick 2 s_p + 1) are phases s_p - 34: the first E is -34..-1, A^4 is 0..27,
# E is 28..61, A^7 is 62..110, E is 111..144, the final black is 145. Sources: tick 109 = phase 20, tick 275 = phase 103.
# An arc [a, b] constrains column 1 at phases a..b only; the row at phase a is free (every window with the right bit),
# exteriors are free at every move. Forward images, one backward prune. Every right half beside the alternating centre
# whose samples match the trace on the arc has its windows in these sets (the relaxation only weakens).
import sys, time, os, json
import numpy as np
A = [2, 5]; E = [3, 3, 5, 3, 5, 5, 5, 5]
WORD = A * 4 + E + A * 7 + E; P = sum(WORD); assert P == 145
u = np.zeros(P, dtype=np.uint8); t = 0
for g in WORD: u[t % P] = 1; t += g
assert t == P and u.sum() == 38
def tr(phase): return int(u[phase % P])
MASK = lambda w: (np.uint64(1) << np.uint64(w)) - np.uint64(1)
def Bstep(x, b, w):
    one = np.uint64(1)
    left = (x << one) | np.uint64(b)
    return (left ^ (x | (x >> one))) & MASK(w)
def move(x, e, W):
    y = x | (np.uint64(e) << np.uint64(W))
    y = Bstep(y, 0, W + 2) & MASK(W + 1)
    return Bstep(y, 1, W + 1) & MASK(W)
def isin_sorted(a, b):
    if b.size == 0: return np.zeros(a.shape, dtype=bool)
    idx = np.searchsorted(b, a); idx[idx == b.size] = 0
    return b[idx] == a
def label_words(a, W):
    out = np.zeros(a.shape, dtype=np.int64); x = a.copy(); w = W
    for k in range(14):
        out |= ((x >> np.uint64(7)) & np.uint64(1)).astype(np.int64) << k
        b = 0 if k % 2 == 0 else 1
        x = Bstep(x, b, w); w -= 1
        x &= MASK(w)
    return out
def free_row(W, phase):
    allw = np.arange(1 << W, dtype=np.uint64)
    return allw[(allw & np.uint64(1)) == np.uint64(tr(phase))]
def forward(W, a, b, F0=None):
    """forward sets F[s], s = a..b (dict), from the free row at a (or a given set F0 at a)."""
    F = {a: free_row(W, a) if F0 is None else F0}
    for s in range(a + 1, b + 1):
        prev = F[s - 1]
        if prev.size == 0: F[s] = prev; continue
        img = np.unique(np.concatenate([move(prev, e, W) for e in range(4)]))
        F[s] = img[(img & np.uint64(1)) == np.uint64(tr(s))]
    return F
def backward(W, F, b, down_to):
    """B[s] for s = b down to down_to: windows of F[s] with a successor in B[s+1]."""
    B = {b: F[b]}
    for s in range(b - 1, down_to - 1, -1):
        a_ = F[s]; nxt = B[s + 1]
        keep = np.zeros(a_.shape, dtype=bool)
        for e in range(4): keep |= isin_sorted(move(a_, e, W), nxt)
        B[s] = a_[keep]
    return B
def readings(S, W, phase):
    out = {'n': int(S.size)}
    if S.size:
        out['low7'] = np.unique((S & np.uint64(127)).astype(np.int64)).tolist()[:16]
        if W >= 21:
            labs = np.unique(label_words(S, W)).tolist(); out['labels'] = labs[:20]; out['nlabels'] = len(labs)
    return out
def quartet(S):
    return np.unique(((S >> np.uint64(5)) & np.uint64(15)).astype(np.int64)).tolist() if S.size else []
def arc_labels(W, a, b, phases, F=None):
    """label sets at the given phases for the arc [a, b]."""
    if F is None: F = forward(W, a, b)
    lo = min(phases); B = backward(W, F, b, lo)
    return {p: readings(B[p], W, p) for p in phases}, F, B

def forward_sub(W, a, b, constrained):
    """forward sets with the bit filter applied only at the constrained phases (a set); the row at a is free."""
    allw = np.arange(1 << W, dtype=np.uint64)
    F = {a: allw[(allw & np.uint64(1)) == np.uint64(tr(a))] if a in constrained else allw}
    for s in range(a + 1, b + 1):
        prev = F[s - 1]
        if prev.size == 0: F[s] = prev; continue
        img = np.unique(np.concatenate([move(prev, e, W) for e in range(4)]))
        F[s] = img[(img & np.uint64(1)) == np.uint64(tr(s))] if s in constrained else img
    return F
def labels_sub(W, a, b, constrained, src):
    F = forward_sub(W, a, b, constrained); B = backward(W, F, b, src)
    return sorted(np.unique(label_words(B[src], W)).tolist()) if B[src].size else []

def main():
    W = int(sys.argv[1]); mode = sys.argv[2]
    t0 = time.time()
    if mode == 'passage':
        a, b = int(sys.argv[3]), int(sys.argv[4])
        F = forward(W, a, b); B = backward(W, F, b, a)
        print(f"W={W} arc [{a},{b}] (ticks {2*(a+34)+1}..{2*(b+34)+1}); forward sizes at a..a+30: {[int(F[s].size) for s in range(a, min(b, a+30)+1)]}")
        print(f"  sizes after prune, phases 0..145 step 5: {[(s, int(B[s].size)) for s in range(max(a,0), b+1, 5)]}")
        for name, p in (('source109', 20), ('source275', 103)):
            if a <= p <= b: print(f"  {name} (phase {p}): {readings(B[p], W, p)}")
        for name, p in (('gate119', 25), ('gate285', 108)):
            if a <= p <= b: print(f"  {name} (phase {p}): n={int(B[p].size)} cells6..9 (cell 6 low bit) = {quartet(B[p])}")
        for name, p in (('seam69', -34+34), ('seam193', 62)):
            if a <= p <= b: print(f"  {name} (phase {p}): n={int(B[p].size)}")
        print(f"  wall {time.time()-t0:.1f}s", flush=True)
    elif mode == 'minimal':
        # minimal arcs for the label at a source: vary b with a fixed (forward once), then vary a with b fixed.
        src = int(sys.argv[3]); a0, b0 = int(sys.argv[4]), int(sys.argv[5]); target = 4520
        F = forward(W, a0, b0)
        res = {'W': W, 'source': src, 'a0': a0, 'b0': b0, 'by_b': {}, 'by_a': {}}
        # by b: the earliest end that forces the target with the whole past from a0
        prev = None
        for b in range(src, b0 + 1):
            B = backward(W, F, b, src)
            labs = sorted(np.unique(label_words(B[src], W)).tolist()) if B[src].size else []
            res['by_b'][b] = labs
            if labs != prev: print(f"  a={a0} b={b}: n={int(B[src].size)} labels={labs if len(labs)<=8 else str(len(labs))+' labels'}", flush=True)
            prev = labs
            if labs == [target]:
                print(f"EARLIEST END forcing {target} at source phase {src} with past from {a0}: b*={b} (tick {2*(b+34)+1})", flush=True); break
        else:
            print(f"NOT FORCED by b0={b0}: labels {prev}", flush=True)
        # by a: the latest start that forces the target with the whole future to b0 (binary search, monotone)
        def labs_for_a(a):
            Fa = forward(W, a, b0); Ba = backward(W, Fa, b0, src)
            return sorted(np.unique(label_words(Ba[src], W)).tolist()) if Ba[src].size else []
        lo, hi = a0, src   # lo forces (checked below), hi presumably not
        l_lo = labs_for_a(lo); res['by_a'][lo] = l_lo
        print(f"  a={lo} b={b0}: labels={l_lo if len(l_lo)<=8 else str(len(l_lo))+' labels'}", flush=True)
        if l_lo != [target]:
            print(f"NOT FORCED from a0={a0}: labels {l_lo if len(l_lo)<=8 else len(l_lo)}", flush=True)
        else:
            l_hi = labs_for_a(hi); res['by_a'][hi] = l_hi
            print(f"  a={hi} b={b0}: labels={l_hi if len(l_hi)<=8 else str(len(l_hi))+' labels'}", flush=True)
            if l_hi == [target]:
                print(f"LATEST START forcing {target}: a*={hi} (the source phase itself; only the future is needed)", flush=True)
            else:
                while hi - lo > 1:
                    mid = (lo + hi) // 2
                    l = labs_for_a(mid); res['by_a'][mid] = l
                    print(f"  a={mid} b={b0}: labels={l if len(l)<=8 else str(len(l))+' labels'}", flush=True)
                    if l == [target]: lo = mid
                    else: hi = mid
                print(f"LATEST START forcing {target} at source phase {src} with future to {b0}: a*={lo} (tick {2*(lo+34)+1}); a={hi} does not", flush=True)
        print(f"  wall {time.time()-t0:.1f}s", flush=True)
        with open(sys.argv[6], 'w') as f: json.dump(res, f)

    elif mode == 'rect':
        # Pareto frontier of minimal arcs [a, b(a)] forcing the target at the source, for a from a_lo to the source
        src = int(sys.argv[3]); a_lo, b_max = int(sys.argv[4]), int(sys.argv[5]); target = 4520
        print(f"W={W} source phase {src}: for each start a, the earliest end b(a) forcing {target} (b<={b_max})")
        front = []
        for a in range(a_lo, src + 1):
            F = forward(W, a, b_max); found = None
            for b in range(src, b_max + 1):
                B = backward(W, F, b, src)
                labs = sorted(np.unique(label_words(B[src], W)).tolist()) if B[src].size else []
                if labs == [target]: found = b; break
            front.append((a, found)); print(f"  a={a} (tick {2*(a+34)+1}): b(a)={found}" + (f" (tick {2*(found+34)+1}), span {found-a+1} samples" if found is not None else " NOT FORCED"), flush=True)
        print(f"  wall {time.time()-t0:.1f}s", flush=True)
    elif mode == 'subset':
        # irreducible sample supports inside the arc [a, b]: free one sample at a time, keep it free if the target stays forced
        src = int(sys.argv[3]); a, b = int(sys.argv[4]), int(sys.argv[5]); target = 4520
        base = labels_sub(W, a, b, set(range(a, b + 1)), src)
        print(f"W={W} source phase {src}, arc [{a},{b}]: full-arc labels {base}")
        assert base == [target]
        orders = {'ends-inward': sorted(range(a, b + 1), key=lambda p: -abs(p - src)),
                  'source-outward': sorted(range(a, b + 1), key=lambda p: abs(p - src)),
                  'past-first': list(range(a, b + 1)), 'future-first': list(range(b, a - 1, -1))}
        for name, order in orders.items():
            cons = set(range(a, b + 1))
            for p in order:
                trial = cons - {p}
                if labels_sub(W, a, b, trial, src) == [target]: cons = trial
            kept = sorted(cons)
            print(f"  order {name}: irreducible support {len(kept)} samples: phases {kept}")
            print(f"     as (phase, tick, bit): {[(p, 2*(p+34)+1, tr(p)) for p in kept]}", flush=True)
        print(f"  wall {time.time()-t0:.1f}s", flush=True)
if __name__ == '__main__':
    main()
