#!/usr/bin/env python3
"""Generate the TRIDIRECTIONAL interpolation shader from the bidirectional base.

    ./gen_tridirectional.py [output.glsl [base.glsl]]     (default: ../tridirectional-interpolation.glsl)

THE HYPOTHESIS THIS BUILDS. A 2-frame shader can only encode constant
velocity: something was at A, it is at B, and an inserted frame places it on
the straight line between them. Under acceleration that placement is wrong by
a/8 px at mid-interval (a in px per frame-interval^2) -- imperceptible at
24fps cinema rates, systematically wrong for anything that needs positions to
be RIGHT rather than plausible. Three frames are three data points, and three
points determine a quadratic: velocity AND acceleration. This generator
produces a shader that fits that quadratic per texel and places the object at
its correct position on the curve, not at the constant-velocity midpoint.

WHY GENERATED, NOT FORKED. The tridirectional shader is the proven
bidirectional pipeline plus three additions: a third-frame luma pyramid, one
more flow-field chain (anchor -> outer frame), and a quadratic warp
correction. Everything else -- the block match, the tie-breaking, the
regularisation, the medians, the caching -- is identical, and should STAY
identical as the base improves. A hand-fork would rot the way the diffuse-*
forks rotted (see SHADERS.md); a generator inherits base fixes on
regeneration, and the smoke test can verify the committed file is exactly
what the generator produces. Same reasoning as gen_variational.py.

THE 3-FRAME WINDOW, AND THE MISTAKE WORTH NOT REPEATING. Binding FRAME2
declares frame_mix_count = 3. The patch guarantees the first two selected
frames straddle the output time, then adds the temporally nearest third -- so
the window is {prev2, prev, next} while the output sits in the first half of a
source interval and {prev, next, next2} in the second half.

The first version of this generator built every pass around ROLES: frame "A",
frame "B", the "anchor", the "outer" frame, each resolved at runtime from
rts_mix. That is the natural way to describe the algorithm and it silently
corrupted every cached field, because roles ROTATE WITHIN A FIXED WINDOW. At
24->60 two consecutive output frames share the window {S0,S1,S2} while the
straddling pair advances from (S0,S1) to (S1,S2). `pair_changed` correctly
reports that the window did not change; the cached "A->B" flow then belongs to
the wrong pair.

That was misdiagnosed twice before it was understood -- first as a Vulkan
storage-image ceiling (refuted: the device reports no such limit), then as a
deficiency in `pair_changed` itself (also wrong). `pair_changed` means exactly
what it says: the window changed. It is the right invalidation signal for
anything that is a function of the window, and the wrong one for anything that
is not.

So this generator is SLOT-KEYED. Every pass works on fixed slots -- 0, 1, 2 in
ascending time -- and computes the four adjacent-slot flows F01, F10, F12,
F21, all pure functions of the window and all safely cacheable. Only the final
pass knows about roles, and it derives them per output frame from rts_mix
without recomputing anything. The payoff beyond correctness: the anchor is
ALWAYS slot 1, so the acceleration solve loses its phase dependence and
reduces to a = F10 + F12.

This is also the shape that generalises. An N-frame window has N-1 adjacent
slot pairs and fits a degree-(N-1) polynomial; nothing here is specific to
three.

THE ALGEBRA. Let A and B be the straddling frames, s in [0,1] the output's
position across that interval, f the flow A->B, and a the per-texel
acceleration in px per interval^2. The constant-acceleration trajectory
through the three frames gives the displacement of A's content at s as

    d(s) = f*s - (a/2)*s*(1-s)

i.e. the bidirectional shader's linear warp PLUS a correction that vanishes
at both endpoints and peaks at a/8 mid-interval. Both warp directions get the
same +(a/2)*s*(1-s) term (it is the same trajectory bowing). Acceleration
itself comes from the two flows out of the ANCHOR frame (the straddling frame
adjacent to the outer one): for uniform spacing they cancel exactly under
constant velocity, so their sum IS the acceleration. The general non-uniform
solve, VFR-safe, is in the generated final pass. At a = 0 the tridirectional
shader degenerates to the bidirectional one EXACTLY -- which is both the
safety property and the null hypothesis.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
# The base to generate from. Default is the shipped bidirectional shader;
# a second positional argument names a VARIANT base (e.g. a two-descent
# bidirectional-interpolation-<variant>.glsl), so tri/quad variants can be
# generated beside the stock files without overwriting them.
SRC = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else \
    HERE.parent / "bidirectional-interpolation.glsl"
DST = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else \
    HERE.parent / "tridirectional-interpolation.glsl"

LEVELS = [("S", 16), ("E", 8), ("Q", 4), ("H", 2)]

# ---------------------------------------------------------------------------
# SLOT-KEYED, NOT ROLE-KEYED. This is the whole architecture, and getting it
# wrong the first time cost a round of invalid results.
#
# The three bound frames arrive in ascending timestamp order, so FRAME0
# (HOOKED), FRAME1 and FRAME2 are stable identities: slot k is slot k for as
# long as the window lasts. Their ROLES are not stable. Which pair straddles
# the output, and therefore which frame is "A" and which is "B", flips at
# mid-interval while the window stays the same -- at 24->60 two consecutive
# outputs share the window {S0,S1,S2} with the straddling pair advancing from
# (S0,S1) to (S1,S2).
#
# Everything cached must therefore be keyed on SLOTS. `pair_changed` reports
# that the window changed, which is exactly right for a slot-keyed quantity
# and useless for a role-keyed one -- cache a role-keyed flow and it silently
# survives a role rotation it should not have. That is not a defect in the
# patch; it is what the signal means.
#
# So the flows here are F01, F10, F12, F21: adjacent slot pairs, both
# directions, all pure functions of the window and all safely cacheable. The
# final pass picks which of them play which role from rts_mix, per output
# frame, reading cached fields rather than recomputing.
#
# The payoff beyond correctness is that the acceleration solve loses its phase
# dependence entirely. The anchor -- the frame with two outgoing flows inside
# the window -- is ALWAYS slot 1, whichever half of the interval the output
# sits in, so for uniform spacing
#
#     a = F10 + F12
#
# with no case analysis at all. The general VFR solve in the final pass
# reduces to it.
#
# This is also the shape that generalises. An N-frame window has N-1 adjacent
# slot pairs and fits a degree-(N-1) polynomial; nothing above is specific to
# three.
# ---------------------------------------------------------------------------
THREE_BINDS = "//!BIND HOOKED\n//!BIND FRAME1\n//!BIND FRAME2"


# ---------------------------------------------------------------------------
# Chunking: split the base into per-pass blocks, keeping each pass's banner
# comments and //!TEXTURE declarations attached to the pass they belong to.
# ---------------------------------------------------------------------------
def chunk(text):
    lines = text.split("\n")
    blocks, cur = [], []
    for ln in lines:
        # A //!TEXTURE decl always starts a new block; a //!HOOK starts one
        # unless the current block already holds a //!TEXTURE decl but no
        # //!HOOK yet (then the HOOK belongs to that decl's block).
        # A //!HOOK or //!TEXTURE line starts a new block unless the current
        # block holds //!TEXTURE decls and no //!HOOK yet: then a HOOK
        # attaches to those decls, and a further TEXTURE joins them (a pass
        # may own more than one storage texture).
        if ln.startswith("//!HOOK") or ln.startswith("//!TEXTURE"):
            has_tex = any(l.startswith("//!TEXTURE") for l in cur)
            has_hook = any(l.startswith("//!HOOK") for l in cur)
            starts = not (has_tex and not has_hook)
        else:
            starts = False
        if starts and cur:
            blocks.append(cur)
            cur = []
        cur.append(ln)
    if cur:
        blocks.append(cur)
    # Move each block's trailing banner (comment/blank lines after the last
    # code line) to the head of the next block, where it belongs.
    for i in range(len(blocks) - 1):
        b = blocks[i]
        j = len(b)
        while j > 0 and (b[j - 1].strip() == "" or b[j - 1].lstrip().startswith("//")):
            # Never peel back past directive lines.
            if b[j - 1].startswith("//!"):
                break
            j -= 1
        blocks[i + 1] = b[j:] + blocks[i + 1]
        del b[j:]
    return ["\n".join(b) for b in blocks]


def block_id(b):
    save = re.search(r"^//!SAVE (\S+)", b, re.M)
    desc = re.search(r"^//!DESC (.+)$", b, re.M)
    return (save.group(1) if save else None,
            desc.group(1).strip() if desc else None)


def inject_before_code(b, snippet):
    """Insert snippet after the last //! directive line of the block."""
    lines = b.split("\n")
    last = max(i for i, l in enumerate(lines) if l.startswith("//!"))
    return "\n".join(lines[:last + 1] + ["", snippet.rstrip()] + lines[last + 1:])


