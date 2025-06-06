#!/usr/bin/env python3
"""Validate research note headers based on note type."""
import argparse
import json
import sys


def load_config(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_note(path: str, note_type: str, config: dict) -> list:
    expected_headers = config.get(note_type)
    if expected_headers is None:
        raise ValueError(f"Unknown note type: {note_type}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    missing = [h for h in expected_headers if h not in content]
    return missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate research note headers")
    parser.add_argument("note_file", help="Path to the note file")
    parser.add_argument("--type", required=True, dest="note_type", help="Note type defined in config")
    parser.add_argument("--config", default="note_headers.json", help="Path to header config JSON")
    args = parser.parse_args()

    config = load_config(args.config)
    try:
        missing = validate_note(args.note_file, args.note_type, config)
    except ValueError as exc:
        print(exc)
        sys.exit(2)

    if missing:
        print("Missing headers:")
        for header in missing:
            print(f"- {header}")
        sys.exit(1)
    print("All expected headers are present.")


if __name__ == "__main__":
    main()
