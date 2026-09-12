#!/usr/bin/env python3
"""Translate an mpv-hook shader into per-pass Metal compute shaders.

    ./gen_metal.py <hook.glsl> <outdir> [--compile]

Parses the //! directive structure (HOOK/BIND/SAVE/WIDTH/HEIGHT/
COMPONENTS/DESC/WHEN pass blocks; TEXTURE/SIZE/FORMAT/STORAGE texture
blocks; PARAM/DESC/TYPE/MINIMUM/MAXIMUM parameter blocks), wraps each
`vec4 hook()` body as a standalone GLSL compute shader with the implicit
mpv API shimmed, and emits:

    <outdir>/NN_<save>.comp      one standalone GLSL pass each
    <outdir>/graph.json          the pass graph a host executes:
                                 textures, binds in binding order,
                                 size expressions, components, the
                                 window (frames), the parameters, and
                                 each pass's WHEN condition
    <outdir>/NN_<save>.metal     with --compile: glslc + spirv-cross

The GLSL source stays the single source of truth (METALPORT.md): the
output of this tool is generated material, regenerated after any shader
edit, never hand-edited. Proven by the P0 spike (metal-demo/spike/):
this road preserves semantics, not just syntax -- the real coarse-flow
pass recovered a known motion on 99.3% of texels after translation.

Shim contract (must match the host in metal-demo/):
  - buffer(0), std140: vec2 out_size; vec2 <NAME>_size_u per sampled
    bind in bind order; vec4 rts_pack[2] (rts_mix packed to dodge the
    std140 float-array stride trap -- P0 lesson 2); int pair_changed;
    THEN (since 2026-09-08) float mix_t_u and one scalar per //!PARAM in
    declaration order, 4 bytes each, listed in graph.json under
    "uniforms": the host writes them after pair_changed at 4-byte
    stride. mix_t is the two-frame family's phase (HOOKED..NEXT); the
    host computes it from the window (0 for N > 2 shaders, which use
    rts_mix). A //!PARAM becomes a uniform of its own name and type, as
    libplacebo does, so the body's `read_view == 1` reads it directly.
    num_mix (the frames in the mix) is a compile-time constant equal to
    the window, not a uniform: this host always delivers a full window
    or falls back to hold.
  - texture indices in MSL follow GLSL binding order: sampled binds
    first (in //!BIND order), storage binds next, the SAVE target last.
    spirv-cross's entry point is main0; its signature is the authority
    if in doubt (P0 lesson 1).
  - gl_FragCoord is shimmed as a macro over a global set to
    vec4(gid + 0.5, 0, 1): the fused passes of the propagated family
    write their flow cache at that coordinate, and in the fragment path
    it is the pass's own output pixel. NOTE the consequence for a host
    that can resize: a //!STORAGE texture has a FIXED //!SIZE, and the
    family's are sized for a 3840x2160 SOURCE at each pyramid level's
    divisor (S/16 = 240x135, E/8 = 480x270, Q/4 = 960x540, H/2 =
    1920x1080; MODE_MEM 1440x270 = E with three candidate slots). So any
    working size up to 4K fits every shader, and ABOVE 4K the caches
    truncate silently. (The -4k variants are a different matter: they
    scale the shader's pixel-space CONSTANTS so its judgement is the same
    fraction of the screen -- scale_shader.py -- not its storage.)
    graph.json's textures carry the sizes; a host that resizes should
    compare them against its working size and say so rather than
    truncate.
  - <NAME>_pos for every bind is the same normalized output position,
    which is what libplacebo's shared-uv sampling means at matched
    aspect. Sizes/pt are per-bind.
  - frame binds: HOOKED is slot 0; the two-frame family's NEXT is slot 1;
    FRAMEk is slot k. graph.json's "window" is the number of frames the
    shader needs (2, 3, 4, 5 or 6 in this family); the host's window
    must be built from it, not assumed to be four.
  - //!WHEN <rpn> on a pass (the human-reading tail: `read_view 0 >`)
    is evaluated by the HOST each frame from the current parameter
    values (RPN over numbers, parameter names and + - * / > < = !),
    and a false pass is SKIPPED: not dispatched, its SAVE not flipped.
    graph.json carries it as "when_rpn" (null when absent). The tail's
    passes are all gated, and the tail's last pass re-saves FRAME_MIX,
    so with read_view = 0 the picture is the shader's own.

The traps this encodes: a `//!` line ALWAYS terminates a body (bodies
comment with plain //); WIDTH/HEIGHT are RPN over HOOKED.w/h and
literals, evaluated by the HOST, carried symbolically here; SAVE names
never collide with STORAGE names in this shader family -- asserted, so
a future edit that breaks that assumption fails loudly here instead of
silently misbinding; a //!PARAM block's //!DESC is the parameter's, not
a pass's, so the state machine tracks which block it is in.
"""
import json
import pathlib
import re
import subprocess
import sys

