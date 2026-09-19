# Verification（W5查核）

全用便宜agent，貴模型全關。查核對象是主張，不是URL。數字解讀另見 `data-verification.md`；審稿標準見 `editorial-standards.md`。

## 引用鎖定

W5先建 Approved／Dropped 登記表，編號凍結，起草禁引 Dropped。全文件 URL 收斂成來源合併索引，差集為空。

## Entailment 查核（必跑）

對每條 load-bearing claim、執行摘要的每條主張與數字、每條 recommendation 所依賴的主張，打開來源原文逐條判：

- supports：原文直接支持，保留。
- partially supports：只支持一部分，縮小主張到被支持的範圍。
- contradicts：換來源或刪除主張，二選一。
- unrelated：換來源或刪除，二選一。

URL活著不算驗證成功。判完回寫修正，partial 的縮小記錄在案。

## 數字查核範圍

100%查核：所有影響結論的 load-bearing numbers、執行摘要中的數字、recommendation 直接依賴的數字。其餘數字抽樣查核（每章至少抽一條高風險的）。時效主張標來源日。

## 紅隊（按主張風險排優先級）

只對高風險主張開紅隊；無高風險主張時用反方五問代替，不硬湊編制。優先查：對最終結論影響大、confidence低、來源互相衝突、recommendation對它敏感的主張。編制1辯護＋3反方（claim挑刺／矛盾搜索／來源多樣性），同模型三prompt並行。contest（互斥結論、單源高風險推論）才加輪；論點不再推進就停，硬上限3輪；停火後標 GENUINELY_UNCERTAIN 並寫下何種證據可解。異議（多數 verdict＋直接引文）寫進「核心爭議」區。

## 連結驗證波（報告完成後必跑）

另派便宜agent對全區http連結逐一連入驗證，逐條判活著／轉址／需登入／已死。處置：已死的換可開替代源或刪；需登入的標需登入；轉址更新URL。禁編新URL充數。驗證表存檔備查，不進正文。

## 反方五問（每案必跑，允許零發現）

結論可能錯在哪？高影響主張是否單一家族？來源能否直接觀察該事實？時效是否用舊源？查過什麼反證？無證據爭議就明寫無，不湊數。
