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

# routing.yaml：有 PyYAML 就真正 parse 驗型態，沒有就 fallback 結構檢查
try:
    import yaml  # type: ignore

    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False

WS = os.environ.get("REPORTER_WS", "")


def check_routing(text, where):
    if _HAS_YAML:
        try:
            d = yaml.safe_load(text)
        except Exception as e:
            fail(f"{where} YAML parse 失敗: {e}")
            return
        for k in ["primary_model", "supporting_models", "overlays",
                  "narrative_pattern", "required_artifacts",
                  "verification", "presentation"]:
            if k not in d:
                fail(f"{where} 缺 key: {k}")
        if not isinstance(d.get("supporting_models"), list):
            fail(f"{where} supporting_models 非 list")
        if not isinstance(d.get("verification"), dict):
            fail(f"{where} verification 非 mapping")
    else:
        for k in ["primary_model:", "supporting_models:", "overlays:", "narrative_pattern:",
                  "required_artifacts:", "verification:", "presentation:"]:
            if k not in text:
                fail(f"{where} 缺 key: {k}（無 PyYAML，只做結構檢查）")


try:
    check_routing(
        open(os.path.join(SAMP, "routing.sample.yaml"), encoding="utf-8-sig").read(),
        "routing sample",
    )
except Exception as e:
    fail(f"routing sample 讀取失敗: {e}")

if WS:
    rp = os.path.join(WS, "research", "routing.yaml")
    if os.path.exists(rp):
        try:
            check_routing(open(rp, encoding="utf-8-sig").read(), "workspace routing.yaml")
        except Exception as e:
            fail(f"workspace routing 讀取失敗: {e}")
    merged = []
    for fn in ["questions.jsonl", "claims.jsonl", "evidence.jsonl", "sources.jsonl"]:
        fp = os.path.join(WS, "research", fn)
        if os.path.exists(fp):
            try:
                merged.extend(
                    [json.loads(l) for l in open(fp, encoding="utf-8-sig") if l.strip()]
                )
            except Exception as e:
                fail(f"workspace {fn} parse 失敗: {e}")
    if merged:
        claims, evids, srcs, questions = {}, {}, {}, {}
        for e in merged:
            for key, store, pat in [
                ("claim_id", claims, r"C\d+"),
                ("evidence_id", evids, r"E\d+"),
                ("source_id", srcs, r"S\d+"),
                ("question_id", questions, r"Q\d+"),
            ]:
                if key in e:
                    if not re.fullmatch(pat, str(e[key])):
                        fail(f"workspace {key} 格式非法: {e[key]}")
                    store[str(e[key])] = e
        for cid, c in claims.items():
            for eid in c.get("evidence", []) + c.get("counterevidence", []):
                if eid not in evids:
                    fail(f"workspace claim {cid} 引用不存在 evidence: {eid}")
            for qid in c.get("questions", []):
                if qid not in questions:
                    fail(f"workspace claim {cid} 引用不存在 question: {qid}")
        for eid, e in evids.items():
            if e.get("source_id") not in srcs:
                fail(f"workspace evidence {eid} 引用不存在 source: {e.get('source_id')}")
        for qid, q in questions.items():
            for cid in q.get("claims", []):
                if cid not in claims:
                    fail(f"workspace question {qid} 引用不存在 claim: {cid}")

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
if pt.count("right_of_reply") != 1:
    fail("portal right_of_reply 渲染次數異常（應恰一次）")
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
