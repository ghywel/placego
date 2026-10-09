"""GC657 bounded proof audit, predictions recorded in CLOUD-LOCAL first.

q=4..6 only; scalar compatibility and phases, no root ancestry or census.
q=5 is the identified unexpected non-dyadic control. No external data.
"""
import json


def audit(q):
    mask = (1 << q)-1
    bit = lambda w, t: (w >> (t % q)) & 1
    wait = lambda w, t: next(k+1 for k in range(q) if bit(w, t+k))
    totals = dict(q=q, pairs=0, arrival_checks=0, mismatch_checks=0,
                  zero_source_covered_incoming=0)
    for b in range(1, mask+1):
        for c in range(mask+1):
            a = sum((bit(c, t+1) ^ (bit(b, t) | bit(c, t))) << t
                    for t in range(q))
            totals['pairs'] += 1
            # Enumerate actual forward resets from all gated parent phases.
            incoming = [0]*q
            for t in range(q):
                gate = bit(a, t-1) if a else bit(b, t) ^ bit(b, t-1)
                if gate:
                    incoming[(t+wait(b, t)) % q] += 1
            for s in range(q):
                if not bit(b, s-1):
                    assert incoming[s] == 0
                    continue
                gap = next(k for k in range(1, q+1) if bit(b, s-1-k))
                u = s-gap
                k = 1-bit(c, u) + sum(bit(c, t+1) ^ bit(c, t)
                                      for t in range(u, s-1))
                covered = all(bit(c, t) for t in range(u, s))
                if a:
                    assert incoming[s] == k
                    assert (k == 0) == covered
                    totals['arrival_checks'] += 1
                elif covered and incoming[s]:
                    totals['zero_source_covered_incoming'] += 1
            if not c:
                continue
            # Independently integrate both possible initial bits and close period.
            outputs = []
            for seed in (0, 1):
                values = [seed]
                for t in range(q):
                    values.append(bit(b, t) ^ (bit(c, t) | values[-1]))
                if values[-1] == seed:
                    outputs.append(sum(v << t for t, v in enumerate(values[:-1])))
            assert len(outputs) == 1
            d = outputs[0]
            if not d:
                assert b == c
                continue
            for t in range(q):
                s = t+wait(b, t)
                s += wait(c, s)
                if not bit(b, s-1):
                    expected = 1
                else:
                    r = next(k for k in range(q) if bit(b ^ c, s+k))
                    expected = r+2
                assert wait(d, s) == expected
                totals['mismatch_checks'] += 1
    assert totals['zero_source_covered_incoming'] > 0
    # Exact identified exception: pulse B, constant C, predecessor A=0.
    assert all(bit(mask, t+1) == (bit(1, t) | bit(mask, t)) for t in range(q))
    assert (bit(1, 1) ^ bit(1, 0)) == 1 and wait(1, 1) == q
    return totals


if __name__ == '__main__':
    print(json.dumps([audit(q) for q in (4, 5, 6)], indent=2))
