# L891: preparation review for the width-76 lower bound

GPT, 2026-10-24, GC1801 / MI734. Source at `70d016e6`, request at
`bd8fcbf8d41f5478586ef7bf7d1dd3fed26fa65c`.

**Verdict: preparation source PASS for the intended W76 use, with the wider-scope
correction below.** Local may prepare the W76 artifacts once a successful census
supplies the actual inputs. This does not approve a new census, a concurrent build,
or final submission bytes that do not yet exist. The GC1800 agreement remains one
W76 stage; L890 reports it launched. Final witness/digest/source/checker/notebook
review stays pending. No repeat of W74 or previously submitted notebooks is needed.

## Exact sources examined

| File | SHA-256 |
|---|---|
| `tests/probes/wolfram/d7_lower_submission.py` | `db29fe4224fe8f12c4aee964bc8f89c84fdc8759e3835f0ec67e60754ec36040` |
| `reports/wolfram-agents/submissions/d-lower-template/essay-template.md` | `275ccac7a1332aec54e5e2d50ed9a2d5f121d9bcb9c2b7f15ac16a91bed1af39` |
| `reports/wolfram-agents/pipeline/nb_gate_lowerW.py` | `dddb85ef79e18097acf77071e0e1b4413b5c627ce5a817b5938944fdbdd57879` |
| `reports/wolfram-agents/pipeline/build_sub.wl` | `1771b518d6071fd1537e5857c1a9afde21b449e22d088a7edf608bcd63dac02a` |

The generator retains D5's mathematical body byte for byte after the new header.
The shared validator, frozen-result digest, smallest-index selection and scalar
plus independent witness checks retain the reviewed D6 architecture. The notebook
gate changes its generator import, with the earlier gate logic preserved. It must
be loaded after the actual witness is frozen: its WIT/HEAD values are captured at
import, and the present empty list is preparation state, not a usable final gate.

## Corrections and limits

1. **The essay is not yet fully width-parametric.** It still executes
   `firstEvenWhite[#, 400]`. A valid completed W76 census has T = 304, so its
   uncensored death value is within that diagnostic horizon. The advertised
   arbitrary even-width interface has no such 400-step guarantee. Replace 400 by
   the frozen `@@D@@` (including the death endpoint), or explicitly restrict this
   version to W76. This is nonblocking for W76 and must be fixed before wider reuse.
   An isolated writer fixture W202/D402 emits the insufficient horizon400. Its
   orbit/reconstruction validators were deliberately stubbed: this is a serializer
   countercontrol, **not** a physical W202 witness or evidence that D(202) = 402.
2. **Freeze the actual historical metadata too.** PRIOR and the literal submission
   references are suitable for the first W76 instance, not an automatically updated
   future table. `PROVENANCE = 'L887 to L892'` currently names a future entry;
   replace it with the actual carrying entries when freezing the result.
3. **A failed write can leave a partial artifact.** The previous-width assertion
   runs after the Lean file is written. A missing-prev control fails as intended
   but leaves that file without an essay. Treat nonzero exit and partial output as
   failed preparation; preferably validate all inputs before writing either file.
   This is an operational improvement, not a gap in the generated theorem.
4. The structural census validator is not an independent audit of exact named
   checks, source pins, coverage ranges or receipt identity. GC1799's qualification
   continues to apply; final retained-evidence review supplies those checks. A
   proof of a witness lower bound must not promote numerical maximality to a
   kernel-certified upper bound.

The FileHash revision closes GC1800's source-level logging correction: both digest
labels now hash the file bytes. Local reports its one-file comparison agrees with
the independently verified essay digest. No GPT Wolfram execution or old notebook
rebuild was performed or requested.

## Controls and evidence boundaries

Pure-file checks used one synthetic W76 writer fixture, 16 malformed-validator
fixtures, exact D5-body equality, placeholder/width/coverage substitution checks,
the missing-prev partial-write control, and the W202 horizon countercontrol.
Rebinding the new gate to the retained W74 fixture gives one positive and ten
nonempty mutation controls passing. This checks reused gate behavior, not new W76
outputs. No numerical evolution, GPU, Lean or Wolfram job ran on GPT's host.

L890 reports submission17 `R30-20261024-a129c3` submitted, Lean Unverified/queued;
the public status endpoint was inaccessible through the web tool in this read.
External verification is therefore still pending, not silently promoted. L891's
14/512 W76 progress is nonterminal. Its disclosed approximately one-second
Wolfram FileHash test overlapped the census: retain that ancillary overlap in
timing attribution rather than calling the whole interval perfectly isolated.
The overlap alone neither invalidates the numerical result nor warrants a rerun.
Keep subsequent preparation to source writing until the census finishes.

Next concrete read: terminal W76 receipt/result and the frozen witness/digest;
then generated source, same-source checker receipt and actual notebook outputs.
Preparation review is complete; these are actual missing dependencies. No W78,
retry, or concurrent research permission is conveyed here.
