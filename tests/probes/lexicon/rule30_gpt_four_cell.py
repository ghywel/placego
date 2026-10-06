"""Width-four one-hole certificate audit, preregistered 2026-10-06.

FC0 must: all64 four-cell updates agree with independent Rule30 truth table.
FC1 must: complete direct/subset languages agree for p3,5,7, n1..6.
FC2 blind: width four removes some visible word at p5, first restrictive
  width there because G15-G17 prove full freedom at widths1..3.
FC3 unexpected blind: p9 still has full visible freedom at width four.
FC4 blind: black relation powers repeat with period eight by exponent32.
CF must fail: width-two p4 admits11 (known forbidden).
REFUTED-BY: a control mismatch invalidates the run; a full reachable closed
  nonempty subset graph refutes FC2; an empty p9 transition refutes FC3.
OUTCOME first run: exit0, ALL CONTROLS PASS. FC0 all64 updates and FC1
all18 complete languages pass. FC2 REFUTED: p5 has a closed three-subset
full-shift certificate. Unexpected FC3 HELD: p9 also full. FC4 HELD: B^8=B^16,
first period-eight repeat exponent8. Other sampled odd p7,11,13,15 also full.
CF rejects known width-two p4 word11.

ADDENDUM before second run:
FC5 must: B^8=B^16 with the recorded exact masks; all representative odd
  p5,7,9,11,13,15 certificates close on the three-subset full-shift shape;
  every odd p5..129 matches this shape. p3 keeps its forbidden100 language.
FC6 must: all p5 visible words through12 bits exist in the subset graph;
  counts2**n at each length, n0..12.
OUTCOME second run: pending. Sixteen-state audit, no Local large entropy job duplicated.
"""

from itertools import product
from rule30_gpt_two_cell import step, direct, macro, advance, words


def black_power(k):
    rel = {s: {s} for s in range(16)}
    for _ in range(k):
        rel = {s: {step(x, 1, u, 4) for x in xs for u in (0,1)}
               for s,xs in rel.items()}
    return rel


def graph(p):
    rel = macro(4,p)
    start = frozenset(range(16))
    queue = [(start,'')]
    seen = {start}
    edges = {}
    missing = []
    for sub, prefix in queue:
        edges[sub] = []
        for bit in (0,1):
            nxt = advance(sub,bit,rel)
            edges[sub].append(nxt)
            if not nxt:
                missing.append(prefix+str(bit))
            elif nxt not in seen:
                seen.add(nxt)
                queue.append((nxt,prefix+str(bit)))
    return edges,missing


def main():
    for s,wall,u in product(range(16),(0,1),(0,1)):
        assert step(s,wall,u,4) == direct(s,wall,u,4)
    print('FC0 PASS: all64 transitions')
    for p,n in product((3,5,7),range(1,7)):
        assert words(4,p,n,'subset') == words(4,p,n,'direct')
    print('FC1 PASS: all18 complete languages')
    for p in (3,5,7,9,11,13,15):
        edges,missing = graph(p)
        print('GRAPH',p,'subsets',len(edges),'missing',missing)
        if p == 5:
            print('FC2','HELD' if missing else 'REFUTED')
            print('CERTIFICATE p5',[(sorted(s),[sorted(x) for x in out])
                                    for s,out in edges.items()])
        if p == 9:
            print('FC3','REFUTED' if missing else 'HELD')
    repeats = [k for k in range(33) if black_power(k) == black_power(k+8)]
    print('FC4','HELD' if repeats else 'REFUTED','exponents',repeats)
    if repeats:
        k = repeats[0]
        print('BLACK MASKS',k,[sum(1 << x for x in black_power(k)[s]) for s in range(16)])
    assert (1,1) not in words(2,4,2,'direct')
    print('CF FAILS AS REQUIRED: width-two p4 excludes11')
    print('ALL CONTROLS PASS')


if __name__ == '__main__':
    main()
