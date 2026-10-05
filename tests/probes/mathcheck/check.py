#!/usr/bin/env python3
"""check.py: the math check run after every edit of a document with TeX in it (PRIZE-PROBLEMS.md and others).

COMMAND:    python3 tests/probes/mathcheck/check.py PRIZE-PROBLEMS.md
SETUP:      once, in this folder: npm install. A Chromium is needed for the PDF; set CHROME to its executable if
            Playwright cannot find one (in the cloud container: /opt/pw-browsers/chromium-1194/chrome-linux/chrome).
PASSES when render.js reports 0 TeX errors (MathJax with GitHub's packages: base, ams, boldsymbol) and the typeset
page has no dollar sign left outside the maths (a $ followed by a digit is allowed: it is money, not maths).
Writes <name>.html and <name>.pdf next to this script (ignored by git).
"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]).resolve()
html, pdf = HERE / (src.stem + ".html"), HERE / (src.stem + ".pdf")
out = subprocess.run(["node", str(HERE / "render.js"), str(src), str(html), str(pdf)], capture_output=True, text=True)
print(out.stdout.strip())
text = re.sub(r"<[^>]+>", "", html.read_text()) if html.exists() else ""
loose = len(re.findall(r"\$(?!\d)", text))
print(f"dollar signs left outside the maths: {loose}")
ok = out.returncode == 0 and "TeX errors: 0" in out.stdout and loose == 0
print("MATH CHECK PASSES" if ok else "MATH CHECK FAILS")
sys.exit(0 if ok else 1)
