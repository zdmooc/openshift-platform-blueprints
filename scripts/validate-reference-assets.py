#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
ACTIVE_TEXT_ROOTS = [
    ROOT / "README.md",
    ROOT / "architecture",
    ROOT / "docs" / "governance",
    ROOT / "docs" / "standards",
    ROOT / "platform",
]

errors: list[str] = []


def iter_files():
    for root in ACTIVE_TEXT_ROOTS:
        if root.is_file():
            yield root
        elif root.exists():
            for path in root.rglob("*"):
                if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py", ".sh"}:
                    yield path


for path in iter_files():
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)

    for stale in ("rh-openshift-architect-lab", "example/portal-platform"):
        if stale in text:
            errors.append(f"{rel}: stale repository reference: {stale}")

    if "-----BEGIN PRIVATE KEY-----" in text or "-----BEGIN RSA PRIVATE KEY-----" in text:
        errors.append(f"{rel}: private-key marker found")

    if re.search(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", text):
        errors.append(f"{rel}: JWT-like token found")

    if path.suffix.lower() in {".yaml", ".yml"}:
        if re.search(r"^--------+$", text, re.MULTILINE):
            errors.append(f"{rel}: invalid legacy YAML separator")
        if re.search(r"repoURL:\s*\[https?://", text):
            errors.append(f"{rel}: Markdown link syntax embedded in repoURL")
        try:
            list(yaml.safe_load_all(text))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: YAML parse error: {exc}")

# Validate local Markdown links for the curated active documentation surface.
link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
for path in iter_files():
    if path.suffix.lower() != ".md":
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)
    for target in link_re.findall(text):
        target = target.strip().split()[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{rel}: broken local link: {target}")

if errors:
    print("REFERENCE_VALIDATION=FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("REFERENCE_VALIDATION=PASS")
