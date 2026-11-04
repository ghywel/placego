"""Serial, exact-source review of the two release forms with each kit's own Check.lean.

Run under run_capped.py. KIT_CACHE is a git clone containing both pinned commits.
The existing stage supervisor enforces the CPU/thermal budget across the compilers.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PACKET = Path("reports/wolfram-agents/submissions/universal-left-side")
NEW = "Ruliology.CellularAutomata.Rule30UniversalLeftSide"
HEADS = ("universal_of_strip", "universal_left_side", "one_left_side", "seed_left_side",
         "fork_dichotomy", "first_fork", "left_side_not_unique", "odd_farther_weights", "even_farther_weight")
CASES = (("portal", "722a0c515486066f97ccc81aed57eca949cf38db", "Rule30Submission"),
         ("kit", "a91c727339e2348b0351b3d1311a60a44ee89561", NEW))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    out = Path(os.environ["CAPPED_OUT"])
    cache = Path(os.environ["KIT_CACHE"])
    lean = os.environ["METAL_SCOPE_BINARY"]
    assert "eb6cafb7290e8bd5f2937522d8d804f58f02bafc" in subprocess.check_output([lean, "--version"], text=True)
    jobs, hashes = [], {}
    for kind, commit, module in CASES:
        root = out/kind
        root.mkdir()
        def blob(name):
            return subprocess.check_output(["git", "-C", str(cache), "show", commit+":"+name])
        assert blob("lean-toolchain").strip() == b'leanprover/lean4:v4.35.0'
        checker = root/"Check.lean"
        checker.write_bytes(blob("Check.lean"))
        seen = set()
        def emit(name, data):
            if name in seen:
                return
            seen.add(name)
            for dep in re.findall(rb'^(?:public )?import (Ruliology\.[\w.]+)\s*$', data, re.M):
                dep = dep.decode()
                if dep not in seen:
                    emit(dep, blob("lean/"+dep.replace(".","/")+".lean"))
            source = root/(name.replace(".","/")+".lean")
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_bytes(data)
            jobs.append(dict(name=kind+'-'+name.rsplit('.',1)[-1],
                             args=['env','LEAN_PATH='+str(root),lean,'-j1','-R',str(root),'-o',
                                   str(source.with_suffix('.olean')),str(source)],cpu=32,wall=60))
            hashes[str(source.relative_to(out))] = sha(data)
        src = PACKET/(module.rsplit('.',1)[-1]+'.lean')
        emit(module,src.read_bytes())
        args=['env','LEAN_PATH='+str(root),lean,'-j1','--run',str(checker),module,'--claim','partial']
        for head in HEADS:
            args.extend(['--headline',module+'.'+head])
        jobs.append(dict(name=kind+'-official-check',args=args,cpu=60,wall=100))
        hashes[str(checker.relative_to(out))] = sha(checker.read_bytes())
    # Check byte identity of the four canonical release inputs before compiling.
    for name,digest in PINS.items():
        assert sha((PACKET/name).read_bytes())==digest,name
    (out/'sources.json').write_text(json.dumps(hashes,sort_keys=True,indent=2)+'\n')
    plan = out/'jobs.json'
    plan.write_text(json.dumps(dict(worker_stop=225,input_sha256={},jobs=jobs),indent=2)+'\n')
    os.execv(sys.executable,[sys.executable,'tests/probes/metal_scope/stage.py',str(plan)])


PINS = {
    "Rule30Submission.lean": "fbe8869531ed3ee2edc59faf7c20ea211a2b78a90e690626440d6d48ec28874c",
    "Rule30UniversalLeftSide.lean": "991be6f58b57d92fe62bc760ecec8a823728b8b03498b5d5b9eb84442745d437",
    "abstract.txt": "f1672edd83205618f99331089fc2ecc5869416ecca74ee75e8942f0c3a58d0c4",
    "essay.md": "ef32ec78a8976a0c73f3f8220485b2e2fcf43db7ef980eef2b8a0f1f0040b9c7"
}


if __name__=='__main__':main()
