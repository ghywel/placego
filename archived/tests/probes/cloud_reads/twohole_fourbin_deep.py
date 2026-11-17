"""CL500: two-hole four-bin exceptions at least margin >= 3 all have two equal-size bins with equal targets. OUTCOME: M=13 3333: 90 of 90; M=14 3334: 60 of 60."""
import sys
from collections import Counter
sys.argv=['x']
exec(open('/home/user/placego/tests/probes/cloud_reads/twohole_fourbin.py').read().rsplit("\nif __name__ == '__main__':",1)[0])
for M,C in ((13,(3,3,3,3)),(14,(3,3,3,4))):
    cnt, exc = run(M, C)
    deep=[(h,t,m) for h,t,m in exc if m>=3]
    rep=sum(1 for h,t,m in deep if any(t[i]==t[j] and C[i]==C[j] for i in range(4) for j in range(i+1,4)))
    print(M, C, 'spec', cnt['spec'], 'infeasible by margin', sorted((k[1],v) for k,v in cnt.items() if isinstance(k,tuple)), '| margin>=3:', len(deep), 'with a repeated (size,target):', rep)
    seen=set()
    for h,t,m in deep:
        key=(h,tuple(sorted(zip(C,t))))
        if key in seen: continue
        seen.add(key)
        if not any(t[i]==t[j] and C[i]==C[j] for i in range(4) for j in range(i+1,4)): print('   NO REPEAT:', h, sorted(zip(C,t)), m)
