#!/usr/bin/env python3
"""GC2107: freeze/copy pure receipt fixtures and exec one existing kernel under run_capped.py."""
from pathlib import Path
import hashlib,os,shutil,sys
if len(sys.argv)!=2 or not os.environ.get('CAPPED_OUT'):
 raise SystemExit('REFUSED: need supervised root and existing kernel executable')
base=Path(__file__).resolve().parent
pins={'notebook_receipt.wl':'4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7',
      'notebook_receipt_control.wl':'b24543a2cb722272cbc5da100da477f3fc7b44783c32106cafee852cbda470ae'}
files={name:(base/name).read_bytes() for name in pins}
for name,data in files.items():
 if hashlib.sha256(data).hexdigest()!=pins[name]:raise SystemExit('REFUSED: frozen '+name)
kernel=shutil.which(sys.argv[1])
if not kernel:raise SystemExit('REFUSED: existing kernel unavailable')
out=Path(os.environ['CAPPED_OUT']).resolve(strict=True);src=out/'src';src.mkdir();tmp=out/'tmp';tmp.mkdir()
for name,data in files.items():(src/name).write_bytes(data)
for key in ('TMPDIR','TMP','TEMP'):os.environ[key]=str(tmp)+os.sep
print('NOTEBOOK_RECEIPT_CONTROL_SOURCES_OK',flush=True)
os.execv(kernel,[kernel,'-script',str(src/'notebook_receipt_control.wl')])
