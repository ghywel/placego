"""GC686: one uniform temporal-period-six all-S candidate, not a period sweep."""
import json
from collections import deque

P = 6


def bit(w, t):
    return (w >> (t % P)) & 1


def children(left, centre):
    fixed, free = 0, []
    for t in range(P):
        if bit(centre, t):
            if bit(centre, t + 1) != 1 ^ bit(left, t):
                return []
            free.append(t)
        else:
            fixed |= (bit(centre, t + 1) ^ bit(left, t)) << t
    out = [fixed | sum(((choice >> j) & 1) << t for j, t in enumerate(free))
           for choice in range(1 << len(free))]
    return sorted(out)


def literal_children(left, centre):
    table = (0, 1, 1, 1, 1, 0, 0, 0)
    return [r for r in range(64) if all(
        bit(centre, t + 1) == table[4 * bit(left, t) + 2 * bit(centre, t) + bit(r, t)]
        for t in range(P))]


def search(wall):
    cache = {}
    def next_words(a, b):
        pair = (a, b)
        if pair not in cache:
            cache[pair] = children(a, b)
            assert cache[pair] == literal_children(a, b)
        return cache[pair]
    initial = [c for c in range(64) if [bit(c, t) for t in (0, 2, 4)] == [1, 0, 0]]
    prefixes = {(wall, c): [wall, c] for c in initial}
    # Actual recurrent marker and short-loop entrance: sites1..5 =11101.
    for required in (1, 1, 0, 1):
        extended = {}
        for (a, b), row in prefixes.items():
            for c in next_words(a, b):
                if bit(c, 0) == required:
                    extended.setdefault((b, c), row + [c])
        prefixes = extended
    graph, parent = {}, {pair: None for pair in prefixes}
    queue = deque(prefixes)
    while queue:
        pair = queue.popleft()
        graph[pair] = [(pair[1], c) for c in next_words(*pair)]
        for child in graph[pair]:
            if child not in parent:
                parent[child] = pair
                queue.append(child)
    reverse = {pair: [] for pair in graph}
    degree = {pair: len(edges) for pair, edges in graph.items()}
    for pair, edges in graph.items():
        for child in edges:
            reverse[child].append(pair)
    leaves = deque(pair for pair, d in degree.items() if d == 0)
    removed = set()
    while leaves:
        pair = leaves.popleft()
        if pair in removed:
            continue
        removed.add(pair)
        for previous in reverse[pair]:
            degree[previous] -= 1
            if degree[previous] == 0:
                leaves.append(previous)
    live = set(graph) - removed
    witness = None
    if live:
        start = next(pair for pair in prefixes if pair in live)
        seen, path, pair = {}, [], start
        while pair not in seen:
            seen[pair] = len(path)
            path.append(pair)
            pair = min(child for child in graph[pair] if child in live)
        witness = dict(initial_column_profiles=prefixes[start],
                       pair_path=path, cycle_start_pair_index=seen[pair])
    return dict(wall_profile=wall, entrance_pairs=len(prefixes),
                reachable_pairs=len(graph), live_pairs=len(live),
                independent_pair_controls=len(cache), witness=witness)


def ring_certificate(result):
    witness = result['witness']
    assert witness is not None and witness['cycle_start_pair_index'] == 0
    pairs = witness['pair_path']
    profiles = [a for a, b in pairs]
    assert all(b == profiles[(i + 1) % len(profiles)]
               for i, (a, b) in enumerate(pairs))
    prefix = witness['initial_column_profiles']
    start = next(i for i in range(len(profiles))
                 if [profiles[(i + k) % len(profiles)] for k in range(len(prefix))] == prefix)
    profiles = profiles[start:] + profiles[:start]
    row = [bit(w, 0) for w in profiles]
    initial = row[:]
    table = (0, 1, 1, 1, 1, 0, 0, 0)
    for t in range(1, P + 1):
        row = [table[4 * row[(i - 1) % len(row)] + 2 * row[i]
                     + row[(i + 1) % len(row)]] for i in range(len(row))]
        assert row == [bit(w, t) for w in profiles]
    assert row == initial
    assert [bit(profiles[0], t) for t in range(P)] == [0, 1, 0, 1, 0, 1]
    assert [bit(profiles[1], t) for t in (0, 2, 4)] == [1, 0, 0]
    assert initial[1:6] == [1, 1, 1, 0, 1]
    return dict(spatial_period=len(row), initial_row_hex=hex(sum(v << i for i, v in enumerate(initial))),
                site0_time_word=''.join(str(bit(profiles[0], t)) for t in range(P)),
                site1_time_word=''.join(str(bit(profiles[1], t)) for t in range(P)),
                global_cell_checks=P * len(row))


def main():
    white = search(42)
    print(json.dumps(dict(period=P, white_even=white,
                          black_even_control=search(21),
                          global_ring_certificate=ring_certificate(white)), sort_keys=True))


if __name__ == '__main__':
    main()
