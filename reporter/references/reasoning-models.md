# Reasoning Models（可組合的研究方法庫）

以下 13 種是可選方法，不是必經流程。Agent 可以：不選任何模型、同時使用多個、研究途中再取用、捨棄原本使用的模型、自行建立更適合題目的方法。每種含：適用問題、核心研究問題、主要分析方法、必查證據、最常見錯誤、推薦 narrative（見 `narrative-models.md`）、推薦 visual。primary-capable 標 ★，通常只做 overlay 的標 ◇——星號只是使用頻率提示，不是選擇義務。

## 1. Causal 因果 ★

- 適用：為什麼 X 發生（漲價、衰退、上升）。
- 核心：哪些因素真的造成結果？如何作用？區分 root cause／proximate cause／trigger／enabling condition／amplifier／feedback／consequence／confounder／non-causal correlation。
- 方法：建 competing explanations（H1/H2/H3…），重要 edge 標 observed／strongly_supported／plausible／speculative；停止前至少測試主要 alternative hypotheses。
- 必查：時間先後、機制合理性、反例；劑量反應只在領域適用時查（宏觀／制度／歷史題改用 temporal precedence、confounding、reverse causality、counterfactual、robustness）。
- 最常見錯誤：相關性直接畫成因果箭頭。
- 推薦 narrative：puzzle_to_resolution；visual：causal graph／driver tree／timeline。

## 2. Mechanism 機制 ★

- 適用：它到底怎麼運作。
- 核心：X 透過什麼中間步驟產生 Y。拆 inputs／components／activities／organization／intermediate states／constraints／outputs／failure modes。
- 方法：progressive zoom 黑箱逐層打開，最後組回整體。
- 必查：每層輸入輸出是否閉環、約束條件、失效模式。
- 最常見錯誤：只介紹零件，不說明如何共同產生結果。
- 推薦 narrative：progressive_zoom；visual：process flow／block diagram／sequence diagram。

## 3. System 系統 ★

- 適用：反直覺系統行為（拓寬又塞、單一政策無效、生態形成）。
- 核心：feedback loops／stocks／flows／delays／reinforcing／balancing／bottlenecks／emergent behavior。accumulation 重要（庫存、人口、債務）時用 stock-flow，不只畫 causal-loop。
- 方法：先找 surprising behavior，再逐條揭 loop，解釋干預為何失效。
- 必查：延遲、存量變化、反饋方向。
- 最常見錯誤：讀者圖直接丟完整 spaghetti diagram；必須逐步 reveal。
- 推薦 narrative：system_reveal；visual：causal-loop／stock-flow／bottleneck map。

## 4. Evolution 演化 ★

- 適用：怎麼變成今天這樣（制度形成、產業格局）。
- 核心：initial conditions／turning points／critical junctures／branching alternatives／path dependence／lock-in／reversal。問哪些事件真的改變之後可走的路。
- 方法：present puzzle → 回早期狀態 → turning point → 當時可能的替代路 → 選擇 → 路徑依賴 → 回到現在。
- 必查：轉折點的當時文獻（防 hindsight bias）。
- 最常見錯誤：把今天結果寫成從一開始就必然。
- 推薦 narrative：present_past_present；visual：annotated timeline／branching timeline。

## 5. Feasibility 可行性 ★

- 適用：在什麼條件下可行（捷運、政策、方案）。
- 核心：objective／baseline（什麼都不做會怎樣）／options／critical success factors／demand／technical／finance／regulation／risk／alternatives／sensitivity／switching values。
- 方法：decision／appraisal 型必須有 baseline 與 credible alternatives（BAU、minimum intervention、main proposal 四角比較）；技術 feasibility 依問題建立比較集，不硬套公共投資 appraisal。禁只評估預先偏好方案；禁輸出難解釋的單一總分，寫哪些維度成立、什麼條件翻盤。
- 必查：需求證據、工程約束原文、財務假設、法規門檻、替代方案成本。
- 最常見錯誤：沒有 baseline；沒有可信替代方案。
- 推薦 narrative：constraint_cascade；visual：constraint map／option matrix／sensitivity chart。

## 6. Comparative 比較 ★

