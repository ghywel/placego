# Finite right halves beside the alternating centre, evolved exactly (bit-packed), and measured (Cloud, CL757). Own code.
# For each row (support k): the E launches (ticks), the lock time and period, the return word between E's, the passage.
# Usage: python3 -I transient_scan.py MODE OUT.json [args]
#   MODE=exhaustive LO HI T      rows r in [LO, HI) (bit j = cell j+1), horizon T ticks
#   MODE=random KMIN KMAX N T SEED   N random rows for each support k in KMIN..KMAX
import sys, json, time
import numpy as np
E_GAPS = [3, 3, 5, 3, 5, 5, 5, 5]; A_GAPS = [2, 5]
def template(gaps):
    L = sum(gaps) + 1; t = np.zeros(L, dtype=np.uint8); p = 0; t[0] = 1
    for g in gaps: p += g; t[p] = 1
    return t
E_T = template(E_GAPS); A_T = template(A_GAPS); PASS_T = template(E_GAPS + A_GAPS * 4 + E_GAPS + A_GAPS * 7 + E_GAPS)
assert E_T.size == 35 and A_T.size == 8 and PASS_T.size == 180
def evolve(rows, T):
    """rows: int array (python ints or uint64 < 2^63 for support <= 62) -> sampled traces U[N, (T+1)//2] uint8 (ticks 1,3,...)."""
    N = len(rows); K = max(int(r).bit_length() for r in rows)
    nw = (K + T + 2 + 63) // 64
    X = np.zeros((N, nw), dtype=np.uint64)
    for w in range(nw):
        X[:, w] = np.array([(int(r) >> (64 * w)) & ((1 << 64) - 1) for r in rows], dtype=np.uint64)
    S = (T + 1) // 2; U = np.zeros((N, S), dtype=np.uint8)
    U[:, 0] = (X[:, 0] & np.uint64(1)).astype(np.uint8)
    one, s63 = np.uint64(1), np.uint64(63)
    for t in range(1, T):                      # row at tick t -> tick t+1; centre at tick t is black iff t even
        c = np.uint64(1 if t % 2 == 0 else 0)
        left = X << one
        left[:, 1:] |= X[:, :-1] >> s63
        left[:, 0] |= c
        right = X >> one
        right[:, :-1] |= (X[:, 1:] & one) << s63
        X = left ^ (X | right)
        if (t + 1) % 2 == 1: U[:, (t + 1) // 2] = (X[:, 0] & one).astype(np.uint8)
    return U
def match(U, tpl):
    """boolean [N, S-len+1]: template matches at offset s."""
    L = tpl.size; S = U.shape[1]
    if S < L: return np.zeros((U.shape[0], 0), dtype=bool)
    M = np.ones((U.shape[0], S - L + 1), dtype=bool)
    for j in range(L): M &= (U[:, j:j + S - L + 1] == tpl[j])
    return M
def lock_times(U, periods=(2, 5, 7), min_periods=10):
    """per row: (lock sample s0, period) with the smallest s0 among the periods that hold to the end for >= min_periods periods; (-1, 0) if none."""
    N, S = U.shape; best = np.full(N, -1, dtype=np.int64); bestp = np.zeros(N, dtype=np.int64)
    for p in periods:
        D = U[:, p:] != U[:, :-p]
        anyD = D.any(axis=1)
        last = np.where(anyD, D.shape[1] - 1 - np.argmax(D[:, ::-1], axis=1), -1)
        s0 = last + 1
        ok = (S - s0) >= min_periods * p
        take = ok & ((best < 0) | (s0 < best))
        best[take] = s0[take]; bestp[take] = p
    return best, bestp
def analyse(rows, U, ks, acc):
    N, S = U.shape
    ME = match(U, E_T); MP = match(U, PASS_T)
    nE = ME.sum(axis=1)
    lock, per = lock_times(U)
    for i in range(N):
        k = int(ks[i]); a = acc.setdefault(k, {'rows': 0, 'withE': 0, 'maxE': 0, 'latestE_tick': -1, 'latestE_row': None,
                                                'E_launch_ticks': [], 'unlocked': 0, 'lock_max_sample': -1, 'lock_max_row': None,
                                                'lock_sum': 0, 'periods': {}, 'return_words': {}, 'passages': []})
        a['rows'] += 1
        a.setdefault('E_hist', {}); a.setdefault('lock_hist', {}); a.setdefault('E_per_row', {})
        a['E_per_row'][int(nE[i])] = a['E_per_row'].get(int(nE[i]), 0) + 1
        if nE[i]:
            a['withE'] += 1; a['maxE'] = max(a['maxE'], int(nE[i]))
            pos = np.flatnonzero(ME[i]); ticks = (2 * pos + 1).tolist()
            a['E_launch_ticks'].extend(ticks)
            for tk in ticks: b_ = (tk // 200) * 200; a['E_hist'][b_] = a['E_hist'].get(b_, 0) + 1
            if ticks[-1] > a['latestE_tick']: a['latestE_tick'] = ticks[-1]; a['latestE_row'] = int(rows[i])
            if len(pos) >= 2:
                word = []
                for s1, s2 in zip(pos[:-1], pos[1:]):
                    d = int(s2 - s1)
                    if d >= 34 and (d - 34) % 7 == 0:
                        n = (d - 34) // 7; okA = True
                        for m in range(n):
                            seg = U[i, s1 + 34 + 7 * m: s1 + 34 + 7 * m + 8]
                            if seg.size < 8 or not np.array_equal(seg, A_T): okA = False; break
                        word.append(n if okA else f"nonA{d}")
                    else: word.append(f"nonA{d}")
                key = ','.join(map(str, word)); a['return_words'][key] = a['return_words'].get(key, 0) + 1
        if lock[i] < 0: a['unlocked'] += 1
        else:
            a['lock_sum'] += int(lock[i]); a['periods'][int(per[i])] = a['periods'].get(int(per[i]), 0) + 1
            b_ = (int(lock[i]) // 100) * 100; a['lock_hist'][b_] = a['lock_hist'].get(b_, 0) + 1
            if lock[i] > a['lock_max_sample']: a['lock_max_sample'] = int(lock[i]); a['lock_max_row'] = int(rows[i])
        if MP.shape[1] and MP[i].any(): a['passages'].append((int(rows[i]), (2 * np.flatnonzero(MP[i]) + 1).tolist()))
def summary(acc, T):
    print(f"{'k':>3} {'rows':>8} {'withE':>7} {'maxE':>4} {'latestE tick':>12} {'/k':>6} {'unlocked':>8} {'lock mean(smp)':>14} {'lock max(smp)':>13} {'/k':>6} periods | return words")
    for k in sorted(acc):
        a = acc[k]; locked = a['rows'] - a['unlocked']
        print(f"{k:>3} {a['rows']:>8} {a['withE']:>7} {a['maxE']:>4} {a['latestE_tick']:>12} {a['latestE_tick']/k if a['latestE_tick']>0 else 0:>6.1f} {a['unlocked']:>8} "
              f"{(a['lock_sum']/locked if locked else 0):>14.1f} {a['lock_max_sample']:>13} {a['lock_max_sample']/k:>6.1f} {dict(sorted(a['periods'].items()))} | {dict(sorted(a['return_words'].items(), key=lambda kv: -kv[1])[:6])}", flush=True)
    npass = sum(len(a['passages']) for a in acc.values()); print(f"passage E A^4 E A^7 E occurrences: {npass}")
def main():
    mode, out = sys.argv[1], sys.argv[2]; t0 = time.time(); acc = {}
    if mode == 'exhaustive':
        lo, hi, T = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]); CH = 1 << 17
        for a in range(lo, hi, CH):
            rows = np.arange(a, min(hi, a + CH), dtype=np.uint64); ks = [int(r).bit_length() for r in rows.tolist()]
            U = evolve(rows.tolist(), T); analyse(rows, U, ks, acc)
            print(f"  chunk [{a},{min(hi,a+CH)}) done, {time.time()-t0:.0f}s", flush=True)
    else:
        kmin, kmax, n, T, seed = map(int, sys.argv[3:8]); rng = np.random.default_rng(seed); CH = 1 << 16
        for k in range(kmin, kmax + 1):
            rows = [(1 << (k - 1)) | int(x) for x in rng.integers(0, 1 << (k - 1), n, dtype=np.int64)] if k > 1 else [1] * n
            for a in range(0, n, CH):
                sub = rows[a:a + CH]; U = evolve(sub, T); analyse(sub, U, [k] * len(sub), acc)
            print(f"  support {k} done, {time.time()-t0:.0f}s", flush=True)
    summary(acc, int(sys.argv[5]) if mode == 'exhaustive' else int(sys.argv[6]))
    for a in acc.values(): a['E_launch_ticks'] = sorted(a['E_launch_ticks'])[-50:]   # keep the latest 50 per support
    json.dump({'mode': mode, 'args': sys.argv[3:], 'acc': {str(k): v for k, v in acc.items()}, 'wall': time.time() - t0}, open(out, 'w'))
    print(f"done; wall {time.time()-t0:.1f}s", flush=True)
if __name__ == '__main__': main()
