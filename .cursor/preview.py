#!/usr/bin/env python3
"""Offline GitHub-style preview server for this profile repository.

Renders README.md locally (no GitHub API call, so no rate limits and no token
or secret required) and serves it with GitHub-like styling. Files referenced
with relative paths (for example ``header.svg``) are served straight from the
repository root so the banner and other local assets resolve. The README is
re-rendered on every request, so saving an edit and refreshing the browser
shows the change immediately.

Usage:
    python3 .cursor/preview.py            # serves on 0.0.0.0:6419
    PREVIEW_PORT=8080 python3 .cursor/preview.py

Environment variables:
    PREVIEW_HOST   interface to bind (default 0.0.0.0)
    PREVIEW_PORT   port to bind (default 6419)
"""

from __future__ import annotations

import os
import re
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import markdown

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")
HOST = os.environ.get("PREVIEW_HOST", "0.0.0.0")
PORT = int(os.environ.get("PREVIEW_PORT", "6419"))

MD_EXTENSIONS = [
    "tables",
    "fenced_code",
    "codehilite",
    "sane_lists",
    "md_in_html",
    "attr_list",
]
MD_EXTENSION_CONFIGS = {
    "codehilite": {"guess_lang": False, "noclasses": True},
}

# GitHub renders Markdown found inside block-level HTML such as
# ``<div align="center">`` even though the tag carries no ``markdown``
# attribute. Python-Markdown's md_in_html only descends into a tag when that
# attribute is present, so inject it into container tags before rendering.
_DIV_OPEN = re.compile(r"<(div|details|summary)\b(?![^>]*\bmarkdown=)([^>]*)>", re.IGNORECASE)


def _enable_markdown_in_html(text: str) -> str:
    return _DIV_OPEN.sub(r'<\1 markdown="1"\2>', text)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>README preview</title>
<style>{css}</style>
</head>
<body>
<div class="page">
  <div class="filename">README.md</div>
  <article class="markdown-body">
{body}
  </article>
</div>
</body>
</html>"""

# Compact GitHub-like stylesheet (self-contained, no external fetch) so the
# preview renders consistently offline.
CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #f6f8fa;
  color: #1f2328;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
}
.page { max-width: 1012px; margin: 32px auto; padding: 0 16px; }
.filename {
  font: 12px/1.4 ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  color: #59636e; background: #f6f8fa; border: 1px solid #d1d9e0;
  border-bottom: none; border-radius: 6px 6px 0 0; padding: 8px 16px;
}
.markdown-body {
  background: #ffffff; border: 1px solid #d1d9e0; border-radius: 0 0 6px 6px;
  padding: 32px 40px; font-size: 16px; line-height: 1.5; word-wrap: break-word;
}
.markdown-body > *:first-child { margin-top: 0; }
.markdown-body h1, .markdown-body h2, .markdown-body h3,
.markdown-body h4, .markdown-body h5, .markdown-body h6 {
  margin: 24px 0 16px; font-weight: 600; line-height: 1.25;
}
.markdown-body h1 { font-size: 2em; padding-bottom: .3em; border-bottom: 1px solid #d1d9e0; }
.markdown-body h2 { font-size: 1.5em; padding-bottom: .3em; border-bottom: 1px solid #d1d9e0; }
.markdown-body h3 { font-size: 1.25em; }
.markdown-body p, .markdown-body ul, .markdown-body ol, .markdown-body table { margin: 0 0 16px; }
.markdown-body a { color: #0969da; text-decoration: none; }
.markdown-body a:hover { text-decoration: underline; }
.markdown-body img { max-width: 100%; vertical-align: middle; }
.markdown-body hr { height: .25em; margin: 24px 0; background: #d1d9e0; border: 0; }
.markdown-body sub { font-size: 75%; color: #59636e; }
.markdown-body code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  font-size: 85%; background: rgba(129,139,152,.12); padding: .2em .4em; border-radius: 6px;
}
.markdown-body pre {
  background: #f6f8fa; border-radius: 6px; padding: 16px; overflow: auto;
  font-size: 85%; line-height: 1.45;
}
.markdown-body pre code { background: transparent; padding: 0; font-size: 100%; white-space: pre; }
.markdown-body table { border-collapse: collapse; display: block; width: max-content; max-width: 100%; overflow: auto; }
.markdown-body table th, .markdown-body table td { padding: 6px 13px; border: 1px solid #d1d9e0; }
.markdown-body table th { font-weight: 600; background: #f6f8fa; }
.markdown-body table tr:nth-child(2n) { background: #f6f8fa; }
.markdown-body blockquote {
  margin: 0 0 16px; padding: 0 1em; color: #59636e; border-left: .25em solid #d1d9e0;
}
"""


def render_readme() -> str:
    with open(README, encoding="utf-8") as handle:
        text = handle.read()
    text = _enable_markdown_in_html(text)
    body = markdown.markdown(
        text,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
        output_format="html5",
    )
    return PAGE.format(css=CSS, body=body)


class PreviewHandler(SimpleHTTPRequestHandler):
    """Serve the rendered README at ``/`` and repo files everywhere else."""

    def do_GET(self):  # noqa: N802 (http.server API)
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        if path in ("/", "/index.html", "/README.md"):
            payload = render_readme().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()


def main() -> None:
    handler = partial(PreviewHandler, directory=REPO_ROOT)
    with ThreadingHTTPServer((HOST, PORT), handler) as httpd:
        print(f"README preview (offline) serving {README}", flush=True)
        print(f"  -> http://{HOST}:{PORT}/  (Ctrl+C to stop)", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
