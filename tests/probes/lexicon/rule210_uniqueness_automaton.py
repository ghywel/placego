#!/usr/bin/env python3
"""rule210_uniqueness_automaton.py: UQ, a finite check intended to prove that the empty-left full 0101 Rule 210 family
is exactly G60's seed R (sites coprime to 6): no mixed-parity member. Local's lane (the real-orbit census, GC461);
follows TS, SW, CL (L270-L273). Claimed in CLOUD-LOCAL.md with these predictions pushed before the run.

RUN-ON:     cpu, one core, Python standard library
COMMAND:    python3 tests/probes/lexicon/rule210_uniqueness_automaton.py
COST:       to be recorded (expected seconds).

THE ARGUMENT (hand part; the probe does the finite part).
Diagonals. Put D_c(s) = x_s(c - s), the cells with i + s = c. Rule 210, x' = l XOR (1 - c) r, becomes
    D_c(s+1) = D_(c-2)(s) XOR (1 - D_(c-1)(s)) D_c(s),      D_c(0) = x_0(c),      clock: D_c(c) = c mod 2.
So diagonal c is an XOR accumulator fed by diagonal c - 2 that resets wherever diagonal c - 1 is black, and the
census adds one diagonal per site.
R's background. R runs Rule 90 (L270), so every cell with i + s even is white: every even diagonal of R is white for
all s, including the left half (G26's parity). Away from the left boundary (cells whose cone [i - s, i + s] lies in
sites >= 1, that is s <= (c - 1)/2), R agrees with the full-line periodic orbit x_s(i) = [i + s odd][3 does not
divide i]: at s = 0 this is R, and one Rule 90 step maps it to itself with the parity flipped (for i + s odd, the
neighbours i - 1, i + 1 are not both multiples of 3, and they are both non-multiples exactly when 3 divides i).
Deviations. Fix a prefix equal to R through site c and a candidate for sites c + 1, ...; write Delta_c' = D'_c' XOR
D_c' for the deviation of diagonal c' > c (Delta = 0 for c' <= c). Inside a window s <= L with c >= 2L + 24, every
background cell is the periodic formula, so the deviation dynamics in the window depends only on c mod 6.
Beyond the window, for a candidate that survives the clock:
  - an even diagonal c' with Delta_c'(L) = 0 stays 0 for all s >= L, provided Delta_(c'-2) = 0 beyond L;
  - an odd diagonal c' keeps Delta_c'(s) = Delta_c'(L) for all s >= L, because R's diagonal c' - 1 is white
    everywhere (no resets) and Delta_(c'-1), Delta_(c'-2) vanish beyond L; so the clock at time c' holds exactly
    when Delta_c'(L) = 0, whatever the non-periodic region near the wall contains.
By induction over c', every surviving candidate has all deviations confined to the window, provided no even
diagonal ends the window with Delta(L) = 1 (an IRREGULAR state, which would void this argument at that L).
The automaton. States: (c' mod 6, Delta_(c'-1)[0..L], Delta_c'[0..L]). From each state, for each choice of site
c' + 1, compute Delta_(c'+1)[0..L]; kill the branch if c' + 1 is odd and Delta_(c'+1)(L) = 1 (the clock), flag
IRREGULAR if c' + 1 is even and Delta_(c'+1)(L) = 1. Start at the zero state at every residue. Uniqueness for all
prefixes from c0 = 2L + 24 on follows if no IRREGULAR state is reachable, and no path that has deviated (some site
differs from R) survives indefinitely: in a finite graph that means no cycle through deviated states and no return
to the zero state after a deviation. Below c0 the census (CL, to depth 1200) already forces R.

PREDICTIONS (Local's, published before the run):
  UQ-P1 (confidence 0.7): with L = 48, no IRREGULAR state is reachable from any residue.
  UQ-P2 (confidence 0.7): no deviated path returns to the zero state and the deviated states form no cycle; every
         deviation is killed within 4 added diagonals (CL: decided by the next depth = 1 or 5 mod 6).
  UQ-P3: so, with CL's census through depth 1200 > c0 = 120, the family is exactly {R}.
  UQ-C0 (control): from the zero state at residue 1 (prefix through 6k + 1), the surviving site pairs after two
         steps are {00, 10, 11}, and the surviving triples after three steps from residue 1 match CL's set
         (all except 010, 011) for sites 6k + 2 .. 6k + 4; both values of site 6k + 6 survive one step from residue 5.
  UQ-C1 (control, can say no): with the background shifted by one site (a wrong far field), the automaton disagrees
         with CL's tail sets or reports a surviving deviated cycle or an IRREGULAR state.
OUTCOME (main run), 2026-10-08 05:26 (M5, one run at commit a3b9838; transcript outside Git; 0.0 s). UQ-P1, P2, P3
HELD and UQ-C0, C1 PASS. No IRREGULAR state; 9 deviated surviving states, acyclic, none returning to the zero state;
the longest deviated life is 3 diagonals (CL: decided by the next depth = 1 or 5 mod 6); the residue-1 pairs and
triples and the residue-5 singles equal CL's tail sets; the shifted background gives 32 IRREGULAR states and
different tails. Independent reading of the argument requested (L274) before anything is filed.
CROSS MODE (python3 tests/probes/lexicon/rule210_uniqueness_automaton.py cross), prediction published before its run:
  UQ-X1: for every e = 601 .. 612 and all 16 assignments of sites e .. e+3 on top of R through e - 1, direct
         simulation of the full orbit (sites beyond e + 3 white) first breaks the clock in [e, e + 3] exactly at the
         diagonal where the automaton kills that path, and keeps it through e + 3 exactly when the automaton keeps it.
"""
import time

