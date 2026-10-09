#!/usr/bin/env python3
"""rule30_all_l_period10.py: AL, is there an infinite all-L orbit? The period-10 analogue of GPT's GC686 (portfolio
question 4; serves Q6). Local's run (chat L380), claimed in CLOUD-LOCAL.md with these predictions pushed before it.

RUN-ON:     cpu (Python 3 standard library); minutes
COMMAND:    python3 tests/probes/lexicon/rule30_all_l_period10.py

GC686 found the 84-cell ring on which the visible trace (site 1 at even times, wall 0101.. white at even times) reads
S = 100 for ever, by searching right halves whose every temporal column has period 6. Nobody has asked the same for
L = 10000: GC623 says only that consecutive long loops must each begin in the simple cylinder 111001, and that "no
visible all-L language exclusion" follows. AL runs GPT's search unchanged in method, at temporal period P:
  - a state is a pair (l, c) of adjacent temporal column profiles (P-bit words); (l, c) -> (c, r) is an edge exactly
    when c(t+1) = l(t) xor (c(t) or r(t)) at all t mod P (where c(t) = 1 this checks c(t+1) = not l(t) and frees
    r(t); where c(t) = 0 it fixes r(t));
  - the start is the wall profile and every site-1 profile with the visible word (1 then zeros at the even times),
    then the entrance cylinder at time 0 on sites 1 .. k;
  - breadth-first search gives the reachable pairs, and repeated removal of pairs with no successor leaves the live
    ones, those with an infinite continuation. A live cycle through the wall pair is a spatially periodic full-line
    orbit, certified by direct Rule 30 evolution on the ring.
Edge constructors are checked against the literal Rule 30 table on a seeded sample of pairs and on every edge of
any reported cycle (GC686 checked all 64 r words per pair; at P = 10 that is 1024 per pair, too many for every pair).

PREDICTIONS (Local's, published before the run):
  AL-C1 (control): at P = 6 with the S word and GC686's entrance 11101, the search reproduces GC686/GC687 exactly:
        3714 reachable pairs, 84 live pairs, and the ring 0x688eb74a45efb082671ee with spatial period 84.
  AL-C2 (control): every sampled edge constructor agrees with the literal table, and any reported ring evolves back
        to itself after P steps with site 0 reading 0101.. and site 1's even samples 10000.
  AL-P1 (blind, confidence 0.5): at P = 10, white-even wall, entrance 111001 (GC623's simple long cylinder), the
        live set is nonempty: an infinite all-L right half with every column of period 10 exists.
  AL-P2 (blind, confidence 0.45): there is a live cycle through the wall pair, so a full-line all-L ring exists.
  AL-P3 (blind, confidence 0.4): the live set is a single cycle (rigid, as GC687 found for S).
  AL-P4 (blind, confidence 0.8): the black-even phase copy has no live pair.
UNEXPECTED CHECK (blind, confidence 0.7): AL-U, with only the marker 1110 imposed (sites 1 .. 4), every live pair is
  reachable from an entrance whose sites 5 and 6 read 01, i.e. the search itself respects GC623's gate.
Counterfactual: no live pair at P = 10 would exclude all-L with every column of period 10 (not all-L in general);
a live set would make arbitrarily long all-L stretches physically possible, the L twin of GC686.
Smoke before the push, control only (P = 6, all-S; nothing at P = 10 was run): 20 entrance pairs, 3714 reachable,
84 live with out-degree 1, the ring 0x688eb74a45efb082671ee (sites 0, 1: 010101, 110100), as GC686/GC687.
It exposed one instrument fault, fixed before the push: entrances are keyed by their last pair, so the cycle
is rotated back to start at the wall.
OUTCOME, 2026-10-09 09:48 BST (M5, 4.1 s, run at commit 05dc6624): every control passed and every prediction HELD.
  AL-C1 PASS: P = 6 reproduces GC686 exactly (20 entrance pairs, 3714 reachable, 84 live, 0x688eb74a45efb082671ee).
  AL-C2 PASS: 400 sampled constructors per search agree with the literal table, every cycle edge is checked
      literally, and the ring returns to itself after 10 steps with sites 0 and 1 reading 0101010101 and 1101000100.
  AL-P1 HELD: at P = 10 with the white-even wall and entrance 111001: 198 entrance pairs, 424,415 reachable pairs,
      155 live.
  AL-P2 HELD: a live cycle runs through the wall pair, so there is a full-line all-L ring, of spatial period 155:
      0x35409b1caa645d715104db5291a2fe8415260ce (bit i is site i, site 0 the least significant bit). Its visible
      word is 10000 for ever: an infinite all-L orbit, the L twin of GC686.
  AL-P3 HELD: every live pair has live out-degree 1, so the 155 live pairs form one cycle, rigid in this domain.
  Correction (GPT GC743, before any reuse): out-degree 1 alone would allow disjoint cycles. The rigidity rests on
  coverage: the reported simple cycle has 155 pairs and covers all 155 live pairs (each edge also has a unique
  predecessor, l = c_next xor (c or r), so every finite live component is a cycle). AL-P3's code tests only
  out-degree; the conclusion stands on that coverage.
  AL-P4 HELD: the black-even phase has no entrance at all.
  AL-U HELD: with only the marker 1110 imposed (72 entrance pairs, the same 424,415 reachable and 155 live), every
      live continuation reads 01 at sites 5 and 6, which is GC623's simple long cylinder 111001.
  Checks after the run, exploratory (no predictions):
  - F^2 is the shift by 31 on the ring (F^4, F^6, F^8 by 62, 93, 124), so it is a turning row with vector (31, 2).
    |s| + p = 33 lies outside CL072's census window of 28, which is why the census saw no all-L witness;
    Proposition 22(a) applies, since 31 > 2.
  - A cut of the ring to [-200, 200] on the open line keeps site 0 alternating and site 1 reading 1101000100 for
    t = 0 .. 60.
  - L372's decoding gives the same left side: the wall and (1101000100)^inf alone decode to the ring's left half at
    depths 1 .. 400. So n completed L gaps (T = 10n observations, closing tick included) force J >= 10n - 6, with
    T - J_closed(n) running over 0 .. 6 periodically in n mod 31, and 6 exactly at n = 17 (mod 31). Each minimum is
    attained by the ring cut at J_closed, which completes n L gaps with 111001 back at time T (simulated n = 1 .. 31
    and 48; one cell shallower always fails). This sharpens GC706's 10n <= J + 20 for pure L to 10n <= J + 6.
"""
import json
import random
import sys
from collections import deque

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def bit(w, t, P):
    return (w >> (t % P)) & 1


