#!/usr/bin/env python3
"""GC974: boundary-only widening obstruction, not a physical clock witness.
Record searched: RRL/GC970 + prefix/suffix/widen/overapprox -> 5 hits;
boundary/prefix/suffix + widening/triangular/coefficient -> 50 hits, including
G18.4's known triangular dependence. New scope: GC970 boundary abstraction.
Prediction before execution: preserving the first and last m pair letters while
forgetting all middle letters admits C+1 consecutive white initial-row cells at
negative depths m..m+C. Test both phases, m=4,8,16, C=32. Construction uses
literal_image; verification independently inverts the Rule 30 truth table.
CF: flipping the last selected pivot must flip only that target among depths
through m+C. Unexpected: even the unused terminal right bit is preserved.
No claim of membership in the full clock language; that membership must fail.
OUTCOME: six constructions PASS, both phases and all three boundary sizes.
CF/U PASS; the full clock language rejects each relaxed construction.
"""
import rule30_rrl_transducer as t


def cell(word, depth, inverse=t.literal_image):
    for _ in range(depth):
        word=inverse(word)
    return word[0]//2


def table_inverse(word):
    out=[]
    for a,b in zip(word,word[1:]):
        centre,right=a//2,a%2
        target=b//2
        lefts=[left for left in (0,1)
               if ((30 >> (4*left+2*centre+right)) & 1)==target]
        assert len(lefts)==1
        out.append(2*lefts[0]+centre)
    return out


def run():
    for phase in (0,1):
        for m in (4,8,16):
            C=32
            n=2*m+C+1
            original=tuple(2*((i+phase)%2)+(i//2)%2 for i in range(n))
            assert t.accepted(t.initial(phase),original)
            candidate=list(original)
            for d in range(m,m+C+1):
                candidate[d] ^= 2*cell(candidate[:d+1],d)
            assert candidate[:m]==list(original[:m])
            assert candidate[-m:]==list(original[-m:])
            assert all(cell(candidate[:d+1],d,table_inverse)==0
                       for d in range(m,m+C+1))
            assert not t.accepted(t.initial(phase),candidate)
            flipped=candidate.copy(); flipped[m+C]^=2
            assert all(cell(flipped[:d+1],d,table_inverse)==0
                       for d in range(m,m+C))
            assert cell(flipped[:m+C+1],m+C,table_inverse)==1
            assert candidate[-1]%2==original[-1]%2
    print('6 boundary-preserving 33-white constructions PASS; CF/U PASS; full clock rejects')


if __name__=='__main__':
    run()
