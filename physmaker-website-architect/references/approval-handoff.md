# 核准與交接

以專案上層 `PROJECT_RULES.md` 和現有正式文件為準；本檔只提供判斷順序。

## 狀態

- `PROPOSED`：已提出，尚未取得小威明確核准。
- `APPROVED`：小威已核准產品或架構決策。
- `READY`：已有 `APPROVED` 依據，規格、影響、驗收及文件入口完整，可交由指定角色執行。
- `IMPLEMENTING`、`CONTENT_PENDING`、`IMPLEMENTED`、`VERIFIED`、`BLOCKED`、`REJECTED`：依專案原始規則使用，不由推測升級狀態。

## 判斷順序

1. 找出小威的明確核准內容與範圍。
2. 找出對應 ADR 或正式規格。
3. 純架構決策只寫 `APPROVED`，不要建立虛假的 `READY`。
4. 工程工作包需列出目的、依據、範圍、連帶影響、明確不變、實作限制、驗收與回報位置。
5. 在 `PROJECT_LOG.md` 與 `IMPLEMENTATION_HANDOFF.md` 建立雙向引用。
6. 未核准部分保留為待決問題，不混入已核准工作包。

## 最小決策摘要

- 結論
- 主要影響
- 建議選項
- 單一待決問題

## 最小完成回報

- Details：實際修改或新增的檔案與內容。
- Verification：執行命令與實際結果。
- Preview：只有 UI 變更時提供啟動方式、URL 與驗證步驟。
- Skills Used：列出實際使用的技能與主要工具。
