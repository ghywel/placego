#!/usr/bin/env python3
"""B23: seven fixed m=28 receiving-chain constructions; MI056, 2026-10-16.

Preregistered in 9fb25568 before execution. No enumeration or solver.
P1: k=2..8, roots (1,3) except k=5 uses (1,7), have eight distinct
    complementary pairs supporting two length-three receiving chains.
P2: literal swaps preserve ownership and produce targets
    (56+6*k)^2, (112-2*k)^6, with cardinalities 2,2,4,4,4,4,4,4.
P3: closed-form final bins independently match the swap simulation;
    a separate multiset checker certifies coverage and target sums.
Counterfactuals: naive roots (1,3), k=5 repeat a pair and are rejected;
    a corrupted final witness with a duplicated token is rejected.
Unexpected: k=9 asks for two 2-element sums 110, above 55+53=108;
    this kills only this cardinality choice, not the target tuple.
Stop: these seven schedules and controls. Intended CPU below one second.
Record searched and prior-art boundary: MI056. Hand derivation, not novelty.
Raw JSON output belongs outside git.

OUTCOME (2026-10-16, GPT Intel CPU): P1-P3 pass on all seven schedules;
naive k=5 roots and all seven corrupted witnesses rejected; k=9 boundary
confirmed. Measured process CPU 0.000825 s. Raw output outside git:
math-instinct-b23-receiving-chains.json. No arbitrary-E28 conclusion or
independent carrying read. The seven literal partitions are COMPUTED;
the hand argument is PROOF-SKETCH pending a second reader.
Raw SHA256: dac93a1d148a505baa6ed860ef374922e67c724cc4fdc6b47cce86b98e8895f5.
"""

from collections import Counter
import json
import time


def checked_schedule(k, roots):
    chains = [[a + 2 * k * j for j in range(4)] for a in roots]
    tokens = [v for chain in chains for v in chain]
    if any(v % 2 != 1 or not 1 <= v <= 55 for v in tokens):
        raise ValueError("chain token outside the odd pool")
    labels = [min(v, 56 - v) for v in tokens]
    if len(set(labels)) != 8:
        raise ValueError("complementary pair reused")
    pairs = {x: {x, 56 - x} for x in range(1, 28, 2)}
    fillers = [x for x in pairs if x not in labels]
    assert len(fillers) == 6
    bins = [set(pairs[a]) for a in roots]
    direct = [{a + 6 * k, 56 - a} for a in roots]
    moves = []
    for r, chain in enumerate(chains):
        for j in range(1, 4):
            filler = pairs[fillers[3 * r + j - 1]]
            donor = len(bins)
            bins.append(pairs[min(chain[j], 56 - chain[j])] | filler)
            direct.append({chain[j - 1], 56 - chain[j]} | filler)
            moves.append((r, donor, chain[j - 1], chain[j]))
    initial = Counter(v for b in bins for v in b)
    assert initial == Counter(range(1, 56, 2))
    for receiver, donor, current, next_token in moves:
        assert current in bins[receiver] and next_token in bins[donor]
        bins[receiver].remove(current)
        bins[donor].remove(next_token)
        bins[receiver].add(next_token)
        bins[donor].add(current)
    assert bins == direct
    return bins, chains, labels


def certificate_ok(bins, targets):
    # Does not use the chain, pair allocation or transfer differences.
    flat = [v for b in bins for v in b]
    return (len(bins) == 8
            and Counter(flat) == Counter(2 * j + 1 for j in range(28))
            and sorted(map(sum, bins)) == sorted(targets)
            and sorted(map(len, bins)) == [2, 2, 4, 4, 4, 4, 4, 4])


def main():
    start = time.process_time()
    results = []
    for k in range(2, 9):
        roots = (1, 7) if k == 5 else (1, 3)
        bins, chains, labels = checked_schedule(k, roots)
        targets = [56 + 6 * k] * 2 + [112 - 2 * k] * 6
        assert sum(targets) == 28 ** 2
        assert min(targets) >= 68 and max(targets) <= 122
        assert certificate_ok(bins, targets)
        bad = [list(b) for b in bins]
        bad[0][0] = bad[1][0]
        assert not certificate_ok(bad, targets)
        results.append(dict(k=k, roots=roots, chains=chains, pair_labels=labels,
                            bins=[sorted(b) for b in bins], targets=targets))
    try:
        checked_schedule(5, (1, 3))
    except ValueError as exc:
        assert str(exc) == "complementary pair reused"
    else:
        raise AssertionError("bad roots accepted")
    assert 56 + 6 * 9 == 110 > 55 + 53 == 108
    print(json.dumps(dict(results=results, naive_k5="REJECTED",
                          corrupted_witnesses="7 REJECTED", k9="2-element cap 108 < 110",
                          cpu_seconds=time.process_time() - start), indent=2))


if __name__ == "__main__":
    main()
