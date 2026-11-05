#!/usr/bin/env python3
"""wall_replay.py (Local, L1529): independent replay of the exact wall language for short words, in absolute cell positions with whole-row big-integer steps.
A word w_0 .. w_(L-1), in backward order, is tested by search on the row of its last letter: cells below the window are chosen one at a time, the forward rows are recomputed by the
plain map on the known cells, and each forward window is compared wherever it is known. This shares nothing with wall_exact.c but the definition of the two words."""
import sys
A=[0,0,1,1,1,1,0,0,0,1,1]; B=[0,1,0,1,1,1,0,0,0,1,1]
WORD={'A':A,'B':B}
def forward_known(bits,lo):
    """bits: dict-free list of known cells at positions lo..lo+n-1; returns (list, lo+2) for one step"""
    return [bits[i+2]^(bits[i+1]|bits[i]) for i in range(len(bits)-2)],lo+2
def feasible(word):
    L=len(word)
    deep=WORD[word[-1]]
    P=1000                      # position of the window's first cell on the deepest row
    rain=[]; b=deep[-1]
    for i in range(10):
        b^=1; rain.append(b)
    Kmax=5*(L-1)
    sys.setrecursionlimit(10000)
    nodes=[0]
    def check(cells):
        """cells: known cells of the deepest row from P-len(low) up"""
        lo=P-(len(cells)-11-len(rain)); row=cells
        for s in range(1,L):
            row,lo=forward_known(row,lo)
            if len(row)==0: break
            want=WORD[word[L-1-s]]; p=P-3*s
            for i in range(11):
                q=p+i-lo
                if 0<=q<len(row) and row[q]!=want[i]: return False
        return True
    def rec(cells,left):
        nodes[0]+=1
        if not check(cells): return False
        if left==0: return True
        return rec([0]+cells,left-1) or rec([1]+cells,left-1)
    return rec(deep+rain,Kmax),nodes[0]
if __name__=='__main__':
    for w in sys.argv[1:]:
        print(w,feasible(w),flush=True)
