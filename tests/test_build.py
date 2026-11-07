"""Verification suite for the Trust-but-Verify Manual.

Run with:  python3 -m unittest discover tests -v
"""

import pathlib
import re
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"
LICENSE_FILE = ROOT / "LICENSE"
README_FILE = ROOT / "README.md"

REQUIRED_PAGES = [
    "index.html",
    "01-why-confident-seeming-sources-can-be-invented.html",
    "02-the-claim-chasing-workflow.html",
    "03-honest-phrasing-for-uncertain-facts.html",
    "04-printable-source-check-worksheets.html",
]


class TestBuild(unittest.TestCase):
    """build.py runs and produces a complete site."""

    def test_build_script_runs_cleanly(self):
        result = subprocess.run(
            [sys.executable, "build.py"],
            cwd=ROOT, capture_output=True, text=True, timeout=120,
        )
        self.assertEqual(result.returncode, 0,
                         f"build.py failed:\n{result.stdout}\n{result.stderr}")

    def test_generated_pages_exist(self):
        for page in REQUIRED_PAGES:
            self.assertTrue((SITE_DIR / page).is_file(), f"missing site/{page}")

    def test_stylesheet_exists(self):
        self.assertTrue((SITE_DIR / "styles.css").is_file())

    def test_meta_includes_required_line(self):
        html_text = (SITE_DIR / REQUIRED_PAGES[0]).read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", html_text)


class TestGeneratedHtml(unittest.TestCase):
    """The generated HTML looks structurally sane and links resolve."""

    def setUp(self):
        self.pages = {
            p.name: p.read_text(encoding="utf-8")
            for p in SITE_DIR.glob("*.html")
        }

    def test_pages_are_well_formed_enough(self):
        for name, text in self.pages.items():
            with self.subTest(page=name):
                self.assertIn("<!DOCTYPE html>", text)
                self.assertIn("</html>", text)
                self.assertEqual(text.count("<main"), 1)
                self.assertEqual(text.count("</main>"), 1)

    def test_internal_links_resolve(self):
        for name, text in self.pages.items():
            for href in re.findall(r'href="([^"#]+)"', text):
                if href.startswith(("http://", "https://")) or href == "styles.css":
                    continue
                with self.subTest(page=name, link=href):
                    self.assertTrue((SITE_DIR / href).is_file(),
                                    f"broken link {href!r} in {name}")

    def test_nav_covers_all_pages(self):
        landing = self.pages["index.html"]
        for page in REQUIRED_PAGES[1:]:
            self.assertIn(page, landing, f"index does not link {page}")

    def test_chapters_have_prev_next_pager(self):
        for name, text in self.pages.items():
            if name == "index.html":
                continue
            with self.subTest(page=name):
                self.assertIn('class="pager"', text)

    def test_rendered_elements_present(self):
        text = "".join(self.pages.values())
        self.assertIn("<table>", text)
        self.assertIn("<blockquote>", text)
        self.assertIn("<pre><code>", text)
        self.assertIn("<ol>", text)
        self.assertIn("<hr>", text)
        self.assertIn("<strong>", text)

    def test_worksheet_page_keeps_code_blocks(self):
        text = self.pages["04-printable-source-check-worksheets.html"]
        self.assertIn("Claim Ledger", text)
        self.assertIn("Checked (date/init)", text)


class TestSourceDocs(unittest.TestCase):
    """The markdown sources carry the full intended content."""

    DOCS = [
        "index.md",
        "01-why-confident-seeming-sources-can-be-invented.md",
        "02-the-claim-chasing-workflow.md",
        "03-honest-phrasing-for-uncertain-facts.md",
        "04-printable-source-check-worksheets.md",
    ]

    def test_all_docs_exist(self):
        for name in self.DOCS:
            self.assertTrue((DOCS_DIR / name).is_file(), f"missing docs/{name}")

    def test_docs_link_to_each_other(self):
        total_links = 0
        for name in self.DOCS:
            text = (DOCS_DIR / name).read_text(encoding="utf-8")
            total_links += len(re.findall(r"\]\(\d", text))
        # cross-chapter links (e.g. "](02-the-claim-chasing-workflow.md)")
        self.assertGreaterEqual(total_links, 6)

    def test_worksheets_include_all_five(self):
        text = (DOCS_DIR / "04-printable-source-check-worksheets.md").read_text(
            encoding="utf-8")
        for sheet in ("Worksheet 1", "Worksheet 2", "Worksheet 3",
                      "Worksheet 4", "Worksheet 5"):
            self.assertIn(sheet, text)

    def test_hedging_chapter_has_phrasebook(self):
        text = (DOCS_DIR / "03-honest-phrasing-for-uncertain-facts.md").read_text(
            encoding="utf-8")
        for phrase in ("Based on my own experience", "There's genuine debate",
                       "I don't know", "As of"):
            self.assertIn(phrase, text)


class TestProjectArtifacts(unittest.TestCase):
    """LICENSE, README, and repo hygiene."""

    def test_license_is_mit_with_exact_copyright(self):
        text = LICENSE_FILE.read_text(encoding="utf-8")
        self.assertIn("MIT License", text)
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text)
        self.assertNotIn("Co-authored-by", text)

    def test_readme_credits_asdale_dynamics(self):
        text = README_FILE.read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", text)

    def test_no_secrets_in_tracked_files(self):
        secret_patterns = [
            r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}",
            r"ghp_[A-Za-z0-9]{20,}",
            r"sk-[A-Za-z0-9]{20,}",
            r"AKIA[0-9A-Z]{16}",
        ]
        skip_dirs = {".git", "site", "__pycache__"}
        offenders = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix in {".pyc", ".pyo"}:
                continue
            if any(dir_name in path.relative_to(ROOT).parts for dir_name in skip_dirs):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in secret_patterns:
                if re.search(pattern, text):
                    offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual(offenders, [], f"possible secrets in: {offenders}")


if __name__ == "__main__":
    unittest.main()
