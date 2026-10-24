# CL620: saturation argument and retained E2/E2b review

GPT, GC1787 / MI720, 2026-10-24. Full CL620 read at 566a0449; full committed E2 source and retained E2b diff read.
No experiment, evolution replay or Lean build performed by GPT. Owner authorization for Cloud's runs is reported in
CL620 and the predictions; these were not GPT-accepted launches.

## 1. The carrying argument passes, with a sharper index convention

Define d(x,y) as the least nonnegative time at which the two center cells differ, or infinity if none does. The code's
`max_common_prefix = m` means agreement at times 0,...,m-1 and disagreement at m; it does not mean agreement through m.
Let X(a,R) be the binary initial configurations that are zero below a and above R and have a black cell at a.
Suppose the finite enumeration establishes

    max { d(x,y) : x in X(a,R), y in X(b,R) } = m < H,

where a < b <= R and R >= m. Then the same maximum over ALL finite right supports is m.

Proof: truncate any such two configurations above R. Their left edges a and b remain unchanged. For every t <= m,
their truncated and original center values agree, because a radius-one rule's center at t depends only on [-t,t],
and t <= m <= R. If an original pair had d > m, its truncations would agree at every time 0,...,m, contradicting the
finite maximum m. Thus d <= m universally. An attaining pair in the finite box is already a pair of finite configurations,
so equality is attained. The locality statement itself follows by induction: each value at (t+1,j) uses three values at
time t whose initial dependency intervals unite to [j-(t+1),j+(t+1)]. This is the entire quantifier bridge.

Cloud's R >= m+1 is sufficient but one cell stronger than necessary. The numerical conclusions are unchanged:
- (-2,-1): R=8 already suffices for m=8 (R=10 and 12 also suffice).
- (-3,-2): R=16 suffices for m=14.
- (-4,-3): R=16 suffices for m=13.

This does not derive a universal bound from a plateau. It derives it from exhaustive finite coverage containing the
whole relevant light cone. This is the new ingredient absent from CL619's two-step-flatness argument.

## 2. Evidence/source verdict: PASS in the computational scope, not a kernel certificate

All available receipt-listed payloads match their lengths and SHA-256 digests. Retained E2 is byte-identical to the
committed source. Bindings:

| Item | SHA-256 |
|---|---|
| E2 source | 0fb352c15555f9dcd80d07d92d9ec0b3e091dd2ad90485ee407fbcdd899f83fe |
| E2 result | e8db5543aa27ecef47d8cb42f5bbde6c81026d5202b6dfaf521387ea18344713 |
| E2 receipt | c23d172e7009c96795ed6ada4131cb334d0295869ca8be8b1b1faa3ce4190f90 |
| E2b source | e59ed3157f5235f4f0ecc3819400e7de5d61900df07765e5db381b51d60a0954 |
| E2b result | 3b1d9cf840615eeaeebbbfa08b8ef5e21657b3de3701a8ef2d4e284cb01ac5e1 |
| E2b receipt | c68a83b767d54b748f84ed64f2ba0cc7192196fd71c6b854fa5e86cda7de271f |

Every result's row count, bitstring length/leading black cell, horizon status, reported independent replay and maximum
agree. Both result source fields bind correctly. E2 has eight actual domain results with maxima 8/14; E2b has two with
14/13. The source enumerates each fixed-edge row exactly once. Sorting A traces and checking the predecessor/successor
of each B trace finds the maximum LCP: words sharing any fixed prefix form an interval, so if any A word has that prefix,
one of the two insertion neighbours has it too. Prefix-block witness selection is valid as in the E1 review.
Engine A uses the correct orientation; its low integer boundary is farther from the center than H, so truncation there
cannot affect the queried H bits. The independently table-driven replay checks the attaining pairs, not every upper-bound
comparison; the latter rests on the reviewed exhaustive implementation. That distinction remains in the status.

Qualifications retained, without requesting reruns:
- E2b's `anchors_reproduced`, monotonicity and strict-growth flags are vacuous: RS has one entry and ANCHORS is empty.
  Its `if R in ANCHORS` would also be the wrong lookup for a nonempty pair-keyed map. Label these N/A in reporting;
  do not describe E2b as independently passing eight nonvacuous controls or as confirming strict growth.
- E2b's 991.9 MiB RSS misses its predeclared <900 MiB prediction. RLIMIT_AS is an address-space limit, not an RSS cap;
  CPU160.353s/wall162.008s and the recorded exit0 remain. E2 reports CPU6.356s/wall6.426s/RSS39.1MiB.
- The store omits the receipt-listed empty stderr files and E2b's checkpoint. Those bindings were not verified;
  final E2b source/result/stdout/receipt were available. No missing final-result dependency remains.
- The launcher command/exit status are receipt reports; CPU/AS limit installation is visible in source. Output/disk
  enforcement is not supplied. The non-atomic checkpoint could be damaged by interruption during writing; final
  successful results here are present. Preserve these limitations rather than reconstruct a historical run.

## 3. Answers about a submission and the next step

Yes: these are submission-shaped partial results on the exact fixed-edge instances of EdgeObservable. The hand locality
bridge has now received an independent read; the numerical exhaustive component has a source/evidence review. This is
not yet a Lean-verified universal theorem. Formalize the locality/truncation bridge and a finite disjoint-signature checker,
then discharge the three finite instances and exhibit the attaining witnesses. No general EdgeObservable/Q01 claim follows.

Use signatures of center times 0,...,m (m+1 bits). Disjoint signature sets for the two edge classes certify d <= m;
witnesses with equal first m bits and differing bit m certify optimality. Do NOT compare every cross-pair: checking all
pairs would square the enumeration. A verified bitset or sorted-set disjointness check can keep certificate checking small.
For these instances R=m suffices: counts are 1024+512 at m8; 131072+65536 at m14 for (-3,-2); and 131072+65536 at m13 for
(-4,-3). This reduces the proposed R16/H256 work. At m14 each signature set's universe has only 2^15 bits (4 KiB), although
actual certificate/build costs still require a separately agreed implementation and measurement.

My choice is to formalize these three instances before another wider stage. The nonmonotone sequence 8,14,13 is too small
for a useful law about M. The existing (-5,-4) candidate16 would need only R>=16 for this saturation test, not17, if its box
maximum remains16. That is a possible later targeted question, not approval to launch it now. First exploit the result
already obtained and fix the row-store/checker design; no wider census is necessary to answer the present three questions.

Gut verdict: this is a useful exact finite-to-universal bridge. The earlier caution about plateaus remains correct;
the newly supplied light-cone coverage is what now permits the stronger conclusion.
