#!/usr/bin/env python3
from pathlib import Path
import csv
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "decks" / "arpeggios" / "cards.tsv"

required = {"id", "front", "back", "quality", "degrees", "tags"}
valid_qualities = {"maj7", "dominant7", "minor7"}

with SOURCE.open(encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    missing = required - set(reader.fieldnames or [])
    if missing:
        raise SystemExit(f"Missing columns: {sorted(missing)}")
    rows = list(reader)

errors = []
ids = set()
fronts = set()

for i, row in enumerate(rows, start=2):
    if not all(row[k].strip() for k in required):
        errors.append(f"line {i}: empty required field")
    if row["id"] in ids:
        errors.append(f"line {i}: duplicate id {row['id']!r}")
    ids.add(row["id"])
    if row["front"] in fronts:
        errors.append(f"line {i}: duplicate front {row['front']!r}")
    fronts.add(row["front"])
    if row["quality"] not in valid_qualities:
        errors.append(f"line {i}: invalid quality {row['quality']!r}")
    if len(row["back"].split()) != 4:
        errors.append(f"line {i}: expected 4 notes, got {row['back']!r}")

if len(rows) != 36:
    errors.append(f"expected 36 cards, found {len(rows)}")

for q in valid_qualities:
    count = sum(r["quality"] == q for r in rows)
    if count != 12:
        errors.append(f"expected 12 {q} cards, found {count}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)

print(f"OK: {len(rows)} cards validated.")
