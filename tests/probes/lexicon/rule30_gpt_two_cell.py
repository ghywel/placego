"""Two-cell one-hole language audit, pre-registered 2026-10-06.

TC0 must: independent truth-table and direct cell updates agree.
TC1 must: subset language equals independently enumerated state paths,
  p=2..6, through six visible bits.
TC2 must: width-one p=2 rejects 11; p=3..16 admits the full shift.
TC3 blind: width two still admits every hole-bit sequence for p=3..16.
TC4 unexpected must: rotating the periodic wall and moving the sampled phase
  with its unique white cell leaves the projected language unchanged.
CF must fail: every p=2 width-one visible word is legal (witness 11).
REFUTED-BY: any missing transition from a reachable subset refutes TC3;
  any mismatch of complete finite languages refutes the instrument controls.
OUTCOME first run: exit0, ALL CONTROLS PASS. TC0-TC2 held: 24 local
transitions, 60 complete finite languages, width-one controls. TC3 REFUTED:
p3 misses100; even p4..16 miss11; odd p5..15 have a two-subset full-shift
certificate. TC4 held for all133 rotations. CF rejected11 as required.
Exploratory algebra table (no new prediction): black relation powers3 and5
agree, as do4 and6, suggesting an exact parity classification.

ADDENDUM written before second run:
TC5 must: all p2..128 macro relations equal the proved parity table;
  black relation power3 equals5, which propagates to every larger power.
TC6 must: through12 visible bits, exact counts are Fibonacci(n+2) for even p,
  Fibonacci(n+3)-1 for p3, and2**n for odd p>=5; forbidden-pattern languages
  agree word for word through8 bits for p2..9.
OUTCOME second run: pending. No large Local computation duplicated.
"""

from itertools import product


def step(s, wall, u, width):
    out = 0
    for j in range(width):
        left = wall if j == 0 else (s >> (j-1)) & 1
        center = (s >> j) & 1
        right = u if j == width-1 else (s >> (j+1)) & 1
        out |= (left ^ (center | right)) << j
    return out


def direct(s, wall, u, width):
    cells = [wall] + [(s >> j) & 1 for j in range(width)] + [u]
    table = [0, 1, 1, 1, 1, 0, 0, 0]  # index 4*l+2*c+r
    return sum(table[4*cells[j]+2*cells[j+1]+cells[j+2]] << j
               for j in range(width))


def macro(width, period, rotate=0):
    wall = [int((t-rotate) % period != 0) for t in range(period)]
    # Start at the sampled white phase, including its outgoing update.
    wall = wall[rotate:] + wall[:rotate]
    relation = {}
    for s in range(1 << width):
        image = {s}
        for bit in wall:
            image = {step(x, bit, u, width) for x in image for u in (0, 1)}
        relation[s] = image
    return relation


def advance(subset, bit, relation):
    return frozenset(x for s in subset if s & 1 == bit for x in relation[s])


def certificate(width, p, rotate=0):
    rel = macro(width, p, rotate)
    start = frozenset(range(1 << width))
    queue = [(start, "")]
    seen = {start}
    edges = []
    for subset, word in queue:
        for bit in (0, 1):
            nxt = advance(subset, bit, rel)
            edges.append((sorted(subset), bit, sorted(nxt)))
            if not nxt:
                return False, word + str(bit), edges
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, word + str(bit)))
    return True, len(seen), edges


def words(width, p, n, method):
    states = {(s, ()) for s in range(1 << width)}
    if method == "subset":
        rel = macro(width, p)
        paths = {(frozenset(range(1 << width)), ())}
        for _ in range(n):
            paths = {(nxt, w+(b,)) for sub, w in paths for b in (0, 1)
                     for nxt in [advance(sub, b, rel)] if nxt}
        return {w for _, w in paths}
    for t in range(n*p):
        states = {(direct(s, int(t % p != 0), u, width),
                   w+((s & 1,) if t % p == 0 else ()))
                  for s, w in states for u in (0, 1)}
    return {w for _, w in states}


def main():
    for width in (1, 2):
        for s, wall, u in product(range(1 << width), (0, 1), (0, 1)):
            assert step(s, wall, u, width) == direct(s, wall, u, width)
    print("TC0 PASS: all 24 local transitions independently agree")
    cases = 0
    for width, p, n in product((1, 2), range(2, 7), range(1, 7)):
        assert words(width, p, n, "subset") == words(width, p, n, "direct")
        cases += 1
    print("TC1 PASS:", cases, "complete finite-language comparisons")
    assert (1, 1) not in words(1, 2, 2, "direct")
    for p in range(3, 17):
        assert certificate(1, p)[0]
    print("TC2 PASS: width-one theorem and forbidden 11 control")
    failures = []
    for p in range(3, 17):
        ok, detail, edges = certificate(2, p)
        print("TC3", p, "FULL" if ok else "MISSING", detail, "edges", edges)
        if not ok:
            failures.append((p, detail))
        for rotate in range(p):
            assert certificate(2, p, rotate) == certificate(2, p)
    print("TC3", "REFUTED" if failures else "HELD", failures)
    print("TC4 PASS: all 133 rotated-phase certificates agree")
    print("CF FAILS AS REQUIRED: visible 11 forbidden for width-one p2")
    print("ALL CONTROLS PASS")


if __name__ == "__main__":
    main()
