"""GC375: finite guard for the hand-classified abstract increasing-zero-gap word.
Prediction: every length-n left-special factor starts at least B_floor((n-1)/2).
No Rule30 realizability or actual zero-run counterexample is claimed.
"""
import json


def main():
    w=''.join('1'+'0'*j for j in range(1,61))
    assert '11' not in w  # Unexpected: even this visible-bit necessary condition holds.
    results=[]
    for n in range(3,21):
        contexts={}; first={}
        for i in range(1,len(w)-n+1):
            f=w[i:i+n]
            contexts.setdefault(f,set()).add(w[i-1]); first.setdefault(f,i)
        special=[f for f,v in contexts.items() if len(v)==2]
        assert special
        a=(n-1)//2; bound=a*(a+1)//2
        earliest=min(first[f] for f in special)
        assert earliest>=bound
        assert all(f.count('1')<=1 for f in special)
        results.append(dict(length=n,earliest=earliest,bound=bound,special_count=len(special)))
    print(json.dumps(results,indent=2))

if __name__=='__main__': main()
