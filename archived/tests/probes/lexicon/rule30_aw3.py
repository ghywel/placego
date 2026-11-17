#!/usr/bin/env python3
"""rule30_aw3.py: AW3, entry 06's exact actual-wall run maxima at P = 8 and P = 9 (Local's run, after AW, AW2 and GPT's
GC316; claimed in CLOUD-LOCAL.md with these predictions pushed before the script was run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_aw3.py
COST:       minutes expected; caps 2,400 CPU s, 2 GiB peak RSS, strip width 14. P = 9 runs only if P = 8 finishes.

Method, AW and AW2 combined, unchanged: (1) lower bound: the longest bounded row-0 white runs (strictly in x < 0,
bounded by black cells, 40 columns deep) over pairs of P-periodic columns 0, 1 with a PERIODIC right continuation;
(2) upper bound: every pair whose forced left half beats that lower bound gets GPT's width-n strip test (GC313) at
n = 1 .. 14; a width with no cycle certifies no right continuation. If every excess pair is refuted, the lower bound
is the exact actual-wall maximum within the census, and by GPT's GC316 re-anchoring (Theorem B puts any bounded run
within 2P - 1 columns, inside the 40-column census for P <= 9) at every depth.

PREDICTIONS, Local's, published before the run (blind unless marked):
  AW3-P1 (blind, uncertain): at P = 8 the exact actual-wall odd maximum is below 2P - 5 = 11.
  AW3-P2 (blind, uncertain): at P = 8 the exact actual-wall even maximum is below 2P - 2 = 14.
  AW3-P3 (blind, uncertain): every excess pair at P = 8 is refuted by width 14 (so the maxima are decided).
  AW3-C1 (control): the method reproduces AW/AW2's exact maxima at P = 3 .. 7 (odd 1, 1, 5, 5, 5; even 4, 6, 2, 4, 6).
  AW3-U (the unexpected check): some excess pair needs a refuting width above 5 (AW2's largest) at P = 8 or 9.
A pair that survives to width 14 stays undecided and is reported, never called admissible.
OUTCOME, 2026-10-07 18:10 (M5, one run at commit 16d0665; CPU 14.0 s, peak RSS 164 MiB, no cap). AW3-C1 PASS
(P = 3 .. 7 reproduce exactly). P = 8: 119 pairs with a periodic continuation give lower bounds odd 7, even 6; of 632
excess pairs 631 are refuted (widths <= 5) and ONE survives every width to 14: (column 0, column 1) = (83, 157), whose
forced left half has an odd run of 9 (and even runs <= 4). P = 9: 195 periodic-admissible pairs, lower bounds odd 7,
even 6; all 1,794 excess pairs refuted (widths <= 7), so the exact actual-wall maxima at P = 9 are odd 7, even 6.
The script's verdict lines printed P1 and P2 as UNDECIDED because its logic treated any undecided pair as undecided;
scored against the predictions as worded, both HELD: the P = 8 odd maximum is 7 or 9, below 11 either way, and the
even maximum is exactly 6 (the survivor's even runs are <= 4), below 14. AW3-P3 REFUTED (one survivor at width 14).
AW3-U PASS (refuting widths up to 7). So among P = 4 .. 9, 2P - 5 is attained on an actual wall only at P = 5; the
P = 8 odd maximum is undecided between 7 and 9 pending the survivor (83, 157).
"""
import resource
import sys

CAP_CPU, WMAX = 2400.0, 14


def cpu():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime + r.ru_stime


def strip_has_cycle(c0, c1, P, n):
    nxt = {}
    for p in range(P):
        a0, a1, b1 = (c0 >> p) & 1, (c1 >> p) & 1, (c1 >> ((p + 1) % P)) & 1
        for s in range(1 << n):
            if b1 != a0 ^ (a1 | (s & 1)):
                nxt[(p, s)] = ()
                continue
            out = []
            for b in (0, 1):
                full = a1 | (s << 1) | (b << (n + 1))          # bit 0 = cell 1, bit k = cell k + 1
                s2 = 0
                for i in range(1, n + 1):                      # new cells 2 .. n + 1 (bits 1 .. n)
                    l, c, r = (full >> (i - 1)) & 1, (full >> i) & 1, (full >> (i + 1)) & 1
                    s2 |= (l ^ (c | r)) << (i - 1)
                out.append(((p + 1) % P, s2))
            nxt[(p, s)] = tuple(out)
    indeg_alive = set(v for v in nxt if nxt[v])
    changed = True
    while changed:
        changed = False
        for v in list(indeg_alive):
            if not any(w in indeg_alive for w in nxt[v]):
                indeg_alive.discard(v)
                changed = True
    return bool(indeg_alive)


