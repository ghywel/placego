"""GC589 E14 finite identity audit, 2026-10-08.
Before the exploratory symbolic calculation: predict no-11 suffices for
E14 white silence; counterfactual unconstrained-code silence; unexpected
check tests whether another visible-language restriction is necessary.
INITIAL OUTCOME: prediction REFUTED. Reduced E14 = c1*c3*c6, not zero.
The early zero assertion stopped that calculation before scalar controls.
FOLLOW-UP before this fixed control: polynomial E14 equals c1*c3*c6;
independent literal inverse agrees on all 34 seven-symbol no-11 words;
sole firing word is 0101001, excluded by the reviewed 101001 restriction.
CF no-11 suffices must fail on that formal word. Unexpected check retains
that exact equivalence, not merely one relaxed witness. No actual-right
census or SAT; no inferred infinite silent-depth family. Single-party.
"""
from itertools import product
from rule30_gpt_gc549_certificate import polynomials, mul, add, ONE, evaluate

def scalar(code):
    wall = [t % 2 for t in range(14)]
    right = [code[t//2] if t % 2 == 0 else 0 for t in range(13)]
    values = [0]
    for _ in range(13):
        left = [wall[t+1] ^ (wall[t] | right[t]) for t in range(len(wall)-1)]
        values.append(left[0])
        right, wall = wall, left
    return values

def main():
    f = polynomials()
    event = mul(f[12], add(ONE, f[13]))
    assert event == frozenset({frozenset({1,3,6})})
    words = [c for c in product((0,1), repeat=7)
             if not any(c[i] and c[i+1] for i in range(6))]
    firing = []
    for c in words:
        values = scalar(c)
        assert values == [evaluate(p,c) for p in f[:14]]
        e = values[12] & (1-values[13])
        assert e == c[1]*c[3]*c[6]
        if e: firing.append(''.join(map(str,c)))
    assert len(words) == 34 and firing == ['0101001']
    assert not [w for w in firing if '101001' not in w]
    print('PASS: reduced E14=c1*c3*c6; literal inverse agrees on 34 no-11 words.')
    print('CF rejected; unexpected exact firing set: 0101001, containing 101001.')

if __name__ == '__main__': main()

# FOLLOW-UP OUTCOME: fixed controls PASS, 34 no-11 words and all 14 depths.
# Reduced source is c1*c3*c6; sole relaxed firing word 0101001.
# The initial no-11-sufficiency prediction failed; actual silence uses GC504.