def main():
    text = SRC.read_text()
    assert "TIE_MARGIN" in text, "base shader lacks TIE_MARGIN -- wrong vintage?"

    # Drop the base's file-header comment block. It documents 2-frame
    # semantics ("mix_t = 0.0 (at HOOKED) .. 1.0 (at NEXT)") that are simply
    # false here, and carrying prose that contradicts the file it heads is
    # worse than not carrying it. This generator's own banner points readers
    # at the base for the shared machinery it still accurately describes.
    first = text.index("//!")
    text = text[first:]

    # SUB-PIXEL REFINEMENT IS A FIELD FEATURE, so it is off in the base and on
    # here. The base shader is a pure interpolator and fractional flow only
    # costs it resampling sharpness; this shader's product is the acceleration
    # field, where the integer lattice was the dominant error at low |a|. Both
    # halves of that are measured -- see the constant's comment in the base and
    # ACCEL_DEADBAND below, which pays back the warp cost this incurs.
    n_sub = text.count("const int SUBPEL_REFINE = 0;")
    assert n_sub == 2, f"expected 2 SUBPEL_REFINE sites in base, found {n_sub}"
    text = text.replace("const int SUBPEL_REFINE = 0;",
                        "const int SUBPEL_REFINE = 1;")

    blocks = chunk(text)
    hook_blocks = [b for b in blocks if "//!HOOK" in b]
    assert len(hook_blocks) == 24, f"expected 24 base passes, found {len(hook_blocks)}"

    out = []

    def find(save, desc_frag=None):
        cands = [b for b in blocks if block_id(b)[0] == save and
                 (desc_frag is None or desc_frag in (block_id(b)[1] or ""))]
        assert len(cands) == 1, f"lookup {save}/{desc_frag}: {len(cands)} matches"
        return cands[0]

    # -- per-block transforms, applied as we stream the file through --------
    for b in blocks:
        save, desc = block_id(b)
        nb = b

        # LUMA_A is slot 0 and the base already reads HOOKED, so its body is
        # correct unchanged. It only needs the extra binds that declare
        # frame_mix_count = 3.
        if save and re.fullmatch(r"LUMA_A_[SEQH]", save):
            nb = nb.replace("//!BIND HOOKED", THREE_BINDS)
            nb = nb.replace("[high] downsample frame A", "[tri] downsample slot 0")

        # LUMA_B is slot 1. The base reads NEXT, which for a 2-frame window
        # IS slot 1 -- here it has to be named explicitly. LUMA_C (slot 2) is
        # appended behind it.
        elif save and re.fullmatch(r"LUMA_B_[SEQH]", save):
            lvl = save[-1]
            nb = nb.replace("//!BIND NEXT", THREE_BINDS)
            nb = nb.replace("NEXT_tex(NEXT_pos)", "FRAME1_tex(HOOKED_pos)")
            nb = nb.replace("[high] downsample frame B", "[tri] downsample slot 1")
            div = dict(S=16, E=8, Q=4, H=2)[lvl]
            nb += f"""

//!HOOK FRAME_MIX
{THREE_BINDS}
//!SAVE LUMA_C_{lvl}
//!WIDTH HOOKED.w {div} /
//!HEIGHT HOOKED.h {div} /
//!COMPONENTS 1
//!DESC [tri] downsample slot 2 to 1/{div} res (luma)
vec4 hook() {{
    return vec4(dot(FRAME2_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}"""

        elif save == "SCENE_DIFF":
            # Base statistic is slots 0-1; add slots 1-2 behind it. Which is
            # the straddling pair and which is the "other" pair depends on the
            # output's phase, so the final pass picks -- but both are pure
            # functions of the window and therefore cacheable and stable.
            nb = nb.replace("[high] scene-cut statistic (whole-frame luma difference)",
                            "[tri] scene-cut statistic, slots 0-1")
            nb += """

//!HOOK FRAME_MIX
//!BIND LUMA_B_S
//!BIND LUMA_C_S
//!SAVE SCENE_DIFF_BC
//!WIDTH 1
//!HEIGHT 1
//!COMPONENTS 1
//!DESC [tri] scene-cut statistic, slots 1-2
vec4 hook() {
    const int N = 24;
    float acc = 0.0;
    for (int y = 0; y < N; y++) {
        for (int x = 0; x < N; x++) {
            vec2 uv = (vec2(float(x), float(y)) + 0.5) / float(N);
            acc += abs(LUMA_B_S_tex(uv).r - LUMA_C_S_tex(uv).r);
        }
    }
    return vec4(acc / float(N * N), 0.0, 0.0, 0.0);
}"""

        # EDGE_A/EDGE_B feed the texel-snap gate, which is inert while
        # SNAP_STRENGTH is 0.0. Kept in lockstep with the base and pinned to
        # slots 0-1 rather than made phase-dependent, since nothing reads
        # their output at present.
        elif save in ("EDGE_A", "EDGE_B"):
            nb = nb.replace("//!BIND HOOKED\n//!BIND NEXT", THREE_BINDS)
            nb = re.sub(r"\bNEXT_tex\(", "FRAME1_tex(", nb)
            nb = nb.replace("NEXT_pos", "HOOKED_pos")

        elif save == "FRAME_MIX":
            nb = FINAL_PASS  # replaced wholesale, banner included

        out.append(nb)

        # -- the two slot-1 <-> slot-2 chains, inserted after the base's --
        if save == "FLOW_H_BA" and desc and "pass 2" in desc:
            out.append(bc_chain(blocks, find))
            out.append(cb_chain(blocks, find))
            # Full-res level: lumas, then one F pass per pair per direction,
            # each seeded from the post-median H flow emitted above.
            out.append(fullres_luma("A", 0, "HOOKED", THREE_BINDS, "tri"))
            out.append(fullres_luma("B", 1, "FRAME1", THREE_BINDS, "tri"))
            out.append(fullres_luma("C", 2, "FRAME2", THREE_BINDS, "tri"))
            out.append(to_fullres(find("FLOW_H_AB", "refine"), "AB", "tri"))
            out.append(to_fullres(find("FLOW_H_BA", "refine"), "BA", "tri"))
            out.append(to_fullres(shift_slot(find("FLOW_H_AB", "refine"), "H", "BC"), "BC", "tri"))
            out.append(to_fullres(shift_slot(find("FLOW_H_BA", "refine"), "H", "CB"), "CB", "tri"))

    result = "\n".join(out)

    # -- assertions: nothing 2-frame-only survived --------------------------
    # Check CODE only: a comment may legitimately name mix_t to explain why
    # it is not used. A stale reference in code would silently read a
    # uniform the patch only fills in for num_mix == 2.
    code = "\n".join(l for l in result.split("\n")
                     if not l.lstrip().startswith("//"))
    for bad in ("BIND NEXT", "NEXT_tex(", "NEXT_pos", "NEXT_size", "NEXT_pt"):
        assert bad not in code, f"residual 2-frame reference in code: {bad}"
    assert not re.search(r"\bmix_t\b", code), \
        "mix_t survived in code -- it is only valid for num_mix == 2"
    hooks = result.count("//!HOOK")
    braces = result.count("{") - result.count("}")
    parens = result.count("(") - result.count(")")
    assert hooks == 48, f"expected 48 passes, got {hooks}"
    assert braces == 0 and parens == 0, f"unbalanced: braces {braces}, parens {parens}"
    header = HEADER
    if SRC.name != "bidirectional-interpolation.glsl":
        header = header.replace("bidirectional-interpolation.glsl", SRC.name)
        header = header.replace("//   ./tests/gen_tridirectional.py\n",
                                f"//   ./tests/gen_tridirectional.py {DST.name} {SRC.name}\n")
    DST.write_text(header + result, newline="\n")
    print(f"  {DST.name}: {hooks} passes "
          f"(24 base + 4 slot-2 lumas + 1 cut stat + 12 slot1<->slot2 flow "
          f"+ 3 full-res lumas + 4 full-res refines), braces/parens balanced  OK")


