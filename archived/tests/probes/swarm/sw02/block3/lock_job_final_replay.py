#!/usr/bin/env python3
"""Small independent lineage replay and reuse of already checked A/E histories.

No new solver, width census or independent-tail realization claim.
"""
import argparse
import json
from pathlib import Path
import struct
import networkx as nx
from lock_width_job import scalar_moves, graph_rows, projected


def rule(a,b,c):return a ^ (b|c)


def patch(state, top):
    a,b,c,d=state
    out=[]
    for r in top:
        upper=r ^ (c|d)
        lower=upper ^ (a|b)
        a,b,c,d=lower,a,upper,c
        out.append(lower)
    return [out[3],out[2],out[1],out[0],state[0]]


def main():
    p=argparse.ArgumentParser();p.add_argument('--job',type=Path,required=True)
    p.add_argument('--histories',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    data=(args.job/'Bseed.bin').read_bytes();state=set(struct.unpack('<'+'Q'*(len(data)//8),data))
    rows=[json.loads(l) for l in (args.job/'B/scc_xx.jsonl').read_text().splitlines()]
    lineage=[]
    for width in range(40,45):
        if width>40:state={x|(b<<(width-1)) for x in state for b in (0,1)}
        graph=nx.DiGraph();graph.add_nodes_from(state)
        graph.add_edges_from((x,y) for x in state for y in scalar_moves(x,width) if y in state)
        deleted=[]
        while True:
            gone=[x for x in graph if not graph.in_degree(x) or not graph.out_degree(x)]
            if not gone:break
            deleted.append(sorted(gone));graph.remove_nodes_from(gone)
        state=set(graph)
        expected=graph_rows(sorted(state),width)
        actual=[r for r in rows if r['W']==width and r['stage']=='CORE']
        assert projected(expected)==projected(actual)
        lineage.append({'width':width,'core':sorted(state),'deletion_rounds':deleted,
                        'sccs':expected,'no_target_deletion_used':True})
    assert [len(r['core']) for r in lineage]==[78,78,77,29,0]
    # Known local identity: Rule30FirstChecks.two_tick in reflected indexing.
    for bits in range(32):
        a,b,c,d,e=[bits>>j&1 for j in range(5)]
        old=rule(rule(a,b,c),rule(b,c,d),rule(c,d,e))
        assert old==(a ^ (int(b==c)&(d|e)))
    result={'lineage':lineage,'five_bit_identity_cases':32,'saved_histories':[]}
    cases=[r for r in json.loads(args.histories.read_text()) if r['answer'] is True]
    assert {r['word'] for r in cases}=={4482,4498,4520,4521,4522,14429}
    for case in cases:
        witness=case['witness'];root=int(witness['root'])
        saved=list(map(lambda x:int(x,16),witness['rows_hex']))
        cells=[root>>j&1 for j in range(root.bit_length()+90)]
        for t in range(86):
            assert sum(x<<j for j,x in enumerate(cells))==saved[t]
            cells=[(int(t%2==0) if j==0 else cells[j-1]) ^
                   (cells[j]|(cells[j+1] if j+1<len(cells) else 0)) for j in range(len(cells))]
        def at(t,p):return saved[t]>>(p-1)&1
        state4=[at(11,10),at(11,11),at(12,11),at(12,12)]
        incoming=[at(13,j) for j in (11,10,9,8)]
        window=[at(11,j) for j in range(6,11)]
        assert patch(state4,incoming)==window
        a,b,c,d,e=window;q=at(13,8)
        assert q==(a ^ (int(b==c)&(d|e)))==1 and at(3,1)==1
        expected=28 if case['word']==14429 else 100
        assert saved[11]&127==expected
        assert c==0 and a==b
        result['saved_histories'].append({'word':case['word'],'root':str(root),
            'source64':saved[1]&127,'low7_at11':expected,'row11_cells6_to10':window,
            'state4':state4,'actual_row13_cells11_10_9_8':incoming,
            'older_pulse':at(3,1),'pair_or':b|c,'pair_equal':int(b==c),'later_input':q,
            'mechanism':'right_OR' if b==c else 'left_copy','all85_saved_rows_scalar_replayed':True})
    assert next(r for r in result['saved_histories'] if r['word']==14429)['pair_or']==0
    (args.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Independent unfiltered lineage counts',[(r['width'],len(r['core'])) for r in lineage])
    print('Known two_tick32 cases PASS; all6 retained whole-E histories scalar replay PASS')
    print(json.dumps(result['saved_histories'],indent=2))


if __name__=='__main__':main()
