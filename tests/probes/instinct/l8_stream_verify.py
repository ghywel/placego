#!/usr/bin/env python3
"""Independent READ-ONLY post-run completeness/tiling verifier for E24..E32.
No search, source mutation or production execution on import.
Strict target order + domain membership + independent cardinality = coverage.
Run on the finished output directory: python3 l8_stream_verify.py OUTDIR
"""
from pathlib import Path
from functools import lru_cache
import hashlib,json,sys

class AuditError(ValueError):pass

def need(ok,message):
    if not ok:raise AuditError(message)

@lru_cache(None)
def rectangle(k,b,r):
    """Partitions of r into <=k positive parts each <=b; pad with zeros."""
    if r<0 or k<0 or b<0 or r>k*b:return 0
    if r==0:return 1
    dp=[[0]*(r+1) for _ in range(k+1)];dp[0][0]=1
    for value in range(1,min(b,r)+1):
        for count in range(1,k+1):
            for total in range(value,r+1):
                dp[count][total]+=dp[count-1][total-value]
    return sum(row[r] for row in dp)

def expected(m,lo):return rectangle(7,2*m+66-lo,m*m-8*lo)

def specs():
    return {(m,lo) for m in range(24,33)
            for lo in range(68,min(2*m+66,m*m//8)+1)}

def check_chunk(lines,m,lo):
    need((m,lo) in specs(),'chunk outside expected manifest')
    want=expected(m,lo);previous=None;count=0;done=False
    for line_number,line in enumerate(lines,1):
        need(not done,'content after DONE')
        try:row=json.loads(line)
        except (ValueError,TypeError) as e:raise AuditError('invalid JSON') from e
        need(isinstance(row,dict),'record is not an object')
        need(type(row.get('m')) is int and row['m']==m,'wrong level')
        if 'end' in row:
            need(row['end']=='DONE','invalid terminator')
            need(type(row.get('l1')) is int and row['l1']==lo,'wrong footer minimum')
            need(type(row.get('towns')) is int and row['towns']==count==want,'footer/coverage count mismatch')
            st=row.get('stats');need(isinstance(st,dict),'missing footer stats')
            need(st.get('tiled')==count and st.get('unknown')==0 and st.get('impossible')==0,'footer not all tiled')
            done=True;continue
        need('r' not in row,'unresolved or impossible record')
        town=row.get('town')
        need(isinstance(town,list) and len(town)==8 and all(type(x) is int for x in town),'invalid town shape')
        need(town==sorted(town) and town[0]==lo,'wrong minimum or unsorted town')
        need(all(68<=x<=2*m+66 for x in town) and sum(town)==m*m,'town outside domain')
        key=tuple(town);need(previous is None or previous<key,'duplicate or nonincreasing town')
        previous=key
        a=row.get('a');need(isinstance(a,str) and len(a)==m and all(c in '01234567' for c in a),'invalid assignment inventory')
        sums=[0]*8
        for i,c in enumerate(a):sums[int(c)]+=2*(m-i)-1
        need(sorted(sums)==town,'assignment sums do not match town')
        count+=1;need(count<=want,'too many towns')
    need(done,'missing DONE')
    return count

def verify(outdir):
    root=Path(outdir);wanted={f'E{m}_l{lo}.jsonl':(m,lo) for m,lo in specs()}
    present={p.name for p in root.glob('*.jsonl')}
    need(present==set(wanted),'missing or unexpected chunk files')
    totals={m:0 for m in range(24,33)};digest=hashlib.sha256()
    for name,(m,lo) in sorted(wanted.items()):
        with (root/name).open('rb') as stream:
            def lines():
                for raw in stream:
                    digest.update(raw)
                    try:yield raw.decode('utf8')
                    except UnicodeError as e:raise AuditError('invalid UTF8') from e
            totals[m]+=check_chunk(lines(),m,lo)
    return {'result':'COMPLETE VERIFIED STREAM','chunks':len(wanted),'levels':totals,'towns':sum(totals.values()),'stream_sha256':digest.hexdigest()}

if __name__=='__main__':
    try:
        need(len(sys.argv)==2,'supply finished output directory')
        print(json.dumps(verify(sys.argv[1]),sort_keys=True))
    except (AuditError,OSError) as e:
        print(json.dumps({'result':'REJECTED','reason':str(e)}));sys.exit(1)
