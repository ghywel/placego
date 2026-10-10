"""L584: bounded exact-gate/global-affine closure explanation test.
OPEN is not SAT. Predictions and retained failure in RULE30-GPT.md.
"""
from itertools import product
F='0010001000100010100001010100010000101000010101'
TRUTH=(0,1,1,1,1,0,0,0)
class Basis:
    def __init__(self):self.b={};self.bad=False
    def reduce(self,x,y=0):
        while x:
            k=x.bit_length()-1
            if k not in self.b:break
            a,c=self.b[k];x^=a;y^=c
        return x,y
    def add(self,x,y):
        x,y=self.reduce(x,y)
        if not x:self.bad|=bool(y);return False
        self.b[x.bit_length()-1]=(x,y);return True

def infer(w,cap=8):
    last=2*len(w)-2
    ix={(t,i):j for j,(t,i) in enumerate((t,i) for t in range(last+1) for i in range(last-t+2))}
    unit=lambda t,i:1<<ix[t,i]
    b=Basis()
    for t in range(last+1):b.add(unit(t,0),t%2)
    for s,a in enumerate(w):b.add(unit(2*s,1),int(a))
    gates=[]
    valid=[l|(c<<1)|(r<<2)|(TRUTH[4*l+2*c+r]<<3) for l,c,r in product((0,1),repeat=3)]
    parity=[[((a&m).bit_count()%2) for a in valid] for m in range(16)]
    for t in range(last):
        for i in range(1,last-t+1):
            vs=[unit(t,i-1),unit(t,i),unit(t,i+1),unit(t+1,i)]
            masks=[sum(vs[k] for k in range(4) if m>>k&1) for m in range(16)]
            gates.append(masks)
    for turn in range(cap):
        before=len(b.b)
        for masks in gates:
            constraints=[]
            for m in range(1,16):
                r,y=b.reduce(masks[m])
                if r==0:constraints.append((m,y))
            survivors=[a for a in range(8) if all(parity[m][a]==y for m,y in constraints)]
            if not survivors:return 'CONTRADICTION',turn+1,len(b.b)
            for m in range(1,16):
                vals={parity[m][a] for a in survivors}
                if len(vals)==1:b.add(masks[m],vals.pop())
            if b.bad:return 'CONTRADICTION',turn+1,len(b.b)
        if len(b.b)==before:return 'OPEN-fixed',turn+1,len(b.b)
    return 'OPEN-cap',cap,len(b.b)

# Global parity-cycle control, invisible to unit-domain propagation.
b=Basis()
for x,y in [(3,0),(6,0),(5,1)]:b.add(x,y)
assert b.bad
assert infer('11')[0]=='CONTRADICTION'
for name,w in [('f',F),('prefix',F[:-1]),('suffix',F[1:])]:
    r=infer(w);print(name,r,flush=True)
    if name!='f':assert r[0].startswith('OPEN')
for seed in range(16):
    row={i:int(i<=4 and seed>>(i-1)&1) for i in range(1,20)};code=''
    for t in range(9):
        if t%2==0:code+=str(row[1])
        row={i:((t%2 if i==1 else row.get(i-1,0))^(row[i]|row.get(i+1,0))) for i in row}
    assert infer(code)[0].startswith('OPEN')
print('Controls PASS')
