"""GC1123: exact macro-language transfer of L630's f69, including endpoints.

Missing inference: f69 removes the named E_m bridges, but what does it
remove from the whole paired-L macro language, and is an immediate122
rejection sound for finite black-A return chains? A precise finite guard
would constrain surviving111 paths without claiming the SCC closed.
Record searched: f69/69-bit/69 bits with122/macro/spacing/prefix ->3 hits,
GC1121/1122 prefix application and current room state; no exact macro guard.
P1 BEFORE execution: on continued M_k=SLLS^k, k>=1, f69 occurs iff the
macro word contains122. For a FINITE completed chain read with its final
black-A endpoint1, it occurs iff122 has at least one further macro.
P2 BEFORE execution: a four-state parser 0,1,12,122 is exact for that
finite language. State122 is an allowed terminal state with no outgoing
macro. Every word on k>=2 is allowed by this cut, including M3 forever.
The111 obstruction is therefore not removed by this cut alone.
REFUTED-BY: a literal factor/parser disagreement or failed FIRST-L parsing.
Counterfactual: reject122 as soon as its third macro completes, even for
finite chains. Must fail on the finite word122 plus its final endpoint.
Independent controls: physical h versus gap spelling, literal substring
matching versus the four-state parser, FIRST-L-window recognition.
Unexpected check: raw1221 has70 visible samples and avoids f69, but its
completed black-A endpoint at sample70 makes f69 appear at offset2.
Do not silently replace finite cone membership by infinite extension.
Controls enumerate complete four-macro cones, not spatial depths or
actual right-language membership. Unbounded k is covered by the hand
marker-spacing proof;17 is its independent long-S control.
OUTCOME: P1/P2 HELD on341 complete cones and the independent controls.
FIRST-L offsets1,17,36,55 force spacings16,19,19. The raw1221
endpoint counter holds; terminal122 remains accepted; M3 survives.
These controls do not test actual language membership or replace the
unbounded-k hand proof in RULE30-GPT.md GC1123.
"""

from itertools import product
import rule30_mixed_cut_transfer as spell


F69='010000100001001001000010000100100100100001000010010010010000100001001'
H='10000100001'


def parser(word):
    state=0
    for k in word:
        if state==3:
            return False
        if k==1:
            state=1
        elif k==2:
            state={0:0,1:2,2:3}[state]
        else:
            assert k>=3
            state=0
    return True


def direct_macro_guard(word):
    return all(word[i:i+3]!=(1,2,2) for i in range(len(word)-3))


def main():
    assert len(F69)==69
    assert [i for i in range(59) if F69[i:i+11]==H]==[1,17,36,55]
    assert [17-1,36-17,55-36]==[16,19,19]
    samples=0
    for n in (0,1,2,3,4):
        for word in product((1,2,3,17),repeat=n):
            q=spell.visible(word)+'1'
            assert q==spell.physical(word)[::2]+'1'
            assert (F69 not in q)==parser(word)==direct_macro_guard(word),word
            # The marker detector is checked independently of the parser.
            extended=spell.visible(word+(1,))
            detected=[i for i in range(len(q)-1)
                      if extended[i:i+11]==H]
            assert detected==spell.first_l_positions(word),word
            samples+=1

    assert parser((1,2,2))
    assert F69 not in spell.visible((1,2,2))+'1'
    assert len(spell.visible((1,2,2,1)))==70
    assert F69 not in spell.visible((1,2,2,1))
    assert (spell.visible((1,2,2,1))+'1').find(F69)==2
    assert not parser((1,2,2,1))
    # A late terminal122 is retained, unlike immediate rejection.
    assert parser((3,2,3,1,2,2))
    assert not parser((3,2,3,1,2,2,17))
    # The actual joint relaxation has a reviewed M3 self-loop. This cut
    # cannot remove that periodic output, independently of any solver.
    v3=spell.visible((3,))
    assert F69 not in v3*5
    assert parser((3,)*9)
    print(dict(P1='HELD',P2='HELD',complete_macro_cones=samples,
               first_l_offsets=[1,17,36,55],spacing_guard=[16,19,19],
               hidden_states=4,terminal122='retained',
               missing_endpoint_counter='raw1221 avoids; endpoint rejects',
               M3_survives_this_cut=True,actual_membership_tested=False))


if __name__=='__main__':
    main()
