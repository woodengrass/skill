# Artifacts（可選的機器中間件 schema）

Complex, long-running, multi-agent, high-risk, or incrementally updated research may externalize state using these schemas. 適合時使用，不適合時不要為了符合架構製造一堆空 JSON。簡單題目不用 ledger，直接研究即可。

唯一強規範：如果 agent 決定使用某 artifact，其格式必須符合以下 schema，確保跨階段互讀。如果沒用 ledger，check.py 不應因此 fail。

只定義跨階段互讀的最小欄位，不要巨型 schema。

## Ledger（research/ 下按需使用）

### questions.jsonl（複雜題推薦，簡單題不用）

對複雜、多層、容易跳步的題目，Question Tree／Question Graph 是推薦工具：每題 question_id／parent／text／importance（load_bearing 與否）／status／claims／opens，用來追蹤回答、找跳步與缺口。簡單問題不用。

```json
{"question_id": "Q0042", "parent_id": "Q0010", "text": "...",
 "importance": "load_bearing", "status": "answered",
 "claims": ["C014"], "opens": ["Q043"]}
```

### claims.jsonl

```json
{"claim_id": "C014", "text": "...",
 "type": "factual",
 "importance": "load_bearing",
 "status": "supported",
 "evidence": ["E022"], "counterevidence": ["E031"],
 "questions": ["Q0042"]}
```

`type`: factual／quantitative／causal／mechanistic／comparative／evaluative／forecast／interpretive。`importance`: load_bearing／supporting／context。`status`: unverified／supported／partially_supported／contradicted／unresolved／dropped。

### evidence.jsonl

```json
{"evidence_id": "E022", "source_id": "S012", "origin_id": "O004",
 "locator": "p.47 / table 3", "excerpt_or_summary": "...",
 "entailment": "supports", "claims": ["C014"]}
```

`entailment`: supports／partially_supports／contradicts／unrelated／insufficient_context。

### sources.jsonl

```json
{"source_id": "S012", "origin_id": "O004",
 "url": "https://...", "title": "...", "author_or_org": "...",
 "published_at": "...", "accessed_at": "...",
 "source_role": "primary_document", "provenance_family": "O004"}
```

`source_role` 常見值：primary_document／primary_data／firsthand_statement／original_reporting／academic_peer_reviewed／academic_preprint／secondary_analysis／commentary／lead_only。Origin 不獨立成檔；`origin_id`＋`provenance_family` 已足夠表達家族，未來需要 richer origin graph 才新增 `origins.jsonl`。

## Ledger 唯一性規則

Question Tree 可引用 claim_id；模型 artifact 可引用 claim_id；Verification 結果必須回寫 ledger（status、entailment）；Story Architect 只讀最新狀態；source-map 由 passage→claim→evidence/source 關係生成，不重配。

## 模型 Artifact 最小 schema（決定用才生成）

### causal.json

```json
{"nodes": [{"id": "N1", "label": "...", "claims": ["C014"]}],
 "edges": [{"from": "N1", "to": "N2", "relation": "causal",
   "confidence": "strongly_supported", "claims": ["C014"]}]}
```

confidence: observed／strongly_supported／plausible／speculative。

### options.json

```json
{"baseline": "O0",
 "options": [{"option_id": "O0", "name": "Business as usual", "claims": ["C020"]}],
 "dimensions": [{"dimension": "cost", "comparisons": []}],
 "switching_conditions": []}
```

### system.json

```json
{"nodes": [], "links": [], "stocks": [], "flows": [],
 "delays": [], "claims": []}
```

不要求每案都有 stock-flow。

### timeline.json

```json
[{"event_id": "T001", "event_date": "2026-01-01",
  "publication_date": "2026-01-03", "knowledge_date": "2026-01-02",
  "event": "...", "actors": [], "claims": ["C031"], "sources": ["S020"]}]
```

三個日期欄位可為 null，禁混在一起。

### scenarios.json

```json
{"drivers": [], "critical_uncertainties": [],
 "scenarios": [{"scenario_id": "SC1", "name": "...",
   "conditions": [], "implications": [], "signposts": []}]}
```

無 probabilistic forecasting model 禁加 probability。
