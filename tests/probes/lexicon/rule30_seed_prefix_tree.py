#!/usr/bin/env python3
"""rule30_seed_prefix_tree.py: the prefix-tree search over the ordinary seeds of GC1184's birth representation, proposed in
CHAT-LEDGER L676 and corrected by GPT in GC1192.

Why a prefix suffices (L676, GC1192). The right-edge diagonals of a finite seed with rightmost black at site 0 obey
V_0 = 1, V_(-1) = 0, V_j(t + 1) = V_j(t) XOR (V_(j-1)(t) OR V_(j-2)(t)): a triangular permutation, so V_0 .. V_(k-1) at
any T depend only on those k initial bits and the prefix orbit is purely periodic. GC1184's child depth i is
V_(i+2-p)(T), T = N - p - 1, so a W-tick child test (clock and the child phase's certified cuts) reads edge indices up
to W + 2 - p; with k known bits the safe window is W = k - 3 in both phases (GC1192's correction). A residue dead at a
prefix is dead for every extension (GC1190). First sample 1 gives the headers 1011 (r = 0) and 1100 (r = 1) (GC1191);
every binary continuation is searched, the zero rays of finite seeds included, with no grammar pruning (GC1192).
If every branch closes with W <= W*, GC1192's guard B_j = W* + 4j and the proved promotion and age accounting would
give, subject to GPT's carrying read, a bound on every band at depth d >= 6 of W* + 4 floor((d - p)/2) - 1.

The evaluator runs every alive residue of a node at once (numpy): the child's clamped evolution over W ticks and the
cuts by an Aho-Corasick automaton on the child's visible samples. Caps: k <= 40 bits, period horizon 2^16, plus a node
cap and a wall-clock cap so that a branching frontier is reported rather than run without end.

RUN-ON:     cpu, numpy, the certified cut lists in the RLK scratch.
COMMAND:    python3 tests/probes/lexicon/rule30_seed_prefix_tree.py [KCAP=40] [NODECAP=300000] [MINUTES=45]

Record searched (record_find, 2026-10-13 18:33 BST): 'prefix tree|prefix-tree' -> 6 hits in 3 files (GC1192, GPT's
rule30_seed_prefix_scope.py control, and this file); 'seed prefix' -> 2 hits in 2 files (a PERIOD-TWO board line on
another object, and this file); with the searches of rule30_birth_deficit_census.py (L672 .. L676).

PREDICTIONS (written 2026-10-13 18:33 BST, before any run).
  C0 must hold (the instrument): the vectorized evaluator agrees with verdict_fast (L672) on alive/dead for 2,000 random
     child rows in each phase, windows 3 .. 30.
  C1 must hold (GPT's independent control): the zero ray of the j = 3 exceptional seed (gap 00101, P, r = 0) closes at
     W = 29 in phase 0 and W = 27 in phase 1, as E3 and F1 found.
  C2 must hold (GPT's index counter): 10110001 and 101100001 at r = 0, p = 0, T = 1 give five-tick depth-1 traces that
     agree for four ticks and differ at the fifth.
  C3 must hold (the zero-ray guard): the path 10111 followed by zeros is explored, not pruned; its closing window is
     reported.
  Q1 blind (0.7, GPT's): the tree does not close: a live prefix at k = 40 or a period-cap hit. Counterfactual: every
     branch closes at some W* <= 37, which then goes to GPT for the carrying read before anything is claimed.
  Q2 blind (0.65, mine): not closed, with live prefixes at the cap (not only period-cap UNKNOWNs).

OUTCOME (2026-10-13 18:35 BST, M5, 101 s; machine output quoted): C0 HELD, C1 HELD, C2 HELD, C3 reported, Q1 HELD,
  Q2 HELD: the tree does NOT close within the caps.
  C0: the vectorized evaluator agrees with verdict_fast on 2,000 rows per phase. C1: the j = 3 exceptional seed
     101101101's zero ray closes at {0: 29, 1: 27}. C2: traces ['01111', '01110'], GPT's exact numbers. C3: 10111's zero
     ray closes at {0: 4, 1: 5}.
  The search stopped at the node cap (300,000 nodes, all within header 1011; header 1100 was not reached), with the
     largest closing window 37. Live nodes per prefix length: 1 at each k = 4 .. 11, then 2, 1, 2, 4, 8, 15, 15, 22, 35,
     57, 113, 183, 338, 520, 792, 1300, 1927, 2914, 4317, 7327, 8835, 14627, 19562 at k = 12 .. 34 (about 1.5 per bit),
     then 14331 .. 9272 at k = 35 .. 40 as period-cap UNKNOWNs (63,760, from W = 32) cut branches. Live at k = 40:
     9,272.
  Diagnostic after the run (GC1191's decoder on the first six live prefixes at the cap): one is a zero ray that the
     grammar rejects (terminal 00, a relaxation artefact); the other five are accepted primitive words, Q and P at
     deficits 18 and 19, each with one time residue alive in one or both phases at W = 37. Their own cores make windows
     of at least d + L - 1 >= 82 available, so these are not counterexamples, only branches the capped relaxation
     cannot close.
"""
import os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from rule30_birth_deficit_census import make_index, verdict_fast, seed_bits      # Local's own (L672 .. L676)

