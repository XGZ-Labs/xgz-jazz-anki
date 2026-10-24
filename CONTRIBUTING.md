# Contributing to XGZ Jazz

Contributions are welcome through issues and pull requests.

## Principles

1. Keep the learning goal of each card narrow and explicit.
2. Prefer one recall task per card.
3. Preserve correct harmonic spelling.
4. Keep source data platform-independent where practical.
5. Do not add copyrighted lead sheets, commercial method-book text, recordings,
   solos, transcriptions, or other material unless XGZ Labs has the rights to
   redistribute it under the repository's content license.

## Arpeggio cards

For `decks/arpeggios/cards.tsv`:

- `id` must be unique and stable.
- `front` is the recall prompt.
- `back` is the note sequence.
- `quality` is a machine-readable family name.
- `degrees` is the chord formula.
- `tags` is a space-separated list for Anki.

Run:

```bash
python scripts/validate_cards.py
python scripts/build_anki.py
```

before opening a pull request.

## Licensing contributions

By contributing code, you agree that it may be distributed under the MIT License.

By contributing educational content/data, you agree that it may be distributed
under CC BY 4.0.

If you cannot license a contribution under those terms, do not submit it.
