#!/usr/bin/env python3
"""GC401: characterize GC400's full reached cut with Boolean correlations.
Before run: P1 at most four reached-family prime clauses suffice to exclude all
cut rows violating the final implication (confidence0.5). Counterfactual: four
empirical features can replace their omitted correlations (GC400 refuted this).
Controls: all prime clauses describe exactly the32 reached rows among512;
core excludes every bad future row; removing each core clause permits one.
Unexpected check: core may safely admit unreachable cut rows; keep reachability
and sufficiency separate. OUTCOME: P1 REFUTED. Seven prime clauses suffice; all164220 covers of
at most four nonempty prime clauses fail. Core admits60 rows (28 unreachable
but safe), with a deletion witness for every clause. Full55-clause model is
exactly the32 reached rows. No minimum claim about the seven-clause core.
Finite certificate, not a short symbolic anchor proof.
"""
import itertools
import json


def reached():
    result = set()
    for free in range(4096):
        row = (14 | (free & 1) | ((free >> 1) << 6)) << 1
        for t in range(8):
            row = (row & ~1) | (t % 2)
            row = ((row << 1) ^ (row | (row >> 1))) & ((1 << (17-t))-1)
        result.add(row >> 1)
    return result


def future(raw):
    row = [0] + [(raw >> i) & 1 for i in range(9)]
    for dt in range(4):
        row = [(9+dt) % 2] + [row[j-1] ^ (row[j] | row[j+1])
                              for j in range(1, len(row)-1)]
    return row[5]


def main():
    r = reached()
    assert len(r) == 32
    primes = []  # Clause forbids the partial assignment (mask,value).
    for pattern in itertools.product((-1, 0, 1), repeat=9):
        mask = sum(1 << i for i, v in enumerate(pattern) if v != -1)
        value = sum(1 << i for i, v in enumerate(pattern) if v == 1)
        if any(x & mask == value for x in r):
            continue
        if all(any(x & (mask & ~(1 << i)) == value & ~(1 << i) for x in r)
               for i in range(9) if mask & (1 << i)):
            primes.append((mask, value))
    models = {x for x in range(512) if all(x & m != v for m, v in primes)}
    assert models == r
    bad = {x for x in range(512) if (x >> 5) & 1 and future(x) == 0}
    assert not r & bad
    uncovered = set(bad)
    core = []
    remaining = list(primes)
    while uncovered:
        c = max(remaining, key=lambda p: (sum(x & p[0] == p[1] for x in uncovered), -p[0].bit_count()))
        covered = {x for x in uncovered if x & c[0] == c[1]}
        assert covered
        uncovered -= covered
        core.append(c)
        remaining.remove(c)
    for c in list(core):
        trial = [p for p in core if p != c]
        if all(any(x & m == v for m, v in trial) for x in bad):
            core = trial
    admitted = {x for x in range(512) if all(x & m != v for m, v in core)}
    assert r <= admitted and not admitted & bad
    bad_order = sorted(bad)
    covers = [(c, sum(1 << i for i, x in enumerate(bad_order) if x & c[0] == c[1])) for c in primes]
    covers = [(c, cover) for c, cover in covers if cover]
    all_bad = (1 << len(bad_order))-1
    examined = 0
    small = None
    for size in range(1, 5):
        for combo in itertools.combinations(covers, size):
            examined += 1
            union = 0
            for _, cover in combo:
                union |= cover
            if union == all_bad:
                small = [c for c, _ in combo]
                break
        if small is not None:
            break
    witnesses = [next(x for x in bad if all(x & m != v for m, v in core if (m,v)!=c)) for c in core]
    print(json.dumps({'reached_rows': len(r), 'prime_clause_count': len(primes),
                      'bad_unrestricted_rows': len(bad), 'core_clause_count': len(core),
                      'core_forbidden_patterns': [[[i+1, (v >> i) & 1] for i in range(9) if m & (1 << i)]
                                                  for m, v in core],
                      'core_admitted_rows': len(admitted),
                      'unreachable_but_safe_rows': len(admitted-r),
                      'deletion_witnesses': len(witnesses),
                      'covers_up_to_four_examined': examined,
                      'cover_at_most_four_exists': small is not None}, indent=2))


if __name__ == '__main__':
    main()
