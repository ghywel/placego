# A guarded front explains the finite clock imitation

GPT,30 October2026, GC2223. **PROOF-SKETCH, solo hand derivation.** Independent carrying
review remains pending. This resolves a finite-family question suggested by PR48's retained
data; it proves neither an edge-density limit nor a prize claim. The bounded self-check was
frozen separately at GC2223 and passed once at GC2224; its actual scope and receipts are below.

## Claim and conventions

Use depth from the right edge, increasing to the left. Extend the actual row by zero to
negative depths and update by

    x_j(t+1) = x_j(t) XOR (x_(j-1)(t) OR x_(j-2)(t)).

The negative depths remain zero. This gives the official special updates at depths0 and1.
Let B(t,j) be bit(t mod8) of the word [149,101,89,86][j mod4], with Euclidean residues for
negative j. The eight rows, read in increasing j mod4, are

    1110, 0001, 1101, 0010, 1011, 0100, 0111, 1000.

These obey the same recurrence on all integer depths. This is PR48's carrier, already
identified in the record as the period-eight ring orbit passing through0001 and0111.
It satisfies B(t+4,j+6)=B(t,j).

Start the actual half-line with x_j(0)=B(0,j) for j>=0 and zero below0. Define b(t) as the
largest depth where x(t) differs from B(t). For h>=0,

    b(4h+1)=6h,    b(4h+2)=6h+2,
    b(4h+3)=6h+2,  b(4h+4)=6h+4.

Thus b(t+4)=b(t)+6 for t>=1. The leading defect has a guarded four-phase cycle,
even though the older cells behind it need not repeat.

For PR48's finite seeds

    c_n = sum_(0<=i<n) 7*16^i + 5*16^n,

let f_n be the first time the pair at depths4n+3,4n+4 differs from the periodic words234,170.
The exact first-failure times are

    f_0=6;
    f_(3k+1)=8k+6, f_(3k+2)=8k+9, f_(3k+3)=8k+13  (k>=0).

The numerical values were already observed in the author's67 retained cases. The proposed
contribution here is the guarded induction for all n, not the discovery of those numbers.

## The four-phase front, including its incoming guard

At phase A, time t=4h+1 and front s=6h, the background from s onward is00010001... .
Assume actual cells s-2,s-1,s are101, and every cell above s is background. Cells below
s-2 are arbitrary. Direct substitution gives this table; words are read in increasing depth.

| Phase | Time | Front | Known actual word ending at the front |
|---|---|---|---|
| A | t | s | 101 at s-2..s |
| B | t+1 | s+2 | 1011 at s-1..s+2 |
| C | t+2 | s+2 | 100 at s..s+2 |
| D | t+3 | s+4 | 100 at s+2..s+4 |
| A | t+4 | s+6 | 101 at s+4..s+6 |

Every cell strictly above the listed front is still background. Here are the carrying
calculations that remove the arbitrary incoming cells. From A, the new cells at s-1,s,s+1,s+2
are respectively1,0,1,1: the old1 at s-2 masks the unspecified s-3. From B, the new cells
s,s+1,s+2 are1,0,0: its first1 masks the unspecified s-2. From C the three new cells at
s+2,s+3,s+4 are1,0,0. From D those at s+4,s+5,s+6 are1,0,1.

The maximal defect can advance by at most two in one step. At A,C,D the background cell just
above the old front is0, so the flipped front forces a defect two places ahead. At B that
background cell is1 and masks the two-place advance. The next cell stays background because
both the actual and background OR are1. The front itself remains defective because its actual
preceding cell is1. This verifies both the absence of an earlier leading defect and the exact
stalled step. **GC2225 clarification:** at the specified phase A, the leading defect itself
forces the needed one-step B guard. The three-cell hypothesis closes the displayed trailing
signature and the exit calculation; it is not necessary for the front speed.

The first phase A at t=1,s=0 has001, not101, at s-2..s. Its two negative cells remain zero.
At t=2 the cells0,1,2 are111; at t=3 the cells0,1,2 are100; at t=4 the cells2,3,4 are100;
at t=5 the cells4,5,6 are101. No larger depth differs from background at those times.
This supplies the exceptional entrance, then the four-phase induction applies forever.
The first-failure front statement is therefore not inferred from a repeated finite sample.

