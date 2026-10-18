# 明智選擇（Wise Choice）

可安裝到手機主畫面的網頁應用程式（PWA）。用戶填寫處境後，AI 先搜尋公開資料寫初稿，再由第二輪獨立審查檢查邏輯、利益衝突與置信度，最後輸出排名建議、步驟、止蝕點、來源與實踐追蹤清單。

## 兩個版本

| 版本 | 開啟方式 | 網上搜尋 | 需要 |
|---|---|---|---|
| 試用版 | claude.ai Artifact 連結 | 沒有（只用模型既有知識，報告不列網址） | 你的 claude.ai 帳戶 |
| 安裝版 | https://kongincanada2.github.io/wise-choice-suggest/ | 有（Claude API 網上搜尋工具） | 你自己的 Anthropic API 金鑰 |

## 來源核實

安裝版會記錄每次搜尋實際取得的網址。AI 寫出的引用如果不在這份清單內，會在顯示前自動刪除，報告頂部會寫明刪除了多少個。

## 安裝到手機

用手機開啟 https://kongincanada2.github.io/wise-choice-suggest/ ，到「設定與說明」輸入 Anthropic API 金鑰，然後：

- iPhone：Safari → 分享 → 「加入主畫面」
- Android：Chrome → 選單 → 「安裝應用程式」

網站由 GitHub Pages 從 `main` 分支的 `docs/` 資料夾發佈。

## 修改

只改 `src/app.html`（試用版與安裝版共用），然後執行 `python3 tools/build.py` 重建 `docs/`。
