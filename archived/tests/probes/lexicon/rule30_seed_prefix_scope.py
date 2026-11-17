"""GC1192: two named controls for L676's seed-prefix proposal; no tree run.

PREDICTIONS BEFORE controls, 2026-10-13: the primitive Q inputs10110001
and101100001 share k=7 initial bits, but at legal r0/p0/T1 differ at
child depth5 and child tick4. Their first four ticks agree. Hence W=k-2
overreads in phase0; W=k-3 is safe in both phases. Counterfactual:
triangularity somehow eliminates that extra coordinate, so all five
ticks agree. Independent control: ordinary full-line Wolfram-table
update versus the edge recurrence; clamped table evolution versus
literal XOR/OR evolution. Unexpected: the accepted short seed10111
is still a relevant finite input when zero-padded past its terminal1;
an end-of-word acceptance test must not delete that infinite zero ray.
Record searched: prefix.tree|seed.prefix withtriangular|residu ->1
GC1158 hit; prefix|triangular withwindow|crop ->219hits66files.
G249, GC1184/1190/1191 and committed L676 read. No solver, membership,
period/profile/survival census, prefix-tree search or Local run replay.
OUTCOME: both registered primitive controls PASS, including the fifth-tick
counter; the zero-padded short input is retained. No search run.
"""
from rule30_primitive_seed_language import decode

TABLE=(0,1,1,1,1,0,0,0)


def edge(word):
    x=list(map(int,word))+[0,0]
    return [v ^ ((x[j-1] if j>=1 else 0) |
                 (x[j-2] if j>=2 else 0)) for j,v in enumerate(x)]


def ordinary(word):
    black={-j for j,v in enumerate(word) if v=='1'}
    nxt={s for s in range(-len(word)-1,2)
         if TABLE[4*int(s-1 in black)+2*int(s in black)+int(s+1 in black)]}
    # New right edge is1; coordinate j is physical site1-j.
    return [int(1-j in nxt) for j in range(len(word)+2)]


def trace(row,p,table):
    row=list(row); out=[]
    for t in range(len(row)):
        out.append(row[0]); x=[(t+p)%2]+row
        row=[TABLE[4*x[j+1]+2*x[j]+x[j-1]] if table else
             x[j+1] ^ (x[j] | x[j-1]) for j in range(1,len(x)-1)]
    return out


def main():
    words=('10110001','101100001')
    traces=[]
    for w in words:
        assert decode(w)[2]=='Q'
        y=edge(w); assert y==ordinary(w)
        # p0: depth i reads V_(i+2) at T1.
        row=y[3:8]
        a=trace(row,0,True); assert a==trace(row,0,False)
        traces.append(a)
    assert words[0][:7]==words[1][:7]
    assert traces[0][:4]==traces[1][:4]
    assert traces[0][4]!=traces[1][4]
    short='10111'; assert decode(short)[2]=='Q'
    padded=short+'0'*5
    assert decode(padded) is None # full-word rejection is not prefix rejection
    assert edge(short)==edge(padded)[:len(short)+2]
    print('two primitive inputs:',words,'T1 five-tick traces:',traces)
    print('safe four-tick agreement PASS; fifth-tick counter PASS; short zero-ray control PASS')


if __name__=='__main__':main()
