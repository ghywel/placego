#!/usr/bin/env python3
"""GC2355 small exact controls; predictions in genealogy report section14.

Fixed right111000..., all256 eight-bit ribbons, 24-update hard bound.
64 three-episode candidates in1..4, plus two named rejection controls.
Independent finite-set truth-table oracle versus bounded triangular prefix.
No files, random samples, external packages, or automatic horizon increase.
"""
from itertools import product


def horizon(q, lengths):
    exposed = total = 0
    for length in lengths:
        assert length >= 1
        total += (q + exposed + 1) // 2
        exposed += length
    return total


class Prefix:
    """z_d(t)=x_(q+t-d)(t); depth beyond the stored prefix is irrelevant."""
    def __init__(self, word, right=(1, 1, 1)):
        self.q = len(right) - 1
        assert right[0] == right[-1] == 1 and self.q > 0
        self.z = list(reversed(right)) + list(word)
        self.t = 0

    def bit(self, depth):
        assert 0 <= depth < len(self.z)
        return self.z[depth]

    def step(self):
        old = [0, 0] + self.z
        self.z = [old[d + 2] ^ (old[d + 1] | old[d])
                  for d in range(len(self.z))]
        self.t += 1


class Ordinary:
    """Independent physical coordinates and the eight-entry rule30 table."""
    def __init__(self, word, right=(1, 1, 1)):
        self.q = len(right) - 1
        self.row = {i for i, bit in enumerate(right) if bit}
        self.row |= {-j for j, bit in enumerate(word, 1) if bit}
        self.t = 0

    def bit(self, depth):
        return int(self.q + self.t - depth in self.row)

    def step(self):
        row = self.row
        self.row = {i for i in range(min(row) - 1, max(row) + 2)
                    if (30 >> (4 * (i-1 in row) + 2 * (i in row)
                               + (i+1 in row))) & 1}
        self.t += 1


def advance(model, n, cap):
    assert model.t + n <= cap, ('fixed cap', model.t, n, cap)
    for _ in range(n):
        model.step()


def gap(model, depth):
    assert model.bit(depth) == 1
    nearest = next(d for d in range(depth - 1, -1, -1) if model.bit(d))
    return depth - nearest - 1


def encode(model, size, cap):
    depth = model.q
    code, queries = [], []
    while len(code) < size:
        advance(model, gap(model, depth) // 2, cap)
        length = 1
        while len(code) < size:
            value = model.bit(depth + length)
            code.append(value)
            queries.append((model.t, depth + length))
            if value == 0 or len(code) == size:
                break
            length += 1
        if len(code) == size:
            break  # a prefix may end inside a black run
        advance(model, 1, cap)
        depth += length
    return tuple(code), tuple(queries)


def verify(model, lengths):
    cap = horizon(model.q, lengths)
    depth, exposed = model.q, 0
    for episode, length in enumerate(lengths, 1):
        advance(model, gap(model, depth) // 2, cap)
        for j in range(1, length + 1):
            wanted = int(j < length)
            actual = model.bit(depth + j)
            if actual != wanted:
                return dict(accepted=False, episode=episode, index=exposed+j,
                            time=model.t, depth=depth+j, wanted=wanted,
                            actual=actual, bound=cap)
        # Oracle also verifies the actual follower landing independently.
        old_front = model.q + model.t - depth
        advance(model, 1, cap)
        if isinstance(model, Ordinary):
            landing = max(i for i in model.row if i <= old_front + 1)
            assert landing == old_front - length + 1
        depth += length
        exposed += length
        assert model.bit(depth) == 1
    return dict(accepted=True, time=model.t, bound=cap, consumed=exposed)


def decode(code, right=(1, 1, 1)):
    """GC699 constant-diagonal repair, with the adaptive genealogy query clock.

    Store columns through the proved bound. A repaired column is complemented at
    EVERY time, not merely at its query: otherwise it is not a valid CA column.
    """
    q = len(right) - 1
    cap = sum((q+j+1)//2 for j in range(len(code)))
    columns = []

    def column(initial):
        col = [initial]
        for t in range(cap):
            a = columns[-1][t] if columns else 0
            b = columns[-2][t] if len(columns) > 1 else 0
            col.append(col[-1] ^ (a | b))
        return col

    for initial in reversed(right):
        columns.append(column(initial))
    initial_word = []
    depth, t, start = q, 0, True
    for index, wanted in enumerate(code, 1):
        if start:
            assert columns[depth][t] == 1
            nearest = next(d for d in range(depth-1, -1, -1) if columns[d][t])
            t += (depth-nearest-1)//2
            assert t <= cap
        col = column(0)
        repair = col[t] ^ wanted
        columns.append([bit ^ repair for bit in col])
        initial_word.append(repair)
        start = wanted == 0
        if start:
            t += 1
            depth = q + index
            assert t <= cap
    return tuple(initial_word)


def main():
    size = 8
    cap = sum((2+j+1)//2 for j in range(size))
    assert cap == 24
    maps = [dict() for _ in range(size + 1)]
    longest = 0
    for word in product((0, 1), repeat=size):
        result = encode(Prefix(word), size, cap)
        assert result == encode(Ordinary(word), size, cap), word
        code, queries = result
        longest = max(longest, queries[-1][0])
        for k in range(size + 1):
            key, value = word[:k], code[:k]
            assert maps[k].setdefault(key, value) == value
    for k, mapping in enumerate(maps):
        assert len(mapping) == len(set(mapping.values())) == 2**k
    print(f'PASS: 256 words, both implementations; all prefix bijections; latest query {longest} <= {cap}')
    for code in product((0, 1), repeat=size):
        word = decode(code)
        assert maps[size][word] == code
    print('PASS: all256 output words inverted by adaptive constant-diagonal repair')

    accepted = []
    for lengths in product(range(1, 5), repeat=3):
        word = (0,) * sum(lengths)
        answer = verify(Prefix(word), lengths)
        assert answer == verify(Ordinary(word), lengths)
        if answer['accepted']:
            accepted.append(lengths)
    assert accepted == [(1, 1, 4)], accepted
    print('PASS: 64 candidate lists, identical first-obstruction records; sole acceptance (1,1,4)')
    for lengths in ((1, 1, 3), (1, 1, 4), (1, 1, 5)):
        word = (0,) * sum(lengths)
        result = verify(Prefix(word), lengths)
        assert result == verify(Ordinary(word), lengths)
        code = tuple(bit for length in lengths for bit in [1]*(length-1)+[0])
        decoded = decode(code)
        assert verify(Ordinary(decoded), lengths)['accepted']
        print(f'{lengths}: {result}; decoded {"".join(map(str, decoded))}')

    # First difference of input and output occurs at exactly the same bit.
    # The rejected third episode L=3 needs its fifth initial bit flipped.
    assert maps[5][(0, 0, 0, 0, 1)] == (0, 0, 1, 1, 0)
    assert maps[6][(0,)*6] == (0, 0, 1, 1, 1, 0)

    n = 60
    itinerary = []
    for _ in range(6):
        itinerary.append(n % 2)
        n = (3*n + n % 2)//2
    assert itinerary == [0, 0, 1, 1, 1, 0]
    print('PASS: Mahler start60 has parity001110; its 11 forbids a half-surviving fractional companion')


if __name__ == '__main__':
    main()
