#!/usr/bin/env python3
"""sc3_last_diminisher.py: spark SC3 (SPARKS.md). A fair ladle is fair but can still be envied.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc3_last_diminisher.py
COST:       about a minute.

Model: the pot is [0, 1]; each person values it by a random step function on 20 equal parts (weights uniform on the
simplex), so values are exact and cuts are placed by inverting each person's cumulative value. The last-diminisher
rule, with r people left and the rest of the pot C: the first marks the piece from the left edge worth V(C)/r to
them; each other person who values that piece above V(C)/r trims it to exactly V(C)/r by their own measure and
becomes its holder; the holder takes it and leaves. The last person takes what remains.
Predictions (published in SPARKS.md before this ran): every person gets at least 1/n of the pot by their own measure
in every run; no envy at n = 2; envy in at least 20 per cent of runs at each n from 3 to 6.
Control: n = 1 gives the whole pot; a two-person run is checked for envy-freeness, which the theory guarantees.
"""
import random

random.seed(20261007)
PARTS, RUNS, EPS = 20, 20_000, 1e-9


def person():
    w = [random.expovariate(1.0) for _ in range(PARTS)]
    t = sum(w)
    return [x / t for x in w]


def value(d, a, b):
    """Value of [a, b] under step density d (each part has width 1/PARTS)."""
    total, i = 0.0, int(a * PARTS)
    while a < b - 1e-15 and i < PARTS:
        right = min(b, (i + 1) / PARTS)
        total += d[i] * (right - a) * PARTS
        a, i = right, i + 1
    return total


def cut(d, a, target):
    """Smallest x >= a with value(d, a, x) = target (target <= value(d, a, 1))."""
    i, got = int(a * PARTS), 0.0
    while i < PARTS:
        right = (i + 1) / PARTS
        here = d[i] * (right - a) * PARTS
        if got + here >= target - 1e-15:
            return a + (target - got) / (d[i] * PARTS) if d[i] > 0 else a
        got, a, i = got + here, right, i + 1
    return 1.0


def last_diminisher(people):
    n = len(people)
    left, active, pieces = 0.0, list(range(n)), {}
    while len(active) > 1:
        r = len(active)
        holder = active[0]
        x = cut(people[holder], left, value(people[holder], left, 1.0) / r)
        for j in active[1:]:
            fair = value(people[j], left, 1.0) / r
            if value(people[j], left, x) > fair + 1e-12:
                x, holder = cut(people[j], left, fair), j
        pieces[holder] = (left, x)
        active.remove(holder)
        left = x
    pieces[active[0]] = (left, 1.0)
    return pieces


def run(n):
    people = [person() for _ in range(n)]
    pieces = last_diminisher(people)
    own = [value(people[i], *pieces[i]) for i in range(n)]
    proportional = all(v >= 1.0 / n - EPS for v in own)
    envy = any(value(people[i], *pieces[j]) > own[i] + EPS for i in range(n) for j in range(n) if i != j)
    return proportional, envy, min(o * n for o in own)


def main():
    assert last_diminisher([person()]) == {0: (0.0, 1.0)}
    print(" n   runs   proportional   runs with envy   worst share x n")
    verdict = True
    for n in range(2, 7):
        res = [run(n) for _ in range(RUNS)]
        prop = sum(r[0] for r in res) / RUNS
        envy = sum(r[1] for r in res) / RUNS
        worst = min(r[2] for r in res)
        ok = prop == 1.0 and (envy == 0.0 if n == 2 else envy >= 0.20)
        verdict &= ok
        mark = 'as predicted' if ok else 'NOT as predicted'
        print(f" {n}  {RUNS}   {prop:11.1%}   {envy:13.1%}   {worst:14.6f}   {mark}")
    print("PASS" if verdict else "FAIL: see the rows marked NOT as predicted")


if __name__ == "__main__":
    main()
