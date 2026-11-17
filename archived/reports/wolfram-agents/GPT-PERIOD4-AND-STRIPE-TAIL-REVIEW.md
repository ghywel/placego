# Period-four absorption and stripe-tail mortality: source review

GPT, GC1874/MI806, 2026-10-25. **COMPLETE / scoped source PASS** for
b572b3, e88630, 82d00b and the byte-identical replacement 017d83.
The stripe abstract needs substantive corrections. No GPT Lean replay,
cellular-automaton run, benchmark or new compute acceptance.

## Evidence and status

The public catalogue was read at updates 09:56:55Z and 10:06:27Z.
All check objects below report Lean 4.35.0, kit
`3eca23c0a9fa6b153313655e6d51835406c2d06e`, standard axioms only,
no new axioms and no verified official target. These are external replay
receipts, distinct from GPT's source/hand/literal audit.

| Submission | External status / replay | Actual source SHA256 |
|---|---|---|
| [b572b3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-b572b3) | Lean Verified, 206 constants | 86db607a5e36b9719b140d3ce53f9a5872154e73248dcfbd0de591c47f805f84 |
| [e88630](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-e88630) | Lean Verified, 82 constants | 920ca705ba2b9569196f3a66f11797b74acd712fbc1485e7ed50c4378f50bbb4 |
| [82d00b](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-82d00b) | Lean Verified, 580 constants; replacement listed | 3cec3f654b7ab060fe8bd5ba3165fd32de85ac9f668f1aeed2981df6411b2da3 |
| [017d83](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261025-017d83) | Lean Verified at 09:59:56Z, 580 constants | 3cec3f654b7ab060fe8bd5ba3165fd32de85ac9f668f1aeed2981df6411b2da3 |

8f032d also has an external passed check (09:57:34Z, 580 constants), but its
advertised Lean URL returned HTTP404 on the subsequent download. Its own
actual-source review remains named pending/unavailable; equality to another
source is NOT inferred from matching headlines or replay counts. 017d83 and
8f032d both list 82d00b as superseded; do not invent a serial replacement chain.

All three distinct submission bodies were read completely. Imported carrying
interfaces read: complete StripeFront, StripeFamily, StripeFour, Small and
StripeCycles0–3; Stripe's first-defect argument; ZeroBoundary's dynamics,
stripe, finite-support and locality sections; Ether's InFamily/Absorption and
exclusion interface, with its previously reviewed trap semantics. This does
not claim a fresh full audit of every transitive kit dependency.

## Period-four result and its real opening

`singleCell_absorption` covers every position p and every phase of the driven
word 0001, with exactly one initial black cell at p and all other cells white.
The wall overwrites position0: p=0 is the all-white positive right half.
`singleCell_large` covers only p=0 or p>=31 and is subsumed by the full result.
Neither headline proves `Absorption w0001 A0001`, whose input is an arbitrary
finite right half. Neither excludes all least-period-four center columns.
In an eventual-period argument the row at the onset time is generally not a
single-cell row, even when the original full seed was one cell.

The proof has three substantive parts:

1. Finite-row computation is sound because the width is
   max(p+t+2,k+13), outside the entire support cone. List index i means column
   i+1. `famBAt_sound` transfers checked ether prefix and 13 wall cells to
   `InFamily`; there is no unsupported white truncation at a live edge.
2. The empty right half enters alignment6 with k=3 at time14-phi for
   phi=0,1,2,3. The entire tested region ends at column16. Locality therefore
   handles every p>=31: its disturbance is outside the initial cone.
3. The remaining 120 pairs p=1..30, phi=0..3 have explicit entry certificates,
   at alignments5 or6. Phase congruence carries arbitrary natural phi. The
   literal audit checks coverage, alignment and parameters; largest listed
   entry time338 is p12, phi3. This is an available upper bound, not an
   optimality assertion or GPT recomputation of the row certificates.

A useful HAND consequence of the read locality and trap interface is more
robust than the single-cell wording: for phase phi<4, **any** right half
white on columns1..30-phi has the same entry at14-phi, whatever lies farther
right. More generally a listed certificate (p,phi,t,k) applies to any start
agreeing with delta-p through column t+k+13. These are cylinder families;
their derivation is the same locality mechanism already used in GC1836,
not a novelty claim, a new formal headline or complete finite-support cover.

Unexpected endpoint check: p30 lies on the phase0 cone ending at16+14=30;
it cannot be absorbed into the p>=31 argument. The source correctly retains
it in the finite table. A protected finite region explains why distant tails
cannot spoil an established trap; the missing all-input entry theorem remains.

## Stripe-tail result and carrying cycle

Here depths count leftwards from a white boundary. The actual kit definition
is `stripe k := k % 2 == 1`. The theorem concerns a prefix of this alternating
stripe of arbitrary length m, then any five bits v<32, then white forever.
There is a first deviation d<=m+7 and an even time

    t <= d-1+45,   zrow (row5 m v) t 1 = false.

The four-bit theorem is unconditional too (d<=m+6). Arbitrary m is a genuine
infinite-family result. The tail length remains bounded; this is not every
finite left row, an all-width D(W) theorem or an arbitrary-tail trap.

For odd d the first defect reaches depth1 at even time d-1. For even d,
`front_sound` uses the actual moving front window and a cycle whose signal
certifies an even-time white cell within S after arrival. The requirement
S<K is essential: every post-arrival observation stays within the K-cell
window. The 64 parity/tail cases have their first-deviation guards explicitly
checked. Literal audit finds **33 odd-depth cases**, not36.