HORIZON = 1 << 16


class AhoCorasick:
    def __init__(self, words):
        goto, out, fail = [[-1, -1]], [False], [0]
        for w in words:
            s = 0
            for ch in w:
                c = int(ch)
                if goto[s][c] == -1:
                    goto[s][c] = len(goto)
                    goto.append([-1, -1]); out.append(False); fail.append(0)
                s = goto[s][c]
            out[s] = True
        queue = []
        for c in (0, 1):
            if goto[0][c] == -1:
                goto[0][c] = 0
            else:
                fail[goto[0][c]] = 0
                queue.append(goto[0][c])
        while queue:
            s = queue.pop(0)
            out[s] = out[s] or out[fail[s]]
            for c in (0, 1):
                u = goto[s][c]
                if u == -1:
                    goto[s][c] = goto[fail[s]][c]
                else:
                    fail[u] = goto[fail[s]][c]
                    queue.append(u)
        self.goto = np.array(goto, dtype=np.int32)
        self.out = np.array(out, dtype=bool)


def child_alive(R, p, ac):
    """R: n x W child rows (depths 1 .. W). True where the child passes the clock and the cuts over ticks 0 .. W - 1."""
    n, W = R.shape
    rows = np.zeros((n, W + 2), dtype=np.uint8)
    rows[:, 1:W + 1] = R
    alive = np.ones(n, dtype=bool)
    state = np.zeros(n, dtype=np.int32)
    for t in range(W):
        d1 = rows[:, 1]
        if (t + p) % 2 == 1:
            alive &= d1 == 1
        else:
            v = (1 - d1).astype(np.int32)
            state = ac.goto[state, v]
            alive &= ~ac.out[state]
        if t < W - 1:
            rows[:, 0] = (t + p) % 2
            new = rows.copy()
            new[:, 1:W + 1] = rows[:, 2:W + 2] ^ (rows[:, 1:W + 1] | rows[:, 0:W])
            rows = new
    return alive


def extend(cols, b):
    c = cols[-1] | (cols[-2] if len(cols) >= 2 else np.zeros_like(cols[-1]))
    cum = np.bitwise_xor.accumulate(c)
    v = np.empty_like(c)
    v[0] = b
    v[1:] = b ^ cum[:-1]
    return v


def path_cols(bits):
    cols = [np.ones(HORIZON + 1, dtype=np.uint8)]
    for b in bits[1:]:
        cols.append(extend(cols, b))
    return cols


def period(cols, base):
    t = base
    while t <= HORIZON:
        if all(col[t] == col[0] for col in cols[1:]):
            return t
        t += base
    return None


def node_eval(cols, r, alive, mod, acs):
    """New alive residue arrays per phase at window W = k - 3, and the period; None if the period is beyond the horizon."""
    k = len(cols)
    W = k - 3
    Pt = period(cols, mod)
    if Pt is None:
        return None, None, W
    assert Pt % 2 == 0
    new = {}
    for p in (0, 1):
        cand = np.arange((r - p - 1) % 2, Pt, 2)
        if alive[p] is not None:
            cand = cand[np.isin(cand % mod, alive[p])]
        if W < 1 or len(cand) == 0:
            new[p] = cand
            continue
        R = np.stack([cols[i + 2 - p][cand] for i in range(1, W + 1)], axis=1)
        new[p] = cand[child_alive(R, p, acs[p])]
    return new, Pt, W


def ray_close(bits, r, acs, kmax=44):
    """Follow bits then zeros; the window at which each phase's alive set empties."""
    cols = path_cols(bits[:4])
    alive, mod, done = {0: None, 1: None}, 1, {}
    seq = list(bits) + [0] * kmax
    for k in range(4, kmax + 1):
        if k > 4:
            cols = cols + [extend(cols, seq[k - 1])]
        new, Pt, W = node_eval(cols, r, alive, mod, acs)
        if new is None:
            return done, 'UNKNOWN at W=%d' % W
        for p in (0, 1):
            if p not in done and len(new[p]) == 0 and W >= 1:
                done[p] = W
        alive, mod = new, Pt
        if 0 in done and 1 in done:
            return done, 'closed'
    return done, 'open at the cap'


