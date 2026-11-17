#!/usr/bin/env python3
"""mutate.py (Local, L1548): one-digit mutations of the data, each of which the kernel must reject. Prints one line per mutant."""
import re,subprocess,os,sys,shutil
src=open('Rule30Submission.lean',encoding='utf-8').read()
K=os.path.expanduser('~/placego-data/wall/pkg/kit')
L=os.path.expanduser('~/.elan/toolchains/leanprover--lean4---v4.35.0/bin/lean')
def mut(name,f):
    s=f(src)
    assert s!=src,name
    os.makedirs('mut',exist_ok=True)
    p=f'mut/{name}.lean'; open(p,'w',encoding='utf-8').write(s)
    env=dict(os.environ,LEAN_PATH=K+'/lean/.lake/build/lib/lean',LEAN_NUM_THREADS='2')
    r=subprocess.run(['nice','-n','10','timeout','120',L,p],env=env,capture_output=True,text=True)
    errs=[l for l in r.stdout.split('\n') if ': error' in l or 'error:' in l]
    print(name,'rc',r.returncode,'errors',len(errs),(errs[0][:140] if errs else ''),flush=True)
def sub_in(ns,pat,rep):
    def f(s):
        a=s.index(f'namespace {ns}\n'); b=s.index(f'end {ns}\n')
        t=s[a:b]; m=re.search(pat,t)
        u=t[:m.start()]+rep(m)+t[m.end():]
        return s[:a]+u+s[b:]
    return f
# 1 flip one low bit of a window in each lock
for ns,W in (('LockAB',45),('LockAAB',136),('LockThird',175)):
    mut('win_'+ns,sub_in(ns,r'\[\[(\d+)',lambda m:'[['+str(int(m.group(1))^(1<<40))))
# 2 lower one rank and change one window of the cloud
mut('rank',lambda s:re.sub(r'(\.n \.e 27392014413220) 2 ',r'\1 1 ',s,count=1))
mut('rank17',lambda s:s.replace('rk n ≤ 17','rk n ≤ 16',1))
mut('cloud_win',lambda s:s.replace('27392014413220','27392014413221',1))
# 3 the entry row, one bit inside the window at tick 6 and the letters
def flip(s,name,bit):
    m=re.search(r'def '+name+r' : Nat := (0x[0-9a-f]+)',s); v=int(m.group(1),16)^(1<<bit)
    return s[:m.start(1)]+hex(v)+s[m.end(1):]
mut('E_bit',lambda s:flip(s,'E',500))
mut('LB_bit',lambda s:flip(s,'LB',60))
# 4 the sweep itself
mut('sweep',lambda s:s.replace('(y >>> (i + 1)) ||| (y >>> i)','(y >>> (i + 1)) &&& (y >>> i)',1))
mut('rain',lambda s:s.replace('(42 <<< W)','(41 <<< W)'))