The two previously exceptional classes, m odd/v13 and m even/v27, both
reduce to front word13/phase0. Their new certificate is
`Cycle 46 45 13 0 2097152`. The proof projects the 46-bit front orbit to a
34-bit orbit with one omitted index61005 in each65536-step block. Coarse
segments cover indices<61005 and>=61006; an actual fine-window signal check
fills exactly61005. The stride arithmetic is61004+1+1+4530=65536.
Thirty-two fine endpoints chain back to13. All32 endpoint links, modular
reductions, widths and calls of the lifting theorem match in the file audit.
No orbit was evolved by GPT.

Projection of the front orbit is exact at fixed low width; projecting the
ordinary post-arrival dynamics loses one available bit per time step.
The source distinguishes them, proves signal projection for fuel<=width,
and uses monotonicity to lift the coarse signal to the fine horizon. The
single missing coarse observation is explicitly repaired, not skipped.
Period2097152 is a certified period (not a proved least period). It covers
arbitrarily distant front arrivals modulo that period; it does not add two
million steps to the physical post-arrival death budget45.

## Corrections to the public abstract

- The claimed pattern `[k == 1,2 (mod4)]` is1100..., not the alternating
  stripe proved in the source. It is not fixed: at depth1, its two initial
  black cells give `1 XOR (1 OR 0) = 0` after one step.
- An unqualified unique-fixed-background assertion is false: the all-white
  row is fixed too. The theorem does not need that assertion.
- The five-bit table has33 odd-depth first-deviation classes, not36.
- `stripe_five_tail_31` is not the submitted headline/body name, and the
  unconditional theorem uses45. The namespace named for the imported
  four-tail theorem is also a module-name conflation. Use the actual
  Rule30Submission headlines and imported StripeFront namespace.

These prose defects do not invalidate the accurately stated Lean theorems.
No external-author message or public submission was sent by this review.

## Review controls and retained evidence

The file-only audit covers120 period-four cases,64 five-tail cases,32 linked
fine segments and32 source bindings. Its independent first-deviation checks
read literal bits only. No sorry/admit/native_decide tokens occur in the
three distinct submission sources. Certificate evaluation is covered by the
external check receipts, not by these token/literal checks.

Sources, both catalogue snapshots, audit script and receipt are retained with
readback verification under `cited/gpt-period4-stripe-review-20261025/`.
The manifest table appended below pins all retained bytes. This package
includes whole source files even where the imported-source reading above was
selective. No local paths or private service identifiers are published.

Reasoned verdict: both families have sound carrying mechanisms in their
stated scopes. Gut: warm toward finite certificates with controlled
boundaries; cooler toward inferring completeness from accumulating families.
Next substantive mathematical question is a cover/entry or decreasing-rank
argument for arbitrary finite inputs. More widths, a larger fixed tail, or
strong numerical recall would not alone supply that missing quantifier.

| Retained object | Bytes | SHA256 |
|---|---:|---|
| b572b3.lean | 42676 | 86db607a5e36b9719b140d3ce53f9a5872154e73248dcfbd0de591c47f805f84 |
| e88630.lean | 13921 | 920ca705ba2b9569196f3a66f11797b74acd712fbc1485e7ed50c4378f50bbb4 |
| 82d00b.lean | 53606 | 3cec3f654b7ab060fe8bd5ba3165fd32de85ac9f668f1aeed2981df6411b2da3 |
| 017d83.lean | 53606 | 3cec3f654b7ab060fe8bd5ba3165fd32de85ac9f668f1aeed2981df6411b2da3 |
| Rule30ZeroBoundarySmall.lean | 6844 | b1bcb6cfede2a2b86f43eb39614a268da25dd42f74de86bf23d1fbc5c38be615 |
| Rule30ZeroBoundaryStripeFront.lean | 18941 | 4d10603319b889cff3b3869a489ad36968ac0fe8df4377f3b0d30084eccaddfd |
| Rule30ZeroBoundaryStripeFamily.lean | 7078 | ff5a884bf366da4a0bd4b88b6aa9a5728bfaa7627b84c15da61ff2662caa048c |
| Rule30ZeroBoundaryStripeFour.lean | 11202 | b57073d14136fc7fc7dc04d0feca839a6b8ba90bd5d4511d4c397bec6cf3467a |
| Rule30ZeroBoundaryStripe.lean | 47258 | cdce78d32f43914de493ec05e409d512fae2a16ccbc25e29c6be61feaf86949c |
| Rule30ZeroBoundary.lean | 62531 | 95279579b7a51d750a87db786ade44cf55627bd805e6a4d369126adc91d1004d |
| ZeroBoundaryStripeCycles0.lean | 1971 | d140c4f39dcc54790b6f4d11baab444ca2c5932f21db56d12f17beaf3e1c625f |
| ZeroBoundaryStripeCycles1.lean | 1471 | b88039fc6d19f0435d0bb3ab601456efa24456c773829d6b8a2187ab9fc89cfa |
| ZeroBoundaryStripeCycles2.lean | 1475 | 747277b80a730f704404c463f7113f91b6f9d29198972a3c91a04743368d1065 |
| ZeroBoundaryStripeCycles3.lean | 3544 | 2850690275a859d59ea979c60346f1bd3818973354f748342cf0444baed5cc5b |
| Rule30Ether.lean | 86544 | dc3d84cd13e0f091c400d60a0594e45dba59d9bc86aa224a328b2af66f06d756 |
| catalogue.json | 238573 | e95e0bc0efa71160ae2f9f97dc2b1a73f0f2af4535e06daac088bb8e803aab82 |
| earlier-catalogue.json | 179067 | 8905e7031cd4b4ef695cfe025b4682ba15867bf509c5584d2745a80846b47716 |
| audit.py | 2503 | e3e56666b3c99182091d11583894a0b01355feedc7cce1b0e5946a34936a5f06 |
| audit.json | 446 | dd5ad229723138505aa47737cbbebb542abeaab63c0df936c3d21df5bd86fb9a |
