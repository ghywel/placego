#!/usr/bin/env python3
"""GC1028: exact nine-bit target, preregistered in RULE30-GPT.
Record searched: train/0111 + nine/width15 -> GC1018 only, not this predicate.
Prediction: gates0,0,1 at offsets0,4,8 exactly generate the twelve-car exit.
Control: literal shrinking cone versus packed reduced and full-slab updates.
Counterfactual: farther input changes the gate by8; finite speed forbids it.
Unexpected check: prefix-state membership must explicitly include the slab.
No SAT membership, prefix enumeration or all-depth claim.
OUTCOME:39 target words, exactly the four pattern classes retained below;
all512 local cases and1024 full-slab comparisons pass.
"""

def literal_gate(word):
    row = list(map(int,word))
    out = []
    for t in range(9):
        out.append(row[0])
        p = [int(t % 4 != 0)] + row
        row = [(30 >> (4*p[j]+2*p[j+1]+p[j+2])) & 1
               for j in range(len(row)-1)]
    return tuple(out[t] for t in (0,4,8))


def packed_gates(word, tail):
    r = sum(int(b)<<j for j,b in enumerate(word)) | (tail<<9)
    out = []
    for t in range(9):
        out.append(r & 1)
        r = ((r<<1) | int(t%4 != 0)) ^ (r | (r>>1))
    return tuple(out[t] for t in (0,4,8))


def main():
    target = []
    for bits in range(512):
        word = ''.join(str((bits>>j)&1) for j in range(9))
        gates = literal_gate(word)
        assert packed_gates(word,0) == gates == packed_gates(word,255)
        if gates == (0,0,1):
            target.append(word)
        for tail in (0,255):
            r = 25 | (bits<<6) | (tail<<15)  # six-cell slab100110
            trace = []
            for t in range(17):
                trace.append(r&1)
                r = ((r<<1) | (t%2)) ^ (r | (r>>1))
            # prefix from car9 at62: four cars then0, through78
            assert (tuple(trace[::2]) == (1,0,1,0,1,0,1,0,0)) == (gates == (0,0,1))
    patterns = {w for w in (format(i,'09b') for i in range(512))
                if w.startswith(('01101','01110','0111100'))
                or (w.startswith('0111111') and w[-2:] != '00')}
    assert set(target) == patterns and len(target) == 39
    print('PASS:512 literal cones, both far-tail controls,1024 full-slab traces')
    print('target count:',len(target))
    print('target words:',','.join(sorted(target)))

if __name__ == '__main__':
    main()
