#!/usr/bin/env python3
"""rule30_fbr16.py: FBR16, the bounded first-genuine-branch test at common period Q = 16 (GPT's G161 procedure;
requested by GPT in GC192 and preregistered in RULE30-GPT.md at commit 10a3c13, before this script was written).

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_fbr16.py [TRANSCRIPT_DIR]
COST:       seconds expected; hard limits below.

The representative path of G161 on Q-periodic temporal words (bit t is time t; S c means c(t+1)): start at the root
pair (a, b) = (0, 1) with pair period q = 1. An active driver b has one child, built here by resetting at a black
cell of b, c(t0 + 1) = a(t0) XOR 1, and running c(t + 1) = a(t) XOR (b(t) OR c(t)) round the cycle. A zero driver
with even block parity of a (least period q) is a genuine branch: stop. With odd parity, stop at q = Q (the cap leaf);
otherwise integrate c(t + 1) = c(t) XOR a(t) from a chosen c(0) and double q. Every retained transition is checked by
the literal equation S c = a XOR (b OR c) at all Q times, separately from the constructor; the terminal node's type is
checked directly (at a cap leaf neither integration closes; at a branch the two children are not rotations).

PREDICTIONS, GPT's, published at 10a3c13 before this run (blind unless marked):
  FBR-P1 (blind): no even-parity zero-driver node on the Q = 16 path.
  FBR-P2 (blind): completion within 100,000 visited nodes.
  FBR-C1 (control): Q = 1, 2, 4, 8 give heights 3, 8, 29, 400 and labeled counts 3, 13, 97, 3065.
  FBR-C2 (control, forced by the smaller tree): K(16) > 400 if the cap leaf is certified.
  FBR-U (the unexpected check): the run with odd-integration choice c(0) = 1 has the same terminal type and height,
        and its same-depth pairs differ from the c(0) = 0 run's by a common temporal rotation.
Limits (GPT's): CPU 120 s, working memory 128 MiB, 100,000 nodes per representative; the first limit hit stops the
run, which is then partial and never a negative certificate. No Q = 32 in this block. Transcripts are written to
TRANSCRIPT_DIR, outside Git.

OUTCOME, 2026-10-07 (M5, one run; CPU 1.05 s for everything, peak RSS 20.8 MiB, both representatives far inside the
node cap). FBR-C1 PASS: heights 3, 8, 29, 400 and labeled counts 3, 13, 97, 3065. FBR-P1 REFUTED: the Q = 16 path
stops at a genuine branch, an even-parity zero-driver node at depth 53,207 (path length 53,208), so the rooted
rotation quotient at Q = 16 is not a chain. FBR-P2 HELD (completion within 100,000 nodes). FBR-C2 not applicable
(no cap leaf was reached; K(16) is at least 53,208 and is not determined here). FBR-U PASS: with c(0) = 1 the
terminal type and the length agree, and every same-depth pair differs by a common rotation. Independent checks
outside the run, on the transcript: from the witness pair (a, 0), a = 0000110001010011 in time order (least period
16, six ones), the map B walks back to the root (0, 1^16) in exactly 53,207 steps and the root then maps to zero; every
path node maps by B to its predecessor; the witness's two integrated children both close and are not rotations of
each other. Pair periods along the path: 3 nodes at 1, 5 at 2, 21 at 4, 371 at 8, then 52,808 at 16 from depth 400.
Prior record (found by GPT after the run, GC193): RULE30-GPT.md G2.3 had already certified the first branch at
diagonal 53,208 (white driver at 53,207) and the earlier doublings at 3, 8, 29, 400. So this run is an independent
replay that agrees with that record, not a new discovery; FBR-P1 was already refuted by it. Both GPT's
preregistration and Local's L115 ('open') missed the existing record.
"""
import json
import os
import resource
import sys
import time

CPU_LIMIT, MEM_LIMIT, NODE_CAP = 120.0, 128 * 1024 * 1024, 100000
resource.setrlimit(resource.RLIMIT_CPU, (int(CPU_LIMIT) + 5, int(CPU_LIMIT) + 5))   # hard backstop


def bit(w, t, Q):
    return (w >> (t % Q)) & 1


def rot(w, r, Q):
    m = (1 << Q) - 1
    r %= Q
    return ((w >> r) | (w << (Q - r))) & m


def least_period(w, Q):
    for d in range(1, Q + 1):
        if Q % d == 0 and rot(w, d, Q) == w:
            return d


def literal_ok(a, b, c, Q):
    return all(bit(c, t + 1, Q) == bit(a, t, Q) ^ (bit(b, t, Q) | bit(c, t, Q)) for t in range(Q))


def integrate(a, c0, Q):
    c, out = c0, 0
    for t in range(Q):
        out |= c << t
        c ^= bit(a, t, Q)
    return out, c == c0                          # the word, and whether it closes round the cycle


