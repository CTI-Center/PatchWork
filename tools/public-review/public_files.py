"""Explicit allowlist for the framework-only public distribution."""

from pathlib import Path


PUBLIC = (
    "README.md", "LICENSE", "LICENSE-MIT", ".gitignore", ".github",
    "docs/CONTRIBUTING.md", "docs/Patchwork-CTI-Framework.md",
    "docs/Member-Registry.md", "docs/Publication-Checklist.md",
    "docs/Third-Party-Notices.md",
    "docs/Report-Types.md", "docs/Vocabularies.md", "docs/Sectors.md",
    "docs/Report-Templates", "docs/Real-Examples", "docs/Resources",
    "docs/Easy-access", "tools/check-links", "tools/repo-tree",
    "tools/gtidocs-mirror", "tools/public-review", "tools/documentation",
)


def is_public(path: str) -> bool:
    parts = Path(path).parts
    if not parts or ".." in parts or Path(path).is_absolute():
        return False
    if any(p.startswith(".") and p not in {".gitignore", ".github"} for p in parts):
        return False
    if "__pycache__" in parts or path.endswith((".pyc", ".pyo")):
        return False
    if path.startswith("docs/Resources/tools/"):
        return False
    return any(path == entry or path.startswith(entry + "/") for entry in PUBLIC)


def public_paths(root: Path) -> list[str]:
    paths = set()
    for entry in PUBLIC:
        target = root / entry
        if target.is_symlink():
            raise ValueError(f"symlink is not permitted in public export: {entry}")
        candidates = target.rglob("*") if target.is_dir() else [target]
        for path in candidates:
            rel = path.relative_to(root).as_posix()
            if is_public(rel) and path.is_symlink():
                raise ValueError(f"symlink is not permitted in public export: {rel}")
            if is_public(rel) and path.is_file():
                paths.add(rel)
    return sorted(paths)
