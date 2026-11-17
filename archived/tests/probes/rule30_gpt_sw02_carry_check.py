#!/usr/bin/env python3
"""GC2689 source-review replay of AM-3 finite premises.
RUN-ON: cpu (Python standard library, one worker, no subprocesses).
Use run_capped.py with the frozen review plan; no imports of swarm code.
Independent reset-language regex instead of the prover's subset-mask scanner.
Frozen scope: kit K=87867 four literals x16 phases, plus K20 four phases.
No new horizons, seed census or BN12 enlargement. CLI: python3 THIS KIT_SOURCE.
Expected strip (min,max): (7997,8012),(7979,7994),(7929,7944),(7911,7926).
Counterfactual: any mismatch blocks B1/B2 numerical carrying status.
"""
import hashlib,itertools,json,re,sys,time
from pathlib import Path
start=time.process_time(); src=Path(sys.argv[1]).read_bytes(); text=src.decode()
pat=re.compile(r'01(?:111)*0[01]')
def image(word):
    states={(0,0),(0,1),(1,0),(1,1)}
    for char in word:
        y=int(char); states={(b,y^(a|b)) for a,b in states}
    return states
# Complete short-word controls, including the missing following-bit mutant.
for n in range(10):
    for chars in itertools.product('01',repeat=n):
        word=''.join(chars)
        assert (pat.search(word) is not None)==(len(image(word))==1),(word,image(word))
assert len(image('010'))>1
assert len(image('0100'))==len(image('0101'))==1
assert pat.search('010') is None
assert pat.search('0111101') is not None

def chain(words,phase):
    # All strings read from highest wheel downwards. Moving one row earlier
    # shrinks width by one, so after m.end()-1 the next start is m.end().
    pos=0; n=0; ends=[]; k=len(words[0]); period=len(words)
    while pos<k:
        m=pat.search(words[phase%period],pos)
        if m is None: break
        assert m.end()>pos
        ends.append(k-m.end());pos=m.end();phase-=1;n+=1
    return n,ends

def check_step(v,k):
    y=0
    for j in range(k):
        left2=(v>>(j-2))&1 if j>=2 else 0
        left1=(v>>(j-1))&1 if j>=1 else 0
        bit=left2^(left1|((v>>j)&1))
        y|=bit<<j
    assert y==((v<<2)^((v<<1)|v))&((1<<k)-1)

cyc=[0x1e713,0x4737b,0xd3a13,0xb967b]
for v in cyc:check_step(v,20)
# Independent scalar basin check: first entry, rather than evolving a vector
# of all states and comparing its terminal image. No scope enlargement.
max_entry=need26=0
cycle_set=set(cyc)
for initial in range(1,1<<20,2):
    x=initial; entry=0
    while x not in cycle_set and entry<=26:
        x=((x<<2)^((x<<1)|x))&0xfffff;entry+=1
    assert entry<=26,(initial,entry)
    max_entry=max(max_entry,entry);need26+=entry==26
assert max_entry==26 and need26==40960
words20=[format(v,'020b') for v in cyc]
cert20=[chain(words20,p) for p in range(4)]
assert all(n>=2 for n,ends in cert20)
assert [ends[:2] for n,ends in cert20]==[[11,1],[16,2],[14,1],[10,2]],cert20
A0=int(re.search(r'^def A0 : Nat := 0x([0-9a-f]+)\s*$',text,re.M).group(1),16)
def literal(base,name,basename):
    m=re.search(r'^def '+name+r' : Nat := '+basename+r' \^\^\^ \(0x([0-9a-f]+) <<< (\d+)\)\s*$',text,re.M)
    assert m is not None,name
    return base^(int(m.group(1),16)<<int(m.group(2)))
A1=literal(A0,'A1','A0');B0=literal(A0,'B0','A0');B1=literal(B0,'B1','B0')
k=87867;mask=(1<<k)-1;expected=[(7997,8012),(7979,7994),(7929,7944),(7911,7926)];summary={}
for (name,v),want in zip([('A0',A0),('A1',A1),('B0',B0),('B1',B1)],expected):
    assert 0<v<=mask and v&1
    rows=[];x=v
    for _ in range(16):rows.append(x);x=((x<<2)^((x<<1)|x))&mask
    assert x==v and len(set(rows))==16
    assert set(x&0xfffff for x in rows)==set(cyc)
    words=[format(x,'0'+str(k)+'b') for x in rows]
    ns=[chain(words,p)[0] for p in range(16)]
    assert (min(ns),max(ns))==want,(name,ns)
    summary[name]={'chain_by_phase':ns,'min':min(ns),'max':max(ns),'period':16}
print(json.dumps({'source_sha256':hashlib.sha256(src).hexdigest(),'short_word_control_length':9,
                  'basin':{'odd_states':524288,'max_entry':max_entry,'need_26':need26},
                  'missing_following_bit_mutant_rejected':True,'k20_collapse_wheels':[e[:2] for _,e in cert20],
                  'strips':summary,'cpu_s':round(time.process_time()-start,4)},sort_keys=True))