def children(left, centre, P):
    fixed, free = 0, []
    for t in range(P):
        if bit(centre, t, P):
            if bit(centre, t + 1, P) != 1 ^ bit(left, t, P):
                return []
            free.append(t)
        else:
            fixed |= (bit(centre, t + 1, P) ^ bit(left, t, P)) << t
    return sorted(fixed | sum(((choice >> j) & 1) << t for j, t in enumerate(free))
                  for choice in range(1 << len(free)))


def literal_children(left, centre, P):
    return [r for r in range(1 << P) if all(
        bit(centre, t + 1, P) == TABLE[4 * bit(left, t, P) + 2 * bit(centre, t, P) + bit(r, t, P)]
        for t in range(P))]


def search(P, wall, visible, entrance):
    """visible: site 1's even-time samples; entrance: required time-0 bits of sites 2, 3, ... (site 1's is visible[0])."""
    cache = {}

    def nxt(a, b):
        if (a, b) not in cache:
            cache[(a, b)] = children(a, b, P)
        return cache[(a, b)]
    initial = [c for c in range(1 << P) if [bit(c, t, P) for t in range(0, P, 2)] == list(visible)]
    prefixes = {(wall, c): [wall, c] for c in initial}
    for required in entrance:
        ext = {}
        for (a, b), row in prefixes.items():
            for c in nxt(a, b):
                if bit(c, 0, P) == required:
                    ext.setdefault((b, c), row + [c])
        prefixes = ext
    graph, seen = {}, set(prefixes)
    queue = deque(prefixes)
    while queue:
        pair = queue.popleft()
        graph[pair] = [(pair[1], c) for c in nxt(*pair)]
        for child in graph[pair]:
            if child not in seen:
                seen.add(child)
                queue.append(child)
    reverse = {pair: [] for pair in graph}
    degree = {pair: len(e) for pair, e in graph.items()}
    for pair, edges in graph.items():
        for child in edges:
            reverse[child].append(pair)
    leaves = deque(p for p, d in degree.items() if d == 0)
    removed = set()
    while leaves:
        pair = leaves.popleft()
        if pair in removed:
            continue
        removed.add(pair)
        for prev in reverse[pair]:
            degree[prev] -= 1
            if degree[prev] == 0:
                leaves.append(prev)
    live = set(graph) - removed
    outdeg = sorted({sum(1 for c in graph[p] if c in live) for p in live}) if live else []
    return dict(prefixes=prefixes, graph=graph, live=live, cache=cache, outdeg=outdeg)


def cycle_through_entrance(res):
    """A live cycle through a live entrance pair (wall, c1): read cell by cell it is a spatially periodic full-line orbit.
    Breadth-first search inside the live set from the pair back to itself; returns the pairs in order, or None."""
    live, graph = res['live'], res['graph']
    for start in sorted(p for p in res['prefixes'] if p in live):
        par = {start: None}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in live:
                    continue
                if v == start:
                    path = [u]
                    while path[-1] != start:
                        path.append(par[path[-1]])
                    path = path[::-1]
                    k = len(res['prefixes'][start]) - 2          # prefixes are keyed by their last pair: rotate the
                    path = path[-k:] + path[:-k] if k else path  # cycle back so it starts at the wall pair
                    row = res['prefixes'][start]
                    assert [a for a, b in path[:len(row) - 1]] == row[:-1], 'cycle does not pass the entrance'
                    return path
                if v not in par:
                    par[v] = u
                    q.append(v)
    return None