def active_child(a, b, Q):
    t0 = next(t for t in range(Q) if bit(b, t, Q))
    c = {(t0 + 1) % Q: bit(a, t0, Q) ^ 1}
    for k in range(1, Q):
        t = (t0 + k) % Q
        c[(t + 1) % Q] = bit(a, t, Q) ^ (bit(b, t, Q) | c[t])
    return sum(v << t for t, v in c.items())


def run(Q, c0_choice):
    a, b, q = 0, (1 << Q) - 1, 1
    path, t_start = [], time.process_time()
    while True:
        if len(path) >= NODE_CAP:
            return dict(stop='node cap', path=path)
        if len(path) % 1000 == 0:
            if time.process_time() - t_start > CPU_LIMIT:
                return dict(stop='cpu limit', path=path)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > MEM_LIMIT:
                return dict(stop='memory limit', path=path)
        path.append((a, b, q))
        if b != 0:
            c = active_child(a, b, Q)
            if not literal_ok(a, b, c, Q):
                return dict(stop='literal check failed at an active driver', path=path)
            a, b = b, c
            continue
        par = bin(a & ((1 << q) - 1)).count('1') % 2
        assert least_period(a, Q) == q, 'pair period drifted'
        if par == 0:
            k0, ok0 = integrate(a, 0, Q)
            k1, ok1 = integrate(a, 1, Q)
            distinct = ok0 and ok1 and all(rot(k0, r, Q) != k1 for r in range(0, Q, q))
            return dict(stop='genuine branch', path=path, verified=distinct)
        if q == Q:
            closes = integrate(a, 0, Q)[1] or integrate(a, 1, Q)[1]
            return dict(stop='cap leaf', path=path, verified=not closes)
        c, ok = integrate(a, c0_choice, Q)
        if not (ok and literal_ok(a, b, c, Q)):
            return dict(stop='literal check failed at an integration', path=path)
        a, b, q = b, c, 2 * q


def labeled(path):
    return sum(q for _, _, q in path)


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None
    t0 = time.process_time()
    ctl = {Q: run(Q, 0) for Q in (1, 2, 4, 8)}
    c1 = all(ctl[Q]['stop'] == 'cap leaf' and ctl[Q]['verified'] for Q in ctl)
    c1 &= [len(ctl[Q]['path']) for Q in (1, 2, 4, 8)] == [3, 8, 29, 400]
    c1 &= [labeled(ctl[Q]['path']) for Q in (1, 2, 4, 8)] == [3, 13, 97, 3065]
    print('FBR-C1', 'PASS' if c1 else 'FAIL', 'heights', [len(ctl[Q]['path']) for Q in (1, 2, 4, 8)],
          'labeled', [labeled(ctl[Q]['path']) for Q in (1, 2, 4, 8)])
    r0 = run(16, 0)
    r1 = run(16, 1)
    K0, K1 = len(r0['path']), len(r1['path'])
    print('Q = 16, choice c(0) = 0: stop = %s, verified = %s, K = %d' % (r0['stop'], r0.get('verified'), K0))
    print('Q = 16, choice c(0) = 1: stop = %s, verified = %s, K = %d' % (r1['stop'], r1.get('verified'), K1))
    complete = r0['stop'] in ('cap leaf', 'genuine branch') and r0.get('verified')
    print('FBR-P1', ('HELD' if r0['stop'] == 'cap leaf' else 'REFUTED') if complete else 'NOT DECIDED (%s)' % r0['stop'])
    print('FBR-P2', 'HELD' if complete and K0 <= NODE_CAP else 'REFUTED (%s)' % r0['stop'])
    if r0['stop'] == 'cap leaf' and r0.get('verified'):
        print('FBR-C2', 'PASS' if K0 > 400 else 'FAIL', 'K(16) = %d; labeled N(16) = %d; identity 3065 + 16 (K - 400) = %d'
              % (K0, labeled(r0['path']), 3065 + 16 * (K0 - 400)))
    same = r0['stop'] == r1['stop'] and K0 == K1
    if same:
        for (a0, b0, q0), (a1, b1, q1) in zip(r0['path'], r1['path']):
            if q0 != q1 or not any(rot(a0, r, 16) == a1 and rot(b0, r, 16) == b1 for r in range(16)):
                same = False
                break
    print('FBR-U', 'PASS' if same else 'FAIL', '(terminal type, height and same-depth rotation agreement)')
    rus = resource.getrusage(resource.RUSAGE_SELF)
    print('resources: CPU %.2f s, peak RSS %.1f MiB (macOS reports bytes), node cap %d per representative'
          % (time.process_time() - t0, rus.ru_maxrss / 1048576, NODE_CAP))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, 'fbr16-transcript.json'), 'w') as f:
            json.dump(dict(choice0=dict(stop=r0['stop'], K=K0, path=r0['path']),
                           choice1=dict(stop=r1['stop'], K=K1, path=r1['path'])), f)
        print('transcript written outside Git')


if __name__ == '__main__':
    main()
