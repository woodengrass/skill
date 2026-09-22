---
name: reporter
description: Use ONLY when the user explicitly requests reporter via /reporter or by naming reporter. Do NOT auto-load for general coding, debugging, or file edits. Takes a complex question, researches it to defined breadth and depth, preserves evidence quality and provenance, and ships a browsable report site under a strict publishing contract.
---

# reporter

> Reporter 不替強 agent 規定研究步驟；它規範研究必須達到的廣度、深度與證據品質，提供可選的方法庫，並對最終文章的可查證性、清晰度與呈現品質做強約束。

> Reporter does not prescribe how a capable agent must research. It defines how broad and deep the research should be, provides optional reasoning and verification methods, preserves evidence quality and provenance, and enforces a high-quality final publishing contract.

定位：research quality + evidence + publishing harness for strong agents。不是固定研究流程（workflow for doing research）。

Research freedom + Breadth / Depth targets + Truth invariants + Optional method library + Strict output contract。

## 輸入

- 題目必填，一句話。語言直接從使用者輸入推斷（寫進 `report-meta.json` 的 `lang`，不要問）。
- 研究強度由題目複雜度自動決定，只在使用者明確要求省成本時調低；廣度／深度選項僅做 optional override，不主動追問。

## Breadth / Depth quality target

**Breadth**＝是否覆蓋所有可能 materially change the answer 的重要面向，不用方向數、agent 數、來源篇數衡量。高廣度通常意味著有考慮：核心面向、competing explanations、credible alternatives、relevant stakeholders／geography／populations、important exceptions、temporal changes、dependencies、different evidence families、original question 的 hidden premises。以上是方法提示，不是每案 checklist。

**Depth**＝是否對 load-bearing questions 深入到足以可靠理解、驗證並解釋其機制、證據與不確定性，不用輪數、篇數、evidence 條數衡量。高深度通常意味：重要主張優先追近原始資料、不停留在摘要與轉述、理解資料口徑與方法、處理矛盾證據、必要時測試主要 alternative explanations、必要時讀長文件論文財報法規原始資料、找不到時保留 unresolved。仍然不要規定數量。

## Research freedom

Agent 自由選擇工具、拆分方式、搜尋策略、agent 數量、執行順序、迭代方式、內部筆記形式。`orchestration.md` 的階段只是常見研究階段的概念分類，不是 mandatory execution order；可自由搜尋、拆題、重排、回頭、並行、reframe、重做。推理模型、敘事模型、視覺模型、artifacts 全部是可選方法庫。

## Epistemic sequencing（決策時機原則）

> **Fix the question early; commit to the research model only after sufficient orientation; keep the research plan revisable as evidence arrives; commit to the final narrative only after the evidence model is stable enough to support it.**

> **問題早定、方法晚定且可改、證據持續更新模型、故事最後才定。**

即：**Stable question, flexible plan, evidence-informed reasoning, late-bound storytelling.**

- Question Contract（要回答什麼、意圖、明確約束、已知範圍／時間／地理／對象、已知歧義）早固定；它不是正式研究計畫。
- 不熟悉／含糊／多層／快速變化題目先做必要的 Orientation／Reconnaissance，再決定 working research model；熟悉且結構明確題目可直接研究，禁止為形式硬做 reconnaissance。
- Research plan 是 mutable external state，隨證據可改；reasoning lens 從 candidate → working → stable 演化，即使 stable，重大證據仍可 reframe。
- Exploratory findings 只產生 candidate hypothesis／question，不自動驗證 load-bearing conclusion。
- Final narrative 與 reader visual 原則上 late binding：等 load-bearing evidence 與 reasoning model 實質穩定後，才由 Story Architect 決定。
- 目標是 epistemic readiness，不是 process compliance。細則見 `orchestration.md`、`routing.md`。

## Truth invariants（不可談判）

- Strong constraints on truth；weak constraints on storytelling。
- Claim → Evidence → Origin：每個結論主張能追到證據，每份證據標出真正生產資訊的出處。
- 不同 URL 不等於獨立證據；同一出處的轉載只算一個 evidence family。
- 正文只留結果；過程 metadata 永不進正文；material uncertainty 在最接近相關 claim 的位置呈現，全局限制才集中整理。
- 同一規則只有一個 authoritative definition，其他文件用引用指向它。

## Output contract（強約束在最終輸出）

最終成品必須滿足 `writing.md`、`presentation.md`、`editorial-standards.md` 的全部 hard requirements：真正回答 central question；依人類理解順序組織；load-bearing claims 可追到來源；material uncertainty 就近揭露；分歧與 gaps 不藏；數字口徑正確；quote／scene 不得虛構；不用虛假精確的 confidence／overall score；圖表不誤導；來源與更新狀態可查；有真正的 explanatory structure，不是 research dump。

## 層索引

- `orchestration.md`：Research Guidance（heuristics＋停搜判斷＋反注入＋git歷史）。
- `routing.md`：可選的 reasoning-lens working note。
- `artifacts.md`：ledger 與模型 artifact schema（用才守格式）。
- `reasoning-models.md`：13 種研究方法（方法庫，可組合、可棄用、可自創）。
- `narrative-models.md`、`visual-models.md`：敘事與視覺方法庫。
- `evidence.md`：Claim→Evidence→Origin、出處獨立性、claim-relative 來源品質。
- `verification.md`＋`data-verification.md`：結果要求（查什麼，不規定儀式）。
- `editorial-standards.md`：審稿視角、強弱約束分級。
- `writing.md`：寫作鐵律（強契約）。
- `presentation.md`：閱讀器、入口頁、meta/gaps/source-map、圖表。
