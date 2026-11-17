"""GC1101: a fixed full-strip rank for repeated delayed A resets.

Missing inference: can the GC1100 delayed macro M=S-D101-H-SS-A
repeat indefinitely in a sound finite hidden relaxation? A nilpotent
20-cell macro relation would bound these resets uniformly in age and
arbitrary exterior; a cycle invalidates this candidate rank only.
Record searched: delayed|white.SS|black.A with strip|rank|potential;
GC1100 and GC1096..99, CL275/277 read; no delayed-reset strip rank.
P1 BEFORE run: M has nonempty but proper endpoint image among the128
20-cell black-A prefixes. Retain all20 updated cells and both fresh
right boundary inputs each tick; never clamp column5 independently.
P2 BEFORE run: deleting GC1096's forbidden mature-A20 packet makes
this macro graph acyclic. If true, its topological rank is a sound
all-age reset bound. If false, keep an explicit directed cycle and
stop this width candidate; do not widen cosmetically.
Counterfactual: full-strip consistency alone gives a monotone reset
rank. A recurrent vertex refutes this finite rank, not all finite-type
routes or eventual actual admission.
Controls: each packed transition checked against scalar local Rule30;
GC1100's actual source gives a positive macro path; its impossible
GC1096 packet is excluded at every macro boundary. Relation keeps
joint ancestry by propagating sets of origin labels through updates.
Unexpected check: distinguish recurrent endpoints that actually have
an incoming M from the large one-step image, rather than asserting
that every surviving endpoint is recurrent.
P1/P2 HELD:181 edges,38 endpoint states, graph acyclic after age guard.
P3 BEFORE rank extraction: maximal chain is at most4 macros. A
verified vertex potential, not layer counts, certifies any bound.
P4 BEFORE guard attribution: acyclicity persists if the single
GC1096 packet is restored. All intermediate101 rows still have16
clamped past ticks, so CL277's tenth-bit exclusion remains sound.
P5 BEFORE endpoint closure check: any white SS returning A with
black11 has all four sites10..13 black, so this complete A label
covers that branch. Exhaust its19-cell six-tick cones, retaining
actual fifth111010 track and marker white; failure limits the rank
scope, and is not repaired by widening the strip.
Record searched: white.SS|white.marker with A13|A11|black.eleventh;
GC1089/1090/1099 read before P5; black-origin identity is not imported.
P3/P4 HELD: mature graph rank<=2; restoring the forbidden packet
still gives an acyclic graph. P5 REFUTED: black11 exit selectors at
sites10..13 are1100,1101,1111. This rank initially covers1111 only.
P6 BEFORE the adaptive local check: the extra1100/1101 selectors
enter absorbing C on their next S. Check their complete15-cell
six-tick cones; if false, keep the additional noncore branch.
P6 REFUTED: both extra selectors return low001 (sixth black), not
C. They must be represented, rather than removed by a core shortcut.
P7 BEFORE correcting endpoint scope: the same20-cell representation,
now retaining all three black11 A selectors and only the common low
001 prefix, remains acyclic with rank<=3. This is a type correction
forced by P5/P6, not a width sweep. A cycle stops this broader rank.
P7 HELD:383 mature type states,209 edges,rank<=2. Restoring the
fresh guard packet gives384 states,273 edges,still rank<=2; no age
premise is needed. The final certificate is an explicit seven-packet
potential, checked at every macro edge. It bounds consecutive M
returns with black11, not arbitrary numbers of white SS per return.
The initially inferred245 fresh edges was incorrect: the joint
three-type construction has273. Only the exhaustive273-edge relation
is used for the potential certificate.
GC1100 CONFIRMED by CL278; existence does not supply a reset rank.
No solver, CUT, exact visible membership or relaxed-record run.
"""
from rule30_black_A_white_SS_entrance import ACTUAL, BLACK_A, S, D, H, SS
from rule30_sl_no_refork import bits, run

WIDTH=20
MASK=(1<<WIDTH)-1

def pack(x):return sum(b<<j for j,b in enumerate(x))
def unpack(x):return tuple((x>>j)&1 for j in range(WIDTH))
A=pack(BLACK_A)
AMASK=(1<<len(BLACK_A))-1
FORBIDDEN=pack(bits('11101000111110000011'))
TRACK=S+D+H+SS


def successors(x,t):
    y=(((x<<1)|(t&1))^(x|(x>>1)))&MASK
    # The extra cell at WIDTH affects only the last image, and is
    # masked precisely when the last known origin cell is black.
    return (y,) if (x>>(WIDTH-1))&1 else (y,y^(1<<(WIDTH-1)))


def scalar_successors(x,t):
    old=unpack(x);out=set()
    for exterior in (0,1):
        image=tuple(((t&1) if j==0 else old[j-1])^
                    (old[j]|(old[j+1] if j+1<WIDTH else exterior))
                    for j in range(WIDTH))
        out.add(pack(image))
    return out


def potential(x):
    if x&AMASK!=A:return 0
    suffix=x>>13
    if suffix in (32,96):return 2
    if suffix in (15,23,55,87,119):return 1
    return 0


