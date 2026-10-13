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

Record searched (record_find, 2026-10-13 15:56 BST): 'extremal' -> 68 hits in 18 files (the prize records' extremal
cases, not this corner); 'P corner' -> 2 hits (GC1176 and its probe); 'oldest age' -> 0 hits; 'six.diagonal|moving
front' -> 9 hits in 6 files (GC840's moving-front digit recursion, another object; GC1176); 'defect front' -> 1 hit
(GC602, a portfolio note). GC1170, GC1172, GC1174 and its L667 response, and GC1176 itself read.

PREDICTIONS (written 2026-10-13 15:57 BST, before any run; committed 15:58).
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

OUTCOME (2026-10-13 15:59 BST, M5, one minute; machine output quoted): R1 HELD, R2 HELD, U1 HELD, U2 HELD.
  R1: alignment HELD on 640 cases (r = 1 .. 5, both p, 64 roots): C_1(0^r w) is the checkerboard to depth 2r + 1 and
     advancing it a ticks gives C_p(w) on every shared determined depth.
  R2: HELD for r = 1 .. 256: 40 tails each give one depth-1 column; the synthetic part and the shield hold; the arrival
     defects are GC1176's table row r mod 16; the open residues are exactly [9, 13].
  U1: HELD: with the core exactly six, depth 1 at old tick 2r + 6 is 1 at residues 1 and 5 (it passes), so the seventh
     cell carries those exclusions.
  U2: HELD at C = 10: periods 16, 16, 32, 32 at C = 7 .. 10; surviving classes in each phase 2, 1, 1, 0.
     Diagnostic added after the run (detail(), the same verdict code, direct simulation for r <= 512 with random
     tails, no recurrence): only the clock and no11 are used. Residue 9 (r = 9, 25 mod 32) gives the child word 1011
     at C = 8; r = 29 mod 32 fails the black test at old tick 2r + 8 at C = 9; r = 13 mod 32 gives 10011 at C = 10.
     Every surviving r has r >= 9 and so a core >= 35, more than the 10 used. With GC1176: in the extremal corner a P
     birth with a core of at least 7 is impossible for every r, so the corner is empty for r >= 2 and, at r = 1, for
     L >= 3 + 2p (GC1175's d = 3 example, L = 3 with a core of 5, sits below this).

ADDENDUM PREDICTIONS (2026-10-13 16:05 BST, before the run): GPT's GC1177 (75c296db), its three carrying steps, with
  a full-line Rule 30 written here (not GPT's rule30_corner_two_cell.py). Record searched: as above, plus GC1177's own
  terms 'right.edge|two.cell' and G249 read.
  G1 must hold (crop identity, cone length): for r = 1 .. 64, p in {0, 1}, cores K = 7 .. 14 and 4 random tails, the
     child row (corner_row advanced a ticks under the black-start wall) equals x_T(2r - 2 - j) of the seed-11 orbit at
     T = 2r - p for every depth j <= K + p - 1, and is white at depths d .. K + p - 1.
  G2 blind (0.7): the cone length is sharp: at depth K + p the child depends on the tail for some r, p, K.
  G3 must hold (the unexpected check, a third route to GC1176's table): the seed-11 right diagonals V_j(t) = x_t(t - j)
     at t = 2r give GC1176's arrival defects as D_k = V_(k+3)(2r) XOR ((k + 1) mod 2) for k = 0 .. 5 and r <= 256; and
     V_3 .. V_11 at t = 2r have period 32 in r, U2's period for C = 10.
ADDENDUM OUTCOME (2026-10-13 16:06 BST, M5, seconds): G1 HELD, G2 HELD, G3 HELD. The crop identity and the white band
  hold through depth K + p - 1 for r <= 64, both phases, K = 7 .. 14 (4 tails each); depth K + p depends on the tail;
  the seed-11 right diagonals at t = 2r reproduce GC1176's table for r <= 256 and have period 32 in r (V_3 .. V_11).

ADDENDUM PREDICTIONS (2026-10-13 16:13 BST, before the run): the white-wall oldest-age corner, d + p = 3 mod 4 (8.97).
  There d = 4q - 1 - p, the oldest age is a = 2q - p, the birth parent is C_0(0^q w) (checkerboard through 2q, white at
  2q), and only P is possible, with a core of at least L + 4q - 2p - 2 black cells from 2q + 1: the same row as
  GC1176's corner, under a white-start wall. The child's samples are at ticks 2q, 2q + 2, ... and its black tests at
  2q + 1, 2q + 3, ... in both phases. Hand argument: the wall at tick 0 is masked by depth 1's black, the one-step image
  is GC1176's seed, and the front reaches depth 1 at tick 2q + 1, which is now a black tick, so depth 1 is white there.
  W1 must hold (alignment): for q = 1 .. 5, p in {0, 1} and all 64 roots of length 6, C_0(0^q w) is the checkerboard at
     depths 1 .. 2q and advancing it a = 2q - p ticks gives C_p(w) on every shared determined depth.
  W2 blind (0.8): for q = 1 .. 256 and a core of two cells (any tail), depth 1 is black at ticks 0 .. 2q and white at
     tick 2q + 1: every core of at least two fails the child's first black test. Then the corner is empty except at
     q = 1, p = 1, L = 1 (d = 2, core 1). REFUTED-BY: one q where depth 1 is black at 2q + 1 or depends on the tail.
  W3 must hold (the control: the test can pass): with a core of exactly one cell (white at 2q + 2) the row is the
     checkerboard through 2q + 2, and depth 1 is black at tick 2q + 1.
ADDENDUM OUTCOME (2026-10-13 16:13 BST, seconds): W1 HELD, W2 HELD, W3 HELD. With 8.97's other three classes, no band
  at depth d >= 6 reaches the oldest birth age, in either phase; the exceptions are at d <= 5 (listed in 8.97).
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


def detail(cmax=10, rmax=512):
    """Added after the run (a diagnostic): which test excludes each class, by direct simulation, no11 and clock only."""
    rng = random.Random(5)
    for C in range(8, cmax + 1):
        seen = {}
        for r in [r for r in range(1, rmax + 1) if r % 16 in (9, 13)]:
            cols = {tuple(depth1_column(corner_row(r, C, [rng.randrange(2) for _ in range(12)]), 1, 2 * r + C - 1))
                    for _ in range(3)}
            assert len(cols) == 1
            v, w = child_verdict(list(cols.pop()), r, C, ['11'])
            seen.setdefault((r % 32, v.split(' at ')[0], w), []).append(r)
        for k in sorted(seen):
            print('detail C=%d  r mod 32 = %2d: %-14s child word %-6s (r = %s ...)' % (C, k[0], k[1], k[2], seen[k][:3]))


def seed11(T):
    """Full-line Rule 30 from black cells at -1 and 0; returns rows as dicts site -> bit, t = 0 .. T."""
    rows = [{-1: 1, 0: 1}]
    for t in range(T):
        x = rows[-1]
        rows.append({i: x.get(i - 1, 0) ^ (x.get(i, 0) | x.get(i + 1, 0)) for i in range(-t - 3, t + 3)})
    return rows


def gc1177():
    rng = random.Random(1177)
    g1, g2_dep = True, False
    rows = seed11(2 * 64 + 2)
    for r in range(1, 65):
        for p in (0, 1):
            a, T, X, d = 2 * r + 1 - p, 2 * r - p, 2 * r - 2, 4 * r - p
            for K in range(7, 15):
                kids = []
                for _ in range(4):
                    row = corner_row(r, K, [rng.randrange(2) for _ in range(10)])
                    for t in range(a):
                        row = step(row, (t + 1) % 2)
                    kids.append(row)
                J = K + p - 1
                for kid in kids:
                    g1 &= all(kid[j] == rows[T].get(X - j, 0) for j in range(1, J + 1))
                    g1 &= all(kid[j] == 0 for j in range(d, J + 1))
                if len({kid[J + 1] for kid in kids}) > 1:
                    g2_dep = True
    print('G1 crop identity and white band through K+p-1 (r <= 64, both p, K = 7..14):', 'HELD' if g1 else 'FAILED')
    print('G2 depth K+p depends on the tail somewhere:', 'HELD' if g2_dep else 'REFUTED')
    rows = seed11(2 * 256 + 2)
    V = lambda j, t: rows[t].get(t - j, 0)
    g3 = all(''.join(str(V(k + 3, 2 * r) ^ ((k + 1) % 2)) for k in range(6)) == GC1176_TABLE[r % 16]
             for r in range(1, 257))
    seq = [tuple(V(j, 2 * r) for j in range(3, 12)) for r in range(256)]
    per = next(q for q in range(1, 129) if all(seq[i] == seq[i + q] for i in range(256 - q)))
    print('G3 seed-11 right diagonals give GC1176 table:', 'HELD' if g3 else 'FAILED', '| period of V_3..V_11 at t = 2r:', per)


def white_corner():
    ok1 = True
    for q in range(1, 6):
        for p in (0, 1):
            a = 2 * q - p
            for m in range(64):
                w = [(m >> i) & 1 for i in range(6)]
                X = forced_row([0] * q + w, 0)
                ok1 &= X[1:2 * q + 1] == [j % 2 for j in range(1, 2 * q + 1)]
                Y = X
                for t in range(a):
                    Y = step(Y, t % 2)
                Z = forced_row(w, p)
                n = min(len(Y), len(Z))
                ok1 &= n > 4 and Y[1:n] == Z[1:n]
    print('W1 white-wall alignment (C_0(0^q w) advanced 2q-p ticks = C_p(w); checkerboard to 2q):',
          'HELD' if ok1 else 'FAILED')
    rng = random.Random(3)
    ok2, ok3 = True, True
    for q in range(1, 257):
        cols = {tuple(depth1_column(corner_row(q, 2, [rng.randrange(2) for _ in range(6)]), 0, 2 * q + 1))
                for _ in range(6)}
        x = cols.pop()
        ok2 &= not cols and all(x[t] == 1 for t in range(2 * q + 1)) and x[2 * q + 1] == 0
        x1 = depth1_column(corner_row(q, 1, [0] + [rng.randrange(2) for _ in range(6)]), 0, 2 * q + 1)
        ok3 &= x1[2 * q + 1] == 1
    print('W2 core of two fails the black test at tick 2q+1 (q <= 256):', 'HELD' if ok2 else 'REFUTED')
    print('W3 core of exactly one passes it:', 'HELD' if ok3 else 'FAILED')


if __name__ == '__main__':
    r1()
    r2_u1()
    u2()
    detail()
    gc1177()
    white_corner()
