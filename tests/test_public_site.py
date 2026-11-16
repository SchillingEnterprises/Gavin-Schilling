"""Dependency-free checks for the public root website and its service pages."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGES = [
    ROOT / "index.html",
    ROOT / "about.html",
    ROOT / "contact.html",
    ROOT / "insights.html",
    ROOT / "privacy.html",
    ROOT / "services.html",
    ROOT / "work.html",
    ROOT / "404.html",
    *sorted((ROOT / "services").glob("*.html")),
]


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.images_without_alt = []
        self.external_blank_links_without_noopener = []
        self.lang = None
        self.title_seen = False
        self.viewport_seen = False
        self.main_seen = False
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "title":
            self._in_title = True
        if tag == "meta" and attrs.get("name", "").lower() == "viewport":
            self.viewport_seen = True
        if tag == "main":
            self.main_seen = True
        for key in ("href", "src"):
            value = attrs.get(key, "")
            if value:
                self.references.append(value)
        if tag == "img" and "alt" not in attrs:
            self.images_without_alt.append(attrs.get("src", "(unnamed image)"))
        if tag == "a" and attrs.get("target") == "_blank":
            rel = set(attrs.get("rel", "").lower().split())
            if "noopener" not in rel:
                self.external_blank_links_without_noopener.append(attrs.get("href", "(missing href)"))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title and data.strip():
            self.title_seen = True


class PublicWebsiteTests(unittest.TestCase):
    def test_expected_public_pages_exist(self):
        for page in PUBLIC_PAGES:
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertTrue(page.is_file())

    def test_every_public_page_has_document_basics(self):
        for page in PUBLIC_PAGES:
            parser = PageAudit()
            parser.feed(page.read_text(encoding="utf-8"))
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertTrue(parser.lang, "HTML language is required")
                self.assertTrue(parser.title_seen, "A descriptive document title is required")
                self.assertTrue(parser.viewport_seen, "Responsive viewport metadata is required")
                self.assertTrue(parser.main_seen, "A main landmark is required")

    def test_all_local_links_and_assets_resolve_inside_repository(self):
        failures = []
        root = ROOT.resolve()
        for page in PUBLIC_PAGES:
            parser = PageAudit()
            parser.feed(page.read_text(encoding="utf-8"))
            for reference in parser.references:
                parsed = urlsplit(reference)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                if reference.startswith(("#", "data:")):
                    continue
                target = (page.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(root):
                    failures.append(f"{page.relative_to(ROOT)} escapes repository: {reference}")
                elif not target.exists():
                    failures.append(f"{page.relative_to(ROOT)} -> missing {reference}")
        self.assertEqual(failures, [], "\\n".join(failures))

    def test_images_have_alt_attributes(self):
        failures = []
        for page in PUBLIC_PAGES:
            parser = PageAudit()
            parser.feed(page.read_text(encoding="utf-8"))
            if parser.images_without_alt:
                failures.append(f"{page.relative_to(ROOT)}: {parser.images_without_alt}")
        self.assertEqual(failures, [])

    def test_new_tab_links_prevent_opener_access(self):
        failures = []
        for page in PUBLIC_PAGES:
            parser = PageAudit()
            parser.feed(page.read_text(encoding="utf-8"))
            for href in parser.external_blank_links_without_noopener:
                failures.append(f"{page.relative_to(ROOT)}: {href}")
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
