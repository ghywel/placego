#!/usr/bin/env python3
"""G56 preregistered PH1-PH3. NOT RUN at publication. No data files."""
from rule30_gpt_ring_quotient import rotate, rotations, vector, cycles


def theta(x, p):
    weight = x.bit_count()
    assert 0 < weight < p
    moment = sum(i for i in range(p) if (x >> i) & 1) % p
    return moment * pow(weight, -1, p) % p


def normalize(x, p):
    if x in (0, (1 << p) - 1):
        return x
    phase = theta(x, p)
    for _ in range((-phase) % p):
        x = rotate(x, p)
    return x


def audit(p):
    states = range(1 << p)
    lex_to_phase, checked = {}, 0
    for x in range(1, (1 << p) - 1):
        assert theta(rotate(x, p), p) == (theta(x, p) + 1) % p
        rep = normalize(x, p)
        assert theta(rep, p) == 0
        lex = min(rotations(x, p))
        if lex in lex_to_phase:
            assert lex_to_phase[lex] == rep
        else:
            lex_to_phase[lex] = rep
        checked += 1
    assert len(set(lex_to_phase.values())) == len(lex_to_phase)
    reps = sorted({normalize(x, p) for x in states})
    quotient = cycles(reps, lambda x: normalize(vector(x, p), p))
    phase_cycles = []
    for cycle in quotient:
        if cycle == [0]:
            continue
        total = sum(theta(vector(x, p), p) for x in cycle) % p
        x = cycle[0]
        for _ in cycle:
            x = vector(x, p)
        direct = rotations(cycle[0], p).index(x)
        assert total == direct
        phase_cycles.append((len(cycle), total))
    print('PH1/PH2 PASS:', p, 'phase cycles=', sorted(phase_cycles))
    return checked


if __name__ == '__main__':
    count = sum(audit(p) for p in (3, 5, 7, 11, 13))
    assert len(set(rotations(3, 4))) == 4 and (3).bit_count() == 2
    try:
        pow(2, -1, 4)
    except ValueError:
        pass
    else:
        raise AssertionError('Composite-ring guard failed')
    print('PH3 PASS: free four-cell orbit has noninvertible weight2.')
    print('Nonconstant state checks:', count)
    print('Coordinate control only; nonzero phase-sum mechanism remains open.')
