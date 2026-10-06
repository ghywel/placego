#!/usr/bin/env python3
"""Check G9's birth-restart transfer, not a new large Rule 30 search.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_birth_restart.py
RUN-ON: GPT Intel CPU, one process, Python 3.10+ standard library.
COST: seconds; no stored arrays and no Local million-diagonal job.
PREDICTIONS before first run, 2026-10-06:
 BR0 control: scalar next-black scans reproduce waiting-table evaluation.
 BR1 theorem control: the birth front equals the maximum of unclamped
     fronts started at the initial time or EACH preceding birth barrier.
 BR2 theorem control: if every unclamped interval and starting phase has
     excess above slope 5/2 at most C, births b_j<=j preserve T_k<=5k/2+C.
     Compute exact doubled C independently over all intervals and phases.
 BR3 unexpected check: BR1/BR2 also hold for odd period7 and a barrier
     that drops to zero between indices divisible by3; monotone births
     are not needed. Test 24 seeded word lists per P=1,2,3,4,7,8, length24.
 CF must reject: an endpoint bound only on the original phase suffices.
     Four white words followed by word1 at P16 have original front1 but
     birth front17 at five edges, above slope5/2 with endpoint debt0.
 REFUTED-BY: any scalar/restart equality or all-interval transfer fails;
     CF not rejected. Random lists need not be Rule30 compatible: this
     generic monotone-map theorem does not require compatibility.
OUTCOME 2026-10-06 06:26 BST: exit0, ALL CONTROLS PASS.
 BR0-BR3 PASSED: 57600 comparisons, by P=1,2,3,4,7,8:
 2304,4608,6912,9216,16128,18432. Largest doubled interval debt21.
 Odd P7 and decreasing barriers passed. No blind prediction was made.
 CF REJECTED: original1, born17, wrong endpoint-only bound25/2.
 Generic-map diagnostic; the actual finite-period consequence uses G8's
 exact edge certificate and G9's proof, not sampled incompatible words.
"""
import random
from rule30_gpt_front import waiting


def scalar_step(word,p,time):
    if not word:return time
    while not ((word>>(time%p))&1):time+=1
    return time+1


def apply_interval(words,p,a,b,start):
    time=start
    for word in words[a:b]:time=scalar_step(word,p,time)
    return time


def all_interval_debt(words,p):
    maximum=0
    for a in range(len(words)):
        for phase in range(p):
            time=phase
            for b in range(a+1,len(words)+1):
                time=scalar_step(words[b-1],p,time)
                maximum=max(maximum,2*(time-phase)-5*(b-a))
    return maximum


def check_list(words,p,barriers):
    tables=[waiting(w,p) for w in words]
    debt=all_interval_debt(words,p)
    comparisons=0
    for phase in range(p):
        time=phase
        for k,(word,barrier) in enumerate(zip(words,barriers),1):
            start=max(time,barrier+phase)
            updated=start+tables[k-1][start%p]
            assert updated==scalar_step(word,p,start)
            time=updated
            restarted=max([apply_interval(words,p,0,k,phase)]+
                [apply_interval(words,p,j,k,barriers[j]+phase) for j in range(k)])
            assert time==restarted,(p,k,phase,time,restarted)
            assert 2*(time-phase)<=5*k+debt,(p,k,phase,time,debt)
            comparisons+=1
    return comparisons,debt


def main():
    rng=random.Random(2026100609);comparisons=0;maximum=0
    for p in [1,2,3,4,7,8]:
        count=0
        for _ in range(24):
            words=[rng.randrange(1<<p) for _ in range(24)]
            for barriers in [[max(0,j+1-L) for j in range(24)] for L in [1,2,5]]+[
                    [j if j%3==0 else 0 for j in range(24)]]:
                n,debt=check_list(words,p,barriers)
                count+=n;maximum=max(maximum,debt)
        comparisons+=count
        print('PASS BR0-BR3 P%d: %d scalar/restart/bound comparisons'%(p,count),flush=True)
    words=[0]*4+[1];p=16
    original=apply_interval(words,p,0,5,0)
    born=0
    for j,w in enumerate(words):born=scalar_step(w,p,max(born,j))
    assert original==1 and born==17 and 2*born>5*len(words)
    print('PASS CF rejected: original1, born17, claimed bound25/2; words are a generic-map control',flush=True)
    print('PASS totals: %d comparisons; largest doubled all-interval debt %d'%(comparisons,maximum),flush=True)
    print('ALL CONTROLS PASS',flush=True)


if __name__=='__main__':main()
