#!/usr/bin/env python3
"""GC508 fixed singleton-reset controls, not an iid speed simulation.
COMMAND: python3 tests/probes/lexicon/rule30_gpt_front_reset.py
PREDICTIONS registered in CLOUD-LOCAL before execution:
 FR0: GC507 reset pair has first row {-2,-1,1}, damage singleton N+1.
 FR1: at least floor(N/2) further left moves, N=2..13.
 FR2: for odd N, the following move is not a left advance.
 CF: singleton reset immediately sees a fair healing bit, must fail;
     the next move in this family is always left.
 UNEXPECTED: right jump size controls a deterministic compensating bout.
 OUTCOME (2026-10-08): FR0/FR1/FR2 PASS for all 12 pairs in
 both implementations; singleton-regeneration CF REFUTED. All-N proof in GC508.
"""
from rule30_gpt_front_selection import step


def main():
    for n in range(2,14):
        expected=list(range(n+1,n+1-n//2-1,-1))
        traces=[]
        for literal in [False,True]:
            x={-1,0};y={-1}|set(range(1,n+1))
            x,y=step(x,literal),step(y,literal)
            assert x=={-2,-1,1} and x^y=={n+1}
            fronts=[min(x^y)]
            for _ in range(n//2+1):
                x,y=step(x,literal),step(y,literal)
                fronts.append(min(x^y))
            assert fronts[:len(expected)]==expected
            if n%2: assert fronts[-1]>=fronts[-2]
            traces.append(fronts)
        assert traces[0]==traces[1]
    print('FR0/FR1/FR2 PASS: 12 reset pairs, two implementations')
    print('singleton-regeneration CF REFUTED: immediate left move always')
    print('ALL CHECKS PASS')


if __name__=='__main__':main()
