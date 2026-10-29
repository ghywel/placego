#!/usr/bin/env python3
"""GC2110: verify/copy the exact arc notebook inputs and exec one bare kernel under run_capped.py."""
from pathlib import Path
import hashlib,json,os,re,shutil,sys
if len(sys.argv)!=4 or not os.environ.get('CAPPED_OUT'):
 raise SystemExit('REFUSED: need supervised root and KERNEL ESSAY KIT')
base=Path(__file__).resolve().parent
pins={'arc_notebook_checks.wl':'45a91ca279a0ef286fcbed86d4319d6012cd2300b815dc14f2f6cbb1cf235ca5',
      'arc_notebook_control.wl':'24569ce66fe3943fbac8faa456da4a02455a038b48e92bf42bbef31aa21f550c',
      'arc_notebook_run.wl':'fdb9f56ddf4d4b1f8cc35ba4f048ec0b8cf247332360405f0e97616e72a43f7a',
      'notebook_receipt.wl':'4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7'}
files={name:(base/name).read_bytes() for name in pins}
for name,data in files.items():
 if hashlib.sha256(data).hexdigest()!=pins[name]:raise SystemExit('REFUSED: frozen '+name)
essay=Path(sys.argv[2]).read_bytes()
if hashlib.sha256(essay).hexdigest()!='37bcdad893f1e432cfffc67223665f1ade25b0a6f66ff5859cbea6dc2e641a59':
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
(out/'input-pins.json').write_text(json.dumps({**pins,'essay':'37bcdad893f1e432cfffc67223665f1ade25b0a6f66ff5859cbea6dc2e641a59','source':'56d226a644ffc0c061239fc6daccdd88ba4a69efc9507939994b685411fe9594'},indent=2)+'\n')
for key in ('TMPDIR','TMP','TEMP'):os.environ[key]=str(tmp)+os.sep
print('ARC_NOTEBOOK_INPUTS_OK',flush=True)
os.execv(kernel,[kernel,'-script',str(src/'arc_notebook_run.wl'),str(out/'source-essay.md'),sys.argv[3]])
