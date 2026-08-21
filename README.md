# ChipWhisperer-Lite 實驗筆記

一片 ChipWhisperer-Lite CW1173(目標晶片 STM32F303 / CWLITEARM),在 macOS 上從零建環境,完成側信道分析與故障注入,並延伸到無人機硬體安全研究。

| Lab | 內容 | 結果 |
|---|---|---|
| 1 連線測試 | 燒錄 AES 韌體、抓功耗波形、密文交叉比對 | ✓ 整條鏈路通,密文與 Python AES 相符 |
| 2 SCA101 CPA | 相關性功耗分析 | ✓ 100 條波形還原 16/16 金鑰位元組 |
| 3 Fault101 時脈毛刺 | 讓迴圈算錯 | ✓ 5 次毛刺成功、22 次打當晶片 |
| 4 毛刺繞過密碼驗證 | 跳過 `passok=0` | ✓ 錯密碼 4 次被判定通過 |
| 5 SCA DPA | 差分功耗分析 | ✓ 約 700 條波形還原全金鑰(CPA vs DPA 收斂比較) |

**📄 網頁版筆記(GitHub Pages):** 見本 repo 的 Pages 網址
**📝 完整文字筆記:** [NOTES.md](NOTES.md)
**🚁 無人機安全研究延伸:** [無人機安全研究延伸.md](無人機安全研究延伸.md)

## 內容

- `index.html` — 排版好的網頁版筆記(圖表已內嵌,單檔即可開)
- `NOTES.md` — Markdown 版完整筆記(含踩坑實錄與重跑指令)
- `無人機安全研究延伸.md` — 把 ChipWhisperer 技巧接到無人機硬體安全的研究地圖
- `scripts/` — 八支 lab 腳本(連線測試、SCA CPA/DPA、Fault 毛刺與密碼繞過)
- `figures/` — 三張結果圖(功耗波形、CPA 相關性、glitch map)

## 環境

Python 3.12 + chipwhisperer 6.0.0,目標晶片 STM32F303。詳細環境設定與踩坑筆記見 [NOTES.md](NOTES.md)。

> 所有攻擊皆針對自有硬體、供資安學習與防禦研究用途。