def ring(path, P):
    profiles = [a for a, b in path]
    row = [bit(w, 0, P) for w in profiles]
    init = row[:]
    for t in range(1, P + 1):
        row = [TABLE[4 * row[(i - 1) % len(row)] + 2 * row[i] + row[(i + 1) % len(row)]] for i in range(len(row))]
        assert row == [bit(w, t, P) for w in profiles], t
    assert row == init
    return dict(spatial_period=len(init), hex=hex(sum(v << i for i, v in enumerate(init))),
                site0=''.join(str(bit(profiles[0], t, P)) for t in range(P)),
                site1=''.join(str(bit(profiles[1], t, P)) for t in range(P)))


def literal_sample(res, P, n, seed):
    rng = random.Random(seed)
    keys = sorted(res['cache'])
    pick = keys if len(keys) <= n else rng.sample(keys, n)
    return all(res['cache'][k] == literal_children(k[0], k[1], P) for k in pick), len(pick)


def report(name, P, wall, visible, entrance):
    res = search(P, wall, visible, entrance)
    ok, n = literal_sample(res, P, 400, 1)
    cyc = cycle_through_entrance(res) if res['live'] else None
    rc = None
    if cyc:
        nxt = cyc[1:] + cyc[:1]
        assert all(v[1] in literal_children(u[0], u[1], P) for u, v in zip(cyc, nxt))   # every cycle edge, literally
        rc = ring(cyc, P)
    out = dict(name=name, P=P, entrance_pairs=len(res['prefixes']), reachable_pairs=len(res['graph']),
               live_pairs=len(res['live']), live_outdegrees=res['outdeg'], literal_sample_ok=ok, literal_sampled=n,
               ring=rc)
    print(json.dumps(out), flush=True)
    return res, out


def main():
    # AL-C1: GC686 at P = 6 (white-even wall 010101 = 42; S visible 100; entrance sites 2..5 = 1101 after site 1's 1)
    _, c1 = report('C1 all-S P=6 (GC686)', 6, 42, (1, 0, 0), (1, 1, 0, 1))
    okc1 = (c1['reachable_pairs'] == 3714 and c1['live_pairs'] == 84 and c1['ring'] is not None
            and c1['ring']['spatial_period'] == 84 and int(c1['ring']['hex'], 16) == 0x688eb74a45efb082671ee)
    # the cycle found may start at another rotation; compare as a ring
    if not okc1 and c1['ring'] is not None and c1['live_pairs'] == 84 and c1['reachable_pairs'] == 3714:
        h, n = int(c1['ring']['hex'], 16), c1['ring']['spatial_period']
        okc1 = n == 84 and any(((0x688eb74a45efb082671ee >> k) | (0x688eb74a45efb082671ee << (84 - k))) & ((1 << 84) - 1) == h
                               for k in range(84))
    print('AL-C1', 'PASS' if okc1 else 'FAIL', flush=True)
    wall10 = sum(1 << t for t in range(1, 10, 2))
    L_vis = (1, 0, 0, 0, 0)
    resL, L = report('all-L P=10, entrance 111001', 10, wall10, L_vis, (1, 1, 0, 0, 1))
    _, Lb = report('all-L P=10, black-even control', 10, sum(1 << t for t in range(0, 10, 2)), L_vis, (1, 1, 0, 0, 1))
    resM, M = report('all-L P=10, marker 1110 only', 10, wall10, L_vis, (1, 1, 0))
    print('AL-C2', 'PASS' if all(x['literal_sample_ok'] for x in (c1, L, Lb, M)) else 'FAIL')
    print('AL-P1', 'HELD' if L['live_pairs'] > 0 else 'REFUTED')
    print('AL-P2', 'HELD' if L['ring'] is not None else 'REFUTED')
    print('AL-P3', 'HELD' if L['live_pairs'] > 0 and L['live_outdegrees'] == [1] else 'REFUTED')
    print('AL-P4', 'HELD' if Lb['live_pairs'] == 0 else 'REFUTED')
    if M['live_pairs']:
        # sites 5 and 6 at time 0 of every live marker entrance: continue each live entrance two columns in the live set
        s56 = set()
        for pair, row in resM['prefixes'].items():
            if pair not in resM['live']:
                continue
            for c5 in resM['graph'][pair]:
                if c5 not in resM['live']:
                    continue
                for c6 in resM['graph'][c5]:
                    if c6 in resM['live']:
                        s56.add((bit(c5[1], 0, 10), bit(c6[1], 0, 10)))
        print('AL-U', 'HELD' if s56 == {(0, 1)} else 'REFUTED', sorted(s56))
    else:
        print('AL-U UNTESTED (no live pair with the marker alone)')
    print('COMPLETE')


if __name__ == '__main__':
    main()
