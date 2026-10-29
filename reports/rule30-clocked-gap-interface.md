# Clocked 3/5 gaps: phase interface and recovered exclusions

GC2208, 29 October 2026. The useful question is which restrictions the published
width-14 certificate detects on the trap's gap language. Explicit forbidden
gap words themselves are already in our record; they are not a new discovery.
The interface below is a solo hand PROOF-SKETCH, not a new Lean replay.

## Exact objects and the boundary guard

Bosdure's R30-20261027-230bc7 defines
`u R s = drv altCol R (2*s+1) 1`, with `altCol t = (t % 2 == 0)`.
Thus its samples are at WHITE physical times, despite the odd index.
Its `gaps_of_entry` assumes an odd entry time t0, membership in the particular
829-window trap, t0 <= 2*s+1 and u R s = true. The next true sample is exactly
three or five samples later. For the empty right half, entry is physical293,
visible index146. The index146 is not a universal entry time for all R.

The channel-14 source samples column1 at EVEN physical times, under a clock
white at time0. Restart the driven row at any odd T=2*a+1 and write
`y(t,p) = drv altCol R (T+t) p`. The driver's value is now `t % 2 == 1`;
the restart identity is the existing kit `Rule30PeriodTwoSideways.drv_shift`.
Then `y(2*k,1) = u R (a+k)`. Gaps3 and5 count exactly the same visible
symbols, or6 and10 physical ticks, on both sides. There is no factor-of-two
rescaling of the published entropy per visible symbol.

**Do not assume a whole-line extension with a genuine clock.** The published
`channel_bound_14` is stated with a whole-line `Clock` premise. An arbitrary
clamped row is not supplied with such an extension. Instead its underlying
certificate applies directly:

1. At every even restarted time, pack columns1 through14 into s. It is below
   2^14, and its low bit is the observed symbol.
2. The next packed row is exactly `step2 14 (2^14-1) s u v`, for the actual
   two successive right-boundary inputs u and v, each0 or1. The source's
   `nxt` applies the white boundary first and the black boundary second.
3. `root14` puts every starting s in certificate state0. `all14` and
   `explicit_sound` give `EdgeOK` for every live state and symbol. Induction
   therefore keeps the actual window in a live successor state for every
   observed symbol. A graph edge to DEAD cannot occur on the driven trace.
4. The existing weighted path bound applies to those accepted words. The
   constant300 and ratio1184655442/10^9 therefore also bound the number of
   clamped-trace prefixes, by this interface proof. No new axiom or condition
   on the unknown right boundary is being assumed.

This proves a rejection transfer, not a converse: arbitrary allowed boundary
choices in a width-14 graph need not come from one consistent infinite right
half. Graph acceptance must not be called actual realizability.

For an infinite trace in the trap, take its one-sided orbit closure, or the
factor language of all trapped tails and its shift closure. These are the
appropriate shift-closed objects. Their language is contained in both the
clocked language and the3/5 renewal language. A raw collection of initial
finite-seed traces need not itself be closed, so calling it a subshift without
taking a closure is unwarranted. The strict entropy comparison in GC2146
applies to the closure: the renewal root exceeds1.19, while the certified
channel ratio is below1.19. This is a known-certificate consequence, not a
new realization theorem, density claim, or prize result.

## Prior art recovered before computing

The claim in SYNTHESIS-20261029 sections3.5/5.2 that nobody has written down
forbidden gap words overlooks at least these exact earlier results:

- L590, 10 October: two42-symbol phase-0 forbidden words,
  `010010010000100001001001000010000100001001` and
  `001001000010000100001000010010000100001001`.
  Local reported DRAT-to-LRAT/cake_lpr VERIFIED UNSAT and direct simulations
  of the proper one-symbol deletions. These are retained historical verdicts;
  this block reads the complete entries and encoder/translation, but does not
  replay those proof files.
- GC1009/CL185 and GC1011 translate them to recurrent macro factors
  `SSLLSSLLLS` and `SLLLLSLLS`, where S=001 and L=00001 follow an initial1.
  Startup matters: deleting the leading0 of the first gives an actual
  startup-only word; deleting00 from the second gives an actual word possible
  at visible indices0 or1, but not2 or later. A recurrent ban is not a blanket
  rejection of those startup suffixes. The independent CL185 hand read
  carries the first predecessor argument; GC1011 additionally uses101001.
- GC1007 and SLC/SLC2/SLC3 already intersected the3/5 gap grammar with exact
  finite forbidden-word lists. The source header records83 certified cuts
  after18 rounds and remaining branching. Neither finite surviving branching
  nor graph entropy establishes actual infinite branching.
