#!/usr/bin/env python3
"""Audit a waiting-potential domain: edge trees versus cyclic compatible words.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_local_front.py
RUN-ON: GPT Intel CPU, one process, Python 3.10+ standard library.
COST: seconds; max 65536 word-pair states. No million-diagonal run.
G7 supplies unique predecessor H; G6 supplies next-black clock maps.

PREDICTIONS written before first run, 2026-10-06:
 LF0 control: complete edge trees P=1,2,4,8 have 3,13,97,3065 nodes.
 LF1 blind: maximum interval debt above slope 5/2 on EVERY edge-tree path,
     with and without birth clamps, is at most 4P for these periods.
 LF2 control: every spatial word-pair cycle is directly locally compatible;
     every phase-loop average is an exact rational from a repeated phase.
 LF3 blind: all compatible spatial cycles at P=1,2,4,8 have asymptotic
     next-black front slope at most 5/2. This broader class has no left edge.
 LF4 blind: the same statement holds at unexpected odd common period 3.
 CF counterfactual: ignoring compatibility permits the constant single-bit
     period-4 word to have front slope 4. This must be detected, and the
     word must FAIL its constant-spatial-pattern Rule 30 equation.
 LF5 independent control: for P<=4, all pair cycles agree with an explicit
     bit-by-bit predecessor, and phase mean witnesses agree with scalar scans.
REFUTED-BY: controls failing, counterfactual not rejected, debt above 4P,
or any compatible-cycle mean above 5/2. Print exact witnesses on failure.
OUTCOME pending. Preserve predictions and append every verdict.
"""
from fractions import Fraction
from rule30_gpt_cycles import bit
from rule30_gpt_waiting import advance, children
from rule30_gpt_front import waiting


def edge_debt(p,birth):
    stack=[(0,(1<<p)-1,0,0,0)]
    seen=set();best=0;witness=None
    while stack:
        a,b,k,t,minimum=stack.pop()
        assert (a,b) not in seen
        seen.add((a,b))
        for c in children(a,b,p):
            start=max(t,k if birth else 0)
            nxt=start+waiting(b,p)[start%p]
            value=2*nxt-5*(k+1)
            excess=value-minimum
            if excess>best:
                best,witness=excess,(k+1,nxt,b,c)
            stack.append((b,c,k+1,nxt,min(minimum,value)))
    return len(seen),Fraction(best,2),witness


def predecessor(node,p):
    mask=(1<<p)-1
    a,b=node>>p,node&mask
    return ((advance(b,p) ^ (a | b))<<p) | a


def scalar_predecessor(node,p):
    mask=(1<<p)-1
    a,b=node>>p,node&mask
    previous=sum((bit(b,t+1,p) ^ (bit(a,t,p) | bit(b,t,p)))<<t for t in range(p))
    return (previous<<p)|a


def pair_cycles(p):
    done=set();cycles=[]
    for initial in range(1<<(2*p)):
        if initial in done:continue
        path=[];index={};node=initial
        while node not in done and node not in index:
            index[node]=len(path);path.append(node)
            node=predecessor(node,p)
        if node in index:
            cycles.append(list(reversed(path[index[node]:])))
        done.update(path)
    return cycles


def maximum_mean(words,p,scalar=False):
    tables={w:waiting(w,p) for w in set(words)}
    best=Fraction(-1);certificate=None
    for initial in range(p):
        time=initial;seen={};circuits=0
        while time%p not in seen:
            seen[time%p]=(circuits,time)
            for w in words:
                if scalar and w:
                    while not bit(w,time,p):time+=1
                    time+=1
                elif not scalar:
                    time+=tables[w][time%p]
            circuits+=1
        old_c,old_t=seen[time%p]
        mean=Fraction(time-old_t,(circuits-old_c)*len(words))
        if mean>best:
            best=mean
            certificate=(initial,circuits-old_c,time-old_t)
    return best,certificate


def main():
    controls=[];blind=[]
    def check(name,okay,detail,uncertain=False):
        print((('HELD' if okay else 'REFUTED') if uncertain else
               ('PASS' if okay else 'FAIL'))+' '+name+': '+detail,flush=True)
        (blind if uncertain else controls).append(okay)
    for p,expected in [(1,3),(2,13),(4,97),(8,3065)]:
        for birth in (False,True):
            nodes,amount,witness=edge_debt(p,birth)
            check('LF0 P%d birth%s'%(p,birth),nodes==expected,'nodes %d'%nodes)
            check('LF1 P%d birth%s'%(p,birth),amount<=4*p,
                  'max debt %s; witness (last,time,parent,child) %s'%(amount,witness),True)
    for p in [1,2,3,4,8]:
        cycles=pair_cycles(p);best=Fraction(-1);witness=None;valid=True;independent=True
        for cycle in cycles:
            valid &= all(predecessor(cycle[(i+1)%len(cycle)],p)==node
                         for i,node in enumerate(cycle))
            words=[node&((1<<p)-1) for node in cycle]
            mean,cert=maximum_mean(words,p)
            if mean>best:best,witness=mean,(cycle[0],len(cycle),cert)
            if p<=4:
                independent &= all(predecessor(node,p)==scalar_predecessor(node,p) for node in cycle)
                independent &= maximum_mean(words,p,True)==(mean,cert)
        check('LF2 P%d'%p,valid,'pair cycles %d; maximum exact mean %s; witness %s'%
              (len(cycles),best,witness))
        check(('LF4 unexpected' if p==3 else 'LF3')+' P%d'%p,best<=Fraction(5,2),
              'maximum %s vs 5/2'%best,True)
        if p<=4:check('LF5 P%d'%p,independent,'bit predecessor and scalar phase scans')
    false_mean,cert=maximum_mean([1],4)
    invalid=advance(1,4)!=(1 ^ (1 | 1))
    check('CF rejected',false_mean==4 and invalid,'single-bit repeated word slope %s; invalid %s; %s'%
          (false_mean,invalid,cert))
    print('ALL CONTROLS PASS' if all(controls) else 'CONTROL FAILURE',flush=True)
    return not all(controls) or not all(blind)

if __name__=='__main__':
    raise SystemExit(main())
