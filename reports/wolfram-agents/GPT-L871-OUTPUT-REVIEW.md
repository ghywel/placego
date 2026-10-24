# L871 retained-output review and heartbeat correction

GPT, GC1784 / MI717, 2026-10-24. L871 at ef106130e5ade4208c38c3b16bb2cb533948f5a0;
latest Local entry L873 at b399e84096565c00b078511833a550579f016a1d fully read.

## Actual output verdict: PASS

The lower-bound mathematical source and all eleven actual output cells pass review in their stated scope.
This closes the pending L871 output read. It is a retained-evidence/source review, not an independent Lean replay,
external verifier result, proof of maximality, or authorization for a new census.

Downloaded all 15 payloads listed in `cited/lower-64-72/manifest.json`; every byte length and SHA-256 matches.
The manifest itself is an additional file, hence Local's 16-file total. The committed module, essay and gate digests
match their manifest fields. The notebook bytes themselves were not supplied; its 72,790-byte size and digest remain
Local's manifest binding, not an independent whole-notebook hash verification.

- Module: `4912905337e645c425c71162ad16b43c3ae7c0d527f76e2b79008a9cc4bf2812`.
- Essay: `2b9339780363b73d8f97df2601a9c182b80cd2be126012fa1829d0f32f5071f4`.
- Checker JSON: `eb274e6ed43f172e420ec93b268da26e0ee39fb6af258cb864b5f214e4850bb3`.
- Gate revision 3: `ebf9af64a69fbc8c4e9f6b91d81e755056527355d2e726fb46b844db2211eb62`.
- Notebook digest reported by the manifest: `6181671a9dc5c205286d9d7cbc40437c94c7eb362c72872786c231e7932297ee`.

Read every output cell in full. Bit lengths are 64,65,67,70,72; first even-white times are116,120,122,124,130.
The raster output is present with dimensions210 by133; its compressed pixel payload was retained/hash-checked, not
independently recomputed as an orbit. It is illustrative, not carrying proof evidence. The kit-directory output is True
and environment head is LeanEnvironment. All38 environment association names/kinds match the checker's declared list:
five definitions and33 theorems. Every headline displays the correct paired width and survival bound; all five axiom
lists are exactly Quot.sound and propext. The width72 survival/death statements and two bridge lemmas are correct.
The complete KernelCheck cell displays Success and its underlying Success association agrees:52 accepted declarations,
one consistent temporary module identifier. No contradictory hidden count or failure was found in these actual cells.

The checker JSON reports partial claim, pass, no new axioms, all38 declarations standard-axiom, all five expected headlines
found/ok/type-matching, and replay52 ok. It does not report an official prize target proved. The essay's decoded embedded
Lean source is byte-identical to the standalone module, and comparison with the previously reviewed module confirms the
Lean text outside the module documentation comment is unchanged. The prior carrying mathematical source PASS therefore
continues to apply. Revised depth orientation and detailed census-validation scope are correct.

## Two remaining maintenance corrections; no new mathematical review loop

The **frontmatter Abstract**, unlike the corrected essay body, still says “every start of widths64 to72” and makes the
unpinned claim that the kit has no statement above52. Before publishing, change those frontmatter sentences to:

> At the pinned kit commit cc1e0e0, the kit proves D(52) <=96 and has no statement above width52. A complete numerical
> GPU census of the reconstructed starts surviving the even times below each width found the stated maxima; earlier
> deaths cannot exceed the exhibited values, which are greater than their widths.

This is the already-requested scope correction, not a change to a theorem, witness or executed output. Local can apply
this editorial repair under the owner's standing submission permission without another mathematical-review round trip.
The actual-output sign-off above is complete; a final submission must retain the reviewed Lean source and outputs.

The gate's `controls.mutated` helper truncates the cell before reading it:
`open(p, 'w').write(f(open(p).read()))` evaluates the write receiver first. Thus its reported cell-mutation tests were
empty-cell rejection tests, not the advertised planted-content tests. Read `before` first, compute and assert a changed,
nonempty `after`, and only then write it; use TemporaryDirectory so test copies are cleaned up.

Independent pure-file controls, avoiding that helper, reject the unexpected underscore/digit axiom, changed width,
changed bound, changed death list, and bad checker axiom. Replacing all copies of each summary count also fails as expected.
However, changing only the first displayed count in cell5 or cell11 **still passes**: another unchanged copy satisfies
the substring search. This shows why the flawed helper had concealed a real limitation. Parse and require agreement of
all displayed and underlying summary fields, or compare their complete normalized structures, before treating this gate
as an automatic full-output certificate in future. The exact theorem/axiom cells now correctly reject the original
GC1782 counterexample. These gate limitations do not negate the direct complete read of the current actual cells.

No rebuild, census, orbit experiment or kernel replay was run by GPT. No further mathematics sign-off is needed for
these five lower-bound statements. The source/evidence review is CLOSED; gate-helper maintenance and the final metadata
correction should be recorded separately from that completed result.

## Heartbeat correction executed, not merely proposed

At the owner's instruction, updated both existing automations through the app tool and reread the saved configuration.
The research heartbeat remains ACTIVE every13 minutes and coordination ACTIVE every5 minutes, on the same chat.
Removed the stale GC1778/L866 restart snapshot and the instruction to defer every substantial review until a research tick.
Both now use live durable pending reviews. A poll still refreshes flags and git on every scheduled wake, but then resumes
active work or starts an available already-authorized review. New ticks do not cancel the active review. Receipt-only
bookkeeping is insufficient when the required evidence is accessible. No schedule or work was started for Cloud.

The immediate check of that correction is this completed L871 review. Next available work is CL619's retained E1 results
and corrected source, followed by Local's L872/S0 and L873 exact driver; those are received, not launch-accepted.
