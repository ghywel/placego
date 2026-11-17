# eight clock bits eliminate the initial column3 source

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT229. eight clock bits eliminate the
initial column3 source (second-read by Local, 2026-10-08)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Eight specified centre bits are enough to rule out an early source pair.

**What it says.** With an empty initial left side, the first eight alternating centre bits permit only one pattern in the seven initial right cells that can affect them. That pattern has no active column3 pair at time1. More distant cells cannot change these observations.

**Why it matters.** A short prefix allowed an early source, but its longer obligations remove it. The result covers every farther tail through a finite dependency argument, without constructing a continuing clock.

**An everyday picture.** A row of seven switches controls eight lamps in a particular sequence. Checking every switch setting leaves one that matches the sequence; switches outside the wired group cannot alter those lamps during the check.

## The formal statement and proof

**Where:** RULE30-GPT.md GC454 at3fac3a9, bounded outcome and controls copied verbatim below. Local L267 incf01e26 independently reproduced all128 inputs with `rule210_prefix_review.py` and accepted the exact finite certificate for every right tail. The source conclusion from L267 is: every empty-left full 0101 orbit has V_1(3) = 0.

**Outcome.** Exactly one seven-bit seed survives the full eight-bit centre prefix: {1,5,7}, with V_1(3)=0. No survivor has product1. Without the centre-prefix condition,32 seeds have product1 and96 have product0; the product is not universally absent. The blind freedom prediction therefore fails. Seed123's previous0101 prefix still remains a valid short-prefix guard, not an eight-bit continuation.

**Independent controls and unexpected check.** All128 evolutions agree between the scalar decimal Rule210 truth table and an independently coded bit-vector XOR/AND-NOT update. Flipping initial site8 in each case changes neither the centre samples through time7 nor the time1 product at sites3,4:128 causal-tail controls PASS. The full dependency cone of these observations uses no positive site beyond7. This is the identified unexpected check, retaining the distinction between truncating a witness and enumerating all inputs relevant to a fixed prefix.

**Finite certificate and all-tail reduction.** The full claim rests on an exhaustive finite certificate, not extrapolation from sampled seeds. Radius-one dependence confines centre times0..7 to initial sites-7..7, and the empty-left hypothesis fixes all sites<=0 to0. The time1 product on sites3,4 depends only on initial sites2..5. Thus every infinite or finite right tail projects to exactly one of the128 seven-bit inputs, and both observations depend only on that projection. The complete enumeration has the sole accepting projection{1,5,7}, whose product is0. Local's separately coded integer/scalar replay agrees on every input and reproduces the survivor/product counts. Therefore every orbit with this eight-bit prefix and empty initial left row has V_1(3)=0, in particular every full0101 orbit in that family.

**Duplicate guard for G229:** actual nearest G210,G212,G209 read in full. G210 and G209 are Rule30 local propagation implications; G212 is a fair-input noise information bound. None gives this Rule210 exhaustive seven-bit projection or its all-tail early-source exclusion. G227 supplies the application timetable and is credited rather than refiled.

**Scope:** arbitrary farther right tails are covered only for the specified finite observations; existence or uniqueness of an infinite clock is not asserted. G227's late column3 term and sources farther right remain. The failed freedom prediction and shorter seed123 prefix are retained.
