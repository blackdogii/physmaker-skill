# 操作發文參考

第一版只設計了瀏覽器自動化一條路，被小威要求重新認真查過。這次實際查了 GitHub 上維護活躍的 skill repo 跟官方 MCP 服務，發現其實有「官方 API 串接」這條更好的路，只是需要小威做一次性設定跟一個信任第三方服務的決定——不是我能替他決定的事，必須先攤開來說清楚，再讓他選。

## 兩條可行路徑

### 路徑 A：官方 API 自動化(透過 Composio / Rube MCP)——功能更完整，但需要小威設定與同意

查證發現 [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude)(3,260 星、453 fork、2026-08-07 當天仍有更新，維護活躍)收錄的 `instagram-automation`、`facebook-automation` 等 skill，是透過 [Composio](https://composio.dev) 這家第三方服務的 Rube MCP(`https://rube.app/mcp`)串接 Instagram、Facebook Pages、YouTube 的**官方 Graph API**，不是瀏覽器模擬操作。實際能力包含建立貼文、輪播貼文、上傳影片、查詢 insights(觸及、互動數據)、查發布限制。

**這條路徑需要小威決定，不是我能自己接上去用的**：
- Rube MCP 是 Composio 這家第三方公司提供的服務，要把 Instagram/Facebook 帳號的 OAuth 授權交給它中介，不是直接對 Meta/Google 授權——這是信任與隱私上的取捨，要不要用這條路徑必須小威自己決定。
- Instagram 只支援 **Business 或 Creator 帳號**，個人帳號不支援；Facebook 只支援**粉專**，不支援個人塗鴉牆——如果目前帳號類型不符，需要先在平台端轉換。
- 素材(照片/影片)必須是「公開可存取的網址」，不能直接從本機上傳——代表需要先有一個素材託管的地方(例如網站自己的 media 資料夾、雲端硬碟公開連結)，這件事現在還沒有著落。
- 查證範圍內沒有找到 Threads 或 LINE 官方帳號的對應 MCP/API 串接，這兩個平台目前只能走路徑 B。

**如果小威同意走這條路**，設定步驟：
1. 在 Claude Code / Codex 的 MCP 設定裡加入 `https://rube.app/mcp`(不需要另外申請 API key)。
2. 依 [davepoon/buildwithclaude 的 instagram-automation](https://github.com/davepoon/buildwithclaude/blob/main/plugins/all-skills/skills/instagram-automation/SKILL.md)、facebook-automation 流程，用 `RUBE_MANAGE_CONNECTIONS` 走 OAuth 完成帳號授權。
3. 確認 Instagram/Facebook 帳號類型符合要求(Business/Creator、粉專)。
4. 準備素材的公開託管位置。
5. 之後才能真正做到「排程」「批次發布」「查 insights」這種進階操作，不再是每次都要人在場點按鈕。

### 路徑 B：瀏覽器自動化(claude-in-chrome)——現在就能用，不用額外設定，但每次都要人在場

不需要新設定，用小威已登入的 Chrome session 操作。**這是 Threads、LINE 官方帳號目前唯一可行的路徑**，也是還沒決定要不要走路徑 A 之前的預設做法。

## 路徑 B 流程

1. **確認前置條件**：文案與素材已經過小威在 SKILL.md「把關檢查點」確認，不是草稿階段就跳過來這步。
2. **開啟瀏覽器工具**：用 `tabs_context_mcp` 檢查目前分頁，確認是否已經開著目標平台且已登入；沒有的話用 `tabs_create_mcp` 開新分頁導覽過去。
3. **核對登入狀態**：用 `get_page_text`/`read_page` 確認頁面顯示的是小威的帳號/粉專身分，不是登出狀態或別的帳號——身分不對就停下來回報，不要猜測繼續操作。
4. **填入內容**：用 `computer`/`form_input` 貼上已核准的文案文字；素材(照片/影片)用 `file_upload`/`upload_image` 上傳小威提供的檔案——絕對不能自己找免費圖庫或生成圖片頂替。
5. **發布前最後確認**：截圖或用文字呈現「即將送出的最終畫面」給小威看，取得這一次的明確同意才進到下一步——不能用「文案早先核准過」當理由跳過這一步，發布動作本身才是真正公開、難以撤回的那一下。
6. **執行發布/排程**：小威同意後才點擊平台的發布或排程按鈕。平台原生的排程功能(例如 FB 預約發文)可以用，但排程動作本身一樣要事前給小威看過內容再設定。
7. **驗證結果**：發布後用 `get_page_text`/截圖確認貼文真的成功出現，回報貼文連結或截圖給小威。

## 兩條路徑共同的風險處理

- 不觸發平台的 alert/confirm 對話框(這類對話框會卡住整個瀏覽器連線)。
- 連續 2-3 次操作失敗(頁面沒反應、找不到元素、登入狀態異常、API 回傳錯誤)就停下來回報，不要一直重試硬闖或改用猜測性的替代操作。
- 遇到平台介面改版、API 規則變動，先如實回報現況，不要憑印象亂點或亂猜參數。
- 不管走哪條路徑，「發布前最後確認」這一步都不能省略——路徑 A 效率高不代表可以跳過人工把關。

## 出處與查證邊界

- 官方 API 路徑的存在與能力：完整讀過 [davepoon/buildwithclaude — instagram-automation SKILL.md](https://github.com/davepoon/buildwithclaude/blob/main/plugins/all-skills/skills/instagram-automation/SKILL.md)、[ComposioHQ/awesome-claude-skills — facebook-automation SKILL.md](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/composio-skills/facebook-automation/SKILL.md) 全文，並用 `gh repo view` 查證過 davepoon/buildwithclaude 的星數與更新時間。
- Threads、LINE 官方帳號沒有查到對應 MCP/API 串接：這是「查過沒找到」，不是「確定不存在」——查證方式是關鍵字搜尋 Composio 官方站與 GitHub，沒有窮舉 Composio 全部 1000+ 個工具列表逐一確認，如果之後要下定論，建議直接去 composio.dev 的完整工具清單頁面查一次。
