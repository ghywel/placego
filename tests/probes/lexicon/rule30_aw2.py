#!/usr/bin/env python3
"""rule30_aw2.py: AW2, settling AW's open negatives by GPT's width-n strip certificates (GC313). Local's run, claimed in
CLOUD-LOCAL.md with these predictions pushed before the script was run.

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_aw2.py
COST:       minutes expected; caps 1,200 CPU s, 1 GiB peak RSS, width 12.

Question. AW (rule30_aw.py) found entry 06's bounds attained on pairs of P-periodic columns 0 and 1 that have a
PERIODIC right continuation, and could not decide the rest. GPT's GC313: for width n, the states (phase mod P, the n
cells right of column 1) form a finite graph, in which column 1's equation constrains the first cell and the far-right
input is free. A right strip exists for all t >= 0 iff this graph has a cycle (the free initial row enters it at phase
0), and an actual right continuation exists iff there are cycles at every width (compactness). So a width with no cycle
certifies that the pair is not admissible. Method: for P = 3 .. 7, take every pair (column 0 nonzero) whose forced
left half has a bounded row-0 white run longer than AW's admissible maxima (the census of rule30_aw.py, 40 columns
deep), and look for the least width n <= 12 whose strip graph has no cycle.

PREDICTIONS, Local's, published before the run:
  AW2-P1 (blind, uncertain): the formal witnesses of S106 that AW could not place (odd 3 at P = 4, odd 9 at P = 7) are
          refuted at some width <= 12.
  AW2-P2 (blind, uncertain): at every P = 3 .. 7 every pair exceeding AW's admissible maxima is refuted by width 12,
          so the admissible maxima are exactly AW's (odd 1, 1, 5, 5, 5 and even 4, 6, 2, 4, 6 at P = 3 .. 7).
  AW2-C1 (control): every pair AW found admissible survives at every width tried (a periodic continuation is a real one).
  AW2-C2 (control): GPT's 01/11 at P = 2 is refuted at width 1.
  AW2-U (the unexpected check): the refuting width is not always 1, i.e. some pair passes column 1's one-step
          condition and still dies only at a larger width, so the strip graph does more than the one-step test.
A pair that survives to width 12 stays undecided; it is not called admissible.
OUTCOME: not yet run.
"""
import resource
import sys

CAP_CPU, WMAX = 1200.0, 12


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


AWMAX = {3: (1, 4), 4: (1, 6), 5: (5, 2), 6: (5, 4), 7: (5, 6)}          # AW's admissible (odd, even) maxima
c2 = not strip_has_cycle(0b10, 0b11, 2, 1)
print('AW2-C2', 'PASS' if c2 else 'FAIL')
c1 = True
p1_targets, p1_refuted = [], []
p2 = True
u = False
for P in range(3, 8):
    adm = periodic_admissible(P)
    for c0, c1w in list(adm)[:30]:                                         # control sample of AW's survivors
        if c0:
            c1 &= all(strip_has_cycle(c0, c1w, P, n) for n in range(1, 7))
    oddmax, evenmax = AWMAX[P]
    excess = []
    for c0 in range(1, 1 << P):
        for c1w in range(1 << P):
            b = runs(c0, c1w, P)
            if b['odd'] > oddmax or b['even'] > evenmax:
                excess.append((c0, c1w, b))
    refuted, undecided, widths = 0, [], []
    for c0, c1w, b in excess:
        w = next((n for n in range(1, WMAX + 1) if not strip_has_cycle(c0, c1w, P, n)), None)
        if cpu() > CAP_CPU:
            print('CAP at P = %d' % P)
            sys.exit(1)
        if w is None:
            undecided.append((c0, c1w, b))
        else:
            refuted += 1
            widths.append(w)
            u |= w > 1
        if (P == 4 and b['odd'] == 3) or (P == 7 and b['odd'] == 9):
            p1_targets.append((P, c0, c1w))
            if w is not None:
                p1_refuted.append((P, c0, c1w, w))
    p2 &= not undecided
    print('P = %d: pairs exceeding AW maxima %d; refuted %d (widths %s); undecided to width %d: %s'
          % (P, len(excess), refuted, sorted(set(widths)), WMAX, [(c0, c1w, bb) for c0, c1w, bb in undecided][:6]))
print('AW2-C1', 'PASS' if c1 else 'FAIL')
print('AW2-P1', 'HELD' if p1_targets and len(p1_refuted) == len(p1_targets) else 'REFUTED',
      '(targets %d, refuted %d)' % (len(p1_targets), len(p1_refuted)))
print('AW2-P2', 'HELD' if p2 else 'REFUTED')
print('AW2-U', 'PASS' if u else 'FAIL')
print('CPU %.1f s, peak RSS %.1f MiB' % (cpu(), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20))