L = 48


def bg(c, s, shift=0):
    i = c - s + shift
    return 1 if (c + shift) % 2 == 1 and i % 3 != 0 else 0


def R(i, shift=0):
    return bg(i, 0, shift)


def step(state, delta, shift=0):
    """state = (r, A, B): r = c' mod 6, A = Delta_(c'-1), B = Delta_c' (tuples of L+1 bits). Add diagonal c'+1."""
    r, A, B = state
    cn = (r + 1) % 6 + 600                      # c'+1, lifted far from the wall: the window sees only residues
    cm1, c0 = cn - 2, cn - 1
    D = [0] * (L + 1)
    D[0] = delta
    for s in range(L):
        bA, bB, bN = bg(cm1, s, shift), bg(c0, s, shift), bg(cn, s, shift)
        new_b = bA ^ ((1 - bB) & bN)
        assert new_b == bg(cn, s + 1, shift), 'far-field background is not a Rule 210 orbit'
        pA, pB, pN = bA ^ A[s], bB ^ B[s], bN ^ D[s]
        D[s + 1] = (pA ^ ((1 - pB) & pN)) ^ new_b
    return ((r + 1) % 6, B, tuple(D))


def run(shift=0):
    zero = tuple([0] * (L + 1))
    irregular, killed, dev_return = 0, 0, False
    tails = {}
    graph = {}                                   # deviated surviving state -> successor deviated states
    frontier = []
    for r0 in range(6):
        paths = [((r0, zero, zero), ())]
        for k in range(1, 4):                    # tails of up to three added sites from the zero state
            nxt_paths = []
            for st, sites in paths:
                for delta in (0, 1):
                    nxt = step(st, delta, shift)
                    c1 = nxt[0]
                    if nxt[2][L]:
                        if c1 % 2:
                            killed += 1
                        else:
                            irregular += 1
                        continue
                    nsites = sites + (R(c1 + 600, shift) ^ delta,)
                    tails.setdefault((r0, k), set()).add(nsites)
                    nxt_paths.append((nxt, nsites))
            paths = nxt_paths
        for delta in (1,):
            nxt = step((r0, zero, zero), delta, shift)
            frontier.append(nxt)
    # every deviated path starts with one deviating site from a zero state; explore all surviving continuations
    todo = [st for st in frontier if not (st[2][L] and st[0] % 2)]
    for st in todo:
        if st[2][L] and st[0] % 2 == 0:
            irregular += 1
    todo = [st for st in todo if not st[2][L]]
    while todo:
        st = todo.pop()
        if st in graph:
            continue
        graph[st] = []
        for delta in (0, 1):
            nxt = step(st, delta, shift)
            if nxt[2][L]:
                if nxt[0] % 2:
                    killed += 1
                else:
                    irregular += 1
                continue
            if nxt[1] == zero and nxt[2] == zero:
                dev_return = True
                continue
            graph[st].append(nxt)
            todo.append(nxt)
    colour, cycle, depth = {}, False, {}

    def longest(v):
        nonlocal cycle
        if colour.get(v) == 1:
            cycle = True
            return 0
        if colour.get(v) == 2:
            return depth[v]
        colour[v] = 1
        d = 1 + max([longest(w) for w in graph[v]] or [0])
        colour[v] = 2
        depth[v] = d
        return d

    import sys
    sys.setrecursionlimit(100000)
    life = max([longest(v) for v in graph] or [0])
    return irregular, killed, cycle, dev_return, life, tails, len(graph)


