"""GC1031 bounded test of 1^n 0^infinity, free visible model only.
Preregistered in RULE30-GPT; no new membership or Cloud-template scan.
P1: growing runs suggest an explicit unbounded family. Outcome inconclusive:
n=1,2,4,8,16,32,64 gives closed-run maxima 1,3,4,4,6,9,7.
No unboundedness or uniform bound follows; stop without a parameter sweep.
Controls: independent literal and packed inverse recurrence agree.
Unexpected check: only runs with both bounding black cells are counted.
Record searched: junction AND periodic|bound -> CL200, no such family.
"""
from rule30_cloud_junctions import left_row

def packed_row(vis):
    horizon = 2*len(vis)-1
    right = sum((t%2)<<t for t in range(horizon+1))
    col = sum((1 if t%2 else 1-int(vis[t//2]))<<t for t in range(horizon+1))
    out = []
    for width in range(horizon+1,1,-1):
        out.append(str(col&1))
        right,col = col,((col>>1)^(col|right))&((1<<(width-1))-1)
    return ''.join(out)

def closed_runs(row):
    previous = None
    for j,b in enumerate(row):
        if b == '1':
            if previous is not None and j > previous+1:
                yield j-previous-1,previous+2
            previous = j

if __name__ == '__main__':
    expected = (1,3,4,4,6,9,7)
    for n,want in zip((1,2,4,8,16,32,64),expected):
        visible = '1'*n+'0'*(4*n+16)
        row = left_row(visible)
        assert row == packed_row(visible)
        best = max(closed_runs(row),default=(0,0))
        assert best[0] == want
        print(n,best)
    print('PASS literal/packed agreement; boundary-censored runs excluded')
