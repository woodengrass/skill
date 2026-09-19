# Reader（閱讀器規格）

## 架構

MDX正源＋站內SPA閱讀器。精緻全放reader層，正源保持純淨；文首固定frontmatter只三行（title／description／date）。

## 入口狀態（report-meta.json＋gaps.json）

工作區根目錄放 `report-meta.json`：`{topic, breadth, depth, updateCount, baselineDate, verdict, coverage:{files,items,sources}, score}`，入口首頁讀它渲染狀態列、KPI和完善度分數條。`gaps.json`放缺口陣列，入口讀它渲染缺口區，正文不出現。兩檔都是機器寫、機器讀，人不直接讀。

## 必備功能（模板見 `../assets/reader-template.html`）

三欄佈局（左跨頁導航／右頁內大綱／文末上下篇）、可收合側欄、`Ctrl+K`全文搜尋＋命中高亮、麵包屑、深色模式、手機版（漢堡選單＋表格橫滑）、互鏈懸停預覽＋文末反向連結、表格優化（表頭黏住）、標題錨點＋回頂部、列印樣式。

## 部署

每個報告工作區根目錄放 `index.html`（從模板填NAV）＋`start_server.bat`（`python -m http.server`＋自動開瀏覽器）。file://下fetch被擋，必須走本地伺服器，頁面要顯示引導橫幅。

## 驗收

手機表格可橫滑讀完；`Ctrl+K`三秒找到詞；長文右側可跳節；互鏈懸停可預知去向。
