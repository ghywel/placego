#!/usr/bin/env python3
"""dead_passes.py [shader.glsl ...]: passes whose saved texture no later pass binds (REPAIRS.md lead L1, 2026-10-04).

A libplacebo user shader is a sequence of //!HOOK blocks; each may //!SAVE its output under a name, and later blocks
//!BIND names to read them. A pass that saves a name nothing binds afterwards, and that is not the hook's output (no
SAVE, or a SAVE of the hooked texture itself), does work that cannot reach the picture. With no arguments it scans
every shader under ../../../shaders.
"""
import re, sys, pathlib

def passes(text):
    out = []
    for block in re.split(r"(?m)^(?=//!HOOK\b)", text):
        if not block.startswith("//!HOOK"):
            continue
        hook = re.search(r"(?m)^//!HOOK\s+(\S+)", block).group(1)
        save = re.search(r"(?m)^//!SAVE\s+(\S+)", block)
        desc = re.search(r"(?m)^//!DESC\s+(.*)$", block)
        binds = re.findall(r"(?m)^//!BIND\s+(\S+)", block)
        out.append(dict(hook=hook, save=save.group(1) if save else None, binds=binds,
                        desc=desc.group(1).strip() if desc else ""))
    return out

def dead(text):
    """Liveness from the end: the hook's output passes are live, and a pass is live if a LATER live pass binds the
    name it saves. Everything else is dead, including whole chains that only feed a dead pass."""
    ps = passes(text)
    live = [False] * len(ps)
    for i in range(len(ps) - 1, -1, -1):
        p = ps[i]
        if p["save"] is None or p["save"] == p["hook"]:
            live[i] = True
            continue
        live[i] = any(live[j] and p["save"] in ps[j]["binds"] for j in range(i + 1, len(ps)))
    return len(ps), [(i, ps[i]["save"], ps[i]["desc"]) for i in range(len(ps)) if not live[i]]

if __name__ == "__main__":
    here = pathlib.Path(__file__).resolve().parents[3] / "shaders"
    files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(here.rglob("*.glsl"))
    total = 0
    for f in files:
        n, found = dead(f.read_text(encoding="utf-8"))
        if found:
            total += len(found)
            names = ", ".join(s for _, s, _ in found)
            print(f"{f.name}: {len(found)} dead of {n} passes ({names})")
    print(f"DEADPASSES DONE: {total} dead pass(es) in {len(files)} file(s)")
