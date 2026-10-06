"""G91 CM1-CM2, preregistered before execution. NOT RUN.
CM1 MUST HOLD: widths 2..5, horizons m..9: all literal H increments
equal the matched/unmatched decomposition; retain empty and lost children.
CM2 MUST HOLD: G90 pair matches once and contributes 1/2. Synthetic
two-odd/three-even multiplicities match twice with correct residual.
UNEXPECTED CHECK: width2,T4,t3 lost even child contributes -1/2.
COUNTERFACTUAL MUST FAIL: remove failed children before regrouping.
REFUTED-BY: any exact rational mismatch or a zero lost-child contribution.
No mass, rate or global bias estimate; no large population.
"""
from collections import Counter
from fractions import Fraction
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_terminal_pooling import trajectory


def grouped(parents, delta, t, drop_failed=False):
    odd, even = Counter(), Counter()
    for x, a in parents:
        bit = x % 2
        b = a + bit
        y = (3 * x + 1) // 2 if bit else x // 2
        if drop_failed and 3 ** b < 2 ** (t + 1):
            continue
        (odd if bit else even)[y, b] += 1
    total = Fraction(0)
    matches = 0
    for key in odd.keys() | even.keys():
        _, b = key
        o, e = odd[key], even[key]
        matched = min(o, e)
        matches += matched
        total += (matched * (delta.get(b-1, 0)-delta.get(b, 0))
                  + (o-matched)*delta.get(b-1, 0)
                  - (e-matched)*delta.get(b, 0))/2
    return total, matches


def main():
    cases = increments = empty = 0
    for w in range(2, 6):
        m = w-1
        rows = states_at(w, 9)
        for T in range(m, 10):
            f = backward(T)
            cases += 1
            for t in range(m, T):
                delta = {a: f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
                before = sum((f[t][a] for _, a in rows[t]), Fraction(0))
                after = sum((f[t+1][a] for _, a in rows[t+1]), Fraction(0))
                assert grouped(rows[t], delta, t)[0] == after-before
                increments += 1
                empty += not rows[t]
    f = backward(34)
    delta = {a: f[34][a+1]-f[34][a] for a in range(35)}
    parents = []
    for n in (11843133435, 11843133439):
        counts, states, _ = trajectory(n)
        parents.append((states[33], counts[33]))
    assert grouped(parents, delta, 33) == (Fraction(1, 2), 1)
    synthetic = [parents[0]]*2 + [parents[1]]*3
    assert grouped(synthetic, delta, 33) == (Fraction(1), 2)
    # Enumerate the last bit independently instead of relying on backward DP.
    outcomes = [int(3 ** (2+b) >= 2 ** 4) for b in (0, 1)]
    literal = Fraction(outcomes[0]) - Fraction(sum(outcomes), 2)
    assert literal == Fraction(-1, 2)
    guard_delta = {2: Fraction(outcomes[1]-outcomes[0])}
    assert grouped([(4, 2)], guard_delta, 3)[0] == literal
    assert grouped([(4, 2)], guard_delta, 3, drop_failed=True)[0] != literal
    print('CM1 PASS:', cases, 'horizons,', increments, 'increments,', empty, 'empty parents')
    print('CM2 PASS: true pair and synthetic multiplicities; lost-child guard -1/2')
    print('Surviving-children-only counterfactual REFUTED; no global bound measured')


if __name__ == '__main__':
    main()
