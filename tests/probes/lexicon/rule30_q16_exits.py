#!/usr/bin/env python3
"""rule30_q16_exits.py: QX, PR196-D1's exit census and PR198-D2's successor test on every rooted q = 16 even return
that RC16 found (rule30_r88_census.py), not only r = 52,808. Q7, drawn by Local (chat L482, L483); predictions pushed
before the run.

RUN-ON:     cpu (Python 3); about a minute
COMMAND:    python3 tests/probes/lexicon/rule30_q16_exits.py

For each return word w (RC16's rotation-class representative, time order) with m = (r - 2)/2 and h = 8:
  1. Check that the paired sixteen-cycle is a cycle of H_m: PR196's control 5 (F_m = 1 at every phase, the XOR
     equation, the target V labels, G193's identity). G196 then applies.
  2. D1: the alternative (both appended bits flipped) at phase t is legal exactly when d(t) = d(t + 8) = 0.
  3. D2: at each exit target, the two candidate second appends (0, K) and (1, K + 1), with K = 1 + V(T_X 0) + V(T_Y 0),
     are legal when F_m = 1 on both new windows. This uses PR198-D2's own evaluators (FV, base_table), imported
     unchanged.
A component with no exits, or whose every exit target has out-degree 0, is exactly its directed sixteen-cycle (swap
displacement 8; q = 16 only), as in PR195-D0, PR196-D1 and PR198-D2.

PREDICTIONS (Local's, published before the run):
  QX-C1 (control): at r = 52,808 the class representative (PR196's word rotated by one phase) gives exits at the
        phases 1, 5, 9 and 13. Both unordered exit targets have out-degree 0, reproducing PR198-D2.
  QX-C2 (control): every return passes step 1, and the exits from step 2 are legal edges under PR198-D2's evaluators.
  QX-P1 (blind, confidence 0.5): at 18826, 26356, 34854 and 40804, every exit target has out-degree 0, so all four
        components are exactly their sixteen-cycles.
  QX-D1 (descriptive): the out-degree of every exit target.
OUTCOME, 2026-10-09 20:56 BST (M5, 13 s, 44 MB, run at commit 6b1b9e23): QX-C1 PASS, QX-C2 PASS, QX-P1 REFUTED.
  - Every sixteen-cycle is in its H_m, and every D1 exit is a legal edge under PR198-D2's evaluators.
  - Exit phases and exit-target out-degrees:
    - 18826: phases 1, 9; out-degrees 1, 1;
    - 26356: phases 2, 7, 10, 15; all 0;
    - 34854: phases 1, 4, 5, 9, 12, 13; out-degrees 1, 0, 0, 1, 0, 0;
    - 40804: phases 0, 1, 7, 8, 9, 15; out-degrees 0, 2, 0, 0, 2, 0;
    - 49732: no exits;
    - 52808: phases 1, 5, 9, 13; all 0. That is PR198-D2's result in the class representative's phases.
  - Closed, each component exactly its directed sixteen-cycle (swap displacement 8; q = 16 only): r = 26,356, 49,732
    and 52,808.
  - Open: 18,826, 34,854 and 40,804. Each has an exit target with a successor, which is a two-edge prefix only (no
    return or persistence shown).
DEEPER (registered before running; COMMAND: ... rule30_q16_exits.py deep [DEPTH=300]): from every exit target with a
  successor (18826, 34854 and 40804), follow every successor path in H_m with PR198-D2's step. From (X, Y) at phase p
  the tails are TX, TY; K = 1 + V(TX 0) + V(TY 0); the candidates are (b, K + b), legal when F = 1 on both new windows.
  Exhaustive breadth-first to DEPTH steps. An exit flips a bit that stays in the window for m steps, so no exit path
  can rejoin the cycle before step m (m >= 9,412). A path that dies within DEPTH therefore closes nothing beyond itself.
  If every path from every exit dies, the component is exactly its sixteen-cycle. A survivor at DEPTH is a longer
  prefix only.
  QX2-C1 (control): at step 1 the out-degrees equal QX's (1, 1, 2 at phase 1, and their mirrors).
  QX2-P1 (blind, confidence 0.5): for at least two of the three, every exit path dies within 300 steps.
  QX2-D1 (descriptive): the number of live paths at each depth, and the depth of death or survival.
  Instrument repair (before any result): the first attempt stopped at once on PR198's strip-evaluator assertion. That
  evaluator assumes the window differs from the baseline only in its last 3 positions, and an exit path deviates in
  more. The search now uses PR198's packed evaluator (both paddings must agree) without its memo, which would keep every
  10^4-bit window. The strip evaluator stays as a spot check, widened to S = deviations + 3, at depths <= 5 and every
  50th depth. No result was seen before the repair.
"""
import sys

