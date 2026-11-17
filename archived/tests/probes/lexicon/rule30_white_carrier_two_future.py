"""GC1066: retain GC1065's actual origin through two future updates.
Missing inference: the joint boundary pair alone does not lift the
second freely chosen exterior sample. Retain the complete child prefix
through j ending Q0, initial through j-1 ending01, and choose child R.
Record searched: halfwidth|origin|white carrier + four tick|two future|
second future ->13 hits in4 files. GC1059's masked-exterior primitive
and GC1065's exact G236 carrier reused; no origin-conditioned two-future
construction in the record. No solver, language or width census.
P1 before execution: for every next pair R,S and second free sample G,
the construction below preserves BOTH complete future interior rows.
If R=S=0 choose b=c=0,d=e=1,f=G,g=0: next child triple is00G.
If R0,S1 choose b=c=d=0,e=1,f=g=0: child triple010.
If R1 choose b=c=d=e=0,f=S,g=0: child triple1SS.
When R OR S=1 the next boundary is black and masks any disagreement
between G and the actual next exterior. Otherwise actual next input=G.
Counterfactual: G must always equal the actual next exterior. Positive
controls with a masked mismatch must refute this stronger condition.
P2: retaining three complete future rows is already impossible in the
feasible child cylinder L,Q,R,S,T=10001 with free inputs010. Keeping
the first two rows forces S0,T1, then the third actual input is1 for
every U. This blocks row-preserving iteration, not trace halfwidth.
Unexpected check: this third-row failure has the SAME first-column
observations at that horizon. Thus do not mistake it for a trace loss.
Controls use literal/packed original cones and decimal-table strips,
both phases, selected constructors and arbitrary farther bits.
"""
from itertools import product
from rule30_sl_no_refork import run
from rule30_trace_prefix_repair import strip, trace


def origin(v, R, S, G):
    if R == S == 0:
        d, e, f, g = 1, 1, G, 0
    elif R == 0:
        d, e, f, g = 0, 1, 0, 0
    else:
        d, e, f, g = 0, 0, S, 0
    return (v, 0, 1, 0, 0, d, e, f, g)


def main():
    lifts = masked = 0
    for v, phase, R, S, G, h in product((0, 1), repeat=6):
        prefix = (v, 0, 1)
        reference = run(prefix + (1, 0, 0, 0, 0, 0), 2, phase)
        child = reference[2][:4] + (R,)
        wanted = strip(child, (S, G), phase)
        actual = run(origin(v, R, S, G) + (h, 1-h), 4, phase)
        assert actual[0][:3] == prefix
        assert actual[2][:5] == child
        assert actual[3][:5] == wanted[1]
        assert actual[4][:5] == wanted[2]
        assert trace(actual[:2]) == trace(reference[:2])
        if actual[3][5] != G:
            assert wanted[1][-1] == 1
            masked += 1
        lifts += 1
    # Feasible all-depth obstruction: j=4, L=initial j-3=1.
    # It is a local Rule30 obstruction even with an unrestricted origin.
    failures = 0
    for phase, U, farther in product((0, 1), repeat=3):
        actual = run(origin(1, 0, 0, 1) + (U, farther, 0), 5, phase)
        child = actual[2][:5]
        assert actual[2][2:7] == (1, 0, 0, 0, 1)
        wanted = strip(child, (0, 1, 0), phase)
        assert actual[3][:5] == wanted[1]
        assert actual[4][:5] == wanted[2]
        assert actual[4][5] == 1  # Third exterior forced independently of U.
        assert actual[5][:4] == wanted[3][:4]
        assert actual[5][4] != wanted[3][4]
        assert trace(actual[2:6]) == trace(wanted)
        failures += 1
    print({'two_future_lifts': lifts, 'masked_input_mismatches': masked,
           'third_row_obstructions': failures, 'literal_packed': 'PASS',
           'prefix_and_past': 'PASS', 'trace_loss_countercheck': 'PASS'})


if __name__ == '__main__':
    main()
