# A question for the kit's maintainers: the verifier sandbox's memory limit, and certificates larger than one module

*Drafted by Cloud at the owner's word, 2026-10-24 (CL626). To be posted by the owner as an issue on
https://github.com/WolframInstitute/Rule30PrizeKit/issues (Cloud's GitHub access does not reach that repository). The text
below is ready to paste; nothing in it is private.*

---

**Title:** Verifier sandbox memory limit, and how to submit a certificate that needs more than one module

Hello, and thank you for the kit and the verifier; eighteen of our partial results have gone through it in two days.

One submission failed with a message we cannot act on without knowing the limit behind it, and we would like to know how
to shape larger certificates so that later work is not blocked.

**What happened.** Submission `R30-20261024-71f858` ("The death time at width 60 is exactly 114: a complete chunk certificate
and its witness") was accepted at 07:59Z and failed at 08:25Z with the check detail "evaluating the notebook ran out of the
sandbox's memory". Its module is one `Rule30Submission` with 4,096 kernel checks of the kit's `Rule30ZeroBoundaryLanes.check`
at width 60 (the kit's own width-52 certificate uses 256 checks in four modules). On our machine the module builds and
replays under the kit's `Check.lean` with a peak of about 4.5 GB (build) and 4.3 GB (replay). By contrast `R30-20261023-ac3898`
(1,024 checks at width 56, one module, about 1.9 GB here) passed in 36 minutes, and `R30-20261024-991a71` (194 small kernel
theorems, about 3.9 GB in our checker run) passed directly. A variant of the width-60 certificate with fewer, larger checks
(1,024 checks of 2^20 lanes) exceeded 6 GB here before finishing its build, so fewer declarations did not reduce memory.

**Questions.**

1. What are the sandbox's memory and time limits for the automatic check, and does the "four-minute" clock apply to the
   build, the replay, the notebook evaluation, or their sum? Knowing the numbers would let submitters size a certificate
   before submitting.
2. Is there a supported way for one notebook to build and import **several Lean modules** (as the kit's own
   `Rule30ZeroBoundaryWidth52` is four chunk modules and a wrapper), for instance `LeanBuild` on files the notebook writes
   into the kit copy, or an import of a module defined in an earlier cell? LeanLink's `LeanImportString` joins a list of
   sources into one module as far as we can tell.
3. Failing that, is a certificate split across **several submissions** (each a module proving a range of chunks, the last
   one assembling them through the kit's `q01_of_chunks`) something the verifier can accept, i.e. can a submission import
   another submission's module, or must a chunk-range result first be merged into the kit by pull request?
4. Could `R30-20261024-71f858` be rerun by a maintainer with more memory, as was done for the four-minute timeouts of our
   first submissions? The mathematics is unchanged and the module passes the kit's checker here.

We are happy to open a pull request porting the width-56 and width-60 chunk certificates into the catalog in the form you
prefer (several modules of 64 or 256 checks each), if that is the intended route for results of this size.

Thank you.

---

## The maintainer's answer (issue 14, sw1sh, 2026-10-24; read by Cloud 2026-10-25 00:10 BST, paraphrased from the issue page, not verbatim)

https://github.com/WolframInstitute/Rule30PrizeKit/issues/14

1. **Limits.** Each check runs with 8 cores and 32 GB of memory. The four-minute limit covers the whole automatic check:
   evaluating the notebook, building the module and replaying it. A timeout is retried once, then recorded as an error.
   Maintainer reruns allow 15 minutes for evaluation, 15 for the build and 10 for the replay, with the same 32 GB.
   71f858 ran out of memory during **notebook evaluation**, because `LeanImportString` elaborates the module inside the
   Wolfram kernel.
2. **Several modules:** not supported; the verifier builds one module, `Rule30Submission`.
3. **Imports across submissions:** not supported; a submission imports only the kit at a specific commit. Results reach
   later submissions through merged pull requests, once the verifier image is rebuilt.
4. **Rerun of 71f858:** no. A width-60 certificate settles only that width; a pass would change nothing.
5. **Pull request with the width-56 and width-60 certificates:** declined. The catalog accepts certificate data only as part
   of a theorem about an infinite family; single widths stay on the submissions site, and the kit keeps only
   `Rule30ZeroBoundaryWidth52`. **A bound on D(W) for all widths W is what would be accepted. The maintainer also asked for
   no more single-width submissions, including widths 64 to 76.**
