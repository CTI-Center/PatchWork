"""Public exports must contain framework material, never private history/plans."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("prepare-public.py")


class PublicExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.output = self.root / "public"
        self.source.mkdir()
        self.file("README.md", "# Patchwork\n<!-- repo-tree:start -->\n<!-- repo-tree:end -->\n[Framework](docs/Patchwork-CTI-Framework.md)\n")
        self.file("LICENSE", "Documentation license\n")
        self.file("LICENSE-MIT", "Tooling license\n")
        self.file("docs/Patchwork-CTI-Framework.md", "# Framework\n")

    def file(self, name, text="private data\n"):
        path = self.source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def export(self):
        return subprocess.run([sys.executable, str(SCRIPT), "--source", str(self.source), "--output", str(self.output)], capture_output=True, text=True)

    def test_export_keeps_framework_and_excludes_plans_history_and_caches(self):
        self.file("docs/Report-Templates/threat-activity.md", "# Template\n")
        self.file("docs/Real-Examples/example.md", "# Example\n")
        for name in ["docs/OpenCTI-Transfer-Plan.md", "docs/GTI-Data-Structures.md", "docs/GTI-OpenCTI-Backend-Plan.md", "docs/design-system/prototype/app.js", ".git/logs/HEAD", ".openai/hosting.json", "docs/Resources/tools/gtidocs-mirror/.cache/raw.md", "docs/new-private-plan.md"]:
            self.file(name)
        result = self.export()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        published = {str(p.relative_to(self.output)) for p in self.output.rglob("*") if p.is_file()}
        self.assertIn("docs/Patchwork-CTI-Framework.md", published)
        self.assertIn("docs/Report-Templates/threat-activity.md", published)
        self.assertIn("docs/Real-Examples/example.md", published)
        self.assertNotIn("docs/OpenCTI-Transfer-Plan.md", published)
        self.assertNotIn("docs/GTI-Data-Structures.md", published)
        self.assertNotIn("docs/GTI-OpenCTI-Backend-Plan.md", published)
        self.assertFalse(any(p.startswith((".git/", ".openai/", "docs/design-system/", "docs/Resources/tools/")) for p in published))
        self.assertNotIn("docs/new-private-plan.md", published)
        self.assertTrue((self.source / "docs/OpenCTI-Transfer-Plan.md").exists())

    def test_existing_destination_is_not_overwritten(self):
        self.output.mkdir()
        sentinel = self.output / "keep.txt"
        sentinel.write_text("keep me", encoding="utf-8")
        result = self.export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("exists", result.stdout + result.stderr)
        self.assertEqual(sentinel.read_text(), "keep me")

    def test_documentation_workflow_helper_is_included_in_public_copy(self):
        self.file("tools/documentation/check_tag.py", "print('check development tag')\n")
        self.file(".github/workflows/documentation-tag.yml", "name: Documentation build\n")
        result = self.export()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.output / ".github/workflows/documentation-tag.yml").exists())
        self.assertTrue((self.output / "tools/documentation/check_tag.py").exists())

    def test_publication_documents_are_copied_and_their_links_resolve(self):
        documents = (
            "docs/Member-Registry.md",
            "docs/Publication-Checklist.md",
            "docs/Third-Party-Notices.md",
        )
        for name in documents:
            self.file(name, "# Publication\n[Framework](Patchwork-CTI-Framework.md)\n")
        self.file("README.md", "<!-- repo-tree:start -->\n<!-- repo-tree:end -->\n" +
                  "\n".join(f"[Publication]({name})" for name in documents))
        result = self.export()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name in documents:
            with self.subTest(document=name):
                self.assertEqual((self.output / name).read_text(),
                                 "# Publication\n[Framework](Patchwork-CTI-Framework.md)\n")

    def test_enisa_profile_sources_and_assets_survive_public_export(self):
        documents = {
            "docs/ENISA-Alignment.md": "# ENISA\n[Profile](Report-Templates/annual-threat-landscape.md)\n[Schema](Easy-access/ENISA/enisa-threat-landscape-2026-schema.md)\n",
            "docs/Report-Templates/annual-threat-landscape.md": "# Annual\n[Alignment](../ENISA-Alignment.md)\n[Method](../Easy-access/ENISA/enisa-ctl-methodology-2026.md)\n",
            "docs/Easy-access/ENISA/enisa-threat-landscape-2026-schema.md": "# Schema\n[Method](enisa-ctl-methodology-2026.md)\n",
            "docs/Easy-access/ENISA/enisa-ctl-methodology-2026.md": "# Method\n![Figure](assets/enisa-ctl-methodology-2026/figure.png)\n",
            "docs/Easy-access/ENISA/assets/enisa-ctl-methodology-2026/figure.png": "asset fixture\n",
        }
        for name, content in documents.items():
            self.file(name, content)
        self.file("README.md", "<!-- repo-tree:start -->\n<!-- repo-tree:end -->\n[ENISA](docs/ENISA-Alignment.md)\n")
        result = self.export()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name, content in documents.items():
            with self.subTest(document=name):
                self.assertEqual((self.output / name).read_text(), content)
        self.assertFalse(any(self.output.rglob("*.pdf")))

    def test_public_links_cannot_point_to_private_files(self):
        self.file("docs/OpenCTI-Transfer-Plan.md")
        self.file("README.md", "[Private](docs/OpenCTI-Transfer-Plan.md)\n")
        result = self.export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing file", result.stdout + result.stderr)

    def test_symlink_to_private_material_is_rejected(self):
        private = self.file("docs/secret.md")
        link = self.source / "docs/Real-Examples/innocent.md"
        link.parent.mkdir()
        link.symlink_to(private)
        result = self.export()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink", result.stdout + result.stderr)

    def test_tree_in_nested_export_lists_public_files(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        (self.root / ".gitignore").write_text("public/\n", encoding="utf-8")
        tree_source = SCRIPT.parents[1] / "repo-tree/repo-tree.py"
        self.file("tools/repo-tree/repo-tree.py", tree_source.read_text(encoding="utf-8"))
        result = self.export()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        tree_result = subprocess.run([sys.executable, str(self.output / "tools/repo-tree/repo-tree.py"), "--print"], capture_output=True, text=True)
        self.assertIn("Patchwork-CTI-Framework.md", tree_result.stdout)


if __name__ == "__main__":
    unittest.main()
