# Verification（結果要求，不規定儀式）

最終報告必須滿足以下結果要求。用什麼模型、幾輪、幾個人驗，由 agent 依風險自行決定；簡單技術說明不用硬跑全套。查核對象是主張，不是 URL。數字解讀另見 `data-verification.md`；審稿視角見 `editorial-standards.md`。

## 最終報告的品質要求

- load-bearing factual claims 有可靠 evidence。
- important citations entail the claim：對承重主張、執行摘要的主張與數字、recommendation 所依賴的主張，打開來源原文逐條判 entailment——supports 保留；partially_supports 就縮小主張到被支持的範圍；contradicts／unrelated 換來源或刪除；insufficient_context（上下文不足以支持或反駁）就找完整上下文或原始來源，否則保持 unresolved，禁硬塞成 partial。URL 活著不算驗證成功。
- important numbers 有正確 denominator／definition／time context（適用哪些檢查見 `data-verification.md`）。
- major causal claims 不把 correlation 當 causation。
- duplicated provenance 不冒充 independent corroboration。
- quotes／scenes 不可 fabricated：引語只能用發表過的真話＋出處；場景只能重建有來源的時刻。
- material uncertainty 必須揭露，且在最接近相關 claim 的位置。
- high-risk allegation 要適當歸因、來源與 right of reply（見 `presentation.md` 的 trust 欄位）。
- 最終 links／sources 可查：全文件 URL 收斂成來源合併索引；报告完成後對全區連結驗活（活著／轉址／需登入／已死），死的換可開替代源或刪，需登入的標需登入，禁編新 URL 充數。驗證表存檔備查，不進正文。

## Exploratory findings ≠ verification

> Exploratory findings generate hypotheses; they do not automatically verify them.

Reconnaissance／broad search 發現的 possible cause／mechanism／pattern 只應變成 candidate claim／candidate hypothesis／candidate question。Load-bearing conclusion 必須用適合的方法驗證（上列 entailment／denominator／provenance 要求），且 verification 可在研究中途對高風險主張先驗，不只在最後。Final verification 是 publication 前的完整 gate。

## Adversarial checking（risk-based）

Before publication, actively consider material counterevidence, competing interpretations, and failure modes when they could change the answer. 高風險、高不確定性、因果、調查、爭議查核時可以做更強 adversarial pass；簡單技術說明不用硬跑。

做 adversarial pass 時：challenger 提交必須含 challenged_claim（被挑戰的主張原文）、specific_objection、supporting_evidence_or_reasoning（新證據，或具體可查核的方法論問題如分母錯誤、selection bias、反向因果、identification 不成立）、origin、entailment、why_it_changes_claim；challenged_claim_id 只有在有用 ledger 時才附（optional if available），不為 verification 被迫建 claim ledger。空泛「可能有其他解釋」直接 discard。裁決看 provenance、測量品質、entailment、獨立性、時效、解釋力，不看票數。論點不再推進就停；停火標 GENUINELY_UNCERTAIN 並寫下何種證據可解。異議原文寫進「核心爭議」區。
