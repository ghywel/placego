# Mutants of Rule30LateTwins: each must fail to build. Run from the kit root with lake on PATH.
import subprocess,sys,os
src=open('lean/Ruliology/CellularAutomata/Rule30LateTwins.lean').read()
muts=[
 ('onset 45',            'theorem late_twin {y : Nat} (hy : y ≠ 0) {t : Nat} (ht : 46 ≤ t)', 'theorem late_twin {y : Nat} (hy : y ≠ 0) {t : Nat} (ht : 45 ≤ t)'),
 ('stage 1 in 13 ticks', 'chk (fun u => inC13 (iterR 14 u)) 4096 12 = true', 'chk (fun u => inC13 (iterR 13 u)) 4096 12 = true'),
 ('stage 2 in 11 ticks, all phases, proof adjusted', None, None),
 ('settle in 25 ticks',  '(h2 : u < 2 ^ 20) {t : Nat} (ht : 26 ≤ t) :', '(h2 : u < 2 ^ 20) {t : Nat} (ht : 25 ≤ t) :'),
 ('wrong C20 element',   'v == 911005 || v == 912610', 'v == 911005 || v == 912611'),
 ('wrong factor bit',    '⟨14, 0, 6, 0, ⟨Or.inl rfl', '⟨13, 0, 6, 0, ⟨Or.inl rfl'),
 ('corrupted reset word','[false, true, true, true, true, false].getD j false', '[false, true, true, true, false, false].getD j false'),
]
tmp='lean/Ruliology/CellularAutomata/Rule30LateTwinsMutant.lean'
bad=0
def mutate(name,a,b):
    if a is not None:
        assert src.count(a)==1,(name,src.count(a)); return src.replace(a,b,1)
    t=src
    for c in ('6411','6428','7117','7129'):
        x='inC20 (iterR 12 ('+c+' * 128 + b))'; assert t.count(x)==1; t=t.replace(x,'inC20 (iterR 11 ('+c+' * 128 + b))')
    for x,y in (('have h26 : inC20 (iterR 12 v) = true','have h26 : inC20 (iterR 11 v) = true'),
                ('have : iterR t u = iterR (t - 26) (iterR 12 v)','have : iterR t u = iterR (t - 25) (iterR 11 v)'),
                ('(h2 : u < 2 ^ 20) {t : Nat} (ht : 26 ≤ t) :','(h2 : u < 2 ^ 20) {t : Nat} (ht : 25 ≤ t) :')):
        assert t.count(x)==1,(x,t.count(x)); t=t.replace(x,y)
    return t
for name,a,b in muts:
    open(tmp,'w').write(mutate(name,a,b).replace('namespace Ruliology.CellularAutomata.Rule30LateTwins','namespace Ruliology.CellularAutomata.Rule30LateTwinsMutant').replace('end Rule30LateTwins','end Rule30LateTwinsMutant'))
    r=subprocess.run(['lake','env','lean',tmp],capture_output=True,text=True)
    out=(r.stdout+r.stderr)
    failed = r.returncode!=0 and 'error' in out
    print(('REJECTED' if failed else 'ACCEPTED (bad)'),'|',name,'|',(out.strip().split('\n')[0][:110] if failed else ''))
    bad+= (not failed)
os.remove(tmp)
print('mutants accepted:',bad,'of',len(muts))
sys.exit(1 if bad else 0)
