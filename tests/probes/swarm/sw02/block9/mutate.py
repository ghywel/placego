#!/usr/bin/env python3
"""Block 9 step 2 mutants of Rule30PeriodThreeLanguage. Prediction (written 19:38 UTC before the run): all six are rejected.
M1 adds 11 to col1Forbidden011 (occurs3 true: K011w7_occ_all fails); M2 adds 1001 to col1Forbidden001 (forbidden only
from width 13: K001w10_occ_all fails); M3 gives K011w7 the word 001 (checkb fails); M4 sets K001w10_bad := 1;
M5 sets node 0's rank of K011w7 to 65535 (checkb fails); M6 states col1_001 at phase 2 (the proof breaks)."""
import os, re, subprocess, sys
src = open(sys.argv[1]).read(); kit = sys.argv[2]; d = os.path.join(kit, 'Ruliology/CellularAutomata')
def m1(s): return s.replace('def col1Forbidden011 : List (List Bool) :=\n  [[false, false]', 'def col1Forbidden011 : List (List Bool) :=\n  [[true, true], [false, false]', 1)
def m2(s): return s.replace('def col1Forbidden001 : List (List Bool) :=\n  [', 'def col1Forbidden001 : List (List Bool) :=\n  [[true, false, false, true], ', 1)
def m3(s):
    i = s.index('def K011w7 : Cert where'); j = s.index('w := [false, true, true]', i)
    return s[:j] + 'w := [false, false, true]' + s[j + len('w := [false, true, true]'):]
def m4(s): return s.replace('def K001w10_bad : Nat := 0', 'def K001w10_bad : Nat := 1', 1)
def m5(s):
    m = re.search(r'def K011w7_rankP : Nat := (\d+)', s); v = int(m.group(1)); v = (v & ~0xFFFF) | 0xFFFF
    return s[:m.start(1)] + str(v) + s[m.end(1):]
def m6(s): return s.replace("∃ T', T ≤ T' ∧ ∀ t, T' ≤ t → (t - T) % 3 = 1 → ∀ pat ∈ col1Forbidden001,\n      ¬ ∀ i, i < pat.length → cell (t + 3 * i) 1 = pat.getD i false := by\n  have hP : K001w10.P",
                            "∃ T', T ≤ T' ∧ ∀ t, T' ≤ t → (t - T) % 3 = 2 → ∀ pat ∈ col1Forbidden001,\n      ¬ ∀ i, i < pat.length → cell (t + 3 * i) 1 = pat.getD i false := by\n  have hP : K001w10.P", 1)
sys.set_int_max_str_digits(0)
env = dict(os.environ, PATH=os.path.expanduser('~/.elan/bin') + ':' + os.environ['PATH'])
for k, f in enumerate([m1, m2, m3, m4, m5, m6], 1):
    s = f(src); assert s != src, k
    name = f'Rule30PeriodThreeLanguageMut{k}'
    s = s.replace('namespace Rule30PeriodThreeLanguage', f'namespace {name}').replace('end Rule30PeriodThreeLanguage', f'end {name}')
    path = os.path.join(d, name + '.lean'); open(path, 'w').write(s)
    r = subprocess.run(['lake', 'build', f'Ruliology.CellularAutomata.{name}'], cwd=kit, env=env, capture_output=True, text=True)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if 'error:' in l and name in l]
    print(f'M{k}: {"REJECTED" if r.returncode != 0 else "ACCEPTED"}; first error: {errs[0].split("error:")[-1].strip()[:150] if errs else "-"}', flush=True)
    os.remove(path)
    for ext in ('.olean', '.ilean', '.trace', '.hash', '.olean.hash', '.ilean.hash'):
        p = os.path.join(kit, '.lake/build/lib/lean/Ruliology/CellularAutomata', name + ext)
        if os.path.exists(p): os.remove(p)
