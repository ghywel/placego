#!/usr/bin/env python3
"""Bounded necessary-condition audit for G9's arbitrary-period potential.
COMMAND: PYTHONDONTWRITEBYTECODE=1 python3 tests/probes/lexicon/rule30_gpt_cycle_obstructions.py
RUN-ON: GPT Intel CPU, one process, Python 3.10+ standard library.
COST: complete pair graphs P=1..10, at most1048576 pairs; no Local side run.
PREDICTIONS before first run, 2026-10-06:
 CC0 controls: all cycles satisfy scalar Rule30 compatibility; known
     P1,2,3,4,8 maxima are0,1,7/6,7/3,7/3. Every maximizing clock loop
     closes and its exact mean agrees with independent scalar scans.
 CC1 blind: every P=1..10 maximum is at most7/3 (small-period plateau).
 CC2 blind: every maximum is at most5/2 (necessary for the G8 candidate).
 CC3 blind: every maximum is strictly below3 (necessary for some sub3
     budget on the broader periodic-compatible domain).
 CC4 unexpected control: odd non-power-of-two periods5,7,9 are included;
     lifting a P4 witness by repeating its bits to P8 preserves its mean.
 CF must reject: slope2 can charge every compatible clock cycle. The
     known valid P4 cycle advances28 over12 edges, excess4 at slope2.
 REFUTED-BY: a control fails, or a printed mean violates a blind threshold.
 Print each maximizing word list and its recurrent phase/loop certificate
 if CC2 fails. Never identify a full-line cycle as a finite-seed side.
 Non-power-of-two obstructions alone cannot refute the power-of-two
 edge-domain candidate. No potential-size bound follows from CC2 holding.
OUTCOME 2026-10-06 06:32 BST, cycle run: ALL CONTROLS PASS.
 CC0 maxima P1..10:0,1,7/6,7/3,15/8,5/2,5/2,7/3,1006/493,89/41.
 CC1 REFUTED at P6/P7; held at the other eight periods.
 CC2/CC3 HELD at all ten periods. CC4 and CF passed.
 Wrapper printed the log after Python; its exit0 masks Python's return.
 The diagnostic's return expression is1 because CC1 failed; actual Python
 process exit was not captured. Preserve this harness limitation.
ADDENDUM before run with argument "potential":
 AP0 controls: construct G9.4's quotient potential at EVERY P1..10;
     check every quotient edge, independently lift every phase/forward
     child at P<=8, and match G8's known maxima at P1,2,3,4,8.
 AP1 blind: max_h/2<=4P at each period, as in the earlier LP1 candidate.
 AP2 counterfactual: zero potential fails a valid P4 delay4 edge.
 Unexpected check: AP includes odd periods with tight mean5/2 at P7;
     positive excess in a zero-total-weight cycle must still propagate
     to a finite potential. All arrays remain outside git.
 Cap50million edge-relaxation attempts per P; stopping is PARTIAL,
 not a certificate. REFUTED-BY: any edge/lift/known-value check fails,
 cap reached, AP1 too large, or zero counterfactual not rejected.
OUTCOME aligned potential run: exit1, ALL CONTROLS PASS.
 AP0 max_h P1..10:0,0,2,6,10,21,37,45,59,97; every quotient edge
 passed; independent phase/forward-child lifts through P8 passed.
 AP1 REFUTED at P10: debt97/2 exceeds4P=40; held at P1..9.
 AP2 zero counterfactual rejected. No cap reached.
CERTIFICATE EXPANSION before run with argument "witness":
 CC5 control: expand the known P7 maximum into its scalar closed loop.
 AP3 control: reconstitute only P10's potential and extract a tight path
     from a maximizing state to potential0. Convert aligned pairs back
     to actual words; scalar compatibility and elapsed time must give
     signed reward97. This is independent validation of the existing
     maximum, not a new blind discovery. AP1 must still fail at P10;
     witness mode therefore returns1 even when all controls pass.
OUTCOME witness expansion 2026-10-06 06:35 BST: exit1, ALL CONTROLS PASS.
 CC5 P7 words [97,101,56,57,14,46,67,75,112,114,28,92,7,23],
     recurrent phase2, one spatial circuit14, elapsed35, mean5/2.
 AP3 P10:39 edges, elapsed146, signed reward97, terminal_h0.
     All39 scalar triple equations at all10 residues and next-black
     scans passed. Complete literal words/delays retained in G10.3.
 AP1 remains refuted, so exit1 is expected. No control failure.
"""
from fractions import Fraction
from rule30_gpt_local_front import pair_cycles, maximum_mean
from rule30_gpt_front import waiting
from rule30_gpt_cycles import bit


