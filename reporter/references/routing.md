# Reasoning Lens（可選的方法視角，不是必經路由）

判斷「這個問題需要什麼認知操作」，不靠關鍵字硬對（「為什麼不可行」可能是 feasibility 不是 causal）。但這只是思考輔助：**如果模型很明顯，直接研究即可，不必生成任何路由文件。**

只有題目模糊、多層、容易走偏時，才值得先做 orientation／premise check／broad search，再決定適合的方法；此時可選用 `reasoning-models.md` 中的方法，並可把決定記在 `research/routing.yaml`（格式示例見 `assets/schema-samples/routing.sample.yaml`）：primary 定主視角，supporting 處理子問題，overlays 橫切全案。

一個題目可多方法並存，也可以在研究途中取用、捨棄、重調（記錄什麼證據導致轉向即可）。13 種都不自然時可自建更適合題目的方法，不必硬套。`routing.yaml` 永遠 optional；check.py 不因缺少它而 fail。

## source-map 穩定 ID

`source-map.json` 條目格式：`[{id, passage, sources:[{t, u}]}]`，id 為 P0001… passage ID（`S` 保留給 source）。閱讀器反白查詢先對 id（內文錨有 id 时），無 id 才對 passage 文字模糊匹配。禁只用段落前 40 字當 key。
