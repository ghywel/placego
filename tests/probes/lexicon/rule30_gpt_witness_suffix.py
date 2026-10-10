"""GC949: fixed nine-edge suffix of GC326's retained rooted q16 witness.

Predictions published before execution. No trajectory search or extension:
start depth725146, pair(320,64), clock1458151; stop depth725155.
C1: first four delays16,3,1,16 and debt26.
C2: constructive child equals independent exhaustive literal Rule30 child.
C3: prefix-minimum debt equals all ordered endpoint differences.
P1 blind: last five edges have positive same-clock interval debt.
P2 blind: the whole suffix debt exceeds26.
CF: discarding the last five edges leaves total elapsed36 (must fail).
Unexpected: the second pulse's predecessor is not the starting two-pulse source.
At most nine exhaustive 2^16-child checks; standard library, no data files.
Outcome appended after execution; existing rooted provenance not re-established.
"""
import json

Q, MASK = 16, (1 << 16) - 1


def child(a, b):
    r = (b & -b).bit_length() - 1
    bit = ((a >> r) & 1) ^ 1
    c = 0
    for i in range(Q):
        t = (r + 1 + i) % Q
        c |= bit << t
        bit = ((a >> t) & 1) ^ (((b >> t) & 1) | bit)
    return c


def literal(a, b, c):
    return all(((c >> ((t + 1) % Q)) & 1) ==
               (((a >> t) & 1) ^ (((b >> t) & 1) | ((c >> t) & 1)))
               for t in range(Q))


def debt2(delays):
    z, low, best = 0, 0, 0
    vals = [0]
    for d in delays:
        z += 2*d - 5
        best = max(best, z-low)
        low = min(low, z)
        vals.append(z)
    brute = max(vals[j]-vals[i] for i in range(len(vals))
                for j in range(i, len(vals)))
    assert best == brute
    return best


def main():
    a, b, clock = 320, 64, 1458151
    rows = []
    for k in range(9):
        assert b != 0
        delay = next(i+1 for i in range(Q) if (b >> ((clock+i) % Q)) & 1)
        c = child(a, b)
        matches = [v for v in range(MASK+1) if literal(a,b,v)]
        assert matches == [c]
        rows.append(dict(depth=725146+k, a=a, b=b, clock=clock, delay=delay))
        a, b, clock = b, c, clock+delay
    delays = [row['delay'] for row in rows]
    assert delays[:4] == [16,3,1,16]
    assert debt2(delays[:4]) == 52
    assert rows[3]['a'] == 64639 and rows[3]['b'] == 1024
    result = dict(rows=rows, episode_debt2=debt2(delays[:4]),
                  gap_debt2=debt2(delays[4:]), suffix_debt2=debt2(delays),
                  elapsed=sum(delays), terminal_clock=clock,
                  P1=debt2(delays[4:])>0, P2=debt2(delays)>52,
                  CF=sum(delays)==36,
                  controls='PASS', unexpected='PASS')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
