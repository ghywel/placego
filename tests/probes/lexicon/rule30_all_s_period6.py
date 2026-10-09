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


def main():
    print(json.dumps(dict(period=P, white_even=search(42),
                          black_even_control=search(21)), sort_keys=True))


if __name__ == '__main__':
    main()