For comparison, if phase A has001 at s-2..s, with the two older cells s-4,s-3 equal01,
then the corresponding word at s+4..s+6 four ticks later is001, not101. The extra older1
changes the guard. This is a hand countercontrol to dropping the three-cell hypothesis from
the signature claim, not a counterexample to the phase-dependent front-speed law.

## The exit has three arrival phases

Set N=4n. PR48's free template C_n equals B through depth N; its next four temporal words
are154,21,234,170. Initially c_n agrees with C_n through N+4. No larger depth can affect
these columns. Through depth N the actual evolution agrees with that of the half-line
carrier, by triangularity.

Before the front reaches N, all columns beyond that front through N+4 still agree with C_n.
Indeed, the carrier/front induction applies while its next front is at most N, and one step
cannot pass a defect more than two depths forward. In particular the update from a front at
N-2 cannot affect N+1. This proves agreement of the terminal pair at every earlier time,
not just at the displayed arrival times.

For n>=1 the first arrival at N and its guard are:

| n | Arrival time tau | Phase | Guard at N |
|---|---|---|---|
| 3k, k>=1 | 8k+1 | A | 101 at N-2..N |
| 3k+1 | 8k+4 | D | 100 at N-2..N |
| 3k+2 | 8k+6 | B | 1011 at N-3..N |

For clarity, write the actual four exit cells at N+1..N+4 in increasing depth. Subsequent
substitutions give:

| Arrival phase | Exit words at tau,tau+1,..., through the first failure |
|---|---|
| A, tau mod8=1 | 1011, 0100, 1111, 0000, **00 in the last two cells** |
| D, tau mod8=4 | 1100, 1011, **00 in the last two cells** |
| B, tau mod8=6 | 0010, 1111, 1000, **10 in the last two cells** |

The first listed word in each line is exactly the unperturbed template at arrival.
In line A the observed pair is11,00,11,00,00, while its target is11,00,11,00,11.
In line D it is00,11,00, against00,11,10. In line B it is10,11,00,10, against10,11,00,11.
The terminal mismatch is respectively four, two, or three ticks after arrival.

Here are the only guard-dependent exit steps. In line A the actual value at N changes
1,0,1 through its first three times, using the actual0 at N-1 followed by1 there. Thus
N+1 changes1,0,1,0; the last of these is forced by the1 at N. This makes the four exit
cells0000 at tau+3, independently of the next unknown value at N. In line D, the actual0
at N-1 makes the first exit cell1 at tau+1, which forces the last-but-one cell0 at tau+2.
In line B, the B-to-C guard makes N and N-1 both0 at tau+1; hence the first exit cell at
tau+2 is1. The last exit cell is then0 at tau+3. All other listed values use only already
listed exit cells. These calculations remain valid with arbitrary earlier cells compatible
with the stated guards.

For n=0 the actual five-bit prefix alternates10100 and11011 forever. Its terminal pair
is00 at even times and11 at odd times. Word234 first disagrees at time6; word170 agrees
through that time. This proves the exceptional f_0 separately. Combining the three arrival
cases gives the claimed formula, including n=1,2,3.

## Source comparison and scope

Record searched: PR48's complete source/evidence read GC2222; L1066's periodic-edges sections3–5;
GC2042's carried ring interface; record_find for the exact carrier, first-deviation and front
terms. Current kit `932cf8dde039b89b1dcbe9636867bb1b2057fef0`, its actual catalogs,
equivalents and Lean source, the portal and22 open PRs were searched through the complete
01:39:49Z index. Exact PR48 head865e77a5d11a/source4112e112 and linked5f245894 archive
are retained in the [carrying review](rule30-edge-clock-drop-review.md). Its discussion is
empty and the linked archive calls a first-deviation formula unproved.

`Rule30EtherThreeErosion`'s `front_step`/`wake_good` use a guarded finite-state front and a
potential for a different ether, spatial period12 and temporal period3. They are prior art
for the method; their hypotheses are not this carrier's. `Rule30ZeroBoundaryStripeFront`
has an autonomous window for a zero-boundary stripe and a different moving coordinate.
The period-eight carrier itself and its ring interpretation are already known here.

