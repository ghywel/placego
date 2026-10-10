#!/usr/bin/env python3
"""GC1015: the whole GC1014 family is insufficient to retain exact past.
Registered closure attempt and outcome are in RULE30-GPT. This retains
only the separating cylinder and its independent controls, not a census.
"""
from itertools import product
from rule30_marker_prehistory import image_language, advance
from rule30_mature_short_gate import step


def main():
    word = '1110111110'
    # After its fifth bit the first later one is doubled; every extension
    # satisfies the entire family constraint, not merely a finite cutoff.
    j = word.index('1', 5)
    assert word[j+1] == '1'
    a, b, c, d = map(int, word[5:9])
    assert (not a or b) and (a or not b or c) and (a or b or not c or d)
    e = image_language()
    q = frozenset(range(4, 8))
    expected = [(13, 14, 15), (10, 11, 12), (4, 5, 6, 7, 8, 9),
                (0, 13, 14, 15), (1, 10, 11, 12), ()]
    for bit, target in zip(word[4:], expected):
        q = advance(e, q, bit)
        assert tuple(sorted(q)) == target
    nine_present = False
    for row in product((0, 1), repeat=12):
        image = ''.join(map(str, step(step(row, 0), 1)))
        assert image != word
        nine_present |= image[:9] == word[:9]
    assert nine_present
    # No past does not imply no valid future: this cylinder emits SS.
    for tail in ([0]*24, [1]*24, [0, 1]*12):
        row = list(map(int, word))+tail
        ones = []
        for t in range(15):
            if t % 2 == 0 and row[0]:
                ones.append(t//2)
            row = step(row, t % 2)
        assert ones[:3] == [0, 3, 6]
    print('PASS: full family and nine-cell gate pass; exact past absent; prefix9 present; SS future retained')


if __name__ == '__main__':
    main()
