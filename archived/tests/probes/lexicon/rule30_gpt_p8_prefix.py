#!/usr/bin/env python3
"""GC932: fixed witnesses for GC878, not the full relaxed-language census.
Original prediction before execution: 00000->01,10000->10,01000->00 with zero outside.
FAIL retained: 00000 gives00. The first run stopped at that assertion.
Registered repair:32 starting states, fixed zero exterior, one macro only (256 steps).
Repair found exactly one01 witness:00010->10011. No 256-input macro census.
Two independent scalar updates; phase countercontrol; length1 count is2.
This does not run Lean or prove physical right-half language equality.
"""
TABLE=(0,1,1,1,1,0,0,0)


def step(s,w):
    row=(w,)+s+(0,)
    xor_or=tuple(row[i-1]^(row[i]|row[i+1]) for i in range(1,6))
    literal=tuple(TABLE[4*row[i-1]+2*row[i]+row[i+1]] for i in range(1,6))
    assert xor_or==literal
    return literal


def macro(s):
    for t in range(8):
        s=step(s,int(t!=0))
    return s


def main():
    z=(0,0,0,0,0)
    assert (z[0],macro(z)[0])==(0,0)  # retained failed original prediction
    candidates=[]
    for k in range(32):
        s=tuple((k>>i)&1 for i in range(5))
        if (s[0],macro(s)[0])==(0,1):candidates.append(s)
    assert candidates==[(0,0,0,1,0)]
    for s,pair in [(z,(0,0)),((1,0,0,0,0),(1,0)),(candidates[0],(0,1))]:
        m=macro(s);m2=macro(m)
        assert (s[0],m[0])==pair and m2[0]==0
        print(''.join(map(str,s)),pair,'macro states',m,m2)
    b=candidates[0]
    for _ in range(8):b=step(b,1)
    assert b[0]==0 and macro(candidates[0])[0]==1  # all-black phase cannot replace the white-first macro
    print('PASS repaired fixtures, 256-step selection, literal and phase controls; original prediction REFUTED')


if __name__=='__main__':main()
