# Presentation（閱讀器與入口）

## 架構

MDX正源＋站內SPA閱讀器＋入口頁。精緻全放呈現層，正源保持純淨。模板在 `../assets/`，libs（echarts.min.js、taiwan-counties.geojson）由skill自帶，部署時整個 `assets/libs/` 複製到工作區 `libs/`，不斷網、不靠CDN。

## 閱讀器（reader-template.html）

填NAV（分區→標題→路徑）、PDFS、`<title>`、首頁塊即用。實際功能：三欄佈局、可收合側欄、`Ctrl+K`全文搜尋＋高亮、右側頁內大綱＋跟隨、文末上下篇、麵包屑、深色模式、手機版、互鏈懸停預覽＋文末反向連結、表格優化、標題錨點＋回頂部、列印樣式、反白按S查來源（讀source-map.json）、`chart`圍欄圖表渲染、單行`日期：`引文渲染成右上小字。

## 入口頁（portal-template.html＋report-meta.json）

入口頁零手寫內容，全部讀 `report-meta.json` 渲染：

```json
{
  "title": "題目", "date": "查證基準日", "verdict": "結論句",
  "lang": "zh-Hant",
  "summary": [{"k": "維度", "v": "一句判斷", "d": "關鍵數字"}],
  "score": 82,
  "kpis": [{"n": "數字", "l": "標籤"}],
  "charts": ["同chart圍欄spec"],
  "chapters": [{"t": "標題", "d": "一句話", "path": "index.html#/..."}]
}
```

含執行摘要卡、完善度分數條、KPI、圖表、章節卡。`gaps.json`放缺口陣列（`[{item, status}]`，status限待補／已放棄／下版追），入口讀它渲染缺口區，正文不出現。兩檔機器寫機器讀。

## 呈現模式（同一證據核多視圖，不要全開）

Quick（5分鐘核心）、Deep（完整）、Evidence（Claim→Evidence→Origin）、Timeline（事件演變）、Disagreement（爭議與未決）、Updates（相對上次改變了什麼）。不要所有題目顯示所有tab，按 `routing.yaml` 的 presentation 段開關。

## Story／Dossier 分離

長篇敘事另有 story 呈現（適合 explainer／investigation／evolution／mechanism），研究卷宗走 dossier（適合 feasibility／comparison／policy）。同一研究可同時生成兩者。

## 分數顯示規則

完善度分數只放內部／debug，不對讀者顯示百分比。讀者優先看到：資料截止日期、主要證據來源、原始來源比例、關鍵 unresolved、重要缺口、right of reply、更新與更正紀錄。

## 圖表圍欄（`chart` JSON）

研究員只寫資料不寫JS。`type`: bar／hbar／line／area／pie／donut／radar／scatter／heatmap／map；`title`必須是結論句；`note`（方法＋截止日）必填；配色渲染器內建Paul Tol七色；bar零基線、pie超5片改bar；一節超4圖退回。map的name須為縣市繁中名（2014年界注意對齊）。

## 部署

工作區根目錄：`index.html`（填模板）、`portal.html`（填模板）、`report-meta.json`、`gaps.json`、`source-map.json`、`libs/`、`start_server.bat`（`python -m http.server`＋自動開瀏覽器）。file://下fetch被擋，必須走本地伺服器。
