#!/usr/bin/env python3
"""tailcheck.py (Local, L1543): e_m from the time-reversed estimate against |U| 2^(10-K) 8^m P(arrival > m), with arrivals sampled directly."""
import re,math
blocks=open('arrive_all.out').read().split('samples ')[1:]
sets=[('AB 45',4,45,'entry45.out',0.8124),('AAB 136',6,136,'run_entry3/out.txt',0.8131),('third 175',40,175,'run_entry2/out.txt',1.0)]
for (name,U,K,f,exitfrac),b in zip(sets,blocks):
    n=int(b.split()[0])
    h={int(a):int(c) for a,c in re.findall(r' (\d+):(\d+)\(',b.split('arrival row')[1])}
    tot=sum(h.values())
    e={}
    for l in open(f):
        m=re.match(r'(\d+) (-?[\d.]+) ([\d.e+-]+) ',l)
        if m: e[int(m.group(1))]=float(m.group(3))
    row=[]
    for mm in sorted(e):
        tail=sum(c for a,c in h.items() if a>mm)/tot
        if tail==0: continue
        pred=U*2.0**(10-K)*8.0**mm*tail*exitfrac
        row.append(f'{mm}: {e[mm]:.2e} / {pred:.2e}')
    print(name,'m: estimate / formula:',' | '.join(row[-9:]))
    print('   mean arrival',round(sum(a*c for a,c in h.items())/tot,2),'cells per tick',round((K-11)/(sum(a*c for a,c in h.items())/tot),2))
