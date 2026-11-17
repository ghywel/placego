# Trap-conditioned E statistics (Cloud, CL758). Own code. Finite right halves beside the alternating centre, bit-packed exact
# evolution (as cloud_transient_scan.py); per row: first odd-time entry tau into the kit's gate trap (829 width-16 codes),
# the E launches (35-sample block), the check E_t => tau > t, at-risk counts outside the trap and conditional launch rates.
# Usage: python3 -I trap_measure.py TRAPCODES OUT.json MODE ...   MODE=random K N T SEED | exhaustive LO HI T | roots T r1 r2 ...
# Env START0=1 places the rows at tick 0 (one tick earlier, centre black first) instead of tick 1.
import sys, os, json, time
import numpy as np
START0 = os.environ.get("START0", "0") == "1"
E_GAPS = [3, 3, 5, 3, 5, 5, 5, 5]
def template(gaps):
    L = sum(gaps) + 1; t = np.zeros(L, dtype=np.uint8); p = 0; t[0] = 1
    for g in gaps: p += g; t[p] = 1
    return t
E_T = template(E_GAPS)
codes = [int(x) for x in open(sys.argv[1]).read().split()]; assert len(codes) == 829
TRAP = np.zeros(1 << 16, dtype=bool); TRAP[np.array(codes)] = True
def evolve(rows, T):
    """sampled traces U[N, S] (ticks 1,3,...) and trap-membership M[N, S] of the width-16 window at those odd ticks."""
    N = len(rows); K = max(int(r).bit_length() for r in rows)
    nw = (K + T + 3 + 63) // 64
    X = np.zeros((N, nw), dtype=np.uint64)
    for w in range(nw):
        X[:, w] = np.array([(int(r) >> (64 * w)) & ((1 << 64) - 1) for r in rows], dtype=np.uint64)
    one, s63 = np.uint64(1), np.uint64(63)
    def tick(X, c):
        left = X << one; left[:, 1:] |= X[:, :-1] >> s63; left[:, 0] |= np.uint64(c)
        right = X >> one; right[:, :-1] |= (X[:, 1:] & one) << s63
        return left ^ (X | right)
    if START0: X = tick(X, 1)                 # the row is placed at tick 0 (centre black); this is its tick-1 image
    S = (T + 1) // 2; U = np.zeros((N, S), dtype=np.uint8); M = np.zeros((N, S), dtype=bool)
    U[:, 0] = (X[:, 0] & one).astype(np.uint8); M[:, 0] = TRAP[(X[:, 0] & np.uint64(0xFFFF)).astype(np.int64)]
    for t in range(1, T):
        X = tick(X, 1 if t % 2 == 0 else 0)
        if (t + 1) % 2 == 1:
            s = (t + 1) // 2; U[:, s] = (X[:, 0] & one).astype(np.uint8); M[:, s] = TRAP[(X[:, 0] & np.uint64(0xFFFF)).astype(np.int64)]
    return U, M
def match(U, tpl):
    L = tpl.size; S = U.shape[1]; Mt = np.ones((U.shape[0], S - L + 1), dtype=bool)
    for j in range(L): Mt &= (U[:, j:j + S - L + 1] == tpl[j])
    return Mt
