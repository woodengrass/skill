# Reasoning Models（方法庫，只描述研究方法，不定義文章模板）

> Reasoning models are tools selected against the current understanding of the problem. For unfamiliar or ambiguous topics, use them as candidate lenses until enough external evidence has been gathered to justify the working model.

> A model should help decide what evidence would distinguish explanations, not decide in advance what the answer must be.

> A reasoning model is a working lens, not a conclusion. 狀態演化（candidate → working → stable）見 `routing.md`；時機（何時才定 working model）見 `orchestration.md`。

方法庫可自由組合：一個題目可用多種 lenses 並存，agent 可選用、組合、改造或忽略任一方法。同一規則只有一個 authoritative definition 的是 truth／safety invariant（見 `editorial-standards.md` 強約束），其餘皆為建議。

每種含：適合什麼問題、可用方法、重要檢查、常見錯誤、可搭配 narrative（見 `narrative-models.md`）、可搭配 visual。

## 1. Causal 因果

- 適合：為什麼 X 發生（漲價、衰退、上升）。
- 核心：哪些因素真的造成結果？如何作用？區分 root cause／proximate cause／trigger／enabling condition／amplifier／feedback／consequence／confounder／non-causal correlation。
- 可用方法：建 competing explanations（H1/H2/H3…），重要 edge 標 observed／strongly_supported／plausible／speculative。
- 重要檢查：時間先後、機制合理性、反例；劑量反應只在領域適用時看（宏觀／制度／歷史題改用 temporal precedence、confounding、reverse causality、counterfactual、robustness）。
- 常見錯誤：相關性直接畫成因果箭頭。
- 對 consequential causal claims，主動測試 plausible alternative explanations 通常能顯著提高可靠性。
- 可搭配 narrative：puzzle_to_resolution；visual：causal graph／driver tree／timeline。

## 2. Mechanism 機制

- 適合：它到底怎麼運作。
- 核心：X 透過什麼中間步驟產生 Y。拆 inputs／components／activities／organization／intermediate states／constraints／outputs／failure modes。
- 可用方法：progressive zoom 黑箱逐層打開，最後組回整體。
- 重要檢查：每層輸入輸出是否閉環、約束條件、失效模式。
- 常見錯誤：只介紹零件，不說明如何共同產生結果。
- 可搭配 narrative：progressive_zoom；visual：process flow／block diagram／sequence diagram。

## 3. System 系統

- 適合：反直覺系統行為（拓寬又塞、單一政策無效、生態形成）。
- 核心：feedback loops／stocks／flows／delays／reinforcing／balancing／bottlenecks／emergent behavior。accumulation 重要（庫存、人口、債務）時用 stock-flow，不只畫 causal-loop。
- 可用方法：先找 surprising behavior，再逐條揭 loop，解釋干預為何失效。
- 重要檢查：延遲、存量變化、反饋方向。
- 常見錯誤：讀者圖直接丟完整 spaghetti diagram；複雜 system diagram 通常適合 progressive disclosure，以降低讀者認知負擔。
- 可搭配 narrative：puzzle_to_resolution（反直覺行為先擺再解）；visual：causal-loop／stock-flow／bottleneck map。

## 4. Evolution 演化

- 適合：怎麼變成今天這樣（制度形成、產業格局）。
- 核心：initial conditions／turning points／critical junctures／branching alternatives／path dependence／lock-in／reversal。問哪些事件真的改變之後可走的路。
- 可用方法：present puzzle → 回早期狀態 → turning point → 當時可能的替代路 → 選擇 → 路徑依賴 → 回到現在。
- 重要檢查：轉折點的當時文獻（防 hindsight bias）。
- 常見錯誤：把今天結果寫成從一開始就必然。
- 可搭配 narrative：present_past_present；visual：annotated timeline／branching timeline。

## 5. Feasibility 可行性

- 適合：在什麼條件下可行（捷運、政策、方案）。
- 核心：objective／baseline（什麼都不做會怎樣）／options／critical success factors／demand／technical／finance／regulation／risk／alternatives／sensitivity／switching values。
- 可用方法：decision／appraisal 類問題通常應比較 baseline 與 credible alternatives（BAU、minimum intervention、main proposal 四角比較）；技術 feasibility 依問題建立比較集，不硬套公共投資 appraisal。缺少 baseline 或可信替代方案時，結論容易受到 framing bias；單一總分難解釋時，寫哪些維度成立、什麼條件翻盤。
- 重要檢查：需求證據、工程約束原文、財務假設、法規門檻、替代方案成本。
- 常見錯誤：沒有 baseline；沒有可信替代方案；只評估預先偏好方案。
- 可搭配 narrative：constraint_cascade；visual：constraint map／option matrix／sensitivity chart。

## 6. Comparative 比較

- 適合：A 和 B 真正差在哪。
- 核心：structured focused comparison——先建共同問題，對每個 case 問相同問題：baseline／dimensions／measurement conditions／structural differences／trade-offs／context dependence。
- 可用方法：同一套標準走完全部對象。
- 重要檢查：時間、價格、population、定義是否可比。
- 常見錯誤：不同標準、cherry-pick 指標、名目實質混比。
- 可搭配 narrative：structured_contrast；visual：comparison matrix／small multiples。

