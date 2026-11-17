# Mutants of Rule30SeparatorQ01: each must fail to build. Run from the kit root with lake on PATH.
import subprocess,sys,os
src=open('lean/Ruliology/CellularAutomata/Rule30SeparatorQ01.lean').read()
muts=[
 ('class with no two adjacent black bits', 'def NoAdjWhite (f : Nat → Bool) : Prop := ∀ s, f s = true ∨ f (s + 1) = true',
                                           'def NoAdjWhite (f : Nat → Bool) : Prop := ∀ s, f s = false ∨ f (s + 1) = false'),
 ('endpoint at the even tick',             'def zEnd (L : Nat → Bool) (j : Nat) : Sym := zpair L (2 * j + 1) 1',
                                           'def zEnd (L : Nat → Bool) (j : Nat) : Sym := zpair L (2 * j) 1'),
 ('peel chart one depth deeper',           '∀ d t, t + d ≤ S → peelPow d (inverse (zEnd L)) t = zpair L t (2 * d + t + 2) := by',
                                           '∀ d t, t + d ≤ S → peelPow d (inverse (zEnd L)) t = zpair L t (2 * d + t + 3) := by'),
 ('tail symbol 1 allowed (false: phi 1 1 = 2)', 'theorem phi_const_tail : ∀ c : Sym, constantTail c → phi c c = 0 := by',
                                           'theorem phi_const_tail : ∀ c : Sym, (c = 1 ∨ constantTail c) → phi c c = 0 := by'),
 ('layer word at the black ticks (false: black_tick_control)',         'def layerWord (x0 : Bool) (r : Nat → Bool) (s : Nat) : Bool := layerCol x0 r (2 * s + 1)',
                                           'def layerWord (x0 : Bool) (r : Nat → Bool) (s : Nat) : Bool := layerCol x0 r (2 * s + 2)'),
 ('even death bounds from n = 6',          '(∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 2) → ¬ SurvivesTo L (2 * n + 2)) ∧',
                                           '(∀ n, 6 ≤ n → ∀ L, ExactWidth L (2 * n + 2) → ¬ SurvivesTo L (2 * n + 2)) ∧'),
 ('odd width without top two black',       '(∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 3) → L (2 * n + 2) = true →\n    ¬ SurvivesTo L (2 * n + 2))',
                                           '(∀ n, 7 ≤ n → ∀ L, ExactWidth L (2 * n + 3) →\n    ¬ SurvivesTo L (2 * n + 2))'),
 ('death bound 2W + 2',                    '(hL : ∀ k, W < k → L k = false) : ∃ s, s ≤ W + 2 ∧ zrow L (2 * s) 1 = false := by',
                                           '(hL : ∀ k, W < k → L k = false) : ∃ s, s ≤ W + 1 ∧ zrow L (2 * s) 1 = false := by'),
 ('odd guard witness to tick 38',          'SurvivesTo (IntegerForm.rowOfNat 272125) 18 :=',
                                           'SurvivesTo (IntegerForm.rowOfNat 272125) 19 :='),
 ('threshold witness to tick 32',          'ExactWidth (IntegerForm.rowOfNat 11083) 14 ∧ SurvivesTo (IntegerForm.rowOfNat 11083) 15 :=',
                                           'ExactWidth (IntegerForm.rowOfNat 11083) 14 ∧ SurvivesTo (IntegerForm.rowOfNat 11083) 16 :='),
]
tmp='lean/Ruliology/CellularAutomata/Rule30SeparatorQ01Mutant.lean'
bad=0
for name,a,b in muts:
    assert src.count(a)==1,(name,src.count(a))
    t=src.replace(a,b,1).replace('namespace Rule30SeparatorQ01','namespace Rule30SeparatorQ01Mutant').replace('end Rule30SeparatorQ01','end Rule30SeparatorQ01Mutant')
    open(tmp,'w').write(t)
    r=subprocess.run(['lake','env','lean',tmp],capture_output=True,text=True)
    out=(r.stdout+r.stderr)
    failed = r.returncode!=0 and 'error' in out
    first=[l for l in out.strip().split('\n') if 'error' in l][:1]
    print(('REJECTED' if failed else 'ACCEPTED (bad)'),'|',name,'|',(first[0].split('lean:')[-1][:110] if failed and first else ''))
    bad+= (not failed)
os.remove(tmp)
print('mutants accepted:',bad,'of',len(muts))
sys.exit(1 if bad else 0)
