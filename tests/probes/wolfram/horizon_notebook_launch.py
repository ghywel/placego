#!/usr/bin/env python3
"""L1184: verify/copy the exact horizon notebook inputs and exec one bare kernel under run_capped.py.
Adapted from the arc's GC2115 launcher (arc_notebook_launch.py): the same checks, with this package's pins."""
from pathlib import Path
import hashlib, json, os, re, shutil, sys
if len(sys.argv) != 4 or not os.environ.get('CAPPED_OUT'):
    raise SystemExit('REFUSED: need supervised root and KERNEL ESSAY KIT')
base = Path(__file__).resolve().parent
ESSAY = '4d24ea0712555cec4c8645a3055a369fc791891a68575ab68e05cd7904592355'
SOURCE = '791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110'
pins = {'horizon_notebook_checks.wl': '003aab35ce7760fcaac2ab4245901996ecc09a1fc24adc6e4d43f6cf20364c70',
        'horizon_notebook_control.wl': '0f066b3a5db550ce04f1de6fb8f66d0278e9e6b4585eda70985652f8c79e3fba',
        'horizon_notebook_run.wl': '588f1cbda2794f6561e05d74d309a272bb437e3a7de92789cb1c0db59da4fa4e',
        'notebook_receipt.wl': '4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7'}
files = {name: (base / name).read_bytes() for name in pins}
for name, data in files.items():
    if hashlib.sha256(data).hexdigest() != pins[name]:
        raise SystemExit('REFUSED: frozen ' + name)
essay = Path(sys.argv[2]).read_bytes()
if hashlib.sha256(essay).hexdigest() != ESSAY:
    raise SystemExit('REFUSED: frozen essay')
source = (base.parents[2] / 'reports/wolfram-agents/submissions/finite-horizon/Rule30Submission.lean').read_bytes()
if hashlib.sha256(source).hexdigest() != SOURCE:
    raise SystemExit('REFUSED: source pin')
literal = re.search(r'LeanImportString\[("(?:[^"\\]|\\.)*"), "ProjectDir"', essay.decode(), re.S)
if not literal or json.loads(literal.group(1)).encode() != source:
    raise SystemExit('REFUSED: embedded source differs')
if not Path(sys.argv[3]).is_dir():
    raise SystemExit('REFUSED: existing kit unavailable')
kernel = shutil.which(sys.argv[1])
if not kernel:
    raise SystemExit('REFUSED: existing kernel unavailable')
out = Path(os.environ['CAPPED_OUT']).resolve(strict=True)
src = out / 'src'; src.mkdir(); tmp = out / 'tmp'; tmp.mkdir()
for name, data in files.items():
    (src / name).write_bytes(data)
(out / 'Rule30Submission.lean').write_bytes(source); (out / 'source-essay.md').write_bytes(essay)
(out / 'input-pins.json').write_text(json.dumps({**pins, 'essay': ESSAY, 'source': SOURCE}, indent=2) + '\n')
for key in ('TMPDIR', 'TMP', 'TEMP'):
    os.environ[key] = str(tmp) + os.sep
print('HORIZON_NOTEBOOK_INPUTS_OK', flush=True)
os.execv(kernel, [kernel, '-script', str(src / 'horizon_notebook_run.wl'), str(out / 'source-essay.md'), sys.argv[3]])
