#!/usr/bin/env python3
"""sc10_false_memory.py: spark SC10 (SPARKS.md). A detail that feels like memory.

RUN-ON:     cpu (Python 3, standard library); the model answers come from fresh Claude instances run separately
COMMAND:    python3 tests/probes/sparks/sc10_false_memory.py prompts         (prints the three prompt kinds)
            python3 tests/probes/sparks/sc10_false_memory.py score DIR       (scores the answers saved in DIR)
COST:       instant; the model calls are nine short ones, made by Cloud through its agent tool.

DIR holds A1.txt .. A3.txt (list in view), B1_1.txt .. B1_3.txt (descriptions) and B2_1.txt .. B2_3.txt (lists rebuilt
from the descriptions alone). A word counts if it appears whole, as itself or with -s, -es or -ing, ignoring case.
Predictions (published in SPARKS.md before any model call): absent word in at most 1 of A's 18 lists, in at least
half of B's 18 descriptions, in at least 70 per cent of B's 18 rebuilt lists; another list's absent word in at most
5 per cent of B's rebuilt lists; the two new lists behaving like the classic ones.
Control: no list contains its own absent word (checked below), and scoring a list against itself finds 15 hits.
"""
import pathlib, re, sys

LISTS = [
    ("sleep", "bed rest awake tired dream wake snooze blanket doze slumber snore nap peace yawn drowsy"),
    ("chair", "table sit legs seat couch desk recliner sofa wood cushion swivel stool sitting rocking bench"),
    ("kettle", "tea boil steam spout whistle handle kitchen cup hot pour electric lid brew mug stove"),
    ("needle", "thread pin eye sewing sharp point prick thimble haystack thorn hurt injection syringe cloth knitting"),
    ("ladder", "rung climb step roof tall wooden aluminium painter fall reach height extend top wall gutter"),
    ("mountain", "hill valley climb summit top molehill peak plain glacier goat bike climber range steep ski"),
]
NEW = {"kettle", "ladder"}


def lure_re(w):
    return re.compile(rf"\b{re.escape(w)}(s|es|ing)?\b", re.I)


def block():
    return "\n".join(f"List {i + 1}: {', '.join(words.split())}" for i, (_, words) in enumerate(LISTS))


PROMPT_A = ("Here are six numbered lists of words.\n\n{lists}\n\nFirst, work out 17 x 23 and write the answer on one "
            "line. Then write out each list again, in order, one list per line, starting each line with its number. "
            "Answer in plain text only and do not use any tools.")
PROMPT_B1 = ("Here are six numbered lists of words.\n\n{lists}\n\nDescribe each list in one short sentence of at most "
             "15 words, without repeating any of its words. Write one line per list, starting each line with its "
             "number. Answer in plain text only and do not use any tools.")
PROMPT_B2 = ("Each of the six numbered sentences below describes a list of 15 words. For each one, write the 15 words "
             "you think the list contained, separated by commas, one line per list, starting each line with its "
             "number. Answer in plain text only and do not use any tools.\n\n{descriptions}")


def split6(text):
    parts = re.split(r"(?m)^\s*(?:\*\*)?(?:List\s*)?([1-6])\s*[.):\-]", text)
    out = {}
    for k in range(1, len(parts) - 1, 2):
        out.setdefault(int(parts[k]), parts[k + 1].strip())
    return [out.get(i, "") for i in range(1, 7)]


def score(d):
    d = pathlib.Path(d)
    res = {"A": [], "B1": [], "B2": [], "cross": [], "hits": []}
    for r in range(1, 4):
        a = split6((d / f"A{r}.txt").read_text())
        b1 = split6((d / f"B1_{r}.txt").read_text())
        b2 = split6((d / f"B2_{r}.txt").read_text())
        for i, (lure, words) in enumerate(LISTS):
            res["A"].append((lure, bool(lure_re(lure).search(a[i]))))
            res["B1"].append((lure, bool(lure_re(lure).search(b1[i]))))
            res["B2"].append((lure, bool(lure_re(lure).search(b2[i]))))
            others = [o for o, _ in LISTS if o != lure]
            res["cross"].append(any(lure_re(o).search(b2[i]) for o in others))
            res["hits"].append(sum(1 for w in words.split() if lure_re(w).search(b2[i])))
    n = 18
    fa = sum(x for _, x in res["A"]); fb1 = sum(x for _, x in res["B1"]); fb2 = sum(x for _, x in res["B2"])
    print(f"absent word in A's rebuilt lists: {fa}/{n}")
    print(f"absent word in B's descriptions: {fb1}/{n}")
    print(f"absent word in B's rebuilt lists: {fb2}/{n}")
    print(f"another list's absent word in B's rebuilt lists: {sum(res['cross'])}/{n}")
    print(f"true list words recovered in B's rebuilt lists: mean {sum(res['hits']) / n:.1f} of 15")
    for lure, _ in LISTS:
        kind = "new" if lure in NEW else "classic"
        print(f"  {lure:9s} ({kind}): descriptions {sum(x for l, x in res['B1'] if l == lure)}/3,"
              f" rebuilt {sum(x for l, x in res['B2'] if l == lure)}/3, list in view {sum(x for l, x in res['A'] if l == lure)}/3")
    ok = fa <= 1 and fb1 >= 9 and fb2 >= 13 and sum(res["cross"]) <= 1
    print("PASS" if ok else ("FAIL" if fb2 <= 5 or fa >= 4 else "PARTIAL: see the lines above"))


def main():
    for lure, words in LISTS:
        assert not lure_re(lure).search(words), lure
        assert sum(1 for w in words.split() if lure_re(w).search(words)) >= 15
    if sys.argv[1:2] == ["prompts"]:
        print("=== A ===\n" + PROMPT_A.format(lists=block()))
        print("\n=== B1 ===\n" + PROMPT_B1.format(lists=block()))
        print("\n=== B2 (descriptions filled in from B1) ===\n" + PROMPT_B2.format(descriptions="<B1 answer>"))
    elif sys.argv[1:2] == ["score"]:
        score(sys.argv[2])


if __name__ == "__main__":
    main()