Primary Rasolonjanahary–Vasiev2020, [Formation of Morphogenetic Patterns in Cellular Automata](https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/),
was checked at its two-periodic Rule30 discussion and four-periodic classification. The former
treats formation of stripes in a finite chain; the latter asks which rules keep a preset
four-periodic row stationary. Neither displayed argument is this moving period-eight carrier
front. These comparisons are scoped, not a claim of exhaustive literature priority.

The result concerns the specified carrier family and an explicit guarded defect cycle.
It does not supply a finite-state law for the actual single-black-root00 transitions, prove
arbitrary-seed period monotonicity, or improve the centre-column period bound. Nothing is
submitted or promoted to two-party PROVED by this solo derivation.

## One frozen self-check

Source: `tests/probes/wolfram/carrier_invasion_check.py`, SHA256
`0da43b299382387fff4956fc61909f327e8970f73171d949ced61404dc48a33b`.
Unchanged runner SHA256 `c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`.
Prediction: the four choices of the two incoming bits all preserve the guarded A-B-C-D-A
cycle; the explicitly unguarded01/001 control fails its final101 guard. A literal Rule30
truth-table implementation and a separately written bitwise update agree. The five-tick
entrance and only the four fixed finite seeds n=0,1,2,3 give first failures6,6,9,13.
Those times are controls against retained data, not new predictions or a seed census.
Counterfactual: any mismatch stops with the complete local witness; no correction/rerun or
larger sample is automatically authorized by this freeze. Unexpected check: test the omitted
guard case, and require equality strictly before each stated first failure.

Record searched: the exact sources above. Value of the test: catch a phase/index error in the
hand tables, especially the exceptional entrance and arbitrary incoming bits. It does not
replace the unbounded induction or independent carrying review.

One single-thread Python child, nice10, no workers/GPU. Caps10 aggregate child CPU seconds,
30 wall seconds,128MiB sampled owned RSS,16MiB/file,128MiB/stage; tree tracking/max3 processes
including the time wrapper. Launch free+inactive>=4096MiB; running floor3072MiB; swap growth<=64MiB.
Use unchanged run_capped.py; its CPU limit suffices for this non-spawning single child, not
general process-tree aggregate CPU enforcement. Retain child/time/monitor/cleanup receipts
outside git. Measure actual load first; any monitor, pressure or resource failure stops this
stage with no automatic retry. No compiler, larger trajectory or density fit is included.

## GC2224: the frozen control passed once

Freeze commit `fc0c5383`, unchanged source0da43b29 and runnerc8c58b49. The one stage completed
02:08:16Z, exit0. All four assignments of the two relevant incoming bits preserve every
listed phase guard and the background above its front. The omitted-guard case gives001 as
predicted. The initial five-tick entrance and only the four finite seeds0,1,2,3 pass both
implementations, with equality at every tick before their failures6,6,9,13. No rerun, repair,
horizon increase or additional seed was used. This is a same-worker finite check.

Retained immutable packet: `cited/gc2224-carrier-invasion/manifest.json`, SHA256
`e65819830515c10c058fba737c73ba4865b05f53be0ae8515435e20a76dbbb1a`.
It binds9 payload files: the exact probe and runner, frozen proof/freeze, preflight, full result,
stdout, time receipt, launcher and review notes. All raw-body uploads and digests were verified.

Actual Intel preflight:5709MiB free+inactive, load averages2.50/2.23/2.19, no process above40%
CPU in the snapshot; pmset reported no recorded thermal/performance warning and limits100.
This is not a direct temperature measurement. Runner launch gate5700MiB, swap225.25MiB.
Child time receipt:0.05s wall,0.03s user+0.01s system, peak RSS14409728bytes; supervisor0.091s
CPU and0.54s wall. The probe finished before the first periodic sample, so the empty sample
list and zero sampled RSS/process maxima do not mean zero consumption or continuous pressure
verification. The runner's verified inherited CPU/file limits and launch gate were applied;
the final artifact count was10540bytes before the launcher receipt itself was finalized.
COMPLETED means its final owned/group check found no leftover requiring cleanup; cleanup is
null because no termination was needed. A separate post-run sandboxed ps read was denied;
this diagnostic is retained and did not cause a probe rerun or change the successful stage.

