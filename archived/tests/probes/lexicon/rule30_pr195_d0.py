#!/usr/bin/env python3
"""rule30_pr195_d0.py: PR195-D0, first-edge branching on the fixed return-88 witness, of RULE30-GPT.md (GPT's
preregistration at c0f3e90; claimed by Local in CLOUD-LOCAL.md at 7513fd3 before this script was written or run).

RUN-ON:     cpu (Python 3 standard library), one process
COMMAND:    python3 tests/probes/lexicon/rule30_pr195_d0.py
COST:       seconds; capped at 60 CPU s.

The witness: S84's first enumerated q = 8 source whose walk first returns to zero at r = 88 (m = 43, h = 4), the
profiles followed from the first child of (a, 0). Its closed paired walk has eight ordered vertices
v_t = (X(t), X(t + 4)), X(t) the 43-bit window of the q-periodic word w at t, with edges appending
(b, b') = (w(t + 43), w(t + 47)). G190's edge equation fixes b + b', so the only other candidate edge from v_t
appends (b + 1, b' + 1); it is legal exactly when F43 = U_85 is 1 on both new windows. Phase t + 4 is the swap of t.

PREDICTION (GPT's, published before this run): at least one of the four distinct unordered decisions has a legal
alternative. If all fail, the fixed component is exactly its eight-cycle (swap displacement 4, admitting q = 8 only).
CONTROLS (GPT's): the unflipped edges reproduce S84's cycle and length-4 swap path; F43 by a literal scalar backward
recurrence and by an independent packed-bit reconstruction; the affine V43 identity and G193's target-label condition;
phase t + 4 is the swapped copy of t with equal legality; flipping X then solving Y equals flipping Y then solving X;
padding independence: F43 on a 43-bit window is the same with either padding bit, in both implementations.

OUTCOME, 2026-10-07 (M5, one process; CPU 0.03 s, peak RSS 9.0 MiB; one run for the result, rerun once after
recording to confirm the file, identical output). Witness: source a = 17
(4-bit block 1000), first child, first return at r = 88; w = 00111101 (time order). Controls all PASS: on every cycle
window F43 is the same with padding 0 and 1 and in both implementations; the unflipped edges reproduce S84's
eight-cycle, each satisfying the XOR equation and G193's label condition, with v_4 the swap of v_0; the affine V43
identity holds; at every phase the two controlled streams give the same alternative pair (both bits flipped), the XOR
equation holds for it, and both evaluators and both paddings agree on the new F43 values. The eight ordered
alternatives have F43 pairs (1, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 0), (1, 0), (1, 0) at phases 0 to 7; phase
t + 4 mirrors t; none is legal, and no alternative target lies on the cycle. PR195-D0's prediction (at least one legal
alternative) is REFUTED. As preregistered, that certifies the fixed component: the eight-cycle has no outgoing edge
but its recorded successor, so its strongly connected component is exactly that directed cycle, with swap
displacement 4, admitting q = 8 only. Other components at r = 88 remain unclassified.
"""
import resource
import sys
import time

Q, H, M = 8, 4, 43


def rot(w, d, q):
    d %= q
    return ((w >> d) | (w << (q - d))) & ((1 << q) - 1)


def children(a, b, q):
    """Children by the descending recursion from two seeds (rule30_rq3.children), checked forward."""
    out = []
    bit = lambda w, t: (w >> (t % q)) & 1
    for c0 in (0, 1):
        c = [c0]
        for t in range(q - 1):
            c.append(bit(a, t) ^ (bit(b, t) | c[t]))
        if bit(a, q - 1) ^ (bit(b, q - 1) | c[q - 1]) == c0:
            out.append(sum(v << t for t, v in enumerate(c)))
    return out


def witness():
    """S84's first q = 8 source (odd 4-bit block, first child) whose walk first returns to zero at 88."""
    for blk in range(16):
        if bin(blk).count('1') % 2 == 0:
            continue
        a = blk | (blk << 4)
        c = children(a, 0, Q)[0]
        prof, x, y = [0, c], 0, c
        while y and len(prof) < 1000:
            x, y = y, children(x, y, Q)[0]
            prof.append(y)
        if len(prof) - 1 == 88:
            return a, prof
    raise SystemExit('witness not found')


def U_scalar(n, bits):
    """Literal scalar recurrence on a list: U_0 = U_1 = w, U_(k+2)(t) = U_k(t + 1) + (U_(k+1)(t) OR U_k(t))."""
    L = [list(bits), list(bits)]
    for k in range(2, n + 1):
        a, b = L[k - 2], L[k - 1]
        L.append([a[t + 1] ^ (b[t] | a[t]) for t in range(min(len(a) - 1, len(b)))])
    return L[n][0]


def U_packed(n, bits):
    """Independent packed-bit reconstruction: words as integers (bit t = time t) with explicit lengths."""
    v = sum(b << t for t, b in enumerate(bits))
    a, la, b, lb = v, len(bits), v, len(bits)          # U_0 and U_1
    for k in range(2, n + 1):
        ln = min(la - 1, lb)
        mask = (1 << ln) - 1
        c = ((a >> 1) ^ (b | a)) & mask
        a, la, b, lb = b, lb, c, ln
    return b & 1


