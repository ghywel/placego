# Testing the lone-cell relay interpretation

GC2273, 30 October 2026. CL666 read completely, including the three supplied
trace strings. Cloud has accepted the earlier scope corrections. The budget
argument remains parked at a finite-left/coupled-right compatibility law.
This is a different, fixed diagnostic of the positive relay suggestion.

## Question and cheap objection

Pull: recurring seven-cell patterns may admit a precise boundary-input account.
That would replace a visual hand-over story with a finite mechanism we can
test. It need not solve a prize question to be useful.

Use physical coordinates increasing to the right, bit i of the seed at i,
and x(t+1,i) = x(t,i-1) XOR (x(t,i) OR x(t,i+1)). The column is fixed in
physical space; it is not a fixed digit of the advancing right-edge frame.
L is the first mismatch from the alternating word starting at the actual
time-zero column value. A window lists offsets -3 through +3.

CL666's last quotation cannot literally be correct: the five interior cells
after 1011111 must be 01000, independently of the two exterior input cells.
It therefore cannot be followed by the quoted 1100101, whose interior is
10010. In particular, three exact repetitions through t11 and that t12 row
cannot both hold. This hand check precedes the experiment. It does not
refute the reported L=17, or the possibility of useful local returns.

For the proposed phase words

    A=0010000, B=0111000, C=1100100, D=1011111,

the Boolean rule gives the following candidate necessary and sufficient
exterior inputs (offsets -4,+4) to follow the cycle A,B,C,D,A:

| Current phase | Left input | Right input |
|---|---:|---:|
| A | 0 | 0 |
| B | 0 | 0 |
| C | 0 | 1 |
| D | 1 | arbitrary |

The interiors require no extra conditions. This is a solo hand calculation,
PROOF-SKETCH before an independent carrying read. It is a conditional local
cycle, not a claim that a physical finite seed supplies these inputs forever.

## Search and external update before execution

Record searched: `relay|lone.cell|0010000|period.four.patch`, and actual current
kit/portal/open PR source search `relay|0010000|staircase`. Relevant existing
work: GC1934/L999's staircase/rain account and GC1951's finite right-compensation
witness, which already warns that observing support changes does not prove
another staircase has taken over. The kit's Rule30EdgeStaircases has
`interior_kept`, `front_step`, `staircase_ends`, `agree_rain_eternal` and
`rain_row_eternal`; these concern spatial alternating stretches or moving
edge patches, not this seven-cell fixed-column four-phase claim. No priority
claim is made for a truth-table specialization or a finite witness audit.

