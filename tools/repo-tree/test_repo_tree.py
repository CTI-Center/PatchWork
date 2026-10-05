"""Public layouts must exclude internal material even when Git tracks it."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("repo-tree.py")
POLICY = SCRIPT.parents[1] / "public-review/public_files.py"


class PublicLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.script = self.root / "tools/repo-tree/repo-tree.py"
        self.script.parent.mkdir(parents=True)
        shutil.copy2(SCRIPT, self.script)
        policy = self.root / "tools/public-review/public_files.py"
        policy.parent.mkdir()
        shutil.copy2(POLICY, policy)
        self.file("README.md", "# Framework\n<!-- repo-tree:start -->\n<!-- repo-tree:end -->\n")
        self.file("docs/Patchwork-CTI-Framework.md", "# Framework\n")
        self.file("docs/design-system/internal.md", "# Internal design\n")
        self.file("docs/OpenCTI-Transfer-Plan.md", "# Transfer plan\n")
        self.file("tools/repo-tree/descriptions.json", json.dumps({
            "README.md": "", "docs": "", "docs/Patchwork-CTI-Framework.md": "Specification",
            "tools": "Tools", "tools/repo-tree": "Layout generator",
            "tools/public-review": "Public export policy",
        }))
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True, capture_output=True)

    def file(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_tree(self, *args):
        return subprocess.run([sys.executable, str(self.script), *args], capture_output=True, text=True)

    def test_public_print_excludes_tracked_internal_documents(self):
        result = self.run_tree("--public", "--print")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Patchwork-CTI-Framework.md", result.stdout)
        self.assertNotIn("design-system", result.stdout)
        self.assertNotIn("OpenCTI-Transfer-Plan", result.stdout)

    def test_public_generation_passes_check_and_preserves_private_files(self):
        stale = self.run_tree("--public", "--check")
        self.assertNotEqual(stale.returncode, 0)
        generated = self.run_tree("--public")
        self.assertEqual(generated.returncode, 0, generated.stdout + generated.stderr)
        checked = self.run_tree("--public", "--check")
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        self.assertTrue((self.root / "docs/design-system/internal.md").exists())

    def test_default_print_still_lists_internal_git_files(self):
        result = self.run_tree("--print")
        self.assertIn("design-system", result.stdout)
        self.assertIn("OpenCTI-Transfer-Plan.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
