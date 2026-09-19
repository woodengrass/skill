# skill

我自己寫、自己用的 agent skills。每個 skill 獨立一層目錄，維持輕量：只收用得到的規則和模板，不收依賴。

## Skills

| Skill | 做什麼 | 依賴 |
|---|---|---|
| [reporter](./reporter/) | 輸入題目＋選廣深，一次跑完產出全面研究報告：五波管線（方向→採集→擴大→缺口→交叉驗證＋紅隊辯論）、MDX文件集＋站內閱讀器＋入口頁。 | OhMyOpenCode primitives（task並行、explore／librarian、todowrite）；閱讀器需 `python -m http.server`；不需付費API；高成本模型預設全關 |

## 安裝

把要用的目錄複製到你的 skills 路徑即可（OhMyOpenCode：`~/.agents/skills/`），重開會話生效：

```bash
cp -r reporter ~/.agents/skills/
```

手動觸發才會跑，不會在寫code時自動載入（opencode.json設`permission.skill.<name>: ask`＋description顯式限定，另有`/reporter`命令入口可照抄）。
