#!/usr/bin/env python3
"""retire_dead_gates.py <shader.glsl> ...: retire the contrast gates that cannot fire (REPAIRS.md lead L3, 2026-10-04).

In a pass that declares `const float MIN_CONTRAST = 0.0;`, the early exit `if (local_contrast_*(uv) < MIN_CONTRAST)
{ ... }` can never be taken: a contrast (max - min) is never negative and the test is a strict <. Its 5x5 (or 3x3)
contrast still ran for every texel. Here the early exit and its contrast function go, and the constant becomes a
dated note. Passes whose gate is live (0.02, the 1/16 level) are left alone. For HAND-MAINTAINED files only: the
generated ones are rebuilt from them (rebuild_generated.py). Every removal is counted and asserted.
"""
import re, sys, pathlib

NOTE = ("// RETIRED 2026-10-04 (REPAIRS.md L3): at 0.0 this level's gate could never\n"
        "// fire (a contrast is never negative, and the test was a strict <), yet its\n"
        "// contrast window was read for every texel. The early exit is gone; the\n"
        "// 1/16 level keeps its gate at 0.02.\n")


def retire_block(b):
    if not re.search(r"(?m)^const float MIN_CONTRAST = 0\.0;$", b):
        return b, 0
    lines = b.split("\n")
    calls = [i for i, ln in enumerate(lines) if re.search(r"if \(local_contrast_\w+\(\w+\) < MIN_CONTRAST\) \{$", ln)]
    fns = set()
    for i in reversed(calls):
        fns.add(re.search(r"(local_contrast_\w+)\(", lines[i]).group(1))
        ind = re.match(r"^( *)", lines[i]).group(1)
        j = next(k for k in range(i + 1, len(lines)) if lines[k] == ind + "}")
        del lines[i:j + 1]
        if i < len(lines) and lines[i] == "" and i > 0 and lines[i - 1] == "":
            del lines[i]
    text = "\n".join(lines)
    # The contrast functions stay: generators inject code of their own into these passes, and the global-seed cage
    # calls local_contrast_5x5_q/_q2 itself (deleting them broke 14 generated files on the first try, 2026-10-04).
    # A function nothing calls costs nothing: the compiler drops it.
    assert not re.search(r"(?m)^(?!\s*//).*< MIN_CONTRAST", text), "a gate survived in code"
    text, n = re.subn(r"(?m)^const float MIN_CONTRAST = 0\.0;\n", NOTE, text)
    assert n == 1
    return text, len(calls)


def main():
    total = 0
    for a in sys.argv[1:]:
        p = pathlib.Path(a)
        t = p.read_text(encoding="utf-8")
        assert "GENERATED FILE" not in t[:400], f"{p.name} is generated: rebuild it instead"
        parts = re.split(r"(?m)^(?=//!HOOK\b)", t)
        n = 0
        out = []
        for b in parts:
            nb, k = retire_block(b)
            out.append(nb); n += k
        if n:
            p.write_text("".join(out), encoding="utf-8", newline="\n")
        print(f"  {p.name}: {n} gate(s) retired")
        total += n
    print(f"RETIRE DONE: {total} gate(s) in {len(sys.argv) - 1} file(s)")


if __name__ == "__main__":
    main()
