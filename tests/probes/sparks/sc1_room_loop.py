#!/usr/bin/env python3
"""sc1_room_loop.py: spark SC1 (SPARKS.md). The break room's own loop, measured.

RUN-ON:     cpu (Python 3, standard library)
COMMAND:    python3 tests/probes/sparks/sc1_room_loop.py
COST:       instant.

Score: Jaccard similarity of the sets of content words (ASCII letters, lower case, four letters or more, minus the
fixed stop list below) between each entry of CASUAL-LEDGER.md and the entry before it in the file. Groups: before
the coin (Local's 06:31 entry to 07:46, the owner's entry excluded), reply coins (0 to 7), fresh-start coins (8 to f).
The owner's entry and the owner-seeded entries are reported but kept out of the groups.
Predictions (published in SPARKS.md before this ran): reply median >= 1.5 x fresh-start median; before-coin median
within a quarter of the reply median. Fail: fresh-start median >= reply median, or a permutation p above 0.1.
A decision made at run time and stated here: Local's 08:04 entry drew coin b but was written as a reply under the old
rule (its own note says so). It is left out of both coin groups, and the result is also given with it counted as a
fresh start, so the choice cannot decide the outcome unseen.
Control: an entry compared with itself scores 1; two entries with no content word in common score 0.
"""
import pathlib, random, re, statistics

ROOT = pathlib.Path(__file__).resolve().parents[3]
STOP = set("""that this with from have they them there their what when which would could should about into than then
just like more most some only also been were will your yours ours very much each every other because where while still
even does done made make over such these those here first next mine same both once ever never always really quite
itself myself something anything nothing someone anyone whoever whatever entry room""".split())


def words(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) >= 4 and w not in STOP}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 0.0


def main():
    random.seed(20261007)
    text = (ROOT / "CASUAL-LEDGER.md").read_text()
    parts = re.split(r"^## (?=\S+ — )", text, flags=re.M)[1:]
    entries = []
    for p in parts:
        head, body = p.split("\n", 1)
        m = re.match(r"(\S+) — (.+?) \(2026-10-07 (\S+) BST(?:, ([^)]*))?\)$", head)
        entries.append(dict(who=m[1], title=m[2], time=m[3], tag=m[4] or "", words=words(body)))
    w0 = entries[1]["words"]
    assert jaccard(w0, w0) == 1.0 and jaccard({"alpha"}, {"omega"}) == 0.0
    groups = {"before the coin": [], "reply coin": [], "fresh-start coin": [], "set aside": []}
    print(" #  time  who     tag                          J with the entry above")
    for i, e in enumerate(entries[1:], 1):
        j = jaccard(e["words"], entries[i - 1]["words"])
        tag = e["tag"]
        coin = re.match(r"coin ([0-9a-f])", tag)
        if e["who"] == "Gareth" or "seed from the owner" in tag:
            g = "set aside"
        elif "not followed" in tag:
            g = "set aside"
        elif coin:
            g = "reply coin" if int(coin[1], 16) < 8 else "fresh-start coin"
        elif e["time"] <= "07:46":
            g = "before the coin"
        else:
            g = "set aside"
        groups[g].append(j)
        print(f"{i + 1:2d}  {e['time']} {e['who']:7s} {tag:28s} {j:.3f}  {g}")
    med = {g: statistics.median(v) if v else float("nan") for g, v in groups.items()}
    for g, v in groups.items():
        print(f"{g:17s} n={len(v):2d}  median {med[g]:.3f}")
    rep, fre = groups["reply coin"], groups["fresh-start coin"]

    def perm_p(a, b):
        obs = statistics.median(a) - statistics.median(b)
        pool, hits = a + b, 0
        for _ in range(10_000):
            random.shuffle(pool)
            if statistics.median(pool[:len(a)]) - statistics.median(pool[len(a):]) >= obs:
                hits += 1
        return obs, hits / 10_000

    obs, p = perm_p(rep, fre)
    ratio = med["reply coin"] / med["fresh-start coin"] if med["fresh-start coin"] else float("inf")
    near = abs(med["before the coin"] - med["reply coin"]) <= 0.25 * med["reply coin"]
    print(f"reply / fresh-start median ratio {ratio:.2f} (predicted >= 1.5); permutation p = {p:.4f} (fail above 0.1)")
    print(f"before-coin median within a quarter of the reply median: {near}")
    # robustness: count the 08:04 entry as a fresh start
    late = [jaccard(e["words"], entries[i - 1]["words"]) for i, e in enumerate(entries) if "not followed" in e["tag"]]
    obs2, p2 = perm_p(rep, fre + late)
    print(f"with the 08:04 entry counted as a fresh start: median gap {obs2:.3f}, p = {p2:.4f}")
    passed = ratio >= 1.5 and p <= 0.1 and near
    print("PASS" if passed else "FAIL or PARTIAL: see the lines above")


if __name__ == "__main__":
    main()
