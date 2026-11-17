#!/usr/bin/env python3
"""GC407: time-translate reviewed G210 into the recorded class12 front.
Before run: G210 and observed5(s-2)=0 force6(s-6)=0 under anchor at s-14.
Counterfactual full exterior uniqueness: not implied; GC393 still has eight
relaxed histories after fixing that bit. No full census repeat.
Control: reference word indexing and actual observation reconstruction.
Unexpected check: does a reference anchor recur exactly12 ticks later?
OUTCOME: anchor phases8,18,28,38,54; every reference pair satisfies G210;
none regenerates the anchor after12. Actual phase54 pair is0,0 versus1,1.
The implication explains one forced exterior defect, not the entire path,
first defect time, long preparation or death127. Under0.1 seconds.
"""
import json
from rule30_gpt_gate_completion import WORDS,EXTRA,target


def main():
    words={**EXTRA,**WORDS}
    # Independent indexing: zip creates the five-cell spatial words at each phase.
    spatial=[''.join(bits) for bits in zip(*(words[j] for j in range(2,7)))]
    anchors=[p for p in range(0,56,2) if spatial[p]=='11100']
    assert anchors==[p for p in range(0,56,2)
                     if ''.join(words[j][p] for j in range(2,7))=='11100']
    rows=[]
    for p in anchors:
        a=int(words[6][(p+8)%56]);c=int(words[5][(p+12)%56])
        assert not a or c
        rows.append({'phase':p,'six_after8':a,'five_after12':c,
                     'anchor_after12':spatial[(p+12)%56]})
    assert [target(j,-14) for j in range(2,7)]==[1,1,1,0,0]
    assert target(5,-2)==target(6,-6)==0
    print(json.dumps({'even_anchor_phases':anchors,'reference_pairs':rows,
        'class12_anchor_phase':54,'observed_five_at_minus2':target(5,-2),
        'forced_six_at_minus6':0,'actual_six_at_minus6':target(6,-6),
        'direct12_step_anchor_regeneration':any(r['anchor_after12']=='11100' for r in rows)},indent=2))


if __name__=='__main__':main()