def analyse(rows, U, M, acc, T):
    N, S = U.shape; ME = match(U, E_T)
    first_in = np.where(M.any(axis=1), np.argmax(M, axis=1), -1)            # first sample in the trap (-1: never within horizon)
    # permanence check: once in, always in
    perm_bad = int(sum(1 for i in range(N) if first_in[i] >= 0 and not M[i, first_in[i]:].all()))
    acc['rows'] += N; acc['perm_violations'] += perm_bad
    tau_tick = np.where(first_in >= 0, 2 * first_in + 1, -1)
    acc['never_in_trap'] += int((first_in < 0).sum())
    for s in range(S):
        b = (2 * s + 1) // 200
        acc['atrisk_bin'][b] = acc['atrisk_bin'].get(b, 0) + int(((first_in < 0) | (first_in > s)).sum())   # rows outside the trap at sample s
    for i in range(N):
        if first_in[i] >= 0: acc['entry_hist'][(int(tau_tick[i]) // 200) * 200] = acc['entry_hist'].get((int(tau_tick[i]) // 200) * 200, 0) + 1
        pos = np.flatnonzero(ME[i])
        if pos.size:
            acc['rows_with_E'] += 1; acc['E_count'] += int(pos.size)
            for p in pos:
                tk = 2 * int(p) + 1; acc['E_hist'][(tk // 200) * 200] = acc['E_hist'].get((tk // 200) * 200, 0) + 1
                if first_in[i] >= 0 and first_in[i] <= p: acc['E_in_trap'] += 1; acc['E_in_trap_examples'].append((int(rows[i]), tk, int(tau_tick[i])))
                if first_in[i] >= 0 and p < first_in[i] <= p + 34: acc['entry_during_E'] += 1
def main():
    out, mode = sys.argv[2], sys.argv[3]; t0 = time.time()
    acc = {'rows': 0, 'rows_with_E': 0, 'E_count': 0, 'E_in_trap': 0, 'E_in_trap_examples': [], 'entry_during_E': 0, 'never_in_trap': 0,
           'perm_violations': 0, 'atrisk_bin': {}, 'entry_hist': {}, 'E_hist': {}, 'start0': START0}
    if mode == 'roots':
        T = int(sys.argv[4]); rows = [int(x) for x in sys.argv[5:]]
        U, M = evolve(rows, T)
        for i, r in enumerate(rows):
            pos = np.flatnonzero(match(U[i:i+1], E_T)[0]); fi = int(np.argmax(M[i])) if M[i].any() else -1
            w = None
            if fi >= 0:
                # recover the window code at entry by re-evolving? report sample and tick only
                pass
            print(f"root {r}: E launch ticks {(2*pos+1).tolist()}, first trap entry tick {2*fi+1 if fi>=0 else None}", flush=True)
        return
    if mode == 'random':
        K, N, T, seed = map(int, sys.argv[4:8]); rng = np.random.default_rng(seed); CH = 1 << 14
        rows = [(1 << (K - 1)) | int(x) for x in rng.integers(0, 1 << (K - 1), N, dtype=np.int64)]
        for a in range(0, N, CH):
            sub = rows[a:a + CH]; U, M = evolve(sub, T); analyse(np.array(sub, dtype=object), U, M, acc, T)
            print(f"  chunk {a} done {time.time()-t0:.0f}s", flush=True)
    else:
        lo, hi, T = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]); CH = 1 << 16
        for a in range(lo, hi, CH):
            sub = list(range(a, min(hi, a + CH))); U, M = evolve(sub, T); analyse(np.array(sub, dtype=object), U, M, acc, T)
            print(f"  chunk [{a},{min(hi,a+CH)}) done {time.time()-t0:.0f}s", flush=True)
    S = (T + 1) // 2
    # conditional rate per untrapped row per tick, by 200-tick bin: launches in bin / (sum over samples in bin of at-risk rows * 2 ticks per sample)
    print(f"rows {acc['rows']}, with E {acc['rows_with_E']}, E launches {acc['E_count']}, launches from inside the trap {acc['E_in_trap']}, entries during an E {acc['entry_during_E']}, never in trap by horizon {acc['never_in_trap']}, permanence violations {acc['perm_violations']}, start0={START0}")
    print("entry histogram (tick bin: rows entering):", dict(sorted(acc['entry_hist'].items())))
    print("E launch histogram:", dict(sorted(acc['E_hist'].items())))
    print("bin | at-risk row-samples | launches | launches per untrapped row per tick")
    for b in sorted(acc['atrisk_bin']):
        rs = acc['atrisk_bin'][b]; e = acc['E_hist'].get(b * 200, 0)
        print(f"{b*200:>5} | {rs:>12} | {e:>6} | {e / (2 * rs) if rs else float('nan'):.3e}")
    acc['atrisk_bin'] = {str(k): v for k, v in acc['atrisk_bin'].items()}; acc['entry_hist'] = {str(k): v for k, v in acc['entry_hist'].items()}; acc['E_hist'] = {str(k): v for k, v in acc['E_hist'].items()}
    acc['E_in_trap_examples'] = acc['E_in_trap_examples'][:50]
    json.dump({'args': sys.argv[3:], 'acc': acc, 'wall': time.time() - t0}, open(out, 'w')); print(f"done; wall {time.time()-t0:.1f}s", flush=True)
main()
