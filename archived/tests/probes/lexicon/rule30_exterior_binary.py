"""GC1044: keep ALL repairs through two additional updated columns.

Missing inference: GC1042's selected repair loses an actual train. Can the
full choice relation be kept without enumerating its optional bits?
Record searched: 2.SAT|bijunctive|binary clause + repair|column|exterior
-> two unrelated SAT probes; GC1042 supplies the exact one-step projection.
P1, before controls: the binary clauses below characterize ALL next-column
tracks for which w and z BOTH update, at every finite horizon.
P2: on actual1001 through four ticks, the clauses force col2's first two
bits01. This is an interior correlation, not just a chosen terminal bit.
Counterfactual: this proves arbitrary iteration or CL210's halfwidth bound.
It does neither: the coefficients depend on the fixed adjacent tracks.
Independent controls: every u,v,w at T=1..4, literal Wolfram-table existential
enumeration of z; h is free per tick. Constructed z,h replay literally.
Unexpected check: at T=3, repair0001 survives although GC1042's0000 dies;
the free terminal must be preserved. At T=4 it cannot repair w's first00.
OUTCOME: P1/P2 HELD: 18,720 literal triples, 324 constructed repairs;
free-terminal positive and actual-train bulk correlation PASS.
"""

from itertools import product

from rule30_exterior_repair import guards, repair


def clauses(u, v):
    """Literals (site, desired bit); a clause holds if any literal holds."""
    T = len(u)
    q = tuple(v[t+1] ^ u[t] for t in range(T))
    if any(v[t] and not q[t] for t in range(T)):
        return [()]  # the original column itself is impossible
    out = [((t, q[t]),) for t in range(T) if not v[t]]
    # w=1 requires its own next value to be NOT(v).
    out += [((t, 0), (t+1, 1-v[t])) for t in range(T)]
    for t in range(T-1):
        if not v[t]:
            continue
        if v[t+1]:
            out.append(((t, 1), (t+2, 0)))
        elif not q[t+1]:
            out.append(((t, 1), (t+2, 1)))
    for t in range(T-2):
        if v[t] or q[t]:
            continue
        if not v[t+2] and not q[t+2]:
            out.append(((t+1, 0), (t+3, 0)))
        elif v[t+2] and v[t+1]:
            out.append(((t+1, 0), (t+3, 1)))
    return out


def holds(cnf, w):
    return all(any(w[t] == b for t, b in clause) for clause in cnf)


def literal(a, b, c):
    return (30 >> (4*a + 2*b + c)) & 1


def exists(u, v, w):
    """Independent direct update test, with z enumerated and h local/free."""
    T = len(u)
    if not all(literal(u[t], v[t], w[t]) == v[t+1] for t in range(T)):
        return False
    for z in product((0, 1), repeat=T+1):
        if all(literal(v[t], w[t], z[t]) == w[t+1]
               and any(literal(w[t], z[t], h) == z[t+1] for h in (0, 1))
               for t in range(T)):
            return True
    return False


def main():
    cases = positives = 0
    for T in range(1, 5):
        for u in product((0, 1), repeat=T):
            for v in product((0, 1), repeat=T+1):
                cnf = clauses(u, v)
                for w in product((0, 1), repeat=T+1):
                    good = holds(cnf, w)
                    assert exists(u, v, w) == good, (u, v, w, cnf)
                    cases += 1
                    if good:
                        assert all(guards(v[:-1], w)[:3])
                        z, h = repair(v[:-1], w)
                        assert all(literal(u[t], v[t], w[t]) == v[t+1]
                                   and literal(v[t], w[t], z[t]) == w[t+1]
                                   and literal(w[t], z[t], h[t]) == z[t+1]
                                   for t in range(T))
                        positives += 1
    # Actual seed1001, independently shrink a literal cone through four ticks.
    row = [1, 0, 0, 1, 0, 0, 0, 0]
    v, actual = [row[0]], [row[1]]
    for t in range(4):
        old = [t % 2] + row
        row = [literal(old[i], old[i+1], old[i+2])
               for i in range(len(row)-1)]
        v.append(row[0])
        actual.append(row[1])
    assert v == [1, 1, 0, 0, 1] and actual[:4] == [0, 1, 0, 0]
    u = (0, 1, 0, 1)
    survivors = [w for w in product((0, 1), repeat=5)
                 if holds(clauses(u, v), w)]
    assert survivors and all(w[:2] == (0, 1) for w in survivors)
    assert holds(clauses(u, v), actual)
    # Stop one tick earlier: a terminal repair is still available.
    cnf = clauses(u[:3], v[:4])
    assert not holds(cnf, (0, 0, 0, 0))
    assert holds(cnf, (0, 0, 0, 1)) and exists(u[:3], v[:4], (0, 0, 0, 1))
    print('P1 PASS:', cases, 'literal triples;', positives, 'constructed repairs')
    print('P2 PASS: actual1001 forces first optional pair01 through four ticks')
    print('Unexpected free-terminal0001 positive through three ticks PASS')


if __name__ == '__main__':
    main()