if len(sys.argv) < 3:
    sys.exit(__doc__.strip().splitlines()[2].strip())

src_path = pathlib.Path(sys.argv[1])
outdir = pathlib.Path(sys.argv[2])
do_compile = "--compile" in sys.argv
outdir.mkdir(parents=True, exist_ok=True)

lines = src_path.read_text().splitlines()

textures = {}   # name -> {w,h,format,storage}
passes = []     # {hook,binds,save,width,height,components,desc,when,body}
params = []     # {name,type,desc,min,max,default}

i = 0
cur = None      # current pass being accumulated
mode = None     # None | 'pass_directives' | 'pass_body' | 'texture' | 'param'
tex = None
prm = None

def close_pass():
    global cur, mode
    if cur is not None:
        cur["body"] = "\n".join(cur["body"]).rstrip() + "\n"
        # A pass with no //!SAVE overwrites the texture it hooked (libplacebo's default). Name it, so
        # the graph never carries a null save: the host keys its ping-pong pair by this name, and a
        # Swift `let save: String` cannot decode null at all.
        if cur["save"] is None:
            cur["save"] = cur["hook"]
        passes.append(cur)
    cur = None
    mode = None

while i < len(lines):
    ln = lines[i]
    if ln.startswith("//!"):
        parts = ln[3:].split()
        key = parts[0] if parts else ""
        if key == "HOOK":
            close_pass()
            cur = {"hook": parts[1], "binds": [], "save": None,
                   "width": None, "height": None, "components": 4,
                   "desc": "", "when": None, "body": []}
            mode = "pass_directives"
        elif key == "TEXTURE":
            close_pass()
            tex = {"name": parts[1], "w": None, "h": None,
                   "format": None, "storage": False}
            textures[parts[1]] = tex
            mode = "texture"
        elif key == "PARAM":
            close_pass()
            prm = {"name": parts[1], "type": None, "desc": "",
                   "min": None, "max": None, "default": None}
            params.append(prm)
            mode = "param"
        elif mode == "texture":
            if key == "SIZE":
                tex["w"], tex["h"] = int(parts[1]), int(parts[2])
            elif key == "FORMAT":
                tex["format"] = parts[1]
            elif key == "STORAGE":
                tex["storage"] = True
            else:
                sys.exit(f"line {i+1}: unknown TEXTURE directive {key}")
        elif mode == "param":
            if key == "DESC":
                prm["desc"] = " ".join(parts[1:])
            elif key == "TYPE":
                prm["type"] = parts[1]
            elif key == "MINIMUM":
                prm["min"] = float(parts[1])
            elif key == "MAXIMUM":
                prm["max"] = float(parts[1])
            else:
                sys.exit(f"line {i+1}: unknown PARAM directive {key}")
        elif cur is not None:
            if key == "BIND":
                cur["binds"].append(parts[1])
            elif key == "SAVE":
                cur["save"] = parts[1]
            elif key == "WIDTH":
                cur["width"] = parts[1:]
            elif key == "HEIGHT":
                cur["height"] = parts[1:]
            elif key == "COMPONENTS":
                cur["components"] = int(parts[1])
            elif key == "DESC":
                cur["desc"] = " ".join(parts[1:])
            elif key == "WHEN":
                cur["when"] = parts[1:]
            else:
                sys.exit(f"line {i+1}: unknown pass directive {key}")
            mode = "pass_directives"
        else:
            sys.exit(f"line {i+1}: directive {key} outside any block")
    else:
        if mode in ("pass_directives", "pass_body"):
            mode = "pass_body"
            cur["body"].append(ln)
        elif mode == "texture" and ln.strip() == "":
            mode = None
        elif mode == "param":
            s = ln.strip()
            if s == "":
                if prm["default"] is None:
                    sys.exit(f"line {i+1}: PARAM {prm['name']} has no default value line")
                mode = None
            elif prm["default"] is None:
                prm["default"] = float(s)
            else:
                sys.exit(f"line {i+1}: unexpected text in PARAM {prm['name']}: {s}")
        # content outside blocks (file header comments) is dropped
    i += 1
