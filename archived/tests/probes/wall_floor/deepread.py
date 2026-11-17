#!/usr/bin/env python3
"""deepread.py (Local, L1534): what the deep period-6 words are: where they part from the AAB lock's strip, and where reset words sit in all six phases."""
import json
L=[l.strip() for l in open('deep6.txt')]
S=json.load(open('lock136.json'))
K=len(L[0])
def isF(c): return c[0]==0 and c[1]!=c[2] and c[3]==1 and c[5]==1 and c[6]==0 and c[8]==0 and c[9]==1
def off(word):
    """cells by offset from the wall: word is low..high"""
    return word[::-1]
lock=[off(s) for s in S]
for wi in range(0,18,6):
    ph=[off(L[wi+p]) for p in range(6)]
    # agreement with the lock strip by phase
    ag=[]
    for p in range(6):
        best=max(range(6),key=lambda i:next((k for k in range(136) if ph[p][k]!=lock[i][k]),136))
        ag.append(next((k for k in range(136) if ph[p][k]!=lock[best][k]),136))
    print('word',wi//6,'agrees with the lock down to offset',ag)
    # period 3 in the cells: first offset where phase p and p+3 differ
    d=[next((k for k in range(K) if ph[p][k]!=ph[p+3][k]),K) for p in range(3)]
    print('  first offset where the word is not period 3:',d)
    # columns: all-black, reset sites common to the six phases
    sites=[]
    for k in range(10,K-1):
        # a reset word with its low end at offset k: cells offsets k, k-1, ..., k-9
        if all(isF([1 if ph[p][k-i]=='#' else 0 for i in range(10)]) for p in range(6)): sites.append(k)
    print('  offsets where all six phases have a reset word (low end):',sites[:30])
    per=[]
    for k in range(10,K-1):
        n=sum(isF([1 if ph[p][k-i]=='#' else 0 for i in range(10)]) for p in range(6))
        if n>=3: per.append((k,n))
    print('  offsets with at least three:',per[:30])
