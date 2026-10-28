#!/usr/bin/env python3
"""GC2021: audit retained whole-line left-crystal seams and jump witnesses.
No reconstruction or generator import. A periodic background plus a checked
finite seam certifies the infinite-left continuation by induction in depth.
"""
import base64,gzip,hashlib,json,math,os,sys
from pathlib import Path
TRUTH=(0,1,1,1,1,0,0,0)


def main():
    src=Path(sys.argv[1]);out=Path(os.environ['CAPPED_OUT'])
    vr=(src/'view.json').read_bytes();cr=(src/'certificates.json').read_bytes()
    assert hashlib.sha256(vr).hexdigest()=='e4ea4e9206514c9fa686702b163eb75c0c230be88abf31c53220feaf44dc6af0'
    assert hashlib.sha256(cr).hexdigest()=='a3f887f8e55051b25d1d8d2173e9a6711ebce33c6396053f1b08e01c918d934b'
    v=json.loads(vr);c=json.loads(cr);arrays={}
    for name in ('a','b'):
        raw=gzip.decompress(base64.b64decode(v[name]));rows=[]
        for d in range(513):
            offset=(-d-v['t0'])*v['stride']
            rows.append(bytes((raw[offset+i//8]>>(7-i%8))&1 for i in range(v['w'])))
        arrays[name]=rows
    counts={'seams':0,'periodic_equations':0,'left_matches':0,'right_matches':0,'jump_cells':0}
    for name in ('a','b'):
        cert=c['rows'][name];rows=arrays[name];lo=v['x0'];hi=lo+v['w']-1
        assert all(rows[0][x-lo]==int(x==0) for x in range(lo,hi+1))
        for d in range(1,513):
            r=cert[d];prev=cert[d-1];pat=r['left_pattern'];p=len(pat);old=prev['left_pattern'];q=len(old)
            assert r['left_period']==p and r['first_defect']==r['left_end']+1
            for i in range(math.lcm(p,q)):
                assert TRUTH[4*pat[(i-1)%p]+2*pat[i%p]+pat[(i+1)%p]]==old[i%q]
                counts['periodic_equations']+=1
            for i in range(lo,r['first_defect']):
                assert rows[d][i-lo]==pat[i%p];counts['left_matches']+=1
            assert rows[d][r['first_defect']-lo]!=pat[r['first_defect']%p]
            assert TRUTH[4*pat[(lo-1)%p]+2*rows[d][0]+rows[d][1]]==rows[d-1][0]
            counts['seams']+=1
            rp=r['right_period'];right=r['right_pattern']
            for i in range(1-d,hi+1):
                assert rows[d][i-lo]==right[(i-1)%rp];counts['right_matches']+=1
            assert rows[d][-d-lo]!=right[(-d-1)%rp]
            start=r['first_defect'];end=prev['first_defect'];event=c['events'][name][d-1]
            assert end-start==event['jump']>=-1
            counter={'masked':0,'cancelled':0,'already_equal':0}
            for i in range(start-1,end+1):
                actual=TRUTH[4*rows[d][i-1-lo]+2*rows[d][i-lo]+rows[d][i+1-lo]]
                background=TRUTH[4*pat[(i-1)%p]+2*pat[i%p]+pat[(i+1)%p]]
                assert actual==rows[d-1][i-lo]
                assert (actual!=background)==(i==end)
                if i<end:
                    l=rows[d][i-1-lo]!=pat[(i-1)%p]
                    m=rows[d][i-lo]!=pat[i%p] or rows[d][i+1-lo]!=pat[(i+1)%p]
                    counter['cancelled' if l else 'masked' if m else 'already_equal']+=1
                counts['jump_cells']+=1
            assert all(counter[k]==event[k] for k in counter)
    # A/B's three largest event patches: do equal counts reflect the same local
    # configuration up to translation? Inspect only a fixed 100-cell window.
    alignment=[]
    for d in (172,185,213):
        sa=c['rows']['a'][d]['first_defect'];sb=c['rows']['b'][d]['first_defect']
        same=all(arrays['a'][dd][sa+j-v['x0']]==arrays['b'][dd][sb+j-v['x0']]
                 for dd in (d,d-1) for j in range(-12,88))
        alignment.append({'depth':d,'horizontal_shift_b_minus_a':sb-sa,'two_row_100_cell_patch_equal':same})
    result={'counts':counts,'largest_jump_patches':alignment,'status':'PASS'}
    (out/'verified.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
