#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    ROOT / "specs/state-transition-rule.yaml",
    ROOT / "specs/adaptive-cadence-policy.yaml",
]

BLOCK_SCALAR_RE = re.compile(r"^(?P<indent>\s*)[^#\n]+:\s*[>|][-+]?\s*$")


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def repair_file(path: Path) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()

    repaired: list[str] = []
    inside_block = False
    required_indent = 0

    for line in lines:
        # Blank line ends the current simple block-scalar repair region.
        if inside_block and line.strip() == "":
            repaired.append(line)
            inside_block = False
            continue

        if inside_block:
            current_indent = leading_spaces(line)

            if current_indent < required_indent:
                line = (" " * required_indent) + line.lstrip(" ")

            repaired.append(line)
            continue

        repaired.append(line)

        match = BLOCK_SCALAR_RE.match(line)

        if match:
            key_indent = len(match.group("indent"))
            required_indent = key_indent + 2
            inside_block = True

    path.write_text(
        "\n".join(repaired) + "\n",
        encoding="utf-8",
    )

    print(f"[fixed] {path.relative_to(ROOT)}")


def main() -> None:
    for path in TARGETS:
        repair_file(path)


if __name__ == "__main__":
    main()
