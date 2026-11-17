#!/usr/bin/env python3
"""sc17_reef_granny.py: spark SC17 (SPARKS.md). A reef bow and a granny bow are different knots.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc17_reef_granny.py
COST:       well under a second (at most 2^6 states per knot).

Each knot is the closure of a braid. A trefoil is the closure of three same-sign crossings on two strands; the granny
is two trefoils of the same sign on three strands (s1^3 s2^3), the reef two of opposite signs (s1^3 s2^-3). The
Kauffman bracket is computed exactly as a state sum: every crossing is split one of two ways, the loops are counted
with a union-find, and <K> = sum over states of A^(#A - #B) (-A^2 - A^-2)^(loops - 1). The Jones polynomial is
V(t) = (-A^3)^(-w) <K> with A = t^(-1/4), where w is the writhe (the sum of the crossing signs).
Predictions (published in SPARKS.md before this ran): V(granny) = V(trefoil)^2; V(reef) = V(trefoil)(t) V(trefoil)(1/t),
unchanged under t -> 1/t; V(granny) changes under t -> 1/t; so the two differ and the granny is chiral.
Controls: the unknot (one positive kink) gives 1, which also fixes which way of splitting a crossing is the A one; the
positive trefoil gives t + t^3 - t^4; the figure-eight knot (s1 s2^-1 s1 s2^-1) gives t^2 - t + 1 - t^-1 + t^-2.
"""
from collections import Counter
from itertools import product


def padd(p, q, k=1):
    out = Counter(p)
    for e, c in q.items():
        out[e] += k * c
    return {e: c for e, c in out.items() if c}


def pmul(p, q):
    out = Counter()
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            out[e1 + e2] += c1 * c2
    return {e: c for e, c in out.items() if c}


def ppow(p, n):
    out = {0: 1}
    for _ in range(n):
        out = pmul(out, p)
    return out


def bracket(word, strands):
    """Kauffman bracket of the closure of a braid word [(i, sign), ...], as {exponent of A: coefficient}."""
    m = len(word)
    node = lambda level, s: level * strands + s          # level 0..m, strand 0..strands-1; level m is level 0
    delta = {2: -1, -2: -1}                               # -A^2 - A^-2
    total = {}
    for state in product((0, 1), repeat=m):               # 1 = the A-smoothing
        parent = list(range((m + 1) * strands))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def join(a, b):
            parent[find(a)] = find(b)

        for s in range(strands):
            join(node(m, s), node(0, s))                  # the closure
        for k, ((i, sign), a) in enumerate(zip(word, state)):
            i -= 1
            for s in range(strands):
                if s not in (i, i + 1):
                    join(node(k, s), node(k + 1, s))
            # For a positive crossing the A-smoothing keeps the two strands running straight down (top end to
            # bottom end); the unknot control below fixes this choice. The first run had it the other way round and
            # the control caught it, giving A^-6 instead of 1.
            horizontal = (a == 1) != (sign > 0)
            if horizontal:
                join(node(k, i), node(k, i + 1)); join(node(k + 1, i), node(k + 1, i + 1))
            else:
                join(node(k, i), node(k + 1, i)); join(node(k, i + 1), node(k + 1, i + 1))
        loops = len({find(x) for x in range(m * strands)})
        na = sum(state)
        total = padd(total, pmul({na - (m - na): 1}, ppow(delta, loops - 1)))
    return total


def jones(word, strands):
    """V(t) as {exponent of t: coefficient}, assuming the closure is a knot (integer exponents)."""
    w = sum(sign for _, sign in word)
    v = bracket(word, strands)                            # start from <K>
    factor = {-3 * w: -1 if w % 2 else 1}                 # (-A^3)^(-w) = (-1)^w A^(-3w), kept an integer
    v = pmul(factor, v)
    out = {}
    for e, c in v.items():                                # A = t^(-1/4): A^e = t^(-e/4)
        assert e % 4 == 0, ("not a knot?", v)
        out[-e // 4] = c
    return out


def mirror(p):
    return {-e: c for e, c in p.items()}


def show(p):
    terms = []
    for e in sorted(p):
        c = p[e]
        mono = "1" if e == 0 else ("t" if e == 1 else f"t^{e}")
        coef = "" if abs(c) == 1 and e != 0 else str(abs(c))
        terms.append(("- " if c < 0 else "+ ") + (coef if e == 0 else coef + mono))
    return " ".join(terms).lstrip("+ ")


def main():
    P, N = 1, -1
    unknot = jones([(1, P)], 2)
    trefoil = jones([(1, P)] * 3, 2)
    eight = jones([(1, P), (2, N), (1, P), (2, N)], 3)
    granny = jones([(1, P)] * 3 + [(2, P)] * 3, 3)
    reef = jones([(1, P)] * 3 + [(2, N)] * 3, 3)
    granny_mirror = jones([(1, N)] * 3 + [(2, N)] * 3, 3)
    assert unknot == {0: 1}, unknot
    assert trefoil == {1: 1, 3: 1, 4: -1}, show(trefoil)
    assert eight == {2: 1, 1: -1, 0: 1, -1: -1, -2: 1}, show(eight)
    print("controls: unknot 1; trefoil", show(trefoil), "; figure-eight", show(eight))
    print("granny:", show(granny))
    print("reef:  ", show(reef))
    print("granny's mirror:", show(granny_mirror))
    checks = {
        "granny = trefoil squared": granny == pmul(trefoil, trefoil),
        "reef = trefoil times its mirror": reef == pmul(trefoil, mirror(trefoil)),
        "reef unchanged by t -> 1/t (as an amphichiral knot's must be)": reef == mirror(reef),
        "granny changed by t -> 1/t, so the granny is chiral": granny != mirror(granny),
        "granny's mirror computed directly equals granny with t -> 1/t": granny_mirror == mirror(granny),
        "granny and reef differ, so they are different knots": granny != reef,
    }
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
    print("PASS" if all(checks.values()) else "FAIL")


if __name__ == "__main__":
    main()