_ARGS = sys.argv[1:]
sys.argv = sys.argv[:1]
import rule30_pr196_d1 as d1          # noqa: E402
import rule30_pr198_d2 as d2          # noqa: E402

Q, H = 16, 8
RETS = {18826: '1111111111101110', 26356: '1011110111010000', 34854: '1111100111011000', 40804: '1001001111011000',
        49732: '1111111111111100', 52808: '1100010100110000'}


def analyse(r, cls):
    full = (1 << Q) - 1
    wint = int(cls[::-1], 2)
    m = (r - 2) // 2
    Um = d1.U_masks(wint, Q, 2 * m)
    F, Vm, Cm = Um[2 * m - 1], Um[2 * m - 2], Um[2 * m]
    c5 = F == full and all(((Cm >> t) & 1) ^ ((Cm >> ((t + H) % Q)) & 1) == 1 for t in range(Q))
    c5 &= all(((Vm >> ((t + 1) % Q)) & 1) ^ ((Vm >> ((t + 1 + H) % Q)) & 1) == 1 for t in range(Q))
    c5 &= Cm == full ^ d1.rot(Vm, 1, Q)
    dm = d1.d_masks(Um, Q, m)
    exit_phases = [t for t in range(Q) if not (dm >> t) & 1 and not (dm >> ((t + H) % Q)) & 1]
    w = [int(b) for b in cls]
    win = lambda t: [w[(t + i) % Q] for i in range(m)]
    TAB = d2.base_table(w, 2 * m - 1)
    legal_ok, degs = True, {}
    for t in exit_phases:
        X, Y = win(t), win(t + H)
        bx, by = w[(t + m) % Q], w[(t + H + m) % Q]
        Xp, Yp = X[1:] + [1 - bx], Y[1:] + [1 - by]
        fXp, vXp, a1 = d2.FV(Xp, m, TAB, t + 1)
        fYp, vYp, a2 = d2.FV(Yp, m, TAB, t + H + 1)
        legal_ok &= fXp == fYp == 1 and vXp ^ vYp == 1 and a1 and a2
        TX, TY = Xp[1:], Yp[1:]
        _, vX0, _ = d2.FV(TX + [0], m, TAB, t + 2)
        _, vY0, _ = d2.FV(TY + [0], m, TAB, t + H + 2)
        K = 1 ^ vX0 ^ vY0
        deg = 0
        for b in (0, 1):
            fx, vx, e1 = d2.FV(TX + [b], m, TAB, t + 2)
            fy, vy, e2 = d2.FV(TY + [K ^ b], m, TAB, t + H + 2)
            legal_ok &= e1 and e2
            deg += fx == 1 and fy == 1 and vx ^ vy == 1
        degs[t] = deg
    return c5, exit_phases, legal_ok, degs


def main():
    d2.T_START = __import__('time').time() + 10 ** 6       # PR198's 60 s wall cap is per witness; disable it here
    res = {}
    for r, cls in sorted(RETS.items()):
        c5, ex, lok, degs = analyse(r, cls)
        res[r] = (c5, ex, lok, degs)
        print('r = %5d: in H_m %s; exit phases %s; exits legal %s; exit-target out-degrees %s'
              % (r, c5, ex or 'none', lok, degs or '-'), flush=True)
    c5, ex, lok, degs = res[52808]
    print('QX-C1', 'PASS' if ex == [1, 5, 9, 13] and all(v == 0 for v in degs.values()) else 'FAIL')
    print('QX-C2', 'PASS' if all(v[0] and v[2] for v in res.values()) else 'FAIL')
    four = [18826, 26356, 34854, 40804]
    print('QX-P1', 'HELD' if all(all(d == 0 for d in res[r][3].values()) for r in four) else 'REFUTED %s'
          % {r: res[r][3] for r in four if any(res[r][3].values())})
    closed = [r for r in sorted(res) if all(d == 0 for d in res[r][3].values())]
    print('components exactly their sixteen-cycles:', closed)
    print('COMPLETE')


