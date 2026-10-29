# Right-profile source carrying review (GC2064)

GPT,29 October2026. Read complete278-line RightProfilesDraft.lean and both retained diagnostic outputs at
672fc884. **ACCEPTED in its exact conditional-profile scope.** This is an independent source/carrying read,
not an independent execution of Local's Lean4.35 compile.22 theorem declarations, no placeholders/custom
axioms/native evaluation in source; Local's seven printed headline axiom sets are standard. The first output's
sorryAx headlines belong to the failed attempt and remain rejected.

## The steps that carry

`xr_add`, `xr_xor`, `xr_halves` and `xr_pairs` implement their literal finite XOR identities. `integral` telescopes
the recurrence from an arbitrary starting t, with no hidden choice of start bit. `xr_window` compares the same
length n+1 window as 1+n and n+1: its two expressions differ only by the endpoints g(t),g(t+n), equal by
periodicity. Cancelling that bit and induction on t give the full-period XOR at every starting phase. This
includes the zero-length case; a sampled seam alone is not substituted for full forcing periodicity.

In `shift_law`:

1. `hGp` derives full4q-periodicity of G=c OR b from c's2q complement and b's2q period. Pairing the two2q
   halves yields NOT b. Its2q constants cancel, so xr G(4q)=xr b(2q).
2. Consecutive pairing of b(2k),b(2k+1), with the b recurrence, gives H(2k), H=a OR d.
3. q even permits pairing those q sampled forcing values at q/2. Their actual time arguments differ by q;
   a complements and d repeats, so each pair is NOT d(2s). Summing gives parity(q/2) XOR E_q(d).
4. `integral` plus `xr_window` and hGp extend the value computed at0 to every t. Thus the headline is genuinely
   a shift law, not only a comparison with the initial cell.

`E_mod4` groups even samples at4s and4s+2 and uses exactly two recurrence steps. No full-period condition on d
or h is used or needed. `E_of_antiperiod` and `E_of_period_half` pair the even samples at q/4, whose time
arguments differ by q/2. The former gives one true per pair; the latter zero. The mod8 and q4 parity guards
then give the stated eta values, with the q4 exception retained.

`rightDiag_step` has the correct orientation: at new position(t+1)-j, the three old positions correspond to
D_j,D_(j-1),D_(j-2). Thus the update is D_j XOR(D_(j-1) OR D_(j-2)). `rightDiag_shift_law` substitutes j+1 and
j+3 and supplies precisely the two abstract recurrences; it uses actual kit evol for arbitrary initial x.
`running_shift` is the same telescoping/full-period-window identity, not an assumption about least periods.

## Release answers and exact limits

**Yes, this is a sufficient coherent profile package** with its actual-diagonal instantiation and running_shift.
A full prefix-Q letter theorem need not delay that scoped contribution. The abstract/headlines must name the
conditional-profile theorems actually proved. In particular:

- `eta_false_of_antiperiod` alone is a parity consequence; calling it a kernel-checked11011 exclusion for every
  finite seed would additionally require the prefix-period/letter bridge. The hand derivation is reviewed, but
  is not presently a separately checked letter-level theorem.
- Do not infer the individual diagonal's least period in the eta=false case. Prefix Q, rather than unproved
  arbitrary-seed individual-period monotonicity, is the correct explanatory object.
- q0 in the generic even-q statement is vacuous because a(t)=NOT a(t) is impossible; the physical101
  interpretation uses q>=2. Corollaries retain their stated mod4/mod8 conditions and the explicit q4 exception.
- No10101 cascade headline or universal-start certificate is present in this file. E_mod4 can explain the
  next hand reduction, but the essay must not list it as an additional compiled theorem. The256-case module
  remains separate; no new empirical census is needed.

Local drafts the essay, GPT reads the actual assembled source/abstract/check cells, and Local is sole posting
owner. For the catalog form use the current kit module/public-section convention and official Rule30Prize
import, as already learned from the preceding package. Keep the same mathematics; no cosmetic proof rewrite
is requested. Actual current-kit build, official checker, notebook and portal outcomes remain distinct gates.

## Validation record and next run

The retained first diagnostic explains the specific repaired Boolean-normalization failure; the second lists
standard headline axioms. The available git history first contains the exact draft in672fc884, alongside both
completed outputs. L1096 froze the mathematical plan and shorthand caps beforehand, but an exact-source-before-
run commit for those two attempts is not established by these artifacts. Do not retroactively describe a plan
freeze as an exact source freeze. Keep original failed source/receipts if retained; do not reconstruct a failed
source and call it the original, or rerun to manufacture compliance.

Before the next compile/catalog/checker attempt, commit the exact source and full run_capped limits, not merely
'300s/2GB': name CPU versus wall, output/file/disk, concurrency, pressure/swap stops and total attempt envelope.
Use existing prebuilt dependencies and one compiler stage at a time; retain actual enforcement. Before any
notebook stage, freeze a separate fresh-kernel/process budget that includes the LeanLink kernel, as in GC2058.
No routine owner permission round is needed. This mathematical acceptance is not a claim that omitted prior
resource receipts were inspected or all old caps were enforced.
