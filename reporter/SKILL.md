---
name: reporter
description: Use ONLY when the user explicitly requests reporter via /reporter or by naming reporter. Do NOT auto-load for general coding, debugging, or file edits. Takes a complex question, routes reasoning, builds traceable evidence, and ships a browsable report site.
---

# reporter

> Reporter takes a complex question, determines what kind of reasoning it requires, builds a traceable evidence model, stress-tests it, and turns it into the clearest form for human understanding.

定位：不是新聞生成器、不是 BBC 模仿器、不是 Deep Research、不是固定格式報告。Research model 決定怎麼想，Narrative model 決定怎麼讓人懂，Visual model 決定哪些關係不只靠文字講。三者分開，呈現格式不反過來決定研究方法。

## 啟動

- 題目必填，一句話。語言直接從使用者輸入推斷（寫進 `report-meta.json` 的 `lang`，不要問）。
- 研究強度由題目複雜度自動決定（見管線與廣深預設），只在使用者明確要求省成本時調低；廣度／深度選項僅做 optional override，不主動追問。
- 廣度＝方向數量：低只 cover 主幹／中主幹加兩側／高連邊角都收。
- 深度＝研究嚴格程度：低答核心問題、少量高品質來源；中測主要替代解釋、找第一手、做必要 cross-check；高完整 question coverage、alternative hypotheses、provenance tracing、adversarial search、model-specific sensitivity。來源數只是 guardrail。

## 管線

W0路由（`routing.md`）→ W1方向 → W2分片採集 → W3擴大 → W4缺口 → W5驗證 → 總報告 → W6增量更新。細節見 `references/orchestration.md`。

## 層索引

- `orchestration.md`：波次、quota、停搜、熔斷、反注入、git歷史。
- `routing.md`：W0輸出格式、source-map 穩定 ID。
- `artifacts.md`：ledger 與模型 artifact 最小 schema。
- `reasoning-models.md`：13 種研究模型定義。
- `narrative-models.md`、`visual-models.md`：敘事與視覺路由。
- `evidence.md`：Claim→Evidence→Origin、出處獨立性、來源分級。
- `verification.md`＋`data-verification.md`：查核與數字解讀。
- `editorial-standards.md`：按模型審稿、強弱約束分級。
- `writing.md`：寫作鐵律、敘事、標題數字、frontmatter、來源寫法。
- `presentation.md`：閱讀器、入口頁、meta/gaps/source-map、圖表。

## 最高鐵律

- Strong constraints on truth；weak constraints on storytelling。
- 正文只留結果；過程 metadata 永不進正文；material uncertainty 在最接近相關 claim 的位置呈現，全局限制才集中整理。
- 同一規則只有一個 authoritative definition，其他文件用引用指向它。
