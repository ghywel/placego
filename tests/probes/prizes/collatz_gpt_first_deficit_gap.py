"""G48 FD1-FD3; published before run. Initial status NOT RUN."""
from itertools import product
from collatz_gpt_actual_ceiling import specification, trajectory


def terminal(n, w):
    for b in w:
        assert n % 2 == b
        n = (3*n+1)//2 if b else n//2
    return n


def first_deficit(w):
    a = 0
    for t, b in enumerate(w, 1):
        a += b
        if 3**a < 2**t:
            return t == len(w)
    return False


def main():
    words = lifts = 0
    returns = []
    strict = []
    for t in range(1, 17):
        modulus = 2**t
        for w in product((0, 1), repeat=t):
            if not first_deficit(w):
                continue
            r, K = specification(w)
            q = terminal(r, w)
            D = modulus-3**sum(w)
            g = q-r
            lo = 0 if r else 1
            for m in range(lo, lo+3):
                n = r+modulus*m
                final = terminal(n, w)
                predicted = g-D*m
                assert final-n == predicted
                assert trajectory(n, t) == (w, predicted >= 0)
                assert (n <= K) == (predicted >= 0)
                lifts += 1
            # Record all predicted positive surviving lifts, not just the three controls.
            for m in range(lo, g//D+1):
                n = r+modulus*m
                gap = terminal(n, w)-n
                assert trajectory(n, t) == (w, True)
                row = (t, ''.join(map(str, w)), n, gap)
                (returns if gap == 0 else strict).append(row)
            words += 1
    assert specification((0,)) == (0, 0)
    assert trajectory(2, 1) == ((0,), False)
    print(f'FD1: {words} first-deficit words/{lifts} direct positive lifts checked')
    print('FD2 realized returns:', returns)
    print('FD2 strict overshoots:', strict)
    held = returns == [(2, '10', 1, 0)] and not strict
    print('FINITE PREDICTION '+('HELD' if held else 'REFUTED; failures retained above'))
    print('Unexpected FD3: zero-residue gap0 is not a positive survivor')
    print('ALL CONTROLS PASS; no all-length equality or cycle theorem inferred')


if __name__ == '__main__':
    main()
