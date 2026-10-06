#!/usr/bin/env python3
"""G27: FS1 binary-index DFAO vs G26 formula; FS2 leading-zero invariance.
CF: aperiodicity prohibits every finite-state representation (false).
OUTCOME: FS1=65536, FS2=9216, FS3=32 seeds/256 words pass; counterfactual rejected.
No CA simulation or right-compatibility claim. Preregistered before execution.
"""
# States S, A, B. Initial S; outputs1,0,1 respectively.
TRANS=((0,1),(2,2),(1,1)); OUT=(1,0,1)

def evaluate(digits):
    state=0
    for digit in digits:state=TRANS[state][int(digit)]
    return OUT[state]

def scalar(row, wall):
    ext=[wall]+row+[0]
    return [(210>>(4*ext[j+2]+2*ext[j+1]+ext[j]))&1 for j in range(len(row)-1)]

def classification():
    from rule30_gpt_210_audit import inverse, backwards
    for seed in range(32):
        initial=[int(j%2==1 and ((seed>>((j-1)//2))&1)) if j<=9 else 0 for j in range(1,43)]
        row=initial[:];sig=[]
        for t in range(32):
            assert all(not x for j,x in enumerate(row,1) if (t+j)%2==0)
            assert t%2==0 or row[0]==0
            sig.append(1-row[0] if t%2==0 else 0)
            row=scalar(row,t%2)
        tau=[t%2 for t in range(33)]
        assert inverse(tau,sig+[0],32)==initial[:32]
        assert backwards(tau,sig+[0],32)==initial[:32]
    for word in range(256):
        tau=[t%2 for t in range(17)]
        sig=[(word>>(t//2))&1 if t%2==0 else 0 for t in range(17)]
        row=inverse(tau,sig,16)
        assert row==backwards(tau,sig,16)
        assert all(row[j-1]==0 for j in range(2,17,2))
        for t in range(16):
            assert t%2==0 or row[0]==0
            if t%2==0:assert 1-row[0]==sig[t]
            row=scalar(row,t%2)
    bad=[0,1]+[0]*10
    assert scalar(bad,0)[0]==1
    print('FS3 PASS all32 odd-depth seeds and256 inverse visible words; even-depth control rejected')

def main():
    for n in range(65536):
        expected=1 if n==0 else (n.bit_length()-1)%2
        assert evaluate(format(n,'b'))==expected
    checks=0
    for n in range(1024):
        word=format(n,'b');expected=evaluate(word)
        for padding in range(9):
            assert evaluate('0'*padding+word)==expected;checks+=1
    print('FS1 PASS all65536 indices; FS2 PASS all',checks,'padded words')
    classification()
    print('CF REJECTED: G26 aperiodic word has this three-state indexed representation')

if __name__=='__main__':main()
