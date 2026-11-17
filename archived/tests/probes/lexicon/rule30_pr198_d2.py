#!/usr/bin/env python3
"""rule30_pr198_d2.py: PR198-D2, one successor decision at each rooted exit target, of RULE30-GPT.md (GPT's
preregistration at 0a3b33f; claimed by Local in CLOUD-LOCAL.md at 9a3b36c before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_pr198_d2.py
COST:       seconds expected; caps 60 s wall and 256 MiB peak RSS (GPT's); a breach stops without raising them.

The rooted word w = 1000101001100001 (q = 16, m = 26,403, h = 8; PR196-D1). D1's exits are at phases 0 and 4 (mirrors
8 and 12): from the paired windows (X, Y) at phases t and t + 8, the exit appends both flipped bits, giving the exit
target (X', Y'). Its second-step tails are T_X = tail(X'), T_Y = tail(Y'); with K = 1 + V(T_X 0) + V(T_Y 0) the only
candidate second appends are (0, K) and (1, K + 1), legal when F_m = 1 on both new windows (their V values are then
opposite). F_m = U_(2m-1) and V_m = U_(2m-2) at position 0 of an m-bit window (one padding bit appended).

PREDICTION (GPT's, published before this run): at least one of the two exit targets has out-degree 0 in H_m. If both
have a successor, that is retained as a refutation; a survivor is a two-edge prefix only.
EVALUATORS: (1) packed finite-window recurrence on integers, storing two profiles; (2) independent scalar periodic
baseline (the original word at the window's phase, computed cyclically) plus a scalar boundary strip of the final
three valid positions at each level, advanced by the scalar recurrence. Both, with both padding bits, must agree.
CONTROLS: exhaustive m = 1 to 6 (every m-bit word as its own cyclic baseline, every change of the final up to two
positions, both paddings) against full scalar arrays; D1's F/V conditions and four ordered exits; V(T1) = 1 + V(T0)
at every second-step tail; the candidates' opposite target labels; the t + 8 mirror.

OUTCOME, 2026-10-07 (M5, one process, one run of the diagnostic; wall 4.75 s, CPU 4.76 s, peak RSS 28.0 MiB). Before the
run the two evaluators were tested on the small controls and on a synthetic, non-witness 16-periodic input at
m = 26,403 with its last two bits changed (they agreed); the first draft's strip had an off-by-one for windows shorter
than the strip, fixed before the run. Controls all PASS: the exhaustive m = 1 to 6 set (1,000 inputs) agrees across
packed, strip and full scalar evaluators and is padding-free; D1's original F/V conditions and its four ordered exits
are reproduced by both evaluators; at every second-step tail V(T1) = 1 + V(T0); every candidate has opposite target
labels; both evaluators and both paddings agree on every window. At all four exit targets K = 0, and both candidates
fail F on at least one window: phase 0, F = (0, 0) and (0, 1); phase 4, (0, 1) and (0, 1); phase 8, (0, 0) and
(1, 0); phase 12, (1, 0) and (1, 0), the mirrors of 0 and 4. Out-degrees are 0 at both unordered exit targets.
PR198-D2's prediction (at least one dead end) HELD, and more: both are dead ends. With D1's complete first-edge census,
the rooted q = 16 component is exactly its directed sixteen-cycle (swap displacement 8; q = 16 only), as preregistered
for this outcome. Other components at r = 52,808 remain unclassified.
"""
import resource
import sys
import time
from itertools import product

T_START = time.time()
W = '1000101001100001'
Q, H, M = 16, 8, 26403


def check_caps():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576
    if time.time() - T_START > 60 or rss > 256:
        print('CAP REACHED (wall %.1f s, peak RSS %.1f MiB): stopped, not a result' % (time.time() - T_START, rss))
        sys.exit(2)


def eval_packed(bits, n_list):
    """U_n(0) for n in n_list on a finite word (list of bits), packed recurrence keeping two profiles."""
    v = sum(b << t for t, b in enumerate(bits))
    a, la, b, lb = v, len(bits), v, len(bits)
    out = {}
    if 0 in n_list:
        out[0] = v & 1
    if 1 in n_list:
        out[1] = v & 1
    top = max(n_list)
    for k in range(2, top + 1):
        ln = min(la - 1, lb)
        c = ((a >> 1) ^ (b | a)) & ((1 << ln) - 1)
        a, la, b, lb = b, lb, c, ln
        if k in n_list:
            out[k] = c & 1
    return out


