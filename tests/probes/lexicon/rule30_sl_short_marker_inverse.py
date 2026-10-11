"""GC1108: the nonlinear left12 carrier has a finite inverse.

Missing inference: does GC1107's short-marker forget the L choices in
the recurrent mixed output? A lossless finite inverse would give a
sound finite-language representation on the left without affine fits.
Record searched: short.marker|short.gap|left12|twelfth|13.gap with
inverse|reconstruct|lossless|recover|paired|entropy ->4 hits2files;
GC624/1008 and GC1107 checked. No such inverse in those sources.

P1 BEFORE controls: z_s=q_s*q_(s+3) reconstructs every S/L trace
having at most two consecutive L by
 q_s=z_s OR z_(s-3) OR [z_(s-8) AND NOT z_(s-5)].
Counterfactual: dropping the guard gives the same inverse; all-S
must expose the spurious residue created by that unguarded term.
Independent controls: every cyclic length8 gap word with no LLL;
the published temporal h(S)/h(L) determines q independently of
the gap-position generator. Retain a cyclic SLLL counter to P1
without its premise. No actual realization is asserted for controls.
P2 BEFORE code control: GC1106 FE and EF yield distinct left12
even words, first differing at physical tick34, while their column1
words first differ at44. Their common future prefix makes the
left12 blocks concatenate independently of the next choice.
Unexpected check: L runs of length1 also satisfy P1; exact LL
pairs are stronger than the inverse needs. The full image language
has gaps3/8/13, whereas typed-A mixed outputs have only3/13.
No record, solver, membership, wider-strip or depth scan. The
finite inverse preserves entropy; pruning the L markers is not
an entropy reduction or an all-depth support-growth certificate.
OUTCOME: P1/P2 HELD on131 cyclic gap controls, including82 with
an isolated L; both guardedness/premise countercontrols fail as
predicted. The left12 code first differs at34 and its complete
inverse triangles agree. All-depth transport remains OPEN.
"""
from itertools import product


def gap_markers(letters):
    q=[0]*sum(3 if a=='S' else 5 for a in letters)
    s=0
    for a in letters:
        q[s]=1;s+=3 if a=='S' else 5
    return tuple(q)


def lifted(letters):
    return ''.join('110100' if a=='S' else '1101000100' for a in letters)


def short(q):
    return tuple(a*q[(s+3)%len(q)] for s,a in enumerate(q))


def decode(z,guard=True):
    n=len(z)
    return tuple(z[s]|z[(s-3)%n]|(z[(s-8)%n]&
                 (1-z[(s-5)%n] if guard else 1)) for s in range(n))


def left12(q):
    n=len(q)
    return tuple(v for s in range(n)
                 for v in (q[(s+2)%n]*q[(s+5)%n],
                           q[(s+4)%n]|q[(s+6)%n]))


def no_three_l(letters):
    return 'LLL' not in ''.join(letters)*2


def main():
    count=singles=0
    for letters in product(('S','L'),repeat=8):
        if not no_three_l(letters):continue
        q=gap_markers(letters)
        assert q==tuple(map(int,lifted(letters)[::2]))
        z=short(q);assert decode(z)==q
        n=len(q);points=[s for s,v in enumerate(z) if v]
        gaps=[(points[(i+1)%len(points)]-s)%n or n
              for i,s in enumerate(points)]
        assert set(gaps)<={3,8,13}
        if 'LSL' in ''.join(letters)*2:singles+=1
        count+=1
    q=gap_markers('SSS');assert decode(short(q),False)!=q
    q=gap_markers('SLLL');assert decode(short(q))!=q
    f='SLLSSS'
    e='SLLS'+'SLLSS'*3+'SLLSSS'
    q0,q1=gap_markers(f+e),gap_markers(e+f)
    assert len(q0)==len(q1)==117
    assert q0[:6]==q1[:6]  # Every future sample needed by left12.
    a,b=left12(q0),left12(q1)
    first=next(i for i,(x,y) in enumerate(zip(a[::2],b[::2])) if x!=y)*2
    assert first==34
    assert next(i for i,(x,y) in enumerate(zip(lifted(f+e),lifted(e+f))) if x!=y)==44
    # Independent complete inverse triangles, not just the new formula.
    from rule30_sl_left_short_marker import left_columns
    for q,out in ((q0,a),(q1,b)):
        c=left_columns(q+q[:6])[12]
        assert c[:234]==out
        z=short(q);assert decode(z)==q
    print(dict(cyclic_gap_controls=count,single_L_controls=singles,
               inverse='z[s] OR z[s-3] OR (z[s-8] AND NOT z[s-5])',
               image_gap_alphabet=[3,8,13],typed_A_alphabet=[3,13],
               left12_code_ticks=234,first_even_difference=first,
               inverse_guard_counter='SSS',premise_counter='SLLL',
               depth_advancing_update='OPEN',record_bound='OPEN'))


if __name__=='__main__':main()
