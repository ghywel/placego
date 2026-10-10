"""Reuse GC686/L380 to guard SLC against impossible pure-power cuts.
No new orbit search; certificates are independently replayed literally.
"""
CERTS = ((84, 6, 0x688eb74a45efb082671ee, '100'),
         (155, 10, 0x35409b1caa645d715104db5291a2fe8415260ce, '10000'))
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)

def check(n, period, seed, visible):
    initial = [(seed >> i) & 1 for i in range(n)]
    row = initial[:]
    observed = ''
    for t in range(period):
        if row[0] != t % 2:
            return False
        if t % 2 == 0:
            observed += str(row[1])
        row = [TABLE[4*row[(i-1)%n]+2*row[i]+row[(i+1)%n]]
               for i in range(n)]
    return row == initial and observed == visible

def pure_factor(w):
    """Whether w belongs to either actual pure periodic factor language."""
    return any(all(b == cycle[(i+offset)%len(cycle)] for i,b in enumerate(w))
               for cycle in ('001','00001') for offset in range(len(cycle)))

if __name__ == '__main__':
    for n,p,seed,w in CERTS:
        assert check(n,p,seed,w)
        assert not check(n,p,seed ^ 1,w)
        for offset in range(len(w)):
            sample=''.join(w[(i+offset)%len(w)] for i in range(81))
            assert pure_factor(sample)
    assert not pure_factor('100100001')
    print('84/155-cell literal certificates and all visible rotations PASS')
    print('Mutated-wall and mixed-gap controls PASS; pure-power cuts are invalid')
