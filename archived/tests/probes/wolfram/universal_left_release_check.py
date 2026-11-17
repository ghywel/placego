"""Serial, exact-source review of the two release forms with each kit's own Check.lean.

Run under run_capped.py. KIT_CACHE is a git clone containing both pinned commits.
RELEASE_FIRST names the initial checkpoint. To compare normal command-line elaboration,
set RELEASE_WARM to the completed synchronous release run instead. The stage supervisor
enforces the CPU/thermal budget across the compilers.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
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
    warm = Path(os.environ["RELEASE_WARM"]) if "RELEASE_WARM" in os.environ else None
    if warm:
        assert json.loads((warm/"launcher.json").read_bytes())["exit_reason"]=="COMPLETED"
        assert sha((warm/"sources.json").read_bytes())=="3cbb2e90b51edfb4250505a7cf6595ae6b28d22c35789db97ccee632c582cd78"

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
            hashes[str(source.relative_to(out))] = sha(data)
            if warm and name != module:
                prior = warm/kind/source.relative_to(root)
                assert prior.read_bytes()==data and prior.with_suffix(".olean").is_file()
                for obj in prior.parent.glob(prior.stem+".*"):
                    if obj != prior:
                        shutil.copyfile(obj, source.parent/obj.name)
                return
            # Only resume successful exact-source objects from the pinned first launch.
            if not warm and kind == "portal" and name in RESUME:
                prior = Path(os.environ["RELEASE_FIRST"])/kind/source.relative_to(root)
                assert prior.read_bytes()==data
                receipt = prior.parents[len(name.split("."))-1].parent/("portal-"+name.rsplit(".",1)[-1]+".receipt.json")
                assert json.loads(receipt.read_bytes())["returncode"]==0
                for suffix, digest in RESUME[name].items():
                    obj = prior.with_suffix(suffix)
                    assert sha(obj.read_bytes())==digest
                    shutil.copyfile(obj,source.with_suffix(suffix))
                return
            jobs.append(dict(name=kind+'-'+name.rsplit('.',1)[-1],
                             args=['env','LEAN_PATH='+str(root),lean,'-j1',*([] if warm else ['-DElab.async=false']),'-R',str(root),'-o',
                                   str(source.with_suffix('.olean')),str(source)],cpu=32,wall=60))
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
    plan.write_text(json.dumps(dict(worker_stop=55 if warm else 200,input_sha256={},jobs=jobs),indent=2)+'\n')
    os.execv(sys.executable,[sys.executable,'tests/probes/metal_scope/stage.py',str(plan)])


RESUME = {
    "Ruliology.CellularAutomata.Rule30Diagonals": {
        ".ir": "92e75cf20c7a3db4ca9b938085f85721b7a66aa8d5aec43f5adf84643e70bd66",
        ".ir.sig": "249ad26d9869027ca959789f3d6ce813e9e51b15ec25f903c2992aa250db450b",
        ".olean": "ab0c1ce3df341f493880631118ebdabea362ce5610789c37f5c6f656ded5dad0",
        ".olean.private": "2a7b9e050d62ea8045b59fa493af9fa30792f0ef81c21d0f990d5cf883561868",
        ".olean.server": "19755687edd18d062c5a3127aeb05c8b00d5b024003d6a590d7cf6e99aa10153"
    },
    "Ruliology.CellularAutomata.Rule30Jen": {
        ".ir": "1e4c1c960ec46e03c293f1bc5d89df5a132dfca642d6978ff82f6ac31bbab7b2",
        ".ir.sig": "3efeacee152b0ff6f0b2b53592a70a5345e5ab4839e68d54f2f5ef07db7402f1",
        ".olean": "4417b773634d0ecde29ef4d89ba91b974d4544d35f0ca840879282f83fd54e1a",
        ".olean.private": "2e493dec694e6b593888b0d73f767649272f82ad1e5aae601b7aa57c40eab4e6",
        ".olean.server": "87b23aa9b10757a66701c471e1c8a4c65f1a23a8c1c88827c35fcd2b763f1bf7"
    },
    "Ruliology.CellularAutomata.Rule30MaskedJen": {
        ".ir": "13b8179e37f800f38f9bcff53f2c4f49d633db8644766eac0d7143e41761a55c",
        ".ir.sig": "3adc70075872ce7d1d012798d829a81b55c6fc28ba92227d4c0731925ad3175b",
        ".olean": "4dc06f090059af76cfa8f613264d2a0e8ca03ce243c63167445a50fe2bee3340",
        ".olean.private": "c5a5444fd52f03763e0b22a26b06d93b2d6974baceba640ec62bd96537867f52",
        ".olean.server": "8c0ee183159e399dac9fd34946a4ede40bf2137ac78c6d21fb22605a18dd954c"
    },
    "Ruliology.CellularAutomata.Rule30Prize": {
        ".ir": "4c6db0c8b808b6a7f54a9436ea7339b6002b67482c006cb1d9ad37fd7089c4c6",
        ".ir.sig": "080f8967d707b6e92a481dd1fb91fe71658b2dc843ad65ee1f0be58519dff1bd",
        ".olean": "bc0a43b68ea92dcb9c69baced034c858a778b226f88b94e4e9d39494388bc423",
        ".olean.private": "558aeebe536012a331ffc3782e0d19beb23286c1858a3eb0799b0d419a508c86",
        ".olean.server": "8c1f38bf05124719edcf2753ac390b0d62a868fbf9efd6d60636e7d43fca86b8"
    }
}

PINS = {
    "Rule30Submission.lean": "fbe8869531ed3ee2edc59faf7c20ea211a2b78a90e690626440d6d48ec28874c",
    "Rule30UniversalLeftSide.lean": "991be6f58b57d92fe62bc760ecec8a823728b8b03498b5d5b9eb84442745d437",
    "abstract.txt": "f1672edd83205618f99331089fc2ecc5869416ecca74ee75e8942f0c3a58d0c4",
    "essay.md": "ef32ec78a8976a0c73f3f8220485b2e2fcf43db7ef980eef2b8a0f1f0040b9c7"
}


if __name__=='__main__':main()
