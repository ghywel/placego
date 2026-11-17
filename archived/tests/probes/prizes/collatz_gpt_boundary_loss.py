"""G71 BT1–BT2; preregistered at 86d2d06. Exact bounded controls."""
from fractions import Fraction
from itertools import product
from collatz_gpt_actual_ceiling import specification
from collatz_gpt_first_deficit_gap import terminal


def threshold(t):
    a = 0
    while 3**a < 2**t:
        a += 1
    return a


def admissible(word):
    a = 0
    for t, b in enumerate(word, 1):
        a += b
        if 3**a < 2**t:
            return False
    return True


def coin(horizon):
    counts = {0: 1}
    V, N = [], []
    for t in range(horizon+1):
        V.append(sum(counts.values()))
        critical = threshold(t+1) > threshold(t)
        N.append(counts.get(threshold(t), 0) if critical else 0)
        child = {}
        for a, count in counts.items():
            for b in (0, 1):
                if 3**(a+b) >= 2**(t+1):
                    child[a+b] = child.get(a+b, 0)+count
        counts = child
    return V, N


def direct_count(lo, hi, horizon):
    result = 0
    for n in range(lo, hi):
        q, a, stays = n, 0, True
        for t in range(1, horizon+1):
            b = q % 2
            a += b
            q = (3*q+1)//2 if b else q//2
            stays &= 3**a >= 2**t
        result += stays
    return result


def main():
    V, N = coin(24)
    rows = []
    parents = 0
    for m in range(1, 13):
        words = [w for w in product((0, 1), repeat=m) if admissible(w)]
        assert len(words) == V[m]
        critical = threshold(m+1) > threshold(m)
        selected = [w for w in words if critical and sum(w) == threshold(m)]
        O = 0
        for word in selected:
            r, _ = specification(word)
            O += terminal(r, word) % 2
        F = len(selected)-2*O
        C = direct_count(2**m, 2**(m+1), m+1)
        assert len(selected) == N[m]
        assert C == V[m]-O and 2*C-V[m+1] == F
        if not critical:
            assert F == 0
        parents += len(words)
        rows.append((m, len(selected), O, F, C))
    print(f'BT1: {parents} admitted parents across12 widths; exact first-bit identities pass')
    print('BT1 rows (m,N,O,F,C):', rows)

    recurrences = ratios = zeros = 0
    for w in range(2, 11):
        m = w-1
        states = [(n, 0) for n in range(2**m, 2**(m+1))]
        for t in range(24):
            critical = threshold(t+1) > threshold(t)
            E = sum(a == threshold(t) and q % 2 == 0 for q, a in states) if critical else 0
            C = len(states)
            children = []
            for q, a in states:
                b = q % 2
                if 3**(a+b) >= 2**(t+1):
                    children.append(((3*q+1)//2 if b else q//2, a+b))
            following = len(children)
            if t >= m:
                assert following == C-E
                recurrences += 1
                R = Fraction(C*2**t, 2**m*V[t])
                R_next = Fraction(following*2**(t+1), 2**m*V[t+1])
                if C:
                    assert R_next == R*(1-Fraction(E, C))/(1-Fraction(N[t], 2*V[t]))
                    ratios += 1
                else:
                    assert following == 0 and R_next == 0
                    zeros += 1
            if t == m:
                assert C == V[m]
            states = children
    print(f'BT2: {recurrences} boundary-loss recurrences/{ratios} rational ratios/'
          f'{zeros} zero-parent steps pass')
    assert rows[0] == (1, 1, 0, 1, 1)
    print('CF: q-even loss would give0 at width2; direct count is1, wrong sign refuted')


if __name__ == '__main__':
    main()
