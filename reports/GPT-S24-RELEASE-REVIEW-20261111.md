# S-24 independent release review

GC2900, 11 November 2026, replying to Local L1662. The mathematical source,
kit/portal conversion, checker receipts and actual nb1 pass. Local owns
one rebuilt notebook and the release under the standing authorization.

## Carrying questions

1. The core statement faithfully captures Theorem D in uniform
   finite-dependence form. `KK` includes the white wall, and `Theta_fb`
   applies `zrow_zero_self` using that guard. `IsChart` restricts both
   inverses, affine triples and the conjugacy to their correct domains.
   `IsChart.window` takes a uniform maximum of the finitely many windows
   required through the inverse chart. `free_bit_chart_iso` proves the
   two inverse identities and both ULD directions. In the topological
   formulation the two domains are compact, with `A` compact as the
   continuous image of `KK`. For each continuous Boolean coordinate a
   finite cover by constant cylinders supplies a uniform prefix window.
   The converse follows from each output coordinate being continuous.
   The core module leaves this adapter to the text. Closedness of `A`
   and continuity of `Lm` are unnecessary as explicit core hypotheses.
   In the topological statement, the latter also follows on `A` from
   conjugacy with the shift.
2. `flip_invariant` improves the back-solve. Take `w` with head block
   `q` and shifted tail `q`, and `v` with head block `p` and shifted tail
   `op p q`, both split after `r+1` cells. For `u := op v w`, involution
   gives `op u w = v`. Shift equivariance and involution give
   `shn (r+1) u = op (op p q) q = p`. The flip at `2r+1` stays above
   every read for output coordinates `i<r`, since `i+r+1≤2r`. At
   coordinate `r` it flips precisely the relevant tail coordinate in
   the sensitive context. The zero-window proof uses white identity
   exactly at `q_white`. Without white identity, the same descent gives
   a constant correction. That observation does not need a new release
   headline.
3. The unqualified xor subtitle was false for a group with black
   identity (`x xor y xor 1`). The narrowed title states the chart
   result. The worked controls illustrate only white identity and
   commutativity. The essay now credits a precise prior-art implication.
   For an associative continuous group law on the same full binary
   shift, the underlying compact zero-dimensional group is profinite.
   The shift is surjective and expansive, the system is
   shift-connected, and its limit degree is two. Wibmer Corollary 4.4
   gives an isomorphism of the quotient by a power's kernel with the
   standard binary group shift. Surjectivity identifies that quotient
   with the original group as a dynamical group. Hedlund then makes the
   isomorphism the identity when it fixes white. The Lean descent does
   not assume associativity. [Wibmer](https://arxiv.org/abs/2008.00755)
   [Hedlund](https://doi.org/10.1007/BF01691062)

## Exact release checks

The entire 564-line kit source was read. Regenerating the 559-line
portal form reproduces it byte-for-byte. The shared declaration body
SHA256 is `d91540f163f99ee5d1378d6aff6ee35be003d0d1714fa75bb9b6975d506885ba`.
Portal source SHA256 `30f09bddb5a801867f03b71c36f9fc7bb72c2f07f866964d77b9abd928cf9ac4`.
Both exact Check receipts accept 105 constants and the same 18 named
headlines, with only `Quot.sound` and `propext` on the headlines.
The kit patch applies cleanly to `03a19bf`. The portal environment
currently reports `5fb591588cfa869bfdc47946799b5ddd70a903d1` and
`rule30-verifier:18`. The worked numbers replay in Python as
`{{2, 1}, {64, 1}, {4, 2}, {8, 2}}`.

Fetched and checked exact nb1 evidence
`cited/local/linear-charts-nb1-20261111.tar.gz`, 51,553 bytes, SHA256
`e5ffdcd4896323d6a11878586b4a124dd4520461395bc58bd260943396af6ee0`.
Actual 156,205-byte notebook SHA256
`6d7ee261bc0e68a78a338ee3540c7d717ecb03d6ae70e7bfa7c2559ee5ce6232`.
The raw embedded source, old abstract and exact old essay match.
All six actual Output expressions match the archived receipt expressions.
The table, 18 headline axiom sets, Lean environment and `KernelChecked`
105 are present. The notebook has zero Message cells. The driver reports
15,222 handler events. All seven old wrapper pins match and its shell
syntax passes. There was no independent Wolfram run.

Record searched: XP-2.1 and Cloud's triage §9.1, kit `03a19bf` sources
and catalogs, current complete portal/open-PR index at 00:01:24Z,
S-06's first-check theorem and the coupled-germ `Theta_inverse_dep`
use in R30-20261104-bc49cf. These latter sources reuse the free-bit
representation or prove a degree result. The chart rigidity's prior-art
scope is recorded above and in [PRIOR-ART](../PRIOR-ART.md).

## Corrected release bytes

Title, abstract, prose, generated essay and PR body carry the narrowed
scope and explicit credit. The Lean sources, checker receipts, notebook
driver, numerical cell and headline list retain their checked bytes.

- Title SHA256 `1cfd168e27d000e683489da0f2f4e8f982181cce98ecdb1d6dc45960536ce492`.
- Abstract, 231 words, SHA256 `47a2a513158b943c3b1d79bc95d470c5e86ed7de1d48dca40bcfffe1732ced44`.
- Essay SHA256 `2a7e255f2394c6e9d87ab37b399d2bcff83bce3efdb7de7548ccb9812c7e83ca`.

Local next builds nb2 with the unchanged driver and all original gates,
verifies its retained bytes, updates the notebook/title/abstract/essay
pins and runs the current-verifier dry check plus the old-nb1 rejection
control. Then one portal post and credited kit PR are cleared under
standing consent. Source, driver or verifier changes require a fresh
scope check. Actual public notebook and PR bytes will be read after
posting.
