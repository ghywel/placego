"""GC1176 work block: oldest-age P corner, not a record census.

Record searched before controls: alternat/seed/horizon ->8 hits7files;
checkerboard/finite/clock ->12 hits6files; P/oldest ->8 hits7files.
GC677/678/691/692 and the left-only horizon convention read. The old
finite-defect invariant has a checkerboard exterior, not this zero tail.

PREDICTIONS BEFORE execution, 2026-10-13:
  The phase-1 row alternating through N-1, then black from N=2r+1,
  maps to phase-0 seed black at odd depths1..2r-1 and white farther out.
  For r=1,2,3 the first defect reaches depth1 at white tick2r;
  a black failure occurs by tick2r+5. This bound is a blind hypothesis,
  not an all-r claim, and is abandoned if one named fixture refutes it.
  Independent controls: literal Rule30 versus packed evolution and
  inverse-column reconstruction of the required visible prefix before
  the first failed black test. No right membership or solver runs.
  CF: the first defect at tick2r is itself a black-test failure; it is
  white, so the claim must fail. Finite P tail extensions cannot alter
  the first2r+6 depth1 values when the needed causal prefix is fixed.
  Unexpected check: r=2 has a shorter width-relative deadline than r=1;
  neither monotonic excess nor a fixed first-arrival delay is assumed.

SECOND PREREGISTRATION before front-cycle execution:
  In the moving frame f=2r+1-t, the first6 checkerboard defects start
  101010. A two-tick triangular map advances this six-bit state without
  farther inputs. Predict its initial orbit repeats within64 states,
  with period4 or8, and every r=1 mod4 state fails the black test by
  relative tick5 or forces11 by relative tick4 after arrival at tick2r.
  CF: if the closed state orbit has a residue escaping both tests,
  retain that failure and close only the even-r and r=3 mod4 subcases.
  Independent: literal spatial Rule30 transition on the defect triple
  versus expanded parity formulas. Unexpected: a repeat must include
  the initial state; a transient repeat cannot justify period from r0.
  This is one closed six-bit front orbit, not a seed or record census.

OUTCOME: the three seed controls pass (failures7,5,9). The closed
front orbit has period16, REFUTING period4/8. Residue9 also REFUTES
the proposed relative-five-tick deadline: depth1 is0,1,1,1,0,1;
required visible101 and all three black tests pass. No deeper front
or later time is pursued. The fixed orbit nevertheless closes14 of
16 r-residues by those tests; residues9 and13 stay OPEN. These are
all-depth corner obstructions, not an all-birth or prize result.
"""
from itertools import product
from rule30_prefix_realization import inverse, literal, packed, rule


def front(d, t):
    out = []
    for k, old in enumerate(d):
        b = d[k-1] if k >= 1 else 0
        c = d[k-2] if k >= 2 else 0
        # Output depth f(t+1)+k has parity k-t (f(0) odd).
        out.append(old ^ (b*(1-c) if (k-t) % 2 else c*(1-b)))
        j = (k-t) % 2
        # Old physical neighbours have parity 1-j, j, 1-j.
        physical = rule((1-j)^old, j^b, (1-j)^c)
        assert out[-1] == physical ^ j
    return tuple(out)


def front_cycle():
    state = tuple(map(int, '101010'))
    seen, orbit = {}, []
    while state not in seen:
        seen[state] = len(orbit)
        orbit.append(state)
        state = front(front(state, 0), 1)
    start, period = seen[state], len(orbit)-seen[state]
    print('six-bit front orbit transient', start, 'period', period)
    unresolved = []
    for r, d in enumerate(orbit):
        print('residue', r, ''.join(map(str,d)))
        assert d[0] == 1 and d[1] == r % 2
        assert d[2] == 1 ^ (((r+1)//2) % 2)
        assert d[3] == 0
        if r % 4 == 1:
            a = {j: (j % 2)^d[j-1] for j in range(1, 7)}
            rows = literal(a, 0, 5)
            # Only depth1 through tick5 uses these six known cells.
            x = [b[1] for b in rows]
            cut = (x[2] == 0 and x[4] == 0)
            failure = any(x[t] == 0 for t in (1,3,5))
            if not (cut or failure):
                unresolved.append(r)
            print(' residual', '11' if cut else 'black failure' if failure else 'OPEN', x)
    assert start == 0 and period == 16
    assert unresolved == [9,13]
    print('blind period4/8 and universal five-tick deadline REFUTED')
    print('closed front-cycle independent transitions PASS')


def main():
    for r in (1, 2, 3):
        n = 2*r+1
        ticks = 2*r+5
        # Finite prefix of the infinite-black-tail prototype; one output
        # loses one boundary cell, whose value is never treated as known.
        parent = [j % 2 if j < n else 1
                  for j in range(1, n+ticks+3)]
        image = [rule(parent[i+1], parent[i], 1 if i == 0 else parent[i-1])
                 for i in range(len(parent)-1)]
        seed = {j: j % 2 if j < n-1 else 0
                for j in range(1, len(image)+1)}
        assert image == list(seed.values())
        rows = literal(seed, 0, ticks)
        bit = packed(seed, 0, ticks)
        assert bit == [a.get(1, 0) for a in rows]
        assert bit[:2*r] == [1]*(2*r)
        assert bit[2*r] == 0
        failure = next((t for t in range(1, ticks+1, 2) if bit[t] == 0), None)
        assert failure is not None, ('blind deadline refuted', r, bit)
        q = [1-bit[t] for t in range(0, failure, 2)]
        decoded = inverse(q, 0)
        # The last determined cell is before the failed black condition.
        assert decoded[:failure] == [seed[j] for j in range(1, failure+1)]
        for far in product((0, 1), repeat=3):
            ext = dict(seed)
            ext.update({ticks+2+i: b for i, b in enumerate(far)})
            assert packed(ext, 0, ticks) == bit
        print('r', r, 'white visible before black failure', ''.join(map(str,q)),
              'failure tick', failure, 'first defect', 2*r,
              'literal/packed/inverse/8 exterior controls PASS')
    print('THREE FIXTURES ONLY; no all-r bound established')
    front_cycle()


if __name__ == '__main__':
    main()
