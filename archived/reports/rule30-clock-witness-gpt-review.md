# Cut49 optimum52: retained evidence reviewed

GC1951, 27 October 2026. L1011 at fea5b4263daad6f09643100fd6fd831d065e27bf
read completely. The agreed source and supervisor hashes match GC1949.
The one M5 extraction is completed and its exact finite result is accepted.
GPT did not rerun the SAT solver or launch another evolution experiment.

## Evidence examined

All11 files under cited/l1011-gc1949-witness/ were fetched. Upload manifest
SHA256: b0b39188b1025b5865d4ba98192c30f97c77cd992b7a624cd990910508fdde8b.
Verified all10 upload file hashes and all6 artifact hashes inside the probe
manifest. Read the complete right row, natural trace0..56, left diagnostic41..56,
probe manifest, sanitized supervisor receipt and time receipt. The retained
CNF has2500 variables and8502 clauses. A separate data-integrity check confirms
one signed assignment for every variable and satisfaction of every clause.
All56 centre transitions in the retained trace obey left XOR(centre OR right).
This checks the saved evidence; the complete evolution producing the trace is
Local's run of the source already independently reviewed in GC1949.

## Exact finite conclusion

Use the prescribed finite left cut L=49, centre1, and right cells1..50

    00001111001101111111000000110001101000010100000011

with zeros beyond. This explicit finite row keeps the centre alternating
through time51 and first fails at52. At51 the natural triple is000, so its
next centre is0 although the required phase is1.

For ANY right completion preserving the clock that long, the clamped-left
diagnostic agrees with the actual left neighbour. Its values at white ticks
41,43,45,47,49,51 are010110. The required right word is therefore101001.
The previously certified finite right-language exclusion of101001 (GC1945,
L1006) rules this out. Hence no right completion keeps the clock through52.
The retained explicit witness attains first failure52, so the optimum is
exact. This upper bound uses the existing finite certificate, not an
unretained UNSAT proof from the earlier exploratory SAT run.

Scope: one fixed finite left cut of the known infinite-left reference,
arbitrary right completions. Not a bound over all finite seeds, not a theorem
about the single-seed centre, and not a proof that every periodic relay ends.
No new portal contribution or Lean verification is claimed.

## Enforcement receipt

M5/kissat4.0.4, one execution, COMPLETED/rc0; solver rc10, timeout false,
G1 and G2 true, complete model checked. Launch free+inactive5802MiB exceeded
4096MiB. Supervisor wall1.04s, own CPU0.08s. time-l records0.08s real,
0.07s user+0.01s system, max RSS18,563,072 bytes, peak footprint14,778,752 bytes.
Those process receipts are not a system-wide peak.

The stage finished before the first one-second monitor sample. Empty samples
and zero maxima mean unobserved intermediate pressure/RSS, not zero usage.
No claim of continuous whole-system memory verification. Supervisor final
bytes147477; downloaded probe artifacts including their manifest146526bytes,
within256KiB. L1011's164KiB may reflect filesystem allocation; the byte-count
receipt is the quantity used here. The sanitized launcher replaces its private
output path; the original hash is retained in the upload manifest, not claimed
independently re-hashed by GPT. No retry or wider stage was performed.

## Interpretation and next obstruction

The witness contains white ticks with left/right support01 and10. This is
real compatibility of the two immediate support arrangements. The01 instance
at45 precedes the cut's first possible centre influence at50, so it is not
by itself evidence of a new repair mechanism or a newly born staircase taking
over. The extra survival beyond the unedited cut's failure50 is finite right
compensation, ending at the known language obstruction52.

Question: can the right side repair the first disturbance from this cut?
Response: yes, for two ticks, with an explicit row now retained.
Challenge: the next required right word is impossible.
Better question for owner inquisition: what additional relation between
successive *different* supports could control the moving centre? Counting
more edge cycles or longer cuts, without that relation, would repeat the
same finite-compatibility exercise. The programme remains active; this
particular evidence obligation is complete and no numerical follow-up is
proposed merely to extend its graph.
