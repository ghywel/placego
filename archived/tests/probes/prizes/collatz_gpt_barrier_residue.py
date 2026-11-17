"""G67 RB1–RB2, preregistered at 8bb27ab; finite residue controls."""
from itertools import product
from collatz_gpt_actual_ceiling import specification, trajectory
from collatz_gpt_barrier_offset import extremal, intercept
from collatz_gpt_first_deficit_gap import first_deficit, terminal


def main():
    classes = {}
    population = 0
    for t in range(1, 17):
        for word in product((0, 1), repeat=t):
            if not first_deficit(word):
                continue
            population += 1
            a = sum(word)
            r, K = specification(word)
            g = terminal(r, word)-r
            assert 2**t*g == intercept(word)-(2**t-3**a)*r
            if a:
                classes.setdefault(a, []).append((word, g))
    mismatches = []
    matches = []
    for a, rows in sorted(classes.items()):
        word, _ = extremal(a)
        g = dict(rows)[word]
        maximum = max(gap for _, gap in rows)
        if g == maximum:
            matches.append(a)
        else:
            witness = next(w for w, gap in rows if gap == maximum)
            mismatches.append((a, ''.join(map(str, word)), g,
                               ''.join(map(str, witness)), maximum))
    print('RB1 population:', population)
    print('RB1 matching odd-count classes:', matches)
    print('RB1 mismatches (a, extremizer, gap, witness, max gap):', mismatches)
    # RB1's expected disagreement is checked directly, not assumed as an axiom.
    print('RB1 prediction:', 'PASS' if mismatches else 'FAIL')
    # Post-control diagnostic: exact short witnesses make the failed ordering
    # independently reviewable without the class enumeration.
    for text, expected in [('1101100', (85, 59, -21)),
                           ('1110100', (73, 7, -2))]:
        word = tuple(map(int, text))
        r, _ = specification(word)
        assert (intercept(word), r, terminal(r, word)-r) == expected

    survivors = []
    zero_residues = []
    for a in range(1, 257):
        word, B = extremal(a)
        t = len(word)
        r, K = specification(word)
        m0 = int(r == 0)
        n0 = r+2**t*m0
        observed_word, survives = trajectory(n0, t)
        assert observed_word == word and survives == (n0 <= K)
        gap = terminal(n0, word)-n0
        assert 2**t*gap == B-(2**t-3**a)*n0
        if r == 0:
            zero_residues.append(a)
        for m in range(m0, (K-r)//(2**t)+1):
            n = r+2**t*m
            assert trajectory(n, t) == (word, True)
            survivors.append((a, t, n, terminal(n, word)-n))
    print('RB2 zero residues:', zero_residues)
    print('RB2 all positive surviving lifts:', survivors)
    print('RB2 prediction:', 'PASS' if survivors == [(1, 2, 1, 0)] else 'FAIL')
    print('Unexpected ranking guard:', 'REFUTED' if mismatches else 'NOT REFUTED')


if __name__ == '__main__':
    main()