## 7. Evaluation 效果評估

- 適合：政策／計畫到底有沒有效。
- 核心：objective／theory of change／outputs／outcomes／impact／counterfactual／heterogeneous effects／unintended effects。outcome 改善 ≠ intervention 造成，處理「沒做會怎樣」能顯著提高歸因可信度。
- 可用方法：承諾→實做→結果→反事實→歸因→分群→副作用。
- 重要檢查：反事實基線、分群效果、非意圖後果。
- 常見錯誤：把相關改善直接歸因。
- 可搭配 narrative：promise_reality_counterfactual；visual：logic model／counterfactual plot／subgroup chart。

## 8. Investigation 調查

- 適合：到底發生什麼（延誤、責任、錢去哪）。
- 核心：重建 events／documents／knowledge／decisions／actors／contradictions／responsibility／unknowns。建 working＋alternative hypothesis、chronology、document trail、power map、right-of-reply 對象。
- 可用方法：timeline 分 event_date／publication_date／knowledge_date 三軌，防 hindsight。
- 重要檢查：文件鏈、涉事方回應、時間線缺口。
- 常見錯誤：為戲劇性寫成真相唯一；允許高度支持但部分未確認。
- Publication／ethics gate（涉指名道姓的不法、失職、責任歸屬時）：未尋求回應前，指控不得寫成定論（標單方說法＋記錄已尋求回應或為何未能尋求）；load-bearing 指控須可追到 primary source，轉述不得立為定論；涉事方回應（right_of_reply）同時寫入內文就近位置與 `report-meta.json` 的 trust；無法確認又具傷害性的細節寧可不寫並列入 gaps。查核細則見 `verification.md`。
- 可搭配 narrative：anomaly_reconstruction；visual：timeline／relationship map。

## 9. Strategy 戰略

- 適合：護城河、優勢 durability。
- 核心：value creation／capture／assets／capabilities／switching costs／network effects／trade-offs／activity fit／competitor response／substitution／attack surfaces。先問價值在哪產生、誰拿走，再問優勢是單一 asset 還是一組互強活動。只列 asset 清單通常撐不起 moat 分析。
- 可用方法：價值鏈→俘獲→互強→複製成本→破局點。
- 重要檢查：競爭者回應、替代威脅、優勢衰減證據。
- 常見錯誤：asset list 冒充 moat。
- 可搭配 narrative：present_past_present（從現狀出發再回頭），或依材料用其他順序；講述時先交代價值在哪產生、誰拿走，再論優勢是單一 asset 還是一組互強活動。visual：ecosystem／value chain／attack surface map。

## 10. Distribution 分配

- 適合：平均效果背後誰得誰付。
- 核心：income／geography／age／industry／time horizon／risk／externalities 切分。敘事 average → break apart。
- 可用方法：先給總體，再逐維度拆淨損益者。
- 重要檢查：分群定義、地理口徑。
- 常見錯誤：只報 average。
- 可搭配 narrative：break_the_average；visual：group-impact matrix／map／decile chart。

## 11. Contested Claim 爭議查核

- 適合：某句具體 claim 站不站得住。
- 核心：先拆 factual／causal／quantitative／implied conclusion 四部分，逐查 definition／primary evidence／supporting／contradicting／missing context／provenance／time relevance。
- 可用方法：什麼算成立先定義，再擺正反證據與缺失脈絡。
- 重要檢查：原始出處、定義、分母。
- 常見錯誤：只給 True／False；可用 supported／mostly／partially／misleading／unsupported／contradicted／unresolved 七態。
- 可搭配 narrative：claim_trial；visual：claim/evidence table。

## 12. Scenario 情境

- 適合：未來怎麼走、何時更新判斷。
- 核心：drivers／predetermined trends／critical uncertainties／axes／plausible futures／implications／signposts／update triggers。scenario 寫成 prediction 是常見失敗模式；沒有機率模型時不得給出機率數字。
- 可用方法：確定項→不確定軸→組合未來→各未來意涵→signpost。
- 重要檢查：軸的獨立性、signpost 可觀測性。
- 常見錯誤：scenario 變相預測。
- 可搭配 narrative：drivers_to_signposts；visual：2×2 matrix／signpost dashboard。

## 13. Landscape 現況地圖

- 適合：世界現在長什麼樣（算力分布、供應鏈位置、研究進展）。
- 核心：scope／definitions／taxonomy／actors／size／share／relationships／coverage／gaps。coverage 值得特別用心：只列最知名的幾個通常交代不了全貌。
- 可用方法：定邊界→建分類→列 actor 規模角色→連接→標已知與 gap 區。
- 重要檢查：分類完備性、規模口徑。
- 常見錯誤：名單即報告，沒有結構與缺口。
- 可搭配 narrative：map_the_world；visual：taxonomy／ecosystem map／coverage matrix。
