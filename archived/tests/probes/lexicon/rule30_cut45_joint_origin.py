"""GC1039: joint entry/suffix origin compatibility at the existing width24.

Missing inference: CL207's 581 suffix-compatible origins omit the entry
past. Does imposing that past force CL198's common19 row30 pins?
Record searched: (CL207|581|common.pin) + (joint|past|entry) -> GC1038
scope correction only, no joint origin computation.
P1: the joint relation forces all19 common pins (confidence0.45).
P2: some joint origin survives, since the44-prefix is actually realized.
Counterfactual: suffix-only nonpinning does not imply joint nonpinning;
joint nonpinning still does not refute the exact-cone pinning census.
Controls: independently exhaustive six-tick literal forward histories
against forward/backward graph extraction; GC1037 parent truth tables.
Unexpected check: require the suffix-only extraction to reproduce581
before using it, and the original pinned row to survive the joint join.
Reuse CL207's suffix relation, not a new SAT or actual-language query.
Memory-efficient implementation stores row sets then reverses edges,
instead of re-enumerating origin-provenance bitsets of size65536.
Caps: 150000 rows per future layer,20000 per past layer,120seconds.
One width24 join, no wider strip or pin-subset sweep.
First outcome: P1/P2 HELD. The581 suffix origins reduce to TWO joint
origins, common23 cells10011001100110000000001?,45 initial rows,
past peak2857. PIN is one of the two. Common-pin forcing thus follows
from the entry/suffix join, given only the first8 origin pins.
Adaptive support lemma, preregistered before its run: P3, those first8
pins follow from q's samples at20..32 plus the proved train slab/gate
at34, using a width12 reverse relation to20 (confidence0.6). It removes
the last inherited pinning census if true; if false, retain the common8
premise rather than extend the window. Positive realizer: CL193's seed.
P3 REFUTED narrowly: the support relation fixes the first7 cells to
1001100 but permits either x8 value (peak95). Before the new branch:
P4, the original width24 entry/suffix join with x8=0 is empty (0.8).
This uses the full prescribed entry, not a progressively enlarged past
window. It tests the remaining one-bit premise in the SAME join.
Do not increase any cap. If P4 fails, retain first8 as inherited and stop.
FINAL OUTCOME: P4 HELD. The4975 x8=0 suffix origins have no leading0
entry past, peak7300. Together with the nonvacuous first7 support lemma
and the two x8=1 joint origins, this discharges ALL common19 pins using
proved train rigidity and exact correlated-strip relations, without SAT.
The stronger joint conclusion fixes the first23 cells, leaving only24
free. This explains this one cut; an all-depth record bound is still open.
"""

import signal
from rule30_cut45_origin_past import ENTRY, PIN, controls, parents, literal
from rule30_cut45_pin_guard import WORD, step, FREE


def suffix_origins(roots,width,start,end,predicate,advance):
    layers = {start:{s for s in roots if predicate(start,s)}}
    for t in range(start,end):
        layer = {advance(s,t%2,e,width) for s in layers[t] for e in (0,1)}
        layers[t+1] = {s for s in layer if predicate(t+1,s)}
        if len(layers[t+1]) > 150000:
            raise RuntimeError('future row cap; no conclusion')
    suffix = layers[end]
    for t in range(end-1,start-1,-1):
        suffix = {p for s in suffix for p,_ in parents(s,t%2,width)
                  if p in layers[t]}
    return suffix,max(map(len,layers.values()))


def graph_control():
    samples = {0:0,2:1,4:0,6:0}
    predicate = lambda t,s:t not in samples or s&1 == samples[t]
    expected = set()
    for initial in range(64):
        for inputs in range(64):
            s = initial
            for t in range(7):
                if not predicate(t,s):
                    break
                if t < 6:
                    s = literal(s,t%2,(inputs>>t)&1,6)
            else:
                expected.add(initial)
    assert expected and 0 in expected
    actual,_ = suffix_origins(range(64),6,0,6,predicate,step)
    assert actual == expected
    print('independent literal two-sided graph control PASS',len(expected),flush=True)


