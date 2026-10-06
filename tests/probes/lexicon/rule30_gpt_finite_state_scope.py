#!/usr/bin/env python3
"""G27: FS1 binary-index DFAO vs G26 formula; FS2 leading-zero invariance.
CF: aperiodicity prohibits every finite-state representation (false).
OUTCOME: FS1=65536, FS2=9216 pass; counterfactual rejected.
No CA simulation or right-compatibility claim. Preregistered before execution.
"""
# States S, A, B. Initial S; outputs1,0,1 respectively.
TRANS=((0,1),(2,2),(1,1)); OUT=(1,0,1)

def evaluate(digits):
    state=0
    for digit in digits:state=TRANS[state][int(digit)]
    return OUT[state]

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
    print('CF REJECTED: G26 aperiodic word has this three-state indexed representation')

if __name__=='__main__':main()
