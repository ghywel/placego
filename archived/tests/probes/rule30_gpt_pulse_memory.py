"""G110 PM1 predictions published throughf922142 before execution.
PASS:128 words; both current-bit bins split8 versus56 by past error.
128 fair initial words; isolated pulse, literal updates to tick3.
Current K2=(ideal bit,0), past E1 predicts E3; bins8 versus56.
Both marginal four-sample laws uniform despite pair memory.
"""
from collections import Counter
from itertools import product
from rule30_gpt_error_echo import sync,truth


def traces(old):
    a=sync(old)
    b=dict(a)
    b[0]=truth(old[-1],old[0],a[1])
    ideal=[old[0],a[0]]
    noisy=[old[0],b[0]]
    for _ in range(2):
        a,b=sync(a),sync(b)
        ideal.append(a[0])
        noisy.append(b[0])
    return tuple(ideal),tuple(noisy)


def main():
    table=Counter()
    ih,jh=Counter(),Counter()
    for word in product((0,1),repeat=7):
        old=dict(zip(range(-3,4),word))
        i,j=traces(old)
        e=tuple(a^b for a,b in zip(i,j))
        indicator=(1-old[0])*(1-old[1])*old[2]
        assert e==(0,indicator,0,indicator)
        twin=dict(old)
        twin[-2]^=1
        ii,jj=traces(twin)
        assert ii[2]==1-i[2]
        assert (ii[1]^jj[1])==indicator
        table[i[2],e[2],e[1],e[3]]+=1
        ih[i]+=1
        jh[j]+=1
    expected={(b,0,0,0):56 for b in (0,1)}
    expected.update({(b,0,1,1):8 for b in (0,1)})
    assert table==expected
    assert len(ih)==len(jh)==16 and set(ih.values())==set(jh.values())=={8}
    for b in (0,1):
        assert table[b,0,1,1]==8 and table[b,0,1,0]==0
        assert table[b,0,0,0]==56 and table[b,0,0,1]==0
    print('PM1 PASS:128 initial words; exact current/past/next-error table',dict(table))
    print('Both marginal traces uniform; first-order paired-state Markov equality REFUTED in both bins')


if __name__=='__main__':
    main()
