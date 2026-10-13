#!/usr/bin/env python3
"""rule30_extremal_p_corner_read.py: Local's second read of GPT's GC1176 (the extremal P corner), by direct simulation
with code written apart from GPT's probe (its own rule, inverse and evolution; GPT's helpers are not imported).

The corner (GC1176): a child of wall phase p with a white band at depth d = 4r - p, traced through GC1174's canonical
ancestry to the oldest birth age a = 2r + 1 - p. Its birth parent is A_a = C_1(0^r w) (phase 1, r synthetic zeros
before the child's root w), whose depths 1 .. 2r+1 are the checkerboard (black at odd depths). Q is impossible there,
and a P birth needs a black core from N = 2r + 1 of length at least L + 2a - 2 = L + 4r - 2p. GC1176 asks Local for
three carrying steps: the child's phase alignment, the six-front closure through the arrival boundary, and the
transfer of a seven-cell core to the child's tests.

Conventions here (old ticks): A_a is the row at old tick 0, the wall black there (wall(t) = (t + 1) mod 2). The child
is A_a advanced a ticks; its visible samples are column +1 at old ticks 2r + 1, 2r + 3, ..., read as 1 XOR depth 1
(the clock), and its black tests are depth 1 = 1 at old ticks 2r + 2, 2r + 4, .... GC1176's tick t is old tick t + 1.

RUN-ON:     cpu, standard library plus the certified cut lists in the RLK scratch (for U2 only); seconds.
COMMAND:    python3 tests/probes/lexicon/rule30_extremal_p_corner_read.py

Record searched (record_find, 2026-10-13 16:02 BST): 'extremal' -> 68 hits in 18 files (the prize records' extremal
cases, not this corner); 'P corner' -> 2 hits (GC1176 and its probe); 'oldest age' -> 0 hits; 'six.diagonal|moving
front' -> 9 hits in 6 files (GC840's moving-front digit recursion, another object; GC1176); 'defect front' -> 1 hit
(GC602, a portfolio note). GC1170, GC1172, GC1174 and its L667 response, and GC1176 itself read.

PREDICTIONS (written 2026-10-13 16:05 BST, before any run).
  R1 must hold (alignment): for r = 1 .. 5, p in {0, 1} and all 64 roots w of length 6, the inverse row C_1(0^r w)
     is the checkerboard at depths 1 .. 2r + 1, and advancing it a = 2r + 1 - p ticks under its wall gives C_p(w) on
     every depth where both are determined.
  R2 must hold (locality, closure and the verdict, without GPT's recurrence): for r = 1 .. 256, the row checkerboard
     to depth 2r, black on 2r + 1 .. 2r + 7, then every one of the 32 five-cell tails and 8 random 60-cell tails:
     depth 1 is 1 at old ticks 0 .. 2r (the synthetic part and the arrival shield), depth 1 through old tick 2r + 6
     does not depend on the tail, the arrival defects (depths 1 .. 6 at old tick 2r + 1, XOR the checkerboard) are
     GC1176's table row r mod 16, and with the black tests at old ticks 2r + 2, 2r + 4, 2r + 6 and no 11 between any
     two consecutive child samples, the open r are exactly r = 9, 13 mod 16.
  U1 blind (0.5), the unexpected check: with a core of exactly six (white at N + 6), residues 1 and 5 pass the black
     test at old tick 2r + 6, so the seventh core cell carries those two exclusions.
  U2 blind (0.35), the extension: a surviving r (9 or 13 mod 16, so r >= 9) needs a core of at least
     L + 4r - 2p >= 35 cells, so any core length C <= 35 may be assumed there. With C up to 20, the black tests and
     the child phase's certified cut list (mfw44all and cuts40 for p = 0; mfw44allp1 and cuts40 for p = 1) applied to
     the determined child prefix exclude every residue class of 9 and 13 (classes taken modulo the exact period of
     the closed (C - 1)-coordinate front orbit, GC1176's recurrence, itself checked against R2's direct simulation).
     REFUTED-BY: a class surviving at C = 20; then its determined prefix is reported and the extension stops.

OUTCOME: (filled in after the run, below this line)
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

GC1176_TABLE = ("101010 110010 100011 111010 101001 110001 100001 111001 "
                "101011 110011 100010 111011 101000 110000 100000 111000").split()


def r30(l, c, r):
    return l ^ (c | r)


def step(row, wall):
    """One Rule 30 update of the left half; row[0] is the wall cell, row[j] depth j. The last cell is dropped."""
    x = [wall] + row[1:]
    return [None] + [r30(x[j + 1], x[j], x[j - 1]) for j in range(1, len(x) - 1)]


def depth1_column(row, phase, ticks):
    """Depth-1 values at ticks 0 .. ticks; the wall is (t + phase) mod 2."""
    out = []
    for t in range(ticks + 1):
        out.append(row[1])
        if t < ticks:
            row = step(row, (t + phase) % 2)
    return out


def forced_row(samples, phase):
    """Inverse: the forced initial left row for wall phase `phase` and visible samples at its white ticks.
    Returns depths 1 .. M as a list with a None at index 0 (only the determined depths)."""
    T = 2 * len(samples) + phase                      # ticks 0 .. T-1 have known wall and visible values
    wall = [(t + phase) % 2 for t in range(T + 1)]
    vis = [0] * (T + 1)
    for i, s in enumerate(samples):
        vis[2 * i + phase] = s
    cols = [wall]
    # depth 1: wall(t+1) = d1(t) XOR (wall(t) OR vis(t))
    d = [wall[t + 1] ^ (wall[t] | vis[t]) for t in range(T)]
    cols.append(d)
    while len(cols[-1]) > 1:
        cur, prev = cols[-1], cols[-2]
        cols.append([cur[t + 1] ^ (cur[t] | prev[t]) for t in range(len(cur) - 1)])
    return [None] + [c[0] for c in cols[1:]]


def child_verdict(x, r, C, forb):
    """x: depth-1 column at old ticks. Returns (verdict, child word) using old ticks up to 2r + C - 1."""
    last = 2 * r + C - 1
    word = ''
    for t in range(2 * r + 1, last + 1):
        if (t - 2 * r) % 2 == 1:                       # white tick of the child: a sample
            word += str(1 ^ x[t])
        elif x[t] != 1:
            return 'black failure at old tick %d' % t, word
        bad = [f for f in forb if word.endswith(f)]
        if bad:
            return 'cut %s' % bad[0], word
    return 'OPEN', word


def corner_row(r, C, tail):
    N = 2 * r + 1
    return [None] + [j % 2 for j in range(1, N)] + [1] * C + list(tail)


def r1():
    ok = True
    for r in range(1, 6):
        for p in (0, 1):
            a = 2 * r + 1 - p
            for m in range(64):
                w = [(m >> i) & 1 for i in range(6)]
                X = forced_row([0] * r + w, 1)
                ok &= X[1:2 * r + 2] == [j % 2 for j in range(1, 2 * r + 2)]
                Y = X
                for t in range(a):
                    Y = step(Y, (t + 1) % 2)
                Z = forced_row(w, p)
                n = min(len(Y), len(Z))
                ok &= n > 4 and Y[1:n] == Z[1:n]
    print('R1 alignment (C_1(0^r w) advanced a ticks = C_p(w); checkerboard prefix):', 'HELD' if ok else 'FAILED')
    return ok


def r2_u1():
    rng = random.Random(1176)
    ok, opens, u1 = True, [], {}
    for r in range(1, 257):
        C = 7
        tails = [[(m >> i) & 1 for i in range(5)] + [0] * 3 for m in range(32)]
        tails += [[rng.randrange(2) for _ in range(60)] for _ in range(8)]
        cols = []
        for tail in tails:
            row = corner_row(r, C, tail)
            cols.append(depth1_column(row, 1, 2 * r + C - 1))
        x = cols[0]
        ok &= all(c == x for c in cols)                                   # tail independence through 2r + 6
        ok &= all(x[t] == 1 for t in range(0, 2 * r + 1))                 # synthetic part and the shield
        row = corner_row(r, C, tails[0])
        for t in range(2 * r + 1):
            row = step(row, (t + 1) % 2)
        arrival = ''.join(str(row[j] ^ (j % 2)) for j in range(1, 7))
        ok &= arrival == GC1176_TABLE[r % 16]
        v, w = child_verdict(x, r, C, ['11'])
        if v == 'OPEN':
            opens.append(r)
        if r % 16 in (1, 5):                                              # U1: core of exactly six
            x6 = depth1_column(corner_row(r, 6, [0] + tails[0]), 1, 2 * r + 6)
            u1.setdefault(r % 16, set()).add(x6[2 * r + 6])
    ok &= sorted({r % 16 for r in opens}) == [9, 13]
    print('R2 direct simulation r = 1..256 (tails, shield, table, verdict):', 'HELD' if ok else 'FAILED',
          '| open residues', sorted({r % 16 for r in opens}))
    held = all(s == {1} for s in u1.values())
    print('U1 core of exactly six, depth 1 at old tick 2r+6 for residues 1, 5:', {k: sorted(v) for k, v in u1.items()},
          'HELD' if held else 'REFUTED')
    return ok


def front(state, t):
    out = []
    for k in range(len(state)):
        b = state[k - 1] if k >= 1 else 0
        c = state[k - 2] if k >= 2 else 0
        out.append(state[k] ^ ((b & (1 - c)) if (k - t) % 2 else (c & (1 - b))))
    return out


def u2(cmax=20):
    import rule30_relaxed_records_k as rlk
    lists = {0: rlk.load_forbidden('44all') + rlk.load_cuts(0, 40),
             1: rlk.load_forbidden('44allp1') + rlk.load_cuts(1, 40)}
    print('U2 cut lists: phase 0 %d words, phase 1 %d words' % (len(lists[0]), len(lists[1])))
    rng = random.Random(9)
    for C in range(7, cmax + 1):
        K = C - 1
        init = [1 - (k % 2) for k in range(K)]                            # 1010... (D_k = 1 at even k)
        orbit, s = [], list(init)
        while True:
            orbit.append(s)
            s = front(front(s, 0), 1)
            if s == init:
                break
            if len(orbit) > 1 << 20:
                print('U2 C=%d: orbit longer than 2^20, stop' % C); return
        P = len(orbit)
        # the recurrence against direct simulation, for r <= 256 in the open residues
        for r in [r for r in range(1, 257) if r % 16 in (9, 13)][:12]:
            row = corner_row(r, C, [rng.randrange(2) for _ in range(8)])
            for t in range(2 * r + 1):
                row = step(row, (t + 1) % 2)
            assert [row[j] ^ (j % 2) for j in range(1, K + 1)] == orbit[r % P], ('recurrence', C, r)
        surv = {0: [], 1: []}
        for r0 in range(P):
            if r0 % 16 not in (9, 13):
                continue
            D = orbit[r0]
            row = [None] + [(j % 2) ^ D[j - 1] for j in range(1, K + 1)] + [0]
            x = depth1_column(row, 0, K - 1)                              # relative ticks 0 .. C-2 = old 2r+1 ..
            xo = [1] * (2 * r0 + 1) + x                                   # place at old ticks (r0 as a stand-in)
            for p in (0, 1):
                v, w = child_verdict(xo, r0, C, lists[p])
                if v == 'OPEN':
                    surv[p].append((r0, w))
        print('U2 C=%d: period %d; surviving classes of 9, 13 mod 16: phase 0 %d, phase 1 %d%s'
              % (C, P, len(surv[0]), len(surv[1]),
                 '' if surv[0] else '  -> every class excluded'), flush=True)
        if not surv[0] and not surv[1]:
            return C
    for p in (0, 1):
        print('U2 survivors at C=%d, phase %d (class, determined child word):' % (cmax, p), surv[p][:8])
    return None


if __name__ == '__main__':
    r1()
    r2_u1()
    u2()