def window(w, t, m=M):
    return tuple((w >> ((t + i) % Q)) & 1 for i in range(m))


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    t0 = time.process_time()
    a, prof = witness()
    r = len(prof) - 1
    w = prof[r - 1]
    ok = r == 88 and prof[r - 2] == w and (r - 2) // 2 == M
    F = lambda X, pad, impl: impl(2 * M - 1, list(X) + [pad])
    V = lambda X, pad, impl: impl(2 * M - 2, list(X) + [pad])
    A = lambda X: U_scalar(2 * M, list(X) + [0])           # U_86 at 0 with w(t + 43) = 0, i.e. A_43(X)
    # controls on the evaluators: padding independence and agreement of the two implementations, on every window used
    wins = [window(w, t) for t in range(Q)]
    evals_ok = all(F(X, 0, U_scalar) == F(X, 1, U_scalar) == F(X, 0, U_packed) == F(X, 1, U_packed) for X in wins)
    print('witness: source a = %d (block %s), r = %d, m = %d; w = %s' % (a, format(a & 15, '04b')[::-1], r, M,
                                                                         ''.join(str((w >> t) & 1) for t in range(Q))))
    print('evaluator controls on the 8 cycle windows (padding 0/1, scalar/packed agree): %s' % ('PASS' if evals_ok
                                                                                                 else 'FAIL'))
    ok &= evals_ok
    verts = [(window(w, t), window(w, t + H)) for t in range(Q)]
    # the unflipped cycle: each vertex admitted, each actual edge valid (XOR condition, G193 label condition), and the
    # successor of v_t is v_(t+1); v_(t+4) is the swap of v_t
    cyc_ok = all(F(X, 0, U_scalar) == 1 and F(Y, 0, U_scalar) == 1 for X, Y in verts)
    for t in range(Q):
        X, Y = verts[t]
        b, b2 = (w >> ((t + M) % Q)) & 1, (w >> ((t + H + M) % Q)) & 1
        nxt = (X[1:] + (b,), Y[1:] + (b2,))
        cyc_ok &= nxt == verts[(t + 1) % Q]
        cyc_ok &= (b ^ b2) == 1 ^ A(X) ^ A(Y)
        cyc_ok &= V(nxt[0], 0, U_scalar) ^ V(nxt[1], 0, U_scalar) == 1
        cyc_ok &= verts[(t + H) % Q] == (Y, X)
    cyc_ok &= verts[H] == (verts[0][1], verts[0][0])
    print("unflipped cycle reproduces S84's eight-cycle and length-4 swap path: %s" % ('PASS' if cyc_ok else 'FAIL'))
    ok &= cyc_ok
    # the affine V43 identity: flipping the last bit of a window flips V43
    aff_ok = all(V(X, 0, U_scalar) ^ V(X[:-1] + (1 - X[-1],), 0, U_scalar) == 1 for X in wins)
    aff_ok &= all(V(X, 0, U_packed) == V(X, 0, U_scalar) for X in wins)
    print('affine V43 identity on the cycle windows: %s' % ('PASS' if aff_ok else 'FAIL'))
    ok &= aff_ok
    # the eight ordered alternative-edge decisions
    rows = []
    for t in range(Q):
        X, Y = verts[t]
        b, b2 = (w >> ((t + M) % Q)) & 1, (w >> ((t + H + M) % Q)) & 1
        nb, nb2 = 1 - b, 1 - b2
        # controlled streams: flip X's append and solve Y's from the XOR equation, and the reverse
        solveY = 1 ^ A(X) ^ A(Y) ^ nb
        solveX = 1 ^ A(X) ^ A(Y) ^ nb2
        streams_ok = solveY == nb2 and solveX == nb
        X2, Y2 = X[1:] + (nb,), Y[1:] + (nb2,)
        fX = {(pad, impl.__name__): F(X2, pad, impl) for pad in (0, 1) for impl in (U_scalar, U_packed)}
        fY = {(pad, impl.__name__): F(Y2, pad, impl) for pad in (0, 1) for impl in (U_scalar, U_packed)}
        eval_ok = len(set(fX.values())) == 1 and len(set(fY.values())) == 1
        fx, fy = fX[(0, 'U_scalar')], fY[(0, 'U_scalar')]
        xor_ok = (nb ^ nb2) == 1 ^ A(X) ^ A(Y)
        legal = fx == 1 and fy == 1 and xor_ok
        on_cycle = (X2, Y2) in verts
        rows.append((t, legal, fx, fy, xor_ok, streams_ok, eval_ok, on_cycle, X2, Y2))
        ok &= streams_ok and eval_ok and xor_ok
    hexw = lambda Z: format(sum(bit << i for i, bit in enumerate(Z)), '011x')
    for t, legal, fx, fy, xor_ok, streams_ok, eval_ok, on_cycle, X2, Y2 in rows:
        print('phase %d: alternative append flips both bits; F43 = %d, %d; XOR equation %s; streams %s; evaluators %s; '
              'legal %s; target on the cycle %s; windows %s / %s' % (
                  t, fx, fy, xor_ok, streams_ok, eval_ok, legal, on_cycle, hexw(X2), hexw(Y2)))
    sym_ok = all(rows[t][1] == rows[t + H][1] for t in range(H))
    print('phase t + 4 has the legality of phase t: %s' % ('PASS' if sym_ok else 'FAIL'))
    ok &= sym_ok
    legal_reps = [t for t in range(H) if rows[t][1]]
    print('four unordered decisions (phases 0-3): legal alternatives at %s' % (legal_reps or 'none'))
    print('PR195-D0 prediction (at least one legal alternative):', 'HELD' if legal_reps else 'REFUTED')
    if not legal_reps:
        print('so this fixed component is exactly its directed eight-cycle (swap displacement 4; q = 8 only)')
    print('all controls %s' % ('PASS' if ok else 'FAIL'))
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB' % (time.process_time() - t0, rus.ru_maxrss / 1048576))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
