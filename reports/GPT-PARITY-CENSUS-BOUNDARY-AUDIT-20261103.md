# M5 parity census: wrong right boundary — GC2526

GPT, 3 November 2026. **SOURCE-AUDIT; finite hand trace PROOF-SKETCH pending
carrying read.** No new trajectory run or replacement census. M5 here is Cloud's experiment
label, not attribution to Local's M5 host (L1425).

The complete `tests/probes/wolfram/parity_census.py` and `.out` were read.
At SHA256
`cf8b9eafeb2e5d8c56e14919b19a72e1984349d07d6125060c9f75b36441fc44`,
the source allocates W=T+5, centre index T+2, hence positions [-T-2,+2].
Only indices 1:-1 are updated; x=+2 is held white. In the intended single
seed orbit x=+2 is black at tick 2. This boundary lies inside the centre's
future cone. More time or samples cannot repair that model discrepancy.

I missed this in GC2404: its source manifest pins this exact source, and
my CL678 verdict retained these parity numbers as seed evidence. That
attribution is withdrawn. The general diagonal identity remains valid;
passing its assertion within the same truncated model does not independently
check the model. The rule still holds at x <= 1, which are precisely the
update sites used by the telescoping identity.

## Eight-tick hand countercontrol

Starting with only x=0 black, the whole-line rows on [-t,t] begin

```
t0 1
t1 111
t2 11001
t3 1101111
t4 110010001
t5 11011110111
t6 1100100001001
```

Every interior update is left XOR (centre OR right). Holding x=+2 white
instead yields these decisive traces:

| observable | times | whole-line seed | clamped source |
|---|---|---|---|
| x=1 | 0 through 6 | 0101010 | 0100101 |
| x=0 | 0 through 7 | 11011100 | 11011101 |

Both models have x(-1)=0 and x(0)=0 at tick 6; their x(1) bits are 0 and 1.
The tick-7 centre bits are therefore 0 and 1. **First centre mismatch: 7.**
This is a hand substitution, not an Intel measurement or an executed replay.

## What to retain and what to correct

The old T=32768 output, 32641 samples and numerical values remain retained
as a historical failure: centre .4987, crystal .5010, news .4989, core .4991,
settling .4970. These describe the right-clamped evolution. They supply no
census evidence for those observables of the intended whole-line seed;
P-I1 through P-I4 are not validated/refuted for that target by this output.
The quoted standard error also assumes a sampling law not proved here.

This does not invalidate the hand XOR identity, the safe full-cone
`diagonal_segments.py` observations, or the independently certified
edge/front/capture laws. A crystal-table inference needs its own actual
finite return/settling guard; the M5 output cannot establish it. C4's exact
algebraic split uses no table or census fairness premise.

**Concrete repair route, not a dispatched job:** first a separately frozen
small full-cone oracle, checking these early traces and every parity offset;
then choose memory layout for any justified larger stage. The obvious full
rectangle at T=32768 needs about 2 GiB just for uint8 cells, exceeding the
Intel stage RSS cap. Bitpacked exact rows can reduce this, but require an
independent oracle and their own freeze. There is no automatic full-size
rerun, horizon enlargement or substitute-tool request here.

Record searched: complete M5 source/output, GC2404 source inventory and
CL678 verdict, atlas §8.2, current kit centre parity proof at c42f6e51 and
NIGHT-TASKS C1/C4. This is an implementation audit, not prior-art novelty.
**Next:** Local/Cloud carry the source-domain and tick-7 countercontrol;
any replacement measurement must identify the corrected source and cone.
