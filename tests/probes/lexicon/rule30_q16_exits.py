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
"""
import sys

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


if __name__ == '__main__':
    main()
