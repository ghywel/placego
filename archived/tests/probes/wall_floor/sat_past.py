#!/usr/bin/env python3
"""sat_past.py (Local, L1538): the entrance question as SAT, the tool TOOLS.md names for it. Is there a row y_0 with its top W cells a given window, with y_1 = F(y_0) outside a set of windows (or equal to a given window), and with y_1..y_L all reading letters?
Rows are exact: y_s(k) = y_(s-1)(k+3) xor (y_(s-1)(k+4) or y_(s-1)(k+5)). Writes DIMACS and calls kissat. Usage: SETFILE W L INDEX SECONDS [noexclude]. SETFILE: words low..high, cut to the top W cells."""
import sys,subprocess,tempfile,os,time
def build(v,W,L,T,exclude=True):
    K0=max(11+5*L-1,W+5)
    var={}; n=[0]; cl=[]
    def x(s,k):
        key=(s,k)
        if key not in var:
            n[0]+=1; var[key]=n[0]
        return var[key]
    for s in range(1,L+1):
        for k in range(0,K0-5*s+1):
            r=x(s,k);a=x(s-1,k+3);b=x(s-1,k+4);c=x(s-1,k+5)
            for ra in (0,1):
              for aa in (0,1):
                for bb in (0,1):
                  for cc in (0,1):
                    if ra!=(aa^(bb|cc)):
                        cl.append([(-r if ra else r),(-a if aa else a),(-b if bb else b),(-c if cc else c)])
    FIX=[1,1,0,0,0,1,1,1]
    for s in range(0,L+1):
        for k in range(8):
            cl.append([x(s,k) if FIX[k] else -x(s,k)])
        cl.append([x(s,8),x(s,9)]); cl.append([-x(s,8),-x(s,9)])
        cl.append([-x(s,10)])
    for k in range(W):
        cl.append([x(0,k) if v[W-1-k]=='#' else -x(0,k)])
    if exclude:
        for t in T:
            cl.append([(-x(1,k) if t[W-1-k]=='#' else x(1,k)) for k in range(W)])
    return n[0],cl,var,K0
def solve(nv,cl,secs):
    f=tempfile.NamedTemporaryFile('w',suffix='.cnf',delete=False)
    f.write(f'p cnf {nv} {len(cl)}\n')
    for c in cl: f.write(' '.join(map(str,c))+' 0\n')
    f.close()
    t0=time.time()
    r=subprocess.run(['kissat','-q',f'--time={secs}',f.name],capture_output=True,text=True)
    os.unlink(f.name)
    st='?'; model=set()
    for l in r.stdout.splitlines():
        if l.startswith('s '): st=l[2:]
        if l.startswith('v '):
            for z in l[2:].split():
                z=int(z)
                if z>0: model.add(z)
    return st,model,time.time()-t0
if __name__=='__main__':
    S=[l.strip() for l in open(sys.argv[1]) if l.strip()]
    W=int(sys.argv[2]); L=int(sys.argv[3]); idx=sys.argv[4]; secs=int(sys.argv[5]); excl=len(sys.argv)<7
    T=sorted({s[len(s)-W:] for s in S})
    ids=range(len(T)) if idx=='all' else [int(idx)]
    for i in ids:
        nv,cl,var,K0=build(T[i],W,L,T,excl)
        st,model,el=solve(nv,cl,secs)
        print(f'W {W} L {L} window {i}: vars {nv} clauses {len(cl)}: {st} in {el:.1f}s',flush=True)
        if 'SATISFIABLE' in st and not st.startswith('UN'):
            rows=[''.join('#' if var[(s,k)] in model else '.' for k in range(0,40)) for s in (0,1)]
            word=''.join('A' if var[(s,8)] in model else 'B' for s in range(L,-1,-1))
            print('   letters oldest first:',word[:100])
