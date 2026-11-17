#!/usr/bin/env python3
"""GC2110: verify/copy the exact arc notebook inputs and exec one bare kernel under run_capped.py."""
from pathlib import Path
import hashlib,json,os,re,shutil,sys
if len(sys.argv)!=4 or not os.environ.get('CAPPED_OUT'):
 raise SystemExit('REFUSED: need supervised root and KERNEL ESSAY KIT')
base=Path(__file__).resolve().parent
pins={'arc_notebook_checks.wl':'7cda9ac8e4ea4c96a7a0abd596cc1ee4fe4822ab67e4fb7a4ee5f02940ee27b3',
      'arc_notebook_control.wl':'d8bd0074b2b053965e7b23fa7435853a42e6ce5f777900cb8992ed186ca82399',
      'arc_notebook_run.wl':'71dbe01aa1c998c221132b9a0c6b4821bc0b0ed882775fdc014cb3f3369ac191',
      'notebook_receipt.wl':'4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7'}
files={name:(base/name).read_bytes() for name in pins}
for name,data in files.items():
 if hashlib.sha256(data).hexdigest()!=pins[name]:raise SystemExit('REFUSED: frozen '+name)
essay=Path(sys.argv[2]).read_bytes()
if hashlib.sha256(essay).hexdigest()!='0976ea3f35f38e558898bc76e9305badce9f6ad0f1c13d495ad9d8fc117dc64f':
 raise SystemExit('REFUSED: frozen essay')
source=(base.parents[2]/'reports/wolfram-agents/submissions/arc-codes/Rule30Submission.lean').read_bytes()
if hashlib.sha256(source).hexdigest()!='56d226a644ffc0c061239fc6daccdd88ba4a69efc9507939994b685411fe9594':
 raise SystemExit('REFUSED: source pin')
literal=re.search(r'LeanImportString\[("(?:[^"\\]|\\.)*"), "ProjectDir"',essay.decode(),re.S)
if not literal or json.loads(literal.group(1)).encode()!=source:
 raise SystemExit('REFUSED: embedded source differs')
if not Path(sys.argv[3]).is_dir():raise SystemExit('REFUSED: existing kit unavailable')
kernel=shutil.which(sys.argv[1])
if not kernel:raise SystemExit('REFUSED: existing kernel unavailable')
out=Path(os.environ['CAPPED_OUT']).resolve(strict=True);src=out/'src';src.mkdir();tmp=out/'tmp';tmp.mkdir()
for name,data in files.items():(src/name).write_bytes(data)
(out/'Rule30Submission.lean').write_bytes(source);(out/'source-essay.md').write_bytes(essay)
(out/'input-pins.json').write_text(json.dumps({**pins,'essay':'0976ea3f35f38e558898bc76e9305badce9f6ad0f1c13d495ad9d8fc117dc64f','source':'56d226a644ffc0c061239fc6daccdd88ba4a69efc9507939994b685411fe9594'},indent=2)+'\n')
for key in ('TMPDIR','TMP','TEMP'):os.environ[key]=str(tmp)+os.sep
print('ARC_NOTEBOOK_INPUTS_OK',flush=True)
os.execv(kernel,[kernel,'-script',str(src/'arc_notebook_run.wl'),str(out/'source-essay.md'),sys.argv[3]])
