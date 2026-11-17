#!/usr/bin/env python3
"""inquisition_background_rigidity_certificate.py: same-edge rigidity, proof-checked, for eight periodic backgrounds of
the edge frame, among them PR69's one-in-four ether and the classic 7 x 4 ether (L1261, round 6, T-D4).

RUN-ON:     cpu (Python 3 + kissat + cadical), minutes
COMMAND:    python3 tests/probes/inquisition_background_rigidity_certificate.py [WORKERS=6]

Theorem (per background R below): no code with a black edge (PR69's frame, X_0 = 1) follows R at two adjacent depths
(k, k+1) forever, at any depth k >= 1, from any onset and in any alignment; every episode has length at most
M_R(1) + (a + b)(k - 1). Argument (hand, short):
- Generic model: X_j(t) for j in Z, any initial state, X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) at every depth.
  A black-edge code is the generic configuration with X_j = 0 for j < 0 and X_0 = 1. The light cone of X_j(t) is
  depths j-2t..j at time 0, and every state is an initial state (time translation).
- Window instance W(a, b; r, u): over the light cone, if the pair at relative depths (0, 1) follows R (alignment
  (r, u)) on ticks 0..a+b, then X_(-1)(a) = R_(-1+r)(a+u). Each is checked UNSAT under kissat and cadical, and
  cadical's LRAT refutation is verified by lrat_check below.
- Onset-free descent: if the pair at depth k+1 follows R on ticks 0..L-1, apply W(a, b) to the configuration shifted
  to start at s-a, for each tick s in a..L-1-b. Then the pair at depth k (X_(k+1), X_k) follows R on a..L-1-b. So
  M_R(k+1) <= M_R(k) + a + b.
- Base: M_R(1) is finite (exhaustive below, all 4 prefixes and all alignments, horizon checked).
Controls, per instance: the system with the target unit negated is SAT (R itself is a model), and the LRAT proof
replayed against it is rejected. Globally: the alternating background (2, 2), which attaches (T-G), has a
satisfiable window at the same (a, b) as the classic ether. Every check is an explicit require().
The parameters (a, b) were found by T-D, T-D2 and T-D3; this file only checks them.
Predictions P-R1..P-R2: reports/inquisition-20261031.md (round 6), committed before this ran.
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_argv, sys.argv = sys.argv, sys.argv[:1]          # the ring module parses argv at import
from inquisition_ring_references import cycles  # noqa: E402
sys.argv = _argv

WORKERS = int(sys.argv[1]) if len(sys.argv) > 1 else 6
# background (p, q) -> (look-behind a, look-ahead b), one-depth onset-free descent
PARAMS = {(1, 1): (4, 1), (4, 8): (4, 2), (5, 5): (4, 2), (8, 20): (4, 6), (9, 72): (4, 5), (10, 6): (4, 2),
          (12, 12): (4, 2), (7, 28): (8, 50)}
WORK = os.environ.get('BCERT_WORK') or tempfile.mkdtemp(prefix='bcert-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
os.environ['BCERT_WORK'] = WORK                  # spawned workers share the parent's scratch directory


class CheckFailed(Exception):
    pass


def require(cond, msg=''):
    if not cond:
        raise CheckFailed(msg)


def instance(orbit, p, q, r, u, a, b):
    T = a + b
    lo = min(-2 * T, -1 - 2 * a)
    ids = {}

    def var(j, t):
        if (j, t) not in ids:
            ids[(j, t)] = len(ids) + 1
        return ids[(j, t)]

    ref = lambda j, t: orbit[(t + u) % q][(j + r) % p]
    cl = []
    for t in range(T):
        for j in range(lo + 2 * (t + 1), 2):
            x, y, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-x, y, c, d], [x, -y, c, d], [x, y, -c], [-x, -y, -c], [x, y, -d], [-x, -y, -d]]
    for t in range(T + 1):
        for j in (0, 1):
            cl.append([var(j, t)] if ref(j, t) else [-var(j, t)])
    cl.append([-var(-1, a)] if ref(-1, a) else [var(-1, a)])      # target unit: X_(-1)(a) differs from R
    return len(ids), cl


def write(nv, cl):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=WORK)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    return path


def sat(solver, nv, cl):
    path = write(nv, cl)
    try:
        pr = subprocess.run([solver, '-q', '-n', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    require(pr.returncode in (10, 20), (solver, pr.returncode))
    return pr.returncode == 10


def lrat_proof(nv, cl):
    path = write(nv, cl)
    proof = path + '.lrat'
    try:
        pr = subprocess.run(['cadical', '-q', '--lrat=true', '--no-binary', path, proof], capture_output=True, text=True)
        require(pr.returncode == 20, ('cadical did not report UNSAT', pr.returncode))
        with open(proof) as f:
            lines = [ln for ln in f.read().split('\n') if ln.strip()]
    finally:
        os.remove(path)
        if os.path.exists(proof):
            os.remove(proof)
    return lines


def lrat_check(cl, lines):
    """LRAT refutation check of clause list cl (clauses 1..len(cl)); RUP steps only (same checker as T-RC)."""
    db = {i + 1: list(c) for i, c in enumerate(cl)}
    for ln in lines:
        tok = [int(x) if x != 'd' else 'd' for x in ln.split()]
        cid = tok[0]
        if tok[1] == 'd':
            for x in tok[2:-1]:
                db.pop(x, None)
            continue
        z = tok.index(0, 1)
        lits, hints = tok[1:z], tok[z + 1:-1]
        require(tok[-1] == 0 and all(h > 0 for h in hints), "RAT step or malformed line")
        val = {abs(l): (l < 0) for l in lits}
        conflict = False
        for h in hints:
            und = []
            for l in db[h]:
                v = val.get(abs(l))
                if v is None:
                    und.append(l)
                elif v == (l > 0):
                    raise CheckFailed("hint already satisfied")
            if not und:
                conflict = True
                break
            require(len(und) == 1, "hint not unit")
            val[abs(und[0])] = und[0] > 0
        require(conflict, "no conflict along the hints")
        db[cid] = lits
        if not lits:
            return True
    raise CheckFailed("empty clause not derived")


def check_one(job):
    p, q, orbit, r, u, a, b = job
    nv, cl = instance(orbit, p, q, r, u, a, b)
    require(not sat('kissat', nv, cl), ('kissat SAT', p, q, r, u))
    require(not sat('cadical', nv, cl), ('cadical SAT', p, q, r, u))
    proof = lrat_proof(nv, cl)
    lrat_check(cl, proof)
    satvar = cl[:-1] + [[-x for x in cl[-1]]]
    require(sat('kissat', nv, satvar), ('unflipped system not SAT', p, q, r, u))
    try:
        lrat_check(satvar, proof)
        accepted = True
    except (CheckFailed, KeyError):
        accepted = False
    require(not accepted, ('LRAT checker accepted a proof of a satisfiable system', p, q, r, u))
    return len(proof)


def M1(p, q, orbit):
    """Exhaustive longest episode at depth 1 (pair X_2, X_1) following R, over 4 prefixes and all alignments."""
    H = 3 + 3 * q + 24
    best = 0
    for x1 in (0, 1):
        for x2 in (0, 1):
            for r in range(p):
                for u in range(q):
                    X = [1, x1, x2]
                    run = 0
                    for t in range(H):
                        st = orbit[(t + u) % q]
                        if X[1] == st[(1 + r) % p] and X[2] == st[(2 + r) % p]:
                            run += 1
                        else:
                            break
                        X = [1, X[1] ^ X[0], X[2] ^ (X[1] | X[0])]
                    require(run < H, ("depth-1 episode reaches the horizon", p, q))
                    best = max(best, run)
    return best


def main():
    refs = {(p, q): orbit for p in range(1, 13) for (pp, q, orbit) in cycles(p, 72)}
    total = 0
    for (p, q), (a, b) in PARAMS.items():
        orbit = refs[(p, q)]
        jobs = [(p, q, orbit, r, u, a, b) for r in range(p) for u in range(q)]
        with ProcessPoolExecutor(WORKERS) as ex:
            sizes = list(ex.map(check_one, jobs))
        m1 = M1(p, q, orbit)
        total += len(jobs)
        print(f"(p={p}, q={q}, {''.join(map(str, orbit[0]))}): {len(jobs)} alignments, W({a}, {b}) UNSAT under kissat and "
              f"cadical with checked LRAT proofs (largest {max(sizes)} lines); replays rejected; M_R(1) = {m1}  =>  "
              f"M_R(k) <= {m1} + {a + b}(k - 1) for every k", flush=True)
    # control: the alternating background (attaches) must have a satisfiable window at the classic ether's (a, b)
    alt = refs[(2, 2)]
    a, b = PARAMS[(7, 28)]
    open_al = [(r, u) for r in range(2) for u in range(2) if sat('kissat', *instance(alt, 2, 2, r, u, a, b))]
    require(open_al, "control failed: the alternating background's windows are all UNSAT")
    print(f"CONTROL: the alternating background has satisfiable windows W({a}, {b}) at alignments {open_al}")
    os.rmdir(WORK)
    print(f"BACKGROUND_RIGIDITY_CERTIFICATE_PASS ({total} window instances)")


if __name__ == '__main__':
    main()