def keep(t,s):
    if t%2 == 0 and t<=86 and s&1 != int(WORD[t//2]):
        return False
    if t%4 == 2 and 34<=t<=62 and (s>>6)&1 != int(t==62):
        return False
    return True


def main():
    controls()
    graph_control()
    prefix = sum(int(c)<<i for i,c in enumerate(PIN[:8]))
    candidates,peak = suffix_origins((prefix|(tail<<8) for tail in range(65536)),
                                    24,30,86,keep,step)
    print('suffix_origins',len(candidates),'peak',peak,flush=True)
    assert len(candidates) == 581,'must reproduce CL207 before the join'
    sources = sorted(candidates)
    rows = {s:(1<<i,0,s) for i,s in enumerate(sources)}
    past_peak = len(rows)
    for t in range(29,-1,-1):
        nxt = {}
        for child,(labels,inputs,origin) in rows.items():
            for parent,exterior in parents(child,t%2,24):
                if t%2 == 0 and parent&1 != int(ENTRY[t//2]):
                    continue
                if parent in nxt:
                    oldlabels,oldinputs,oldorigin = nxt[parent]
                    nxt[parent] = (oldlabels|labels,oldinputs,oldorigin)
                else:
                    nxt[parent] = (labels,inputs|(exterior<<t),origin)
        rows = nxt
        past_peak = max(past_peak,len(rows))
        if len(rows)>20000:
            raise RuntimeError('past row cap; no pinning conclusion')
    alive = 0
    for labels,_,_ in rows.values():
        alive |= labels
    joint = [s for i,s in enumerate(sources) if alive&(1<<i)]
    pinned = sum(int(c)<<i for i,c in enumerate(PIN))
    assert pinned in joint,'actual pinned origin must survive relaxed joint relation'
    common = ''.join(str((joint[0]>>i)&1) if all(((s>>i)&1)==((joint[0]>>i)&1)
                      for s in joint) else '?' for i in range(24))
    common_pins = [i for i in range(1,25) if i not in FREE]
    forced = all(common[i-1] == PIN[i-1] for i in common_pins)
    print('joint_origins',len(joint),'initial_rows',len(rows),'past_peak',past_peak,
          'common',common,'P1',forced,'P2',bool(joint),flush=True)
    if not forced:
        initial,(labels,inputs,origin) = next((s,v) for s,v in rows.items()
            if any(((v[2]>>(i-1))&1)!=int(PIN[i-1]) for i in common_pins))
        s = initial
        for t in range(30):
            if t%2 == 0:
                assert s&1 == int(ENTRY[t//2])
            s = literal(s,t%2,(inputs>>t)&1,24)
        assert s == origin and origin in candidates
        print('off-pin initial',format(initial,'024b')[::-1],
              'past_inputs',format(inputs,'030b')[::-1],
              'origin30',format(origin,'024b')[::-1],
              'past literal replay PASS; suffix membership by exact graph',flush=True)
    supported = entry_interface()
    wrong_empty = wrong_eighth_bit(False)
    print('COMMON-PIN LEMMA',forced and supported and wrong_empty,
          'all-depth bound OPEN',flush=True)


def entry_interface():
    # GC1027 gives this slab and successful gate at the second car (t34).
    width = 12
    prefix = sum(int(c)<<i for i,c in enumerate('1001100'))
    rows = {prefix|(tail<<7):0 for tail in range(32)}
    peak = len(rows)
    for t in range(33,19,-1):
        nxt = {}
        for child,labels in rows.items():
            for parent,_ in parents(child,t%2,width):
                if t%2 == 0 and parent&1 != int(WORD[t//2]):
                    continue
                newlabel = 1<<(parent&255) if t==30 else labels
                nxt[parent] = nxt.get(parent,0)|newlabel
        rows = nxt
        peak = max(peak,len(rows))
        if len(rows)>20000:
            raise RuntimeError('interface row cap; no first8 inference')
    mask = 0
    for labels in rows.values():
        mask |= labels
    prefixes = [format(k,'08b')[::-1] for k in range(256) if mask&(1<<k)]
    assert prefixes,'support lemma must not have an empty past'
    seed = ('011111100111010100110001100011001001011110110010011010001010011110111000'
            '10100110111010000000000000000000')
    bits = list(map(int,seed))
    for t in range(35):
        if t==30:
            assert ''.join(map(str,bits[:8])) in prefixes
        if t==34:
            assert ''.join(map(str,bits[:7])) == '1001100'
        if 20<=t<=34 and t%2 == 0:
            assert bits[0] == int(WORD[t//2])
        if t<34:
            padded = [t%2]+bits
            bits = [((30>>(4*padded[i]+2*padded[i+1]+padded[i+2]))&1)
                    for i in range(len(bits)-1)]
    print('P3',prefixes == [PIN[:8]],'origin_prefixes',prefixes,
          'peak',peak,'CL193 actual model control PASS',flush=True)
    return all(p[:7] == '1001100' for p in prefixes)


def wrong_eighth_bit(check_controls=True):
    if check_controls:
        controls()
        graph_control()
    prefix = sum(int(c)<<i for i,c in enumerate('10011000'))
    candidates,peak = suffix_origins((prefix|(tail<<8) for tail in range(65536)),
                                    24,30,86,keep,step)
    print('wrong-x8 suffix_origins',len(candidates),'peak',peak,flush=True)
    rows = set(candidates)
    past_peak = len(rows)
    for t in range(29,-1,-1):
        rows = {p for s in rows for p,_ in parents(s,t%2,24)
                if t%2 != 0 or p&1 == int(ENTRY[t//2])}
        past_peak = max(past_peak,len(rows))
        if len(rows)>20000:
            raise RuntimeError('wrong-x8 past row cap; no conclusion')
    print('P4',not rows,'initial_rows',len(rows),'past_peak',past_peak,flush=True)
    return not rows


if __name__ == '__main__':
    import sys
    signal.signal(signal.SIGALRM,
                  lambda *_:(_ for _ in ()).throw(RuntimeError('time cap; no conclusion')))
    signal.alarm(120)
    try:
        if '--wrong-x8' in sys.argv:
            wrong_eighth_bit()
        else:
            main()
    finally:
        signal.alarm(0)
