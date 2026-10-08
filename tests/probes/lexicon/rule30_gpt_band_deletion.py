#!/usr/bin/env python3
"""Fixed GC549.19 deletion audit; preregistered in CLOUD-LOCAL before first run.
Prediction: all five zero equations are indispensable under no11/no101001.
Counterfactual: no11 alone rejects the full band (known false).
Unexpected check: use actual f14, not printed f14+f15, when deleting depth14.
Outcome: prediction REFUTED at depth13. Four zeros14..17 already force
010101001 among the 89 no11 words, hence f13=0; no hand certificate yet.
Other single deletions leave 8,3,5,1 relaxed words. No actual right census.
RUN: python3 tests/probes/lexicon/rule30_gpt_band_deletion.py
"""
from itertools import product
import rule30_gpt_gc549_certificate as p

def main():
    f=p.polynomials()
    words=[]
    for c in product((0,1),repeat=9):
        if any(c[i] and c[i+1] for i in range(8)):
            continue
        v=p.scalar_inverse(c)
        assert all(v[j]==p.evaluate(f[j],c) for j in range(13,18))
        words.append((''.join(map(str,c)),v))
    assert len(words)==89
    four=[w for w,v in words if all(v[j]==0 for j in range(14,18))]
    assert four==['010101001']
    relaxed=[(w,v) for w,v in words if '101001' not in w]
    counts=[]
    for dropped in range(13,18):
        survivors=[w for w,v in relaxed
                   if all(v[j]==0 for j in range(13,18) if j!=dropped)]
        counts.append(len(survivors))
        print('drop',dropped,'count',len(survivors),'first',survivors[:3])
    assert counts==[0,8,3,5,1]
    print('89 polynomial/scalar controls PASS; depth13 premise redundant computationally')

if __name__=='__main__':
    main()
