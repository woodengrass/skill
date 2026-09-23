---
name: reporter
description: Use ONLY when the user explicitly requests reporter via /reporter or by naming reporter. Do NOT auto-load for general coding, debugging, or file edits. Takes a complex question, researches it to defined breadth and depth, preserves evidence quality and provenance, and ships a browsable report site under a strict publishing contract.
---

# reporter

> Reporter 不替強 agent 規定研究步驟；它規範研究必須達到的廣度、深度與證據品質，提供可選的方法庫，並對最終文章的可查證性、清晰度與呈現品質做強約束。

> Reporter does not prescribe how a capable agent must research. It defines how broad and deep the research should be, provides optional reasoning and verification methods, preserves evidence quality and provenance, and enforces a high-quality final publishing contract.

定位：research quality + evidence + publishing harness for strong agents。不是固定研究流程（workflow for doing research）。

> **A lightweight research quality and publishing toolkit for strong agents.**

核心哲學（三句，細則各有歸屬，不在別處重述）：

> **Strong constraints on evidence; weak constraints on research path.**（見 `orchestration.md`）
> **Strong constraints on truth; weak constraints on narrative structure.**（見 `verification.md`、`narrative-models.md`）
> **Strong constraints on clarity and integrity; weak constraints on format and layout.**（見 `writing.md`、`presentation.md`）

Research freedom + Breadth / Depth targets + Truth invariants + Optional method library + Strict output contract。

## 輸入

- 題目必填，一句話。語言直接從使用者輸入推斷（寫進 `report-meta.json` 的 `lang`，不要問）。
- 研究強度由題目複雜度自動決定，只在使用者明確要求省成本時調低；廣度／深度選項僅做 optional override，不主動追問。

## Breadth / Depth quality target

**Breadth**＝是否覆蓋所有可能 materially change the answer 的重要面向，不用方向數、agent 數、來源篇數衡量。高廣度通常意味著有考慮：核心面向、competing explanations、credible alternatives、relevant stakeholders／geography／populations、important exceptions、temporal changes、dependencies、different evidence families、original question 的 hidden premises。以上是方法提示，不是每案 checklist。

**Depth**＝是否對 load-bearing questions 深入到足以可靠理解、驗證並解釋其機制、證據與不確定性，不用輪數、篇數、evidence 條數衡量。高深度通常意味：重要主張優先追近原始資料、不停留在摘要與轉述、理解資料口徑與方法、處理矛盾證據、必要時測試主要 alternative explanations、必要時讀長文件論文財報法規原始資料、找不到時保留 unresolved。仍然不要規定數量。

## Research freedom

Agent 自由選擇工具、拆分方式、搜尋策略、agent 數量、執行順序、迭代方式、內部筆記形式。`orchestration.md` 的階段只是常見研究階段的概念分類，不是 mandatory execution order；可自由搜尋、拆題、重排、回頭、並行、reframe、重做。推理模型、敘事模型、視覺模型、artifacts 全部是可選方法庫。

## Epistemic sequencing（決策時機原則，細則見 `orchestration.md`）

> **Fix the question early; commit to the research model only after sufficient orientation; keep the research plan revisable as evidence arrives; commit to the final narrative only after the evidence model is stable enough to support it.**

> **問題早定、方法晚定且可改、證據持續更新模型、故事最後才定。**

## Truth invariants（不可談判）

- Strong constraints on truth；weak constraints on storytelling。
- Claim → Evidence → Origin：每個結論主張能追到證據，每份證據標出真正生產資訊的出處。
- 不同 URL 不等於獨立證據；同一出處的轉載只算一個 evidence family。
- 正文只留結果；過程 metadata 永不進正文；material uncertainty 在最接近相關 claim 的位置呈現，全局限制才集中整理。
- 同一規則只有一個 authoritative definition，其他文件用引用指向它。

## Output contract（強約束在最終輸出）

最終成品必須滿足 `writing.md` 的寫作鐵律與 `presentation.md` 的 hard invariants：真正回答 central question；依人類理解順序組織；load-bearing claims 可追到來源；material uncertainty 就近揭露；分歧與 gaps 不藏；數字口徑正確；quote／scene 不得虛構；不用虛假精確的 confidence／overall score；圖表不誤導；來源與更新狀態可查；有真正的 explanatory structure，不是 research dump。

## 開發原則（改 skill 本身時）

> **Do not add a new model, artifact, state, role, gate, or output mode unless repeated real-world failures show that the existing system cannot represent the problem cleanly.**

> **沒有真實案例反覆證明現有架構不夠，就不要再增加抽象層。**

## 層索引（每條規則只有一個家，他處只引用）

- `orchestration.md`：研究決策 timing／adaptive research。
- `routing.md`：reasoning lens 表示法。
- `artifacts.md`：ledger 與模型 artifact schema（用才守格式）。
- `reasoning-models.md`：13 種研究方法（方法庫，可組合、可棄用、可自創）。
- `narrative-models.md`：storytelling 方法庫。
- `visual-models.md`：視覺靈感庫。
- `evidence.md`：Claim→Evidence→Origin、出處獨立性、claim-relative 來源品質。
- `verification.md`＋`data-verification.md`：結果要求（查什麼，不規定儀式）。
- `editorial-standards.md`：審稿視角、強弱約束分級。
- `writing.md`：寫作鐵律（強契約）。
- `presentation.md`：呈現原則＋可選工具（強約束只剩 hard invariants）。
