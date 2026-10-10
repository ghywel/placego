"""GC1045: one bounded test of GC1044's proposed binary closure.

Missing inference: can the exact all-choice binary repair relation remain
binary after ONE further updated column? A majority counterexample would
refute this representation, including existential binary auxiliary bits.
Record searched: bijunctive|majority.closure|binary.clause +
repair|exterior|projection -> GC1044 only; its fixed-track result is reused.
Before execution, T=6 fixed, both clock phases, width4 only:
P1 (0.5): the w-track relation at every fixed v is majority-closed.
P2 (0.4): if P1 fails, three ACTUAL clamped finite seeds furnish a counter.
Counterfactual: finding no counter at T=6 proves closure at all horizons.
It does not; no wider sweep or solver job follows an inconclusive result.
Independent controls: literal Wolfram table, separate packed row updates,
and actual shrinking cones; an existing two-column binary relation must
be majority-closed on every triple. Unexpected check: demand actual-seed
positives, not merely three unlifted free-boundary strip paths.
After the bounded test found no counter (no larger test), a hand inference
changes the target: a joint binary relation cannot let v vary as well as w.
Informed P3, before independent controls: actual seeds1010,0100,0000 have
first (v,w) tracks (11,00),(01,11),(00,00) in phase0; their majority
(01,00) fails the first v update. The black phase complements v's last bit
and gives the same obstruction. Thus joint closure fails at EVERY T>=1,
since these three actual clamped seeds have infinite continuations.
Unexpected P3 check: erase v(1), which is an unobserved odd-time bit;
the remaining majority data have the actual0000 completion. This is not
an absent-visible-word certificate, nor a failure of fixed-v closure.
OUTCOME: P1 held only at T=6, P2 not triggered; fixed-v closure OPEN.
P3 hand obstruction and both-phase/deleted-coefficient controls PASS.
"""

from itertools import combinations, product

from rule30_exterior_binary import clauses, holds

T = 6
W = 4


def literal(a, b, c):
    return (30 >> (4*a + 2*b + c)) & 1


def step(row, wall, exterior):
    x = [wall] + list(row) + [exterior]
    return tuple(literal(x[i], x[i+1], x[i+2]) for i in range(W))


def packed_step(row, wall, exterior):
    mask = (1 << W)-1
    left = ((row << 1) | wall) & mask
    right = (row >> 1) | (exterior << (W-1))
    out = left ^ (row | right)
    return tuple((out >> i) & 1 for i in range(W))


def strip(phase):
    # Preserve full projected track labels; no per-cell projection.
    paths = {(r, (r[0],), (r[1],)) for r in product((0, 1), repeat=W)}
    for t in range(T):
        paths = {(n, v+(n[0],), w+(n[1],))
                 for r,v,w in paths for e in (0, 1)
                 for n in (step(r, (t+phase) % 2, e),)}
    out = {}
    for _,v,w in paths:
        out.setdefault(v, set()).add(w)
    return out


def actual(phase):
    out = {}
    for head in product((0, 1), repeat=T+2):
        # Last two bits zero, followed by a zero tail; enough cone for col4.
        row = list(head) + [0, 0]
        v, w = [row[0]], [row[1]]
        for t in range(T):
            x = [(t+phase) % 2] + row
            row = [literal(x[i], x[i+1], x[i+2])
                   for i in range(len(row)-1)]
            v.append(row[0]); w.append(row[1])
        out.setdefault(tuple(v), {})[tuple(w)] = ''.join(map(str,head))
    return out


def majority(a, b, c):
    return tuple(int(x+y+z >= 2) for x,y,z in zip(a,b,c))


def counter(relation, positive=None):
    for v in sorted(relation):
        ws = sorted(relation[v] if positive is None else positive.get(v, {}))
        for a,b,c in combinations(ws, 3):
            m = majority(a,b,c)
            if m not in relation[v]:
                return v,(a,b,c),m
    return None


def bits(x):
    return ''.join(map(str,x))


def main():
    for phase in (0, 1):
        for row in range(1 << W):
            for wall,e in product((0, 1), repeat=2):
                r = tuple((row >> i) & 1 for i in range(W))
                assert step(r,wall,e) == packed_step(row,wall,e)
        relation = strip(phase)
        seeds = actual(phase)
        assert all(set(ws) <= relation[v] for v,ws in seeds.items())
        u = tuple((t+phase) % 2 for t in range(T))
        for v in relation:
            binary = {w for w in product((0, 1), repeat=T+1)
                      if holds(clauses(u,v),w)}
            assert relation[v] <= binary
            assert counter({v:binary}) is None
        found = counter(relation)
        real = counter(relation,seeds)
        print('phase',phase,'P1 majority counter:',found)
        print('phase',phase,'P2 actual counter:',real)
        if real:
            v,ws,m=real
            print('fixed v',bits(v),'positive w',list(map(bits,ws)),
                  'negative majority',bits(m))
            print('actual seeds',[seeds[v][w] for w in ws])
    print('Literal/packed controls, actual inclusion and binary majority PASS')
    # Independent literal shrinking cones for the hand joint obstruction.
    for phase in (0, 1):
        joint = []
        for seed in ((1,0,1,0), (0,1,0,0), (0,0,0,0)):
            x = (phase,) + seed
            nxt = tuple((30 >> (4*x[i]+2*x[i+1]+x[i+2])) & 1
                        for i in range(len(seed)-1))
            joint.append((seed[0], nxt[0], seed[1], nxt[1]))
        expected = [(1,1-phase,0,0), (0,1-phase,1,1), (0,phase,0,0)]
        assert joint == expected
        m = majority(*joint)
        assert m == (0,1-phase,0,0)
        assert literal(phase,m[0],m[2]) != m[1]
        # Deleting the next v bit restores a literal actual completion.
        assert (m[0],m[2],m[3]) == (0,0,0)
        assert joint[2] == (0,phase,0,0)
    print('P3 PASS: actual joint majority fails at first update, both phases')
    print('Deleted odd-time v coefficient restores actual0000 completion PASS')


if __name__ == '__main__':
    main()