def eval_full_scalar(bits, n_list):
    """Direct scalar finite arrays (for the small exhaustive controls)."""
    L = [list(bits), list(bits)]
    for k in range(2, max(n_list) + 1):
        a, b = L[k - 2], L[k - 1]
        L.append([a[t + 1] ^ (b[t] | a[t]) for t in range(min(len(a) - 1, len(b)))])
    return {n: L[n][0] for n in n_list}


def base_table(base_word, n_top):
    """Cyclic baseline profiles U_0 .. U_n_top of the periodic word, as lists indexed from its phase 0."""
    q = len(base_word)
    tab = [list(base_word), list(base_word)]
    for k in range(2, n_top + 1):
        a, b = tab[k - 2], tab[k - 1]
        tab.append([a[(t + 1) % q] ^ (b[t] | a[t]) for t in range(q)])
    return tab


def eval_strip(tab, phase, bits, n_list, S=3):
    """Independent evaluator: the scalar periodic baseline tab (read from phase) plus a scalar strip of the final S valid
    positions at each level. bits, the actual finite input, must agree with the baseline before its final S positions;
    at every level the position just below the strip is recomputed and must equal the baseline (the support claim)."""
    q = len(tab[0])
    Lin = len(bits)
    for i in range(max(0, Lin - S)):
        assert bits[i] == tab[0][(phase + i) % q], 'input differs from the baseline before the strip'
    la = lb = Lin
    sa = {i: bits[i] for i in range(max(0, Lin - S), Lin)}
    sb = dict(sa)
    out = {}
    for n in (0, 1):
        if n in n_list:
            out[n] = bits[0]
    for k in range(2, max(n_list) + 1):
        A, B = tab[k - 2], tab[k - 1]
        ln = min(la - 1, lb)
        a_lo, b_lo = la - S, lb - S
        sc = {}
        for t in range(max(0, ln - S - 1), ln):
            a1 = sa[t + 1] if t + 1 >= a_lo else A[(phase + t + 1) % q]
            a0 = sa[t] if t >= a_lo else A[(phase + t) % q]
            b0 = sb[t] if t >= b_lo else B[(phase + t) % q]
            v = a1 ^ (b0 | a0)
            if t >= ln - S:
                sc[t] = v
            else:
                assert v == tab[k][(phase + t) % q], 'boundary strip too narrow at level %d' % k
        la, lb, sa, sb = lb, ln, sb, sc
        if k in n_list:
            out[k] = sb[0] if 0 >= lb - S else tab[k][phase % q]
    return out


_MEMO = {}


