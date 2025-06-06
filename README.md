# Experiment Note

This repository contains a simple HTML note generator and a Python script for
validating research notes. Notes can belong to different types, each with its
own expected section headers. Header sets are defined in `note_headers.json`.

## Available Note Types

- `cell_harvest` – notes generated from `index.html` describing cell harvest and
  subculture.
- `general_experiment` – a generic experiment note format with standard
  sections.

## Validation Script

Use `validate_note.py` to check that a note contains all required headers for a
specific note type.

```bash
python validate_note.py PATH/TO/NOTE --type NOTE_TYPE
```

The command uses `note_headers.json` by default. Pass `--config` to use a
custom configuration file.

## Sample Notes

Two sample notes are included:

- `sample_cell_harvest.md` – example for the `cell_harvest` type.
- `sample_general_experiment.md` – example for the `general_experiment` type.

You can validate a sample note like this:

```bash
python validate_note.py sample_cell_harvest.md --type cell_harvest
```

If any expected header is missing, the script lists the missing entries and
returns a non-zero exit code.
