#!/usr/bin/env python3
"""G13: exact inverse-row reset automaton, no record enumeration.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_inverse_reset.py
RUN-ON: GPT Intel CPU, one process, standard library; seconds.
PREDICTIONS before first run, 2026-10-06:
 IR0 control: four-state transition (a,b)->(b,y XOR(a OR b)) agrees
     with scalar inverse Rule30 on every Boolean triple.
 IR1 theorem control: shortest words resetting all four states have
     length4 and are exactly0100,0101; enumerate every word to length4.
 IR2 theorem control: arbitrary prefix then010z then arbitrary common
     suffix merges all four scalar reconstructions;512 seeded cases.
 IR3 theorem control: at a hole q=p of0 1^(p-1), p8..32, changing
     sigma(q) changes no depth>=8 in row q-1; eight seeded sigma
     backgrounds, depths1..96. G12 gives common future tail after3.
 IR4 unexpected check: constant drivers0 and1 both admit distinct
     state trajectories forever (fixed states or a 3-cycle).
 CF must fail: the three-symbol word010 already resets all states.
 REFUTED-BY: any control fails or CF not rejected. No blind global
     bound, records search, or universal hole-to-time0 theorem claimed.
"""
import itertools,random
from rule30_gpt_condrey_holes import forced_columns

STATES=list(itertools.product([0,1],repeat=2))


def step(state,y):
    a,b=state
    return b,y^(a|b)


def images(word):
    states=STATES[:]
    for y in word:states=[step(s,y) for s in states]
    return set(states)


def scalar(state,word):
    row=list(state)
    for y in word:row.append(y^(row[-1]|row[-2]))
    return row


def main():
    for a,b,y in itertools.product([0,1],repeat=3):
        assert step((a,b),y)==tuple(scalar((a,b),[y])[-2:])
    resets=[]
    for n in range(5):
        for word in itertools.product([0,1],repeat=n):
            if len(images(word))==1:resets.append(''.join(map(str,word)))
    assert resets==['0100','0101'],resets
    assert images([0,1,0])=={(0,1),(1,1)}
    print('PASS IR0/IR1/CF: shortest reset words exactly0100,0101; 010 not reset',flush=True)
    rng=random.Random(2026100613)
    for _ in range(512):
        before=[rng.randrange(2) for _ in range(rng.randrange(30))]
        reset=[0,1,0,rng.randrange(2)]
        after=[rng.randrange(2) for _ in range(60)]
        rows=[scalar(s,before+reset+after) for s in STATES]
        end=len(before)+4
        assert all(row[end:]==rows[0][end:] for row in rows)
    print('PASS IR2:512 random prefix/reset/suffix scalar controls',flush=True)
    checks=0
    for p in range(8,33):
        n=p+100;tau=[int(t%p!=0) for t in range(n)]
        for _ in range(8):
            sigma=[rng.randrange(2) for _ in range(n)]
            other=sigma[:];other[p]^=1
            a=forced_columns(tau,sigma,96);b=forced_columns(tau,other,96)
            assert all(a[j][p-1]==b[j][p-1] for j in range(7,96)),p
            checks+=1
    print('PASS IR3:%d one-step-back hole comparisons, p8..32, depth96'%checks,flush=True)
    assert len(images([0]*100))==2
    assert len(images([1]*100))==3
    assert step((0,0),0)==(0,0) and step((1,1),0)==(1,1)
    state=(0,0)
    for _ in range(3):state=step(state,1)
    assert state==(0,0)
    print('PASS IR4 unexpected: constant0 fixed-pair obstruction; constant1 3-cycle obstruction',flush=True)
    print('ALL CONTROLS PASS',flush=True)


if __name__=='__main__':main()
