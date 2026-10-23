#!/usr/bin/env python3
"""Kernel-normalizing Lean encoding of GPT's channel certificates (CL587 job 2, GC1702/GC1704).

Reads the shared-store bundle (cited/gpt/cl587-channel-ca4cc38ded5fa750.json, kept outside git) and writes
TreeM16.lean and TreeM20.lean: the weight table as a complete binary tree indexed by the state number's bits
(about log2(states) steps per lookup instead of a linear List walk), rows as List literals (structural
recursion, which `decide` can unfold; GPT's Array.all is well-founded and gets stuck), and each chunk
closed by `decide +kernel`, which the kit permits (only `+native`, `native_decide` and `bv_decide` are
forbidden). The certificate's arithmetic is unchanged: for each row (a, b, w),
0 < w and 10^9 (weights[a] + weights[b]) <= 1159107281 w.

Usage: python3 -I tests/probes/channel_tree_encoding.py BUNDLE.json OUTDIR
"""
import json, re, sys

def build(w, bits, base, step):
    if bits == 0:
        return f"(T.leaf {w[base] if base < len(w) else 0})"
    return f"(T.node {build(w, bits - 1, base, 2 * step)} {build(w, bits - 1, base + step, 2 * step)})"

def main(bundle, outdir):
    b = json.load(open(bundle))
    for m, bits in ((16, 12), (20, 14)):
        src = b["files"][f"ChannelM{m}.lean"]["text"]
        w = [int(x) for x in re.search(r"def weights : Array Nat := #\[([^\]]*)\]", src).group(1).split(",")]
        assert len(w) <= 2 ** bits
        chunks = re.findall(r"def (chunk\d+) : Array \(Nat × Nat × Nat\) := #\[([^\]]*)\]", src)
        out = ["set_option maxRecDepth 200000\nset_option maxHeartbeats 0\nnamespace ChannelTree%d\n" % m,
               "inductive T where\n  | leaf : Nat → T\n  | node : T → T → T\n",
               "def look : T → Nat → Nat\n  | T.leaf w, _ => w\n"
               "  | T.node l r, i => if i % 2 = 0 then look l (i / 2) else look r (i / 2)\n",
               "def weights : T := " + build(w, bits, 0, 1) + "\n",
               "def good (r : Nat × Nat × Nat) : Bool :=\n"
               "  decide (0 < r.2.2 ∧ 1000000000 * (look weights r.1 + look weights r.2.1) ≤ 1159107281 * r.2.2)\n"]
        for name, body in chunks:
            out.append(f"def {name} : List (Nat × Nat × Nat) := [{body}]\n"
                       f"theorem {name}_ok : {name}.all good = true := by decide +kernel\n")
        out.append("example : look weights 1 = %d := by decide\nexample : look weights %d = %d := by decide\n"
                   "end ChannelTree%d\n" % (w[1], len(w) - 1, w[-1], m))
        open(f"{outdir}/TreeM{m}.lean", "w").write("".join(out))
        rows = sum(body.count("),(") + 1 for _, body in chunks)
        print(f"m={m}: {len(w)} weights, {len(chunks)} chunks, {rows} rows")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
