#!/usr/bin/env python3
"""Check public QX modules and write a small status report.

QX itself downloads every enabled remote module using its update-interval.
This script keeps the public repository's upstream health visible without
copying private subscriptions or upstream content into this repository.
"""
from __future__ import annotations

import hashlib
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://[^\s,]+")
urls: list[str] = []
for config in ROOT.glob("*.conf"):
    for url in URL_RE.findall(config.read_text(encoding="utf-8")):
        if "example.com" not in url and "你的私有订阅" not in url:
            urls.append(url.split("#", 1)[0])

rows = []
for url in sorted(set(urls)):
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "qx-upstream-check/1.0"})
        with urllib.request.urlopen(req, timeout=8) as response:
            body = b""
            digest = hashlib.sha256(body).hexdigest()[:12]
            rows.append(f"| `{url}` | {response.status} | `{digest}` |")
    except Exception as exc:  # status reporting should not hide the other URLs
        rows.append(f"| `{url}` | error | `{type(exc).__name__}` |")

stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
report = "# 上游模块状态\n\n"
report += f"最后检查：{stamp}\n\n"
report += "QX 会按照配置中的 `update-interval` 自动更新模块；本表只记录公开模块可访问性和内容摘要。\n\n"
report += "| 模块地址 | HTTP | SHA-256 前 12 位 |\n|---|---:|---|\n"
report += "\n".join(rows) + "\n"
(ROOT / "UPSTREAM_STATUS.md").write_text(report, encoding="utf-8")