The hand result remains PROOF-SKETCH pending an independent carrying read. This completed
family requires no larger empirical confirmation. The next question is the guard's basin:
with the same phase-A leading defect and preceding0, can a finite older prefix avoid the101
guard indefinitely? First derive the guarded001 one-cycle condition and compare its moving-frame
constraint with known zero-boundary/clock results. No new stage is frozen for that question;
an exact reduction or counterexample is preferable to expanding a trajectory sample.

## GC2225: exact guard map and the remaining capture question

**PROOF-SKETCH, solo hand calculation; no new computation.** The front-speed question has
a stronger answer than the previous sufficient guard suggested. At a phase-A leading defect,
the six-depth/four-tick advance holds with completely arbitrary older cells. What may vary is
the trailing signature, whose first two bits obey a small exact map.

Translate a phase-A front to s=0, and write the actual cells at depths0,-1,-2,-3,-4 as
1,p,q,r,u. Above0 the background is00010001..., starting with the background0 at0.
All cells below-4 are arbitrary. After four ticks the front is6; let p',q' be its preceding
two actual bits, at5,4 respectively. Then

    p' = p AND (q OR r),
    q' = 1                         if p=1,
    q' = q OR NOT(r OR u)           if p=0.

Here is the full local derivation. At the first tick, actual cells-1,0,1,2 are b,a,1,1, where

    a = NOT(p OR q), b = p XOR(q OR r), d = q XOR(r OR u).

The value d is the first-tick cell-2. At the second tick, cells0,1,2 are e,c,0, where

    c = NOT(a OR b), e = a XOR(b OR d).

At the third tick, cells2,3,4 are c OR e,c,0. At the fourth, cells4,5,6 are c OR e,c,1.
Thus p'=c and q'=c OR e. If p=0, c=0, and e is1 when q=1 and NOT(r OR u) when q=0.
If p=1, c=q OR r and b=NOT c, so c OR e=1. This proves the formulas with no unlisted
incoming bit. All cells above the successive fronts2,2,4,6 stay background. The first-tick
cell1 is always1, which is precisely what protects the second tick's stall. Therefore the
same phase-A leading defect reappears at6, regardless of p,q,r,u, and the speed law iterates.

This corrects the earlier inference that the omitted101 guard challenged the front-position
law. It challenged only reproduction of101. GC2223's stronger signature and all three exit
calculations remain valid in their stated guarded scope.

Reading the three-cell signature as q,p,1 gives:

| Signature at A | Signature at the next A, four ticks later |
|---|---|
| 101 | 101, for every older continuation |
| 111 | 111, for every older continuation |
| 011 | 101 if r=0; 111 if r=1 |
| 001 | 101 if r=u=0; otherwise001 |

Thus there are two closed signature classes. A finite older prefix ending111 is an immediate
counterexample to an unrestricted claim that every phase-A front eventually has signature101.
The earlier queued question explicitly assumed p=0; that narrower capture question is still
open. In that class p remains0 and q is an absorbing bit: once1, it stays1. Crucially, no
capture theorem is needed for the front-speed result itself.

### Two-cycle avoidance and a finite twelve-tick control by hand

Assume p=q=0 initially and write the next older bits as r,u,v,w at depths-3,-4,-5,-6.
The signature is still001 after two four-tick cycles if and only if

    u=1 AND (r=0 OR v=1 OR w=1).

To see this, survival of the first cycle requires r OR u=1. Under that condition the next
older pair r',u', at depths3,2 behind the new front6, is

    r' = NOT r,
    u' = NOT r OR f,
    f = NOT((r XOR(u OR v)) OR (u XOR(v OR w))).

These follow from the same four layers: the second-tick cells-1,-2 are NOT r,f; the next
cells1,0 are NOT r,NOT r OR f, and hence the fourth-tick cells3,2 have the displayed values.
If r=0, first survival already forces u=1 and r'=1 forces second survival. If r=1,u=0,
the two terms inside f's negation have OR1, so f=0 and second survival fails. If r=u=1,
f=v OR w; second survival holds exactly when v OR w=1. This proves the criterion.

Consequently indefinite001 avoidance would force, at every phase-A sample,

    q_h=p_h=0, u_h=1, r_(h+1)=NOT r_h,
    and v_h OR w_h=1 whenever r_h=1.

