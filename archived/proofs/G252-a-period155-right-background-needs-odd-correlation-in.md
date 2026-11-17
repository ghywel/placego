# A period155 right background needs odd correlation in a period310 all-L bridge

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT252. A period155 right background
needs odd correlation in a period310 all-L bridge (second-read by Local, 2026-10-09)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A hypothetical all-L row that turns back on itself every 310 steps but ends on the right in a pattern repeating every 155 would need a particular odd correlation somewhere between the two.

**What it says.** Far left such a row copies the 155-cell ring, whose columns hold an even number of black cells over 310 steps. Far right its columns repeat every 155 steps, and the last column that does not must hold exactly 155 blacks, an odd number. An exact parity rule links neighbouring columns, so somewhere between the two ends a pair of neighbouring columns must overlap in an odd number of black cells. Second-read by Local.

**Why it matters.** It pins down what an exclusion of this case would have to forbid. It does not forbid it, and the same counting says nothing at period 620 or beyond.

**An everyday picture.** If a row of switches starts with an even count and ends with an odd one, some neighbouring pair along the way must be where the parity changed.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-09 (Local L402).** Second reader: Local, chat L402. Waiting-room heading: "G252. A period155 right background needs odd correlation in a period310 all-L bridge (GPT, 2026-10-09; waiting room)". The text below is unchanged, so its *Status:* line is historical.

*Status:* hand reading pending. *Where:* RULE30-GPT.md GC769. *Provenance:* conditional application of GC759/760/762; reference populations received. Nearest G249,17,18 read in full: G249 supplies the running-XOR complement mechanism,17 physical-column left periodicity,18 Rule210 parity. None states this scoped bridge obligation. Proof copied verbatim below.

**Bounded critical-tail audit after GC762.** Expect an odd-period right background in a period310 all-L lasso to require an odd-black intermediate column, hence a nonzero adjacent-product parity. Counterfactual: the same odd-black conclusion automatically holds at period620. Independent control uses the half-period complement of a running XOR; unexpected check retains the even half-period cancellation. No profile graph, ring census or dynamics run. GC759/760/762 supply the premises; the mechanism is their xor-integration/parity identity, not a new invariant.

Assume a non-ring G-period310 all-L representative with a spatially periodic right background of least G-time period155. Its profiles V_i are310-periodic. Far left they match the aligned reference ring, whose adjacent joint period is310 and whose columns have156 black samples per310 ticks (received ring counts). Far right every individual profile period divides155.

There is therefore a rightmost column k whose profile period does not divide155. Existence follows already from a far-left pair's joint period310; rightmost existence follows from the odd-period tail. At k+1 and k+2 the periods divide155, so the driver H=V_(k+1) OR V_(k+2) is155-periodic. The equation Delta V_k=H implies that

    V_k(t+155) xor V_k(t)

is independent of t: its successive difference is H(t+155) xor H(t)=0. It cannot be zero, since k was chosen not155-periodic. Thus V_k complements after155 ticks and has exactly155 black samples over310 ticks, an odd count. This does not require its least period to be310; it may be2d for a divisor d of155.

Let a_i be the black parity over310 ticks and c_i the adjacent-product parity, as in GC762. Far-left reference columns have a_i=0, while a_k=1. Telescoping the exact identity c_i=a_i xor a_(i+1) from any reference column l through k-1 gives

    XOR_(i=l..k-1) c_i = 1.

Consequently at least one intervening adjacent pair has odd correlation. The candidate must genuinely use the correlation term that defeated the naive conservation route. This is a necessary bridge obligation, not a proof that such a correlation is forbidden, or that an odd-period background is possible.

**Unexpected period620 guard.** At a rightmost column not310-periodic in a620-periodic diagram with a155-periodic tail, the driver has period dividing310, and complementing after310 gives310 black samples over620 ticks, even. The analogous odd-black inference disappears. If all columns already divide310, summing any310-periodic column twice over620 also makes its black parity even. Thus this target is specific to a310-period audit; it cannot exclude higher critical periods by repeating a longer temporal sum. No period620 candidate or background is constructed.

**Disposition.** To exclude the q=155 background at p=310 by parity, one needs an all-L-specific prohibition of the identified odd-correlation bridge. GC762 shows that unrestricted Rule30 periodicity supplies no such prohibition. The q=310 backgrounds and larger p remain untouched; critical uniqueness and Q6 stay open. Independent hand reading requested, no computation requested. Scratch deferred without login retry; break room closed.

*Final filing gate.* Nearest G249,G164,17 read in full; refreshed G251 also read in full. G164 concerns interval reset debt and G251 settled-white L tracks, not this cyclic black-parity bridge. Duplicate controls pass.

*Independent reading (Local L402, 2026-10-09).* Near-entry gate run (`--near W252`: G249, G164, G251; none restated). Verified by hand: G's column equation is the running XOR V_i(t+1) xor V_i(t) = V_(i+1)(t) or V_(i+2)(t); with a driver of period dividing 155, D(t) = V_k(t+155) xor V_k(t) has zero successive difference, so it is constant, and nonzero because k is not 155-periodic, giving exactly 155 blacks; cyclic summation of the same equation with a or b = a + b + ab mod 2 gives c_i = a_i xor a_(i+1); the reference ring's 310-tick G-columns have 156 blacks (154 whites, counted literally in L391), so telescoping from an even column to the odd one forces an odd adjacent product. The 620 guard holds: a 310-half complement gives 310 blacks, and a 310-periodic column summed twice is even.
