#!/usr/bin/env python3
"""om189_cycle_clique.py: openai/math family 189, cycle-clique Ramsey numbers R(C_m, K_n) = (m-1)(n-1) + 1.

RUN-ON:     cpu (Python 3 and the python-sat package: pip install python-sat)
COMMAND:    python3 tests/probes/openai_math/om189_cycle_clique.py [SECONDS per instance, default 600]
            python3 tests/probes/openai_math/om189_cycle_clique.py --sym M N [SECONDS]   (one case, split by degree)
COST:       minutes; the largest case dominates, and an instance that runs out of time is reported as such.

The claim (preprint "Cycle-clique Ramsey numbers", 2026-09-25): for all m >= n >= 3 except (3, 3),
R(C_m, K_n) = (m-1)(n-1) + 1, the Erdos-Faudree-Rousseau-Schelp conjecture; R(C_3, K_3) = 6. That is the least N
such that every red-blue colouring of the complete graph on N vertices has a red m-cycle or a blue n-clique.
The proof is long and Cloud has not reviewed it. What Cloud replicates is the formula on small cases, by its own
encoding: one variable per edge (true = red), a clause against every red m-cycle and one against every blue n-set.
At N - 1 vertices the solver must find a colouring, which is then checked by a separate cycle search; at N it must
report none. The lower bound is also checked from the construction itself: n - 1 disjoint red cliques of m - 1
vertices, blue between them, has no red m-cycle (each red piece is too small) and no blue n-clique (blue is
(n-1)-partite).
Predictions (written before the run): every case below agrees with the formula; (3, 3) is the exception, with a
colouring on 5 vertices (the pentagon) and none on 6. Fail: a colouring at N, or none at N - 1. An instance that
times out confirms nothing and is reported as unsettled.
Control: R(C_3, K_3) = 6 is classical, and the solver's own colourings are re-checked without the solver.
Added after the first run, when the larger cases ran long (--sym): the "no colouring at N" instance is split by the
largest red degree D. Every graph can be relabelled so that vertex 0 has the largest degree and its neighbours are
1..D, so it suffices that each instance "vertex 0 adjacent to exactly 1..D, every degree at most D" has no
solution, for every D from ceil(N/(n-1)) - 1 (below that, greedy colouring gives n independent vertices) to N - 1.
Its control: the same split, one vertex below the threshold, must find a colouring, re-checked without the solver.
"""
import itertools, sys, threading, time

