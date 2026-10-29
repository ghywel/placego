# Universal-start certificate cost: retained stop and cheaper proof route (GC2086)

GPT,29 October2026. Read the full stage3 receipt/RUN-SPEC outcome and the complete frozen cert_cost_probe.sh
at8e5f24e35ef85984b5e56f067a2d366cc77d4306. No duplicate evaluation or larger memory cap proposed.

## What the actual stage establishes

Module/checker digests matched. Stage3 ended RSS_STOP after15.55s, at4300336KiB sampled groupRSS against
4096MiB, with6038MiB minimum headroom and zero swap growth, at most4 live processes. No compiler diagnostic
or checker outcome was printed. This is an unsuccessful bounded compile, not a false certificate or accepted
partial proof. Preserve full source/log/time/launcher/cleanup evidence. There is no completed certificate
validation; 'unevaluated' in earlier notes must not be read as proof that no reduction was attempted.

The cheap placeholder builds make cert evaluation the plausible cost source. That attribution is an inference,
not a per-declaration profiler measurement. The new V0 baseline on the actual module body is the right control.
Do not infer a maximum/case cost or asymptotic law from the rising group samples.

## Read of the already-frozen cost probe

V0/V1/V16 each run in a fresh Lean process, source digest is pinned, the replacement pattern matches once,
and no checker or completed full-cert claim is made. I independently checked the literal source-replacement
pattern against the current file; it matches exactly. The cert_one/16 expressions depend only on concrete
certOK, not on the full-cert placeholder. Thus their measurements can diagnose reduction cost despite the
other stub-dependent headlines retaining sorryAx.

Interpret limits exactly: the per-process300CPU cap applies to each inner time wrapper and Lean process;
600wall/3584MiB sampled groupRSS/16file/64output/5120launch1024ongoing/256swap protect the whole serial group.
The nested time wrapper means up to5 live processes (outer time, Lake, shell, inner time, Lean), not the4
from the prior stage. The shell's `|| echo FAILED` can continue after an elaboration failure and its final DONE
is not a successful control verdict. Retain each exit/output/time and classify it; an errored V1/V16 supplies
no successful proof-cost observation. Do not widen/repeat this already-frozen stage automatically. If it
already ran, consume its exact results, not a cleaner rerun. No new certificate stage is approved by this note.
V1/one16-case group are NOT a measured maximum over both phases/all cases. A split implementation needs an
actual final assembly/replay/resource budget, not linear extrapolation alone. V0 and V1 contain the same
noncertificate body, so compare a per-case increment against that baseline rather than treating total V1 time
as pure case time. Fresh Lean processes do not reset OS file caches, and one noisy wall-time difference may
be negative; report actual user/system/wall/RSS values without forcing the predicted linear fit.

## Answer a cheap structural objection before another large reduction

The original all-time256 bound is deliberately loose. Once a few short parity facts are established,64 ticks
suffice for ALL seven diagonals. This suggests reducing the proof obligation, not only splitting a large
proof. This is a proposed formalization route for the already-known theorem, not a novel theorem or launched
competing test. Local remains the sole universal-start writer/executor.

Write a=alt p, u=E0, v=E1, w=E2, z=E3, h=E4, j=E5, k=E6. All parities below are XOR totals, for arbitrary
start bits. Use the already checked running_shift/xr_halves/xr_not identities.

1. u complements at2 because the two forcing ticks of a have odd parity. Therefore u has period4.
2. v complements at4: pair its forcing(u OR a) at t,t+2. u complements and a repeats, so each pair is NOT a;
   its two-tick XOR is1. Thus v has period8.
3. w has period8: pair(v OR u) at t,t+4. The result is NOT u over four ticks. Its XOR is0, because u
   complements at2 and there are two complementary pairs. This needs no256-case check.
4. The remaining small parity obligation for z to complement at8 is

       XOR[ w(t) OR v(t), 0<=t<8 ] = true.

   It depends only on p and the three initial bits of u,v,w:16 assignments of an8-tick forcing parity,
   not256 assignments of seven256-tick masks. Derive it symbolically if convenient, or freeze a genuinely
   tiny kernel certificate with its correctness bridge. This note has not evaluated those16 cases.
5. Given step4, h complements at16 by the EXISTING101 shift law at q4: d=u (period4, anti2), a=v (anti4),
   b=w (period8), c=z (anti8), and z_of_shift_law=h. eta_four u=true. This is exactly its guarded q4 exception;
   no false general monotonicity is involved.
6. j has period32: pair(h OR z) at t,t+16, yielding NOT z over16 ticks. z complements at8, so those16
   values have even XOR (eight complementary pairs). Hence the running integral repeats at32.
7. k has period64 by run_double, since both h and j repeat at32.

All earlier profiles repeat at64 as well. With this genuinely proved upper bound, a64-bit cyclic checker can
establish the same individual least periods, using the already-reviewed full-cycle/minimality guards. It
must actually replace the all-time bound, mask width and wrap lemma consistently; replacing256 by64 only in
the numerical loop is invalid. The case COUNT remains256 even if the cycle WIDTH becomes64.

These parity arguments establish upper/anti periods, not every least-period assertion. Keep the distinction;
no assumption that failure at P/2 excludes all smaller periods unless a dyadic-divisibility lemma is proved.
Retain the exhaustive smaller-positive-period mechanism or prove the required generic reduction. This route
also needs a carrying read before upgrading new hand steps; I have not claimed a completed all-symbolic
certificate or a cost guarantee. Use the measured V0/V1/V16 result to choose between this proof reduction and
an independently validated split, rather than raising the memory cap or manufacturing further census work.

## GC2087 — actual probe results and selected next step

L1114's actual V0/V1/V16 variants all fail at the old Int/Nat binder mismatch. Their wrapper's COMPLETED/DONE
must not hide those failures. Per-process RSS316571648/335511552/625049600bytes and1.17/1.21/2.34s are retained
partial measurements; they suggest a cost model, not a maximum or universal linear law. The later corrected
S1/S3 skeletons have no errors,15/13 expected placeholders, and process maxima630308864/661864448bytes.
Only the first three16-case groups have actually completed kernel evaluation in those probes (48 distinct
assignments). No full cert or unchanged-checker replay has passed yet.

The actual split source and explicit assembly are independently read GC2087, with an exhaustive source-level
prefix/branch correspondence check. Its one-stage full check at unchanged caps is accepted. Prefer finishing
that already supported path; the hand64-width route remains available if a new discriminating failure calls
for it, and is not a second implementation or launched test. Retain all unsuccessful source/variant outcomes.
