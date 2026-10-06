#!/usr/bin/env python3
"""Finite adaptive waiting debt and all-branch small-period trees (GPT G7).
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_waiting.py
RUN-ON: GPT Intel CPU, one process, Python 3.10+ standard library.
COST: seconds; no Local million-side run, no large seed search.
Built on G2/G6 and Local's Lemma B2; no claim of an asymptotic front theorem.

PRE-REGISTERED 2026-10-06 before first run:
 WT0 control: the G2 certified period-16 prefix's phase-zero front ends at
     107308. Its nonwhite-step plus zero-wait identity is exact.
 WT1 blind: over every interval of that one-phase front, excess over slope 3
     is at most 2P=32. Report the maximizing interval regardless of verdict.
 WT2 blind: excess over slope 5/2 is at most 4P=64 on every such interval.
 WT3 control: every scanned nonempty zero wait has equal parent bits at all
     but its last transition, which has different parents (G6.2).
 CF counterfactual must fail: every interval has slope at most 2; the known
     endpoint already has positive excess, and the interval checker must see it.
 WT4 unexpected check: enumerate ALL period-dividing-P word extensions from
     edge pair (0, all-black), for P=1,2,3,4,8. No pair may recur on any path
     or across distinct branches. Maximum last diagonal must be 2,7,2,28,399.
     Every child's unique predecessor must be its actual parent pair.
 WT5 independent control: for P<=4, enumerating all candidate next words
     agrees with scalar recurrence construction at every reachable node.
REFUTED-BY: WT0/WT3/WT4/WT5 failure; CF not rejected; interval debts above
WT1/WT2 thresholds. Keep blind failures and maximizing witnesses.
OUTCOME pending; append results without changing predictions.
"""
from rule30_gpt_cycles import bit, classify, certified, rows, output_word
from rule30_gpt_front import front


def debt(times, numerator, denominator):
    minimum, at = 0, 0
    best, interval = 0, (0,0)
    for k,t in enumerate(times):
        value=denominator*t-numerator*k
        if value-minimum > best:
            best,interval=value-minimum,(at,k)
        if value < minimum:
            minimum,at=value,k
    return best,interval


def children(a,b,p):
    result=set()
    for initial in (0,1):
        word,end=output_word(a,b,p,initial)
        if end==initial:
            result.add(word)
    return sorted(result)


def advance(w,p):
    return (w >> 1) | ((w & 1) << (p-1))


def tree(p):
    mask=(1<<p)-1
    stack=[(0,mask,0)]
    seen=set(); maxdepth=0; leaves=0; okay=True; brute=True
    while stack:
        a,b,k=stack.pop()
        assert (a,b) not in seen, ('pair collision',p,k,a,b)
        seen.add((a,b)); maxdepth=max(maxdepth,k)
        choices=children(a,b,p)
        if p<=4:
            exact=[c for c in range(1<<p) if advance(c,p)==(a ^ (b | c))]
            brute &= choices==exact
        leaves += not choices
        for c in choices:
            previous=advance(c,p) ^ (b | c)
            okay &= previous==a
            stack.append((b,c,k+1))
    return len(seen),maxdepth,leaves,okay,brute


def main():
    control=[];blind=[]
    def check(name,okay,detail,isblind=False):
        status=('HELD' if okay else 'REFUTED') if isblind else ('PASS' if okay else 'FAIL')
        print(status+' '+name+': '+detail,flush=True)
        (blind if isblind else control).append(okay)
    words,p,_,_,_=classify(53208)
    times=[ts[0] for ts in front(words,p)]
    zero_sum=0;white=0;okay=True;waits=0;transitions=0
    for k,w in enumerate(words[:-1]):
        if not w:
            white+=1;continue
        z=times[k+1]-times[k]-1
        zero_sum+=z
        if not z:continue
        waits+=1
        a=words[k-2] if k>=2 else 0
        b=words[k-1] if k>=1 else 0
        for j in range(z):
            equal=bit(a,times[k]+j,p)==bit(b,times[k]+j,p)
            okay &= equal == (j<z-1)
            transitions+=1
    check('WT0', times[-1]==107308 and times[-1]==len(times)-1-white+zero_sum
          and certified(rows(words,p),len(words)),
          'final %d; steps %d; white parents %d; waiting zeros %d' %
          (times[-1],len(times)-1,white,zero_sum))
    check('WT3',okay,'nonempty waits %d; parent comparisons %d' % (waits,transitions))
    for name,num,den,threshold in [('WT1',3,1,32),('WT2',5,2,64)]:
        amount,(a,b)=debt(times,num,den)
        check(name,amount<=threshold*den,
              'max debt %s at [%d,%d]; elapsed %d; span %d; threshold %d' %
              (amount/den,a,b,times[b]-times[a],b-a,threshold),True)
    amount,interval=debt(times,2,1)
    check('CF rejected',amount>0,'slope-2 max debt %d at %s; endpoint debt %d' %
          (amount,interval,times[-1]-2*(len(times)-1)))
    data=[]
    for q,expected in [(1,2),(2,7),(3,2),(4,28),(8,399)]:
        count,last,leaves,back,brute=tree(q)
        data.append((q,count,last,leaves,back,brute))
        check('WT4 period %d'%q,back and last==expected and count<4**q,
              'nodes %d; last diagonal %d; leaves %d; predecessor %s' %
              (count,last,leaves,back))
    check('WT5',all(d[-1] for d in data),'all candidate words at every P<=4 node')
    print('ALL CONTROLS PASS' if all(control) else 'CONTROL FAILURE',flush=True)
    return not all(control) or not all(blind)

if __name__=='__main__':
    raise SystemExit(main())
