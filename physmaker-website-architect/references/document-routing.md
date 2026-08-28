# 文件路由

先用 `rg` 定位既有內容，再讀取命中區段。只有跨領域決策才同時讀取多份文件。

| 需求 | 主要文件 | 必要時追加 |
|---|---|---|
| 品牌、定位、商業模式 | `00_BRAND_BUSINESS_STRATEGY.md` | `01_PRD.md` |
| 產品範圍、角色、流程 | `01_PRD.md` | `07_AUTH_COMMERCE_ACCESS.md` |
| 導覽、入口、路由、內容關係 | `02_INFORMATION_ARCHITECTURE.md` | `05_PAGE_SPEC.md`、`08_SEO_ANALYTICS.md` |
| schema、metadata、命名、內容邊界 | `03_CONTENT_SPEC.md` | `11_CONTENT_OPERATIONS.md` |
| 設計系統 | `04_DESIGN_SYSTEM.md` | `DESIGN_HANDOFF.md` |
| 頁面目的、區塊、狀態 | `05_PAGE_SPEC.md` | `09_ACCEPTANCE_CRITERIA.md` |
| 技術邊界、服務、安全、效能 | `06_TECHNICAL_SPEC.md` | `07_AUTH_COMMERCE_ACCESS.md` |
| 登入、授權、啟用碼、商務 | `07_AUTH_COMMERCE_ACCESS.md` | `06_TECHNICAL_SPEC.md` |
| SEO、robots、追蹤 | `08_SEO_ANALYTICS.md` | `02_INFORMATION_ARCHITECTURE.md` |
| 驗收 | `09_ACCEPTANCE_CRITERIA.md` | 對應領域文件 |
| 內容與素材流程 | `11_CONTENT_OPERATIONS.md` | 上層 `PROJECT_RULES.md` |
| 長期架構決策 | `decisions/DECISIONS.md` | `PROJECT_LOG.md` |
| 正式核准紀錄 | `PROJECT_LOG.md` | 對應 ADR 與規格 |
| Claude 可執行工作包 | `IMPLEMENTATION_HANDOFF.md` | 對應核准紀錄與 handoff 文件 |

專案子系統先讀取該子目錄的 `PROJECT_ARCHITECTURE.md`、`PROJECT_STATUS.md` 或明示的匯入規則，再回到共用架構文件檢查衝突。
