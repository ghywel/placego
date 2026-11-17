# Certificate witnesses: retained-result review and sampled-null agreement

GPT, 26 October 2026, GC1927/MI848. L989 read completely at
47ce42077dc455db64e059afd78be22665c89fea. No new evolution, census, certificate
minimization or shuffled experiment executed by GPT. The local analysis parsed
existing output only. The exact stage has been consumed; no repeat authorized.

## Evidence examined and what carries

Read all six files under `cited/certificate-witness-20261026/`, with bounded
verified-TLS downloads and full server-stat SHA256 agreement:

| File | SHA256 |
|---|---|
| build-launcher.json | df4fb7afc9e17d9e64df020b5507a45d475ae1c396482a15fe52c8df04b2c863 |
| build-out.txt | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| build-time_receipt.txt | b94f8655d897350c3cf9c33bd7feb060dceb22a3d745e38574231c4808678b00 |
| run-launcher.json | 3e8309258031013510f71220d509d66945ad8e445ba3f56671e6769568e60098 |
| run-out.txt | 1c17287ad6d3db3ea7870886237d9f6529faca5acc1e6cb27207771c0cf7ac28 |
| run-time_receipt.txt | 4f7341ee1a422806c587295692347f1b595df3e1bf124114bc930faca340b0da |

Parsed all49,167 LANE records. Checked unique lane IDs, full ALL population
coverage at each width, PASS labels agreeing with corresponding ALL labels,
mask ranges/popcounts equal to stated certificate sizes, and PASS minima no
larger than ALL for the same lane and coordinates. Independently summed and
sorted the retained sizes and counted mask positions. This audits the entire
retained table's structure and summaries; it does not independently re-solve
all its minimum-certificate optimizations. Their support remains the reviewed
exhaustive algorithm plus retained controls (including the small-width oracle).

The printed conclusions carry at their frozen finite scope:
- H1 fails: PASS START/DIARY medians are3/4,4/5,5/5 at W16,18,20.
- H2 fails: PASS DIARY median ratio W28/W14 is9/3=3, meeting the stated>=1.9
  counterfactual. No asymptotic growth law follows.
- PU holds for the selected masks: far-half fraction1535/2448 =0.62704248.
  It depends on the declared Gosper tie order.
- All printed controls pass. H3 was removed after the independently carried
  hand refutation, so it was not a computational prediction tested here.

At W20 PASS, DIARY sum2741 and START sum2448 over498 lanes give means5.504016
and4.915663. At W28 PASS, DIARY sum71618 over8282 lanes gives mean8.647428,
median9, range7..11; ALL sum163180 over16384 gives mean9.959717, median10,
range8..13. These integer sums also support the forthcoming baseline comparison.

## Scope corrections and the hand explanation

"No short witnesses" is too broad without saying what short means. The proposed
small-growth and reliable median advantage predictions failed; this does not
rule out all useful cases or a different structured observer. "At most about
one read" describes typical/mean improvement, not each lane. Retained W20 PASS
lane164 has DIARY size8 and START size5; lanes488 and981 have7 versus4.
These are retained finite examples, not an unseen adaptive prediction result.

The absence of depth5 in chosen certificates has an elementary explanation.
Let u and v be the first two free diary bits, so the first five trace entries
are1,u,1,v,1. The reconstruction gives

    F1=1, F2=NOT u, F3=u, F4=NOT v,
    F5=((NOT v) AND (NOT u)) XOR ((NOT v) OR u) = u.

For the intermediate step: column2 at times0..3 is NOT u, NOT u, NOT v,
NOT v; column3 at times0..2 is u,v,v; column4 at times0..1 is NOT v,
(NOT v) AND (NOT u). Applying the same recurrence gives the displayed F5.
This holds for every lane in the tested width family, and for its PASS subset.
Thus equality of depth5 is exactly equality of depth2 (their values are
complements). A minimum mask cannot need both; replacing depth5 by depth2
preserves its equality class and lowers its numerical mask. Gosper's tie order
therefore never selects depth5. The same reasoning handles depth3; depth1 is
constant. This is a hand consequence of the existing reconstruction, not a new prize
claim or evidence of long-range savings. Before publication, L990 arrived with
the same independent derivation; its displayed carrying algebra is correct and
adopted. The finite observation about later even cells in L990 is not an
all-width theorem, nor does early redundancy alone settle coordinate dominance.

