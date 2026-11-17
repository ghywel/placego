# Where two rows differ, against the strip front. Rows top-aligned at the same tick (lag d for different clocks).
# front f(t): first wheel where the row at t differs from the row at t + 32 (lag-32 detector, CL739).
import sys
def F(y): return (y>>1)^(y|(y<<1))
def run(y,T,marks):
    out={};t=0
    keep=set(marks)|{m+32 for m in marks}
    while t<=max(keep):
        if t in keep: out[t]=y
        y=F(y); t+=1
    return out
def top_diff(a,b):
    # first wheel where a and b differ, reading from their top cells
    A=format(a,'b');B=format(b,'b');n=min(len(A),len(B))
    x=int(A[:n],2)^int(B[:n],2)
    return n if x==0 else n-x.bit_length()
marks=[10000,20000,40000,60000]
pairs=[(129,154,0),(145,157,0),(64,91,96),(79,68,32)]
for a,b,d in pairs:
    ra=run(a,0,[m+d for m in marks]); rb=run(b,0,marks)
    print('pair',a,b,'lag',d)
    for m in marks:
        A=ra[m+d];B=rb[m];A2=ra[m+d+32];B2=rb[m+32]
        fa=top_diff(A,A2);fb=top_diff(B,B2);g=top_diff(A,B)
        print('  t',m,'f_a',fa,'f_b',fb,'first difference',g,'g-f',g-min(fa,fb),'width',B.bit_length(),'g/t',round(g/m,4),'f/t',round(fb/m,4),flush=True)
