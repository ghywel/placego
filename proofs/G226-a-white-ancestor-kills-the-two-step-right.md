# a white ancestor kills the two-step right source

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT226. a white ancestor kills the
two-step right source (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A white square prevents a particular neighbouring black pair two steps later.

**What it says.** In Rule210, a white square forces the pair two places to its right, two ticks later, to contain at least one white square. Under the alternating wall this removes later even-time sources in column2.

**Why it matters.** A pattern can obey forward equations yet have no allowed past. This checks that missing obligation and removes a previously apparent source possibility.

**An everyday picture.** A ticket may let someone enter the departure gate, but the required connection never arrived. Checking the journey before the gate can rule out what the gate alone permits.

## The formal statement and proof

**Where:** RULE30-GPT.md GC449 at31339ff; Local L264 in11157ee verifies the universal three-case proof, black-ancestor counterexample and clock consequences. Source statement and proof copied verbatim below. This adds actual predecessor constraints to G225's forward equations, superseding the apparent column2 hole without claiming full-clock exclusion.

**Initial endpoint.** Under an empty initial left row and full0101 wall, G26 has s_0=1,s_1=0. G61 forces d_0=0 and c_0=1. Column2's next update is x_2(2)=d_0 XOR ((1-c_0)*x_1(3))=0. Thus the early source V_2(2) vanishes, independently of the farther right tail. Direct scalar evolution of32 positive five-bit seeds has12 centre prefixes0101, all with x_2(2)=0. No continuation beyond that prefix was inferred.

**Stronger local claim.** In any Rule210 orbit, at any time t and site j,

`x_t(j)=0 implies x_(t+2)(j+2)*x_(t+2)(j+3)=0`.

There is no wall, left-support or eventual-periodicity hypothesis for this implication.

**Proof.** Translate j,t to0. Let the six input bits be (0,s,b,q,h,z). The four relevant next-row bits are

`d=(1-s)*b`, `c=s XOR ((1-b)*q)`, `r=b XOR ((1-q)*h)`, `v=q XOR ((1-h)*z)`.

The next pair is B=d XOR ((1-c)*r), Q=c XOR ((1-r)*v). If c=1, then d=0: d=1 would require s=0,b=1, which gives c=0. Hence B=0. If c=0 and r=1, then Q=0. In the remaining case c=r=0, B=d and Q=v. For B=1, d=1 forces s=0,b=1. Then r=0 forces q=0,h=1, and therefore v=0. Thus B*Q=0 in every case. These cases prove the implication for unrestricted farther bits.

**Clock consequence.** In every full0101 wall orbit, x_(2n)(0)=0. Applying the local claim at j=0,t=2n eliminates every column2 source V_(2n+2)(2). Consequently its even-time activity can occur only at time0. Odd source times on column2 are invisible to every odd centre target by G215's parity condition. The complete column2 contribution at odd target T is therefore K_(T-1)(2)*V_0(2). G224 makes its coefficient1 exactly at T=2^h-1, h>=2, and0 otherwise. In particular at T=2^K+1, K>=2, the column2 contribution is0. The early and late endpoints of G225 both vanish once an actual predecessor update is required.

Together with G216, every selected source for these dyadic-plus-one targets has i>=3. Under the finite-support condition 2^K>R+1, the homogeneous centre term is0, so an odd number of selected active sources must occur at i>=3. This still leaves a growing cone; it is not a finite-clock exclusion. The i>=3 statement applies to these targets, not to all odd times.

**Duplicate guard for G226:** actual nearest G225,G224,G215 read in full. G225 only requires an effective switch and checks forward patches; G224 specifies coefficient times; G215 gives the whole cone parity. This entry adds a universal two-step predecessor obstruction and eliminates later even column2 products.

**Scope:** the local implication is universal for Rule210. The clock specialization needs full0101; source time0 is retained. Dyadic-plus-one targets alone require selected sites i>=3, and the farther cone is uncontrolled.
