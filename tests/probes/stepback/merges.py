#!/usr/bin/env python3
"""merges.py (Local, step back, 5 Nov 2026): finite rows merge under F(Y) = (Y>>1) ^ (Y | (Y<<1)). Distinct rows left after s ticks from all rows of exact width W."""
import numpy as np
for W in (16,20):
    S=np.arange(1<<(W-1),1<<W,dtype=np.uint64); out=[]
    for s in range(1,31):
        S=np.unique((S>>np.uint64(1))^(S|(S<<np.uint64(1)))); out.append(len(S))
    print('W',W,'start',1<<(W-1),'distinct after s ticks',out)
