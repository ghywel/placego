"""GC1115: recover renewal markers from the positive left20 code.

Missing inference: GC1110's positive code destroys the canonical
sparse phase template. Does it erase mixed renewal information,
or carry a finite hidden language in a different bit presentation?
Record searched: GC1110|left.?20|depth.?20|column.?20 with
 decoder|invert|recover|zero.*3.*2|recogn ->5 hits in5files,
all unrelated; GC1110 and GC1108 read, no new canonical-depth scan.
Let b_u=x_-20(2u-14), u>=7, as already proved in GC1110.
P1 BEFORE controls: ell_r=(1-b_(r+1))(1-b_(r+4))(1-b_(r+6))
is exactly the marker whose next gap is L, on every S/L word.
P2 BEFORE controls: under no S^5, let J be the nearest ell marker
in {u,u-1,...,u-16}. Then q_u=1 iff J's distance is0,5,8,11,14.
Thus b[u-15..u+6] decodes q_u using22 even samples, for u>=22;
all physical observation times precede the target time2u.
REFUTED-BY: any local detector error or bounded-guard decoder error.
Counterfactual: b alone locally decodes every S/L word with no
S-run bound. All-S at different marker phases must refute this:
its b is identically1 for every phase.
Controls: exact positive-block spelling versus literal Rule30
inverse triangles; independent physical h(S)/h(L) even samples;
all phases of six-gap cyclic words, including isolated L and
four-S boundary cases. The proof is run-spacing, not this census.
Unexpected: even with a lossless inverse, neither b nor its bit
complement can serve as a new S/L visible input: b has11 and,
when any L occurs, its complement has marker gap2. This prevents
claiming depth closure or iteration of the fixed-depth inverse.
No CA membership, CUT, solver, records, widening or depth sweep.
OUTCOME: P1/P2 HELD on 1536 detector and literal inverse samples,
1398 bounded-guard decoder samples, including29 isolated-L and6
four-S controls. The unbounded-S inverse claim is REFUTED by
phase-shifted all-S words with identical b. The 22-sample decoder
uses physical times0..42 for its first target at44. Both plain
image reuse choices fail; decorated depth closure remains OPEN.
"""
from itertools import product
import rule30_sl_phase_collision as prior


def code(letters):
    q=[0]*sum(3 if a=='S' else 5 for a in letters)
    b=[]; r=0
    for i,a in enumerate(letters):
        q[r]=1
        block='10110' if a=='L' else ('111' if letters[i-1]=='S' else '101')
        b.extend(map(int,block));r+=len(block)
    h=''.join('110100' if a=='S' else '1101000100' for a in letters)
    assert tuple(q)==tuple(map(int,h[::2]))
    return q,b


def l_markers(b):
    n=len(b)
    return [int(not b[(r+1)%n] and not b[(r+4)%n]
                and not b[(r+6)%n]) for r in range(n)]


def decode(b):
    ell=l_markers(b);n=len(b);out=[]
    for u in range(n):
        j=next((j for j in range(17) if ell[(u-j)%n]),None)
        assert j is not None,'missing bounded-past L marker'
        out.append(int(j in (0,5,8,11,14)))
    return out


def main():
    detector_checks=decoder_checks=isolated=four=0
    for letters in product('SL',repeat=6):
        q,b=code(letters);n=len(q);ell=l_markers(b)
        expected=[0]*n;r=0
        for a in letters:
            expected[r]=int(a=='L');r+=3 if a=='S' else 5
        assert ell==expected
        for u in range(n):
            window=[q[(u-7+i)%n] for i in range(11)]
            assert prior.literal(window)[20][0]==b[u]
            detector_checks+=1
        cyclic=''.join(letters)*3
        if 'SSSSS' not in cyclic:
            assert decode(b)==q
            decoder_checks+=n
            isolated+=int('SLS' in cyclic)
            four+=int('SSSS' in cyclic)
        assert '11' in ''.join(map(str,b))*2
        if 'L' in letters:
            assert '101' in ''.join(str(1-x) for x in b)*2
    qa,ba=code('SSSSSS')
    qb=qa[1:]+qa[:1]
    assert qa!=qb and ba==[1]*len(ba)
    # Independently force shifted all-S windows: the same dense output.
    for u in range(len(qb)):
        window=[qb[(u-7+i)%len(qb)] for i in range(11)]
        assert prior.literal(window)[20][0]==1
    assert len(range(-15,7))==22
    assert 2*(22-15)-14==0 and 2*(22+6)-14==42<44
    print(dict(P1='HELD',P2='HELD',detector_samples=detector_checks,
               decoder_samples=decoder_checks,isolated_L_controls=isolated,
               four_S_controls=four,input_window=22,first_target_time=44,
               last_observation_time=42,all_S_phase_counter='REFUTED',
               image_reuse='b has11; complement has gap2',
               depth_iteration='OPEN',record_bound='OPEN'))


if __name__=='__main__':main()
