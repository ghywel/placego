# N_t(W): distinct rows at tick t among rows of exact width W, deduplicated every 32 ticks. Exact integers.
import sys,collections,time
sys.path.insert(0,'tests/probes/swarm/sw02/amplifier')
from sector_test import Sect
def F(y): return (y>>1)^(y|(y<<1))
TMAX=int(sys.argv[2]); S=Sect(448)
for W in map(int,sys.argv[1].split(',')):
    ys=list(range(1<<(W-1),1<<W)); sec={}
    for y in ys: sec[y]=S.iota(y)
    t=0; last=0; log=[]; nextp=64
    lab=dict(sec)  # row -> sector, carried forward; a two-sector merge would be a bug
    bad=0; t0=time.time()
    while t<TMAX:
        nxt={}
        for y,i in lab.items():
            z=y
            for _ in range(32): z=F(z)
            if z in nxt and nxt[z]!=i: bad+=1
            nxt[z]=i
        if len(nxt)<len(lab): last=t+32
        lab=nxt; t+=32
        if t>=nextp:
            log.append((t,len(lab))); nextp*=2
    h=collections.Counter(lab.values())
    print('W',W,'N_t',log,'last merge by tick',last,'two-sector merges',bad,'sectors at end',len(h),'per sector',sorted(h.values()),'sec',round(time.time()-t0,1),flush=True)
    # damage between two unmerged rows of one sector
    by=collections.defaultdict(list)
    for y,i in lab.items(): by[i].append(y)
    fr=[]
    for i,g in by.items():
        for a,b in zip(g,g[1:]):
            d=a^b; lo=(d&-d).bit_length()-1; hi=d.bit_length()-1
            fr.append((hi/t,lo))
    if fr:
        fr.sort(); print('   damage top / t: min',round(fr[0][0],4),'median',round(fr[len(fr)//2][0],4),'max',round(fr[-1][0],4),'pairs',len(fr),'row width / t',round((W+t)/t,4),flush=True)
