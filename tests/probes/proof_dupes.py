#!/usr/bin/env python3
"""proof_dupes.py: keep PROOFS.md free of repeated proofs, and show a new entry its nearest older neighbours.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/proof_dupes.py              (hard checks, then the newest five entries' neighbours)
            python3 tests/probes/proof_dupes.py --near C2    (the entries most like one given entry)
COST:       a few seconds. proofs/build.py runs the hard checks on every build and writes nothing if one fails.

Why (the owner, 2026-10-07: "Can you do a proof sweep check to make sure proofs aren't being accidentally repeated -
I am wondering if we guard against this adequately"). Cloud's sweep that day found the record free of copies, but
by good practice, not by any check, and it found one result recorded twice: C.2, the latch, restates the first of
Lemma 3's two rules, filed two days later from another section with no cross-reference. Two kinds of check follow.
Hard (exit 1, and the build refuses): a `### ` heading that appears twice; a paragraph of 150 characters or more that
appears twice, provenance lines aside; one heading form used twice for the same G number (E2 files each proof under
Local's "G.GPTn." heading with GPT's original heading below it, so two forms per number are expected, but never the
same form twice); a summary id used twice. Advisory: for each entry asked about, the three older entries closest to
it in wording, by the formal text and by the plain-words summary. Whoever files or second-reads an entry reads those
three and says in the second reading if the new entry restates one. A high score is a prompt to look, not a verdict:
refinements that cite what they sharpen (G133 to G136, G186 to G187) score high and are not repeats.
Control: a synthetic file that repeats a paragraph must fail the hard checks, and Lemma 3 (entry 03) must be among
C2's three nearest entries, the repeat this probe was built after.
"""
import collections, math, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
STOP = set("the a an of and or to in is are be by for on at as it its this that with from not no any every each one "
           "two all if then so we us our which who than more most can cannot only also there their these those has "
           "have was were been being into out up down over under between both either such same other per but when "
           "where while whose what how does do did".split())
FORMS = (("wrapper", r"G\.GPT(\d+[A-Z]?)\."), ("original", r"GPT G(\d+)\b"), ("numbered", r"G(\d+)\.(?!\d)"))


def paragraphs(text):
    out, start, buf = [], 1, []
    for n, line in enumerate(text.split("\n") + [""], 1):
        if line.strip():
            if not buf:
                start = n
            buf.append(line)
        elif buf:
            out.append((start, " ".join(" ".join(buf).split())))
            buf = []
    return out


def hard(text, summaries=""):
    """Problems that mean something was pasted twice. An empty list means none."""
    bad, lines = [], text.split("\n")
    heads = collections.defaultdict(list)
    forms = collections.defaultdict(list)
    for n, line in enumerate(lines, 1):
        if line.startswith("### "):
            heads[line].append(n)
            for form, pat in FORMS:
                m = re.match(pat, line[4:])
                if m:
                    forms[(m.group(1), form)].append(n)
                    break
    bad += [f"heading repeated at lines {ns}: {h[:90]}" for h, ns in heads.items() if len(ns) > 1]
    bad += [f"G{k[0]} has two {k[1]} headings, at lines {ns}" for k, ns in forms.items() if len(ns) > 1]
    seen = collections.defaultdict(list)
    for n, p in paragraphs(text):
        if len(p) >= 150 and not p.startswith(("|", "*Where:*", "**Where:**")):
            seen[p].append(n)
    bad += [f"paragraph repeated at lines {ns}: {p[:80]}" for p, ns in seen.items() if len(ns) > 1]
    ids = collections.Counter(re.findall(r"^## (\S+)\s*$", summaries, re.M))
    bad += [f"summary id {k} used {c} times" for k, c in ids.items() if c > 1]
    return bad


def words(t):
    t = re.sub(r"\$[^$]*\$", " ", t)
    return [w for w in re.findall(r"[a-z][a-z0-9'-]+", t.lower()) if w not in STOP and len(w) > 2]


def vectors(docs):
    df = collections.Counter(w for d in docs.values() for w in set(d))
    out = {}
    for k, d in docs.items():
        tf = collections.Counter(d)
        v = {w: c / len(d) * math.log(len(docs) / df[w]) for w, c in tf.items()} if d else {}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        out[k] = {w: x / norm for w, x in v.items()}
    return out


def cosine(u, v):
    if len(u) > len(v):
        u, v = v, u
    return sum(x * v.get(w, 0.0) for w, x in u.items())


def neighbours(units, summaries, target, k=3):
    """The k older entries (earlier in PROOFS.md) closest to target, as (score, id, by-what)."""
    ids = [u[0] for u in units]
    form = vectors({i: words(b) for i, s, h, b in units})
    summ = vectors({i: words(summaries.get(i, "").split("**Why it matters.**")[0]) for i, *_ in units})
    older = ids[:ids.index(target)]
    scored = [(max(cosine(form[target], form[j]), cosine(summ[target], summ[j])), j,
               cosine(form[target], form[j]), cosine(summ[target], summ[j])) for j in older]
    return sorted(scored, reverse=True)[:k]


def control(units, summaries):
    para = "x " * 100
    assert hard(f"### A\n\n{para}\n\n### B\n\n{para}\n"), "a repeated paragraph must fail"
    assert not hard(f"### A\n\n{para}\n\n### B\n\n{para}y\n"), "distinct paragraphs must pass"
    assert hard("### G.GPT7. a\n\n### G.GPT7. b\n"), "the same heading form twice for one number must fail"
    near = [j for _, j, *_ in neighbours(units, summaries, "C2")]
    assert "03" in near, f"Lemma 3 must be among C2's nearest entries, got {near}"


def main():
    sys.path.insert(0, str(ROOT / "proofs"))
    import build  # the same reading of PROOFS.md that builds the pages
    text = (ROOT / "PROOFS.md").read_text()
    stext = (ROOT / "proofs" / "summaries.md").read_text()
    units, summaries = build.units(), build.summaries()
    control(units, summaries)
    bad = hard(text, stext)
    print(f"{len(units)} entries: " + ("no repeats found" if not bad else f"{len(bad)} REPEATS FOUND"))
    for b in bad:
        print("  " + b)
    targets = [sys.argv[sys.argv.index("--near") + 1]] if "--near" in sys.argv else [u[0] for u in units[-5:]]
    for t in targets:
        print(f"nearest older entries to {t} (formal text / summary; a prompt to look, not a verdict):")
        for score, j, f, s in neighbours(units, summaries, t):
            print(f"  {j:6s} {f:.2f} / {s:.2f}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
