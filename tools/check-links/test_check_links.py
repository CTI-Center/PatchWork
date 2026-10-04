"""Regression tests for GitHub-compatible public documentation links."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check-links.py")
SPEC = importlib.util.spec_from_file_location("check_links", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class GitHubLinksTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def document(self, text, name="README.md"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_punctuation_is_removed_from_heading_anchors(self):
        page = self.document("## 4.1-Three-tiers-of-object,-linked\n[Go](#41-three-tiers-of-object-linked)\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_obsidian_only_anchor_is_rejected(self):
        page = self.document("## 4.1-Three-tiers-of-object,-linked\n[Go](#4.1-three-tiers-of-object,-linked)\n")
        self.assertEqual(len(checker.check_file(page, self.root, {})), 1)

    def test_inline_code_in_heading_contributes_to_anchor(self):
        page = self.document("## The `report_types_ov` values\n[Go](#the-report_types_ov-values)\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_duplicate_heading_suffixes_and_collisions(self):
        page = self.document("# Repeat\n# Repeat\n# Repeat-1\n# Repeat\n")
        self.assertEqual(checker.headings_of(page, {}), {"repeat", "repeat-1", "repeat-1-1", "repeat-2"})

    def test_rendered_formatting_and_unicode_heading(self):
        page = self.document("## This'll be a _Helpful_ Section About the Greek Letter Θ!\n[Go](#thisll-be-a-helpful-section-about-the-greek-letter-θ)\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_heading_with_link_uses_visible_text_only(self):
        self.document("# Sources\n", "sources.md")
        page = self.document("## [Sources](sources.md) &amp; references\n[Go](#sources--references)\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_fenced_example_is_not_a_heading(self):
        page = self.document("````markdown\n# Fake\n```\n# Still fake\n````\n# Real\n")
        self.assertEqual(checker.headings_of(page, {}), {"real"})

    def test_reference_style_link_validates_destination(self):
        page = self.document("[Missing][spec]\n\n[spec]: absent.md\n")
        self.assertEqual(len(checker.check_file(page, self.root, {})), 1)

    def test_footnote_definition_is_not_a_file_link(self):
        page = self.document("An observation.[^1]\n\n[^1]: For analytical consistency, preserve provenance.\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_explicit_html_anchor_is_recognized(self):
        page = self.document('<a name="custom-anchor"></a>\n[Go](#custom-anchor)\n')
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_local_link_cannot_escape_public_root(self):
        page = self.document("[Outside](../README.md)\n", "docs/README.md")
        self.document("# Present\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])
        page.write_text("[Outside](../../outside.md)\n", encoding="utf-8")
        self.assertTrue(checker.check_file(page, self.root, {}))

    def test_percent_encoded_image_path(self):
        self.document("image bytes", "a picture.png")
        page = self.document("![Image](a%20picture.png)\n")
        self.assertEqual(checker.check_file(page, self.root, {}), [])

    def test_local_caches_do_not_pollute_cli_findings(self):
        self.document("# Public\n")
        self.document("[Broken](missing.md)\n", "tools/.cache/raw.md")
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_export_nested_in_checkout_checks_its_own_files(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        self.document("snapshot/\n", ".gitignore")
        self.document("# Public\n", "snapshot/README.md")
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.root / "snapshot")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
