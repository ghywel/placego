# L1030 actual-result review and the remaining three membership questions

GPT, GC1983, 27 October 2026. Owner asks for actual result review, a decision
about further compute, and Local's plain opinion of the possible-pasts finding.

**Verdict:** the pilot's witness results carry. Existing evidence resolves all
three early cases without a new SAT run. Exactly three near-age100 words remain
undecided, two linked by a one-tick shift. A small exact frontier test is useful;
a larger random sample or the length20..24 census is not the next step.

## Actual evidence examined

Fetched the complete nine-file packet plus manifest from
`cited/l1030-witness-pilot/`. Manifest SHA256
`2095839827018bd0daa4ed352c1bb1d5e27696dbdf0194a5479cefee0a886a77`;
all nine file hashes matched. Read actual summary, language, controls, checkpoint,
witnesses, latest witnesses, stdout and terminal resource receipts.

Independently replayed all61 retained initial rows:25 age100 witnesses and36
latest-age witnesses. A separately written scalar update used the four literal
triples001/010/011/100 that produce1. Every complete visible trace and claimed
window matched. Regenerating MT19937 seed1976 draws, without evolving the200,000
rows again, confirmed every saved row at its recorded draw number. Checked the
pilot/evaluator/MFW hashes and all per-word summary/packet bindings.

The actual frequencies sum to200,000, have exactly the25 witnessed keys, and
give18,857 off-rhythm rows. The12/13 split of distinct witnessed words also
checks. These are source-and-output consistency checks on the full population
statistics, not an independent repeat of the population evolution. The4096
tiny-cone controls are retained as Local's passing run; their source was read,
but they were not rerun here.

The accepted pilot completed on the M5: child10.512s wall/10.509s CPU,
supervisor11.25s wall, child return0. Sampled group RSS peaked at15,632KiB,
minimum free+inactive4316MiB, swap growth0. `/usr/bin/time` reports a separate
process RSS maximum of15,089,664bytes. The uploaded launcher is explicitly
sanitized; no assertion of byte-equality with its private original is made.

Thus the old `00001001@100` timeout is resolved by a concrete checked witness.
P_B's fewer-than10-of19 prediction is refuted by13 distinct witnesses. Neither
this nor the9.4285% off-rhythm row fraction measures entry into the external
trap. 'Only25 words appear' means only25 in this sample, not a universal bound.

## Three early cases close using the existing language record

Let L_n=E_0^n be the initial visible language. By definition,

    E_j(w) iff some length-j prefix u has uw in L_(j+|w|).

This uses the same white-first wall and even-time sampling as the pilot.

For each of `10010100` and `10010101`, there are only two possible one-symbol
prefixes. Prefix1 gives forbidden11. Prefix0 gives a word containing the known
forbidden0100101. Therefore neither word can occur at age1. Both have retained,
independently replayed age0 witnesses: **first absence is exactly1**.

For `10001001`, a bounded audit of the already certified phase0 MFW44 list gives
1493 initial words of length24 and1780 of length25. Exactly one length24 word
ends in the target:

    100010001000100010001001

There is no such length25 word. Any length25 candidate would have to prepend a
bit to the unique length24 word. Prepending1 gives11; prepending0 gives
`0100010001000100010001001`, itself in the certified forbidden list. The pilot
supplies an independently replayed age16 witness. Hence **last possible16,
first absent17**. Earlier references to 'death16' must not be read as first
absence16 in this convention.

This audit is retained-language analysis, not a new cellular-automaton census or
solver run. For exclusion, soundness of the certified forbidden words is enough:
there is no length25 candidate even in the language that merely avoids this list.
Completeness of the list is not needed for that negative conclusion. The record
also certifies exactness through44; no underlying database certificate was
rechecked here. The generated language matched the recorded counts at8,20 and24.

With the five earlier offset exclusions, **eight initial words are now excluded
by age34**. The other28 all have retained witnesses at age34 or later. Thus
E_34^8 has exactly28 words. E_100^8 contains the25 checked words, and its only
remaining candidates are:

| Word | Latest retained witnessed age |
|---|---:|
| P=`00010101` | 98 |
| Q=`00101010` | 99 |
| R=`01010100` | 99 |

## A hand relation removes one independent frontier

P ends in1, so the next visible bit must be0 (11 is forbidden). Consequently
an occurrence of P at age j forces Q at age j+1.

Conversely, if Q occurs at age j>=2, inspect the immediately preceding visible
bit. If it were1, `10010101` would occur at age j-1>=1, contradicting the early
exclusion just established. It is therefore0, giving P at age j-1. Thus

    E_j(Q) iff E_(j-1)(P), for j>=2.

This is about existence with unconstrained initial right rows, not equality of
their initial witnesses. In particular Q at100 is equivalent to P at99. If
finite first-absence times exist here, d(Q)=d(P)+1. The98/99 sample alignment is
consistent with this law, not independent evidence of two different mechanisms.

## Further compute decision: worthwhile, narrowly scoped

Propose at most three exact questions, with no new random sampling:

1. P at99, against the retained positive at98;
2. P at100, unless absence at99 already implies its answer;
3. R at100, against the retained positive at99.

Positive P99 settles Q100. Negative P99 gives exact deaths99 and100 for P andQ.
Positive P99 plus negative P100 gives death100 for P. Negative R100 gives its
exact death100. Positive P100 andR100 close the whole short-word gate. UNKNOWN
answers keep the relevant cases unresolved and trigger no automatic rerun.

Prediction for this proposed stage: all three are possible (the rare-survivor
reading). Counterfactual: any exact negative supplies a genuinely late death
and revises the historical short-word plateau. This prediction is not inferred
from random nonappearance or trap prevalence.

Before launch, Local and GPT should freeze a small driver using the two reviewed
CNF encodings, the retained positive fixtures and independent physical replay
of every SAT witness. Proposed envelope: one solver at a time, at most6 calls,
30s CPU/wall per call, aggregate pre-call CPU guard210s, stage wall300s,
group RSS512MiB, disk256MiB, per-file64MiB; existing pressure stops. Include
post-call accounting and stop on encoding disagreement. Retain all inputs,
outputs and negative proof traces; state whether certificates were actually
checked. This is a proposal, not a source freeze or launch acceptance. No larger
word lengths, longer timeout, seed changes or automatic subsequent stage.

## Retained review outputs

- `cited/gc1983-l1030-review/gpt-audit.json`, SHA256
  `a9b380bd371a05a98567e1333503451124622bbcef68ebf805ed33cea77df0c2`.
- `cited/gc1983-l1030-review/language-audit.json`, SHA256
  `c0564b9d2dc5e670bf4cf170f79af3bff5ccd577224e953ecc2cf993d07fe61e`.

The new prefix and shift arguments are elementary hand/data consequences, not
yet independently read by Local. No asymptotic non-soficity, information-rate,
or natural-centre-clock conclusion follows.
