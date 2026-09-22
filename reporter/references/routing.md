# Routing（optional working note：provisional → evidence-informed）

Router 判斷「這個問題需要什麼認知操作」，不靠關鍵字硬對（「為什麼不可行」可能是 feasibility 不是 causal）。

定位：complex 或 ambiguous 題目的 optional working note。目標是 epistemic readiness，不是 process compliance。完全不生成 routing file 也可以；有用才留。

題目模糊、多層、容易走偏時，才值得先做 orientation／premise check／broad search（見 `orchestration.md`）。

## 不熟悉問題時

禁止僅憑題目字面、模型既有知識、使用者用了「為什麼」，就建立完整 research architecture。先走必要的 Orientation／Reconnaissance，再定 working lens。

## 熟悉且問題結構明確時

禁止為了形式硬做 reconnaissance。定義清楚、domain 熟悉、reasoning operation 明顯、無重要 hidden premise、不需外部現況即可拆題者，直接研究。

## Lens 三態（candidate → working → stable）

reasoning lens 是 optional，且狀態會演化：

- **Candidate lens**：題目剛進來時可有。用來幫助探索，不能因此排除其他 evidence。例：可能是 causal、可能需要 system、可能涉及 evolution。
- **Working lens**：經過基本 orientation，有足夠材料認為某些方法最適合。例：`primary_model: causal`＋supporting `system`、`evolution`。仍不是 immutable。
- **Stable lens**：load-bearing questions 已清楚、主要 evidence families 已找到、沒有重大新資訊持續改變問題結構，才視為目前 reasoning model 穩定。即使 stable，後續重大證據仍可 reframe。

## 輕量格式（參考用，可增減；全部欄位 optional）

```yaml
routing_state: working  # candidate | working | stable（optional）

reasoning_lenses:
  - feasibility
  - comparative
  - causal

# provisional narrative hint only；final narrative 由 Story Architect 後期決定
narrative_hint: question_cascade  # provisional only，不是 final 承諾

notes:
  - "哪個子問題用哪個 lens，為什麼"

routing_basis:
  - "初步資料顯示不同產品類別有不同價格機制"
  - "產業資料將 HBM capacity allocation 視為主要 constraint 之一"

open_routing_questions:
  - "DDR4 漲價是否其實主要來自供應退出，而非 AI demand"

reframe_log:
  - from: causal
    to: causal + system
    trigger: "發現價格變化與 capacity reallocation / inventory cycle 形成 feedback"
```

- `routing_state`／`routing_basis`／`open_routing_questions`／`reframe_log`／`narrative_hint` 皆 optional；不用長表格。研究中 reframe 時追加 `reframe_log`（from／to／trigger），避免 sunk-cost。
- Reasoning routing 與 Story routing 分開：`research/routing.yaml` 只放研究相關決策；final narrative 由 Story Architect 根據證據後期決定（見 `narrative-models.md`）。不要把 final narrative pattern 寫進 pre-search routing contract。

## Custom / Composite

13 種都不自然時可用自述 lens，建議加寫一句為什麼現有方法不夠用。不當成逃避思考的預設，也不設正式狀態機。

## 判型修正

研究中發現判型錯誤（什麼證據導致 reframe），直接調整並記錄觸發證據，避免 sunk-cost。
