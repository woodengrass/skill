# Presentation（呈現原則＋可用工具，不是版型規格）

> **Choose the presentation form that best helps the reader understand this specific subject. Do not conform the report to a predetermined layout.**

> **Presentation components are tools, not obligations.**

Agent 依題目自由決定成品形式，例如 single long-form report、multi-chapter reader、short fact-check page、visual explainer、comparison-oriented report、timeline-oriented report、evidence-heavy dossier、optional landing page。以上只是例子，不是 enum；不要新增 routing state 或 presentation mode。

## Hard invariants（強約束，只留這些）

1. central answer／main takeaway 容易找到。
2. load-bearing evidence 可以追溯（passage→claim→evidence／source，見 `artifacts.md` 的 source-map）。
3. material uncertainty／unresolved issues 不被隱藏（就近揭露，全局限制集中整理，見 `writing.md`）。
4. charts／visuals 不誤導（口徑、基線、標題，見下）。
5. 基本桌面與手機可讀。
6. internal research metadata（搜索輪次、agent 數量、quota、task id、方法論）不直接倒給讀者。
7. 不要為了視覺完整而硬塞 chart／KPI／cards／sections；不需要就不放。

## 可選組件（需要才用）

portal landing（hero／headline／summary cards／trust box／KPI／charts／chapters／gaps 區）、reader 長文檔（三欄、搜尋、大綱、圖表、來源反白）、timeline view、evidence view。每案只選真正幫讀者理解的部分。多 tab 切換與獨立 story view 屬 planned，文件不得寫成已有（現狀：reader 實作單文檔＋Evidence 雛形）。

## Portal（optional landing page asset）

`portal-template.html` 是可選入口，適合需要總覽／dashboard 式入口的大型 feasibility／policy／business research。narrative explainer、mechanism explainer、short fact-check、一頁式研究可以完全不用 portal。不用 portal 的案子，不需要產完整 portal metadata。

## report-meta.json（最小核心＋全可選擴充）

Required 只有：`title`、`date`、`lang`。需要首頁摘要再加 `headline_answer`。其餘全 optional：`summary`、`trust`（cutoff／sources／evidence_basis／unresolved／right_of_reply／changelog）、`footer`、`kpis`、`charts`（同 chart 圍欄 spec）、`chapters`。`check.py` 只驗：required 缺失才 fail；optional 存在時才驗格式。

語言規則：`lang` 決定正文語言；portal 在 runtime 以 `document.documentElement.lang=META.lang` 設定，reader 在部署填模板時以 `__LANG__` 填入（缺省 `zh-Hant`，與 meta.lang 一致）；兩者的 UI chrome（按鈕、標籤、空狀態）維持繁中，不做多語 UI。換句話說：`<html lang>` 跟著內容走，chrome 文字固定繁中。

## 圖表圍欄（`chart` JSON，可選工具）

> Generic charts are available when quantitative relationships are clearer visually than in prose or tables.

Agent 自己決定是否需要圖、用什麼圖、幾張、放哪，或乾脆用 table。不要為了 Skill 有 chart renderer 就找資料來畫圖。

研究員只寫資料不寫JS。`type`: bar／hbar／line／area／pie／donut／radar／scatter／heatmap；`note`（方法＋截止日）必填；配色渲染器內建Paul Tol七色；bar零基線。Choose chart type based on readability and the relationship being shown（pie 片數多時考慮 bar 等替代形式）；Avoid overcrowding, use small multiples or alternative forms when clearer（圖多時拆小多組或換形式，不數上限）；Prefer informative titles, use neutral descriptive titles when the evidence genuinely supports multiple interpretations。渲染邏輯只有一份：`assets/libs/reporter-charts.js`（reader／portal 共用，勿各寫一份）。地圖已移出核心：需要地理視覺請用當下合適的工具自備 SVG／image／custom GeoJSON，不在 Reporter 預建。

## Visual 使用規則（唯一核心）

> **Use a visual only when it communicates an important relationship more clearly than prose or a simple table.**

`visual-models.md` 是 inspiration／method library，不是「某 reasoning model 必須配某 visual」的對照表。

## 部署

工作區根目錄：`index.html`（填模板）、`portal.html`（有用 portal 才填）、`report-meta.json`（最小核心＋有用到的可選欄位）、`gaps.json`（有缺口才需要）、`source-map.json`（有用 claim 級追溯才需要）、`libs/`（部署時整個 `assets/libs/` 複製：echarts.min.js、reporter-charts.js，不斷網、不靠CDN）、`start_server.bat`（`python -m http.server`＋自動開瀏覽器）。file://下fetch被擋，必須走本地伺服器。
