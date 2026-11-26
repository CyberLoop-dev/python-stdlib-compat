#!/usr/bin/env python3
"""Static, curated standard-library compatibility checks."""
import argparse
import ast
import json
from pathlib import Path

MODULE_INTRODUCED = {"graphlib": "3.9", "zoneinfo": "3.9", "tomllib": "3.11"}
SYMBOL_INTRODUCED = {
    ("typing", "Self"): "3.11",
    ("typing", "Required"): "3.11",
    ("typing", "NotRequired"): "3.11",
    ("itertools", "batched"): "3.12",
}
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__", "site-packages"}

def version_tuple(value):
    parts = value.split(".")
    if len(parts) < 2 or not all(p.isdigit() for p in parts[:2]):
        raise ValueError("target version must look like 3.10 or 3.11")
    return tuple(map(int, parts[:2]))

def scan_file(path, target):
    findings = []
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, UnicodeError, SyntaxError) as exc:
        return [{"file": str(path), "line": getattr(exc, "lineno", 0) or 0, "kind": "parse-error", "detail": str(exc)}]
    def check(module, symbol, line, kind):
        introduced = MODULE_INTRODUCED.get(module) if kind == "module" else SYMBOL_INTRODUCED.get((module, symbol))
        if introduced and target < version_tuple(introduced):
            label = module if kind == "module" else f"{module}.{symbol}"
            findings.append({"file": str(path), "line": line, "kind": kind, "symbol": label, "introduced": introduced})
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                check(alias.name.split(".")[0], "", node.lineno, "module")
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            root = node.module.split(".")[0]
            check(root, "", node.lineno, "module")
            for alias in node.names:
                if (root, alias.name) in SYMBOL_INTRODUCED:
                    check(root, alias.name, node.lineno, "symbol")
    return findings

def collect(paths, target):
    files = []
    for item in paths:
        p = Path(item)
        if p.is_file() and p.suffix == ".py":
            files.append(p)
        elif p.is_dir():
            for child in p.rglob("*.py"):
                if not any(part in SKIP_DIRS for part in child.parts):
                    files.append(child)
    findings = []
    for file in sorted(set(files)):
        findings.extend(scan_file(file, target))
    return findings

def main():
    parser = argparse.ArgumentParser(description="Check selected stdlib APIs against a target Python version.")
    parser.add_argument("paths", nargs="+", help="Python files or directories")
    parser.add_argument("--target", default="3.10", help="minimum supported version, e.g. 3.10")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args()
    try:
        target = version_tuple(args.target)
    except ValueError as exc:
        parser.error(str(exc))
    findings = collect(args.paths, target)
    if args.json:
        print(json.dumps({"target": args.target, "findings": findings}, indent=2))
    elif not findings:
        print(f"No findings in the curated rule set for Python {args.target}.")
    else:
        for item in findings:
            if item["kind"] == "parse-error":
                print(f'{item["file"]}:{item["line"]}: parse error: {item["detail"]}')
            else:
                print(f'{item["file']}:{item["line"]}: {item["symbol"]} requires Python {item["introduced"]} (target: {args.target})')
    return 1 if findings else 0

if __name__ == "__main__":
    raise SystemExit(main())
