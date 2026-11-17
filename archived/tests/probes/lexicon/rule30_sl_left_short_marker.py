"""GC1107: nonlinear short-gap marker in the forced left half.

Missing inference: a same-history carrier of the recurrent S/L choices
on the left, rather than another affine explanation of record counts.
The new evidence is GC1106's explicit mixed M2/M3 output language.
Record searched: column.-12|depth12|twelfth|short.gap.*left|
left.*short.gap with S/L|renewal|forced|selector|gap ->5 hits4files;
GC1007's retained finite-forcing/pumping failure, GC706/784 read.
No existing twelfth-column S/L selector found in those sources.

Write q_s=x_1(2s), x_0(2s)=0. In synchronized S/L, q marks
renewals, so successive ones have distances3 or5. P1 BEFORE controls:
x_-12(2s)=q_(s+2)*q_(s+5), x_-12(2s+1)=q_(s+4) OR q_(s+6).
In fact the identities need only distance>=3 between ones.
P2: the marker at s+2 therefore selects S (1) versus L (0).
Counterfactual: the even formula is the affine XOR of the two bits;
a short gap, with both bits1, must refute that formula.
Independent controls: every length9 word with ones separated>=3;
the literal Rule30 eight-entry table on every reconstructed triangle;
all16 four-letter S/L words using the independently published h lift.
Unexpected check: allowing distance2 (still no11) must break at least
one identity. The separation premise cannot be silently weakened.
This is a local algebra certificate, not a record computation, actual
right-half construction or all-depth growth claim. Rebased markers
do not force deeper INITIAL black cells (GC1007); do not pump them.
OUTCOME: P1/P2 HELD;41 sparse cones and16 S/L lifts pass. Affine
control fails on001001000. The unexpected no11-only control fails
on000000101. All complete triangle vertices pass the literal table.
"""
from itertools import product


def left_columns(q):
    wall=tuple(t%2 for t in range(2*len(q)))
    # Exact inverse of the wall; odd column1 samples drop out here.
    first=tuple(b for a in q for b in (1-a,1))
    columns=[wall,first]
    for depth in range(2,13):
        a,b=columns[-1],columns[-2]
        c=tuple(a[t+1]^(a[t]|b[t]) for t in range(len(a)-1))
        # Independent literal table, all complete triangle vertices.
        assert all(((30>>(4*c[t]+2*a[t]+b[t]))&1)==a[t+1]
                   for t in range(len(c)))
        columns.append(c)
    return columns


def identity(q):
    columns=left_columns(q)
    for depth,col in enumerate(columns[1:],1):
        for s in range(len(col)//2):
            u=q[s:]
            pair=(
                (1-u[0],1), (u[0],u[1]), (1-u[1],1-u[1]),
                (0,u[2]), (1-(u[1]|u[2]),1-u[1]),
                (u[2],u[1]|u[2]|u[3]),
                (1-(u[2]|u[3]),1-u[3]), (0,u[3]|u[4]),
                (1-(u[2]|u[4]),1), (u[2]|u[4],u[3]|u[5]),
                (1-(u[3]|u[5]),1-(u[3]|u[5])),
                (u[2]*u[5],u[4]|u[6]))[depth-1] if len(u)>=7 else None
            if pair is not None and tuple(col[2*s:2*s+2])!=pair:
                return False
    col=columns[12]
    return all(col[2*s]==q[s+2]*q[s+5] and
               col[2*s+1]==(q[s+4]|q[s+6])
               for s in range(len(col)//2))


def separated(q,gap):
    p=[i for i,b in enumerate(q) if b]
    return all(b-a>=gap for a,b in zip(p,p[1:]))


def main():
    words=[q for q in product((0,1),repeat=9) if separated(q,3)]
    assert all(identity(q) for q in words)
    short=(0,0,1,0,0,1,0,0,0)
    assert left_columns(short)[12][0]==1
    assert short[2]^short[5]==0  # Affine countercontrol.
    lifted=0
    for letters in product(('S','L'),repeat=4):
        temporal=''.join('110100' if a=='S' else '1101000100' for a in letters)
        q=tuple(map(int,temporal[::2]))
        assert separated(q,3) and identity(q)
        lifted+=1
    weak=next(q for q in product((0,1),repeat=9)
              if separated(q,2) and not identity(q))
    print(dict(sparse_cones=len(words),SL_lift_controls=lifted,
               even_short_marker='q[s+2]*q[s+5]',
               odd_formula='q[s+4] OR q[s+6]',
               affine_counter='001001000',
               no11_counter=''.join(map(str,weak)),
               all_depth_carrier='OPEN',record_bound='OPEN'))


if __name__=='__main__':main()