# ---------------------------------------------------------------------------
# The slot-1 <-> slot-2 flow chains. Textual copies of the base's slot-0 <->
# slot-1 chains with the luma pair shifted along by one. Everything else --
# search shape, TIE_MARGIN, regularisation, caching, medians -- is inherited
# verbatim, which is the point of generating rather than forking.
#
# These ARE cached, unlike the earlier role-based versions. A flow between
# two fixed slots is a pure function of the window, so `pair_changed` is
# exactly the right invalidation signal for it.
# ---------------------------------------------------------------------------
def bc_chain(blocks, find):
    """Slot 1 -> slot 2. The anchor's forward flow."""
    parts = ["""\
// =====================================================================
// SLOT 1 -> SLOT 2 flow chain ([tri], generated). The base's slot-0 -> slot-1
// chain with the luma pair shifted along by one; identical in every other
// respect. Together with the base's chains this gives all four adjacent-slot
// flows, from which the final pass reads whichever ones play the straddling
// and anchor roles for a given output frame.
// ====================================================================="""]
    for lvl, _ in LEVELS:
        b = find(f"FLOW_{lvl}_AB", None if lvl != "H" else "refine")
        parts.append(shift_slot(b, lvl, "BC"))
    for pn in ("pass 1", "pass 2"):
        b = find("FLOW_H_AB", pn)
        parts.append(shift_slot(b, "H", "BC"))
    return "\n\n".join(parts)


