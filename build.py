#!/usr/bin/env python3
"""Build the static HTML site from the markdown docs in docs/.

Usage: python3 build.py

Reads docs/*.md (index.md becomes the landing page, chapters numbered 01-)
and writes site/*.html plus site/styles.css. No external dependencies.
"""

import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"

SITE_TITLE = "The Trust-but-Verify Manual for What AI Tells You"
SITE_TAGLINE = ("Why confident-seeming sources can be invented, how to verify "
                "them step by step, and printable worksheets to keep you honest.")


# --------------------------------------------------------------------------
# inline formatting (input is already html-escaped)
# --------------------------------------------------------------------------

def render_inline(text):
    placeholders = []

    def stash(html_fragment):
        placeholders.append(html_fragment)
        return f"\x00{len(placeholders) - 1}\x00"

    # inline code spans first, so their content is never reformatted
    text = re.sub(r"`([^`]+)`",
                  lambda m: stash(f"<code>{m.group(1)}</code>"), text)

    # links; link text may contain bold/italic, so format it recursively
    def link_sub(m):
        label, url = m.group(1), m.group(2)
        # local markdown links become links to the generated HTML pages
        if url.endswith(".md"):
            url = url[:-3] + ".html"
        return stash(f'<a href="{url}">{render_inline(label)}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link_sub, text)

    # bold then italic (bold must run first so ** inside is gone)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\s][^*]*)\*(?!\*)", r"<em>\1</em>", text)

    text = re.sub(r"\x00(\d+)\x00",
                  lambda m: placeholders[int(m.group(1))], text)
    return text


# --------------------------------------------------------------------------
# block-level markdown
# --------------------------------------------------------------------------

def render_markdown(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # fenced code block
        if line.strip().startswith("```"):
            block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1  # closing fence
            code = html.escape("\n".join(block))
            out.append(f"<pre><code>{code}</code></pre>")
            continue

        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if all(ch == "-" and True for ch in stripped) and len(stripped) >= 3:
            out.append("<hr>")
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{render_inline(html.escape(m.group(2)))}</h{level}>")
            i += 1
            continue

        # table: line starts with | and a separator row follows
        if stripped.startswith("|") and i + 1 < n \
                and re.match(r"^\|[\s\-:|]+\|?\s*$", lines[i + 1].strip()):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head_html = "".join(
                f"<th>{render_inline(html.escape(c))}</th>" for c in header)
            body = []
            for row in rows:
                body.append("<tr>" + "".join(
                    f"<td>{render_inline(html.escape(c))}</td>" for c in row) + "</tr>")
            out.append(
                "<table><thead><tr>" + head_html + "</tr></thead><tbody>"
                + "".join(body) + "</tbody></table>")
            continue

        # blockquote
        if stripped.startswith(">"):
            contents = []
            while i < n and lines[i].strip().startswith(">"):
                contents.append(lines[i].strip()[1:].strip())
                i += 1
            quoted = [render_inline(html.escape(c)) for c in contents if c]
            out.append("<blockquote><p>" + "</p><p>".join(quoted) + "</p></blockquote>")
            continue

        # ordered list
        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i].strip()))
                i += 1
            body = "".join(f"<li>{render_inline(html.escape(c))}</li>" for c in items)
            out.append(f"<ol>{body}</ol>")
            continue

        # unordered list
        if stripped.startswith(("- ", "* ")):
            items = []
            while i < n and lines[i].strip()[:2] in ("- ", "* "):
                # checkbox-style items (e.g. "- [ ]") render the bracket literally
                items.append(lines[i].strip()[2:].strip())
                i += 1
            body = "".join(f"<li>{render_inline(html.escape(c))}</li>" for c in items)
            out.append(f"<ul>{body}</ul>")
            continue

        # paragraph: gather until blank line or a new block opener
        para = [stripped]
        i += 1
        while i < n:
            s = lines[i].strip()
            if (not s or s.startswith("#") or s.startswith(">")
                    or s.startswith("|") or s.startswith("- ") or s.startswith("* ")
                    or s.startswith("```")
                    or (re.match(r"^\d+\.\s+", s) and not s.startswith(str(len(para) + 1) + ". "))
                    or (len(s) >= 3 and set(s) == {"-"})):
                break
            para.append(s)
            i += 1
        out.append("<p>" + render_inline(html.escape(" ".join(para))) + "</p>")

    return "\n".join(out)


# --------------------------------------------------------------------------
# page chrome
# --------------------------------------------------------------------------

NAV_ITEMS = [
    ("index.html", "Start Here"),
    ("01-why-confident-seeming-sources-can-be-invented.html", "1. Invented Sources"),
    ("02-the-claim-chasing-workflow.html", "2. Claim-Chasing Workflow"),
    ("03-honest-phrasing-for-uncertain-facts.html", "3. Honest Phrasing"),
    ("04-printable-source-check-worksheets.html", "4. Printable Worksheets"),
]