def clock_loop(words,p):
    best=Fraction(-1);cert=None
    tables=[waiting(w,p) for w in words]
    for initial in range(p):
        time=initial;circuits=0;seen={}
        while time%p not in seen:
            seen[time%p]=(circuits,time)
            for table in tables:time+=table[time%p]
            circuits+=1
        old_c,old_t=seen[time%p]
        loops=circuits-old_c;elapsed=time-old_t
        mean=Fraction(elapsed,loops*len(words))
        if mean>best:best,cert=mean,(old_t%p,loops,elapsed)
    return best,cert


def scalar_certificate(words,p,cert):
    phase,loops,expected=cert;time=phase
    for _ in range(loops):
        for word in words:
            if word:
                while not bit(word,time,p):time+=1
                time+=1
    return time-phase==expected and time%p==phase


def compatible(words,p):
    n=len(words)
    return all(bit(words[(j+1)%n],t+1,p)==
               (bit(words[(j-1)%n],t,p) ^
                (bit(words[j],t,p) | bit(words[(j+1)%n],t,p)))
               for j in range(n) for t in range(p))


def main():
    controls=[];blinds=[]
    known={1:Fraction(0),2:Fraction(1),3:Fraction(7,6),4:Fraction(7,3),8:Fraction(7,3)}
    for p in range(1,11):
        cycles=pair_cycles(p);best=Fraction(-1);witness=None;valid=True
        cyclic_states=0
        for cycle in cycles:
            words=[node&((1<<p)-1) for node in cycle]
            valid &= compatible(words,p);cyclic_states+=len(cycle)
            mean,cert=clock_loop(words,p)
            if p<=5:valid &= maximum_mean(words,p,True)[0]==mean
            if mean>best:best,witness=mean,(words,cert)
        words,cert=witness
        valid &= scalar_certificate(words,p,cert)
        valid &= p not in known or best==known[p]
        controls.append(valid)
        print(('PASS' if valid else 'FAIL')+' CC0 P%d: pairs%d cycles%d cyclic_states%d maximum%s; spatial_length%d recurrent_phase%d loops%d elapsed%d'%
              (p,1<<(2*p),len(cycles),cyclic_states,best,len(words),*cert),flush=True)
        for name,bound,strict in [('CC1',Fraction(7,3),False),('CC2',Fraction(5,2),False),('CC3',Fraction(3),True)]:
            okay=best<bound if strict else best<=bound;blinds.append(okay)
            print(('HELD' if okay else 'REFUTED')+' %s P%d: %s %s %s'%(name,p,best,'<' if strict else '<=',bound),flush=True)
        if best>Fraction(5,2):print('WITNESS P%d words=%r recurrent=%r'%(p,words,cert),flush=True)
    fixed=[9,8,14,12,4,7,6,2,11,3,1,13]
    lifted=[w|(w<<4) for w in fixed]
    okay=compatible(fixed,4) and compatible(lifted,8) and clock_loop(lifted,8)[0]==Fraction(7,3)
    controls.append(okay);print(('PASS' if okay else 'FAIL')+' CC4 lifted period4 witness retains7/3 at period8',flush=True)
    rejected=compatible(fixed,4) and scalar_certificate(fixed,4,(3,1,28)) and 28>2*12
    controls.append(rejected);print(('PASS' if rejected else 'FAIL')+' CF slope2 rejected: valid cycle28 over12',flush=True)
    print('ALL CONTROLS PASS' if all(controls) else 'CONTROL FAILURE',flush=True)
    return not all(controls) or not all(blinds)