def cb_chain(blocks, find):
    """Slot 2 -> slot 1. The reverse, for round-trip validation."""
    parts = ["""\
// =====================================================================
// SLOT 2 -> SLOT 1 flow chain ([tri], generated). The reverse of the chain
// above, and it exists so the final pass can close a round trip on the
// anchor's forward flow. Without it that flow is the one field in the shader
// nothing checks, and an unchecked flow is indistinguishable from real
// acceleration -- which is how constant-velocity content was being warped.
// ====================================================================="""]
    for lvl, _ in LEVELS:
        b = find(f"FLOW_{lvl}_BA", None if lvl != "H" else "refine")
        parts.append(shift_slot(b, lvl, "CB"))
    for pn in ("pass 1", "pass 2"):
        b = find("FLOW_H_BA", pn)
        parts.append(shift_slot(b, "H", "CB"))
    return "\n\n".join(parts)


def shift_slot(b, lvl, tag):
    """Shift a base flow pass one slot later: A->B becomes B->C.

    LUMA_B must be rewritten before LUMA_A, or the first substitution's
    output is eaten by the second.
    """
    nb = b
    nb = re.sub(rf"\bLUMA_B_{lvl}_tex\(", "__C__(", nb)
    nb = re.sub(rf"\bLUMA_A_{lvl}_tex\(", "__B__(", nb)
    nb = nb.replace("__C__(", f"LUMA_C_{lvl}_tex(")
    nb = nb.replace("__B__(", f"LUMA_B_{lvl}_tex(")
    # LUMA_A's bind STAYS even though no _tex read of it survives: the pass
    # body still uses LUMA_A_*_pt / _pos / _size for texel geometry, and
    # those identifiers only exist if the texture is bound. Removing the bind
    # produced a shader that failed to load, whereupon libplacebo silently
    # fell back to its builtin mixer and every case scored near `linear`.
    nb = nb.replace(f"//!BIND LUMA_B_{lvl}",
                    f"//!BIND LUMA_B_{lvl}\n//!BIND LUMA_C_{lvl}")
    # Same-direction flow references take the pair tag; a CROSS-direction
    # reference (the reverse flow, used for a round-trip check) takes the
    # reversed tag. The block's own direction is read from its //!SAVE line.
    own = "BA" if re.search(r"^//!SAVE FLOW_[SEQH]_BA", nb, re.M) else "AB"
    other = "BA" if own == "AB" else "AB"
    nb = re.sub(rf"FLOW_([SEQH])_{other}", rf"FLOW_\1_{tag[::-1]}", nb)
    nb = re.sub(rf"FLOW_([SEQH])_{own}", rf"FLOW_\1_{tag}", nb)
    nb = nb.replace("flow A->B", "flow slot1->slot2")
    nb = nb.replace("flow B->A", "flow slot2->slot1")
    nb = nb.replace("flow search A->B", "flow search slot1->slot2")
    nb = nb.replace("flow search B->A", "flow search slot2->slot1")
    nb = nb.replace("[high]", "[tri]")
    return nb


# ---------------------------------------------------------------------------
# THE FULL-RESOLUTION LEVEL (T1.2) -- a FIELD feature, like sub-pixel
# refinement, and absent from the base shader for the same reason: the pure
# interpolator gains little from flows finer than its warp can express, while
# the acceleration/jerk fields inherit every halving of the flow quantum
# twice. The 2x-content probe measured the prize (error roughly halves at
# every low-band sample) -- with one honest caveat, pre-registered: the probe
# scaled the CONTENT, which preserves the SAD aperture's relative context,
# whereas a real full-res level halves it. If the level under-delivers
# against the probe, the aperture is the named suspect.
#
# Construction: the H refine pass, transformed one level down. Seeded from
# the POST-MEDIAN H flow (the medians stay at H -- full-res medians would be
# the most expensive passes in the shader, and the isolated-false-match
# problem they exist for is already solved before the seed is handed over);
# radius-2 search with the same tie-breaking, regularisation toward the seed,
# and the equiangular sub-pixel fit, now on a 1-px lattice. Storage-cached
# like every other level. The ladder and the frame clock judge whether the
# unfiltered final level costs anything the medians were hiding.
# ---------------------------------------------------------------------------
def fullres_luma(letter, slot_index, frame_tex, binds, tag):
    return f"""\
//!HOOK FRAME_MIX
{binds}
//!SAVE LUMA_{letter}_F
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!COMPONENTS 1
//!DESC [{tag}] slot {slot_index} luma at full res
vec4 hook() {{
    return vec4(dot({frame_tex}_tex(HOOKED_pos).rgb, vec3(0.299, 0.587, 0.114)), 0, 0, 0);
}}"""


