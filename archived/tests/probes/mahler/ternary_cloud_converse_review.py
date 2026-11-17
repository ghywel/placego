#!/usr/bin/env python3
"""ternary_cloud_converse_review.py: Cloud's independent check of GPT's W295 / GC1249 (the ternary power converse).

RUN-ON:   cpu (Python 3 standard library), seconds.
COMMAND:  python3 tests/probes/mahler/ternary_cloud_converse_review.py

What it checks, without using GPT's shifted-digit lemma or code. Each step tries both next input digits and tests
every output digit of x^e directly, by pow modulo 3^(i+b+1). Here C is the 3-adic integers with digits 0 and 1, and
e = 3^b u with 3 not dividing u. Every e in -60 .. 60 is tried.

PREDICTIONS, written 2026-10-14 before the first run and pushed before it.
  R1: for u = 1 mod 3 and every h in 1 .. 5, the walk from 1 + 3^h never dead-ends to 80 input digits. Both the
      smaller-digit walk and the larger-digit walk are tried.
  R2: no prefix is lost at all. Over lengths 1 .. 9, every locally admissible unit prefix for those e extends.
  R3 (the other direction, 8.110's exclusion): for u = 2 mod 3, the seed 1 + 3^h dies at once. Its output digit h + b
      is 2.
  Counterfactual: a dead end under R1 or R2 would refute the construction's "an allowed next digit always exists".
"""
from itertools import product


def v3(e):
    b = 0
    while e % 3 == 0:
        e //= 3
        b += 1
    return b, e


def ok(y, n):
    for _ in range(n):
        if y % 3 == 2:
            return False
        y //= 3
    return True


def extends(x, i, e, b):
    return [d for d in (0, 1) if ok(pow(x + d * 3 ** i, e, 3 ** (i + b + 1)), i + b + 1)]


def main():
    es = [e for e in range(-60, 61) if e]
    plus = [e for e in es if v3(e)[1] % 3 == 1]
    minus = [e for e in es if v3(e)[1] % 3 == 2]
    r1 = True
    for e in plus:
        b = v3(e)[0]
        for h in range(1, 6):
            for pick in (min, max):
                x, i = 1 + 3 ** h, h + 1
                if not ok(pow(x, e, 3 ** (i + b)), i + b):
                    r1 = False
                while i < 80:
                    c = extends(x, i, e, b)
                    if not c:
                        r1 = False
                        break
                    x += pick(c) * 3 ** i
                    i += 1
    print('R1 walks from 1 + 3^h never dead-end to 80 digits (%d exponents, h = 1..5, both walks): %s' % (len(plus), r1))
    r2, n = True, 0
    for e in plus:
        b = v3(e)[0]
        for L in range(1, 10):
            for digits in product((0, 1), repeat=L - 1):
                x = 1 + sum(d * 3 ** (k + 1) for k, d in enumerate(digits))
                if ok(pow(x, e, 3 ** (L + b)), L + b):
                    n += 1
                    if not extends(x, L, e, b):
                        r2 = False
    print('R2 every locally admissible unit prefix extends (%d prefixes): %s' % (n, r2))
    r3 = all(not ok(pow(1 + 3 ** h, e, 3 ** (h + v3(e)[0] + 1)), h + v3(e)[0] + 1) for e in minus for h in range(1, 6))
    print('R3 sign-minus seeds die at digit h + b (%d exponents): %s' % (len(minus), r3))


if __name__ == '__main__':
    main()