def main():
    t0 = time.time()
    irr, killed, cyc, ret, life, tails, nst = run()
    print('IRREGULAR %d, killed %d, deviated states %d, cycle among them %s, deviated return to zero %s, '
          'longest deviated life %d diagonals' % (irr, killed, nst, cyc, ret, life))
    p1 = irr == 0
    p2 = not cyc and not ret and life <= 4
    pairs = sorted(t for t in tails.get((1, 2), ()))
    triples = sorted(t for t in tails.get((1, 3), ()))
    singles5 = sorted(t for t in tails.get((5, 1), ()))
    c0 = (pairs == [(0, 0), (1, 0), (1, 1)]
          and triples == sorted(t for t in [(a, b, e) for a in (0, 1) for b in (0, 1) for e in (0, 1)]
                                if t[:2] != (0, 1))
          and singles5 == [(0,), (1,)])
    print('residue 1 pairs %s; triples %s; residue 5 singles %s' % (pairs, triples, singles5))
    print('UQ-P1', 'HELD' if p1 else 'REFUTED')
    print('UQ-P2', 'HELD' if p2 else 'REFUTED')
    print('UQ-P3', 'HELD' if p1 and p2 and c0 else 'NOT ESTABLISHED')
    print('UQ-C0', 'PASS' if c0 else 'FAIL')
    try:
        irr1, _, cyc1, ret1, _, tails1, _ = run(shift=1)
    except AssertionError as e:
        irr1, cyc1, ret1, tails1 = 1, False, False, {}
        print('shifted background rejected:', e)
    agree = (sorted(tails1.get((1, 2), ())) == pairs and sorted(tails1.get((1, 3), ())) == triples)
    print('UQ-C1', 'PASS' if (not agree or irr1 or cyc1 or ret1) else 'FAIL',
          '(shifted: irregular %d, cycle %s, return %s, tails agree %s)' % (irr1, cyc1, ret1, agree))
    print('%.1f s' % (time.time() - t0))


def cross():
    import rule210_two_step_review as ts
    t0 = time.time()
    N = 640
    ts.B, ts.OFF = 2 * N + 40, N + 20
    ts.MASK = (1 << (ts.B + 1)) - 1
    zero = tuple([0] * (L + 1))
    agree, total, bad = 0, 0, []
    for e in range(601, 613):
        for pat in range(16):
            vals = [(pat >> j) & 1 for j in range(4)]
            st, auto = ((e - 1) % 6, zero, zero), None
            for j in range(4):
                delta = vals[j] ^ R(e + j)
                st = step(st, delta)
                if st[2][L]:
                    auto = e + j if (e + j) % 2 else ('IRREGULAR', e + j)
                    break
            sites = [i for i in range(1, e) if R(i)] + [e + j for j in range(4) if vals[j]]
            rs = ts.rows_of(sites, e + 3)
            direct = next((t for t in range(e, e + 4) if ts.bit(rs[t], 0) != t % 2), None)
            ok_prefix = all(ts.bit(rs[t], 0) == t % 2 for t in range(e))
            total += 1
            if direct == auto and ok_prefix:
                agree += 1
            else:
                bad.append((e, vals, auto, direct, ok_prefix))
    print('cross: %d of %d agree' % (agree, total), bad[:5])
    print('UQ-X1', 'HELD' if agree == total else 'REFUTED')
    print('%.1f s' % (time.time() - t0))


if __name__ == '__main__':
    import sys
    cross() if sys.argv[1:] == ['cross'] else main()
