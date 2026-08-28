# 收件匣筆記 Frontmatter Schema

唯一版本，取代舊版 `01-收件匣/README.md` 建議格式（中文 key、欄位較少）與實務上已在用的英文 key 版本並存的狀況。

```yaml
---
date: YYYY-MM-DD
agent: Claude Code | Codex | 其他
project: 專案名稱或「跨專案」
category: 規則 | 偏好 | 工作流 | 規劃 | 決策 | 專案 | Skill | Inbox
source: 一句話說明這是從哪個任務／對話蒸餾出來的
related:
  - "[[其他相關筆記檔名]]"   # 可省略，沒有相關筆記就整段不寫
status: 待每日復盤整理 | 待小威確認 | 已合併
---
```

## 欄位說明

- `date`：實際寫入日期（Asia/Taipei），不是任務發生日期。
- `agent`：實際執行寫入動作的 Agent 名稱，用於追溯。
- `project`：對應到 `50-專案記憶/` 的專案筆記名稱；不屬於任何特定專案（例如純偏好、跨專案工作流）填「跨專案」。
- `category`：見 `classification-taxonomy.md`，只能用表列的值。
- `source`：簡短說明來源脈絡，方便之後回頭追溯是哪次任務／對話產生的，不需要完整轉錄對話。
- `related`：選填，用 Obsidian wikilink 語法連結既有筆記（例如查重時發現的部分重疊筆記）。
- `status`：
  - `待每日復盤整理`：capture 模式寫入時的預設值，代表還沒被 consolidate 處理過。
  - `待小威確認`：內容屬於高風險操作或跟既有內容衝突，等待人工核准。
  - `已合併`：consolidate 模式處理完、內容已寫入正式檔案，這篇筆記即將被移到來源封存。

## 檔名格式

`YYYYMMDD-HHmmss_Agent_專案.md`——沿用 `00-系統/寫入規則.md` 既有規定，時間戳確保同時間多 Agent 寫入不會互相覆蓋。
