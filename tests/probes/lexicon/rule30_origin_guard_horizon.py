"""GC1172: discharge a first-bit cut origin after K-1 common bits.

This checks a root-filter simplification for GC1159/1170, not records.
Record searched: origin/coalesc ->16 hits13files; residual/43 ->20 hits
12files; first/forget/cut ->4 hits4files. GC1158/59/1170 read.
Predictions BEFORE execution: surviving origins share a cut residual
after K-1 common bits; a prefix guard plus ordinary internal cuts equals
existential original-bit acceptance. Independent direct substring test.
CF: restarting a fresh residual after both origins died is sound; must
fail for the real B word100101 under the S catalog. Unexpected: a fresh
long all-S suffix passes although neither origin of that prefix survives.
No solver, real membership, record census, inverse-depth scan or new cut.
OUTCOME 2026-10-13, Intel CPU: 2047 direct/guard/residual checks PASS;
K44 dead-origin restart rejected, while the fresh all-S suffix passes.
"""
from itertools import product
from rule30_phase_prepend_guard import cuts, forbidden
from rule30_birth_parent_language import ParentMachine


def origin_paths(common, fs):
    machine = ParentMachine([fs, fs], 0)
    states = {machine.step('', b) for b in '01'} - {None}
    for b in common:
        states = {machine.step(s, b) for s in states} - {None}
    return states


def guarded(common, fs):
    k = max(map(len, fs))
    prefix = common[:k-1]
    return (any(not forbidden(b+prefix, fs) for b in '01')
            and not forbidden(common, fs))


def main():
    fs = ('11', '00000', '101001')
    checks = 0
    for n in range(11):
        for bits in product('01', repeat=n):
            common = ''.join(bits)
            expected = any(not forbidden(b+common, fs) for b in '01')
            states = origin_paths(common, fs)
            assert bool(states) == expected == guarded(common, fs)
            if n >= max(map(len, fs))-1:
                assert len(states) <= 1
            checks += 1
    actual = cuts()[0]
    tail = '100'*16  # known all-S ring language; only finite cuts checked
    common = '100101'+tail
    assert max(map(len, actual)) == 44
    assert not forbidden(tail, actual)
    assert not origin_paths(common, actual)
    assert not guarded(common, actual)
    assert all(forbidden(b+common, actual) for b in '01')
    print('direct/guard/residual controls', checks, 'PASS')
    print('K44 dead-origin reset countercontrol PASS; fresh suffix passes')


if __name__ == '__main__':
    main()
