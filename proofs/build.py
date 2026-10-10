#!/usr/bin/env python3
"""build.py: split PROOFS.md into one file per proof, each opening with a plain-language summary.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 proofs/build.py            (writes proofs/*.md and proofs/README.md)
            python3 proofs/build.py --digest   (prints each proof's opening lines, for writing summaries)
COST:       instant.

PROOFS.md stays the master: the formal text of each file here is copied from it verbatim. The plain-language
summaries live in proofs/summaries.md, one "## <id>" section per proof. The build stops, and writes nothing, if a
proof has no summary, so this folder cannot fall silently behind the master. Edit a proof in PROOFS.md and its
summary in summaries.md, then rebuild; never edit the generated files.
"""
import pathlib, re, sys, textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
HERE = ROOT / "proofs"
SECTIONS = {"A": "The wall form", "B": "Windows, zero runs and the left band", "B′": "Siblings, Jen and the squeeze",
            "C": "Short proofs restated from the running text", "E": "Theorems proved by GPT", "F": "Collatz",
            "E2": "GPT's proofs, second-read", "S": "Proofs from the sparks",
            "G": "The waiting room (not yet verified)"}


PROVENANCE = r"\s*\([^)]*(\.md|§|20\d\d-|awaiting)[^)]*\)"  # "(RULE30-PRIZE.md §8.18; 2026-10-05)" and the like


def slug(text):
    t = re.sub(PROVENANCE, "", text).lower()  # drop provenance, keep descriptions
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return "-".join(t.split("-")[:8])


PREAMBLE = {}  # section -> the text between its "## " heading and its first proof


def units():
    """(id, section, heading, body) for every proof in PROOFS.md, in order. Fills PREAMBLE as a side effect."""
    lines = (ROOT / "PROOFS.md").read_text().split("\n")
    out, sec, sink = [], None, None  # sink: the unit (or preamble) receiving the current lines
    for line in lines:
        m = re.match(r"^## ([A-Z]′?\d?)\. ", line)
        if line.startswith("## "):
            sec = m.group(1) if m else None
            sink = PREAMBLE.setdefault(sec, []) if sec else None
            continue
        if sec is None:
            continue
        if line.startswith("### "):
            h = line[4:].strip()
            gm = re.match(r"G\.GPT(\d+[A-Z]?)\.", h)
            nm = re.match(r"(\d+)\. ", h)
            cm = re.match(r"([CEF])\.(\d+)\.? ", h)
            start = None
            if sec == "E2":
                start = f"G{gm.group(1)}" if gm else None
            elif sec == "G":
                # GPT heads a waiting-room entry "GPT G83 — ..." or "G83. ..."; a heading naming a proof that
                # already has a page ("G70 controls outcome", "G77. ..." under "GPT G77 — ...") continues that page
                n = re.match(r"(?:GPT )?G(\d+)\b", h)
                known = n and next((u for u in out if u[0] in (f"G{n.group(1)}", f"W{n.group(1)}")), None)
                if known:
                    sink = known[3]
                elif n and re.match(r"(GPT G\d+ —|G\d+\. )", h):
                    start = f"W{n.group(1)}"
                elif nm:  # Local's numbered entries wait here under their final number ("21. Proposition 8 ...")
                    start = f"{int(nm.group(1)):02d}"
            elif sec == "S":  # spark proofs, "SP01. ..." (S1, S2, ... already name Local's checks)
                sp = re.match(r"(SP\d+)\. ", h)
                start = sp.group(1) if sp else None
            elif nm:
                start = f"{int(nm.group(1)):02d}"
            elif cm:
                start = f"{cm.group(1)}{cm.group(2)}"
            if start:
                out.append([start, sec, h, []])
                sink = out[-1][3]
                continue
        if sink is not None:
            sink.append(line)
    return [(i, s, h, "\n".join(b).strip("\n")) for i, s, h, b in out]


def preamble(sec):
    return "\n".join(PREAMBLE.get(sec, [])).strip("\n")


def shared_notes(i, sec):
    """A section's opening notes that give verdicts by proof (as E2's do for G39 to G42) belong to those proofs."""
    text = preamble(sec)
    return text if re.search(r"\*\*" + re.escape(i) + r"\b", text) else ""


def source_proof(body):
    """Sections E and F hold statements only; copy the proof from the section their *Where:* line names."""
    m = re.search(r"\*Where:\* (RULE30-GPT\.md|COLLATZ-PRIZE\.md), \"([^\"]+)\"", body)
    if not m:
        return None, None
    src = (ROOT / m.group(1)).read_text().split("\n")
    for k, line in enumerate(src):
        hm = re.match(r"^(#+) (.*)", line)
        if hm and hm.group(2).strip() == m.group(2).strip():
            level, j = len(hm.group(1)), k + 1
            while j < len(src) and not re.match(r"^#{1,%d} " % level, src[j]):
                j += 1
            text = "\n".join(src[k + 1:j]).strip("\n")
            # a statement whose proof is the next subsection (G20.1's certificate is G20.2): take that one too
            proved = re.search(r"\*\*Proof|\*Proof|proof\.\*|certificate", text, re.I)
            if not proved and j < len(src) and src[j].startswith("#" * level + " "):
                n = j + 1
                while n < len(src) and not re.match(r"^#{1,%d} " % level, src[n]):
                    n += 1
                text += "\n\n" + src[j] + "\n" + "\n".join(src[j + 1:n]).rstrip("\n")
            return m.group(1), text
    return m.group(1), None


def relink(text):
    """Relative links in the master point from the repository root; from proofs/ they need one ../ more."""
    return re.sub(r"\]\((?!https?:|mailto:|#|\.\./)([^)]+)\)", r"](../\1)", text)


