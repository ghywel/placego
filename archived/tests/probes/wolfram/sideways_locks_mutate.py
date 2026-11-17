# Mutants of Rule30SidewaysLocks: each must fail to build. Run from the kit root with lake on PATH.
# 'decide' marks a mutant whose failure includes a kernel/decide refutation of a false statement.
import subprocess,sys,os
src=open('lean/Ruliology/CellularAutomata/Rule30SidewaysLocks.lean').read()
muts=[
 ('lock5 word 10001',                     'def word5 : List Bool := [true, false, false, false, false]',
                                          'def word5 : List Bool := [true, false, false, false, true]'),
 ('lock5 with period 4',                  'theorem lock5_ok : lockCheck 34 5 word5 lock5Codes = true := by decide +kernel',
                                          'theorem lock5_ok : lockCheck 34 4 word5 lock5Codes = true := by decide +kernel'),
 ('lock5 missing one window',             '[547958887, 2695442535, 6990409831, 11285377127, 15580344423]',
                                          '[547958887, 2695442535, 6990409831, 11285377127]'),
 ('free column W + 1 at both ticks',      'def dstep (s : List Bool) (x1 x2 : Bool) : List Bool := lin3 (true :: lin3 (false :: (s ++ [x1, x2])))',
                                          'def dstep (s : List Bool) (x1 x2 : Bool) : List Bool := lin3 (true :: (lin3 (false :: (s ++ [x1])) ++ [x2]))'),
 ('lock7 read with the word of lock7b',   'theorem lock7_ok : lockCheck 30 7 word7 lock7Codes = true := by decide +kernel',
                                          'theorem lock7_ok : lockCheck 30 7 word7b lock7Codes = true := by decide +kernel'),
 ('lock5 entry two ticks early',          'theorem lock5_entry : winW 34 (rh 28998) 15 ∈ cls 34 lock5Codes 0 := by',
                                          'theorem lock5_entry : winW 34 (rh 28998) 13 ∈ cls 34 lock5Codes 0 := by'),
 ('lock7b entry in the wrong class',      'theorem lock7b_entry : winW 45 (rh 3793493) 29 ∈ cls 45 lock7bCodes 6 := by',
                                          'theorem lock7b_entry : winW 45 (rh 3793493) 29 ∈ cls 45 lock7bCodes 5 := by'),
 ('windows at the even ticks',            'theorem winW_dstep (W : Nat) (R : Nat → Bool) (t : Nat) (ht : t % 2 = 1) :',
                                          'theorem winW_dstep (W : Nat) (R : Nat → Bool) (t : Nat) (ht : t % 2 = 0) :'),
 ('family prefix one cell short',         'theorem CQ01_lock5_family {R : Nat → Bool} (h : ∀ i, i < 49 → R (i + 1) = (28998 : Nat).testBit i) :',
                                          'theorem CQ01_lock5_family {R : Nat → Bool} (h : ∀ i, i < 48 → R (i + 1) = (28998 : Nat).testBit i) :'),
]
tmp='lean/Ruliology/CellularAutomata/Rule30SidewaysLocksMutant.lean'
bad=0
for name,a,b in muts:
    assert src.count(a)==1,(name,src.count(a))
    t=src.replace(a,b,1).replace('namespace Rule30SidewaysLocks','namespace Rule30SidewaysLocksMutant').replace('end Rule30SidewaysLocks','end Rule30SidewaysLocksMutant')
    open(tmp,'w').write(t)
    r=subprocess.run(['lake','env','lean',tmp],capture_output=True,text=True)
    out=(r.stdout+r.stderr)
    failed = r.returncode!=0 and 'error' in out
    errs=[l for l in out.split('\n') if ': error' in l]
    dec = any('decide' in l for l in out.split('\n') if 'error' in l) or 'proved that the proposition' in out
    print(('REJECTED' if failed else 'ACCEPTED (bad)'),'|',name,'|','decide' if dec else 'proof','|',(errs[0].split('lean:')[-1][:100] if errs else ''))
    bad+= (not failed)
os.remove(tmp)
print('mutants accepted:',bad,'of',len(muts))
sys.exit(1 if bad else 0)
