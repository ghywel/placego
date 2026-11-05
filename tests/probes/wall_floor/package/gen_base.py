#!/usr/bin/env python3
"""gen_base.py (Local, L1548): the base kit module Rule30RightWall from the record's TwoPairs modules, with their proofs unchanged. The row, the tick and
the iterate become the kit's Rule30FrozenRuler.T and iter. Parts the wall does not use (the injectivity law, the shift, the classification) are left out."""
import re,sys
P=sys.argv[1]            # tests/probes/lean
def lines(f): return open(f'{P}/{f}.lean',encoding='utf-8').read().split('\n')
def rng(L,a,b): return '\n'.join(L[a-1:b])
def between(s,a,b):
    i=s.index(a); j=s.index(b,i); return s[i:j]
two=lines('TwoPairs')
twos='\n'.join(two)
out=[]
out.append('''module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30FrozenRuler

/-!
# Rule 30: the wall of a rain-tailed edge code

Read a row from its rightmost black cell, as in `Rule30FrozenRuler`: the row is an edge code, and one tick of rule 30 is the edge map `T`.
This module studies codes with a *rain tail*, cells that alternate from some index on. `T` keeps such a tail and so does every
predecessor, and the *wall* is the last equal pair below the tail. In the `Rule30EdgeStaircases` rain pair, `1010…` has no wall, while `11010…` has its wall at index 0.
The transport and nonperiodicity statements below require a window start at least 2; the local wall rule requires depth at least 5.

* `predecessor_unique`: every code has exactly one predecessor under `T`, so a backward tick is well defined.
* `top_up`, `top_stay`, `top_minus_one`, `top_minus_two`, `top_minus_three`: the wall moves by an exact local rule under `T`.
* `step_rain_tail`, `back_rain_tail`: the tail survives a forward tick and every backward tick.
* `front_back`, `front_not_periodic`: a code with one of eighteen windows of eleven cells at its wall has every predecessor of the same
  form three cells higher, whatever lies below the window, and it is not periodic.
* `deep_words`: three backward advances of three cells leave one of two words at the wall, the *letters* `A = ..####...##` and
  `B = .#.###...##`.
* `no_BB`, `no_AAA`: neither `BB` nor `AAA` occurs. `witness_AA`, `witness_AB`, `witness_BA`, `witness_ABA`: these words do occur.
* `reset`, `above`, `again`, `letters`: the ten-cell word `0, b, !b, 1, u, 1, 0, v, 0, 1`. It contains a reset word `0 1^(3m+1) 0`
  of the family in `Rule30ResetFreeRuns`, with inverse synchronization in `Rule30InverseCascade.run_resets` (kit PR 60), so nothing from below passes it, and with rain above it, it reappears three cells higher.
* `letter_after_B`, `letter_after_A`: the next letter, from the two new cells under the window.
* `Closed`, `Held`, `held_back`, `held_forever`, `held_not_periodic`: a closed set of windows holds a row for ever, whatever lies below.

Nothing here concerns the center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30RightWall

open Rule30FrozenRuler

set_option autoImplicit false
set_option maxRecDepth 8192

/-- A row: bit `0` is the rightmost black cell, bit `k` the cell `k` places behind it. -/
abbrev Row := Nat → Bool

/-- One tick of rule 30 on rows: the kit's edge map. -/
abbrev step : Row → Row := T

/-- `t` ticks, with the row first. -/
abbrev iter (x : Row) (t : Nat) : Row := Rule30FrozenRuler.iter t x
''')
# step lemmas and iter_add
out.append(rng(two,55,57))
out.append('')
out.append(rng(two,59,67))
out.append('')
out.append(between(twos,'/-! ## Rain tails survive both ways -/','/-! ## Controls -/').rstrip())
# transport
tr='\n'.join(lines('TwoPairsWindowTransport'))
out.append('\n/-! ## Forward transport of finite windows -/\n')
out.append(between(tr,'/-- Compute a forward word starting two cells above the input start. -/','/-- Inverse transport once the two lower input cells are specified. -/').rstrip())
six='\n'.join(lines('TwoPairsSixCertificate'))
out.append('\n'+between(six,'def contexts : Nat','/-- The supplied latest row consists').rstrip())
ret='\n'.join(lines('TwoPairsRetreat'))
out.append('\n/-! ## Three advances leave two letters -/\n')
out.append(between(ret,'/-- An alternating tail above one wall excludes every higher wall. -/','#print axioms marker').rstrip())
tm='\n'.join(lines('TwoPairsThreeMoves'))
out.append('\n'+between(tm,'def wordA : List Bool','#print axioms deep_words').rstrip())
st='\n'.join(lines('TwoPairsSettled'))
out.append('\n/-! ## The language of the letters -/\n')
out.append(between(st,'private theorem incompatible','#print axioms no_BB').rstrip())
ex='\n'.join(lines('TwoPairsWindowExclusions'))
out.append('\n/-- Extend bit 10 by alternation above the given eleven-bit source word. -/\n'+between(ex,'def source (w low L j : Nat)','private theorem source_alt').rstrip())
wl='\n'.join(lines('TwoPairsWallLanguage'))
out.append('\n'+between(wl,'private theorem read {x','#print axioms no_AAA').rstrip())
rs='\n'.join(lines('TwoPairsReset'))
out.append('\n/-! ## The shield -/\n')
out.append('namespace Reset\n\n'+between(rs,'/-- The reset word. -/','#print axioms reset').rstrip().replace('ThreeMoves.','')+'\n\nend Reset')
wc='\n'.join(lines('TwoPairsWindowClosed'))
out.append('\n/-! ## Closed sets of windows -/\n')
out.append('namespace WindowClosed\n\n'+between(wc,'/-- A window with seven cells of rain over its last. -/','#print axioms held_back').rstrip()+'\n\nend WindowClosed')
out.append(open(sys.argv[3],encoding='utf-8').read().rstrip())
out.append('\nend Ruliology.CellularAutomata.Rule30RightWall\n')
s='\n'.join(out)
s=s.replace('Six.contexts','contexts').replace('Six.mem_contexts','mem_contexts').replace('Retreat.marker','marker').replace('simp [shrinkN, iter]','simp [shrinkN, iter, Rule30FrozenRuler.iter]')
s=s.replace('if_neg','ite_eq_right').replace('if_pos','ite_eq_left').replace('if_true','ite_true')
# names: the sections each have their own `inp`, `seg_inp`, `chk_*`
open(sys.argv[2],'w',encoding='utf-8').write(s)
print(len(s))
