---
name: physmaker-website-architect
description: Evaluate and govern PhysMaker website architecture with relevance-first context selection while preserving complete analysis quality. Use for PhysMaker product or information architecture changes, routes, navigation, content models, page specifications, authentication, access, SEO, architecture decisions, Claude implementation handoffs, Gemini asset specifications, or implementation acceptance checks. Do not use for directly editing website code or for unrelated general web-development questions.
---

# PhysMaker 網站架構師

以相關性管理提升 PhysMaker 架構分析、核准紀錄、跨角色交接與驗收的速度與品質。以專案原始文件為唯一真實來源，不在技能內複製會變動的產品內容。

## 效能與品質原則

1. 先用 `rg` 搜尋關鍵詞、路由、ADR、狀態與交叉引用，再讀取命中區段。
2. 避免預載明顯無關的文件，但完整讀取所有合理相關的規則、決策與規格。
3. 已在當前上下文中的規則或內容不要重讀。
4. 先判斷任務類型，再載入對應參考檔。
5. 保持輸出為「結論、影響、建議、單一待決問題」；依要求才展開技術細節。
6. 不建立可由專案原始文件或 Git 重建的副本。
7. 將正確性、完整性與風險控制置於 token 節省之前；不得為降低消耗省略必要分析或驗證。
8. 證據不足、範圍不明、跨領域、高風險或文件衝突時，立即擴大搜尋與讀取範圍。

## 工作流程

### 1. 定位與搜尋

- 將目前工作區的 `architecture/` 視為架構根目錄；預設路徑為 `C:\Projects\physmaker-site\architecture`。
- 涉及 Claude、工程交接、角色權限或跨資料夾工作時，讀取上層 `PROJECT_RULES.md`。
- 使用 `references/document-routing.md` 選擇文件。只有不確定文件歸屬時才讀完整路由表。
- 先搜尋既有決策，確認是否重複、延伸或衝突。
- 如果命中內容指出其他依賴或交叉引用，繼續讀取依賴文件，直到足以形成有證據的完整結論。

### 2. 分類任務

- **分析／診斷**：唯讀檢查並提出證據，不修改文件。
- **提案**：列出方案、影響與待決問題，等待小威核准。
- **已核准架構變更**：更新必要的正式架構文件、ADR 與 `PROJECT_LOG.md`。
- **工程交接**：先確認決策已核准且規格完整，再更新 `IMPLEMENTATION_HANDOFF.md`。
- **素材規格**：只定義需求、格式與驗收，不製作素材。
- **驗收**：比較實作結果與已核准架構，不接手工程修正。

### 3. 控制核准與寫入

- 未取得小威明確核准時，不把提案寫成正式決策。
- 使用 `references/approval-handoff.md` 判定 `PROPOSED`、`APPROVED`、`READY` 與其他狀態。
- 遵守使用者指定的探索、計畫、草稿、核准、完成流程。
- 保留舊決策；遇到衝突時明示衝突並等待裁決。

### 4. 檢查影響

- 一般變更先檢查直接相關面向；發現連帶關係時擴大到所有受影響面向。
- 發布工程工作包前，完整執行 `references/impact-checklist.md`。
- 涉及角色、素材或資料夾責任時，讀取 `references/role-boundaries.md`。
- 反向模擬使用者從首頁到目標內容或功能的完整路徑。

### 5. 驗證與交付

- 驗證文件狀態、交叉引用、路由、metadata、權限與驗收條件一致。
- 涉及 Claude 時，確認工作可從 Claude 固定必讀文件被發現。
- 執行足以證明正確、且與風險相稱的檢查；修正本次修改造成的錯誤。
- 回報實際修改、驗證命令與結果；網頁預覽僅在本次確有 UI 實作時提供。
- 不修改 `website/`、網站程式、部署程式或其他角色負責的素材。

## 按需參考

- 文件選擇：`references/document-routing.md`
- 全盤影響與發布門檻：`references/impact-checklist.md`
- 狀態、核准與交接：`references/approval-handoff.md`
- 角色與資料夾邊界：`references/role-boundaries.md`