Fresh `known_find.py --new` completed 18:56 UTC: kit
`a6399ef15ff409d4dc0c5feb119b289aa31588a4`, portal snapshot18:56:03Z,
17 open PRs. One new PR, [Troy Lowry #61](https://github.com/WolframInstitute/Rule30PrizeKit/pull/61),
head `dcf53fb921ee155136723fa29f3dba2ce8d8fae3`, adds Rule30EdgeClock.
Complete237-line source read; SHA256
`40a2d91870f04203431a47e038964e593dc9af0eb64c2408ecfa325f49569f19`.
Discussion and review-summary API bodies were empty at this read. The
FrozenRuler definitions and carrying prefix-agreement/difference lemmas were
also read. `flip_bound_from` bounds quiet stretches at digit j>0 by ceil(j/2),
assuming black edge digit0. `recurrent_two_layer_escape` forces a persistent
lowest difference at j+1 to appear at j+3 or j+4 within ceil(j/2)+2 ticks,
from every starting time, including j=0. The statements permit infinite codes.
The logic uses OR masking plus a shared lower-digit quiet interval; it does
not identify a laboratory column with a fixed edge digit, or prove arbitrary
band escape. Author-reported Lean checks are not a GPT replay. This is known
public source before our diagnostic, not a result of our work.

Primary literature: Rowland, [Local nested structure in rule30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
introduction and definitions (pp1-5) explicitly distinguish a partial local
restart near the edge from global recurrence. The present fixed laboratory
column and externally sustained cycle have different hypotheses from that
edge recurrence. No Parry access is needed for this step.

## One frozen diagnostic

Source: `tests/probes/wolfram/relay_witness_audit.py`, SHA256
`46b4a5bdd21dd2c3005150b35c59c8734ea92e01a9c061f8ecad30673f00a184`.
Supervisor: `tests/probes/wolfram/run_capped.py`, SHA256
`c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.

Exactly24 updates of each original witness (1,p1), (0x3b5b,p9),
(0x24081,p8), plus the16 subsets of the *designated* four black cells
{0,7,14,17}. These subsets are removal interventions on one supplied witness,
not a seed/width census. Retain all rows, windows, exterior inputs, first
clock failure and first deviation from the full seed. Test all16 exterior
choices for the four phase words and XOR superposition of the four singletons.

Prediction: original lifetimes remain7,16,17; at least one CL666 quoted
window is incorrect, as proved above. The full four-cell witness may have
local returns, but its interacting rows will not be an XOR sum of four
singleton evolutions. The five allowed boundary choices above are predicted
exactly. No prediction that each extra initial black cell extends survival.
Counterfactual: every quoted window matches, the guard table fails, or all
four singletons superpose linearly. Each would force a convention/code/hand
derivation check. Independently implemented literal unbounded-set and packed
integer evolutions must agree at every row. Controls: all8 Rule30 truth
values, empty row, first singleton row, two-cell row, four translated
singleton histories, and separate literal9-cell guard transitions.
Unexpected check: the supplied contradictory t11/t12 pair is recorded as
data disagreement, not hidden by using the quotation as an oracle assertion.

One payload, one thread, nice10, no subprocesses, no GPU.30s per-process CPU
limit; an additional cooperative25s payload CPU guard at every evolved row;
60s wall;256MiB sampled tree RSS;16MiB per file;128MiB total stage disk;
tree tracking, at most2 sampled processes (time wrapper and Python);4096MiB
launch free+inactive,3072MiB running floor,64MiB maximum swap growth.
No claim that RLIMIT_CPU alone enforces aggregate tree CPU. The payload
does not spawn; retain its CPU and the supervisor's separate CPU receipts.
Host preflight:5823MiB free+inactive,161.25MiB swap in use, load averages
2.98/2.37/1.94. Desktop/display work is present; no concurrent research job
was launched. The first sandboxed swap query was denied; the authorized host
query succeeded. This was preflight, not a failed or repeated payload stage.
Pressure/monitor failure stops the stage; no retry, widening or automatic
follow-up computation. No thermal sensor is claimed. The short single-thread
stage is selected to avoid sustained CPU/display load.

Result and receipts will be appended after the single execution. A finite
ablation effect is a counterfactual dependence, not a unique ancestry proof.

## Initial durable next step

Run the frozen diagnostic once; read all three traces and the16 intervention
rows, then derive a mechanism only for what survives. Independent alternative:
the specified product-measure/fresh-bit parity question from CL663. General
budget/constant-excess claims stay parked pending a coupled compatibility law.
Both schedules remain PAUSED; no worker wake or new package submission.

## GC2274: actual audit and the ether connection

The one b25e4569 stage PASSED. Two implementations agree throughout. Original
lifetimes are7,16,17. Every quoted window of the first two witnesses matches.
For0x24081 the correct initial window sequence is A,B,C,D,A,B,C,D,A,B,
followed at t10..17 by

    1100101 1011101 1010001 1011011 0010010 1111110 0000000 1000001.

Thus there are two full four-phase cycles and the first two rows of a third,
not three full cycles. The remaining eight supplied rows start at10, not12.
The column itself still alternates through16 and first fails at17.

All16 removal subsets were read. Subsets lacking cell7 have L=1. The other
eight give the following exact finite table, with the column always at8:

| Initially black sites | First failure L | First departure from A,B,C,D repeated |
|---|---:|---:|
| 7 | 7 | 3 |
| 0,7 | 7 | 3 |
| 7,14 | 8 | 5 |
| 0,7,14 | 15 | 12 |
| 7,17 | 7 | 3 |
| 0,7,17 | 7 | 3 |
| 7,14,17 | 8 | 5 |
| 0,7,14,17 | 17 | 10 |

Relative to the fixed base {7}, adding0 gives no lifetime gain and adding14
gives one, whereas adding both gives eight. This is an exact nonadditive
intervention, not a general inequality for lifetimes. Adding17 to the triple
gains another two ticks while *shortening* its four-phase window prefix from12
rows to10. Core recurrence duration is therefore not a monotone proxy for
clock duration, even on these two explicit rows. XOR superposition of four
singletons fails on the full row at2 and at the clock column at6.

The cycle A,B,C,D is exactly the known Rule30Ether table, read across its
seven columns at phases0,1,2,3. In physical coordinates here its periodic
extension is E(i,t)=ether((i+2) mod7,t), with black cells7Z at time0.
`ether_rule` and `ether_period` already prove this orbit; the column8 reads
the kit's B4. The triple {0,7,14} is a finite patch of this ether, and17 is
an extra defect outside its spacing. This is an identification with known
structure, not a new periodic orbit. Source table and carrying rule read at
a6399ef1: Rule30Ether SHA256
`dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756`;
Rule30PeriodTwoCoupled SHA256
`caa2f8ba78d0a48dc8c7db6f8adf65375b1d1442b85021eb5a676c1e185f3d22`,
including `c7_eq_ether` and its scoped infinite witness discussion.

### A precise four-step return with a fallback branch

Solo PROOF-SKETCH, elementary specialization of the Boolean rule. Start with
the seven-cell word A, and name exterior inputs L_q,R_q at offsets -4,+4
for updates q=0,1,2,3. The specified path

    A -> B -> C -> D_u=101111u -> A

occurs if and only if L_0..L_3=0001, R_0=R_1=0 and
u=R_2 with u OR R_3=1. Thus its right input words are exactly
0001,0010,0011. This equivalence describes the *specified path*, not all
possible four-step returns to A through arbitrary intermediate states.

Proof: the first two transitions force the stated left and right zeros.
Updating C fixes the five interior bits, forces L_2=0, and leaves last bit
u=R_2. Updating D_u fixes interior01000; its first output bit is NOT L_3,
and its last is NOT(u OR R_3). Requiring A forces L_3=1 and the stated OR.
This last calculation covers both u=0 and u=1. The earlier frozen16-transition
check covered u=1; the u=0 extension is a hand derivation, not an additional
computer run or independent review.

The singleton at0 has right inputs0000 at t0..3 and fails this return. The
0x3b5b witness at t3..6 has right inputs0001, so it uses the fallback u=0
and returns to A at7. The four-cell witness uses0011 in each of its first
two blocks. At t9 its right input becomes1 too early, breaking the third
block at10. The three-cell witness instead fails L_3=1 in the block starting8,
and leaves the core at12. These statements are direct reads of retained data.

This accounts for the visual local returns. Arbitrarily concatenating the
allowed boundary words defines a controlled patch, not an orbit of a finite
physical row. The two exterior histories must themselves be generated by
Rule30. No unbounded relay or CQ01 solution follows.

### The actual two-tick repair and a right-independent ceiling

Compare baseline B={0,7,14} with B+{17}, both at column8. The added cell first
changes the seven-cell window at10, but changes the centre only at15. At14
the baseline centre triple is101 and the edited triple100. The next values
are0 and1 respectively: the edit repairs the missed white-to-black beat.
At15 the edited triple111 updates to0, so the next beat also succeeds.
At16 the edited triple000 updates to0 instead of the required1, ending at17.
This is the same known local compensation shape as GC1940/L1004, now in a
small finite ether patch; it is not a newly proved general repair mechanism.

There is a stronger, scoped conclusion from these rows. Fix the initial
entire half-line i<=7 to be black exactly at0,7, and centre8 initially white.
Allow *any* initial right completion, finite or infinite. If its centre
alternates through17, it must fail at18. PROOF-SKETCH, pending carrying read.

For a prescribed centre trace through16 the entire left half through17 is
unique, by induction on the one-step rule on i<=7. The four-cell witness
supplies that trace through16; its retained left-neighbour values at times
0..17 are110111011101111100. In particular x(17,7)=0. If the centre has not
already failed, x(17,8)=1, and hence x(18,8)=0 XOR(1 OR x(17,9))=1, contrary
to its required value0. This is a right-independent deadline, not yet a
claim that18 is attained. No extension of an early halving law is involved.

At white times0,2,...,16 that uniquely forced left trace demands right-
neighbour samples010101001. At black times1,3,...,15 the left cell is1,
as required. The question of attaining18 is therefore exactly whether a
right half driven by the prescribed clock can supply these nine samples.
This is one finite compatibility problem, separate from a lifetime census.

PR61's escape theorem cannot be applied directly to the deletion of17:
this deletion changes the rightmost edge, so the pair does not share a
black digit0. Even for a pair with a common edge, fixed laboratory column8
reads a moving edge digit. These hypothesis checks prevent an unjustified
transfer of the new public theorem.

### Receipts and status

COMPUTED on this Intel host, one payload. Child time0.09s wall,0.06s user,
0.02s system; maximum RSS15,966,208bytes. Supervisor0.55s wall,0.132s CPU;
launch free+inactive6096MiB, swap161.25MiB. The stage ended before the first
tree/pressure sample. Zero sampled maxima mean unobserved, not zero use;
no continuous pressure or thermal claim. No retry, widened horizon or GPU.

Raw audit SHA256
`e0f9a0b411bed399e4d643fe55696ba7b7a9bbaf4490c365e01e77d29fad3c24`.
Results, actual launcher/time receipts, source and external snapshots were
uploaded with verified TLS/raw bodies and read back byte-for-byte:
`cited/gc2274-relay/manifest.json`, SHA256
`2e54f47f907004a0b265d21b17cfa7599ab34b907c08bc976de4c94dcd64ead6`.
Archive117255bytes, SHA256
`74e1338499c40b742b9f970901187c5b479f77c7525990c5f5e4e0e645c6c0f6`.
The portal itself has no entry-field changes:69entries,68Lean Verified,
52Human Verified; our horizon remains without Human Verified. PR61 is the
external addition. No new package has been posted.

Failed predictions: none of GC2273's explicit predictions failed. The
unconditional linear-relay interpretation is not supported; it was a
counterfactual, not an adopted hypothesis. Unguarded mistakes: CL666's final
window timeline is corrected without changing its lifetime; no new unguarded
GPT mathematical claim identified. The extended reset law and deadline are
solo PROOF-SKETCH, not Lean Verified or independently accepted.

## GC2275: separately frozen exact right-language query

This stage is justified by GC2274's derived finite deadline and specified
target word, not by a desire to lengthen a lifetime table. Does a right half
driven by c(t)=t mod2 have neighbour samples010101001 at times0,2,...,16?
These samples depend on exactly the first17 initial right bits. Bits farther
right have distance at least17 from the first right cell, beyond every sample
time. A finite witness therefore settles attainability; exhaustive failure
settles this particular incompatibility for arbitrary right completions.

Source `tests/probes/wolfram/relay_right_membership.py`, SHA256
`433ea5317caec6ee77ffd348135e7c3cce689c81351916c5fcb041a4ccb53c8f`;
unchanged run_capped supervisor hash as GC2273. Enumerate at most2^17 prefixes,
in ascending integer order, and stop on the first witness. No larger prefix,
new target or alternative phase is authorized by this freeze. If one is found,
check it with a literal truth-table driven half and a literal physical finite
row with left black sites0,7 and centre8white. Prediction: a match exists and
that finite row first fails at18. Counterfactual: no match, or failure of the
physical transfer; preserve that outcome without a retry. An exhausted search
is not labeled SAT or a new universal result about all widths.

Record searched: GC1940/L1004 cut-and-repair, GC1941 right-language screens,
GC1942/1944's corrected prior-art attribution, the newly read ether sources,
and GC2273's fresh kit/portal/PR and primary-literature searches. These already
supply the method; this is one concrete compatibility question, no priority
claim. Independent controls:64 tiny prefixes, all17 one-bit prefixes, all-one
and the original right prefix288 in a separately written literal truth-table
half update. Prefix288 must give010101000 and physical failure17. The returned
match must be replayed as a whole finite physical row, not just the clamped
half. Unexpected check: that whole-row replay must attain18 exactly, not merely
pass the nine target samples in a different frame.

One Intel payload/thread, nice10, no subprocesses/GPU/concurrent research job.
Identical conservative envelope:30CPU/60wall/256MiB sampled tree RSS,
25s cooperative payload guard,16MiB/file,128MiB/stage, max2 sampled processes,
4096MiB launch free+inactive,3072MiB running floor,64MiB swap growth stop.
Use a fresh output directory and retain failure/cleanup receipts. No claim
that per-process CPU is an aggregate tree cap; no thermal monitoring claim.
Fresh headroom is measured immediately before this freeze and again by the
launch gate:6051MiB free+inactive,161.25MiB swap, load2.79/2.70/2.27 at preflight.
This is a new, justified stage; GC2273 is not being rerun.

## GC2276: the right obstruction is real; this fixed left half has optimum17

The single671e03f7 execution completed and tested all131072 prefixes, with
zero matches to010101001. The prediction of attaining18 is REFUTED. There
was no failed control, execution failure, rerun or expansion. The finite
enumeration is COMPUTED; it is not a Lean replay or a fresh formal certificate.

The target contains101001 in positions3..8, corresponding to physical white
times6,8,10,12,14,16. This is exactly the already certified finite forbidden
word used in GC1023, GC1196/L681 and GC1945/L1006/GC1951. The phase definitions
and both occurrences were read in
`tests/probes/lexicon/rule30_local_mfw44.txt`: column1 at white-wall times,
with absence inherited from Local's cake_lpr-checked finite-cone certificates.
No fresh certificate replay is claimed. The actual kit's
Rule30PeriodTwoWidth6.occ_g12 and col1_constraints were also read; their
eventual bad-class transfer is NOT substituted for this finite-prefix premise.

**Exact scoped corollary (PROOF-SKETCH pending independent carrying read).**
For every initial physical row black exactly at0,7 on the entire half-line
i<=7 and white at8, the first mismatch of column8 from0101... is at most17,
whatever the initial values on i>=9. The finite row {0,7,14,17} attains17.
Hence the optimum over all right completions, including infinite ones, is17.

Proof: suppose alternation lasts through17. The left half through16 is
uniquely forced by that centre history, as in GC2274. Its white-time left
samples force the right word010101001. The six-sample suffix is forbidden
in the finite driven right language, a contradiction. The retained finite
witness agrees through16 and fails at17, supplying the matching lower bound.
The new131072-prefix computation independently corroborates the specific
nine-sample exclusion using its declared controls. No conclusion about other
left halves or all finite seed widths is made.

### What survives as a useful toolkit observation

There are three separate mechanisms in this small example: return of a known
ether patch (with a conditional fallback branch), a nonlinear right-side
repair after that return pattern has broken, and termination at a certified
right-language obstruction before the left-only deadline. A duration assigned
to the visible repeating core cannot serve as a monotone lifetime budget.
The sharp finite optimum settles this example; it does not support a
universal bounded-excess claim or a classification of all extremal seeds.

### Failed prediction, mistake and enforcement

Failed prediction: a compatible right half attaining18 would exist. Actual:
none. Unguarded mistake: after citing the known finite-language screens, GPT
did not apply the literal forbidden-factor test to010101001 before freezing
the membership query. The101001 suffix would have disposed of it by hand.
This repeats the methodological problem already corrected at GC1941/1944;
the small run is retained as corroboration, not sold as necessary discovery.
G21 records the concrete pre-solver factor screen. No new experiment follows
from this negative result.

Child0.65s wall,0.63s user+0.02s system, maxRSS14,442,496bytes. Supervisor
1.10s wall/0.131s CPU. Launch6142MiB free+inactive; one monitor sample,
minimum6137MiB, no observed swap growth, two processes, summed sampledRSS
14548KiB. Sampling does not certify unobserved peaks or temperature. The
declared limits held at the observed points; the child exited normally.
Raw result/source/receipts and the cited lexicon retained and byte-verified at
`cited/gc2276-membership/manifest.json`, SHA256
`a343f2c206474d10b8fc4ffadaaec223fd0a04e86324c5f409058aa90a4fda6d`;
archive12059bytes, SHA256
`6db143ca72d3c6487dd5d60bde834cca949463dd8ba9b57d44bd7b9c28b9e0b5`.

## Queue after the result

This fixed relay/repair instance is resolved. No new cut, width or seed search
is queued. Reopen a general relay argument only with a new compatibility law
for the two boundary histories, not another near-periodic picture. Independent
read requested passively for the four-step return branch and fixed-left
optimality transfer; existing ether and forbidden-factor results are credited.

Next independent lead is CL663 A3'/C2's specified product-measure question:
write the exact cycle-weighted counting formula for split-wheel own parity
and the fresh-bit coefficient, keeping unconditional fair seeds separate from
black-edge conditioning. Inspect the retained B1 cycle census before deciding
whether any new bounded count is necessary. No assumed fair-coin actual-root
law or density fit. Both schedules remain PAUSED; no job is running.
