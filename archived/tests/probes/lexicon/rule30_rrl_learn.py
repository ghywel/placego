#!/usr/bin/env python3
"""GC981: bounded counterexample-guided residual refinement.
Record searched: GC980/RRL + counterexample/residual/refinement ->9 hits in7 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_learn.py
Before execution: at most5 C32 closure attempts, total20-second budget, each
at most40 rounds/3000states. Backtrace each overflow with truth-table controls;
add all suffixes of its first unsupported word to the residual tests. P1:
source contains no recovered loss; next quotient excludes it and preserves
source. CF: preceding quotient admits it. U: stop honestly if reset ancestry
is unsupported. Blind P2: no closure within5 refinements. No K/cutoff scan,
physical witness or finite-refinement convergence claim.
OUTCOME: two source-excluding refinements PASS (28 zeros at counter6/round10;
length23 word at counter11/round15), suites42->66->87 tests. Both overflow
at round37. Third attempt stops on shared time cap. P1 PASS where tested;
no closure, P2 consistent but full5-attempt prediction not completed. First
loss has dead prefix 0^6: next preserve prefix viability, not only acceptance.
"""
import time
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_history as h
import rule30_rrl_residual as z


def run():
    start=time.monotonic()
    for attempt in range(1,6):
        remaining=int(20-(time.monotonic()-start))
        if remaining<1: print('TOTAL BUDGET STOP'); return
        found=[]
        def diagnostic(history,white):
            loss=h.diagnose(history,white,transform=z.residual)
            if loss is not None: found.append(loss)
        print('ATTEMPT',attempt,'tests',len(z.TESTS),flush=True)
        f.run(z.residual,diagnostic,seconds=remaining)
        if not found:
            print('NO RECOVERED LOSS; inspect preceding completion/stop, no refinement claim',flush=True)
            return
        word,source,r,n=found[0]
        assert not t.accepted(source,word) and t.accepted(z.residual(source),word)
        tests=set(z.TESTS)|{word[i:] for i in range(len(word)+1)}
        z.TESTS=sorted(tests,key=lambda w:(len(w),w))
        assert c.subset(source,z.residual(source)) and not t.accepted(z.residual(source),word)
        print('REFINED loss length',len(word),'counter',r,'round',n,flush=True)
    print('FIVE REFINEMENTS FINISHED; no closure',flush=True)


if __name__=='__main__': run()
