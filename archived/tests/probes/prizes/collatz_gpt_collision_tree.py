"""G88 CB1-CB2, preregistered in this publication before running.
CB1 exact tree/direct comparison, admitted a=3..8, displacement4;
all observed prefix extrema independently checked. Unexpected positive
control: unrestricted t9,a2,displacement28, full direct/tree agreement.
CB2 BLIND: no admitted a21 collision, displacement4; 100000 nodes,5s.
A cap is incomplete, never an exclusion. No a22 or large population run.
OUTCOME: CB1 passes six direct comparisons and 722 prefix extrema;
unrestricted control accepts three witnesses. CB2 complete in59 nodes,
30 pruned, no leaves: blind HELD. Separate residue-cover audit pending.
"""
from collections import defaultdict
from time import monotonic


def evolve(n, t):
    bits, states, a = [], [n], 0
    for _ in range(t):
        b = n % 2
        bits.append(b)
        a += b
        n = (3*n+1)//2 if b else n//2
        states.append(n)
    return tuple(bits), states, a


def admitted(bits):
    a = 0
    for s,b in enumerate(bits,1):
        a += b
        if 3**a < 2**s:
            return False
    return True


def limits(a,t,s,j,B,restricted):
    k = a-j
    if k < 0 or k > t-s:
        return None
    scale = 3**k
    lo = scale*B+2**s*(scale-2**k)
    positions = ((3**i).bit_length()-1 for i in range(j,a)) if restricted else range(t-k,t)
    hi = scale*B+sum(3**(a-1-i)*2**p for i,p in zip(range(j,a),positions))
    return lo,hi


def tree(a,t,delta,restricted,cap=100000,seconds=5,cuts=None):
    A = 3**a
    stack = [(0,0,0,0,0,0)]  # s,r,j_low,j_high,B_low,B_high
    out = set()
    nodes = pruned = leaves = 0
    deadline = monotonic()+seconds
    while stack:
        if nodes >= cap or monotonic() >= deadline:
            return dict(complete=False,nodes=nodes,pruned=pruned,leaves=leaves,witnesses=sorted(out))
        s,r,j,k,B,C = stack.pop()
        nodes += 1
        if restricted and (3**j < 2**s or 3**k < 2**s):
            pruned += 1
            if cuts is not None:
                cuts.append((s,r))
            continue
        left,right = limits(a,t,s,j,B,restricted),limits(a,t,s,k,C,restricted)
        if left is None or right is None or not left[0]-right[1] <= delta*A <= left[1]-right[0]:
            pruned += 1
            if cuts is not None:
                cuts.append((s,r))
            continue
        if s == t:
            leaves += 1
            assert j == k == a and B-C == delta*A
            out.add(r)
            continue
        for lift in (1,0):
            rr = r+lift*2**s
            low,high = 3**j*rr+B,3**k*(rr+delta)+C
            assert low % 2**s == high % 2**s == 0
            b,c = (low//2**s)%2,(high//2**s)%2
            stack.append((s+1,rr,j+b,k+c,3**b*B+b*2**s,3**c*C+c*2**s))
    return dict(complete=True,nodes=nodes,pruned=pruned,leaves=leaves,witnesses=sorted(out))


def direct(a,t,delta,restricted,check_bounds=False):
    groups = defaultdict(list)
    witnesses = set()
    M = 2**t
    for r in range(M):
        n = r+2*M
        bits,x,j = evolve(n,t)
        other,y,k = evolve(n+delta,t)
        alive = not restricted or admitted(bits)
        if j == a and alive and check_bounds:
            B = M*x[-1]-3**a*n
            for s in range(t+1):
                prefix = bits[:s]
                odd = sum(prefix)
                offset = 2**s*x[s]-3**odd*n
                groups[(s,prefix,odd,offset)].append(B)
        if j == k == a and x[-1] == y[-1] and alive and (not restricted or admitted(other)):
            witnesses.add(r)
    for (s,prefix,j,B),values in groups.items():
        assert limits(a,t,s,j,B,restricted) == (min(values),max(values))
    return witnesses,len(groups)


def main():
    checks = 0
    for a in range(3,9):
        t = (3**a).bit_length()-1
        expected,groups = direct(a,t,4,True,True)
        got = tree(a,t,4,True)
        assert got['complete'] and set(got['witnesses']) == expected
        checks += groups
    expected,groups = direct(2,9,28,False,True)
    positive = tree(2,9,28,False)
    assert positive['complete'] and expected and set(positive['witnesses']) == expected
    checks += groups
    print('CB1 PASS six admitted direct/tree comparisons;',checks,'attained prefix extrema')
    print('Unexpected unrestricted positive control:',positive)
    a,t = 21,(3**21).bit_length()-1
    result = tree(a,t,4,True)
    for r in result['witnesses']:
        n = r+2*2**t
        low,x,j = evolve(n,t)
        high,y,k = evolve(n+4,t)
        assert j == k == a and x[-1] == y[-1] and admitted(low) and admitted(high)
        assert n.bit_length() == (n+4).bit_length()
        print('Verified witness starts/terminal:',n,n+4,x[-1])
    print('CB2',result)
    print('BLIND', 'INCOMPLETE' if not result['complete'] else 'REFUTED' if result['witnesses'] else 'HELD')
    print('No all-a theorem or prize claim; independent review required')


if __name__ == '__main__':
    main()
