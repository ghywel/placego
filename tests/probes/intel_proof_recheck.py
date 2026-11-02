#!/usr/bin/env python3
"""GC2375: check the preserved complete proof; never rerun its solver."""
import hashlib,json,os,resource,signal,shutil
from pathlib import Path
import intel_phase_review as m
m.OUT=Path(os.environ['CAPPED_OUT']);m.PLAN={'worker_cpu_stop':480,'proof_chunk_mib':8,'proof_expanded_mib':4096}
src=Path(os.environ['CERT_SOURCE']);name='D64-rain0-cert'
for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda s,f:m.STOP.append(s))
resource.setrlimit(resource.RLIMIT_CPU,(500,500))
try:
    m.thermal()
    digest='0f75bf2143166826c087de2d96ad258d01419451da267a769ffd03ff5714ec85'
    parts=json.loads((src/(name+'-parts.json')).read_text())
    assert hashlib.sha256((src/(name+'.cnf')).read_bytes()).hexdigest()=='ab2c06f4ae3f2a8a3092c048a2a53f7bc34eb4d06dcd29fe1ecb2380c8495042'
    for fn in [name+'.cnf',name+'-parts.json',*[p['name'] for p in parts]]:
        assert Path(fn).name==fn
        os.link(src/fn,m.OUT/fn)
    fifo,th,receipt=m.proof_stream(name,False)
    rec=m.command('recheck',['/usr/local/bin/cake_lpr','--CML_HEAP_SIZE=768','--CML_STACK_SIZE=64',str(m.OUT/(name+'.cnf')),str(fifo)],350,450)
    th.join(timeout=3)
    assert not th.is_alive() and receipt.get('complete') and receipt['sha256']==digest
    assert rec['returncode']==0 and 's VERIFIED UNSAT' in (m.OUT/'recheck.stdout').read_text()
    m.save('verified.json',{'certificate_verified':True,'expanded_sha256':digest,'expanded_bytes':receipt['bytes'],'cnf_sha256':hashlib.sha256((m.OUT/(name+'.cnf')).read_bytes()).hexdigest()})
    fifo.unlink();m.thermal()
finally:m.save('summary.json',{'worker_cpu_s':m.cpu(),'stop':m.STOP})