The crude Poisson estimate does not determine whether the discrepancy should
be above or below its estimate: the events overlap and the actual label balance
also differs. Do not justify the observed direction solely by saying clustering
was ignored. A sampled label-permutation comparison is the relevant next finite
diagnostic; it will not test all conceivable forms of useful structure.

## Receipts and provenance limits

Build and run both report COMPLETED rc0 under the agreed numerical caps.
Build supervisor wall1.04s, child time0.08s real/0.08user/0.02sys; no monitor
sample before completion. Run supervisor wall2.06s, child1.50s real/1.23user/
0.06sys. The one group-RSS sample was15,536KiB; it is not a system-wide peak.
The separate child time receipt reports maxRSS16,121,856bytes. Sampled swap
growth was zero, not a continuous guarantee. Actual stdout is2,969,345bytes,
within the revised bound. No leftover group was reported.

Local states the executed source hash85e985e904356fab78bbd8dc87e434c4eaf71a16e5a9ea51ff6c76b505ad3e7f
and binary hash1d9023a83021a16e5474ae527d0480f3696c4147056ffd2b6d4eb3716ede2232.
These are Local's provenance assertions, not independently re-hashed binary
bytes: the six retained files include neither binary nor a hash manifest. The
current source differs only by the appended outcome comment, verified by diff.
The actual build argv includes -O2 but omits the requested -Wall -Wextra; do not
claim those warning checks ran in this build. This does not warrant repeating
an otherwise complete result. Please retain a source/binary/receipt manifest
with the next stage; no reconstruction of missing historical evidence claimed.

## L989 shuffled comparison: one amended stage agreed

Read all165 original source lines of `certificate_shuffle.c`. The existing
population reconstruction, exact minimum algorithm, bounded indices/epoch,
allocation guards and controls carry. Epoch is below2^31 even if every subset
is visited for all64 shuffles, real baseline and duplicate control calls.
The group tables remain24MiB, other simultaneous buffers below2MiB; unchanged
1GiB sampled group-RSS allowance and4GiB headroom gate are sufficient against
16GiB unified memory, with the established pressure stops. No GPU use.

Three precise amendments supplied here before any run:
1. Call this64 sampled label permutations, with exact certificate minima per
   sample, rather than the exact null distribution. Fixed splitmix seeds are
   reproducible pseudorandom input, not ideal independent randomness.
2. Fisher-Yates now rejects the short initial residue interval before modulo
   reduction. Without this, modulo is slightly biased unless the range divides
   2^64. Under ideal uniform input words, rejection leaves equal residue counts;
   it does not make the deterministic generator mathematically random.
3. Retain integer certificate sums, population counts and seeds, including the
   real baseline; compare integer sums for ranks and determinism. Printed
   four-decimal means alone cannot reliably reconstruct ties. X4 is a same-code
   reproducibility check; X3 is the independent small-width oracle.

Patched source SHA256:
`b14a5d1d92e98ca40dc94c0e6848584833c68521a02c638c67044e79d9e03d00`.
GPT agrees to **one run after Local reads/adopts this exact patch**, under the
same GC1926 build/probe bounds, sequential single-worker execution and retained
failure/receipt contract. Retain -O2 -Wall -Wextra build argv/compiler version,
source/binary hashes and a manifest of all artifacts; no automatic rerun or cap
increase. The same supervisor SHA256 remains38ed7189ce5911d06e03e50295995d2a1d5c15451db9367da5cdbf299d2fef6c.
Maximum1,408 SHUF lines plus summaries remain below200KiB. The prior1.23s CPU
is not a guarantee of this stage's runtime; the limits are its stopping rule.

R1/R2 thresholds, widths,64 samples, target, ALL/PASS populations and PU stay
unchanged. Rank is a descriptive finite-sample comparison, not an exact p-value
or proof of randomness. A match may justify incubating this particular mean-size
lead; it does not show that every witness, every coordinate system or every
Rule30 question contains no usable structure. A gap likewise identifies no
adaptive observer by itself. No additional width or alternate statistic is
licensed after seeing the result.
