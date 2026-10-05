"""Offline regression coverage for mirror conversion; no live GTI requests."""

import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("gti_mirror", Path(__file__).with_name("mirror.py"))
mirror = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mirror)


class MirrorConversionTests(unittest.TestCase):
    def test_http_request_identifies_the_current_project(self):
        response = io.BytesIO(b"# Documentation\n")
        response.headers = {"Content-Type": "text/markdown"}
        # Only the external transport is mocked; the HTTP request is real.
        with patch.object(mirror.urllib.request, "urlopen", return_value=response) as transport:
            body, content_type = mirror._raw_get("https://example.invalid/docs", timeout=5)
        request = transport.call_args.args[0]
        self.assertIn("(+https://github.com/CTI-Center/PatchWork)",
                      request.get_header("User-agent"))
        self.assertEqual((body, content_type), (b"# Documentation\n", "text/markdown"))

    def test_transforms_headings_but_preserves_fenced_examples(self):
        page = mirror.Page({"slug": "example", "title": "Example"}, "guides", "group")
        page.raw = "# API Guide\n\n## Analysis / Sandbox\n\n```python\n# Do Not Change\n```\n"
        mirror.transform_page(page, {})
        self.assertEqual(page.title, "API Guide")
        self.assertIn("# api-guide", page.body)
        self.assertIn("## analysis-/-sandbox", page.body)
        self.assertIn("# Do Not Change", page.body)
        self.assertEqual(page.headings["analysis--sandbox"], "analysis-/-sandbox")

    def test_images_and_callouts_become_renderable_markdown(self):
        unknown = {}
        result = mirror.convert_components(
            '<Image src="https://example.invalid/a.png" alt="Example" />\n'
            '<Callout>Keep this note</Callout>', "example", unknown,
        )
        self.assertIn("![Example](https://example.invalid/a.png)", result)
        self.assertIn("> Keep this note", result)
        self.assertEqual(unknown, {})

    def test_unknown_components_are_reported_but_code_examples_are_not(self):
        unknown = {}
        result = mirror.convert_components('<Widget />\n```html\n<Fake />\n```', "example", unknown)
        self.assertIn("<Widget />", result)
        self.assertEqual(unknown, {"Widget": {"example"}})

    def test_hostile_link_destinations_are_wrapped_for_markdown(self):
        self.assertEqual(mirror.md_target("guide (draft).md"), "<guide (draft).md>")
        self.assertEqual(mirror.md_target("guide.md"), "guide.md")

    def test_frontmatter_is_removed_without_dropping_the_body(self):
        meta, body = mirror.strip_frontmatter('---\ntitle: "Example"\nupdatedAt: 2026-10-05\n---\n# Body\n')
        self.assertEqual(meta, {"title": "Example", "updatedAt": "2026-10-05"})
        self.assertEqual(body.strip(), "# Body")


if __name__ == "__main__":
    unittest.main()
