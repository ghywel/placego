#!/usr/bin/env python3
import sys
exec(open('twopair_robust.py').read().split("for w in range(6,23):")[0])
w=int(sys.argv[1])
a=run(w)
with open(f'B{w}.txt','w') as f:
    for x in a:
        m=0
        for i,b in enumerate(x): m|=b<<i
        f.write(f'{m}\n')
print(w,len(a))
