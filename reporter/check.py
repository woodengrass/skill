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


# 1. JSON 可解析＋schema 驗證
for rel in ["report-meta.json", "gaps.json", "source-map.json"]:
    p = os.path.join(ROOT, rel)
    if os.path.exists(p):
        try:
            json.load(open(p, encoding="utf-8-sig"))
        except Exception as e:
            fail(f"{rel} JSON parse 失敗: {e}")

SAMP = os.path.join(ASSETS, "schema-samples")
try:
    meta = json.load(open(os.path.join(SAMP, "report-meta.sample.json"), encoding="utf-8-sig"))
    for f in ["title", "date", "verdict", "lang", "summary", "trust", "kpis", "charts", "chapters"]:
        if f not in meta:
            fail(f"meta sample 缺欄位: {f}")
    for f in ["cutoff", "sources", "original_ratio", "unresolved", "right_of_reply", "changelog"]:
        if f not in meta.get("trust", {}):
            fail(f"meta trust 缺欄位: {f}")
except Exception as e:
    fail(f"meta sample 讀取失敗: {e}")

try:
    gaps = json.load(open(os.path.join(SAMP, "gaps.sample.json"), encoding="utf-8-sig"))
    for i, g in enumerate(gaps):
        if "item" not in g:
            fail(f"gaps sample[{i}] 缺 item")
        if g.get("status") not in ("pending", "dropped", "deferred"):
            fail(f"gaps sample[{i}] status 非法: {g.get('status')}")
except Exception as e:
    fail(f"gaps sample 讀取失敗: {e}")

try:
    sm = json.load(open(os.path.join(SAMP, "source-map.sample.json"), encoding="utf-8-sig"))
    for i, e in enumerate(sm):
        if not re.fullmatch(r"P\d+", e.get("id", "")):
            fail(f"source-map sample[{i}] id 非 P0001 格式: {e.get('id')}")
        if "passage" not in e or "sources" not in e:
            fail(f"source-map sample[{i}] 缺 passage/sources")
except Exception as e:
    fail(f"source-map sample 讀取失敗: {e}")

# routing.yaml 結構檢查（無 PyYAML 依賴，只驗必要 key 行）
try:
    ry = open(os.path.join(SAMP, "routing.sample.yaml"), encoding="utf-8-sig").read()
    for k in ["primary_model:", "supporting_models:", "overlays:", "narrative_pattern:",
              "required_artifacts:", "verification:", "presentation:"]:
        if k not in ry:
            fail(f"routing sample 缺 key: {k}")
except Exception as e:
    fail(f"routing sample 讀取失敗: {e}")

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

# 3. 舊規則 denylist（任一出現即 fail，含 SKILL）
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
    "不確定性只進固定位置",
]
for dp, _, fns in os.walk(REFS):
    for fn in sorted(fns):
        if not fn.endswith(".md"):
            continue
        t = read(os.path.join("references", fn))
        for d in DENY:
            if d in t:
                fail(f"{fn} 含 legacy: {d}")
t = read("SKILL.md")
for d in DENY:
    if d in t:
        fail(f"SKILL.md 含 legacy: {d}")

# 4. 模板 placeholder 與實作一致
rt = read("assets/reader-template.html")
for ph in ["__TITLE__", "__NAV__", "__PDFS__", "__HOME__"]:
    if ph not in rt:
        fail(f"reader-template 缺 {ph}")
for feat in ["getSrcMap", "initCharts", "numberSources", "passage-anchor"]:
    if feat not in rt:
        fail(f"reader-template 缺實作: {feat}")
pt = read("assets/portal-template.html")
for feat in ["report-meta.json", "gaps.json", "document.title", "documentElement.lang", "safeUrl"]:
    if feat not in pt:
        fail(f"portal-template 缺實作: {feat}")
rt = read("assets/reader-template.html")
if "safeUrl" not in rt:
    fail("reader-template 缺 safeUrl")
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
