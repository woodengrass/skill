---
name: reporter
description: Use ONLY when the user explicitly requests reporter via /reporter or by naming reporter. Do NOT auto-load for general coding, debugging, or file edits. One-shot pipeline from topic to browsable report site: breadth/depth dials, 5 waves plus incremental updates, MDX files plus in-site reader and portal.
---

# reporter

一次跑完，不等人。

## 啟動

- 題目必填，一句話。
- 第一題問廣度（低／中／高），第二題問深度（低／中／高）。兩題問完不再問。
- 廣度＝方向數量：低3-4片只cover主幹／中5-8片主幹加兩側／高10片以上連邊角都收。
- 深度＝每片量＋輪次：低10-20則一波收工／中20-50則擴一次／高50則以上擴到達標。
- 預設：事實型廣中深中；輿情型廣中深高；混合型廣高深中；不計成本廣高深高。

## 管線

W1方向 → W2分片採集 → W3擴大 → W4缺口 → W5驗證＋總報告 → W6增量更新，收尾固定動作。細節見 `references/orchestration.md`。

## 層索引

- `orchestration.md`：波次、quota、停搜、熔斷、反注入、git歷史。
- `evidence.md`：Claim→Evidence→Origin、出處獨立性、來源1-5級。
- `verification.md`：引用鎖定、entailment查核、數字查核、紅隊。
- `writing.md`：寫作鐵律、敘事、標題數字、frontmatter、來源寫法。
- `presentation.md`：閱讀器、入口頁、meta/gaps/source-map、圖表。

## 鐵律

- 正文只留結果；研究過程metadata永不進正文；認知不確定性只出現在固定位置（節尾信心行、核心爭議、未決問題、`gaps.json`）。
- omo原生：並行＋免費便宜模型＋todowrite＋task_id續跑；oracle／ultrabrain／metis／momus預設全關。
- 英文目錄與檔名；覆蓋不新增；相同規則只認各層文件定義，不複述。
