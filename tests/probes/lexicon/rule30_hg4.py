#!/usr/bin/env python3
"""rule30_hg4.py: HG4, the four-period-horizon potential check of RULE30-GPT.md §G166 (GPT's design; requested in
GC201; claimed by Local in CLOUD-LOCAL.md at 1f4958a before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_hg4.py
COST:       seconds expected; caps 120 CPU s and 256 MiB RSS (GPT's).

Domain. The common-period-q clock-aligned compatible graph of rule30_gpt_cycle_obstructions.py: a state is an
adjacent pair (A, B) of q-bit temporal words aligned so the front arrives at phase 0; each child C of (A, B) gives
an edge to the pair (B, C) rotated by the waiting time d of B from phase 0 (d = 0 for a zero driver), with doubled
slope-5/2 reward w = 2d - 5. Restricted to G160's arrival gate at phase 0 (A nonzero: A(q - 1) = 1; A = 0:
B(0) XOR B(q - 1) = 1), plus the zero state. H_0 = 0 and H_(n+1)(v) = max(0, max over gated edges v -> u of
w + H_n(u)). The graph helpers (predecessor, waiting, children, bit) are imported from GPT's scripts.

PREDICTIONS, GPT's, published in RULE30-GPT.md §G166 before this run:
  HG-P1 (blind): H_(4q+1) = H_(4q) for every q in 1, 2, 4, 8.
  HG-U (blind, the unexpected check): the same stability at q = 6, despite G10's zero-weight slope-5/2 cycle; a q = 6
        failure does not refute HG-P1.
  HG-C1 (control): independent forward bit equations and scalar reset scans agree with every tested edge for q <= 4,
        including gate closure.
  HG-C2 (control, existing record): H_n never exceeds G10's least potential on gated states; that potential's
        full-domain maxima are 0, 0, 6, 45 at q = 1, 2, 4, 8 and 21 at q = 6.
  HG-CF (counterfactual): H_0 must be rejected at q = 4 by the gated edge (8, 8) -> (8, 0), delay 4, reward 3.
Reported for each q: the first stable horizon if it occurs by 4q, the exact gated maximum of H_(4q), and whether the
4q + 1 inequality holds at every gated vertex. A failure keeps a violating edge, its deficit, and a maximizing path
of at most 4q + 1 edges verified by literal time-bit scans.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.49 s, peak RSS 55.7 MiB, far inside the caps). Controls: HG-C1 PASS at
q <= 4 (every edge's literal forward equation and next-black delay); HG-C2 PASS at every q (H_n never exceeds G10's
least potential on gated states, whose maxima are 0, 0, 6, 21, 45 at q = 1, 2, 4, 6, 8); gate closure PASS; HG-CF
PASS. HG-P1 REFUTED, at q = 8 only: H_(4q) is stable at q = 1, 2, 4 (first stable horizons 0, 0, 4), but at q = 8
H_33 != H_32, with 80 violating edges (one: (241, 1) -> (128, 80), reward -3, deficit 8). HG-U HELD: q = 6 is stable
from horizon 21 <= 24. Gated maxima of H_(4q): 0, 0, 6, 21, 45, equal to G10's maxima. Failure witness (required by
G166): from (A, B) = (143, 8), H_33 = 17 > H_32 = 9 along a path of exactly 33 edges, elapsed 91, reward 17; all
triple equations and next-black scans pass, independently of the DP. The witness words, as time-bit integers at
q = 8 (A, B, then each child, phases un-aligned): [143, 8, 5, 14, 245, 243, 4, 93, 247, 85, 69, 96, 70, 60, 116, 151,
71, 224, 69, 63, 116, 149, 71, 228, 69, 71, 4, 133, 7, 5, 4, 6, 4, 4, 0]; its 34 aligned states are distinct (GC202).
GPT's GC204 audit: the witness is not rooted (its backward ancestry cycles after 4,746 steps). Descriptive, beyond
the prediction: continuing
the recursion at q = 8, it first stabilises at horizon 85 (about 10.6 q), with maximum 45. The first run printed no
witness because the failure report had not yet been written; it was added and the whole script re-run, with the
same verdicts.
"""
import resource
import sys
import time
from array import array
from collections import deque

sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from rule30_gpt_local_front import predecessor          # noqa: E402
from rule30_gpt_front import waiting                    # noqa: E402
from rule30_gpt_cycles import bit                       # noqa: E402
from rule30_gpt_waiting import children                 # noqa: E402

CPU_CAP, MEM_CAP = 120.0, 256 * 1024 * 1024
resource.setrlimit(resource.RLIMIT_CPU, (125, 125))
G10_MAX = {1: 0, 2: 0, 4: 6, 6: 21, 8: 45}