def to_fullres(h_block, pair, tag):
    """Transform an H-level refine pass (already slot-shifted if needed)
    into the full-res pass for the same pair: save/cache one level down,
    seed from the post-median H flow, full-res lumas, full-res geometry."""
    nb = h_block
    nb = nb.replace(f"FLOW_H_{pair}", f"FLOW_F_{pair}")   # save + cache + stores
    nb = nb.replace(f"FLOW_Q_{pair}", f"FLOW_H_{pair}")   # seed: one level up
    nb = re.sub(r"\bLUMA_([A-D])_H", r"LUMA_\1_F", nb)
    nb = nb.replace("3x3_h", "3x3_f")
    # WIDEN THE SAD APERTURE to 5x5 at this level only. The first F build
    # kept the H pass's 3x3, and the field regressed exactly where the
    # aperture hypothesis predicted: a full-res 3x3 spans a third of the
    # pattern context the H-level 3x3 does, and on smooth texture with small
    # displacement the valley flattens and the estimate scatters (measured:
    # A4 f6 4.3% -> 18.3% with the 3x3). The sum is scaled to 3x3-equivalent
    # so REFINE_REG_LAMBDA keeps its meaning; TIE_MARGIN is relative and
    # unaffected. The contrast gate's window is left alone (inert anyway).
    nb = re.sub(
        r"float sad3x3_f(2?)\(vec2 (\w+), vec2 (\w+)\) \{\n"
        r"    float s = 0\.0;\n"
        r"    for \(int y = -1; y <= 1; y\+\+\) \{\n"
        r"        for \(int x = -1; x <= 1; x\+\+\) \{",
        "float sad5x5_f\\1(vec2 \\2, vec2 \\3) {\n"
        "    float s = 0.0;\n"
        "    for (int y = -2; y <= 2; y++) {\n"
        "        for (int x = -2; x <= 2; x++) {",
        nb)
    nb = nb.replace("sad3x3_f", "sad5x5_f")
    # Scale the widened sum back to 3x3-equivalent magnitude.
    nb = re.sub(r"(float sad5x5_f2?\(.*?\n)(    \}\n    return s;)",
                lambda m: m.group(1) + "    }\n    return s * (9.0 / 25.0);",
                nb, flags=re.S)
    nb = nb.replace("//!WIDTH HOOKED.w 2 /", "//!WIDTH HOOKED.w")
    nb = nb.replace("//!HEIGHT HOOKED.h 2 /", "//!HEIGHT HOOKED.h")
    nb = nb.replace("(half res)", "(full res)")
    nb = re.sub(r"\[(high|tri|quad)\] refine", f"[{tag}] refine", nb)
    # Keep the seed-snapping comment honest after the renames.
    nb = nb.replace("the Q->H handoff", "the H->F handoff")
    nb = nb.replace("own texel is 4 full-res px", "own texel is 2 full-res px")
    nb = nb.replace("smear a real boundary across ~4px",
                    "smear a real boundary across ~2px")
    nb = nb.replace("every direction (~8px total)", "every direction (~4px total)")
    return nb


