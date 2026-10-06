"""G113 LM4 preregistered NOT RUN:publish before execution.
Extract lexicographic13-bit zero-child and positive-parent witnesses.
Independent literal-table padded histories must preserve traces in8 checks.
Unexpected boundary guard:both outer bits arbitrary, not fixed zero.
"""
from itertools import product
from rule30_gpt_lagged_memory import traces


def padded(word,left,right):
    a=dict(zip(range(-7,8),(left,)+word+(right,)));b=dict(a)
    it,jt=[a[0]],[b[0]]
    def update(row):
        return {i:(30>>(4*row[i-1]+2*row[i]+row[i+1]))&1
                for i in range(min(row)+1,max(row))}
    for t in range(1,7):
        aa,bb=update(a),update(b)
        if t==1:
            bb[0]=(30>>(4*b[-1]+2*b[0]+bb[1]))&1
        a,b=aa,bb;it.append(a[0]);jt.append(b[0])
    return tuple(it),tuple(jt)


def main():
    found={}
    for word in product((0,1),repeat=13):
        i,j=traces(word);k=tuple((x,x^y) for x,y in zip(i,j))
        if k[4:6]!=((0,0),(0,0)):
            continue
        kind='zero' if k[3]==(0,0) else 'success' if k[3]==(0,1) and k[6][1]==1 else None
        if kind and kind not in found:
            found[kind]=(word,i,j)
        if len(found)==2:
            break
    assert set(found)=={'zero','success'}
    count=0
    for kind,(word,i,j) in sorted(found.items()):
        for l,r in product((0,1),repeat=2):
            assert padded(word,l,r)==(i,j);count+=1
        print(kind+' initial[-6..6]='+''.join(map(str,word))+
              ' I='+''.join(map(str,i))+' J='+''.join(map(str,j)))
    assert count==8
    print('LM4 PASS:two positive finite cylinders,8 independent padded-boundary checks')


if __name__=='__main__':
    main()
