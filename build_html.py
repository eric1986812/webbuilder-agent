#!/usr/bin/env python3
"""把工作流 markdown 转成漂亮的 HTML，方便老板浏览器打开。"""
import markdown
from pathlib import Path

ROOT = Path("/Users/macadmin/Desktop/AI项目/海外网站开发Agent")
MD_PATH = ROOT / "工作流-完整版.md"
HTML_PATH = ROOT / "工作流-完整版.html"

CSS = """
:root {
  --bg: #f8fafc;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --brand: #2563eb;
  --brand-soft: #dbeafe;
  --accent: #f59e0b;
  --good: #16a34a;
  --bad: #dc2626;
  --warn: #f97316;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 1080px; margin: 0 auto; padding: 40px 28px 80px; }

h1 { font-size: 36px; line-height: 1.3; margin: 0 0 12px; letter-spacing: -0.02em; }
h2 {
  font-size: 26px;
  margin: 56px 0 16px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--line);
}
h3 { font-size: 20px; margin: 32px 0 12px; color: var(--brand); }
h4 { font-size: 16px; margin: 24px 0 8px; color: var(--muted); }

blockquote {
  margin: 16px 0;
  padding: 16px 20px;
  background: var(--brand-soft);
  border-left: 4px solid var(--brand);
  border-radius: 0 8px 8px 0;
  color: #1e3a8a;
}
blockquote p { margin: 4px 0; }

p { margin: 12px 0; }
strong { color: var(--ink); font-weight: 700; }
em { color: var(--muted); }

hr { border: none; border-top: 1px dashed var(--line); margin: 32px 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0 24px;
  background: var(--card);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(15,23,42,0.06);
}
th, td { padding: 12px 14px; text-align: left; border-bottom: 1px solid var(--line); font-size: 14px; }
th { background: #f1f5f9; color: var(--ink); font-weight: 600; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: #f8fafc; }

ul, ol { padding-left: 22px; }
li { margin: 6px 0; }

code {
  font-family: "SF Mono", Menlo, monospace;
  background: #f1f5f9;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 13px;
  color: #be185d;
}

pre {
  background: #0f172a;
  color: #f1f5f9;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  font-size: 13px;
  line-height: 1.5;
}
pre code { background: transparent; color: inherit; padding: 0; }

.meta {
  background: var(--card);
  padding: 20px;
  border-radius: 12px;
  margin: 16px 0 32px;
  border: 1px solid var(--line);
}
.meta p { margin: 4px 0; color: var(--muted); font-size: 14px; }

.toc {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 20px 28px;
  margin: 24px 0 40px;
}
.toc h4 { margin: 0 0 12px; color: var(--ink); }
.toc ul { columns: 2; column-gap: 32px; padding-left: 20px; }
.toc li { break-inside: avoid; font-size: 14px; }

.tag {
  display: inline-block;
  padding: 2px 8px;
  background: var(--brand-soft);
  color: var(--brand);
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  margin-right: 6px;
}

@media (max-width: 720px) {
  .wrap { padding: 20px 16px 60px; }
  h1 { font-size: 26px; }
  h2 { font-size: 20px; }
  .toc ul { columns: 1; }
  table { font-size: 13px; }
  th, td { padding: 8px 10px; }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>海外网站开发 Agent — 完整工作流 v1.0</title>
<style>{css}</style>
</head>
<body>
<div class="wrap">
{body}
</div>
</body>
</html>
"""


def main():
    md_text = MD_PATH.read_text(encoding="utf-8")
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists", "nl2br"]
    )
    body = md.convert(md_text)
    html = HTML_TEMPLATE.format(css=CSS, body=body)
    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"OK: {HTML_PATH} ({HTML_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
