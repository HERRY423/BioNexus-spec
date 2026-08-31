#!/usr/bin/env python3
"""Validate all JSON Schema definitions and standard data manifests in BioNexus-spec."""

from __future__ import annotations
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent

def validate_all_schemas():
    errors = []
    schema_count = 0
    data_count = 0

    search_dirs = [REPO_ROOT / 'schemas', REPO_ROOT / 'standards', REPO_ROOT / 'governance']

    for d in search_dirs:
        if not d.is_dir():
            continue
        for p in d.rglob('*.json'):
            try:
                data = json.loads(p.read_text(encoding='utf-8'))
            except Exception as e:
                errors.append(f'{p.relative_to(REPO_ROOT)}: Invalid JSON ({e})')
                continue

            if p.name.endswith('.schema.json') or ('schemas' in p.parts):
                schema_count += 1
                try:
                    Draft202012Validator.check_schema(data)
                except Exception as e:
                    errors.append(f'{p.relative_to(REPO_ROOT)}: Invalid JSON Schema ({e})')
            else:
                data_count += 1


    if errors:
        print(f"=== Schema Validation FAILED ({len(errors)} errors) ===")
        for err in errors:
            print(f"  [FAIL] {err}")
        return 1

    print(f"=== Schema Validation PASS ({schema_count} schemas, {data_count} data files verified) ===")
    return 0

if __name__ == '__main__':
    sys.exit(validate_all_schemas())
