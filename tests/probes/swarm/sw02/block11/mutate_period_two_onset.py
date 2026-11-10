#!/usr/bin/env python3
"""mutate_period_two_onset.py: must-fail mutants of the S-21 module Rule30PeriodTwoOnset (Cloud's K-02).

Prediction (written before the first run): each mutant is rejected. Counterfactual: an accepted mutant means the
statement or hypothesis it touches does not carry the claim. Record searched: GPT's K-02 carry (GC2840/GC2843) and
Cloud's BR-5.2; the kit's Rule30PeriodTwoWidth5/6, Rule30GateTrapWords and Rule30PeriodTwoWidth13; portal R30-20261028-e34744.
False statements: M1 the width-5 image has 19 windows; M2 the width-6 first image is the stabilized 36;
M3 the shortened word at width 5; M4 a shortening that is not forbidden (101000100).
Hypotheses the proof uses: M5 the clock reversed (black, white) in the double step; M6 the clock one tick short in
no_word; M7 the free bits without the second extra tick; M8 the rule at one column fewer in win_dstep.

Run from the kit's lean/ directory: python3 -I PATH/mutate_period_two_onset.py MODULE OUTDIR
"""
import os
import subprocess
import sys

src, out = sys.argv[1], sys.argv[2]
base = open(src, encoding='utf-8').read()
M = [
    ('M1', "theorem img5_length : (img 5).length = 20 :=", "theorem img5_length : (img 5).length = 19 :="),
    ('M2', "theorem img6_length : (img 6).length = 38 :=", "theorem img6_length : (img 6).length = 36 :="),
    ('M3', "theorem excludes_short6 : excludes (img 6) short6 = true :=",
     "theorem excludes_short6 : excludes (img 5) short6 = true :="),
    ('M4', "def short6 : List Bool := [true, false, true, false, true, false, false, false, false]",
     "def short6 : List Bool := [true, false, true, false, false, false, true, false, false]"),
    ('M5', "def dstep (r₁ r₂ : Bool) (x : List Bool) : List Bool := step true r₂ (step false r₁ x)",
     "def dstep (r₁ r₂ : Bool) (x : List Bool) : List Bool := step false r₂ (step true r₁ x)"),
    ('M6', "    (hw : excludes (img b) w = true) (s : Nat)\n    (hc : ∀ i, i < 2 * w.length → H (s + i) 0 = (i % 2 == 1)) :",
     "    (hw : excludes (img b) w = true) (s : Nat)\n    (hc : ∀ i, i < 2 * w.length - 1 → H (s + i) 0 = (i % 2 == 1)) :"),
    ('M7', "    (hc : ∀ i, i < 2 * w.length + 2 → H (s + i) 0 = (i % 2 == 1))\n    (hr :",
     "    (hc : ∀ i, i < 2 * w.length + 1 → H (s + i) 0 = (i % 2 == 1))\n    (hr :"),
    ('M8', "theorem win_dstep {b : Nat} {H : Nat → Int → Bool} (hH : Obeys b H) {s : Nat}",
     "theorem win_dstep {b : Nat} {H : Nat → Int → Bool} (hH : Obeys (b - 1) H) {s : Nat}"),
]
os.makedirs(out, exist_ok=True)
lake = os.path.expanduser('~/.elan/bin/lake')
ok = True
for name, a, b in M:
    assert base.count(a) == 1, (name, base.count(a))
    f = os.path.join(out, 'mut_%s.lean' % name)
    open(f, 'w', encoding='utf-8').write(base.replace(a, b))
    r = subprocess.run([lake, 'env', 'lean', f], capture_output=True, text=True, timeout=900)
    errs = [l for l in (r.stdout + r.stderr).splitlines() if ': error' in l]
    v = 'REJECTED' if r.returncode != 0 and errs else 'ACCEPTED'
    ok = ok and v == 'REJECTED'
    print(name, v, 'first error at line', errs[0].split(':')[1] if errs else '-',
          (errs[0].split(': error', 1)[1].strip()[:90] if errs else ''), flush=True)
print('ALL REJECTED' if ok else 'SOME ACCEPTED')