- 適用：A 和 B 真正差在哪。
- 核心：structured focused comparison——先建共同問題，對每個 case 問相同問題：baseline／dimensions／measurement conditions／structural differences／trade-offs／context dependence。
- 方法：同一套標準走完全部對象。
- 必查：時間、價格、population、定義是否可比。
- 最常見錯誤：不同標準、cherry-pick 指標、名目實質混比。
- 推薦 narrative：structured_contrast；visual：comparison matrix／small multiples。

## 7. Evaluation 效果評估 ★

- 適用：政策／計畫到底有沒有效。
- 核心：objective／theory of change／outputs／outcomes／impact／counterfactual／heterogeneous effects／unintended effects。outcome 改善 ≠ intervention 造成，必須處理「沒做會怎樣」。
- 方法：承諾→實做→結果→反事實→歸因→分群→副作用。
- 必查：反事實基線、分群效果、非意圖後果。
- 最常見錯誤：把相關改善直接歸因。
- 推薦 narrative：promise_reality_counterfactual；visual：logic model／counterfactual plot／subgroup chart。

## 8. Investigation 調查 ★

- 適用：到底發生什麼（延誤、責任、錢去哪）。
- 核心：重建 events／documents／knowledge／decisions／actors／contradictions／responsibility／unknowns。建 working＋alternative hypothesis、chronology、document trail、power map、right-of-reply 對象。
- 方法：timeline 分 event_date／publication_date／knowledge_date 三軌，防 hindsight。
- 必查：文件鏈、涉事方回應、時間線缺口。
- 最常見錯誤：為戲劇性寫成真相唯一；允許高度支持但部分未確認。
- 推薦 narrative：anomaly_reconstruction；visual：timeline／relationship map。

## 9. Strategy 戰略 ★

- 適用：護城河、優勢 durability。
- 核心：value creation／capture／assets／capabilities／switching costs／network effects／trade-offs／activity fit／competitor response／substitution／attack surfaces。先問價值在哪產生、誰拿走，再問優勢是單一 asset 還是一組互強活動。禁退化成 SWOT。
- 方法：價值鏈→俘獲→互強→複製成本→破局點。
- 必查：競爭者回應、替代威脅、優勢衰減證據。
- 最常見錯誤：asset list 冒充 moat。
- 推薦 narrative：value_to_moat；visual：ecosystem／value chain／attack surface map。

## 10. Distribution 分配 ◇（通常 overlay）

- 適用：平均效果背後誰得誰付。
- 核心：income／geography／age／industry／time horizon／risk／externalities 切分。敘事 average → break apart。
- 方法：先給總體，再逐維度拆淨損益者。
- 必查：分群定義、地理口徑。
- 最常見錯誤：只報 average。
- 推薦 narrative：break_the_average；visual：group-impact matrix／map／decile chart。

## 11. Contested Claim 爭議查核 ★

- 適用：某句具體 claim 站不站得住。
- 核心：先拆 factual／causal／quantitative／implied conclusion 四部分，逐查 definition／primary evidence／supporting／contradicting／missing context／provenance／time relevance。
- 方法：什麼算成立先定義，再擺正反證據與缺失脈絡。
- 必查：原始出處、定義、分母。
- 最常見錯誤：只給 True／False；允許 supported／mostly／partially／misleading／unsupported／contradicted／unresolved 七態。
- 推薦 narrative：claim_trial；visual：claim/evidence table。

## 12. Scenario 情境 ◇（通常 overlay）

- 適用：未來怎麼走、何時更新判斷。
- 核心：drivers／predetermined trends／critical uncertainties／axes／plausible futures／implications／signposts／update triggers。禁把 scenario 寫成 prediction；無 probabilistic model 禁給機率數字。
- 方法：確定項→不確定軸→組合未來→各未來意涵→signpost。
- 必查：軸的獨立性、signpost 可觀測性。
- 最常見錯誤：scenario 變相預測。
- 推薦 narrative：drivers_to_signposts；visual：2×2 matrix／signpost dashboard。

## 13. Landscape 現況地圖 ★

- 適用：世界現在長什麼樣（算力分布、供應鏈位置、研究進展）。
- 核心：scope／definitions／taxonomy／actors／size／share／relationships／coverage／gaps。最重要的是 coverage——禁只列最知名的幾個。
- 方法：定邊界→建分類→列 actor 規模角色→連接→標已知與 gap 區。
- 必查：分類完備性、規模口徑。
- 最常見錯誤：名單即報告，沒有結構與缺口。
- 推薦 narrative：map_the_world；visual：taxonomy／ecosystem map／coverage matrix。
