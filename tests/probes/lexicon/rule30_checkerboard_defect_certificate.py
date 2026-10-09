#!/usr/bin/env python3
"""Exact radius-nine checkerboard-defect certificate; GC677 supplies closure."""
import json

RADIUS = 9
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def evolve(mask, literal=False):
    # Two extra reference cells determine two updates of depths 1..RADIUS.
    row = [1] + [(i % 2) ^ ((mask >> (i - 1)) & 1 if i <= RADIUS else 0)
                 for i in range(1, RADIUS + 3)]
    for wall in (0, 1):
        row = [wall] + [TABLE[4 * row[i + 1] + 2 * row[i] + row[i - 1]]
                       if literal else row[i + 1] ^ (row[i] | row[i - 1])
                       for i in range(1, len(row) - 1)]
    return sum((row[i] ^ (i % 2)) << (i - 1) for i in range(1, RADIUS + 1))


def radius_control(mask):
    # More exterior cells explicitly check the invariant beyond the retained map.
    row = [1] + [(i % 2) ^ ((mask >> (i - 1)) & 1 if i <= RADIUS else 0)
                 for i in range(1, RADIUS + 7)]
    radii = []
    for wall in (1, 0, 1):
        if radii:
            row = [wall] + [row[i + 1] ^ (row[i] | row[i - 1])
                           for i in range(1, len(row) - 1)]
        radii.append(max([0] + [i for i in range(1, len(row)) if row[i] != i % 2]))
    assert radii[1] <= radii[0] + 1
    assert radii[2] <= radii[0]
    return radii


def main():
    transition = [evolve(mask) for mask in range(1 << RADIUS)]
    for mask in range(1 << RADIUS):
        assert transition[mask] == evolve(mask, literal=True)
        radius_control(mask)
    assert radius_control(4) == [3, 4, 3]
    assert transition[4] & 1  # Noncontraction does not imply wall compatibility.
    survivors, failures, cycles = [], {}, set()
    for initial in range(1 << RADIUS):
        seen, path, state = {}, [], initial
        while state not in seen and not state & 1:
            seen[state] = len(path)
            path.append(state)
            state = transition[state]
        if state & 1:
            failures[initial] = len(path)  # Black-time index; physical time is twice this.
        else:
            survivors.append(initial)
            cycle = path[seen[state]:]
            canonical = min(tuple(cycle[j:] + cycle[:j]) for j in range(len(cycle)))
            cycles.add(canonical)
    print(json.dumps({'radius': RADIUS, 'states': len(transition),
                      'survivors': survivors, 'survivor_cycles': sorted(cycles),
                      'failures': len(failures),
                      'latest_failure_black_index': max(failures.values()),
                      'latest_failure_masks': [m for m, t in failures.items()
                                               if t == max(failures.values())],
                      'independent_update_comparisons': len(transition),
                      'radius_closure_controls': len(transition),
                      'noncontraction_control': radius_control(4)}, sort_keys=True))


if __name__ == '__main__':
    main()
