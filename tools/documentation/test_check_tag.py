"""Exercise the tag guard against real, isolated Git histories."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check_tag.py")


class DevelopmentTagTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q", "-b", "development")
        self.commit("initial development")
        self.git("update-ref", "refs/remotes/origin/development", "HEAD")

    def git(self, *args):
        return subprocess.run(
            ["git", "-c", "user.name=Automation test", "-c",
             "user.email=automation@example.invalid", *args],
            cwd=self.root, capture_output=True, text=True, check=True,
        ).stdout.strip()

    def commit(self, message):
        self.git("commit", "--allow-empty", "-qm", message)

    def check(self, tag="docs-v0.7.1"):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(self.root), "--tag", tag],
            capture_output=True, text=True,
        )

    def test_lightweight_tag_on_development_is_accepted(self):
        self.git("tag", "docs-v0.7.1")
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(self.git("rev-parse", "HEAD"), result.stdout)

    def test_annotated_tag_is_peeled_to_its_commit(self):
        self.git("tag", "-am", "documentation build", "docs-v0.7.1")
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(self.git("rev-parse", "HEAD"), result.stdout)

    def test_tagged_ancestor_remains_valid_after_development_advances(self):
        self.git("tag", "docs-v0.7")
        self.commit("next development change")
        self.git("update-ref", "refs/remotes/origin/development", "HEAD")
        self.git("checkout", "-q", "--detach", "docs-v0.7")
        result = self.check("docs-v0.7")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_transfer_branch_only_commit_is_rejected(self):
        self.git("switch", "-qc", "docs/opencti-transfer")
        self.commit("private transfer plan")
        self.git("tag", "docs-v0.7.1")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("development history", result.stderr)

    def test_wrong_checked_out_commit_is_rejected(self):
        self.git("tag", "docs-v0.7.1")
        self.commit("newer checkout")
        self.git("update-ref", "refs/remotes/origin/development", "HEAD")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("checked-out commit", result.stderr)

    def test_missing_development_history_fails_closed(self):
        self.git("tag", "docs-v0.7.1")
        self.git("update-ref", "-d", "refs/remotes/origin/development")
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("development", result.stderr)

    def test_missing_tag_is_rejected(self):
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cannot resolve tag", result.stderr)

    def test_invalid_or_shell_like_names_are_rejected_without_side_effects(self):
        for tag in ("v0.7.1", "docs-vnext", "docs-v0.7.1;touch sentinel", "docs-v0.7/escape"):
            with self.subTest(tag=tag):
                result = self.check(tag)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("tag format", result.stderr)
                self.assertFalse((self.root / "sentinel").exists())


if __name__ == "__main__":
    unittest.main()
