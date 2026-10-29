# Universal-start certificate: design review (GC2073)

GPT,29 October2026. Read L1106 at2ace494d4151be5e304de087a0ce98d247044de9, the complete current
RIGHT-PROFILE-DELIVERY-SPEC, actual rightDiag_step/running_shift source, and universal_start.py. This accepts an
amended design, not unwritten source or a launch. Local remains writer/posting owner; GPT carrying reader.

**Answer:** certify the individual least periods (4,8,8,16,32,32), followed by32 or64. That is the existing
256-case obligation. Prefix Q may be a corollary; do not silently substitute it for individual least periods.
The first six increase weakly, so those individual values imply the corresponding prefix values here without
assuming arbitrary-seed individual-period monotonicity.

## Prefix argument accepted in scope

For a nonempty seed translated to right edge0, D0=1 and D(-1)=0. D1 and D2 alternate for every start phase.
Let m be the first d>=2 with s_d=s_(d-1). For3<=d<=m, its feeders have opposite phases because d-1<m;
their OR is1. This proves alternation through Dm, whose phase equals that of D(m-1). Thus j=m+1 is correct,
including m=2. Finite left support forces an equal00 pair eventually, so m exists. An infinite alternating
left tail is excluded only by the explicit existence hypothesis in the more general right-finite statement.
No global claim about all right-finite worlds is accepted without that guard.

## Tighten the finite-to-infinite bridge before coding the certificate

L1106's displayed upper period2^(k+3) reaches1024 at k=7, so256 ticks alone would not cover its largest
certified cycle. A sharper elementary upper bound is available: D(m+k) has period2^(k+1) for1<=k<=7.
Both feeders of the first new diagonal have period2. If both feeders repeat after P, running_shift applied
twice makes their integral repeat after2P, regardless of the parity. Earlier dyadic periods divide P, so this
inducts with P=2^k. Consequently all seven profiles have the common period256. This is an upper period, not
a least-period assertion. Prove it for every t using the recurrence before reducing to a finite certificate.
Alternatively keep a larger full cycle or give another explicit all-time bridge; do not infer periodicity
from a repeated prefix. The sharper256 route is preferred.

For each candidate period p, check the whole256 cycle with modular wrap, not just p or256-p consecutive
comparisons. Retain the initial row and every transition required by the list/recursive correctness lemma;
state clearly whether a list includes ticks0..255 or0..256. Once the all-time256-period bound is proved,
a cyclic certificate is sufficient. These checks are conditional profile arithmetic, not a fresh seed census.

A least-period certificate needs more than showing period p and failure at p/2 unless the reduction of all
possible smaller periods to dyadic divisors is proved/reused. Options: reuse an applicable actual kit
least-period/divisibility lemma after reading its hypotheses; prove that a least period divides a known
period and use dyadicity; or explicitly reject every positive candidate below p on the common cycle. For
the last option a witness t with D(t+k)!=D(t) for each1<=k<p, plus the period-p certificate, directly closes
minimality without any unproved monotonicity/divisibility principle. Do not rely on Python lp as a Lean proof.

The two genuine equal-alternating feeder phases must remain explicit. The16 arbitrary feeder pairs are
counter-controls only, not additional hypotheses or a replacement domain. The finite computation must be
linked to actual evol diagonals by uniqueness/induction, preserving all seven free start bits.

## Implementation and launch gates

Proceed to source preparation with these amendments; no routine owner confirmation is needed. Before any
kernel evaluation, freeze actual source, its correctness bridge, expected theorem/axiom prints, exact
checker command and resource envelope. The460k Boolean-step estimate omits reduction/list/proof overhead;
it is a work estimate, not an enforced wall or memory bound. Any bit-packed fallback is a different source
and needs its own correctness lemma and separately frozen diagnostic-driven stage, not an automatic retry.
No native_decide, sorry, custom axiom or numerical substitute for the all-time bridge. Existing controlled
Python evidence is not to be rerun just to produce another receipt.

L1105's GC2072 real-spacing compile is read separately: exit0,4.09s,1809376KiB sampled groupRSS,6266MiB minimum
headroom, zero swap growth,3 processes and standard printed axioms, as reported by Local's committed receipt.
This verifies the narrow real component on4.35, not a carrying read of the full general-arc assembly. No new
Local compiler attempt is requested for that completed component.
