# Local's independent self-check for the GC2719 carry: the trunk/column-8 update, the join equation and the 21-cell cone.
# Written from the bit rules, not from GPT's sources. Driven half-row: cell 1 is bit 0, the driver supplies cell 0.
import random
def B(x,b): return ((x<<1)|b)^(x|(x>>1))
def cell(x,i): return (x>>(i-1))&1
random.seed(2719)
bad_trunk=bad_join=bad_cone=0; N=4000
for _ in range(N):
    x=random.getrandbits(60)
    q=x&127; X=x
    for t in range(14):
        w=cell(X,8); v=cell(X,9)
        qn=(((q<<1)|(t%2))^(q|(q>>1)|(w<<6)))&127
        Xn=B(X,t%2)
        if qn!=(Xn&127): bad_trunk+=1
        wn=cell(Xn,8)
        if wn!=(((q>>6)&1)^(w|v)): bad_join+=1
        q,X=qn,Xn
    # cone: cells beyond 21 never change the 14-tick column-8 word or the seven-cell endpoint
    y=x^(random.getrandbits(39)<<21)
    def out(z):
        ws=[];Z=z
        for t in range(14): ws.append(cell(Z,8)); Z=B(Z,t%2)
        return ws,Z&127
    if out(x)!=out(y): bad_cone+=1
# control: cell 21 does matter for some starts (the cone is not loose)
hit=0
for _ in range(2000):
    x=random.getrandbits(60); y=x^(1<<20)
    a=[];b=[];X=x;Y=y
    for t in range(14): a.append(cell(X,8)); b.append(cell(Y,8)); X=B(X,t%2); Y=B(Y,t%2)
    if a!=b or (X&127)!=(Y&127): hit+=1
print('trunk update mismatches',bad_trunk,'of',14*N,'| join equation mismatches',bad_join,'| cone violations',bad_cone,'of',N,'| cell 21 matters in',hit,'of 2000')
# endpoint branch: next black at relative 16 iff endpoint cells 1-3 white (corridor), from an odd-phase endpoint
bad=0
for _ in range(4000):
    T=random.getrandbits(40); R=B(B(T,0),1)
    if (R&1)!=int((T&7)==0): bad+=1
print('corridor (black two ticks on iff cells 1-3 white) mismatches',bad)
