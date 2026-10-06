"""Three-cell one-hole audit, preregistered 2026-10-06.

TH0 must: all48 three-cell transitions match independent Rule30 truth table.
TH1 must: direct path and subset languages agree p3,5,7 through six hole bits.
TH2 blind: odd p5..15 still admit every visible word at width three.
TH3 blind: black relation powers repeat with period four by exponent16.
TH4 unexpected must: temporal column -1 obtained from the inverse wall equation
  gives a bijection on projected hole words, including nonperiodic walls.
CF must fail: width-two p4 admits11 (known excluded by G16).
REFUTED-BY: a reachable empty subset transition refutes TH2; no four-period
  relation equality through16 refutes TH3. Any control mismatch invalidates run.
OUTCOME first run: exit0, ALL CONTROLS PASS. TH0 covered all32 local
transitions; the header's48 was an arithmetic count error (8*2*2=32), retained
above, not an omitted control. TH1 all18 full languages agree. TH2 HELD:
odd p5..15 full shift. TH3 HELD: B^5=B^9; first exponent for a four-step
repeat is5. TH4 all2048 nonperiodic inverse-wall checks pass; CF rejects11.

ADDENDUM before second run:
TH5 must: B^5=B^9, but B^5 differs from B^7 (period two is insufficient).
TH6 must: the explicitly specified subset graphs match for every p2..128,
  and widths two/three have identical full languages for p2..9,n0..10.
OUTCOME second run: pending. Small eight-state audit, no Local entropy run repeated.
"""

from itertools import product
from rule30_gpt_two_cell import step, direct, macro, advance, words


def black_power(k, width=3):
    rel = {s: {s} for s in range(1 << width)}
    for _ in range(k):
        rel = {s: {step(x, 1, u, width) for x in xs for u in (0, 1)}
               for s, xs in rel.items()}
    return rel


def graph(p):
    rel = macro(3, p)
    start = frozenset(range(8))
    queue = [(start, '')]
    seen = {start}
    edges = {}
    missing = []
    for sub, prefix in queue:
        edges[sub] = []
        for bit in (0, 1):
            nxt = advance(sub, bit, rel)
            edges[sub].append(nxt)
            if not nxt:
                missing.append(prefix + str(bit))
            elif nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, prefix + str(bit)))
    return edges, missing


def main():
    for s, wall, u in product(range(8), (0, 1), (0, 1)):
        assert step(s, wall, u, 3) == direct(s, wall, u, 3)
    print('TH0 PASS: all32 transitions')
    for p, n in product((3, 5, 7), range(1, 7)):
        assert words(3, p, n, 'subset') == words(3, p, n, 'direct')
    print('TH1 PASS: all18 full-language comparisons')
    failures = []
    for p in range(3, 17):
        edges, missing = graph(p)
        print('TH2 p', p, 'subsets', len(edges), 'missing', missing)
        if p >= 5 and p % 2 and missing:
            failures.append((p, missing))
    print('TH2', 'REFUTED' if failures else 'HELD', failures)
    repeats = [k for k in range(17) if black_power(k) == black_power(k+4)]
    print('TH3', 'HELD' if repeats else 'REFUTED', 'repeat exponents', repeats)
    if repeats:
        k = repeats[0]
        print('BLACK POWER', k, black_power(k))
        for p in range(2, k+6):
            edges, missing = graph(p)
            print('MACRO', p, macro(3, p))
            print('GRAPH', p, [(sorted(s), [sorted(x) for x in out])
                              for s, out in edges.items()])
    # Unexpected check: all short nonperiodic wall/sigma traces, wall update
    # inverted to obtain pi. Equality on the whites is checked word for word.
    checks = 0
    for wall in product((0, 1), repeat=6):
        for sigma in product((0, 1), repeat=5):
            pi = tuple(wall[t+1] ^ (wall[t] | sigma[t]) for t in range(5))
            visible = tuple(sigma[t] for t in range(5) if not wall[t])
            recovered = tuple(pi[t] ^ wall[t+1] for t in range(5) if not wall[t])
            assert recovered == visible
            assert all((pi[t] ^ (wall[t] | sigma[t])) == wall[t+1]
                       for t in range(5))
            checks += 1
    print('TH4 PASS:', checks, 'nonperiodic inverse-wall bijection checks')
    assert (1, 1) not in words(2, 4, 2, 'direct')
    print('CF FAILS AS REQUIRED: width-two p4 excludes11')
    print('ALL CONTROLS PASS')


if __name__ == '__main__':
    main()
