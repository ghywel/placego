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


def language(repaired=False):
    import re
    checks=0
    for n in range(15):
        for word in itertools.product([0,1],repeat=n):
            text=''.join(map(str,word))
            expected=bool(re.search(r'01(?:111)*0[01]',text)) if repaired else '010' in text[:-1]
            assert (len(images(word))==1)==expected,text
            checks+=1
    print('ALL RESET-LANGUAGE CONTROLS PASS: %d words through length14'%checks,flush=True)


def multistep():
    rng=random.Random(2026100614);checks=0
    for p in range(5,65):
        n=p+100;tau=[int(t%p!=0) for t in range(n)]
        for _ in range(4):
            sigma=[rng.randrange(2) for _ in range(n)]
            other=sigma[:];other[p]^=1
            a=forced_columns(tau,sigma,96);b=forced_columns(tau,other,96)
            for r in range((p-5)//3+1):
                start=4*r+4;end=p-1+r;t=p-r
                assert all(a[j-1][t]==b[j-1][t] for j in range(start,97)),(p,r)
                assert all(a[j-1][t]==b[j-1][t]==int(j%2==0)
                           for j in range(start,end+1)),(p,r)
                checks+=1
    extra=0
    for q in range(1,7):
        p=3*q+5;n=q+p+70
        for _ in range(8):
            tau=[rng.randrange(2) for _ in range(n)]
            tau[q]=0;tau[q+1:q+p]=[1]*(p-1)
            sigma=[rng.randrange(2) for _ in range(n)]
            other=sigma[:];other[q]^=1
            a=forced_columns(tau,sigma,64);b=forced_columns(tau,other,64)
            assert all(a[j-1][0]==b[j-1][0] for j in range(4*q+4,65))
            extra+=1
    p=8;q=8;n=180;tau=[int(t%p!=0) for t in range(n)]
    sigma=[0]*n;other=sigma[:];other[q]=1
    a=forced_columns(tau,sigma,160);b=forced_columns(tau,other,160)
    beyond=[j for j in range(4*q+4,161) if a[j-1][0]!=b[j-1][0]]
    assert beyond
    print('ALL MULTISTEP CONTROLS PASS: %d protected-window comparisons; %d unexpected nonperiodic backgrounds'%(checks,extra),flush=True)
    print('CF unrestricted-r rejected: p8 q8 r8, first change beyond35 at%d'%beyond[0],flush=True)


if __name__=='__main__':
    import sys
    if len(sys.argv)>1 and sys.argv[1]=='language':language()
    elif len(sys.argv)>1 and sys.argv[1]=='language-repaired':language(True)
    elif len(sys.argv)>1 and sys.argv[1]=='multistep':multistep()
    else:main()

# OUTCOME 2026-10-06 07:37 BST: default command exit0, ALL CONTROLS PASS.
# IR0/IR1: exactly0100,0101 shortest; CF010 rejected. IR2:512 cases.
# IR3:200 comparisons p8..32, eight arbitrary sigma backgrounds each,
# depth96, no changes at depth>=8 in row q-1. IR4 constants0/1 pass.
# ADDENDUM before command with argument language, 2026-10-06 07:37 BST:
# IR5 theorem control: a word resets iff it contains010 followed by
# at least one bit; exhaust every word through length14. Subset-state
# transition proof is G13. Not a blind or a universal gap prediction.
# OUTCOME IR5: exit1, control failed at0111100, which resets without
# containing010. The candidate iff claim was false; IR0-IR4 stand.
# ADDENDUM IR6 before language-repaired: use exact subset-state proof,
# reset iff word contains0, then1 mod3 ones, then0 and one further bit.
# Test all32767 words through length14; retains IR5 unchanged.
# OUTCOME IR6 2026-10-06 07:38 BST: language-repaired exit0,
# ALL RESET-LANGUAGE CONTROLS PASS for32767 words through length14.
# IR5 still fails at0111100 in its original mode; no erased failure.
# ADDENDUM before multistep, 2026-10-06 07:42 BST:
# MS0 theorem control: p>=3r+5 implies hole flip at q=p changes no
# depths>=4r+4 in row q-r; p5..64, four sigma backgrounds, depth96.
# MS1 theorem control: common cells4r+4..p-1+r are checkerboard.
# MS2 unexpected: theorem only needs the following black window,
# not periodicity; random wall before/after that window, q1..6,
# p=3q+5, eight backgrounds each, compare row0 through64.
# CF must fail: extend to any r, dropping p>=3r+5; p8,q8,r8,
# all other sigma bits0, known C024 spreading, depth160.
# REFUTED-BY: MS0-MS2 fail or CF not rejected. No global gap prediction.
# OUTCOME multistep 2026-10-06 07:44 BST: exit0, ALL MULTISTEP
# CONTROLS PASS. MS0/MS1:2520 comparisons p5..64, four backgrounds,
# all allowed r, depth96; MS2:48 nonperiodic-background comparisons,
# q1..6, eight backgrounds each, depth64. Seed2026100614.
# CF unrestricted-r rejected at changed depth36, p8,q8,r8, cutoff35.