- L627/L628 correct the early unsupported claim about a periodic M2 word:
  `(LLSSS)^6` is a114-symbol forbidden factor in both phases, with another
  minimal cut at117. Not all120-symbol rotations were absent. The exact
  receipt and later correction supersede the informal SLC2 note.
- Earlier GC610/GC611 already studied reported seven-gap exclusions and
  their neutral-family consequences. Their stated evidence gates remain;
  they are not fresh certificates from this block.

Sources: [L590 and CL185](../archive/ledgers/CHAT-LEDGER.12.md),
[L627/L628](../archive/ledgers/CHAT-LEDGER.13.md),
[GC1007/1009/1011](../archive/gpt/RULE30-GPT.8.md),
[exact macro translator](../tests/probes/lexicon/rule30_sl_macro_cut.py),
[SLC source and actual outcomes](../tests/probes/lexicon/rule30_sl_cuts.py).
No old SAT calls, SCC-growth experiments or missing-cut search will be repeated.

Record searched: `SSLLSSLLLS|SLLLLSLLS|gap word|gap-word` plus the exact earlier
IDs; actual current kit932cf8dde039b89b1dcbe9636867bb1b2057fef0, lean/equivalents/
catalogue and listed portal/open-PR index refreshed22:47:13Z. Width6's
`col1_constraints` is conditional on an eventual centre clock and eventual
bad-class entry; its gap notation counts zeros, unlike distances3/5 here.
It is not an unconditional full arbitrary-driven-language classifier.
Actual230bc7 `gaps_of_entry`, current `drv`/`drv_shift`, and source-bound
channel-14 `EdgeOK`/`explicit_sound`/`root14`/`all14` were read.
The published channel proof SHA256 is
7559970244b025c1733a9fc98f1f16a2583366ff8d70edb5cfda50bd71f42fd7.

Primary background: Wolfram, *Computation Theory of Cellular Automata*,
Commun. Math. Phys.96(1984),15–57, section2 and discussion on p54
([author-hosted paper](https://content.wolfram.com/sw-publications/2020/07/computation-theory-cellular-automata.pdf))
already treats finite automata and finite-time CA languages. This is general
background, not a source for this particular temporal trap or its exact cuts.
No novelty claim is based on the search.

## GC2208 frozen certificate diagnostic

One source reader only:
[channel14_gap_audit.py](../tests/probes/wolfram/channel14_gap_audit.py),
SHA256 eb2b3148b11bd692a0416ba7c725c186f5db883bfc388f202453121332e6dc07.
It reads the919-state `succ14`; it does not regenerate the DFA or compile Lean.
Breadth-first search finds a shortest rejected rooted word `1 + blocks` by
number of complete gap blocks, and a fixed dynamic count answers the offered
question through8 gaps. This does not find a shortest arbitrary binary word.

Prediction P1: some rooted gap word is rejected within8 blocks. Counterfactual:
all pass at that cutoff, making the short-word proposal ineffective at this
width. Prediction P2: the certificate misses both of L590's42-symbol cuts.
Counterfactual: one or both already have a graph rejection and can inherit its
existing formal closure certificate. These are diagnostic predictions, not
assumptions used in the phase proof.

Independent control: enumerate only the16384 fixed-width windows, compute all
four two-step images by the literal eight-entry Rule30 table, compare against
the packed formula, and propagate sets for the selected witnesses. This is
an oracle for the finite-width relaxation only. Check11/00000 as negatives,
eight pure S/L blocks as positives, and the old actual startup suffixes as
unexpected boundary controls. A graph/oracle mismatch stops the stage. The
shortest witness must be at most256visible symbols or the stage stops without
automatically widening. No seed census, new SAT, entropy fit or GPU work.

Intel headroom before freeze:8physical/16logical cores,16GiB, load1.70/2.12/2.12,
about5918MiB free+inactive,225.25MiB swap. One Python compute process/thread,
nice10; run_capped120CPU/300wall/768MiB RSS, tree/max3processes, launch4096MiB,
running3072MiB free+inactive,64MiB swap-growth stop,16MiB/file128MiB/stage.
Internal wall stop240s. Per-process CPU covers the sole computing process;
the runner/time wrappers are separately reported, not claimed to have an
aggregate tree CPU cap. No concurrent heavy job. No retry, expansion or cap
relaxation after failure; retain failure and cleanup receipts. No reliable
thermal reading is available. Source reads are bounded8MiB each, JSON output
is bounded by the919-state graph and fixed11cases. Raw data stays outsidegit.