def FV(bits, m, tab=None, phase=None):
    """F_m and V_m at position 0 of an m-bit window, by the packed evaluator (both paddings) and, given a baseline, the
    strip evaluator (both paddings); returns (F, V, all agree). Results are memoized per (window, phase)."""
    key = (tuple(bits), phase)
    if key in _MEMO:
        return _MEMO[key]
    n_list = [2 * m - 2, 2 * m - 1]
    res = []
    for pad in (0, 1):
        x = list(bits) + [pad]
        p = eval_packed(x, n_list)
        res.append((p[2 * m - 1], p[2 * m - 2]))
        if tab is not None:
            st = eval_strip(tab, phase, x, n_list)
            res.append((st[2 * m - 1], st[2 * m - 2]))
    _MEMO[key] = (res[0][0], res[0][1], len(set(res)) == 1)
    return _MEMO[key]


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (65, 65))
    ok = True
    # control 1: exhaustive m = 1 to 6 against full scalar arrays, every word, changes in the final two positions
    c1, n1 = True, 0
    for m in range(1, 7):
        for Z in product((0, 1), repeat=m):
            for flips in product((0, 1), repeat=min(2, m)):
                for pad in (0, 1):
                    x = list(Z) + [pad]
                    base = list(Z)                           # the word's own cyclic repetition
                    y = x[:]
                    for j, f in enumerate(flips):
                        y[m - 1 - j] ^= f
                    y[m] = pad
                    n_list = [2 * m - 2, 2 * m - 1] if m >= 1 else [0]
                    full = eval_full_scalar(y, n_list)
                    pk = eval_packed(y, n_list)
                    st = eval_strip(base_table(base, max(n_list)), 0, y, n_list)
                    c1 &= full == pk == st
                    n1 += 1
            # padding never changes position 0
            for flips in product((0, 1), repeat=min(2, m)):
                y = list(Z)
                for j, f in enumerate(flips):
                    y[m - 1 - j] ^= f
                a0 = eval_full_scalar(y + [0], [2 * m - 2, 2 * m - 1])
                a1 = eval_full_scalar(y + [1], [2 * m - 2, 2 * m - 1])
                c1 &= a0 == a1
    print('control: exhaustive m = 1-6 (%d inputs), packed = strip = full scalar, padding-free: %s'
          % (n1, 'PASS' if c1 else 'FAIL'))
    ok &= c1
    check_caps()
    w = [int(b) for b in W]
    win = lambda t, m=M: [w[(t + i) % Q] for i in range(m)]
    TAB = base_table(w, 2 * M - 1)
    check_caps()
    # control 2: D1's original conditions and its four ordered exits (both evaluators)
    c2 = True
    exits = {}
    for t in (0, 4, 8, 12):
        X, Y = win(t), win(t + H)
        fX, vX, aX = FV(X, M, TAB, t)
        fY, vY, aY = FV(Y, M, TAB, t + H)
        c2 &= fX == fY == 1 and vX ^ vY == 1 and aX and aY
        bx, by = w[(t + M) % Q], w[(t + H + M) % Q]
        Xp, Yp = X[1:] + [1 - bx], Y[1:] + [1 - by]
        fXp, vXp, a1 = FV(Xp, M, TAB, t + 1)
        fYp, vYp, a2 = FV(Yp, M, TAB, t + H + 1)
        c2 &= fXp == fYp == 1 and vXp ^ vYp == 1 and a1 and a2   # D1: these four exits are legal edges
        exits[t] = (Xp, Yp)
        check_caps()
    print("control: D1's original F/V conditions and its four ordered exits (phases 0, 4, 8, 12) reproduced by both "
          "evaluators: %s" % ('PASS' if c2 else 'FAIL'))
    ok &= c2
    # the second-step decision at each exit target
    rows = {}
    for t in (0, 4, 8, 12):
        Xp, Yp = exits[t]
        TX, TY = Xp[1:], Yp[1:]
        _, vX0, a1 = FV(TX + [0], M, TAB, t + 2)
        _, vX1, a2 = FV(TX + [1], M, TAB, t + 2)
        _, vY0, a3 = FV(TY + [0], M, TAB, t + H + 2)
        _, vY1, a4 = FV(TY + [1], M, TAB, t + H + 2)
        aff = vX1 == 1 ^ vX0 and vY1 == 1 ^ vY0 and a1 and a2 and a3 and a4
        K = 1 ^ vX0 ^ vY0
        cands = []
        for b in (0, 1):
            b2 = K ^ b
            fx, vx, e1 = FV(TX + [b], M, TAB, t + 2)
            fy, vy, e2 = FV(TY + [b2], M, TAB, t + H + 2)
            cands.append((b, b2, fx, fy, vx, vy, vx ^ vy == 1, fx == 1 and fy == 1 and vx ^ vy == 1, e1 and e2))
        rows[t] = (aff, K, cands)
        ok &= aff and all(c[6] and c[8] for c in cands)
        check_caps()
    for t in (0, 4, 8, 12):
        aff, K, cands = rows[t]
        deg = sum(1 for c in cands if c[7])
        print('exit target at phase %2d: V(T1) = 1 + V(T0) %s; K = %d; out-degree %d' % (t, aff, K, deg))
        for b, b2, fx, fy, vx, vy, opp, legal, agree in cands:
            print('   append (%d, %d): F = %d, %d; V = %d, %d (opposite %s); legal %s; evaluators agree %s'
                  % (b, b2, fx, fy, vx, vy, opp, legal, agree))
    deg = {t: sum(1 for c in rows[t][2] if c[7]) for t in rows}
    mirror = deg[0] == deg[8] and deg[4] == deg[12]
    print('mirror (phase t + 8 has the out-degree of t): %s' % ('PASS' if mirror else 'FAIL'))
    ok &= mirror
    dead = [t for t in (0, 4) if deg[t] == 0]
    print('unordered exit targets (phases 0 and 4): out-degrees %d and %d' % (deg[0], deg[4]))
    print('PR198-D2 prediction (at least one dead end):', 'HELD' if dead else 'REFUTED')
    if len(dead) == 2:
        print('both exits are dead ends: the rooted component is exactly its sixteen-cycle')
    print('all controls %s' % ('PASS' if ok else 'FAIL'))
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: wall %.2f s, CPU %.2f s, peak RSS %.1f MiB' % (time.time() - T_START, time.process_time(),
                                                                     rus.ru_maxrss / 1048576))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
