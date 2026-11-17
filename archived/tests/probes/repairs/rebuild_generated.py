#!/usr/bin/env python3
"""rebuild_generated.py <outdir> [--install]: rebuild every generated shader from its sources, into <outdir>, and say
whether each body (after the generated header, as smoke.sh compares) matches the committed file. With --install the
rebuilt files replace the committed ones (run without it first: on unchanged sources every file must match).

REPAIRS.md lead L3 (2026-10-04). Each generated file records the command that made it, but not all of it: the
variational files leave out their base (the -variational-propagated line is built on bidirectional-interpolation-
propagated.glsl, the rest on the base) and the propagated line without a global seed leaves out ZERO_SEED=1, which
smoke.sh passes. Both are supplied here; the control run is what proves them right.
"""
import os, re, shlex, subprocess, sys, pathlib, shutil

S = pathlib.Path(__file__).resolve().parents[3]          # scripts/
SH = S / "shaders"
PY = os.environ.get("PY", os.path.expanduser("~/np-build/venv/bin/python3"))


def body(p):
    lines, out, c = pathlib.Path(p).read_text(encoding="utf-8").splitlines(True), [], 0
    started = False
    for ln in lines:
        if started:
            out.append(ln)
        elif ln.startswith("// ====="):
            c += 1
            if c == 2:
                started = True
    return "".join(out)


def recorded(p):
    for ln in pathlib.Path(p).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^//\s{3}(.*\.py\b.*)$", ln)
        if m:
            return m.group(1).strip()
    return None


def run(cmd, env, cwd):
    r = subprocess.run(cmd, cwd=cwd, env={**os.environ, **env}, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError((r.stderr or r.stdout).strip().splitlines()[-1] if (r.stderr or r.stdout) else "failed")


def build(name, out):
    src = SH / name
    cmd = recorded(src)
    if cmd is None:
        raise RuntimeError("no recorded command")
    parts = shlex.split(cmd)
    env = {}
    while parts and re.fullmatch(r"[A-Z_][A-Z0-9_]*=.*", parts[0]):
        k, v = parts.pop(0).split("=", 1)
        env[k] = v
    tool = os.path.basename(parts[0])
    args = parts[1:]
    dst = str(out / name)
    if name == "human-reading-quad.glsl":
        run([PY, str(S / "tests/gen_quaddirectional.py"), dst, "bidirectional-interpolation-propagated.glsl"], env, S)
        run([PY, str(S / "tests/add_human_reading.py"), dst, "--default", "1"], env, S)
        return
    if tool == "scale_shader.py":
        twin = out / args[0]
        if not twin.exists():
            build(args[0], out)
        run([PY, str(S / "tests/scale_shader.py"), str(twin), dst, args[2]], env, S / "tests")
        return
    if tool == "gen_variational.py":
        args = [dst if a == "<output.glsl>" else a for a in args]
        args[3] = dst                                   # the output, whatever the header wrote there
        prop = name.startswith("bidirectional-interpolation-variational-propagated")
        if len(args) < 7:
            args.append("bidirectional-interpolation-propagated.glsl" if prop else "bidirectional-interpolation.glsl")
        if prop and "GLOBAL_SEED" not in env and "ZERO_SEED" not in env:
            env["ZERO_SEED"] = "1"
        run([PY, str(S / "tests/gen_variational.py")] + args, env, S / "tests")
        return
    if tool in ("gen_tridirectional.py", "gen_quaddirectional.py", "gen_quintdirectional.py", "gen_sextdirectional.py"):
        run([PY, str(S / "tests" / tool), dst] + args[1:], env, S)
        return
    raise RuntimeError(f"unknown tool {tool}")


def main():
    out = pathlib.Path(sys.argv[1]).resolve()
    install = "--install" in sys.argv
    out.mkdir(parents=True, exist_ok=True)
    names = sorted(p.name for p in SH.glob("*.glsl") if "GENERATED FILE" in p.read_text(encoding="utf-8")[:400])
    # unscaled first, so every -4k twin finds its source rebuilt
    names.sort(key=lambda n: n.endswith("-4k.glsl"))
    same = differ = failed = 0
    for n in names:
        try:
            if not (out / n).exists():
                build(n, out)
        except Exception as e:
            failed += 1
            print(f"  FAILED   {n}: {e}")
            continue
        if body(out / n) == body(SH / n):
            same += 1
            print(f"  same     {n}")
        else:
            differ += 1
            print(f"  DIFFERS  {n}")
    print(f"REBUILD DONE: {same} same, {differ} differ, {failed} failed, of {len(names)}")
    if install and not failed:
        for n in names:
            shutil.copyfile(out / n, SH / n)
        print(f"installed {len(names)} files into {SH}")


if __name__ == "__main__":
    main()
