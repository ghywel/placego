#!/usr/bin/env python3
"""GC2612: check only the retained, previously uncalled positive certificate.

No regeneration, replay of completed controls or solver. exec keeps the
checker in the same process for the outer stage's aggregate accounting.
Accept only an EXIT/rc0 receipt AND the literal VERIFIED UNSAT output.
"""
import hashlib
import os
from pathlib import Path

root = Path(os.environ['SIX_GUARD_INPUT'])
checker = Path('/usr/local/bin/cake_lpr')
for p, sha in [
    (root/'implication.cnf', 'b3e6d4b9cd6767d5556856f61eff5e8ac5981b82c33aeb46d3756fe684c9441e'),
    (root/'implication.lrat', 'ecee5483d6a52affdd2a7cf0c87a97290f23a4f66309d81576d0a34df10d086e'),
    (checker, '445c63926127267a4f0ae5c363b2bffcb004aece119ca50414e7bc22f8bdec23'),
]:
    assert hashlib.sha256(p.read_bytes()).hexdigest() == sha, 'INPUT_HASH_MISMATCH'
os.nice(10)
os.execv(str(checker), [str(checker), '--CML_HEAP_SIZE=128', '--CML_STACK_SIZE=32',
                      str(root/'implication.cnf'), str(root/'implication.lrat')])
