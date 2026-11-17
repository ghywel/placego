#!/usr/bin/env python3
"""Recheck the L1531 line 'letters forced from width 29': closure of the AB windows at widths 24..46, whether every window has one next letter, and whether every window keeps AB for the next 12 ticks along every path."""
import json
from reachlib import *
from clos import nxt,graph
S=json.load(open('lock45.json'))
wins=[sum(b<<i for i,b in enumerate(v)) for v in S]
for w in list(range(24,46)):
    st={v>>(45-w) for v in wins}
    g=graph(st,w,cap=200000)
    L={v:let(v,w) for v in g}
    split=sum(1 for v in g if len({L[u] for u in g[v]})>1)
    sameAB=sum(1 for v in g if all(L[u]!=L[v] for u in g[v]))
    print(w,'closure',len(g),'letters',''.join(sorted(set(L.values()))),'windows with two next letters',split,'windows whose next letters all differ from theirs',sameAB,'of',len(g))
