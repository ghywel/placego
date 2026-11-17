#!/usr/bin/env python3
"""Shared helpers for the SW-02 task builders (Local). Briefs are written outside git, into DATA/tasks, with real paths."""
import json, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.environ.get("SW02_DATA", os.path.expanduser("~/placego-data/sw02"))
SW = os.path.join(DATA, "sw")          # frozen copy of this folder, read by agents
KIT = os.path.join(DATA, "kit")
REC_FULL = os.path.join(DATA, "rec-full")   # readers, skeptics, judges, compilers: holds the design
REC_PRE = os.path.join(DATA, "rec-pre")     # attack agents: the record before the design existed


def common(task_id, rec):
    s = open(os.path.join(HERE, "COMMON.md"), encoding="utf-8").read()
    out = os.path.join(DATA, "out", task_id)
    return (s.replace("{{REC}}", rec).replace("{{KIT}}", KIT).replace("{{DATA}}", DATA).replace("{{SW}}", SW)
             .replace("{{OUT}}", out).replace("{{ID}}", task_id))


def write_task(task_id, text, rec):
    os.makedirs(os.path.join(DATA, "tasks"), exist_ok=True)
    os.makedirs(os.path.join(DATA, "out", task_id), exist_ok=True)
    body = text.replace("{{REC}}", rec).replace("{{KIT}}", KIT).replace("{{DATA}}", DATA).replace("{{SW}}", SW) \
               .replace("{{OUT}}", os.path.join(DATA, "out", task_id)).replace("{{ID}}", task_id)
    full = body + "\n\n---\n\n" + common(task_id, rec)
    p = os.path.join(DATA, "tasks", task_id + ".md")
    open(p, "w", encoding="utf-8").write(full)
    return hashlib.sha256(full.encode()).hexdigest()[:16]


def write_batch(name, tasks, limit=8):
    os.makedirs(os.path.join(DATA, "batches"), exist_ok=True)
    b = {"batch": name, "base": DATA, "limit": limit, "tasks": tasks}
    json.dump(b, open(os.path.join(DATA, "batches", name + ".json"), "w"), indent=0)
    return b
