# Per-row re-analysis of a cohort (Cloud, CL758): gate-trap entry tau, early short-period lock (periods 2/5/7 holding from
# some sample < 100 to the horizon), E launches split into absorbed (trap entry during the 35-sample block) and live
# (no entry during the block), the at-risk set = rows neither in the gate trap nor early-locked, and the conditional E
# launch rate per such row per tick by 200-tick bin; the return words of the live E's. Own code.
# Usage: python3 -I trap_measure2.py TRAPCODES OUT.json K N T SEED   (env START0=1 as in trap_measure.py)
import sys, os, json, time, numpy as np
sys_argv = sys.argv[:]; sys.argv = ['x', sys_argv[1], 'none', 'none']; ns = {}
exec(open('trap_measure.py').read().split("def main():")[0], ns)
evolve, match, E_T, template = ns['evolve'], ns['match'], ns['E_T'], ns['template']
A_T = template([2, 5])
out, K, N, T, seed = sys_argv[2], int(sys_argv[3]), int(sys_argv[4]), int(sys_argv[5]), int(sys_argv[6])
rng = np.random.default_rng(seed); rows = [(1 << (K - 1)) | int(x) for x in rng.integers(0, 1 << (K - 1), N, dtype=np.int64)]
t0 = time.time(); CH = 1 << 14
S = (T + 1) // 2; nb = (T // 200) + 1
atrisk = np.zeros(nb, dtype=np.int64); launches = np.zeros(nb, dtype=np.int64)
tot = {'rows': 0, 'never_trapped': 0, 'early_lock': 0, 'never_trapped_and_not_early_lock': 0, 'early_lock_and_trapped': 0,
       'E_rows': 0, 'E_total': 0, 'E_absorbed': 0, 'E_live': 0, 'rows_2E': 0, 'live_return_words': {}, 'E_in_trap': 0,
       'first_E_tick_live': [], 'lock_periods_never_trapped': {}}
for a in range(0, N, CH):
    sub = rows[a:a + CH]; U, M = evolve(sub, T); n = len(sub)
    first_in = np.where(M.any(axis=1), np.argmax(M, axis=1), -1)
    # early lock: for p in 2,5,7 the trace is p-periodic from some sample s0 < 100 to the horizon
    early = np.zeros(n, dtype=bool); period = np.zeros(n, dtype=np.int64)
    for p in (2, 5, 7):
        D = U[:, p:] != U[:, :-p]; anyD = D.any(axis=1)
        last = np.where(anyD, D.shape[1] - 1 - np.argmax(D[:, ::-1], axis=1), -1); s0 = last + 1
        ok = s0 < 100
        period[ok & ~early] = p; early |= ok
    ME = match(U, E_T)
    for i in range(n):
        tot['rows'] += 1
        nt = first_in[i] < 0
        if nt: tot['never_trapped'] += 1
        if early[i]: tot['early_lock'] += 1
        if nt and not early[i]: tot['never_trapped_and_not_early_lock'] += 1
        if early[i] and not nt: tot['early_lock_and_trapped'] += 1
        if nt: tot['lock_periods_never_trapped'][int(period[i])] = tot['lock_periods_never_trapped'].get(int(period[i]), 0) + 1
        # at-risk samples: outside the trap and not early-locked (early-locked rows are removed from the start)
        if not early[i]:
            end = S if nt else int(first_in[i])
            for s in range(end):
                atrisk[(2 * s + 1) // 200] += 1
        pos = np.flatnonzero(ME[i])
        if pos.size:
            tot['E_rows'] += 1; tot['E_total'] += int(pos.size)
            if pos.size >= 2: tot['rows_2E'] += 1
            for p in pos:
                tk = 2 * int(p) + 1
                if first_in[i] >= 0 and first_in[i] <= p: tot['E_in_trap'] += 1
                absorbed = first_in[i] >= 0 and p < first_in[i] <= p + 34
                if absorbed: tot['E_absorbed'] += 1
                else: tot['E_live'] += 1; tot['first_E_tick_live'].append(tk)
                if not early[i]: launches[tk // 200] += 1
            if pos.size >= 2:
                word = []
                for s1, s2 in zip(pos[:-1], pos[1:]):
                    d = int(s2 - s1)
                    if d >= 34 and (d - 34) % 7 == 0:
                        nA = (d - 34) // 7; okA = all(np.array_equal(U[i, s1 + 34 + 7 * m: s1 + 34 + 7 * m + 8], A_T) for m in range(nA))
                        word.append(nA if okA else f"nonA{d}")
                    else: word.append(f"nonA{d}")
                key = ','.join(map(str, word)); tot['live_return_words'][key] = tot['live_return_words'].get(key, 0) + 1
    print(f"  chunk {a} done {time.time()-t0:.0f}s", flush=True)
print(f"rows {tot['rows']}: never in the gate trap by {T}: {tot['never_trapped']}; early short-period lock: {tot['early_lock']}; never trapped and not early-locked: {tot['never_trapped_and_not_early_lock']}; early-locked but later trapped: {tot['early_lock_and_trapped']}")
print(f"lock periods of the never-trapped rows (0 = none found): {dict(sorted(tot['lock_periods_never_trapped'].items()))}")
print(f"E rows {tot['E_rows']}, E launches {tot['E_total']}: absorbed (trap entry during the block) {tot['E_absorbed']}, live {tot['E_live']}, from inside the trap {tot['E_in_trap']}; rows with >= 2 E's {tot['rows_2E']}; return words of rows with >= 2 E's: {tot['live_return_words']}")
print(f"live E launch ticks: {sorted(tot['first_E_tick_live'])[:40]}{'...' if len(tot['first_E_tick_live'])>40 else ''}")
print("bin | at-risk row-samples (not trapped, not early-locked) | launches (such rows) | launches per such row per tick")
for b in range(nb):
    if atrisk[b]: print(f"{b*200:>5} | {int(atrisk[b]):>12} | {int(launches[b]):>6} | {launches[b]/(2*atrisk[b]):.3e}")
tot['atrisk'] = atrisk.tolist(); tot['launches'] = launches.tolist(); tot['first_E_tick_live'] = sorted(tot['first_E_tick_live'])
json.dump(tot, open(out, 'w')); print(f"done; wall {time.time()-t0:.1f}s")
