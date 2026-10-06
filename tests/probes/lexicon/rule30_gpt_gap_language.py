#!/usr/bin/env python3
"""G15: exact width-one visible language from white-time gaps.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_gap_language.py
RUN-ON: GPT Intel CPU, one process, standard library, short exhaustive audit.
PREDICTIONS before first run, 2026-10-06:
 VG0 control: scalar existence of rho agrees with the projected local
     conditions at each wall value, for all Boolean triples.
 VG1 theorem control: adjacent white times with gap1 forbid10;
     gap2 forbids11; gap>=3 allows every pair. Full projected language
     equals these nearest-neighbour constraints for all256 wall traces
     of length8; enumerate all256 sigma words for each wall.
 VG2 theorem control: transfer matrices A=[[1,1],[0,1]],
     F=[[1,1],[1,0]], J=[[1,1],[1,1]] count visible words exactly.
     All-black trace has one empty visible word.
 VG3 controls: white-end product A^(p-2)F equals G14's matrix;
     one-hole p>=3 uses J and has1 bit per visible hole, p2 uses F.
 VG4 unexpected: nonperiodic finite white gaps3,5,3,4 admit all32
     five-bit visible words, not just periodic-word examples.
 CF must fail: same white fraction determines width-one visible
     entropy. Primitive period8 words00111111 and01101111 have
     per-period growth3 and4 despite both having two white cells.
 REFUTED-BY: any scalar/language/matrix control fails or CF not rejected.
 Width-one relaxation only: rho is a free input at each time, not
 asserted to evolve as a further Rule30 column. No actual channel
 entropy, LR, cost lower bound or prize proof is claimed.
"""
import itertools
from rule30_gpt_white_latch import matmul,allowed


def gap_matrix(g):
    return [[1,1],[0,1]] if g==1 else [[1,1],[1,0]] if g==2 else [[1,1],[1,1]]


def brute(tau):
    positions=[i for i,v in enumerate(tau) if not v];visible=set()
    for word in itertools.product([0,1],repeat=len(tau)):
        if all(any(word[t+1]==(tau[t]^(word[t]|r)) for r in [0,1])
               for t in range(len(tau)-1)):
            visible.add(tuple(word[i] for i in positions))
    return positions,visible


def predicted(positions):
    n=len(positions);gaps=[b-a for a,b in zip(positions,positions[1:])]
    words={w for w in itertools.product([0,1],repeat=n)
           if all(gap_matrix(gaps[i])[w[i]][w[i+1]] for i in range(n-1))}
    product=[[1,0],[0,1]]
    for g in gaps:product=matmul(product,gap_matrix(g))
    count=sum(map(sum,product)) if n else 1
    return words,count


def main():
    for tau,a,b in itertools.product([0,1],repeat=3):
        assert allowed(tau,a,b)==any(b==(tau^(a|r)) for r in [0,1])
    for tau in itertools.product([0,1],repeat=8):
        positions,actual=brute(tau);expected,count=predicted(positions)
        assert actual==expected and len(actual)==count,(tau,actual,expected)
    print('PASS VG0/VG1/VG2: all256 length8 wall traces and their full projected languages',flush=True)
    a=[[1,1],[0,1]];f=gap_matrix(2);power=[[1,0],[0,1]]
    for p in range(2,65):
        assert matmul(power,f)==[[p-1,1],[1,0]],p
        power=matmul(power,a)
        if p>=3:assert gap_matrix(p)==[[1,1],[1,1]]
    print('PASS VG3: p2..64 white-end product; p>=3 black-end full visible shift',flush=True)
    positions=[0,3,8,11,15];tau=[int(t not in positions) for t in range(16)]
    _,actual=brute(tau);assert actual==set(itertools.product([0,1],repeat=5))
    print('PASS VG4 unexpected: gaps3,5,3,4 give all32 visible words',flush=True)
    clustered=matmul(gap_matrix(1),gap_matrix(7))
    separated=matmul(gap_matrix(3),gap_matrix(5))
    assert clustered==[[2,2],[1,1]] and separated==[[2,2],[2,2]]
    assert clustered[0][0]+clustered[1][1]==3
    assert separated[0][0]+separated[1][1]==4
    print('PASS CF rejected: same fraction2/8, per-period growth3 versus4',flush=True)
    print('ALL CONTROLS PASS',flush=True)


if __name__=='__main__':main()
# OUTCOME 2026-10-06 07:57 BST: exit0, ALL CONTROLS PASS.
# VG0-VG2 all256 length8 wall traces and their full visible languages
# match the nearest-neighbour gap matrices. VG3 p2..64 products pass.
# Unexpected VG4 non-uniform gaps3,5,3,4 admit all32 five-bit words.
# CF same-fraction capacity rejected: primitive period8 words00111111
# and01101111 have exact per-period growth3 and4 in width-one relaxation.