close_pass()

for p in params:
    if p["type"] not in ("int", "float"):
        sys.exit(f"PARAM {p['name']}: unsupported type {p['type']} (int or float)")
    if p["default"] is None:
        sys.exit(f"PARAM {p['name']}: no default")

storage_names = {n for n, t in textures.items() if t["storage"]}
save_names = {p["save"] for p in passes if p["save"]}
overlap = storage_names & save_names
assert not overlap, f"SAVE/STORAGE overlap breaks the shim contract: {overlap}"

FRAME_BINDS = {"HOOKED": 0, "NEXT": 1, "FRAME1": 1, "FRAME2": 2, "FRAME3": 3,
               "FRAME4": 4, "FRAME5": 5, "FRAME6": 6, "FRAME7": 7}
frames_used = {b for p in passes for b in p["binds"] if b in FRAME_BINDS}
window = 1 + max((FRAME_BINDS[b] for b in frames_used), default=0)
param_names = {p["name"] for p in params}

def check_when(rpn):
    """the host's evaluator, run here so an unsupported token fails at generation, not on the Mac"""
    if rpn is None:
        return
    st = 0
    for tok in rpn:
        if tok in param_names or tok in ("+", "-", "*", "/", ">", "<", "=", "!"):
            st += 1 if tok in param_names else (0 if tok == "!" else -1)
        else:
            float(tok); st += 1
        if st < 1:
            sys.exit(f"WHEN {rpn}: stack underflow at {tok}")
    if st != 1:
        sys.exit(f"WHEN {rpn}: leaves {st} values")

for p in passes:
    check_when(p["when"])

import hashlib as _hashlib
graph = {"source": src_path.name,
         # the GLSL this graph was made from, so a host can tell a stale graph from a fresh one
         # (the lockstep check, 2026-09-12: the app once ran old graphs after a re-tail, silently)
         "source_sha256": _hashlib.sha256(src_path.read_bytes()).hexdigest(),
         "window": window,
         "frames": sorted(frames_used, key=lambda b: FRAME_BINDS[b]),
         "textures": [], "passes": [],
         "uniforms": [{"name": "mix_t", "type": "float"}] +
                     [{"name": p["name"], "type": p["type"], "default": p["default"],
                       "min": p["min"], "max": p["max"], "desc": p["desc"]} for p in params]}
for n, t in sorted(textures.items()):
    graph["textures"].append({"name": n, "w": t["w"], "h": t["h"],
                              "format": t["format"], "storage": t["storage"]})