def rotate(w, d, p):
    d %= p
    return ((w >> d) | (w << (p - d))) & ((1 << p) - 1)


def gated(state, p):
    a, b = state >> p, state & ((1 << p) - 1)
    if a:
        return bit(a, p - 1, p) == 1
    return (bit(b, 0, p) ^ bit(b, p - 1, p)) == 1


def aligned_edges(p):
    """Every edge of the aligned graph, as (source, target, d), one per child pair (b, c)."""
    mask = (1 << p) - 1
    out = []
    for child in range(1 << (2 * p)):
        b, c = child >> p, child & mask
        parent = predecessor(child, p)
        d = (b & -b).bit_length() if b else 0
        out.append((parent, (rotate(b, d, p) << p) | rotate(c, d, p), d))
    return out


def least_potential(p, edges):
    """G10's least potential on the full aligned domain (the existing relaxation arithmetic)."""
    count = 1 << (2 * p)
    into = [[] for _ in range(count)]
    for s, t, d in edges:
        into[t].append((s, 2 * d - 5))
    values = array('i', [0]) * count
    queue, queued = deque(range(count)), bytearray([1]) * count
    while queue:
        t = queue.popleft()
        queued[t] = 0
        for s, w in into[t]:
            if values[t] + w > values[s]:
                values[s] = values[t] + w
                if not queued[s]:
                    queue.append(s)
                    queued[s] = 1
    return values


def hg4(p, edges, lp):
    """Bounded-horizon rewards with two rolling arrays; HG-C2 (H_n <= least potential) checked at every n."""
    count = 1 << (2 * p)
    isv = bytearray(count)
    for v in range(count):
        isv[v] = 1 if (v == 0 or gated(v, p)) else 0
    closure_ok = True
    src, dst, wgt = array('i'), array('i'), array('i')
    for s_, t, d in edges:
        if isv[s_] and s_ != 0:
            closure_ok &= bool(isv[t])
        if isv[s_] and isv[t]:
            src.append(s_)
            dst.append(t)
            wgt.append(2 * d - 5)
    prev = array('i', [0]) * count
    c2 = True
    first_stable = None
    H4q = None
    for n in range(1, 4 * p + 2):
        cur = array('i', [0]) * count
        for i in range(len(src)):
            val = wgt[i] + prev[dst[i]]
            if val > cur[src[i]]:
                cur[src[i]] = val
        c2 &= all(cur[v] <= lp[v] for v in range(count) if isv[v])
        if first_stable is None and cur == prev:
            first_stable = n - 1
        if n == 4 * p:
            H4q = cur
        prev = cur
    H4q1 = prev
    stable = H4q1 == H4q
    viol = [(src[i], dst[i], wgt[i], wgt[i] + H4q[dst[i]] - H4q[src[i]]) for i in range(len(src))
            if wgt[i] + H4q[dst[i]] > H4q[src[i]]]
    gmax = max(H4q[v] for v in range(count) if isv[v])
    return dict(nvert=sum(isv), first_stable=first_stable, stable=stable, viol=viol, closure_ok=closure_ok,
                c2=c2, gmax=gmax)


def control_c1(p, edges):
    """Literal forward equation S C = A XOR (B OR C) for every edge, and the scalar next-black delay."""
    mask = (1 << p) - 1
    ok = True
    for s, t, d in edges:
        a, b = s >> p, s & mask
        tb, tc = t >> p, t & mask
        b2, c = rotate(tb, -d, p), rotate(tc, -d, p)        # un-align the target
        ok &= b2 == b
        ok &= all(bit(c, x + 1, p) == (bit(a, x, p) ^ (bit(b, x, p) | bit(c, x, p))) for x in range(p))
        if b:
            u = 0
            while not bit(b, u, p):
                u += 1
            ok &= u + 1 == d == waiting(b, p)[0]
        else:
            ok &= d == 0
    return ok