def summaries():
    text = (HERE / "summaries.md").read_text() if (HERE / "summaries.md").exists() else ""
    parts = re.split(r"^## (\S+)\s*$", text, flags=re.M)
    return {parts[k]: parts[k + 1].strip() for k in range(1, len(parts) - 1, 2)}


def status(sec, body, head=""):
    if sec == "G":
        return "in the waiting room: stated with a proof, not yet checked by a second reader"
    if sec == "E2":  # the reader is named in the heading from 2026-10-08 (GC620); G39 to G204 were all Local's
        m = re.search(r"\(second-read by ([A-Za-z]+(?: and [A-Za-z]+)?)", head)
        return "proved by GPT and second-read by " + (m.group(1) if m else "Local")
    if sec == "E":
        return "proved by GPT (statement in PROOFS.md; the proof is copied below from RULE30-GPT.md)"
    m = re.search(r"\*Status:\*\s*([^.\n]*)", body)
    return m.group(1).strip() if m else "proved"


def main():
    us = units()
    if "--digest" in sys.argv:
        for i, s, h, b in us:
            body = [l for l in b.split("\n") if l.strip()][:7]
            print(f"=== {i} [{s}] {h}\n" + "\n".join(x[:230] for x in body))
        return
    S = summaries()
    sys.path.insert(0, str(ROOT / "tests" / "probes"))
    from proof_dupes import hard  # a proof or paragraph pasted twice (Cloud's sweep, 2026-10-07)
    repeats = hard((ROOT / "PROOFS.md").read_text(), (HERE / "summaries.md").read_text())
    if repeats:
        print("NO FILES WRITTEN: PROOFS.md or summaries.md repeats something; see "
              "tests/probes/proof_dupes.py:\n  " + "\n  ".join(repeats))
        sys.exit(1)
    missing = [i for i, *_ in us if i not in S]
    if missing:
        print("NO FILES WRITTEN: these proofs have no summary in proofs/summaries.md: " + ", ".join(missing))
        sys.exit(1)
    stale = [k for k in S if k not in {i for i, *_ in us}]
    if stale:
        print("note: summaries with no proof in PROOFS.md (renamed or moved?): " + ", ".join(stale))
    for old in HERE.glob("*.md"):  # only generated pages: an id such as 01, C1, G48C, W77 or SP1, then a slug
        if re.match(r"^(\d\d|[CEFGW]\d+[A-Z]?|SP\d+)-.+\.md$", old.name):
            old.unlink()
    index = []
    for i, s, h, b in us:
        lead = r"^(\d+\.|[CEF]\.\d+\.?|G\.GPT\d+[A-Z]?\.|GPT G\d+ —|G\d+\.(?!\d)|SP\d+\.)\s*"
        title = re.sub(PROVENANCE, "", re.sub(lead, "", h))
        name = f"{i}-{slug(title)}.md"
        note = (f"*{SECTIONS.get(s, s)}. Derived from [PROOFS.md](../PROOFS.md), entry \"{h}\"; rebuild with "
                f"`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in "
                f"[summaries.md](summaries.md), never this file.*")
        doc = (f"# {title}\n\n" + textwrap.fill(note, 116, break_long_words=False, break_on_hyphens=False) + "\n\n"
               f"**Status:** {status(s, b, h)}.\n\n"
               f"## In plain words\n\n{S[i]}\n\n"
               f"## The formal statement and proof\n\n{relink(b)}\n")
        notes = shared_notes(i, s)
        if notes:
            doc += (f"\n## Second reader's notes shared with neighbouring proofs\n\n*Copied from the head of "
                    f"PROOFS.md section {s}.*\n\n{relink(notes)}\n")
        if s in ("E", "F"):
            src, proof = source_proof(b)
            if proof:
                doc += (f"\n## The proof, copied from {src}\n\n*Verbatim from [{src}](../{src}), the section named "
                        f"above; the master PROOFS.md holds the statement only.*\n\n{relink(proof)}\n")
            elif src:
                print(f"warning: {i}: the section named in {src} was not found")
        (HERE / name).write_text(doc)
        first = S[i].split("\n\n")[0].replace("\n", " ")
        index.append((s, name, title, first))
    rows, last = [], None
    for s, name, title, first in index:
        if s != last:
            rows.append(f"\n## {SECTIONS.get(s, s)}\n")
            note = preamble(s)
            if note and not any(shared_notes(u, s) for u, us_, *_ in us if us_ == s):
                rows.append("*From the head of this section in PROOFS.md:*\n\n" + relink(note) + "\n\n*The pages:*\n")
            last = s
        link = f"- [{title}]({name}):".replace(" ", "\0")  # never break a line inside the link
        rows.append(textwrap.fill(f"{link} {first}", 116, subsequent_indent="  ", break_long_words=False,
                                  break_on_hyphens=False).replace("\0", " "))
    if last != "G" and preamble("G"):  # an empty waiting room still shows its notes on unproved claims
        rows.append(f"\n## {SECTIONS['G']}\n")
        rows.append("*From the head of this section in PROOFS.md:*\n\n" + relink(preamble("G")) + "\n")
        rows.append("*No proofs are waiting for a second reader at the moment.*")
    intro = (HERE / "README-intro.md").read_text().strip() if (HERE / "README-intro.md").exists() else "# Proofs"
    (HERE / "README.md").write_text(intro + "\n" + "\n".join(rows) + "\n")
    print(f"wrote {len(index)} proof files and README.md")


if __name__ == "__main__":
    main()
