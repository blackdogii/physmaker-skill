# physmaker-skill

個人整理、實戰用過的 [Claude Code](https://claude.com/claude-code) / [Codex](https://openai.com/codex/) Skills 集合，共 13 個。每份都是真的在日常工作（教學、PhysMaker 網站、遊戲開發、檔案整理、社群經營、簡報製作）裡反覆用過、修過的版本，不是隨手寫的範例。

## 目錄

### 通用方法論

| Skill | 用途 |
|---|---|
| [`task-methodology`](./task-methodology) | 接到新功能/新頁面/新工具需求時，先判斷「跟需求方討論架構」還是「調研市面做法再統整模仿」；附反 AI 芭樂樣板設計原則、動畫決策速查、無障礙必查。 |
| [`file-reorganization`](./file-reorganization) | 大規模檔案/資料夾整理方法論：安全鐵律（只能移動不能刪除、可回溯記錄）、分類判準（本質類型 vs 發生場合）、內容驗證工具箱、批次年份推算技巧、常見假陽性清單。不限定特定資料來源。 |
| [`session-handoff`](./session-handoff) | 收工前寫一份交接筆記（今天完成/尚未完成/下一步/注意事項），存在專案自己的 `docs/HANDOFF.md`，下次接手（不管是自己還是別人）打開一個檔案就知道進度到哪，不需要另外接一個共用知識庫。**只能手動明確叫用**，不會自動觸發，裝了也不會平常干擾其他工作。 |
| [`save`](./save) | 把對話/任務產出蒸餾進共用 Obsidian 知識庫（收件匣 capture 模式 + 每日整理 consolidate 模式），讓多個 AI 工具共用同一份長期記憶不會各自失憶。 |

> `session-handoff` 跟 `save` 做的事類似（都是「蒸餾+交接」），差別在規模：`session-handoff` 不需要任何額外設定，單一專案、單一檔案就能用，適合大多數人；`save` 綁定我自己維護的共用 Obsidian 知識庫（分類體系、跨專案索引、多 Agent 協調），是專門為管理大量長期累積筆記設計的重量級版本。不確定要用哪個就先用 `session-handoff`。

### 內容產出

| Skill | 用途 |
|---|---|
| [`social-media-manager`](./social-media-manager) | 社群小編能力：企劃內容主題、寫文案、操作瀏覽器把已核准的貼文送到 Facebook/Instagram/Threads/YouTube/LINE。真實素材與最終把關永遠由使用者自己負責，發布前一定要人工確認畫面。 |
| [`high-quality-presentation-workflow`](./high-quality-presentation-workflow) | 高品質簡報製作的端到端治理流程：來源查證、證據邊界、敘事設計、視覺系統核准、代表樣張核准、逐頁製作、獨立視覺 QA、講者備忘稿、最終 PPTX/HTML 驗證。 |

### 遊戲開發

| Skill | 用途 |
|---|---|
| [`game-upgrade`](./game-upgrade) | 遊戲定期健檢：玩家視角+資深工程師視角雙獨立平行審查（避免互相定錨），彙整成分級修改計畫，核准後才動手改，每輪寫版本化紀錄。跟引擎無關，Godot/Babylon/Bevy 或其他引擎都適用。 |
| [`godot-procedural-world`](./godot-procedural-world) | Godot 4 程序化 3D 世界生成：種子地形、道路、建築、植被、道具、地標、生成規則、分塊、驗證與效能。 |
| [`sound-pro`](./sound-pro) / [`sound-quick`](./sound-quick) | 遊戲音效素材取得，一快一精：`sound-quick` 從 Kenney.nl / Freesound.org 免費 CC0 素材快速湊齊 MVP 音效；`sound-pro` 用付費 AI 文字轉音效 API（ElevenLabs、Stable Audio）做客製化的招牌時刻音效。 |
| [`UI-pro`](./UI-pro) / [`UI-quick`](./UI-quick) | 遊戲/網頁 UI 素材取得，同樣一快一精：`UI-quick` 用現成免費資源包/主題庫（Kenney、shadcn/ui、DaisyUI）幾分鐘做出堪用UI；`UI-pro` 花錢/花時間/花大量 token 換取真正客製化的招牌畫面。 |

### 專案專屬

| Skill | 用途 |
|---|---|
| [`physmaker-website-architect`](./physmaker-website-architect) | PhysMaker 網站架構治理：以相關性優先的方式選讀文件，同時維持完整分析品質，適用架構決策、路由、內容模型、SEO、驗收檢查等。 |

## 安裝

每個資料夾就是一個獨立的 skill，複製整個資料夾（不是只複製 `SKILL.md` —— 有幾個 skill 底下還有 `references/`、`agents/` 子資料夾，缺了功能會不完整）到你的 skills 目錄。

**Claude Code — 全域安裝（所有專案都能用）**

```bash
git clone https://github.com/blackdogii/physmaker-skill.git
cp -r physmaker-skill/<skill-name> ~/.claude/skills/<skill-name>
```

**Claude Code — 只在單一專案安裝**

```bash
cp -r physmaker-skill/<skill-name> .claude/skills/<skill-name>
```

**Codex**

同樣的資料夾結構放進 `~/.codex/skills/<skill-name>`（全域）或專案內對應目錄即可，多數 skill 對 Claude Code / Codex 都通用（少數如 `save`、`game-upgrade` 本來就是雙工具設計）。

安裝後工具會依 `SKILL.md` 開頭的 `description` 自動判斷觸發時機，不需要額外設定。

## 關於「有裝就用、沒裝就走內建備援」

`task-methodology`、`UI-pro`、`UI-quick` 這三份內容裡會提到幾個**沒有收錄在這個 repo 裡**的其他 skill（例如 `emil-design-eng`、`ui-quality`、`asset-gen`）。這些是我自己日常環境裡另外裝的動畫/UI 專用 skill 或特定專案的本地 skill，屬於個人環境的累積經驗，所以刻意保留具體名稱、寫成明確條件句：「這個環境有裝就優先用，沒裝的話本檔案內建的濃縮版/基準就是備援方案」。也就是說，**這三份 skill 單獨拿去用完全沒問題，不會因為缺那些 skill 而故障**，只是在我自己的環境裡會有更深入的分工。

## 關於內容裡的「小威」與「PhysMaker」

這些 skill 是為了我自己（GitHub: [blackdogii](https://github.com/blackdogii)）跟我的教育科技品牌 [PhysMaker](https://physmaker.tw) 日常工作寫的，內容裡會直接稱呼「小威」（我自己）本人，`physmaker-website-architect` 也綁定 PhysMaker 網站的實際架構規則。其餘 skill 都是不限專案的通用方法論，換掉稱呼直接套用在別的專案上完全沒問題。

## 授權

MIT License，詳見 [LICENSE](./LICENSE)。歡迎直接使用、修改、拿去自己的專案套用。
