"""Balanced latch prefix audit, preregistered 2026-10-06.

BL0 must: row-wise prefix construction matches column-wise inverse for all
  visible words on balanced a2..10, not just latched words.
BL1 blind: for balanced a4..128 every monotone word's known2a-1-cell prefix
  has a black cell at depth>=a, extending G18's finite SP2 control.
BL2 blind: at some a4..10, arbitrary nonmonotone white words permit a smaller
  last-black depth than monotone words, identifying a genuine latch effect.
BL3 unexpected blind: a minimizing latch position is always an endpoint r0 or a.
CF must fail: the first latch position determines the entire row (reuse the
  explicit valid a4,b4 next-block witness; first difference is depth9).
REFUTED-BY: a comparison mismatch invalidates BL0. Retain first failures for
  each blind prediction, including all actual minimizing positions and depths.
OUTCOME first run: exit0. BL0 all2044 comparisons pass; BL1 HELD finitely
for a4..128; BL2 HELD at a4,5,7,8,9,10 (arbitrary/monotone minima respectively
5/6,4/7,7/10,9/14,9/15,11/17). Unexpected BL3 REFUTED first at a5:
minimum last-black7 only at r3, neither endpoint. CF rejects complete-row claim.

ADDENDUM before second run:
BL4 must: for a=b5, every one of64 finite left seeds with support depth<=6
  fails the first-period necessary conditions (monotone visible bits and fixed
  black-time column-1). The known prefix for latch r3 supplies a positive
  left-only control at support7. This is not a whole-right-half existence test.
OUTCOME second run: exit0. BL4 all64 width-six seeds rejected. Positive
left-only seed{-7,-4} has support7 and pi000100000 through nine times;
latch r3. Arbitrary minimum witness11001 has prefix100100000 and last-black4. Prefix support only, no record or asymptotic LR measurement.
"""

from itertools import product
from rule30_gpt_slow_switch import prefix
from rule30_gpt_condrey_holes import forced_columns


def last_black(row):
    return max((j for j, bit in enumerate(row, 1) if bit), default=0)


def main():
    checks = 0
    arbitrary = {}
    for a in range(2, 11):
        tau = [int(t % (2*a) >= a) for t in range(6*a+5)]
        depths = []
        for visible in product((0,1), repeat=a):
            sigma = list(visible) + [0]*(len(tau)-a)
            row = [col[0] for col in forced_columns(tau, sigma, 2*a-1)]
            assert row == prefix(a, a, visible), (a,visible)
            depths.append(last_black(row))
            checks += 1
        arbitrary[a] = min(depths)
    print('BL0 PASS:', checks, 'complete prefix comparisons')
    failures = []
    endpoint_failures = []
    latch_effect = []
    for a in range(4, 129):
        values = [last_black(prefix(a,a,[0]*r+[1]*(a-r))) for r in range(a+1)]
        minimum = min(values)
        positions = [r for r, x in enumerate(values) if x == minimum]
        if minimum < a:
            failures.append((a, minimum, positions))
        if 0 not in positions and a not in positions:
            endpoint_failures.append((a, minimum, positions))
        if a <= 10 and arbitrary[a] < minimum:
            latch_effect.append((a, arbitrary[a], minimum))
        print('BALANCED', a, 'minlast', minimum, 'positions', positions,
              'arbitrarymin', arbitrary.get(a))
    print('BL1', 'REFUTED' if failures else 'HELD', failures)
    print('BL2', 'HELD' if latch_effect else 'REFUTED', latch_effect)
    print('BL3', 'REFUTED' if endpoint_failures else 'HELD', endpoint_failures)
    a = 4
    tau = [int(t % 8 >= 4) for t in range(40)]
    sigma0 = [0]*40
    sigma1 = sigma0[:]
    sigma1[8:13] = [1]*5
    rows = [[col[0] for col in forced_columns(tau, sigma, 16)]
            for sigma in (sigma0,sigma1)]
    assert rows[0][:7] == rows[1][:7]
    assert next(j for j,(x,y) in enumerate(zip(*rows),1) if x != y) == 9
    print('CF REJECTED: same first latch, first row difference at depth9')
    print('ALL CONTROLS PASS')


def finite_left_trace(row, wall, steps):
    row = set(row)
    result = []
    for t in range(steps):
        result.append(int(-1 in row))
        leftmost = min(row, default=-1)-1
        def bit(j):
            return wall[t] if j == 0 else int(j in row)
        row = {j for j in range(leftmost,0)
               if bit(j-1) ^ (bit(j) | bit(j+1))}
    return result


def forward_check():
    wall = [0]*5+[1]*5
    def compatible(pi):
        visible = pi[:4]+[1-pi[4]]
        return all(visible[j] <= visible[j+1] for j in range(4)) and pi[5:9] == [0]*4
    survivors = []
    for seed in range(64):
        row = {-j-1 for j in range(6) if (seed >> j) & 1}
        pi = finite_left_trace(row,wall,9)
        if compatible(pi):
            survivors.append(seed)
    assert not survivors, survivors
    finite_prefix = prefix(5,5,[0,0,0,1,1])
    row = {-j for j,x in enumerate(finite_prefix,1) if x}
    assert max(-j for j in row) == 7
    pi = finite_left_trace(row,wall,9)
    assert compatible(pi), pi
    assert pi[:4]+[1-pi[4]] == [0,0,0,1,1]
    print('BL4 PASS: all64 width-six seeds rejected; support-seven left-only control',
          sorted(row), 'pi', pi)
    print('LATCH PREFIXES a5', [(r,prefix(5,5,[0]*r+[1]*(5-r))) for r in range(6)])
    best = [(w,prefix(5,5,w)) for w in product((0,1),repeat=5)
            if last_black(prefix(5,5,w)) == 4]
    print('ARBITRARY a5 minimum witnesses',best)


if __name__ == '__main__':
    main()
    forward_check()
