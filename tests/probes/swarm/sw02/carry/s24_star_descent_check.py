"""Bounded check of the degree step in the direct route to Theorem D (S-24 feasibility map).

Claim checked (finite windows only): let Q(u, w) be a Boolean function of u_0..u_{r-1}, w_0..w_{r-1}
with Q(u, 0) = 0 and Q(u, w) = Q(w, u).  Put (u (+) w)_i = u_i ^ w_i ^ Q(u_{i+1..i+r}, w_{i+1..i+r}).
If Q(u, w) = Q(u (+) w, w) for all u, w, then Q = 0.

Prediction: UNSAT ("Q != 0" impossible) for r = 1, 2, 3.
Counterfactual: a nonzero Q would mean the degree step is wrong.
Controls (must be SAT): (a) drop Q(u, 0) = 0 (Q = 1 works); (b) drop symmetry (Q(u, w) = w_0 works).
Output: one line per case.  No identifiers are printed.
"""
import itertools
import sys

from pysat.solvers import Cadical195


def run(r, identity=True, symmetric=True):
    n = 2 * r  # (u (+) w)_{0..r-1} reads u, w up to index 2r-1
    var = {}

    def q(a, b):
        key = (a, b)
        if key not in var:
            var[key] = len(var) + 1
        return var[key]

    words = list(itertools.product((0, 1), repeat=r))
    for a in words:
        for b in words:
            q(a, b)
    clauses = []
    zero = tuple([0] * r)
    if identity:
        for a in words:
            clauses.append([-q(a, zero)])
    if symmetric:
        for a in words:
            for b in words:
                clauses.append([-q(a, b), q(b, a)])
                clauses.append([q(a, b), -q(b, a)])
    clauses.append([q(a, b) for a in words for b in words])  # Q is not identically 0
    for u in itertools.product((0, 1), repeat=n):
        for w in itertools.product((0, 1), repeat=n):
            # bit i of u (+) w is the literal c_i ^ q(u[i+1:i+1+r], w[i+1:i+1+r]),
            # with c_i = u_i ^ w_i; coordinates beyond the window are irrelevant to Q at 0..r-1
            lits = []
            for i in range(r):
                ui = tuple(u[i + 1:i + 1 + r])
                wi = tuple(w[i + 1:i + 1 + r])
                c = u[i] ^ w[i]
                lits.append((c, q(ui, wi)))
            lhs = q(tuple(u[:r]), tuple(w[:r]))
            for choice in words:
                # if bits == choice then lhs <-> q(choice, w[:r])
                guard = []
                for (c, v), ch in zip(lits, choice):
                    # bit = c ^ v ; bit == ch  <=>  v == (ch ^ c)
                    need = ch ^ c
                    guard.append(-v if need == 1 else v)  # negation of (v == need)
                rhs = q(choice, tuple(w[:r]))
                clauses.append(guard + [-lhs, rhs])
                clauses.append(guard + [lhs, -rhs])
    with Cadical195(bootstrap_with=clauses) as s:
        sat = s.solve()
        model = s.get_model() if sat else None
    return sat, len(var), len(clauses), model


def main():
    for r in (1, 2, 3):
        sat, nv, nc, _ = run(r)
        print(f"r={r} identity+symmetry: {'SAT (nonzero Q exists)' if sat else 'UNSAT (Q = 0 forced)'}"
              f"  vars={nv} clauses={nc}")
    for r in (1, 2):
        sat, *_ = run(r, identity=False)
        print(f"control r={r} no identity: {'SAT' if sat else 'UNSAT'} (expected SAT)")
        sat, *_ = run(r, symmetric=False)
        print(f"control r={r} no symmetry: {'SAT' if sat else 'UNSAT'} (expected SAT)")


if __name__ == "__main__":
    sys.exit(main())
