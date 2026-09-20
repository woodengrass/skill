# Verification（W5查核）

預設便宜：mechanical checks（連結存活、格式、差集）全用便宜agent。ambiguous entailment、複雜統計、因果爭議、高風險 allegation 允許 escalation（用更強模型或人工複核），不硬撐。查核對象是主張，不是URL。數字解讀另見 `data-verification.md`；審稿標準見 `editorial-standards.md`。

## 引用鎖定

W5先建 Approved／Dropped 登記表，編號凍結，起草禁引 Dropped。全文件 URL 收斂成來源合併索引，差集為空。

## Entailment 查核（必跑）

對每條 load-bearing claim、執行摘要的每條主張與數字、每條 recommendation 所依賴的主張，打開來源原文逐條判：

- supports：原文直接支持，保留。
- partially supports：只支持一部分，縮小主張到被支持的範圍。
- contradicts：換來源或刪除主張，二選一。
- unrelated：換來源或刪除，二選一。
- insufficient_context：來源可能相關但上下文不足以支持或反駁。處置：找完整上下文、找原始來源；否則 claim 保持 unresolved 或縮小，禁硬塞成 partial。

URL活著不算驗證成功。判完回寫修正，partial 的縮小記錄在案。

## 數字查核範圍

100%查核：所有影響結論的 load-bearing numbers、執行摘要中的數字、recommendation 直接依賴的數字。其餘數字抽樣查核（每章至少抽一條高風險的）。時效主張標來源日。

## 紅隊（證據制，不投票）

只對高風險主張開；無高風險用反方五問代替。Challenger 提交必須含：challenged_claim_id、specific_objection、supporting_evidence_or_reasoning（新證據，或具體可查核的方法論問題如分母錯誤、selection bias、反向因果、identification 不成立）、origin、entailment、why_it_changes_claim。空泛「可能有其他解釋」直接 discard。裁決看 provenance、測量品質、entailment、獨立性、時效、解釋力，不看票數。contest 才加輪；論點不再推進就停，硬上限3輪（熔斷線非精確閾值）；停火標 GENUINELY_UNCERTAIN 並寫下何種證據可解。異議原文寫進「核心爭議」區。

## 連結驗證波（報告完成後必跑）

另派便宜agent對全區http連結逐一連入驗證，逐條判活著／轉址／需登入／已死。處置：已死的換可開替代源或刪；需登入的標需登入；轉址更新URL。禁編新URL充數。驗證表存檔備查，不進正文。

## 反方五問（每案必跑，允許零發現）

結論可能錯在哪？高影響主張是否單一家族？來源能否直接觀察該事實？時效是否用舊源？查過什麼反證？無證據爭議就明寫無，不湊數。