def page_shell(title, content, current, prev_page, next_page):
    nav_links = []
    for href, label in NAV_ITEMS:
        cls = ' class="active"' if href == current else ""
        nav_links.append(f'<a{cls} href="{href}">{label}</a>')
    nav = "\n      ".join(nav_links)

    pager = ""
    parts = []
    if prev_page:
        parts.append(f'<a class="pager-link prev" href="{prev_page[0]}">&#8592; {prev_page[1]}</a>')
    if next_page:
        parts.append(f'<a class="pager-link next" href="{next_page[0]}">{next_page[1]} &#8594;</a>')
    if parts:
        pager = '<nav class="pager">' + "\n      ".join(parts) + "\n    </nav>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(SITE_TAGLINE)}">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <a class="site-title" href="index.html">Trust-but-Verify Manual</a>
    <p class="site-tagline">Check what AI told you, before your name goes on it.</p>
    <nav class="site-nav">
      {nav}
    </nav>
  </header>

  <main class="content">
{content}
    {pager}
  </main>

  <footer class="site-footer">
    <p>The Trust-but-Verify Manual &middot; by Dylan Asdale &middot; The Massive AI Manual</p>
    <p>Copyright (c) 2026 Asdale Dynamics, LLC &middot; MIT license &middot; Educational content only &mdash; not legal, medical, or financial advice.</p>
  </footer>
</body>
</html>
"""


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------

CHAPTER_PREFIX = "01-"


def build():
    md_files = sorted(DOCS_DIR.glob("*.md"))
    if not md_files:
        raise SystemExit("No markdown files found in docs/.")

    # index first, then numbered chapters in filename order
    md_files.sort(key=lambda p: (0 if p.name == "index.md" else 1, p.name))

    titles = {}
    rendered = {}
    for path in md_files:
        page_name = path.stem + ".html"
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+?)$", text, re.MULTILINE)
        titles[page_name] = m.group(1).strip() if m else page_name
        rendered[page_name] = render_markdown(text)

    pages = list(titles.keys())
    SITE_DIR.mkdir(exist_ok=True)

    for idx, page in enumerate(pages):
        prev_page = (pages[idx - 1], titles[pages[idx - 1]]) if idx > 0 else None
        next_page = (pages[idx + 1], titles[pages[idx + 1]]) if idx < len(pages) - 1 else None
        title = titles[page]
        html_text = page_shell(
            f"{title} — Trust-but-Verify Manual",
            "    " + rendered[page],
            page, prev_page, next_page,
        )
        (SITE_DIR / page).write_text(html_text, encoding="utf-8")
        print(f"  wrote site/{page}")

    (SITE_DIR / "styles.css").write_text(CSS, encoding="utf-8")
    print("  wrote site/styles.css")
    print(f"Build complete: {len(pages)} pages.")


CSS = """:root {
  --ink: #1c2733;
  --muted: #5a6b7a;
  --paper: #fbfaf7;
  --card: #ffffff;
  --accent: #2c6e9b;
  --accent-dark: #1d4e6e;
  --rule: #e3e0d8;
  --warn: #a13d2d;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.65;
  font-size: 17px;
}

code, pre { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace; }

.site-header {
  background: var(--card);
  border-bottom: 3px solid var(--accent);
  padding: 1.6rem 1.2rem 1.1rem;
  text-align: center;
}

.site-title {
  font-size: 1.45rem;
  font-weight: bold;
  color: var(--ink);
  text-decoration: none;
  letter-spacing: 0.01em;
}

.site-tagline {
  margin: 0.3rem 0 0.9rem;
  color: var(--muted);
  font-size: 0.95rem;
  font-style: italic;
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  justify-content: center;
}

.site-nav a {
  display: inline-block;
  padding: 0.35rem 0.85rem;
  border: 1px solid var(--rule);
  border-radius: 999px;
  color: var(--accent-dark);
  text-decoration: none;
  font-size: 0.9rem;
  background: var(--paper);
}

.site-nav a.active,
.site-nav a:hover {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.content {
  max-width: 46rem;
  margin: 0 auto;
  padding: 2.2rem 1.2rem 3rem;
}

h1 { font-size: 1.9rem; line-height: 1.25; margin: 0.2rem 0 0.6rem; }
h2 { font-size: 1.35rem; margin-top: 2.2rem; border-bottom: 1px solid var(--rule); padding-bottom: 0.3rem; }
h3 { font-size: 1.12rem; margin-top: 1.7rem; }

a { color: var(--accent-dark); }

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.2rem 0;
  background: var(--card);
  font-size: 0.95rem;
}

th, td {
  border: 1px solid var(--rule);
  padding: 0.5rem 0.7rem;
  text-align: left;
  vertical-align: top;
}

thead th { background: var(--paper); }

blockquote {
  margin: 1.4rem 0;
  padding: 0.8rem 1.2rem;
  border-left: 4px solid var(--accent);
  background: var(--card);
  border-radius: 0 6px 6px 0;
  font-style: italic;
}

blockquote p { margin: 0.3rem 0; }

pre {
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 1rem;
  overflow-x: auto;
  font-size: 0.82rem;
  line-height: 1.5;
}

pre code { white-space: pre; }

hr { border: none; border-top: 1px solid var(--rule); margin: 2.2rem 0; }

.pager {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2.6rem;
}

.pager-link {
  padding: 0.6rem 1rem;
  border: 1px solid var(--rule);
  border-radius: 6px;
  text-decoration: none;
  background: var(--card);
  font-size: 0.95rem;
}

.site-footer {
  border-top: 1px solid var(--rule);
  padding: 1.4rem 1.2rem 1.8rem;
  text-align: center;
  color: var(--muted);
  font-size: 0.85rem;
}

.site-footer p { margin: 0.3rem 0; }

@media (max-width: 640px) {
  body { font-size: 16px; }
  .pager { flex-direction: column; }
}
"""


if __name__ == "__main__":
    print("Building site from docs/ ...")
    build()
