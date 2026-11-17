"""GC1042: exact correlated repair of one free exterior column.

CL210 asks whether a width-|f| strip always excludes an absent visible f.
Missing inference: can its free exterior be made into an updated column,
preserving the interior? Eliminate that ONE column exactly before seeking
a repeated repair. No SAT, language census, wider strip or Local run.
Record searched: w_min|half.cone|quarter.cone|halfwidth -> SW/SWP, CL210;
column extension + local|two equations -> GC380/381, GC754, GC798.
Those give profile-specific graphs or a different diagonal-OR projection.

Hand predictions before controls:
P1: the A/B guards below exactly characterize one-column repair at any T.
    They use up to three positions of (v,q), hence FOUR original rows:
    q(t)=v(t+1) XOR u(t). Do not drop that indexing offset.
P2: the canonical repair cannot safely be repeated, even for the proved
    eternal 1001 train. Its full col1 prefix1100 should already suffice.
Counterfactual: P1 alone, or arbitrary iteration of its chosen witness,
proves CL210's halfwidth conjecture. The positive train must refute that.
Controls: all pairs of finite tracks through T=1..5, against existential
literal Wolfram-table updates; no temporal or spatial periodicity imposed.
Unexpected check: isolate B with u=011,v=0100, which passes A; terminal
bits are free, so a missing final update must not create a false rejection.
OUTCOME: P1/P2 HELD; 2728 literal track pairs, 414 positive repairs;
B-only obstruction, actual-train positive and finite-terminal checks PASS.
The canonical repair is a witness for ONE added updated column only.
"""

from itertools import product


def guards(u, v):
    T = len(u)
    assert len(v) == T + 1
    q = tuple(v[t+1] ^ u[t] for t in range(T))
    base = all(not v[t] or q[t] for t in range(T))
    a = all(not (v[t] == v[t+1] == 0 and q[t] == 1 and q[t+1] == 0)
            for t in range(T-1))
    b = all(not (tuple(v[t:t+3]) == (0, 1, 0) and q[t] == q[t+2] == 1)
            for t in range(T-2))
    return base, a, b, q


def repair(u, v):
    base, a, b, q = guards(u, v)
    assert base and a and b
    T = len(u)
    w = [q[t] if v[t] == 0 else
         int(t > 0 and v[t-1] == 0 and q[t-1] == 1)
         for t in range(T)]
    # There is no prescribed exterior at the final row.
    w.append(1-v[T-1] if w[T-1] else 0)
    z = [w[t+1] ^ v[t] if w[t] == 0 else 0 for t in range(T)]
    return tuple(w), tuple(z)


def literal(left, centre, right):
    return (30 >> (4*left + 2*centre + right)) & 1


def exists(u, v):
    """Independent direct existential check, with both right choices per tick."""
    T = len(u)
    for w in product((0, 1), repeat=T+1):
        if not all(literal(u[t], v[t], w[t]) == v[t+1]
                   for t in range(T)):
            continue
        if all(any(literal(v[t], w[t], z) == w[t+1] for z in (0, 1))
               for t in range(T)):
            return True
    return False


def main():
    cases = positives = 0
    for T in range(1, 6):
        for u in product((0, 1), repeat=T):
            for v in product((0, 1), repeat=T+1):
                base, a, b, _ = guards(u, v)
                accepted = base and a and b
                assert exists(u, v) == accepted, (u, v, base, a, b)
                cases += 1
                if accepted:
                    w, z = repair(u, v)
                    assert all(literal(u[t], v[t], w[t]) == v[t+1]
                               and literal(v[t], w[t], z[t]) == w[t+1]
                               for t in range(T))
                    positives += 1
    u, v = (0, 1, 1), (0, 1, 0, 0)
    base, a, b, _ = guards(u, v)
    assert base and a and not b and not exists(u, v)
    # Literal full-row positive, with a shrinking cone and clamped clock.
    row = [1, 0, 0, 1, 0, 0, 0, 0]
    cols = [[row[i]] for i in range(3)]
    for t in range(3):
        old = [t % 2] + row
        row = [literal(old[i], old[i+1], old[i+2])
               for i in range(len(row)-1)]
        for i in range(3):
            cols[i].append(row[i])
    u, v = (0, 1, 0), tuple(cols[0])
    assert v == (1, 1, 0, 0) and tuple(cols[1]) == (0, 1, 0, 0)
    w, _ = repair(u, v)
    assert w == (0, 0, 0, 0)
    assert not exists(v[:-1], w)
    assert exists(v[:-1], tuple(cols[1]))
    print('P1 PASS:', cases, 'literal pairs,', positives, 'positive repairs')
    print('P2 PASS: actual1001 col1=1100; canonical col2=0000 cannot extend')
    print('B-only obstruction and finite-terminal controls PASS')


if __name__ == '__main__':
    main()
