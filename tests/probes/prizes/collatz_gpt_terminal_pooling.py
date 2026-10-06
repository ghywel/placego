"""G90 TC1: predictions published before execution.
MUST HOLD: direct admitted trajectories have classes 21/22 at time 33,
22/22 at time 34, and terminal 21632881628. Width is 34.
MUST HOLD: enumerated fair continuations and exact demand weights give
literal changes 1/2 and 0, summing to 1/2.
COUNTERFACTUAL MUST FAIL: equal terminals imply zero weighted pair error.
UNEXPECTED CHECK: an even last step has zero demand weight here; it
does not cancel the odd last step's positive demand weight.
REFUTED-BY: a trajectory, admission, width, rational-weight or total mismatch.
No population enumeration or asymptotic inference. NOT RUN.
OUTCOME TC1 PASS (2026-10-06, GPT Intel Python, under one second): two
admitted trajectories; classes 21/22 to 22/22, common terminal verified.
Literal and demand changes agree: 1/2 and 0, pair total 1/2.
Terminal-pooling cancellation counterfactual REFUTED; no control failed.
Predictions and script published at 23c22c2 before the run.
"""
from fractions import Fraction


def trajectory(n):
    counts, states, bits = [0], [n], []
    for step in range(1, 35):
        bit = n % 2
        bits.append(bit)
        counts.append(counts[-1] + bit)
        assert 3 ** counts[-1] >= 2 ** step, 'admission'
        # Direct arithmetic, independent of collision-tree machinery.
        n = (3 * n + 1) // 2 if bit else n // 2
        states.append(n)
    return counts, states, bits


def main():
    starts = (11843133435, 11843133439)
    assert all(n.bit_length() == 34 for n in starts)
    traces = [trajectory(n) for n in starts]
    assert [c[33] for c, _, _ in traces] == [21, 22]
    assert [c[34] for c, _, _ in traces] == [22, 22]
    assert [s[34] for _, s, _ in traces] == [21632881628] * 2
    literal, demand = [], []
    baselines = []
    for counts, _, bits in traces:
        a, bit = counts[33], bits[33]
        outcomes = [int(3 ** (a + b) >= 2 ** 34) for b in (0, 1)]
        baseline = Fraction(sum(outcomes), 2)
        baselines.append(baseline)
        literal.append(Fraction(outcomes[bit]) - baseline)
        demand.append(Fraction(2 * bit - 1, 2) * (outcomes[1] - outcomes[0]))
    assert baselines == [Fraction(1, 2), Fraction(1)]
    assert literal == demand == [Fraction(1, 2), Fraction(0)]
    assert sum(literal) == Fraction(1, 2)
    assert sum(literal) != 0, 'counterfactual unexpectedly held'
    print('TC1 PASS: two admitted width-34 trajectories, classes 21/22 to 22/22')
    print('Fair baselines:', [str(x) for x in baselines])
    print('Literal and demand-weighted changes:', [str(x) for x in literal])
    print('Pair total: 1/2; terminal-pooling cancellation counterfactual REFUTED')
    print('Selected-pair diagnostic only; no full-population discrepancy measured')


if __name__ == '__main__':
    main()