def emit_pass(idx, p):
    sampled = [b for b in p["binds"] if b not in storage_names]
    storage = [b for b in p["binds"] if b in storage_names]
    body = p["body"]

    g = []
    g.append("#version 450")
    g.append(f"// generated from {src_path.name} pass {idx}: {p['desc']}")
    g.append("// DO NOT EDIT -- regenerate with tests/gen_metal.py")
    g.append("layout(local_size_x = 16, local_size_y = 16) in;")
    b = 0
    for name in sampled:
        g.append(f"layout(binding = {b}) uniform sampler2D {name}_raw;")
        b += 1
    for name in storage:
        fmt = textures[name]["format"]
        g.append(f"layout(binding = {b}, {fmt}) uniform image2D {name};")
        b += 1
    out_binding = b
    g.append(f"layout(binding = {b}) uniform writeonly image2D OUT_TEX;")
    b += 1
    g.append(f"layout(binding = {b}, std140) uniform Params {{")
    g.append("    vec2 out_size;")
    for name in sampled:
        g.append(f"    vec2 {name}_size_u;")
    g.append("    vec4 rts_pack[2];")
    g.append("    int pair_changed_u;")
    g.append("    float mix_t_u;")
    for prm in params:
        g.append(f"    {prm['type']} {prm['name']};")
    g.append("};")
    for name in sampled:
        g.append(f"vec2 {name}_pt; vec2 {name}_size; vec2 {name}_pos;")
        g.append(f"vec4 {name}_tex(vec2 uv) {{ return texture({name}_raw, uv); }}")
    g.append("float rts_mix[8];")
    g.append("bool pair_changed;")
    g.append("float mix_t;")
    g.append("int num_mix;")
    # The fused passes write their flow cache with imageStore(..., ivec2(gl_FragCoord.xy), ...): in
    # libplacebo's fragment path that is the pass's own output pixel, which in a compute shader is the
    # invocation. gl_FragCoord is reserved, so the shim is a macro over a plain global.
    g.append("vec4 frag_coord_shim;")
    g.append("#define gl_FragCoord frag_coord_shim")
    g.append("")
    g.append(body)
    g.append("void main() {")
    g.append("    ivec2 gid = ivec2(gl_GlobalInvocationID.xy);")
    g.append("    if (gid.x >= int(out_size.x) || gid.y >= int(out_size.y)) return;")
    g.append("    vec2 out_pos = (vec2(gid) + 0.5) / out_size;")
    for name in sampled:
        g.append(f"    {name}_size = {name}_size_u;")
        g.append(f"    {name}_pt = 1.0 / {name}_size;")
        g.append(f"    {name}_pos = out_pos;")
    g.append("    for (int i = 0; i < 8; i++) rts_mix[i] = rts_pack[i / 4][i % 4];")
    g.append("    pair_changed = pair_changed_u != 0;")
    g.append("    mix_t = mix_t_u;")
    g.append(f"    num_mix = {window};")
    g.append("    frag_coord_shim = vec4(vec2(gid) + 0.5, 0.0, 1.0);")
    g.append("    imageStore(OUT_TEX, gid, hook());")
    g.append("}")

    stem = f"{idx:02d}_{p['save']}"
    (outdir / f"{stem}.comp").write_text("\n".join(g) + "\n")
    graph["passes"].append({
        "index": idx, "save": p["save"], "desc": p["desc"],
        "width_rpn": p["width"], "height_rpn": p["height"],
        "components": p["components"],
        "when_rpn": p["when"],
        "binds": ([{"name": n, "kind": "frame" if n in FRAME_BINDS
                    else "pass", "slot": k,
                    **({"frame": FRAME_BINDS[n]} if n in FRAME_BINDS else {})}
                   for k, n in enumerate(sampled)]
                  + [{"name": n, "kind": "storage",
                      "slot": len(sampled) + k} for k, n in enumerate(storage)]),
        "out_texture_slot": out_binding,
        "params_buffer": out_binding + 1,
        "entry": "main0",
    })
    return stem

stems = [emit_pass(idx, p) for idx, p in enumerate(passes)]
(outdir / "graph.json").write_text(json.dumps(graph, indent=1) + "\n")
gated = sum(1 for p in passes if p["when"])
print(f"{len(passes)} passes ({gated} gated by WHEN), {len(textures)} textures "
      f"({len(storage_names)} storage), window {window}, {len(params)} params -> {outdir}")

if do_compile:
    fails = 0
    for stem in stems:
        spv = outdir / f"{stem}.spv"
        r = subprocess.run(["glslc", "-fshader-stage=compute", "-O",
                            str(outdir / f"{stem}.comp"), "-o", str(spv)],
                           capture_output=True, text=True)
        if r.returncode:
            print(f"GLSLC FAIL {stem}:\n{r.stderr[:800]}")
            fails += 1
            continue
        # --msl-decoration-binding: MSL texture/buffer indices follow the
        # declared GLSL bindings even when the compiler eliminates unused
        # bindings and would otherwise renumber the survivors densely --
        # found the hard way: without it, any pass not using ALL its binds
        # had its OUT land on the wrong index and wrote into the void.
        r = subprocess.run(["spirv-cross", "--msl", "--msl-version", "20300",
                            "--msl-decoration-binding",
                            str(spv), "--output",
                            str(outdir / f"{stem}.metal")],
                           capture_output=True, text=True)
        if r.returncode:
            print(f"SPIRV-CROSS FAIL {stem}:\n{r.stderr[:800]}")
            fails += 1
    print(f"compile: {len(stems) - fails} ok, {fails} failed")
    sys.exit(1 if fails else 0)