def macro_relation(mature=True,all_black11=False):
    ap=[pack(bits('111010001'+suffix)) for suffix in ('1100','1101','1111')] if all_black11 else [A]
    starts=[a|(v<<13) for a in ap for v in range(1<<(WIDTH-13))]
    if mature:starts.remove(FORBIDDEN)
    labels={x:1<<i for i,x in enumerate(starts)}
    counts=[]
    pins={6:bits('111001001'),16:bits('1110011011'),26:bits('111010')}
    for t,b in enumerate(TRACK):
        nxt={}
        for x,origins in labels.items():
            if ((x>>4)&1)!=b:continue
            assert set(successors(x,t))==scalar_successors(x,t)
            for y in successors(x,t):nxt[y]=nxt.get(y,0)|origins
        if t+1 in pins:
            p=pins[t+1];m=(1<<len(p))-1;v=pack(p)
            nxt={y:o for y,o in nxt.items() if y&m==v}
        labels=nxt;counts.append(len(labels))
    ends={x:o for x,o in labels.items() if x&AMASK in ap and (not mature or x!=FORBIDDEN)}
    index={x:i for i,x in enumerate(starts)}
    edges=[set() for _ in starts]
    for x,origins in ends.items():
        while origins:
            low=origins&-origins;i=low.bit_length()-1
            edges[i].add(index[x]);origins^=low
    return starts,edges,counts


def find_cycle(edges):
    seen=set();active={};path=[]
    def visit(v):
        if v in active:return path[active[v]:]+[v]
        if v in seen:return None
        seen.add(v);active[v]=len(path);path.append(v)
        for w in sorted(edges[v]):
            cycle=visit(w)
            if cycle:return cycle
        path.pop();del active[v]
        return None
    for v in range(len(edges)):
        c=visit(v)
        if c:return c
    return None


def direct_endpoints(source,ap):
    # An independent origin-by-origin set flow, using scalar images.
    states={source}
    pins={6:bits('111001001'),16:bits('1110011011'),26:bits('111010')}
    for t,b in enumerate(TRACK):
        states={y for x in states if (x>>4)&1==b
                for y in scalar_successors(x,t)}
        if t+1 in pins:
            p=pins[t+1];m=(1<<len(p))-1;v=pack(p)
            states={y for y in states if y&m==v}
    return {y for y in states if y&AMASK in ap}


def main():
    from itertools import product
    from rule30_black_A_ancestry_guard import inverse
    # CL277's one-tick past implication, no inverse-layer extension.
    assert not inverse(bits('1110011010'),1)
    assert len(inverse(bits('111001101'),1))==1
    actual=run(ACTUAL+(0,)*40,38)
    for t in range(6,38):
        assert pack(actual[t+1][:WIDTH]) in successors(pack(actual[t][:WIDTH]),t)
    # Reproduce the registered narrow candidate before scope correction.
    narrow,ne,nc=macro_relation()
    assert find_cycle(ne) is None
    assert sum(map(len,ne))==181
    assert {narrow[j] for row in ne for j in row}.__len__()==38
    selectors=set();controls=0
    for pre in ('111010000','111010100','111010101','111010110','111010111'):
        for tail in product((0,1),repeat=10):
            rows=run(bits(pre)+tail,6)
            assert tuple(x[4] for x in rows[:6])==SS
            if rows[6][:9]==bits('111010001') and rows[6][10]:
                selectors.add(rows[6][9:13])
            controls+=1
    assert selectors=={bits(s) for s in ('1100','1101','1111')}
    for pre in ('1110100011100','1110100011101'):
        for tail in product((0,1),repeat=2):
            rows=run(bits(pre)+tail,6)
            assert tuple(x[4] for x in rows[:6])==S
            assert rows[6][5:9]==bits('1001') # low001, not core C.
    fresh,edges,counts=macro_relation(False,True)
    assert len(fresh)==384 and sum(map(len,edges))==273
    assert find_cycle(edges) is None
    assert all(potential(fresh[i])>potential(fresh[j])
               for i,row in enumerate(edges) for j in row)
    assert {fresh[i] for i,row in enumerate(edges) if row}=={
        A|(v<<13) for v in (15,23,32,55,87,96,119)}
    a,b=pack(actual[6][:WIDTH]),pack(actual[38][:WIDTH])
    assert fresh.index(b) in edges[fresh.index(a)]
    assert (potential(a),potential(b))==(1,0)
    ap={pack(bits('111010001'+s)) for s in ('1100','1101','1111')}
    control_sources={a,b,A,FORBIDDEN,A|(32<<13),A|(15<<13)}|{
        pack(bits('111010001'+s)) for s in ('1100','1101')}
    for source in control_sources:
        i=fresh.index(source)
        assert direct_endpoints(source,ap)=={fresh[j] for j in edges[i]}
    mature,me,mc=macro_relation(True,True)
    assert len(mature)==383 and sum(map(len,me))==209
    assert all(potential(mature[i])>potential(mature[j])
               for i,row in enumerate(me) for j in row)
    image={j for row in edges for j in row}
    image_with_outgoing=sum(bool(edges[j]) for j in image)
    assert len(image)==66 and image_with_outgoing==3
    print(dict(width=WIDTH,typed_states=len(fresh),macro_edges=sum(map(len,edges)),
               endpoint_image=len(image),image_with_outgoing=image_with_outgoing,
               rank_two_suffixes=['0000010','0000011'],
               rank_one_suffixes=['1111000','1110100','1110110','1110101','1110111'],
               max_consecutive_M=2,age_guard_needed=False,
               white_SS_selector_cones=controls,scalar_origin_controls=len(control_sources),
               actual_GC1100_rank_drop=[1,0],
               arbitrary_SS_block_rank='OPEN',all_depth_record_bound='OPEN'))


if __name__=='__main__':main()