CASES = [(3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (4, 4), (5, 4), (6, 4), (5, 5)]


def var(i, j, N):
    i, j = min(i, j), max(i, j)
    return i * N - i * (i + 1) // 2 + (j - i - 1) + 1


def clauses(N, m, n):
    out = []
    for cyc in itertools.permutations(range(N), m):
        if cyc[0] == min(cyc) and cyc[1] < cyc[-1]:           # one listing per cycle
            out.append([-var(cyc[k], cyc[(k + 1) % m], N) for k in range(m)])
    for S in itertools.combinations(range(N), n):
        out.append([var(i, j, N) for i, j in itertools.combinations(S, 2)])
    return out


def has_cycle(adj, m):
    N = len(adj)

    def extend(path, seen):
        if len(path) == m:
            return path[0] in adj[path[-1]]
        return any(extend(path + [v], seen | {v}) for v in adj[path[-1]] if v not in seen and v > path[0])
    return any(extend([s], {s}) for s in range(N))


def has_blue_clique(adj, n):
    return any(all(j not in adj[i] for i, j in itertools.combinations(S, 2))
               for S in itertools.combinations(range(len(adj)), n))


def construction(m, n):
    N = (m - 1) * (n - 1)
    part = [v // (m - 1) for v in range(N)]
    return [{u for u in range(N) if u != v and part[u] == part[v]} for v in range(N)]


def solve(N, m, n, seconds):
    from pysat.solvers import Solver
    s = Solver(name="glucose4", bootstrap_with=clauses(N, m, n))
    timer = threading.Timer(seconds, s.interrupt)
    timer.start()
    t0 = time.time()
    ans = s.solve_limited(expect_interrupt=True)
    timer.cancel()
    model = s.get_model() if ans else None
    s.delete()
    if model is None:
        return ans, None, time.time() - t0
    red = set(x for x in model if x > 0)
    adj = [{j for j in range(N) if j != i and var(i, j, N) in red} for i in range(N)]
    return ans, adj, time.time() - t0


def solve_split(N, m, n, seconds):
    """No colouring at N, case by case on the largest red degree D (see the docstring). True, False or None."""
    from pysat.card import CardEnc, EncType
    from pysat.solvers import Solver
    base = clauses(N, m, n)
    top = var(N - 2, N - 1, N)
    for D in range(max(0, -(-N // (n - 1)) - 1), N):
        cls = list(base) + [[var(0, j, N)] for j in range(1, D + 1)] + [[-var(0, j, N)] for j in range(D + 1, N)]
        t = top
        for v in range(1, N):
            enc = CardEnc.atmost([var(v, u, N) for u in range(N) if u != v], bound=D, top_id=t,
                                 encoding=EncType.seqcounter)
            cls += enc.clauses
            t = max(t, enc.nv)
        s = Solver(name="glucose4", bootstrap_with=cls)
        timer = threading.Timer(seconds, s.interrupt)
        timer.start()
        t0 = time.time()
        ans = s.solve_limited(expect_interrupt=True)
        timer.cancel()
        if ans:
            red = {x for x in s.get_model() if 0 < x <= top}
            adj = [{j for j in range(N) if j != i and var(i, j, N) in red} for i in range(N)]
            assert not has_cycle(adj, m) and not has_blue_clique(adj, n)
        s.delete()
        print(f"  R(C{m}, K{n}) at {N} vertices, largest degree {D}: "
              f"{ {False: 'none', True: 'COLOURING', None: 'timed out'}[ans] } ({time.time() - t0:.1f} s)", flush=True)
        if ans is not False:
            return ans
    return False


def main():
    if sys.argv[1:2] == ["--sym"]:
        m, n = int(sys.argv[2]), int(sys.argv[3])
        seconds = float(sys.argv[4]) if len(sys.argv) > 4 else 3600
        N = (m - 1) * (n - 1) + 1
        # Control: the same split must find (and re-check) a colouring one vertex below the threshold.
        assert solve_split(N - 1, m, n, seconds) is True, "the split encoding missed a colouring at N - 1"
        print(f"control: the split finds a colouring at {N - 1} vertices", flush=True)
        ans = solve_split(N, m, n, seconds)
        verdict = {False: "proved by the split", None: "NOT settled", True: "FALSE"}[ans]
        print(f"R(C{m}, K{n}) <= {N}: {verdict}")
        return
    seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 600
    results = []
    for m, n in CASES:
        formula = 6 if (m, n) == (3, 3) else (m - 1) * (n - 1) + 1
        line = f"R(C{m}, K{n}): formula {formula}"
        ok = True
        if (m, n) != (3, 3):
            adj = construction(m, n)
            ok &= not has_cycle(adj, m) and not has_blue_clique(adj, n)
            line += "; construction on %d vertices checked" % (formula - 1)
        sat, adj, t1 = solve(formula - 1, m, n, seconds)
        ok &= sat is True and not has_cycle(adj, m) and not has_blue_clique(adj, n)
        line += f"; {formula - 1} vertices: {'colouring found and re-checked' if sat else sat} ({t1:.1f} s)"
        unsat, _, t2 = solve(formula, m, n, seconds)
        state = {False: "no colouring", True: "COLOURING FOUND", None: "timed out, unsettled"}[unsat]
        line += f"; {formula} vertices: {state} ({t2:.1f} s)"
        results.append((ok and unsat is False, unsat is None))
        print(line, flush=True)
    print(f"{sum(r for r, _ in results)} of {len(CASES)} cases agree with the formula; "
          f"{sum(t for _, t in results)} unsettled by the time limit")
    print("PASS" if all(r for r, t in results if not t) else "FAIL")


if __name__ == "__main__":
    main()