def controls(acs, index):
    rng = random.Random(1192)
    ok0 = True
    for p in (0, 1):
        for _ in range(2000):
            W = rng.randrange(3, 31)
            row = [rng.randrange(2) for _ in range(W)]
            a = child_alive(np.array([row], dtype=np.uint8), p, acs[p])[0]
            b = verdict_fast(row, p, W, index[p])[0] == 'OPEN'
            ok0 &= bool(a) == b
    print('C0 vectorized evaluator = verdict_fast (2,000 rows per phase):', 'HELD' if ok0 else 'FAILED')
    sb = seed_bits(2, (0, 0, 1, 0, 1), 'P')
    done, st = ray_close(sb, 0, acs)
    print('C1 j=3 exceptional seed', ''.join(map(str, sb)), 'zero ray:', done, st,
          'HELD' if done == {0: 29, 1: 27} else 'FAILED')
    traces = []
    for w in ('10110001', '101100001'):
        cols = path_cols([int(c) for c in w])
        R = np.array([[cols[i + 2][1] for i in range(1, 6)]], dtype=np.uint8)
        rows = np.zeros((1, 7), dtype=np.uint8); rows[:, 1:6] = R
        tr = []
        for t in range(5):
            tr.append(int(rows[0, 1]))
            rows[:, 0] = t % 2
            new = rows.copy(); new[:, 1:6] = rows[:, 2:7] ^ (rows[:, 1:6] | rows[:, 0:5]); rows = new
        traces.append(''.join(map(str, tr)))
    ok2 = traces[0][:4] == traces[1][:4] and traces[0][4] != traces[1][4]
    print('C2 index counter traces', traces, 'HELD' if ok2 else 'FAILED')
    done, st = ray_close([1, 0, 1, 1, 1], 0, acs)
    print('C3 10111 zero ray:', done, st)
    return ok0 and ok2 and done is not None


def search(kcap, nodecap, minutes, acs):
    t0 = time.time()
    stats = {'nodes': 0, 'closed_W': 0, 'live_at_cap': [], 'unknown': [], 'per_k_live': {}}
    stopped = None
    for header in ((1, 0, 1, 1), (1, 1, 0, 0)):
        r = header[1]
        stack = [(list(header), path_cols(list(header)), {0: None, 1: None}, 1)]
        while stack:
            if stats['nodes'] >= nodecap or time.time() - t0 > 60 * minutes:
                stopped = 'node cap' if stats['nodes'] >= nodecap else 'time cap'
                stats['pending'] = stats.get('pending', 0) + len(stack)
                break
            bits, cols, alive, mod = stack.pop()
            stats['nodes'] += 1
            new, Pt, W = node_eval(cols, r, alive, mod, acs)
            k = len(bits)
            if new is None:
                stats['unknown'].append((''.join(map(str, bits)), W))
                continue
            if len(new[0]) == 0 and len(new[1]) == 0 and W >= 1:
                stats['closed_W'] = max(stats['closed_W'], W)
                continue
            stats['per_k_live'][k] = stats['per_k_live'].get(k, 0) + 1
            if k >= kcap:
                stats['live_at_cap'].append((''.join(map(str, bits)), W, len(new[0]), len(new[1]), Pt))
                continue
            for b in (1, 0):
                stack.append((bits + [b], cols + [extend(cols, b)], new, Pt))
    return stats, stopped, time.time() - t0


def main():
    kcap = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    nodecap = int(sys.argv[2]) if len(sys.argv) > 2 else 300000
    minutes = float(sys.argv[3]) if len(sys.argv) > 3 else 45
    import rule30_relaxed_records_k as rlk
    lists = {0: rlk.load_forbidden('44all') + rlk.load_cuts(0, 40),
             1: rlk.load_forbidden('44allp1') + rlk.load_cuts(1, 40)}
    acs = {p: AhoCorasick(lists[p]) for p in (0, 1)}
    index = {p: make_index(lists[p]) for p in (0, 1)}
    controls(acs, index)
    stats, stopped, secs = search(kcap, nodecap, minutes, acs)
    closed = not stats['live_at_cap'] and not stats['unknown'] and stopped is None
    print('prefix tree: %s; %d nodes in %.0f s; largest closing window %d; stopped by %s'
          % ('ALL BRANCHES CLOSED' if closed else 'NOT CLOSED', stats['nodes'], secs, stats['closed_W'], stopped))
    print('live nodes per prefix length:', sorted(stats['per_k_live'].items()))
    print('live at the k cap: %d; first %s' % (len(stats['live_at_cap']), stats['live_at_cap'][:6]))
    print('period-cap UNKNOWN: %d; first %s' % (len(stats['unknown']), stats['unknown'][:6]))


if __name__ == '__main__':
    main()