def aligned_potential_main(periods=range(1,11),extract=False):
    """Complete quotient certificate; arrays reconstructed outside git."""
    from array import array
    from collections import deque
    from rule30_gpt_local_front import predecessor
    controls=[];blinds=[]
    known={1:0,2:0,3:2,4:6,8:45}
    for p in periods:
        count=1<<(2*p);mask=(1<<p)-1
        head=array('i',[-1])*count;source=array('I');link=array('i');weight=array('h')
        def rotate(w,d):
            d%=p
            return ((w>>d)|(w<<(p-d)))&mask
        for child in range(count):
            b,c=child>>p,child&mask
            parent=predecessor(child,p)
            d=(b & -b).bit_length() if b else 0
            target=(rotate(b,d)<<p)|rotate(c,d)
            source.append(parent);weight.append(2*d-5)
            link.append(head[target]);head[target]=child
        values=array('I',[0])*count;queue=deque(range(count));queued=bytearray([1])*count
        updates=0;attempts=0
        while queue:
            target=queue.popleft();queued[target]=0;edge=head[target]
            while edge!=-1:
                attempts+=1
                if attempts>50000000:raise RuntimeError('AP cap: partial certificate, not a pass')
                parent=source[edge];candidate=values[target]+weight[edge]
                if candidate>values[parent]:
                    values[parent]=candidate;updates+=1
                    if not queued[parent]:queue.append(parent);queued[parent]=1
                edge=link[edge]
        valid=True
        for target in range(count):
            edge=head[target]
            while edge!=-1:
                valid &= values[source[edge]]>=weight[edge]+values[target]
                edge=link[edge]
        if p<=8:
            # Independent forward children and phase lifts audit every original edge.
            from rule30_gpt_waiting import children
            for pair in range(count):
                a,b=pair>>p,pair&mask
                for c in children(a,b,p):
                    for r,d in enumerate(waiting(b,p)):
                        aligned=(rotate(a,r)<<p)|rotate(b,r)
                        target=(rotate(b,r+d)<<p)|rotate(c,r+d)
                        valid &= values[aligned]>=2*d-5+values[target]
        maximum=max(values);where=values.index(maximum)
        valid &= len(source)==count and (p not in known or maximum==known[p])
        controls.append(valid);blinds.append(maximum<=8*p)
        print(('PASS' if valid else 'FAIL')+' AP0 P%d: quotient states/edges%d max_h%d debt%s maximizing(A,B)%r updates%d attempts%d'%
              (p,count,maximum,Fraction(maximum,2),(where>>p,where&mask),updates,attempts),flush=True)
        print(('HELD' if blinds[-1] else 'REFUTED')+' AP1 P%d: debt<=4P'%p,flush=True)
        if extract:
            from rule30_gpt_waiting import children
            todo=deque([where]);parents={where:None};end=None
            while todo:
                pair=todo.popleft()
                if values[pair]==0:end=pair;break
                a,b=pair>>p,pair&mask
                d=(b & -b).bit_length() if b else 0
                for c in children(a,b,p):
                    target=(rotate(b,d)<<p)|rotate(c,d)
                    if values[pair]==2*d-5+values[target] and target not in parents:
                        parents[target]=(pair,d);todo.append(target)
            assert end is not None,'least potential must have a tight path to zero'
            path=[];pair=end
            while parents[pair] is not None:
                prev,d=parents[pair];path.append((prev,pair,d));pair=prev
            path.reverse();phase=0;elapsed=0
            words=[where>>p,where&mask];delays=[]
            for prev,target,d in path:
                phase=(phase+d)%p;elapsed+=d;delays.append(d)
                words.append(rotate(target&mask,-phase))
            scalar=0
            for word in words[1:-1]:
                if word:
                    while not bit(word,scalar,p):scalar+=1
                    scalar+=1
            valid_path=all(bit(words[j+1],t+1,p)==(bit(words[j-1],t,p) ^
                    (bit(words[j],t,p)|bit(words[j+1],t,p)))
                    for j in range(1,len(words)-1) for t in range(p))
            assert valid_path and scalar==elapsed and 2*elapsed-5*len(path)==maximum
            print('PASS AP3 exact maximal-debt witness: P%d edges%d elapsed%d reward%d terminal_h0'%
                    (p,len(path),elapsed,maximum),flush=True)
            print('AP3 words=%r delays=%r'%(words,delays),flush=True)

    fixed=[9,8,14,12,4,7,6,2,11,3,1,13]
    # The zero potential has a valid positive-weight edge of delay4.
    rejected=compatible(fixed,4) and max(waiting(8,4))==4 and 2*4-5>0
    controls.append(rejected);print(('PASS' if rejected else 'FAIL')+' AP2 zero-potential counterfactual rejected',flush=True)
    print('ALL CONTROLS PASS' if all(controls) else 'CONTROL FAILURE',flush=True)
    return not all(controls) or not all(blinds)


if __name__=='__main__':
    import sys
    if sys.argv[1:]==['witness']:
        best=Fraction(-1);chosen=None
        for cycle in pair_cycles(7):
            words=[node&127 for node in cycle];mean,cert=clock_loop(words,7)
            if mean>best:best,chosen=mean,(words,cert)
        words,cert=chosen
        assert best==Fraction(5,2) and compatible(words,7) and scalar_certificate(words,7,cert)
        print('PASS CC5 exact P7 witness: words=%r recurrent=%r mean%s'%(words,cert,best),flush=True)
        raise SystemExit(aligned_potential_main([10],True))
    raise SystemExit(aligned_potential_main() if sys.argv[1:]==['potential'] else main())
