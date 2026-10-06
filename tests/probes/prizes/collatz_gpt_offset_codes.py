"""G81 CI1-CI2, preregistered at9a9a46d (published via050f51c).
CI1 MUST HOLD: W_a for a1..12, full-prefix admission, two intercept
formulas and parity residues agree; no residue collision for a1..6.
CI2 BLIND: no collision for a7..12. Retain refutation and evolve witnesses.
CF: admission unnecessary for a>=7 threshold; MUST FAIL a2 guard.
REFUTED-BY: unrestricted offsets7/259 modulo9, starts625/597 meet at11.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
CI1 PASS68722 complete position-set/admission comparisons;4403 admitted
words through a12, no residue collision. CI2 HELD. Witness groups empty.
CF REFUTED by offsets7/259, first deficits2. Initial included-word
check was followed by a completeness control on every excluded set;
both passed. No larger actual-start scan or all-a singleton theorem.
"""
from collections import defaultdict
from itertools import combinations
from collatz_gpt_boundary_loss import admissible
from collatz_gpt_actual_ceiling import specification


def intercept(word):
    B = 0
    for j, b in enumerate(word):
        B = 3**b*B+b*2**j
    return B


def evolve(n, length):
    y, a, deficit = n, 0, None
    bits = []
    for t in range(1, length+1):
        b = y % 2
        bits.append(b)
        a += b
        y = (3*y+1)//2 if b else y//2
        if deficit is None and 3**a < 2**t:
            deficit = t
    return tuple(bits), a, y, deficit


def main():
    rows, groups, witnesses = [], [], []
    candidates = 0
    for a in range(1, 13):
        A = 3**a
        t = A.bit_length()-1
        by_residue = defaultdict(list)
        for positions in combinations(range(t), a):
            selected = set(positions)
            word = tuple(int(j in selected) for j in range(t))
            allowed = all(p <= (3**i).bit_length()-1 for i, p in enumerate(positions))
            assert allowed == admissible(word)
            candidates += 1
            if not allowed:
                continue
            B = sum(3**(a-1-i)*2**p for i, p in enumerate(positions))
            assert B == intercept(word)
            r, K = specification(word)
            assert K is None and evolve(r+2**t, t)[0] == word
            by_residue[B % A].append((B, word, r))
        collisions = [g for g in by_residue.values() if len(g) > 1]
        assert a > 6 or not collisions
        for group in collisions:
            groups.append((a, [(B, word) for B, word, _ in group]))
            B, word, r = group[0]
            for Bp, wordp, _ in group[1:]:
                delta = (B-Bp)//A
                assert delta and delta % 2 == 0 and 3*abs(delta) < a
                M = 2**t
                n = r+(2 if delta > 0 else 3)*M
                np = n+delta
                assert 2*M <= n < 4*M and 2*M <= np < 4*M
                first, second = evolve(n, t), evolve(np, t)
                assert first[0] == word and second[0] == wordp
                assert first[1:] == second[1:] and first[3] is None
                witnesses.append((a, t, n, np, first[2]))
        rows.append((a, t, sum(map(len, by_residue.values())), len(collisions)))
    first, second = evolve(625, 9), evolve(597, 9)
    assert first[1:] == second[1:] == (2, 11, 2)
    B, Bp = intercept(first[0]), intercept(second[0])
    assert (B, Bp) == (7, 259) and B % 9 == Bp % 9
    print('CI1 completeness checks:', candidates)
    print('CI1 PASS rows(a,maximal horizon,word count,collision groups):', rows)
    print('CI2', 'HELD' if not groups else 'REFUTED', ': no collision for a7..12')
    print('All modular collision groups:', groups)
    print('Direct admitted witnesses:', witnesses)
    print('CF REFUTED: unrestricted a2 offsets7/259; both first deficits2')


if __name__ == '__main__':
    main()
