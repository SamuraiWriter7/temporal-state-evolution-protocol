#!/usr/bin/env python3

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[1]


VALIDATION_PAIRS = [
    (
        "Pulse Record",
        ROOT / "schemas/pulse-record.schema.json",
        ROOT / "examples/pulse-record.example.yaml",
    ),
    (
        "State Transition Record",
        ROOT / "schemas/state-transition-record.schema.json",
        ROOT / "examples/state-transition-record.example.yaml",
    ),
    (
        "Cadence Decision Record",
        ROOT / "schemas/cadence-decision-record.schema.json",
        ROOT / "examples/cadence-decision-record.example.yaml",
    ),
    (
        "Temporal Causality Binding Record",
        ROOT / "schemas/temporal-causality-binding-record.schema.json",
        ROOT / "examples/temporal-causality-binding-record.example.yaml",
    ),
    (
        "Temporal Lifecycle Audit Record",
        ROOT / "schemas/temporal-lifecycle-audit-record.schema.json",
        ROOT / "examples/temporal-lifecycle-audit-record.example.yaml",
    ),
]


SPEC_FILES = [
    ROOT / "specs/structural-precedence-core.yaml",
    ROOT / "specs/state-transition-rule.yaml",
    ROOT / "specs/adaptive-cadence-policy.yaml",
    ROOT / "specs/temporal-causality-binding.yaml",
    ROOT / "specs/trace-audit-bridge.yaml",
]


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON file and require an object at the root."""
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path}: root must be a JSON object")

    return data


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file and require a mapping at the root."""
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path}: root must be a YAML mapping")

    return data


def format_error_path(error: Any) -> str:
    """Return a readable dotted path for a validation error."""
    if not error.absolute_path:
        return "<root>"

    parts = []

    for item in error.absolute_path:
        if isinstance(item, int):
            parts.append(f"[{item}]")
        else:
            if parts:
                parts.append(".")
            parts.append(str(item))

    return "".join(parts)


def validate_schema(
    label: str,
    schema_path: Path,
) -> tuple[dict[str, Any] | None, list[str]]:
    """Validate that a JSON Schema is structurally valid."""
    errors: list[str] = []

    try:
        schema = load_json(schema_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"Schema load failure: {exc}")
        return None, errors

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        errors.append(f"Invalid JSON Schema: {exc.message}")
        return None, errors

    print(f"[schema-ok] {label}")
    return schema, errors


def validate_example(
    label: str,
    schema: dict[str, Any],
    example_path: Path,
) -> list[str]:
    """Validate one YAML example against its JSON Schema."""
    errors: list[str] = []

    try:
        instance = load_yaml(example_path)
    except (OSError, yaml.YAMLError, ValueError) as exc:
        return [f"Example load failure: {exc}"]

    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )

    validation_errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: list(error.absolute_path),
    )

    for error in validation_errors:
        path = format_error_path(error)
        errors.append(f"{path}: {error.message}")

    if not errors:
        print(f"[example-ok] {label}")

    return errors


def validate_spec(path: Path) -> list[str]:
    """Check basic structural integrity of a specification YAML file."""
    errors: list[str] = []

    try:
        spec = load_yaml(path)
    except (OSError, yaml.YAMLError, ValueError) as exc:
        return [f"Spec load failure: {exc}"]

    if "schema_version" not in spec:
        errors.append("Missing top-level field: schema_version")

    specification = spec.get("specification")

    if not isinstance(specification, dict):
        errors.append("Missing or invalid top-level field: specification")
        return errors

    for required_field in ("id", "name", "status"):
        if not specification.get(required_field):
            errors.append(
                f"Missing specification.{required_field}"
            )

    if not errors:
        print(f"[spec-ok] {path.relative_to(ROOT)}")

    return errors


def main() -> int:
    """Run all schema, example, and specification checks."""
    total_failures = 0

    print("=== Temporal State Evolution Protocol Validation ===")
    print()

    for label, schema_path, example_path in VALIDATION_PAIRS:
        print(f"[validate] {label}")
        print(f"  schema : {schema_path.relative_to(ROOT)}")
        print(f"  example: {example_path.relative_to(ROOT)}")

        schema, schema_errors = validate_schema(
            label,
            schema_path,
        )

        for error in schema_errors:
            print(f"Error: {error}")
            total_failures += 1

        if schema is not None:
            example_errors = validate_example(
                label,
                schema,
                example_path,
            )

            for error in example_errors:
                print(f"Error: {error}")
                total_failures += 1

        print()

    print("=== Specification YAML Checks ===")
    print()

    for spec_path in SPEC_FILES:
        spec_errors = validate_spec(spec_path)

        for error in spec_errors:
            print(
                f"Error: {spec_path.relative_to(ROOT)}: {error}"
            )
            total_failures += 1

    print()

    if total_failures:
        print(
            f"[fail] Validation completed with "
            f"{total_failures} error(s)."
        )
        return 1

    print("[ok] All protocol validation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
