#!/usr/bin/env python3
"""Exact input-labelled A transfer and bounded physical-history witnesses.

An input word stores column8 at times0..13, earliest in its low bit.
Initial time is odd phase; physical boundary bits are0,1,0,1,... .
No symbolic simplifier, wider graph, seed census, or adaptive solve budget.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

from pysat.solvers import Cadical195

SOURCES = (32, 64, 96)
A_END = (32, 64, 96)
E_END = (56, 88, 120)


def physical(x, t):
    return ((x << 1) | (t & 1)) ^ (x | (x >> 1))


def trace(x, duration):
    out = [x]
    for t in range(duration):
        x = physical(x, t)
        out.append(x)
    return out


def trunk(a, word):
    out = [a]
    for t in range(14):
        r = out[-1]
        out.append((((r << 1) | (t & 1)) ^
                    (r | (r >> 1) | (((word >> t) & 1) << 6))) & 127)
    return out


def block_ok(rs, start=0):
    return all((rs[start+t] & 1) == int(t in (2, 6))
               for t in range(2, 15, 2))


def word_of(rs, start=0):
    return sum(((rs[start+t] >> 7) & 1) << t for t in range(14))


def first_adjacent_failure(rs, word):
    for t in range(13):
        if (word >> t) & 1:
            if ((word >> (t+1)) & 1) != (1 ^ ((rs[t] >> 6) & 1)):
                return t
    return None


def free_transfer(out):
    records, counts = [], Counter()
    for a in SOURCES:
        for word in range(1 << 14):
            rs = trunk(a, word)
            if not block_ok(rs) or rs[-1] not in A_END + E_END:
                continue
            end = 'A' if rs[-1] in A_END else 'E'
            bad = first_adjacent_failure(rs, word)
            records.append([a, word, rs[-1], bad])
            counts[(a, end, 'all')] += 1
            if bad is None:
                counts[(a, end, 'adjacent_pass')] += 1
    (out/'input-labelled-transfer.json').write_text(json.dumps(records)+'\n')
    return {'input_assignments': 3*(1 << 14), 'accepted_records': len(records),
            'counts': [{'source': a, 'next': end, 'raw_words': counts[a,end,'all'],
                        'adjacent_pass': counts[a,end,'adjacent_pass']}
                       for a in SOURCES for end in ('A','E')]}


class Cone:
    def __init__(self, solver, offset, blocks=1, source=None, endpoint=None):
        self.solver, self.ids, self.h = solver, [], 14*blocks
        width = self.h + 7
        n = offset
        for t in range(self.h+1):
            self.ids.append(list(range(n+1,n+width-t+1)))
            n += width-t
        self.top = n
        self.true = n+1
        self.top += 1
        solver.add_clause([self.true])
        for t in range(self.h):
            for i,d in enumerate(self.ids[t+1]):
                a = self.ids[t][i-1] if i else (self.true if t & 1 else -self.true)
                b,c = self.ids[t][i:i+2]
                for clause in ([-b,a,d],[-b,-a,-d],[-c,a,d],[-c,-a,-d],
                               [b,c,-a,d],[b,c,a,-d]):
                    solver.add_clause(clause)
        self.fix_prefix(0, source if source is not None else 32)
        for block in range(blocks):
            for t in range(2,15,2):
                self.fix(14*block+t, 0, int(t in (2,6)))
            if block+1 < blocks:
                # Shared intermediate row; never a fresh exterior choice.
                self.require_prefix(14*(block+1), A_END)
        self.require_prefix(self.h, A_END if endpoint == 'A' else E_END)

    def fix(self,t,i,b):
        self.solver.add_clause([self.ids[t][i] if b else -self.ids[t][i]])

    def fix_prefix(self,t,value):
        for i in range(7):
            self.fix(t,i,(value >> i) & 1)

    def require_prefix(self,t,values):
        for x in range(128):
            if x not in values:
                self.solver.add_clause([(-v if (x>>i)&1 else v)
                                        for i,v in enumerate(self.ids[t][:7])])

    def witness(self,model):
        positive = set(x for x in model if x>0)
        root = sum((v in positive) << i for i,v in enumerate(self.ids[0]))
        rs = trace(root,self.h+8)
        for t,ids in enumerate(self.ids):
            for i,v in enumerate(ids):
                assert ((rs[t]>>i)&1) == int(v in positive)
        for b in range(self.h//14):
            assert block_ok(rs,14*b)
            assert trunk(rs[14*b]&127,word_of(rs,14*b)) == [x&127 for x in rs[14*b:14*b+15]]
            assert first_adjacent_failure(rs[14*b:14*b+15],word_of(rs,14*b)) is None
        # Cell-array oracle, separate from the integer update and CNF.
        cells = [(root>>i)&1 for i in range(root.bit_length()+self.h+12)]
        for t in range(self.h+1):
            assert sum(x<<i for i,x in enumerate(cells)) == rs[t]
            cells = [((t&1) if i==0 else cells[i-1]) ^
                     (cells[i] | (cells[i+1] if i+1<len(cells) else 0))
                     for i in range(len(cells))]
        return {'root': root, 'width': root.bit_length(), 'source':root&127,
                'end':rs[self.h]&127,
                'blocks':[{'time':14*b,'source':rs[14*b]&127,
                           'word':word_of(rs,14*b),'end':rs[14*(b+1)]&127}
                          for b in range(self.h//14)],
                'rows_hex':[hex(x) for x in rs], 'scalar_replay':True}


def run_sat():
    results = []
    for a in SOURCES:
        for endpoint in ('A','E'):
            with Cadical195() as s:
                c = Cone(s,0,source=a,endpoint=endpoint)
                s.conf_budget(10000)
                answer = s.solve_limited()
                r={'kind':'one_block','source':a,'endpoint':endpoint,
                   'solver_answer':answer,'stats':s.accum_stats()}
                if answer:r['witness']=c.witness(s.get_model())
                results.append(r)
    # One incoming initial bit changes the outcome; all low seven bits agree.
    with Cadical195() as s:
        a=Cone(s,0,source=32,endpoint='A')
        b=Cone(s,a.top,source=32,endpoint='E')
        diffs=[];n=b.top
        for u,v in zip(a.ids[0][7:],b.ids[0][7:]):
            n+=1;d=n;diffs.append(d)
            for clause in ([-u,-v,-d],[u,v,-d],[u,-v,d],[-u,v,d]):s.add_clause(clause)
        s.add_clause(diffs)
        for i,d in enumerate(diffs):
            for e in diffs[i+1:]:s.add_clause([-d,-e])
        s.conf_budget(10000);answer=s.solve_limited()
        r={'kind':'single_initial_bit','solver_answer':answer,'stats':s.accum_stats()}
        if answer:
            m=s.get_model();r['A']=a.witness(m);r['E']=b.witness(m)
            delta=r['A']['root'] ^ r['E']['root'];assert delta.bit_count()==1
            r['different_cell']=delta.bit_length()
        results.append(r)
    # Independently physical blocks with equal seven-cell seam but an
    # impossible column8 time join. This deliberately tests unsafe splicing.
    with Cadical195() as s:
        a=Cone(s,0,source=32,endpoint='A')
        b=Cone(s,a.top,source=32,endpoint='E')
        a.fix_prefix(14,32);a.fix(13,7,1)
        u,v=a.ids[13][6],b.ids[0][7]
        s.add_clause([-u,v]);s.add_clause([u,-v])
        s.conf_budget(10000);answer=s.solve_limited()
        r={'kind':'bad_splice','solver_answer':answer,'stats':s.accum_stats()}
        if answer:
            m=s.get_model();r['left']=a.witness(m);r['right']=b.witness(m)
            left=[int(x,16) for x in r['left']['rows_hex']]
            right=[int(x,16) for x in r['right']['rows_hex']]
            assert left[14]&127 == right[0]&127
            assert (left[13]>>7)&1 == 1
            assert (right[0]>>7)&1 == (left[13]>>6)&1
            r['required_column8_at_join']=1^((left[13]>>6)&1)
            r['supplied_column8_at_join']=(right[0]>>7)&1
        results.append(r)
    with Cadical195() as s:
        c=Cone(s,0,blocks=2,source=32,endpoint='E')
        s.conf_budget(10000);answer=s.solve_limited()
        r={'kind':'shared_two_blocks','solver_answer':answer,'stats':s.accum_stats()}
        if answer:r['witness']=c.witness(s.get_model())
        results.append(r)
    return results


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    result={'transfer':free_transfer(a.out),'SAT':run_sat()}
    (a.out/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':main()
