# L798: W3 existing-receipt audit

GPT, 2026-10-23 20:08 BST. **PASS in the controlled finite scope; adopted as tier 1.** No benchmark or Lean replay on GPT's host.

L798 at 39d709c9 (published 79480a5b) reports the completed one-run agreement GC1723/L796. The actual stored
`workers/local/w3-20261023-1925/receipts.json` is 288,381 bytes, SHA256
`b39e6b9c37dc90c1297dc986eed305bcbf4ce734454875caf9a782be5ec0359b`, matching the committed pointer.
It has complete = true and elapsed_s = 1849.4. The W3, generator and supervisor digests match the accepted versions;
the matcher is bound by L796. Kit commit, seven source pins, clean initial tracked tree and dependency checks pass.
All fault settings are null and the accepted 3,600-second stage/resource caps are retained.

There are 71 receipt entries: preflight and engine controls, then 69 supervised invocations comprising three controls,
64 modules, wrapper and checker. Every supervised invocation has accepted verdict, completed reason, empty final
problems and zero remaining owned-group members. The 64 module indices are exactly 0 through 63, all object files
exist, all 64 recorded object digests differ, and no post-module cost stop is recorded. These are controlled-run
receipts, not an independent replay or an assertion that different indices mathematically require different hashes.

Source binding was checked without executing the harness: extract the four pure text-generation functions from the
already reviewed, hash-matched W2 generator, render the 64 module strings and wrapper, and compare all 65 SHA256s
with the receipt. All match. The source contains exactly c = 0 through 4095 once each, with K = 129 and n = 18.
This is an artifact/digest audit using the same generator, not an independent mathematical experiment. The previously
reviewed typed range assembly and physical bridge carry the coverage inference.

All three control logs fit completely inside the receipt's stored tails and were read: known-false K1 rejection,
wrong 4095-chunk coverage type, and the positive K129 chunk. The complete checker JSON is present in its tail,
although the first 65 bytes of its 2,065-byte log are not retained there. JSON says headline q01_width_le_60 found,
theorem, typeMatches true, axioms propext/Classical.choice/Quot.sound, no new axioms, no reasons/problems, verdict
pass and replay of five wrapper constants successful. Imported chunk checks were kernel-checked at compilation;
this replay does not repeat all 4,096 checks. No raw binary objects were independently replayed by GPT.

**Adopted conclusion:** every Boolean starting row supported at depths at most 60 has its depth-1 zero-boundary
cell white at some even t <= 128. This is the finite-width Q01 statement. K = 129 is established by the complete
certificate; D(60) = 128, the conjectural 112, arbitrary-width Q01 and the full period-2 prize are not established.
The owner withholds submission. The one-run authorization is consumed; no extension or retry follows.

## Measurements and corrected labels

The precise command real time across modules is 24.45–31.44 seconds, mean 28.1546875 seconds. Supervisor wall is
24.91–32.38, mean 28.6915625. User time mean 23.32078125 and system time mean 5.288125 seconds. Keep these timer
boundaries distinct in later comparisons; the 30.8-minute stage includes supervision and other work.

Time-l maximum process RSS across modules is 1,487,421,440–1,563,197,440 bytes (about 1.385–1.456 GiB).
Sampled process-group peaks are 2,103,508,992–2,244,329,472 bytes (about 1.959–2.090 GiB). L797's 2.08 GiB
comparison against a process-only memory forecast mixed measures; L798 correctly separates them. The literal
1.3–1.4 GiB prediction still has a modest upper-end miss; do not retain an unqualified “all predictions held”.
Neither measure is a system peak or a causal bandwidth measurement. Recorded final pressure is level 1; baseline
swap is nonzero, so zero swap growth is distinct from zero swap use. Maximum recorded new artifacts are 12,044,503
bytes. No cap change or replay is needed to resolve these labels.

## W4 and next compute

Revision 2 SHA256 6ac58e45632ffb2b3b5a2c4a4aa3906fc6785ca681fd8a27019ae914d719a26f was diff-read: it fixes
INPUT_SET to W60 and updates prose only. The first/last W60 source hashes now match the audited W3 receipt.
GC1725's snapshot, timer-boundary and partial-start lifecycle corrections remain required; **W4 is not launch-agreed**.
Local has acknowledged that review. No repeat review of unchanged code or duplicate request is needed.

The owner's GPU question was answered with the small exact Metal survivor-engine design already in
GPT-NEXT-M5-COMPUTE.md: 32 candidates per integer word, independent CPU controls, retained masks/survivors,
measured end-to-end costs. This remains design-only; no Metal job, large census, simultaneous CPU/GPU run or Cloud
queue is authorized. The full Q01 inference remains open. Gut: the completed finite certificate is solid within
its stated scope; prioritize a reliable next pilot and information gained over automatic width growth.
