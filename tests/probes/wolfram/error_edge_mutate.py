#!/usr/bin/env python3
"""mutate_edge.py (Local, L1553): negative controls for Rule30ErrorEdge. Each mutant changes one law's conclusion or a hypothesis; the kernel must reject it. Prints one line per mutant."""
import os,subprocess,sys
src=open(sys.argv[1],encoding='utf-8').read()
L=os.path.expanduser('~/.elan/toolchains/leanprover--lean4---v4.35.0/bin/lean')
LP=sys.argv[2]
M=[('heal_black_flipped','((xor p (s || x) = xor p (s || y)) ↔ s = true)','((xor p (s || x) = xor p (s || y)) ↔ s = false)'),
 ('heal0_flipped','(((s || x) = (s || y)) ↔ s = true)','(((s || x) = (s || y)) ↔ s = false)'),
 ('white_above_flipped','xor true (x2 || x3) = xor true (!x2 || y3) → xor true (x2 || x3) = false := by decide','xor true (x2 || x3) = xor true (!x2 || y3) → xor true (x2 || x3) = true := by decide'),
 ('black_two_flipped','xor x2 (x3 || x4) = xor (!x2) (y3 || y4) → xor x2 (x3 || x4) = true := by decide','xor x2 (x3 || x4) = xor (!x2) (y3 || y4) → xor x2 (x3 || x4) = false := by decide'),
 ('jump_five_flipped','xor (xor x2 (x3 || x4)) (xor x3 (x4 || x5) || xor x4 (x5 || x6)) = true := by decide','xor (xor x2 (x3 || x4)) (xor x3 (x4 || x5) || xor x4 (x5 || x6)) = false := by decide'),
 ('jump_six_flipped','xor (xor x3 (x4 || x5)) (xor x4 (x5 || x6) || xor x5 (x6 || x7)) = false := by decide','xor (xor x3 (x4 || x5)) (xor x4 (x5 || x6) || xor x5 (x6 || x7)) = true := by decide'),
 ('jump_seven_flipped','xor (xor x4 (x5 || x6)) (xor x5 (x6 || x7) || xor x6 (x7 || x8)) = false := by decide','xor (xor x4 (x5 || x6)) (xor x5 (x6 || x7) || xor x6 (x7 || x8)) = true := by decide'),
 ('jump_four_white','a (m + 5) (t + 2) = true := by\n  have w := white_above','a (m + 5) (t + 2) = false := by\n  have w := white_above'),
 ('jump_six_no_white_hypothesis','    xor x5 (x6 || x7) = false →\n    xor (xor x3','    xor (xor x3'),
]
os.makedirs('mut',exist_ok=True)
for n,a,b in M:
    assert a in src,n
    p=f'mut/{n}.lean'; open(p,'w',encoding='utf-8').write(src.replace(a,b,1))
    r=subprocess.run(['nice','-n','10','timeout','100',L,p],env=dict(os.environ,LEAN_PATH=LP),capture_output=True,text=True)
    e=[l for l in r.stdout.split('\n') if 'error' in l]
    print(n,'rc',r.returncode,'errors',len(e),(e[0][:110] if e else ''),flush=True)
