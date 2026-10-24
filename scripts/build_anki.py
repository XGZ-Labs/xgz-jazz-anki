#!/usr/bin/env python3
from pathlib import Path
import csv
import genanki

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "decks" / "arpeggios" / "cards.tsv"
OUTPUT = ROOT / "dist" / "XGZ_Jazz_Arpeggios.apkg"

# Keep these stable forever once published.
DECK_ID = 2059400110
MODEL_ID = 1607392319

class StableNote(genanki.Note):
    @property
    def guid(self):
        # Stable across rebuilds even if Front/Back wording later changes.
        return genanki.guid_for(self.fields[0])

model = genanki.Model(
    MODEL_ID,
    "XGZ Jazz Basic",
    fields=[
        {"name": "ID"},
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }
    ],
    css="""
.card {
  font-family: Arial, sans-serif;
  font-size: 28px;
  text-align: center;
  color: black;
  background-color: white;
}
""".strip(),
)

deck = genanki.Deck(
    DECK_ID,
    "XGZ Jazz::Arpeggios",
)
deck.description = (
    "XGZ Jazz by XGZ Labs. "
    "36 jazz seventh-chord arpeggios: maj7, dominant 7, and minor 7 in all 12 roots. "
    "Educational content licensed CC BY 4.0."
)

with SOURCE.open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        note = StableNote(
            model=model,
            fields=[row["id"], row["front"], row["back"]],
            tags=row["tags"].split(),
        )
        deck.add_note(note)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
genanki.Package(deck).write_to_file(str(OUTPUT))
print(OUTPUT)
