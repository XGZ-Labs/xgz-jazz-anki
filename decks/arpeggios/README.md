# Arpeggios deck

Anki deck: `XGZ Jazz::Arpeggios`

## Scope

Version 0.1.0 contains 36 root-position seventh-chord arpeggios:

- 12 major seventh chords
- 12 dominant seventh chords
- 12 minor seventh chords

## Card format

Front:

```text
Cmaj7 arpeggio
```

Back:

```text
C E G B
```

## Spelling policy

Use harmonic spelling that reflects chord function.

Examples:

- `Db7`: `Db F Ab Cb`
- `Gb7`: `Gb Bb Db Fb`
- `Dbm7`: `Db Fb Ab Cb`
- `Gbm7`: `Gb Bbb Db Fb`

Do not replace these with easier enharmonic spellings unless a separate
beginner-oriented deck explicitly chooses that pedagogical policy.

## Source of truth

`cards.tsv` is the source of truth.

Do not manually edit the generated `.apkg` and treat it as canonical.
Edit `cards.tsv`, validate, then rebuild.
