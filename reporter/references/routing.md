# Routing（W0路由）

Router 判斷「這個問題需要什麼認知操作」，不靠關鍵字硬對（「為什麼不可行」可能是 feasibility 不是 causal）。

## 輸出（ research/routing.yaml ）

```yaml
primary_model: feasibility
supporting_models: [comparative, causal]
overlays: [distribution, scenario]
narrative_pattern: question_cascade
required_artifacts: [question_tree, option_matrix, constraint_map]
verification: {needs_counterfactual: false, needs_right_of_reply: false,
  needs_data_desk: true, needs_chronology: true}
presentation: {quick: true, deep: true, dossier: true, evidence: true, timeline: false}
```

一個題目可多模型並存：primary 定主架構，supporting 處理子問題，overlays 橫切全案。研究中發現判型錯誤（什麼證據導致 reframe）允許重調並記錄，避免 sunk-cost。

## Custom / Composite fallback

13 種都不自然時才可用 `primary_model: custom` 或 `composite`，且必須加寫：

```yaml
custom_reasoning:
  description: "這個研究需要什麼特殊推理"
  why_existing_models_are_insufficient: "..."
```

不得當成逃避 routing 的預設。

## source-map 穩定 ID

`source-map.json` 條目格式：`[{id, passage, sources:[{t, u}]}]`，id 為 P0001… passage ID（`S` 保留給 source）。閱讀器反白查詢先對 id（內文錨有 id 时），無 id 才對 passage 文字模糊匹配。禁只用段落前 40 字當 key。
