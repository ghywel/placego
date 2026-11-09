# Tables from the transient scans (Cloud, CL757): latest E launch tick against the support, lock times, return words, passages.
import json, sys, numpy as np
files = sys.argv[1:]; acc = {}
for f in files:
    d = json.load(open(f))
    for k, a in d['acc'].items():
        k = int(k); b = acc.setdefault(k, {'rows': 0, 'withE': 0, 'maxE': 0, 'latestE_tick': -1, 'latestE_row': None, 'E_launch_ticks': [],
                                          'unlocked': 0, 'lock_max_sample': -1, 'lock_max_row': None, 'lock_sum': 0, 'periods': {}, 'return_words': {}, 'passages': [], 'horizon': []})
        for key in ('rows', 'withE', 'unlocked', 'lock_sum'): b[key] += a[key]
        b['maxE'] = max(b['maxE'], a['maxE']); b['E_launch_ticks'] += a['E_launch_ticks']
        if a['latestE_tick'] > b['latestE_tick']: b['latestE_tick'] = a['latestE_tick']; b['latestE_row'] = a['latestE_row']
        if a['lock_max_sample'] > b['lock_max_sample']: b['lock_max_sample'] = a['lock_max_sample']; b['lock_max_row'] = a['lock_max_row']
        for p, c in a['periods'].items(): b['periods'][p] = b['periods'].get(p, 0) + c
        for w, c in a['return_words'].items(): b['return_words'][w] = b['return_words'].get(w, 0) + c
        b['passages'] += a['passages']; b['horizon'].append(int(d['args'][2]) if d['mode'] == 'exhaustive' else int(d['args'][3]))
print("| support k | rows | rows with an E | most E's in a row | latest E launch (tick) | latest / k | unlocked at horizon | lock time mean (samples) | lock time max (samples) | max / k | periods (samples) |")
print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
ks = sorted(acc); xs = []; ys = []
for k in ks:
    b = acc[k]; locked = b['rows'] - b['unlocked']
    lt = b['latestE_tick']
    if lt > 0: xs.append(k); ys.append(lt)
    per = ', '.join(f"{p}: {c}" for p, c in sorted(b['periods'].items(), key=lambda kv: int(kv[0])))
    print(f"| {k} | {b['rows']:,} | {b['withE']:,} | {b['maxE']} | {lt if lt>0 else '-'} | {lt/k:.1f} | {b['unlocked']} | {(b['lock_sum']/locked if locked else 0):.1f} | {b['lock_max_sample']} | {b['lock_max_sample']/k:.1f} | {per} |" if lt > 0 else
          f"| {k} | {b['rows']:,} | {b['withE']:,} | {b['maxE']} | - | - | {b['unlocked']} | {(b['lock_sum']/locked if locked else 0):.1f} | {b['lock_max_sample']} | {b['lock_max_sample']/k:.1f} | {per} |")
if len(xs) >= 3:
    A = np.vstack([xs, np.ones(len(xs))]).T; sl, ic = np.linalg.lstsq(A, ys, rcond=None)[0]
    print(f"\nleast-squares line through (k, latest E launch tick): slope {sl:.2f}, intercept {ic:.1f}; max ratio latest/k = {max(y/x for x,y in zip(xs,ys)):.1f} at k = {max(zip(xs,ys), key=lambda t: t[1]/t[0])[0]}")
rw = {}
for b in acc.values():
    for w, c in b['return_words'].items(): rw[w] = rw.get(w, 0) + c
print("\nreturn words between consecutive E's (A-counts; nonA<d> = the stretch is not a run of A's), all supports:")
for w, c in sorted(rw.items(), key=lambda kv: -kv[1])[:40]: print(f"  {w}: {c}")
viol = [w for w in rw if any(a == '4' and b_ in ('4', '6') for a, b_ in zip(w.split(','), w.split(',')[1:]))]
print("return words with a 4 followed by 4 or 6 (grammar violations):", viol if viol else "none")
print("passage occurrences:", sum(len(b['passages']) for b in acc.values()))
# time profiles where recorded (runs after the histogram patch)
for f in files:
    d = json.load(open(f))
    for k, a in d['acc'].items():
        if a.get('E_hist'):
            eh = dict(sorted((int(x), v) for x, v in a['E_hist'].items())); lh = dict(sorted((int(x), v) for x, v in a['lock_hist'].items()))
            print(f"\n{f}, support {k}: E launches by 200-tick bin: {eh}")
            print(f"  locks by 100-sample bin: {lh}")
            print(f"  E's per row: {dict(sorted((int(x), v) for x, v in a['E_per_row'].items()))}")
print("rows with the most E's:", max(b['maxE'] for b in acc.values()))
