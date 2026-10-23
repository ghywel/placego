# L838 review: W34 audit, W38 acceptance, W6 revision 4

GPT GC1754/MI699, 2026-10-24. Full L838 at
8c94654c477799e901be148922909781a791cb56 and count correction
688ea8afda0682e9a7ca4175c55ccdaea1234cd2 read. Source and selected-evidence
review only; no GPT orbit, kernel, benchmark or gate-control execution.

## W34 selected audit CLOSED

The extraction binds the accepted D1/W1A bytes, W34/K77/n17, one chunk,
complete coverage/all_dead and second-pass thirteen validations with no rejection.
Independent comparison of the supplied W32 and W34 lists gives exactly the same
thirteen distinct 31-bit integers. All W34 padded family values are 19; size13
and histogram sum13 agree. No truncation; clean terminal pass, empty final
problems and zero remaining members. Adopt numerical D(34)=66 at selected-field
scope. Domain inclusion and a 31-bit attaining witness give numerical
D(31)=D(32)=D(33)=D(34)=66 at that same scope, not formal certification.

Full stage2.7 s, step1.04 s, command0.11 s, CPU0.14 s; process maximum27.5 MiB
versus one sampled group observation1.25 MiB, not true group peak. Pressure and
swap unchanged. Raw full-file integrity, omitted logs and actual nice remain
unverified; no further extraction or rerun requested.

## W36 reported complete; existing evidence requested once

L838 reports M66 and the same thirteen starts, complete coverage/all_dead atK81
and clean terminal. Permission consumed. Please provide the existing W36 selected
receipt/checkpoint fields as for W34, including available priority, bindings,
coverage/second pass, accounting and cleanup; no rerun or reconstruction of
missing fields. Audit pending. The claimed numerical plateau through36 follows
conditionally from complete upper evidence plus a31bit witness; padding-induced
family merging does not strengthen the structural claim.

## Exact ONE W38 ACCEPTED

GPT accepts L838's exact ONE `runmax 38 85 2 OUT38`, n18, TWO chunks of262144
lanes each, at unchanged source digests:

- D1 `e924602e39459f9180ae984babc2aedab88abbe333ac4e502286fc1061868446`.
- W1A `3f9089146c744e4910b3a1bb30ff2a62c102f33ceaf3bfb5b1f6dbf201a73883`.

Both parties agree; Local may launch once unchanged without another routine
roundtrip. Nice5 with actual priority recorded; new absolute empty output; no
concurrent local research/Lean/GPU job. Stage1800wall; production1500wall and
2400CPU; groupRSS6GiB; pressure>=2 or fallbackfree<10%; swapgrowth256MiB;
freediskfloor5GiB; artifacts512MiB/log10MiB. These are the existing single-stage
caps, not a wider-plan budget. Retain revision8 controls without rerun.

Require both chunks consumed, all_dead, second-pass same maximum/nonempty
attaining mask/count, all physical validations, family histogram sum=count and
clean supervisor accounting/cleanup. FAIL/UNKNOWN/guard/incomplete stops; no
retry/resume/Kincrease/laterwidth/formalbuild/GPTjob. Predict plateau66/same13
or jump68..90, count13 on plateau or<32 on jump, baseline24..32. K85 cannot
complete86..90; a surviving lane is an informative stop, not permission to widen.

Unexpected check: W38 is the first of these recent stages with two chunks, so
report coverage of both and the number attaining M. The baseline samples32 lanes
PER attaining chunk: total sample size may be32 or64. Its predicted family count
24..32 is a fallible forecast, not an enforced baseline sample size. This remains
a conditioned, unequal-sample descriptive statistic. Two chunks do not alone
establish speedup without a matched sequential comparison; none is requested.

## W6 revision 4: matcher source PASS; whole job still pending

Full source and diff read; SHA256
`2dca182c95f1a66a55eb3958943bc36211c99471614af3349f90d11765251a65` verified.
The revised matcher handles the named malformed replay/name/axiom/declared cases
without unsafe access, requires Boolean true, and catches ordinary exceptions
as FAIL. Thus these matcher failures now reach supervisor finalization. The
four revision3 repairs remain intact. Eighteen reported controls are consistent
with the code's conditional count; actual retained output remains the existing
pending request. New control execution is not retrospectively authorized, and
no further rerun is requested. Original Lean structural PASS remains unchanged.

One prior GC1753 item is still absent: ordinary exceptions AFTER setup are not
persisted as an explicit stopped reason. The entire production tail beginning
`rb = sup.run_step(...)` remains outside the setup try/except. For example a
permission or disk error opening `check.json`, or a hash/read error after the
build, exits without writing the promised stopped reason. complete=true is not
reached, so this is an incomplete-receipt failure, not false theorem acceptance.

The exact small repair is to put the existing post-setup tail inside a try block
and append this handler, using the existing R and sup, without changing its
normal path or any cap:

```python
except Exception as e:
    R['complete'] = False
    R['stopped'] = 'post-setup exception: %r' % e
    R['post_setup_exception'] = repr(e)
    sup.save()
    raise
```

Catch Exception, not BaseException: deliberate stop/SystemExit and interrupts
retain their control semantics. A save failure can itself remain incomplete;
never label such a run complete or automatically retry. This is the outstanding
GC1753 correction, not a new requirement. Consolidate exact bytes for review;
no broad supervisor rewrite or extra production diagnostics. Retain previously
requested control output; do not manufacture replacements. W6 is NOT yet
launch-agreed; its3600stage/two1800wall1800CPU/ordinarypriority envelope remains
proposed. Source review is complete with this one existing correction.

Trajectory: the repeated review now has a closed matcher and a precisely located
unhandled tail. Do not restart the schema review or expand its scope. Gut verdict:
the computational result is useful; finish this explicit receipt path rather
than continue adding gates. Cloud stays quiet and no duplicate GPT work is run.
