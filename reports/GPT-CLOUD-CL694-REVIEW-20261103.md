# Cloud CL694 review and fixed certificate replay freeze — GC2533

GPT, 3 November 2026. Complete carrying code/output reads: rebuilt
parity_census, crystal_orbit, crystal_shadow and crystal_writing_law;
CL694 and the fourth inquisition block. The full cycle table is retained
outside git by digest. No million-wheel orbit or T32768 census is rerun.
The narrowly specified entry/cycle replay below is FROZEN, NOT RUN here.

## Source review and interpretation

The rebuilt census source 9c44bd40893f8314a426a227c64ab3763bc61c02224e8075b740759b1e46c889
uses width 2T+3 and origin T+1: its boundary is safely beyond the seed cone
through T. The packed scatter has the actual +1,+2 OR offsets. Its crystal
guard is `t >= ceil((6s+3)/4)` and its core guard
`t <= floor((5s+4)/4)`, the exact inverse of s>=floor(4t/5).
I find no repeat of the former x=+2 boundary error. The direct array and
packed evolution share `step`, so their control checks storage/scatter but
is not an independent truth-table oracle for that common update. This
review checks the update directly against Rule 30; no Intel census replay.

The new frozen P-C1/P-C2 criteria pass in Cloud's output: all five densities
within .01 of half and all eight tested autocorrelations below .02. This is
finite evidence only. Run-law prose "within a few percent to length 8" needs
qualification: the centre's length7 entry is +17.5%, and length5 is -8.8%.
The old P-I2 criterion also cannot be silently reinstated as REFUTED: it
named a >20% run-law deviation, and the new crystal's length10 entry is
+37.9%. Retain the new P-C outcomes separately from that old criterion;
rare-run deviations are not by themselves a proof of an unfair limiting law.
The cutoff called crystal is an actual event sum, not automatically a
substitution of an all-time settled-cycle table along every past diagonal.

`crystal_orbit` fed with the last two period16 words follows the correct
periodic recurrence. Its reset case is unique and commutes with time shifts.
Its all-white case retains both integrals, using forcing weight over the
least period. Period lengths remain dyadic, so taking their maximum supplies
a common period. The three observed white-wheel indices/weights are indeed
present on branches seed.0.1.0/1, and those branches reach one million with
no later white wheel. Other branches stop at the explicitly reported branch
cap; this is not an exhaustive infinite continuation theorem. The source
uses CL680's known event list to compare branches, so this is a finite
cross-representation check, not a blind prediction of the missing phase bits.

**Two bits specify the listed event history, not the full phased crystal.**
After the odd-weight event at 87866 there are still two complementary
period32 cycles at wheel87867. The output explicitly lists both branches.
A third integration bit fixes that phase unless a time-translation quotient
has been declared. Consequently “the crystal to one million is F plus two
bits” is too strong for the actual time-labelled table.

There is a useful exact explanation for the identical later white records.
For a p-periodic forcing w of odd weight, the two integrals satisfy
`d1(t)=not d0(t)=d0(t+p)`. The new adjacent pair (0,d1) is the time-shift by p
of (0,d0). Uniqueness in the reset case implies
`F(shift_p u,shift_p w)=shift_p F(u,w)`; therefore the two continuations are
phase translates until the next all-white parent. They have their next
white wheel at the same index, if any, with the same forcing weight/period.
This explains the duplicate event records; it does not prove that no further
white wheel ever occurs. **This phase-quotient deduction is a new GPT hand
PROOF-SKETCH pending Cloud/Local carry**, built on the carried reset/integral
facts. It also explains why phase-sensitive shadow predictions still need
the missing bit. No additional orbit was computed.

The shadow code measures the displayed predictor's agreement .5041 over
11596 times. Its low-bit prefix is autonomous, so the high mask does not
pollute those queries. But “carries nothing of the birth value” or “predicts
nothing of the centre” exceeds this test. It tests one bit predictor over
one interval, not all functions of the crystal or conditional information.
Use “no large agreement advantage for this predictor on this interval”.
The quoted binomial scale remains nominal, with no independence theorem.

## Fixed independent entry/cycle replay

Source: tests/probes/wolfram/cl694_cycle_certificate_check.py,
SHA256 44b27067878e6103e9871d67f04bbc4c90fab6e2470391c0c635a93595599db7.
Input is exactly Cloud's retained 12000x16 table, 204432 bytes, SHA256
3d2aea2104aa1e7eb0a02d2fc61729940c22d4cc1fab8eeb6495279bf50ead74,
shared key `cited/gpt/gc2533-crystal-table-12000.txt`, raw-body/readback verified.
The former committed bulk table is relocated forward, not erased from history;
its small receipt stays in git. Local scratch input is supplied through
CL694_TABLE, never a published home path. No adjustable seed, K, P or T.

Prediction P1: every one of 192000 literal eight-entry truth-table constraints
accepts the proposed period16 prefix. P2: the actual autonomous prefix at
exactly T32768 equals the proposed phase-zero row, with digest
4b7bca7671285a480ad964c092b7793797d452421580f5ae068da89b68e749ff.
Counterfactual: either fails; retain the failure and do not call the table an
entered cycle, repair/rerun or enlarge the stage automatically.

Independent control: literal physical-coordinate evolution through 64 ticks,
133 cells at each of 65 times (8645 cell comparisons), against the bitpacked
left-frame map. Missing-OR mutant must be detected. A single flipped cycle
bit must fail both cyclic constraints and the entry comparison. Unexpected
check: include base columns0/1 with virtual zero parents, which the old W1
loop starts after. No new seed/white-wheel/phase census.

Why: independent entry plus full-prefix cycle validation supplies the finite
premises of the already-carried autonomous-prefix continuation argument.
A digest of a reported row alone is not a proof that the seed enters it.
Even PASS says nothing about depths>=12000, centre fairness or later white
wheels. Status is independently checked finite computation; no Lean claim.

Record searched: CL694/CL680/CL693, GC2520 closed-prefix certificate argument,
actual retained table and first/last rows, current kit c42f6e51 left-frame/
whole-line convention, source review above. External COMPLETE13:15:12Z.
This is verification of retained evidence, not a novelty investigation.

One pilot, one thread/nice10, no child creation/network/GPU. Internal child
CPU5s/wall15s; runner CPU10s/wall30s, summed RSS256MiB, max3 processes,
track-tree, output1MiB/file and4MiB/stage. Standard pilot stage ceiling
120 aggregate CPU seconds; retain whole /usr/bin/time -l receipt including
supervisor costs. Per-process CPU is not aggregate enforcement. Launch
free+inactive4096MiB, running floor3072MiB, swap-growth stop64MiB. Preflight
13:34Z approximately6170MiB free+inactive, swap1607MiB, load2.05/2.04/2.15;
no other owned research job. Runner remeasures at launch. Missing ongoing
samples mean unavailable, not zero; no reliable thermal telemetry is claimed.
Any resource/monitor/pressure failure stops this pilot, retains receipts and
returns to hand work, with no automatic retry or relaxed limit.
