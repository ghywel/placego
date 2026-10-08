#!/usr/bin/env python3
"""GC507 exact augmented transition and finite-window obstruction controls.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_front_window.py
PREDICTIONS registered before execution in CLOUD-LOCAL:
 FW0: all 64 baseline/damage triple combinations satisfy exact derivative.
 FW1: x={-1,0}, y={-1} union {1,...,N} give next damage {N+1}, N=1..12.
 CF: a radius-2 pair window decides the jump; N=3,4 must refute it.
 UNEXPECTED: arbitrarily wide finite damage collapses to one site.
 OUTCOME (2026-10-08): FW0 PASS, FW1 PASS in both implementations;
 radius-2 CF REFUTED. Universal-N proof in GC507; no speed run.
"""
from rule30_gpt_front_selection import step


def rule(l,c,r):return (30>>(4*l+2*c+r))&1


def main():
    for u in range(8):
        ul,uc,ur=[(u>>i)&1 for i in (2,1,0)]
        for d in range(8):
            dl,dc,dr=[(d>>i)&1 for i in (2,1,0)]
            actual=rule(ul,uc,ur)^rule(ul^dl,uc^dc,ur^dr)
            expect=dl^((1-uc)*dr)^((1-ur)*dc)^(dc*dr)
            assert actual==expect
    for n in range(1,13):
        x={-1,0};y={-1}|set(range(1,n+1))
        for literal in [False,True]:
            assert step(x,literal)^step(y,literal)=={n+1}
    def window(n):
        x={-1,0};y={-1}|set(range(1,n+1))
        return tuple((i in x,i in y) for i in range(-2,3))
    assert window(3)==window(4)
    print('FW0 PASS: 64 derivative identities')
    print('FW1 PASS: 12 one-tick finite-pair controls, two implementations')
    print('radius-2 closure CF REFUTED; reset to singleton confirmed')
    print('ALL CHECKS PASS')


if __name__=='__main__':main()
