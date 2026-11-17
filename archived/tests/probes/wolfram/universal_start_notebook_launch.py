#!/usr/bin/env python3
"""GC2093: put the kernel's inherited temporary directory inside the supervised artifact root, then exec it.
Run ONLY under run_capped.py; arguments: KERNEL DRIVER ESSAY KIT. No new child/group or dependency setup.
The WL driver verifies $TemporaryDirectory before any resource/LeanLink/notebook build.
"""
import os
import pathlib
import shutil
import sys

if len(sys.argv) != 5 or not os.environ.get("CAPPED_OUT"):
    raise SystemExit("REFUSED: need CAPPED_OUT and KERNEL DRIVER ESSAY KIT")
out = pathlib.Path(os.environ["CAPPED_OUT"]).resolve(strict=True)
tmp = out / "tmp"
tmp.mkdir()  # Must be fresh, as must the outer supervisor destination.
kernel = shutil.which(sys.argv[1])
if not kernel:
    raise SystemExit("REFUSED: existing kernel executable unavailable")
for key in ("TMPDIR", "TMP", "TEMP"):
    os.environ[key] = str(tmp) + os.sep
os.execv(kernel, [kernel, "-script", *sys.argv[2:]])