def FVp(bits, m):
    res = set()
    for pad in (0, 1):
        p = d2.eval_packed(list(bits) + [pad], [2 * m - 2, 2 * m - 1])
        res.add((p[2 * m - 1], p[2 * m - 2]))
    assert len(res) == 1, 'padding changed F or V'
    return res.pop()


def FVs(bits, m, tab, phase, S):
    res = set()
    for pad in (0, 1):
        st = d2.eval_strip(tab, phase, list(bits) + [pad], [2 * m - 2, 2 * m - 1], S=S)
        res.add((st[2 * m - 1], st[2 * m - 2]))
    assert len(res) == 1
    return res.pop()


def deep(DEPTH=300):
    out, spot_ok = {}, True
    for r in (18826, 34854, 40804):
        cls = RETS[r]
        c5, exit_phases, lok, degs = analyse(r, cls)
        m = (r - 2) // 2
        w = [int(b) for b in cls]
        win = lambda t: [w[(t + i) % Q] for i in range(m)]
        TAB = d2.base_table(w, 2 * m - 1)
        frontier = []
        for t in exit_phases:
            if t >= H:
                continue                                   # phase t + 8 mirrors t
            X, Y = win(t), win(t + H)
            bx, by = w[(t + m) % Q], w[(t + H + m) % Q]
            frontier.append((X[1:] + [1 - bx], Y[1:] + [1 - by], t + 1))
        step1, sizes, depth = None, [len(frontier)], 0
        while frontier and depth < DEPTH:
            nxt = []
            S = depth + 4
            for X, Y, ph in frontier:
                TX, TY = X[1:], Y[1:]
                _, vX0 = FVp(TX + [0], m)
                _, vY0 = FVp(TY + [0], m)
                K = 1 ^ vX0 ^ vY0
                for b in (0, 1):
                    Xn, Yn = TX + [b], TY + [K ^ b]
                    fx, vx = FVp(Xn, m)
                    fy, vy = FVp(Yn, m)
                    if depth <= 5 or depth % 50 == 0:
                        spot_ok &= FVs(Xn, m, TAB, ph + 1, S) == (fx, vx) and FVs(Yn, m, TAB, ph + H + 1, S) == (fy, vy)
                    if fx == 1 and fy == 1 and vx ^ vy == 1:
                        nxt.append((Xn, Yn, ph + 1))
            if depth == 0:
                step1 = len(nxt)
            frontier = nxt
            depth += 1
            sizes.append(len(frontier))
        out[r] = (step1, sizes, bool(frontier), depth)
        print('r = %5d: exit targets %d; live paths by depth %s%s; %s at depth %d'
              % (r, sizes[0], sizes[:12], ' ...' if len(sizes) > 12 else '', 'SURVIVES' if frontier else 'all dead', depth),
              flush=True)
    print('strip spot checks agree with the packed evaluator:', 'PASS' if spot_ok else 'FAIL')
    c1 = out[18826][0] == 1 and out[34854][0] == 1 and out[40804][0] == 2
    print('QX2-C1', 'PASS' if c1 else 'FAIL (step-1 counts %s)' % {r: v[0] for r, v in out.items()})
    dead = [r for r, v in out.items() if not v[2]]
    print('QX2-P1', 'HELD' if len(dead) >= 2 else 'REFUTED', '(all paths dead: %s)' % dead)
    print('COMPLETE')


if __name__ == '__main__':
    deep(int(_ARGS[1]) if len(_ARGS) > 1 else 300) if _ARGS[:1] == ['deep'] else main()
