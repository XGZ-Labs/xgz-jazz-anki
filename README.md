# XGZ Jazz — Anki

Anki flashcard decks for **XGZ Jazz**, an open jazz-learning project from **XGZ Labs**.

This repository is the Anki implementation of XGZ Jazz. The umbrella project can later
expand into sibling repositories for web practice, printable exercises, notation,
ear training, APIs, and other learning platforms.

## First release

### XGZ Jazz — Arpeggios

36 cards covering all 12 roots for:

- Major seventh: `1 3 5 7`
- Dominant seventh: `1 3 5 b7`
- Minor seventh: `1 b3 5 b7`

Examples:

| Front | Back |
|---|---|
| `Cmaj7 arpeggio` | `C E G B` |
| `C7 arpeggio` | `C E G Bb` |
| `Cm7 arpeggio` | `C Eb G Bb` |

The deck uses harmonic/theoretical spellings rather than simplifying everything
enharmonically. For example, `Db7 = Db F Ab Cb`.

The material is instrument-neutral: it works for voice and melodic/harmonic
instruments. Transposition for Bb/Eb instruments is intentionally treated as a
separate skill.

## Repository structure

```text
xgz-jazz-anki/
├── decks/
│   └── arpeggios/
│       ├── cards.tsv
│       └── README.md
├── dist/
│   └── XGZ_Jazz_Arpeggios.apkg
├── scripts/
│   ├── build_anki.py
│   └── validate_cards.py
├── docs/
│   └── roadmap.md
├── .github/
│   └── workflows/
│       └── build.yml
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE
├── LICENSE-CONTENT.md
├── NOTICE.md
├── Makefile
├── requirements.txt
└── VERSION
```

## Build the Anki deck

Requires Python 3.

```bash
python -m pip install -r requirements.txt
python scripts/validate_cards.py
python scripts/build_anki.py
```

Output:

```text
dist/XGZ_Jazz_Arpeggios.apkg
```

The build uses stable deck/model IDs and stable note GUIDs so future releases can
update the same notes instead of intentionally creating a new unrelated deck.

## Import

In AnkiDroid:

1. Download `XGZ_Jazz_Arpeggios.apkg`.
2. Choose **Import**.
3. Select the package.
4. The deck appears as `XGZ Jazz::Arpeggios`.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Possible future areas include inversions, ii–V–I voice-leading, chord extensions,
scales, ear training, rhythm, and instrument-specific transposition decks.

## Licensing

- **Software/code:** MIT License. See [LICENSE](LICENSE).
- **Educational content/data/decks:** CC BY 4.0. See
  [LICENSE-CONTENT.md](LICENSE-CONTENT.md).

Unless a file says otherwise, that split applies throughout this repository.
