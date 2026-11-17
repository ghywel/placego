"""G98 DC1-DC2: preregistered at5bb1aac; PASS 2026-10-06.
DC1: all integer diamonds T0..12, |X|<=T, reachability vs row counts.
DC2: padded seed through12, left edge -t; adjacent update orders differ.
Unexpected guard: T2,X0 inclusive count5, continuum area2.
No damage-speed survey or asynchronous statistical job.
"""


def descendants(points):
    return {x+d for x in points for d in (-1,0,1)}


def diamond(t, x):
    forward = [{0}]
    backward = [{x}]
    for _ in range(t):
        forward.append(descendants(forward[-1]))
        backward.append(descendants(backward[-1]))
    return sum(len(forward[s] & backward[t-s]) for s in range(t+1))


def truth(l,c,r):
    return (30 >> (4*l+2*c+r)) & 1


def evolve(black):
    lo,hi=min(black)-1,max(black)+1
    return {i for i in range(lo,hi+1)
            if truth(int(i-1 in black),int(i in black),int(i+1 in black))}


def sequential(order):
    black={1}
    for i in order:
        bit=truth(int(i-1 in black),int(i in black),int(i+1 in black))
        if bit:
            black.add(i)
        else:
            black.discard(i)
    return black


def main():
    cases=0
    for t in range(13):
        for x in range(-t,t+1):
            count=sum(max(0,min(s,x+t-s)-max(-s,x-t+s)+1)
                      for s in range(t+1))
            assert diamond(t,x)==count
            cases+=1
    assert diamond(2,0)==5 and (2**2-0**2)/2==2
    black={0}
    for t in range(13):
        assert min(black)==-t
        black=evolve(black)
    assert sequential((0,1))=={0}
    assert sequential((1,0))=={0,1}
    print('DC1 PASS:',cases,'diamonds; path reachability agrees with row count')
    print('Unexpected guard PASS: inclusive grid5 vs continuum area2')
    print('DC2 PASS: left edge -t through12; local orders give {0} vs {0,1}')


if __name__=='__main__':
    main()
