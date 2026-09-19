---
name: reporter
description: Use ONLY when the user explicitly requests reporter via /reporter or by naming reporter. Do NOT auto-load for general coding, debugging, or file edits. One-shot pipeline from topic to browsable report site: takes a topic + breadth/depth dials, runs 5 waves, overwrites a single evergreen report set, ships MDX files plus an in-site reader.
---

# reporter

一次跑完，不等人。用戶給題目、選廣深，之後不再確認。

## 輸入

- 題目（必填）：一句話，如「調查新竹捷運可行性」。
- 第一題問廣度（低／中／高），第二題問深度（低／中／高），見 `references/intensity.md`；用戶不選就按情境預設跑。兩題問完不再問。

## 管線（五波，細節見 `references/waves.md`）

1. W1 方向清單：切互不重疊的片，寫進 `00_方向.mdx`，不停等直接往下跑。
2. W2 按片採集：每片獨立成檔，附數量自驗。
3. W3 擴大搜索：循環到配額達標為止。
4. W4 缺口補齊：缺口清單→定向補搜。
5. W5 交叉驗證＋總報告：引用鎖定、家族合併、TOP-15數值查核、三源三角、紅隊辯論（見 `references/correctness.md`），再寫總報告覆寫（見 `references/format.md`）。

收尾固定動作：覆蓋不新增、清垃圾、套閱讀器模板（`assets/reader-template.html`）。

## 情境路由（只定預設，不限制做法）

- 事實型（政策／建設）：官方證據和輿情分區存放，結論只吃官方。
- 輿情型（候選人支持度）：主體是言論＋民調，民調方法識讀獨立一區，言論禁換算成數字。
- 混合型：兩套並行。細節見 `references/scenarios.md`。

## 鐵律（違反即失敗）

- 寫作規則見 `references/doc-rules.md`（禁AI腔、正文禁方法論）。
- 驗收見 `references/acceptance.md`（配額不到就加搜）。
- omo原生：`task`並行＋`explore`／`librarian`（免費便宜）＋`todowrite`＋`task_id`續跑。高成本模型（oracle／ultrabrain／metis／momus）預設全關。
- 英文目錄與檔名；中文只出現在標題與內文。
