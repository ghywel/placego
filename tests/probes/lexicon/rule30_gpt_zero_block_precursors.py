#!/usr/bin/env python3
"""GC409: finite open-interval form of the recorded zero-row preimage idea.
Before run: exactly4 precursors for L zero outputs:0^(L+2),1^L01,
1^L10,1^(L+2), L1..8 controls. Scalar XOR-OR vs literal Rule30 table.
Unexpected endpoint check retains both nonconstant right-end precursors.
Not an added restriction on RR's time0 block without prior-history scope;
G121 warns that a finite seed need not have a finite predecessor.
OUTCOME:2040 rows PASS, exactly4 at every L1..8 including both terminal
exceptions. General local proof proposed in RULE30-GPT GC409; second reading
pending. No new cofinal obstruction or prize claim.
"""
import itertools,json


def main():
    out=[]; total=0
    for length in range(1,9):
        got=set()
        for row in itertools.product((0,1),repeat=length+2):
            scalar=tuple(row[i-1]^(row[i]|row[i+1]) for i in range(1,length+1))
            literal=tuple((30 >> ((row[i-1]<<2)|(row[i]<<1)|row[i+1]))&1
                          for i in range(1,length+1))
            assert scalar==literal;total+=1
            if not any(scalar):got.add(row)
        expected={(0,)*(length+2),(1,)*length+(0,1),
                  (1,)*(length+1)+(0,),(1,)*(length+2)}
        assert got==expected
        out.append({'length':length,'precursors':len(got),'nonconstant_right_end_cases':2})
    print(json.dumps({'rows_checked':total,'cases':out,'scalar_truth_table':'PASS'},indent=2))


if __name__=='__main__':main()