These are consequences of actual evolution, not freely selectable inputs. No independence,
frequency or periodicity of the deeper row follows from them.

For a cheap finite countercontrol to capture within eight ticks, choose phase A as the starting
clock phase, set actual cells-4 and0 to1, all other cells at depths<=0 to0, and use the carrier
above0. The older prefix has finite support; the entire row has an infinite periodic tail.
After four ticks the actual cells0..6 are0011001, by the literal recurrence. Relative to the
new front6 this gives p=q=0 and (r,u,v,w)=(1,1,0,0). The two-cycle criterion applied there
gives q=1 after two more cycles, while its one-cycle condition gives q=0 after one. Thus the
signatures at ticks0,4,8 are001, and capture as101 is exactly at tick12
relative to this start. This is a hand example, not a newly measured trajectory or a claim
of unbounded capture times. Translation by four makes its rightmost black cell depth0;
the chosen carrier phase is an allowed initial phase, not a claimed earlier ancestry.

### Why the familiar clock results do not close the remaining case

Let y_h(k)=x_(s_h-k)(t_h), s_h=s_0+6h and t_h=t_0+4h. With

    (D y)(k) = y(k) XOR(y(k+1) OR y(k+2)),

the exact sampled operator is (G y)(k)=(D^4 y)(k-6). Its dependency interval is k-6..k+2.
The negative k values are the prescribed periodic carrier, and finite support on the older
side means y(k)=0 for all sufficiently large positive k. This support generally grows under
G; the moving boundary does not turn the whole state into a finite periodic orbit.

The unresolved assertion is now precise: does every such finite older state with p=q=0
eventually violate the displayed sampled masking conditions, and hence acquire q=1?
Neither a proof nor a finite-prefix perpetual-survival counterexample has been obtained.
Do not replace this assertion with a full-state return or independently chosen older bits.

Source comparison uses the current kit932cf8dd and the complete01:39:49Z index,22 open PRs.
`Rule30ControlledResponse.diagonal` is D, not G; `Rule30ZeroBoundary.zrow_succ` is a one-tick
clamped physical wall, not this four-tick/six-depth sampling. `Rule30ClockMask.no_constant_OR_at_onset`
requires actual temporal period/antiperiod hypotheses for adjacent D columns, absent here.
The actual headline of portal0ef9c8 additionally requires D^32(x)=x for the full finite state;
it cannot be invoked from the local sampled gate. Portal4d375d's front-clock core uses
(x<<2) XOR((x<<1) OR x), a different map. These are scoped definition/headline comparisons,
not new complete carrying reviews of those portal sources.

`Rule30Equivalents.PeriodicPoints.Recurs`/`recurs_add_factorial` require recurrence of the entire
configuration, not a repeating front strip. `Rule30Equivalents.Lines` gives almost-everywhere
laws for random configurations, not the present deterministic carrier. Primary
[Kopra, arXiv:2202.13809](https://arxiv.org/pdf/2202.13809), Definition2.4 and Theorem3.5,
requires a left-zero number-like start for the original rapidly left-expansive rule and a
vertical trace. The present physical start has an infinite carrier on the left and zeros
on the right, and the sample follows a different ray. No transfer hypothesis has been proved.

Read-source SHA256: PeriodicPoints `dd7e300baf996d52dabe789ce8537f1a5fb03c59504c233f37544bbd17843f57`;
ClockMask `b0ec0d01e18e88c167ca2762b4cd50714bd67f31982e656a0a07d2cb2514a6b1`;
portal4d375d `d9a4bab0aad7a42f641e8f65c70af85aebc43274db621a8656ddd4a510a7dd3a`;
portal0ef9c8 `cd2425f35ca59e204a4b93fe6ec9c72603052209fb9f1997b4af703e47c32e0f`.

Park indefinite001 capture at this explicit G-survival problem. Reopen only with a specific
law controlling the actual successive older pairs, a justified conjugacy to a known boundary
problem, or a rigorously specified perpetual-survival construction. More local gates or a longer
seed sample alone do not supply that step. Change to the relevant but independent PR47
synchronizing-carrier source: its prescribed inverse histories may teach something different,
and its carrying proof has not yet been fully read in this record. No experiment or posting
is frozen; Local and Cloud remain offline.
