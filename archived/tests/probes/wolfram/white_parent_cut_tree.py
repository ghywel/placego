"""Finite lag-16 decision tree between an exact aligned anchor and the seed's saturation wheel."""
import hashlib
import json
import os
from pathlib import Path
import struct

P, LOW, END = 16, 11998, 87867
FULL = (1 << P) - 1
INPUT_HASH = '28d6dc60a6157dc39a5d2c9e41bdee6bce00ab562d05ed821ea1c1a724cbae71'
OUT = Path(os.environ['CAPPED_OUT'])


def children(far, near):
    """Solve forward in time from each possible initial colour."""
    choices = []
    for initial in (0,1):
        x, word = initial, 0
        for t in range(P):
            word |= x << t
            x = ((far >> t) & 1) ^ (((near >> t) & 1) | x)
        if initial == x:
            choices.append(word)
    return choices


def verify(anchor, paths):
    """Read words spatially. Check cyclic identity and exhaustive branching, without the constructor."""
    if not paths or any(w[:2] != list(anchor) for w in paths):
        raise ValueError('anchor')
    stack = [(2,paths)]
    while stack:
        i, group = stack.pop()
        if LOW+i > END:
            if len(group)!=1 or len(group[0])!=i:
                raise ValueError('past end')
            continue
        far, near = group[0][i-2:i]
        if near == 0 and far.bit_count()%2:
            if len(group)!=1 or len(group[0])!=i:
                raise ValueError('odd parity closure')
            continue
        branches = {}
        for w in group:
            if len(w) <= i:
                raise ValueError('missing child')
            d = w[i]
            rhs = far ^ (near | d)
            if (((rhs << 1) & FULL) | (rhs >> (P-1))) != d:
                raise ValueError('false truth row')
            branches.setdefault(d,[]).append(w)
        if near == 0:
            if len(branches)!=2 or (min(branches)^max(branches))!=FULL:
                raise ValueError('missing complementary child')
        elif len(branches)!=1:
            raise ValueError('reset uniqueness')
        stack.extend((i+1,gs) for gs in branches.values())


def main():
    os.nice(10)
    raw = Path(os.environ['WHITE_SEED_CYCLE']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==INPUT_HASH
    size = (END+8)//8
    assert len(raw)==33*size
    rows = [raw[i*size:(i+1)*size] for i in range(33)]
    def word(k):
        return sum(((row[k//8] >> (k%8)) & 1) << t for t,row in enumerate(rows[:P]))
    anchor = (word(LOW),word(LOW+1))
    # A full clock is needed if time-shift equivalence is to be inferred.
    small = (1 << (LOW+2)) - 1
    assert len({int.from_bytes(row,'little') & small for row in rows[:P]})==P
    stack = [([],list(anchor))]
    leaves = []
    while stack:
        history, words = stack.pop()
        while LOW+len(words)<=END:
            j=LOW+len(words)
            far, near=words[-2:]
            cs=children(far,near)
            if not cs:
                history=history+[[j,'no16',far.bit_count()]]
                break
            if len(cs)==2:
                stack.append((history+[[j,1,far.bit_count()]],words+[cs[1]]))
                history=history+[[j,0,far.bit_count()]]
            words.append(cs[0])
        leaves.append((history,words))
    paths=[w for _,w in leaves]
    verify(anchor,paths)
    # Negative controls: remove a complete lawful branch; corrupt a transition;
    # insert a 16-word at the odd leaf. Each must be refused.
    odd=next(i for i,w in enumerate(paths) if LOW+len(w)==END)
    for name,mutant in [('missing',paths[:-1]),('truth',[w[:5]+[w[5]^1]+w[6:] if i==0 else w for i,w in enumerate(paths)]),
                        ('odd',[w+[0] if i==odd else w for i,w in enumerate(paths)])]:
        try:
            verify(anchor,mutant)
        except ValueError as e:
            print('negative',name,str(e))
        else:
            raise AssertionError('accepted '+name)
    seed_words=[word(k) for k in range(LOW,END+1)]
    index=[]
    for i,(history,w) in enumerate(leaves):
        miss=next((LOW+j for j,(a,b) in enumerate(zip(w,seed_words)) if a!=b),None)
        blob=struct.pack('<'+'H'*len(w),*w)
        filename=f'leaf-{i}.u16le'
        (OUT/filename).write_bytes(blob)
        index.append(dict(branch=history,end=LOW+len(w)-1,first_difference=miss,
                          file=filename,sha256=hashlib.sha256(blob).hexdigest()))
    summary={'anchor_words':anchor,'first_index':LOW,'last_index':END,'paths':index}
    (OUT/'tree.json').write_text(json.dumps(summary,indent=2)+'\n')
    assert len(paths)==4 and sum(LOW+len(w)==END for w in paths)==1
    assert index[odd]['first_difference'] is None
    print('WHITE_PARENT_TREE_DONE')


if __name__=='__main__':
    main()
