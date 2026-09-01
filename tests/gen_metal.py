#!/usr/bin/env python3
"""Translate an mpv-hook shader into per-pass Metal compute shaders.

    ./gen_metal.py <hook.glsl> <outdir> [--compile]

Parses the //! directive structure (HOOK/BIND/SAVE/WIDTH/HEIGHT/
COMPONENTS/DESC pass blocks; TEXTURE/SIZE/FORMAT/STORAGE texture blocks),
wraps each `vec4 hook()` body as a standalone GLSL compute shader with
the implicit mpv API shimmed, and emits:

    <outdir>/NN_<save>.comp      one standalone GLSL pass each
    <outdir>/graph.json          the pass graph a host executes:
                                 textures, binds in binding order,
                                 size expressions, components
    <outdir>/NN_<save>.metal     with --compile: glslc + spirv-cross

The GLSL source stays the single source of truth (METALPORT.md): the
output of this tool is generated material, regenerated after any shader
edit, never hand-edited. Proven by the P0 spike (metal-demo/spike/):
this road preserves semantics, not just syntax -- the real coarse-flow
pass recovered a known motion on 99.3% of texels after translation.

Shim contract (must match the host in metal-demo/):
  - buffer(0), std140: vec2 out_size; vec2 <NAME>_size_u per sampled
    bind in bind order; vec4 rts_pack[2] (rts_mix packed to dodge the
    std140 float-array stride trap -- P0 lesson 2); int pair_changed.
  - texture indices in MSL follow GLSL binding order: sampled binds
    first (in //!BIND order), storage binds next, the SAVE target last.
    spirv-cross's entry point is main0; its signature is the authority
    if in doubt (P0 lesson 1).
  - <NAME>_pos for every bind is the same normalized output position,
    which is what libplacebo's shared-uv sampling means at matched
    aspect. Sizes/pt are per-bind.

The traps this encodes: a `//!` line ALWAYS terminates a body (bodies
comment with plain //); WIDTH/HEIGHT are RPN over HOOKED.w/h and
literals, evaluated by the HOST, carried symbolically here; SAVE names
never collide with STORAGE names in this shader family -- asserted, so
a future edit that breaks that assumption fails loudly here instead of
silently misbinding.
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
passes = []     # {hook,binds,save,width,height,components,desc,body}

i = 0
cur = None      # current pass being accumulated
mode = None     # None | 'pass_directives' | 'pass_body' | 'texture'
tex = None

def close_pass():
    global cur, mode
    if cur is not None:
        cur["body"] = "\n".join(cur["body"]).rstrip() + "\n"
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
                   "desc": "", "body": []}
            mode = "pass_directives"
        elif key == "TEXTURE":
            close_pass()
            tex = {"name": parts[1], "w": None, "h": None,
                   "format": None, "storage": False}
            textures[parts[1]] = tex
            mode = "texture"
        elif mode == "texture":
            if key == "SIZE":
                tex["w"], tex["h"] = int(parts[1]), int(parts[2])
            elif key == "FORMAT":
                tex["format"] = parts[1]
            elif key == "STORAGE":
                tex["storage"] = True
            else:
                sys.exit(f"line {i+1}: unknown TEXTURE directive {key}")
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
        # content outside blocks (file header comments) is dropped
    i += 1
close_pass()

storage_names = {n for n, t in textures.items() if t["storage"]}
save_names = {p["save"] for p in passes if p["save"]}
overlap = storage_names & save_names
assert not overlap, f"SAVE/STORAGE overlap breaks the shim contract: {overlap}"

FRAME_BINDS = {"HOOKED", "FRAME1", "FRAME2", "FRAME3",
               "FRAME4", "FRAME5", "FRAME6", "FRAME7"}

graph = {"source": src_path.name, "textures": [], "passes": []}
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
    g.append("};")
    for name in sampled:
        g.append(f"vec2 {name}_pt; vec2 {name}_size; vec2 {name}_pos;")
        g.append(f"vec4 {name}_tex(vec2 uv) {{ return texture({name}_raw, uv); }}")
    g.append("float rts_mix[8];")
    g.append("bool pair_changed;")
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
    g.append("    imageStore(OUT_TEX, gid, hook());")
    g.append("}")

    stem = f"{idx:02d}_{p['save']}"
    (outdir / f"{stem}.comp").write_text("\n".join(g) + "\n")
    graph["passes"].append({
        "index": idx, "save": p["save"], "desc": p["desc"],
        "width_rpn": p["width"], "height_rpn": p["height"],
        "components": p["components"],
        "binds": ([{"name": n, "kind": "frame" if n in FRAME_BINDS
                    else "pass", "slot": k} for k, n in enumerate(sampled)]
                  + [{"name": n, "kind": "storage",
                      "slot": len(sampled) + k} for k, n in enumerate(storage)]),
        "out_texture_slot": out_binding,
        "params_buffer": out_binding + 1,
        "entry": "main0",
    })
    return stem

stems = [emit_pass(idx, p) for idx, p in enumerate(passes)]
(outdir / "graph.json").write_text(json.dumps(graph, indent=1) + "\n")
print(f"{len(passes)} passes, {len(textures)} textures "
      f"({len(storage_names)} storage) -> {outdir}")

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