def failure_witness(p):
    """G166's failure report: a maximizing path of at most 4q + 1 edges for a vertex whose H_(4q+1) exceeds
    H_(4q), verified by literal time-bit scans independently of the DP values; then (descriptive) the first stable
    horizon if the same recursion is continued."""
    mask = (1 << p) - 1
    edges = aligned_edges(p)
    count = 1 << (2 * p)
    isv = bytearray(count)
    for v in range(count):
        isv[v] = 1 if (v == 0 or gated(v, p)) else 0
    E = [(s_, t, 2 * d - 5, d) for s_, t, d in edges if isv[s_] and isv[t]]
    Hs = [array('i', [0]) * count]
    n = 0
    while True:
        n += 1
        cur = array('i', [0]) * count
        for s_, t, w, d in E:
            if w + Hs[-1][t] > cur[s_]:
                cur[s_] = w + Hs[-1][t]
        Hs.append(cur)
        if cur == Hs[-2] or n >= 40 * p:
            break
    stable_at = n - 1 if Hs[-1] == Hs[-2] else None
    N = 4 * p + 1
    v0 = max((v for v in range(count) if isv[v] and Hs[N][v] > Hs[N - 1][v]), key=lambda v: Hs[N][v] - Hs[N - 1][v])
    path, v, k = [], v0, N
    while k > 0 and Hs[k][v] > 0:
        s_, t, w, d = next(e for e in E if e[0] == v and e[2] + Hs[k - 1][e[1]] == Hs[k][v])
        path.append((s_, t, d))
        v, k = t, k - 1
    words, phase, elapsed = [v0 >> p, v0 & mask], 0, 0
    for s_, t, d in path:
        phase, elapsed = (phase + d) % p, elapsed + d
        words.append(rotate(t & mask, -phase, p))
    lit = all(bit(words[j + 1], x + 1, p) == (bit(words[j - 1], x, p) ^ (bit(words[j], x, p) | bit(words[j + 1], x, p)))
              for j in range(1, len(words) - 1) for x in range(p))
    clock = 0
    for wd in words[1:-1]:
        if wd:
            while not bit(wd, clock, p):
                clock += 1
            clock += 1
    reward = 2 * elapsed - 5 * len(path)
    ok = lit and clock == elapsed and reward == Hs[N][v0] and len(path) <= N
    print('FAILURE WITNESS q = %d: start (A, B) = %r, H_(4q+1) = %d > H_(4q) = %d; path of %d edges, elapsed %d, '
          'reward %d; literal triple equations and next-black scans %s' % (p, (v0 >> p, v0 & mask), Hs[N][v0],
                                                                        Hs[N - 1][v0], len(path), elapsed, reward,
                                                                        'PASS' if ok else 'FAIL'))
    print('  words (time-bit integers) %r' % words)
    print('  descriptive: continuing the same recursion, first stable horizon %s (cap %d); max H there %d'
          % (stable_at, 40 * p, max(Hs[-1][v] for v in range(count) if isv[v])))


def main():
    t0 = time.process_time()
    verdict = {}
    for p in (1, 2, 4, 6, 8):
        edges = aligned_edges(p)
        lp = least_potential(p, edges)
        res = hg4(p, edges, lp)
        c2 = max(lp) == G10_MAX[p] and res['c2']
        c1 = control_c1(p, edges) if p <= 4 else None
        verdict[p] = res['stable']
        print('q = %d: gated vertices %d, H_(4q) gated maximum %d, first stable horizon %s, H_(4q+1) = H_(4q): %s, '
              'violations %d; G10 least potential max %d; HG-C2 %s; HG-C1 %s; gate closure %s'
              % (p, res['nvert'], res['gmax'], res['first_stable'], res['stable'], len(res['viol']), max(lp),
                 'PASS' if c2 else 'FAIL', {True: 'PASS', False: 'FAIL', None: 'n/a'}[c1],
                 'PASS' if res['closure_ok'] else 'FAIL'), flush=True)
        if res['viol']:
            v, u, w, deficit = max(res['viol'], key=lambda x: x[3])
            print('  violating edge %r -> %r, reward %d, deficit %d' % ((v >> p, v & ((1 << p) - 1)),
                                                                      (u >> p, u & ((1 << p) - 1)), w, deficit))
        if time.process_time() - t0 > CPU_CAP or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > MEM_CAP:
            print('CAP REACHED after q = %d: partial, not a pass' % p)
            return 2
        if p == 4:
            e = [(s, t, d) for s, t, d in edges if s == (8 << 4) | 8 and t == (8 << 4) | 0]
            cf = bool(e) and e[0][2] == 4 and 2 * 4 - 5 == 3 and gated((8 << 4) | 8, 4) and gated((8 << 4) | 0, 4)
            print('HG-CF', 'PASS (H_0 rejected by the gated edge (8, 8) -> (8, 0), delay 4, reward 3)' if cf else 'FAIL')
    for p in (1, 2, 4, 6, 8):
        if not verdict[p]:
            failure_witness(p)
    print('HG-P1', 'HELD' if all(verdict[q] for q in (1, 2, 4, 8)) else 'REFUTED', {q: verdict[q] for q in (1, 2, 4, 8)})
    print('HG-U', 'HELD' if verdict[6] else 'REFUTED')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