# ---------------------------------------------------------------------------
FINAL_PASS = """\
// ---------------------------------------------------------------------
// Final pass: TRIDIRECTIONAL warp -- quadratic (constant-acceleration)
// placement, full resolution.
//
// The bidirectional warp assumes constant velocity across the straddling
// interval: content moves f*s by output time s. Three frames determine a
// quadratic, and the constant-acceleration trajectory through them puts
// the straddling frames' content at
//
//     d(s) = f*s - (a/2)*s*(1-s)
//
// -- the linear warp plus a correction that vanishes at both endpoints
// and peaks at a/8 mid-interval. Both warp directions get the same
// +(a/2)*s*(1-s) term on their sample position (it is one trajectory
// bowing, seen from either end). At a = 0 this pass IS the bidirectional
// final pass, exactly -- that is both the safety property and the null
// hypothesis the benchmarks test.
//
// EVERYTHING READ HERE IS SLOT-KEYED. The four flows are between fixed
// adjacent slots, so they are pure functions of the window and the base's
// caching is valid for them unmodified. This pass is the only place that
// knows about ROLES, and it derives them per output frame from rts_mix
// without recomputing anything.
//
// WARP ON H, MEASURE ON F -- the two use cases split a third time (after
// the deadband and the sub-pixel default). The full-res flows are the
// finest measurement and feed the ESTIMATOR; the WARP keeps the mediated
// half-res flows, because the first full-res build fed them to both and
// the picture paid 2.95 dB on L1 -- the unfiltered final level moves
// pixels on scatter the medians used to remove, while the field's
// consumers never wanted the medians' smoothing in the first place.
// ---------------------------------------------------------------------
//!HOOK FRAME_MIX
//!BIND HOOKED
//!BIND FRAME1
//!BIND FRAME2
//!BIND SCENE_DIFF
//!BIND SCENE_DIFF_BC
//!BIND FLOW_H_AB
//!BIND FLOW_H_BC
//!BIND FLOW_F_AB
//!BIND FLOW_F_BA
//!BIND FLOW_F_BC
//!BIND FLOW_F_CB
//!BIND EDGE_A
//!BIND EDGE_B
//!SAVE FRAME_MIX
//!WIDTH HOOKED.w
//!HEIGHT HOOKED.h
//!DESC [tri] motion-compensated warp (quadratic placement)

// Texel snap and its edge-consistency gate: carried over from the base
// final pass unchanged (SNAP_STRENGTH is 0.0 there and stays 0.0 here, so
// both warps currently degenerate to plain bilinear -- kept for lockstep,
// see the base shader for the full history of this mechanism).
vec2 snap_texel(vec2 uv, vec2 size) {
    return (floor(uv * size) + 0.5) / size;
}

float edge_consistency(float expected, float snapped) {
    return 1.0 - abs(expected - snapped);
}

const float SNAP_STRENGTH = 0.0;

// Same value and reasoning as the base shader's gate (see its final pass).
const float SCENE_CUT_DIFF = 0.125;

// Acceleration clamp, in full-res px per straddle-interval^2. A physical
// bound, not a tuning knob: sustained acceleration beyond a few px/frame^2
// exits the search's ~23px/frame reach within a handful of frames (see the
// O-series calibration in tests/scenes.sh), and the oscillation ladder tops
// out at ~13. Anything much past that is estimation noise, so it is clamped
// and the shader degrades toward bidirectional behaviour instead of warping
// on noise. A reasoned starting value, not yet a measured optimum.
const float ACCEL_MAX_PX = 16.0;

// Acceleration is a SMALL RESIDUAL of two large, near-cancelling flows: under
// smooth motion the anchor's two outgoing flows point opposite ways and
// mostly cancel, and what survives is the acceleration. A gate is not
// optional -- ungated, this shader lost 13.7 dB on L1_trans_8px, a pure
// constant-velocity case where the true acceleration is exactly zero and it
// should have been a no-op.
//
// The first gate tried rejected by MAGNITUDE -- large |a| relative to the
// flows means they failed to cancel, so distrust it. That cannot work, and
// why is the central difficulty here. Two completely different things stop
// the flows cancelling:
//
//   OCCLUSION: one flow matched unrelated content. The residual is junk.
//   REVERSAL:  the object genuinely turned around. Both flows are good
//              matches pointing the same way, and the residual is the
//              largest, most REAL acceleration in the scene.
//
// A magnitude ratio drives toward 1 in both, so it discarded the signal
// exactly where it was strongest -- the fingerprint being that the gain FELL
// as acceleration rose, when the model should help more. Round-trip
// consistency separates them cleanly, because a reversal round-trips
// perfectly and an occlusion cannot. Judge the answer's provenance, not its
// size. Worth up to +4.4 dB. Thresholds in px of round-trip error; swept.
const float ACCEL_TRUST_LO = 2.0;
const float ACCEL_TRUST_HI = 5.0;

// DEADBAND on the acceleration used for the WARP -- deliberately not on the
// field the diagnostics report, because the two use cases want different
// things from the same number. A sensing consumer wants what was measured; an
// interpolator wants only what is safe to move pixels with.
//
// Why it is needed at all: sub-pixel refinement lifted the flow off the
// integer lattice, which is what made the field usable at low |a| -- but on
// content whose true acceleration is exactly zero the field still carries a
// heavy tail (measured on L7, constant velocity: median 0.000, p90 0.277,
// p99 3.914 px/interval^2). The correction acts on that tail and warps on
// noise. With sub-pixel enabled and no deadband it cost 0.82 dB on
// L1_trans_8px beyond the warp's own resampling cost.
//
// Expressed in px/interval^2 so it can be read against the calibration
// directly. Zero disables it.
//
// SWEPT, and 0.5/1.5 is the knee. On L1_trans_8px, where the true
// acceleration is exactly zero and the shader must be a no-op:
//
//   deadband      L1      O1      O2      O4      O5
//   off        56.16   49.65   46.17   47.35   34.03
//   0.25/0.75  58.21   49.62   46.17   47.35   34.03
//   0.5 /1.5   60.77   49.44   46.19   47.36   34.03
//   1.0 /2.5   61.35   49.06   46.16   47.33     --
//
// L1 climbs 5.2 dB across the sweep while the oscillation cases -- where the
// acceleration is real and the correction is earning its place -- move by
// hundredths until the widest setting finally costs O1 0.6 dB. 0.5/1.5 takes
// nearly all of the recovery for 0.21 dB of it.
//
// Against the pre-sub-pixel shader this is +3.31 dB on L1, which closes the
// -3.80 dB L1 regression that stood as the tridirectional shader's only
// losing case. Suppressing corrections below ~1 px/interval^2 costs at most
// a/8 ~ 0.12 px of placement error, which is not a visible amount.
const float ACCEL_DEADBAND_LO = 0.5;
const float ACCEL_DEADBAND_HI = 1.5;

// TRI_DIAG -- in-shader diagnostic output, for reading the estimator's
// internal fields without building a separate visualiser (tests/trivis.py is
// the full four-panel instrument).
//
//   0 = normal interpolated output
//   1 = the quadratic CORRECTION, i.e. how far this texel is being moved off
//       the constant-velocity straight line, in px
//   2 = the ACCELERATION field, in px per interval^2
//   3 = acceleration MAGNITUDE as a heat map, auto-scaled to ACCEL_DIAG_FS
//   4 = acceleration magnitude as LINEAR LUMA -- a measurement mode, so a
//       whole-frame average is proportional to mean |a|. No marker.
//
// Modes 1 and 2 encode a 2D vector the way tests/flowvis.py does: R and G
// carry the x and y components around a mid-grey zero, so mid-grey means
// "nothing here" and the hue tells you the direction. Mode 3 discards
// direction and shows only magnitude, which is easier to read when the
// question is "is there any acceleration in this shot at all".
//
// A MODE MARKER is burned into the top-left corner whenever TRI_DIAG is
// non-zero: a solid colour block, one colour per mode. It exists because the
// honest failure mode of these diagnostics is a screen of near-uniform
// mid-grey that looks identical to "the switch did nothing" -- and on real
// footage that is the COMMON case, since ordinary camera motion carries far
// less acceleration than the synthetic ladder does. With the marker, "mode is
// active but the field is near zero" and "my edit did not take effect" stop
// looking the same.
const int TRI_DIAG = 0;

// Full-scale values for the diagnostic encodings, in real units, so a reader
// can convert a pixel back to a number rather than guess.
//
// These are deliberately far more sensitive than the synthetic ladder needs.
// The ladder reaches 13 px/interval^2; ordinary camera motion is one to two
// orders of magnitude below that, and the first version of these constants
// was calibrated on the ladder and rendered real footage invisible -- mode 1
// deviated by ONE level out of 255. Set for the content you are looking at:
// raise for synthetic tests, lower to see subtle real motion.
const float ACCEL_DIAG_FS = 2.0;   // px/interval^2 at full scale (modes 2, 3)
const float CORR_DIAG_FS  = 0.25;  // px of correction at full scale (mode 1)

// Mode marker: a solid block in the top-left corner, 24px square.
vec4 tri_diag_marker() {
    if (TRI_DIAG == 1) return vec4(1.0, 0.2, 0.2, 1.0);   // red   -- correction
    if (TRI_DIAG == 2) return vec4(0.2, 0.6, 1.0, 1.0);   // blue  -- acceleration
    return vec4(0.2, 1.0, 0.3, 1.0);                      // green -- magnitude
}

vec4 hook() {
    // ---- roles, derived per output frame from slot-keyed fields ----
    // rts_mix[1] > 0 means slot 1 is still in the future, so the output sits
    // in the FIRST interval (slots 0-1). Otherwise it sits in the second.
    bool first_half = rts_mix[1] > 0.0;

    float tA = first_half ? rts_mix[0] : rts_mix[1];
    float tB = first_half ? rts_mix[1] : rts_mix[2];
    float L  = tB - tA;                       // straddle interval, > 0
    float s  = clamp((0.0 - tA) / L, 0.0, 1.0);

    // Straddling flow: slots 0-1 or slots 1-2.
    vec2 f_fwd = (first_half ? FLOW_H_AB_tex(HOOKED_pos).xy
                             : FLOW_H_BC_tex(HOOKED_pos).xy) * 2.0 * HOOKED_pt;

    // Cut inside the straddling pair: reproduce the cut (base behaviour).
    float cut_straddle = first_half ? SCENE_DIFF_tex(vec2(0.5)).r
                                    : SCENE_DIFF_BC_tex(vec2(0.5)).r;
    if (cut_straddle > SCENE_CUT_DIFF) {
        if (first_half)
            return s < 0.5 ? HOOKED_tex(HOOKED_pos) : FRAME1_tex(HOOKED_pos);
        return s < 0.5 ? FRAME1_tex(HOOKED_pos) : FRAME2_tex(HOOKED_pos);
    }

    // ---- acceleration: the anchor is ALWAYS slot 1 ----
    // Whichever half the output sits in, slot 1 is the frame with two
    // outgoing flows inside the window, so the solve has no phase
    // dependence at all. f10 and f12 are its flows toward slots 0 and 2.
    vec2 f10 = FLOW_F_BA_tex(HOOKED_pos).xy * HOOKED_pt;
    vec2 f12 = FLOW_F_BC_tex(HOOKED_pos).xy * HOOKED_pt;

    // Quadratic through slot 1's three sampled positions, in units of the
    // straddle interval. For uniform spacing tau0 = -1 and tau2 = +1, and
    // this reduces to a = f10 + f12: the two flows cancel under constant
    // velocity and whatever survives IS the acceleration. Written out in
    // full so non-uniform (VFR) spacing is exact rather than assumed away.
    float tau0 = (rts_mix[0] - rts_mix[1]) / L;
    float tau2 = (rts_mix[2] - rts_mix[1]) / L;
    vec2 accel = 2.0 * (f12 * tau0 - f10 * tau2)
               / (tau2 * tau0 * (tau2 - tau0));

    // A cut between slot 1 and the far slot does not stop the straddling
    // pair being blendable -- it only makes the acceleration meaningless. So
    // zero it and degrade exactly to bidirectional, rather than cutting.
    float cut_far = first_half ? SCENE_DIFF_BC_tex(vec2(0.5)).r
                               : SCENE_DIFF_tex(vec2(0.5)).r;
    if (cut_far > SCENE_CUT_DIFF)
        accel = vec2(0.0);

    // ---- confidence: round-trip BOTH of the anchor's flows ----
    // Follow each flow out and back. Content visible in both frames lands
    // where it started; occluded content does not. Both are checked at slot
    // 1's own grid, and the worse of the two decides -- a texel has to
    // survive both to be believed, because the acceleration is built from
    // both and either being wrong is enough to ruin it.
    vec2 r10 = FLOW_F_AB_tex(HOOKED_pos + f10).xy * HOOKED_pt;
    float rt10 = length(f10 + r10) / length(HOOKED_pt);

    vec2 r12 = FLOW_F_CB_tex(HOOKED_pos + f12).xy * HOOKED_pt;
    float rt12 = length(f12 + r12) / length(HOOKED_pt);

    accel *= 1.0 - smoothstep(ACCEL_TRUST_LO, ACCEL_TRUST_HI, max(rt10, rt12));

    // NO SPANNING slot-0 -> slot-2 TEST, and this is a proof rather than an
    // omission. It was built (6 passes) and measured, on the reasoning that
    // the triangle identity d01 + d12 == d02 checks the measurements against
    // each other. Count the degrees of freedom: three frames give TWO unknown
    // displacements and THREE measurements, so exactly ONE redundancy -- and
    // the identity spends it constraining the SUM. Acceleration is the
    // DIFFERENCE. Orthogonal, so the constraint cannot touch it. A
    // common-mode error, which is what a moving edge produces, is invisible
    // to it by construction. Measured: weighting that residual 20x recovered
    // 0.09 dB on L1 while costing 2.59 dB on O2 -- anti-correlated with its
    // purpose. Validating acceleration needs a FOURTH frame; see
    // TRIDIRECTIONAL.md.

    vec2 amax = ACCEL_MAX_PX * HOOKED_pt;
    accel = clamp(accel, -amax, amax);

    // ---- quadratic placement: linear warp plus the s(1-s) correction ----
    // The warp's copy of the acceleration, deadbanded; `accel` itself is left
    // alone so TRI_DIAG still reports the measurement rather than the gate.
    vec2 accel_w = accel;
    if (ACCEL_DEADBAND_HI > 0.0)
        accel_w *= smoothstep(ACCEL_DEADBAND_LO, ACCEL_DEADBAND_HI,
                              length(accel / HOOKED_pt));

    vec2 corr = 0.5 * accel_w * s * (1.0 - s);

    if (TRI_DIAG != 0) {
        // Mode 4 is a MEASUREMENT mode, not an eyeball mode: |a| as linear
        // luma, so a whole-frame average is directly proportional to the mean
        // acceleration in the frame and the field can be reduced to one
        // number per frame by signalstats. No marker, deliberately -- a
        // 24x24 patch would bias that average, and nothing downstream is
        // looking at it by eye.
        if (TRI_DIAG == 4)
            return vec4(vec3(clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS,
                                   0.0, 1.0)), 1.0);

        // Mode marker first, so an active-but-empty diagnostic is never
        // mistaken for an edit that did not take effect.
        if (HOOKED_pos.x < 24.0 * HOOKED_pt.x && HOOKED_pos.y < 24.0 * HOOKED_pt.y)
            return tri_diag_marker();

        if (TRI_DIAG == 1)
            return vec4(0.5 + (corr / HOOKED_pt) * (0.5 / CORR_DIAG_FS), 0.5, 1.0);
        if (TRI_DIAG == 2)
            return vec4(0.5 + (accel / HOOKED_pt) * (0.5 / ACCEL_DIAG_FS), 0.5, 1.0);

        // Mode 3: magnitude only, blue -> cyan -> red across 0..ACCEL_DIAG_FS.
        float m = clamp(length(accel / HOOKED_pt) / ACCEL_DIAG_FS, 0.0, 1.0);
        vec3 c = m < 0.5 ? mix(vec3(0.0, 0.0, 0.25), vec3(0.0, 0.9, 0.9), m * 2.0)
                         : mix(vec3(0.0, 0.9, 0.9), vec3(1.0, 0.1, 0.0), (m - 0.5) * 2.0);
        return vec4(c, 1.0);
    }

    vec2 uv_a = HOOKED_pos - f_fwd * s + corr;
    vec2 uv_b = HOOKED_pos + f_fwd * (1.0 - s) + corr;

    vec4 sa = first_half ? HOOKED_tex(uv_a) : FRAME1_tex(uv_a);
    vec4 sb = first_half ? FRAME1_tex(uv_b) : FRAME2_tex(uv_b);

    // Snap gate, inert at SNAP_STRENGTH 0.0 but kept in lockstep with the
    // base. EDGE_A/EDGE_B are pinned to slots 0-1 (see their passes).
    vec2 sa_uv = snap_texel(uv_a, HOOKED_size);
    vec2 sb_uv = snap_texel(uv_b, HOOKED_size);
    float ea = edge_consistency(EDGE_A_tex(uv_a).r, EDGE_A_tex(sa_uv).r);
    float eb = edge_consistency(EDGE_B_tex(uv_b).r, EDGE_B_tex(sb_uv).r);
    sa = mix(sa, first_half ? HOOKED_tex(sa_uv) : FRAME1_tex(sa_uv),
             SNAP_STRENGTH * ea);
    sb = mix(sb, first_half ? FRAME1_tex(sb_uv) : FRAME2_tex(sb_uv),
             SNAP_STRENGTH * eb);

    return mix(sa, sb, s);
}"""

HEADER = """\
// =====================================================================
// GENERATED FILE -- DO NOT EDIT BY HAND.
//
// Produced by scripts/tests/gen_tridirectional.py from
// bidirectional-interpolation.glsl. Edit the base (shared machinery) or
// the generator (everything [tri]-tagged) and regenerate:
//
//   ./tests/gen_tridirectional.py
//
// TRIDIRECTIONAL INTERPOLATION -- the experiment this file exists for.
// A 2-frame shader can only encode constant velocity, so it places an
// inserted frame's content at the constant-velocity midpoint -- wrong by
// a/8 px under acceleration a. This shader binds THREE frames (the
// straddling pair plus the temporally nearest outer frame), estimates a
// third flow field from the anchor to that outer frame, solves per-texel
// acceleration from the anchor's two outgoing flows, and places content
// on the quadratic trajectory instead of the straight line. With zero
// estimated acceleration it degenerates exactly to the bidirectional
// shader. Hypothesis, algebra, calibration and results: TRIDIRECTIONAL.md.
// Everything below this banner up to the [tri]-tagged passes is the
// bidirectional base, transformed only in how it reads its source frames.
// =====================================================================

"""


if __name__ == "__main__":
    main()
