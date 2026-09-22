# Visual Models（圖只用在比文字有效處；方法庫）

以下 mapping 是推薦，不是必畫清單：畫圖的條件只有一個——Recommended when it communicates the relationship better than prose.

## 推薦 mapping

causal→causal graph／driver tree；mechanism→flow／block diagram；system→causal-loop／stock-flow；evolution→annotated／branching timeline；feasibility→constraint map／option matrix／sensitivity；comparative→comparison matrix／small multiples；evaluation→logic model／counterfactual plot；investigation→timeline／relationship map；strategy→ecosystem／value chain；distribution→map／group-impact matrix；contested claim→claim/evidence table；scenario→2×2 matrix／signposts；landscape→taxonomy／ecosystem／network／map。

禁為有視覺而生成；Each visual should have a clear analytical purpose. Include only the series, annotations, and comparisons needed to support that purpose. 一張圖可同時呈現多個相互依賴的 series（如 revenue／margin／capex），只要它們服務同一 analytical question。

## Progressive disclosure

研究模型可複雜，讀者圖逐步 reveal：先 A→B→C，下節再加 D／E，完整系統圖放 Evidence View。Claim／Evidence／Source 全圖預設不塞正文。

## Internal vs Reader model

內部模型可技術化複雜；讀者版是壓縮版。允許折疊不影響理解的細節，禁刪掉會改變結論的關係。

## Analytical visual（研究期，early / iterative）vs Reader visual（發表期，late）

有些圖在研究早期非常有用（causal graph、timeline、system map、option matrix、evidence map），可幫 agent 思考：允許早期建立 analytical／internal visual 並持續修改，它們是 reasoning artifact。

只有在 Story Architect 確認「這個關係用圖真的比文字更容易理解」（Recommended when it communicates the relationship better than prose）時，才產生 reader visual。

```text
internal visual early / iterative
reader visual late
```
