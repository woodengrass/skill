# Charts（圖表圍欄規格）

研究員只寫資料不寫JS。圍欄語言固定 `chart`，內容嚴格JSON。

## 欄位

- `type`: bar／hbar／line／area／pie／donut 必填。
- `title`: 結論句（含數字區間），必填。標籤式標題退回重寫。
- `x`: 類別軸（bar/hbar/line/area用）。
- `series`: `[{name, data}]`；pie/donut的data是`[{value, name}]`。
- 進階（可選）：`stack:true`堆疊；`markAvg:true`平均線；單series加`chart:"line"/"bar"`＋`axis:0/1`做雙軸組合。
- `note`: 方法註＋資料截止日，必填，渲染在圖下。

## 進階圖種

- `hbar`橫條（長標籤用）、`donut`甜甜圈、`area`面積；`stack:true`堆疊；`markAvg:true`平均線；單series加`chart`＋`axis`做雙軸組合。
- `radar`雷達：`indicators`＋`max`＋series data（評分類必用）。
- `scatter`散佈：series data用`[[x,y]]`，另加`xName`／`yName`。
- `heatmap`熱力：`x`／`y`類別＋data用`[[xi,yi,value]]`（OD矩陣、相關矩陣用）。
- `map`地圖：`map:"taiwan"`＋data用`[{name,value}]`，name須為縣市繁中名（`libs/taiwan-counties.geojson`，2014年界，桃園標示為桃園縣注意對齊）；value缺填null顯示灰色。不做funnel／gauge／treemap／sankey，除非題目指明要。

## 硬規則

- 配色只准Paul Tol Bright七色，渲染器內建，研究員不自定色。
- bar零基線；pie超過5片改bar；數字千分位。
- 每圖註明來源章節；一節超過4圖即退回（防chart-dump）。
