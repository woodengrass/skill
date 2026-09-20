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
  "lang": "zh-Hant", "footer": "頁尾一句話（缺省用中性預設）",
  "summary": [{"k": "維度", "v": "一句判斷", "d": "關鍵數字"}],
  "trust": {"cutoff": "資料截止日", "sources": ["主要證據"],
    "original_ratio": "原始來源比例", "unresolved": ["未決問題"],
    "right_of_reply": "是否取得對造回應（無涉事指控寫 n/a）",
    "changelog": ["更新更正"]},
  "kpis": [{"n": "數字", "l": "標籤"}],
  "charts": ["同chart圍欄spec"],
  "chapters": [{"t": "標題", "d": "一句話", "path": "index.html#/..."}]
}
```

入口渲染：執行摘要卡、可信度說明（讀 trust）、KPI、圖表、章節卡、缺口區（讀 `gaps.json`）。完善度分數只放內部／debug，不對讀者顯示百分比。`document.title` 與 `<html lang>` 由 meta 動態設定。meta 的 `lang` 只決定正文語言；reader 與 portal 的 UI chrome 維持繁中，不做三語 UI（真要做才另開 i18n 工程）。

## 呈現模式（同一證據核多視圖，不要全開）

Quick、Deep、Evidence、Timeline、Disagreement、Updates 是同一證據核的多視圖，按題目需要選開，不要全開。現狀：reader-template 只實作單文檔＋Evidence 雛形（source-map 反白查詢），多 tab 切換與獨立 story-template.html 屬 planned，文件不得寫成已有。

## Story／Dossier 分離

長篇敘事另有 story 呈現（適合 explainer／investigation／evolution／mechanism），研究卷宗走 dossier。獨立 story-template.html 屬 planned；現階段長文直接走 reader 長文檔＋錨點，不宣稱已有 story view。

## 分數顯示規則

完善度分數只放內部／debug，不對讀者顯示百分比。讀者優先看到：資料截止日期、主要證據來源、原始來源比例、關鍵 unresolved、重要缺口、right of reply、更新與更正紀錄。

## 圖表圍欄（`chart` JSON）

研究員只寫資料不寫JS。`type`: bar／hbar／line／area／pie／donut／radar／scatter／heatmap／map；`note`（方法＋截止日）必填；配色渲染器內建Paul Tol七色；bar零基線。Choose chart type based on readability and the relationship being shown（pie 片數多時考慮 bar 等替代形式）；Avoid overcrowding, use small multiples or alternative forms when clearer（圖多時拆小多組或換形式，不數上限）；Prefer informative titles, use neutral descriptive titles when the evidence genuinely supports multiple interpretations。map的name須為縣市繁中名（2014年界注意對齊）。

## 部署

工作區根目錄：`index.html`（填模板）、`portal.html`（填模板）、`report-meta.json`、`gaps.json`、`source-map.json`、`libs/`、`start_server.bat`（`python -m http.server`＋自動開瀏覽器）。file://下fetch被擋，必須走本地伺服器。
