"""reporter skill 自檢：掃描 SKILL.md / references / assets 的 drift。

用法：python check.py（在 skill 根目錄跑）
失敗即列出違規，不合規則就修到通過為止。
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REFS = os.path.join(ROOT, "references")
ASSETS = os.path.join(ROOT, "assets")
errors = []


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8-sig") as f:
        return f.read()


def fail(msg):
    errors.append(msg)


# 1. JSON / YAML 可解析（workspace 執行期產物若存在也驗）
for rel in ["report-meta.json", "gaps.json", "source-map.json"]:
    p = os.path.join(ROOT, rel)
    if os.path.exists(p):
        try:
            json.load(open(p, encoding="utf-8-sig"))
        except Exception as e:
            fail(f"{rel} JSON parse 失敗: {e}")

# 2. 文件存在性
for rel in [
    "SKILL.md",
    "references/orchestration.md",
    "references/routing.md",
    "references/reasoning-models.md",
    "references/narrative-models.md",
    "references/visual-models.md",
    "references/evidence.md",
    "references/verification.md",
    "references/data-verification.md",
    "references/editorial-standards.md",
    "references/writing.md",
    "references/presentation.md",
    "assets/reader-template.html",
    "assets/portal-template.html",
    "assets/libs/echarts.min.js",
    "assets/libs/taiwan-counties.geojson",
]:
    if not os.path.exists(os.path.join(ROOT, rel)):
        fail(f"缺檔案: {rel}")

# 3. 舊規則 denylist（任一出現即 fail）
DENY = [
    "反方證據已找到",
    "每節三件套",
    "連2段數字必接1段人",
    "一個人一時一事",
    "更新日誌",
    "快照＋日誌",
    "看法報",
    "同行評議預印本",
    "82 / 100",
]
for dp, _, fns in os.walk(REFS):
    for fn in sorted(fns):
        if not fn.endswith(".md"):
            continue
        t = read(os.path.join("references", fn))
        for d in DENY:
            if d in t:
                fail(f"{fn} 含 legacy: {d}")

# 4. 模板 placeholder 與實作一致
rt = read("assets/reader-template.html")
for ph in ["__TITLE__", "__NAV__", "__PDFS__", "__HOME__"]:
    if ph not in rt:
        fail(f"reader-template 缺 {ph}")
for feat in ["getSrcMap", "initCharts", "numberSources", "passage-anchor"]:
    if feat not in rt:
        fail(f"reader-template 缺實作: {feat}")
pt = read("assets/portal-template.html")
for feat in ["report-meta.json", "gaps.json", "document.title", "documentElement.lang"]:
    if feat not in pt:
        fail(f"portal-template 缺實作: {feat}")
if "新竹" in pt or "MOTC" in pt:
    fail("portal-template 有特定研究殘留")

# 5. meta schema 一致（presentation 宣稱的欄位 portal 真的讀）
for field in ["title", "verdict", "summary", "trust", "kpis", "charts", "chapters"]:
    if field not in pt:
        fail(f"portal 未讀 meta 欄位: {field}")

print(f"checked, errors={len(errors)}")
for e in errors:
    print("FAIL:", e)
sys.exit(1 if errors else 0)
