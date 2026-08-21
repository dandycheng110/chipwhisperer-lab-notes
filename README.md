# ChipWhisperer-Lite 實驗筆記

一片 ChipWhisperer-Lite CW1173(目標晶片 STM32F303 / CWLITEARM),在 macOS 上從零建環境,完成三個 lab:

| Lab | 內容 | 結果 |
|---|---|---|
| 連線測試 | 燒錄 AES 韌體、抓功耗波形、密文交叉比對 | ✓ 整條鏈路通,密文與 Python AES 相符 |
| SCA101 | CPA 相關性功耗分析 | ✓ 16/16 位元組還原 AES 金鑰 |
| Fault101 | 時脈毛刺故障注入 | ✓ 5 次毛刺成功、22 次打當晶片 |

**📄 網頁版筆記(GitHub Pages):** 見本 repo 的 Pages 網址
**📝 完整文字筆記:** [NOTES.md](NOTES.md)

## 內容

- `index.html` — 排版好的網頁版筆記(圖表已內嵌,單檔即可開)
- `NOTES.md` — Markdown 版完整筆記(含踩坑實錄與重跑指令)
- `scripts/` — 五支 lab 腳本(連線測試、SCA101 擷取/CPA、Fault101 毛刺掃描)
- `figures/` — 三張結果圖(功耗波形、CPA 相關性、glitch map)

## 環境

Python 3.12 + chipwhisperer 6.0.0,目標晶片 STM32F303。詳細環境設定與踩坑筆記見 [NOTES.md](NOTES.md)。

> 所有攻擊皆針對自有硬體、供資安學習用途。
