"""Target the six unresolved width-11 windows in Local's L1521 negative control.

Refine the bottom of each window by three cells once. Explore only until
a proven B11 window, an invalid top step, or an already seen state. No census.
"""
import hashlib
import json
import os
from pathlib import Path

from right_ray_memory import guard

PATTERNS = ("##...#...##", "##...#.#.##", ".#...##.###", "..#..##.###",
            "#.#..##.###", "##.#.##.###")
B11 = set(map(int, Path("tests/probes/twopair_B11.txt").read_text().split()))


def encode(word):
    return sum((ch == "#") << i for i, ch in enumerate(word))


def predecessors(state, width):
    # Above the equal pair the input alternates. The predecessor alternates
    # from original top+4 onward by back_rain_tail. Only its top+3 pair is tested.
    bits = [(state >> i) & 1 for i in range(width)]
    assert bits[-1] == bits[-2]
    for _ in range(5):
        bits.append(1 - bits[-1])
    for lower in range(4):
        a, b = lower & 1, lower >> 1
        back = []
        for bit in bits:
            z = bit ^ (a | b)
            back.append(z)
            assert bit == (z ^ (a | b))
            b, a = a, z
        if back[width + 1] != back[width + 2]:
            yield lower, None
            continue
        assert back[width+3] != back[width+2] and back[width+4] != back[width+3]
        yield lower, sum(bit << i for i, bit in enumerate(back[3:width+3]))


def explore(initial, width):
    shift = width - 11
    frontier = list(initial)
    seen = set()
    edges = {}
    escapes = []
    while frontier:
        state = frontier.pop()
        if state in seen or state >> shift in B11:
            continue
        seen.add(state)
        if len(seen) > 2048:
            raise RuntimeError("prespecified state cap")
        nxt = []
        for lower, child in predecessors(state, width):
            if child is None:
                escapes.append((state, lower))
            elif child >> shift not in B11:
                nxt.append(child)
                frontier.append(child)
        edges[state] = nxt
    # Peel successors backwards to give a finite all-paths entry bound, if one exists.
    rank = {}
    pending = set(edges) - {s for s, _ in escapes}
    while True:
        ready = {s for s in pending if all(c in rank for c in edges[s])}
        if not ready:
            break
        for s in ready:
            rank[s] = 1 + max((rank[c] for c in edges[s]), default=0)
        pending -= ready
    return {"seen": sorted(seen), "bad_steps": escapes, "unranked": len(seen)-len(rank),
            "max_entry_ticks": max(rank.values(), default=0) if len(rank)==len(seen) else None}


def main():
    guard(True)
    assert len(B11)==18 and all(encode(s) not in B11 for s in PATTERNS)
    assert all(z in B11 for s in B11 for _,z in predecessors(s, 11))
    # A white top cannot be a predecessor's +3 black top in this example.
    assert any(z is None for _,z in predecessors(0, 11))
    result = {}
    for s in PATTERNS:
        result[s] = explore([(encode(s) << 3) | below for below in range(8)],14)
        guard()
    data = (json.dumps(result, sort_keys=True, indent=2)+"\n").encode()
    (Path(os.environ["CAPPED_OUT"])/"six.json").write_bytes(data)
    for s,v in result.items():
        print(s, "seen",len(v["seen"]), "bad steps",len(v["bad_steps"]),
              "unranked",v["unranked"], "entry ticks",v["max_entry_ticks"])
    print(hashlib.sha256(data).hexdigest(), guard(True))


if __name__ == "__main__":
    main()