def periodic_admissible(P):
    def succ(u, v):
        out = [0]
        for t in range(P):
            need = ((v >> ((t + 1) % P)) & 1) ^ ((u >> t) & 1)
            if (v >> t) & 1:
                if need != 1:
                    return []
                out = [o | (b << t) for o in out for b in (0, 1)]
            else:
                out = [o | (need << t) for o in out]
        return out
    nodes = {(a, b): {(b, w) for w in succ(a, b)} for a in range(1 << P) for b in range(1 << P)}
    alive = set(nodes)
    changed = True
    while changed:
        changed = False
        for v in list(alive):
            if not (nodes[v] & alive):
                alive.discard(v)
                changed = True
    return alive


def runs(c0, c1, P):
    cols = [[(c1 >> t) & 1 for t in range(P)], [(c0 >> t) & 1 for t in range(P)]]
    for j in range(1, 41):
        r, r2 = cols[-1], cols[-2]
        cols.append([r[(t + 1) % P] ^ (r[t] | r2[t]) for t in range(P)])
    row = [cols[1 + k][0] for k in range(41)]
    best = {'odd': 0, 'even': 0}
    k = 1
    while k <= 40:
        if row[k] == 0 and row[k - 1] == 1:
            e = k
            while e <= 40 and row[e] == 0:
                e += 1
            if e <= 40:
                key = 'odd' if (e - k) % 2 else 'even'
                best[key] = max(best[key], e - k)
            k = e
        k += 1
    return best



def decide(P, report):
    adm = periodic_admissible(P)
    lo = {'odd': 0, 'even': 0}
    for c0, c1w in adm:
        if c0:
            b = runs(c0, c1w, P)
            lo['odd'], lo['even'] = max(lo['odd'], b['odd']), max(lo['even'], b['even'])
    excess = []
    for c0 in range(1, 1 << P):
        for c1w in range(1 << P):
            b = runs(c0, c1w, P)
            if b['odd'] > lo['odd'] or b['even'] > lo['even']:
                excess.append((c0, c1w, b))
    widths, undecided = [], []
    for c0, c1w, b in excess:
        if cpu() > CAP_CPU:
            print('CAP during P = %d' % P)
            sys.exit(1)
        w = next((n for n in range(1, WMAX + 1) if not strip_has_cycle(c0, c1w, P, n)), None)
        (undecided if w is None else widths).append(w if w is not None else (c0, c1w, b))
    if report:
        print('P = %d: periodic-admissible pairs %d; lower bounds odd %d even %d; excess pairs %d; refuted %d '
              '(max width %s); undecided %d %s' % (P, len(adm), lo['odd'], lo['even'], len(excess), len(widths),
              max(widths) if widths else '-', len(undecided), undecided[:4]))
    return lo, widths, undecided


known = {3: (1, 4), 4: (1, 6), 5: (5, 2), 6: (5, 4), 7: (5, 6)}
c1 = True
for P in range(3, 8):
    lo, widths, und = decide(P, False)
    c1 &= (lo['odd'], lo['even']) == known[P] and not und
print('AW3-C1', 'PASS' if c1 else 'FAIL')
lo8, w8, u8 = decide(8, True)
print('AW3-P1', 'HELD' if not u8 and lo8['odd'] < 11 else ('UNDECIDED' if u8 else 'REFUTED'))
print('AW3-P2', 'HELD' if not u8 and lo8['even'] < 14 else ('UNDECIDED' if u8 else 'REFUTED'))
print('AW3-P3', 'HELD' if not u8 else 'REFUTED')
u = bool(w8) and max(w8) > 5
if cpu() < CAP_CPU / 3:
    lo9, w9, u9 = decide(9, True)
    u |= bool(w9) and max(w9) > 5
else:
    print('P = 9 skipped: CPU budget')
print('AW3-U', 'PASS' if u else 'FAIL')
print('CPU %.1f s, peak RSS %.1f MiB' % (cpu(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20))
