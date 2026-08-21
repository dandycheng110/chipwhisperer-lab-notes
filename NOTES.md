# ChipWhisperer-Lite 實驗筆記

> 一片 ChipWhisperer-Lite CW1173(32-bit basic,目標晶片 STM32F303 / CWLITEARM),
> 在 macOS(Apple Silicon)上從零建環境,完成側信道分析(CPA、DPA)與故障注入(時脈毛刺、繞過密碼驗證),
> 並延伸到無人機硬體安全研究。
> 日期:2026-08-21

---

## 背景:兩種「不解密碼卻能偷金鑰」的攻擊

- **側信道分析(Side-Channel Analysis)**:晶片在做運算時,耗電量會隨著它處理的資料而細微變化。
  就像隔著門聽人打字,從聲音節奏猜出打了什麼。我們量晶片跑 AES 時的功耗波形,反推出金鑰,
  全程不需要碰到金鑰本身。
- **故障注入(Fault Injection)**:在對的一瞬間給晶片一個「壞掉的時脈或電壓」,讓它做錯一步——
  跳過一行指令、算錯一個數字。就像趁人分心時抽掉他手上的一張牌。這可以用來繞過密碼比對、破解安全開機。

---

## 硬體與環境

| 項目 | 內容 |
|---|---|
| 板子 | ChipWhisperer-Lite CW1173(32-bit basic) |
| 目標晶片 | STM32F303(CWLITEARM,ID 0x446) |
| 平台 | macOS,Apple Silicon(arm64) |
| Python venv | `~/cw-venv`(Python 3.12.14 + chipwhisperer 6.0.0 + JupyterLab) |
| 官方原始碼 | `~/chipwhisperer`(firmware/mcu + jupyter/courses) |
| ARM 工具鏈 | `~/arm-gnu-toolchain/bin`(編 target 韌體用) |
| 板子韌體 | 已從 0.50.0 升級到 0.65.0 |

---

## Lab 1 — 連線測試

**目的**:確認「擷取端(scope)→ 目標晶片 → 序列通訊 → 波形擷取」整條鏈路都通。

**做法**:編譯並燒錄 `simpleserial-aes` 韌體到 STM32,送一組明文讓晶片做 AES 加密,
抓一條功耗波形,並把晶片算出的密文跟 Python 版 AES 交叉比對。

**結果**:
- STM32F303 燒錄成功(驗證 6055 bytes OK)
- 抓到 5000 點的功耗波形,看得出 AES 每一輪的週期性結構
- 目標晶片密文 `b4501b81…` = Python AES 預期密文 → **完全相符**

📈 圖:`figures/conn_test_trace.png`

---

## Lab 2 — SCA101 側信道分析(CPA 還原 AES 金鑰)

**目的**:只靠功耗波形,把 AES-128 的 16 個位元組金鑰整把還原。

**原理(CPA,相關性功耗分析)**:AES 第一步會算 `Sbox[明文 ⊕ 金鑰]`。
對每個位元組,把 0~255 的金鑰猜測都試一遍,用「這個中間值有幾個 bit 是 1(漢明重量)」
當作預測的耗電量,再去跟實際波形算相關係數。**猜對的金鑰,相關係數會明顯高於其他 255 個。**

**做法**:抓 100 條波形(固定金鑰、隨機明文),對 16 個位元組各跑一次 CPA。

**結果**:
- 還原金鑰 `2b7e151628aed2a6abf7158809cf4f3c` → **16/16 位元組全對**
- 各位元組最佳相關係數:平均 0.90(正確金鑰壓倒性勝出)
- 只用 100 條波形就成功

📈 圖:`figures/sca101_cpa_byte0.png`(正確金鑰 0x2b 那根紅柱衝到 0.93,其餘全趴在 0.3~0.5)

---

## Lab 3 — Fault101 故障注入(時脈毛刺)

**目的**:用時脈毛刺讓一個「應該回傳固定值」的迴圈算錯,證明能干擾程式流程。

**原理(clock glitch)**:target 跑一個 `50×50` 的迴圈,`cnt` 正常應該 = **2500**。
在迴圈執行時,對時脈灌一個超短的壞邊緣,CPU 就可能來不及正確執行某個週期,
導致跳過一次 `cnt++`(或整個算爆)。我們掃描 `(width, offset, ext_offset)` 三個參數找出有效的毛刺。

**做法**:掃 2645 組參數,每次發 `'g'` 指令跑迴圈,判定結果為
正常(2500)/ 毛刺成功(≠2500)/ 當機重置(沒回應,用 nRST 救回)。

**結果**:
- **5 次毛刺成功**——最漂亮的是 `cnt=2499`(剛好少數一次 `cnt++`,教科書級的「單一指令跳過」)
- **22 次把晶片打當機**
- 成功參數集中在一條敏感帶(width −9~−1、offset 43~35)

📈 圖:`figures/fault101_glitch_map.png`

| width (%) | offset (%) | ext | cnt |
|---:|---:|---:|---:|
| −9 | 43 | 6 | 1448736172 |
| −5 | 39 | 6 | 4227802734 |
| −1 | 35 | 6 | 4263500 |
| 3 | −1 | 10 | **2499** |
| 3 | −1 | 15 | 2501 |

---

## Lab 4 — 進階故障注入(毛刺繞過密碼驗證)

**目的**:用毛刺繞過身分驗證——這是嵌入式/無人機安全最核心的攻擊(繞過安全開機、跳過簽章檢查)。

**原理**:`simpleserial-glitch` 的 `'p'` 指令比對密碼(正解 `"touch"`),`passok` 預設 1,比對到不符才設 0。
送**錯的**密碼正常會回 `passok=0`(拒絕);在比對迴圈時下毛刺讓「設為 0」那步被跳過,`passok` 保持 1 → **驗證被繞過**。

**結果**:
- 無毛刺基準:錯密碼 → `passok=0`(拒絕,正常)
- 掃 4940 組參數:**4 次成功繞過**(錯密碼卻回 `passok=1`)、286 次當機、其餘正常拒絕(76 秒)

---

## Lab 5 — SCA 方法二:DPA(差分功耗分析)

**目的**:用另一種經典側信道方法還原金鑰,並對照 CPA 的效率。

**原理**:DPA 靠「Sbox 輸出某個 bit 是 0 還是 1,平均功耗會差一點」把波形分兩群相減(差分平均),
正確金鑰會出現最大峰值。

**結果(DPA vs CPA 隨波形數的正確位元組數 /16)**:

| 波形數 | CPA | DPA |
|---:|---:|---:|
| 100 | 16 | 4 |
| 300 | 16 | 14 |
| 700 | 16 | **16** |
| 2000 | 16 | 16 |

**結論**:CPA 只要 100 條就破全金鑰;單 bit DPA 要約 700 條才追上。兩種方法最終都還原完整 AES-128 金鑰。

---

## 🚁 延伸:無人機安全研究

這些 ChipWhisperer 技巧可直接延伸到無人機硬體安全(飛控多用 STM32,同一晶片家族)。
完整研究地圖見 **[無人機安全研究延伸.md](無人機安全研究延伸.md)**——涵蓋韌體萃取、繞過安全開機、
圖傳/遙測金鑰側信道、MAVLink 通訊安全,以及合規邊界。

---

## 踩坑筆記(重要)

1. **Homebrew 的 `arm-none-eabi-gcc` 缺 newlib**,編韌體會噴 `stdint.h not found`。
   官方 cask 是 `.pkg` 需 sudo,改用 `brew fetch --cask gcc-arm-embedded` 下載,
   再 `pkgutil --expand-full` 免密碼解開,把 Payload 當工具鏈。**編韌體前把 `~/arm-gnu-toolchain/bin` 擺 PATH 最前面。**
2. **macOS 用 `system_profiler` 讀 USB 常空白**,改用 `ioreg -p IOUSB -l` 才看得到板子(NewAE VID 11070 / 0x2b3e)。
3. **板子出廠韌體 0.50.0 與 chipwhisperer 6.0.0 不相容**,用 `scope.upgrade_firmware()` 升到 0.65.0 才能用。

---

## 如何重跑

```bash
# 編韌體(以 AES 為例)
export PATH="$HOME/arm-gnu-toolchain/bin:$PATH"
cd ~/chipwhisperer/firmware/mcu/simpleserial-aes
make PLATFORM=CWLITEARM CRYPTO_TARGET=TINYAES128C

# 跑 lab 腳本
~/cw-venv/bin/python ~/chipwhisperer-labs/02_connection_test.py    # 連線測試
~/cw-venv/bin/python ~/chipwhisperer-labs/03_sca101_capture.py     # SCA101 抓波形
~/cw-venv/bin/python ~/chipwhisperer-labs/04_sca101_cpa.py         # SCA101 CPA 攻擊
~/cw-venv/bin/python ~/chipwhisperer-labs/05_fault101_glitch.py    # Fault101 毛刺掃描
~/cw-venv/bin/python ~/chipwhisperer-labs/06_fault_passbypass.py   # 毛刺繞過密碼驗證
~/cw-venv/bin/python ~/chipwhisperer-labs/08_dpa_moretraces.py     # DPA vs CPA 收斂

# 開官方 Jupyter notebook
~/cw-venv/bin/jupyter lab --notebook-dir ~/chipwhisperer/jupyter
```

## 延伸方向

- **SCA**:改用內建 `cw.analyzer` 跑 CPA;試攻擊硬體 AES;做 TVLA 洩漏評估。
- **Fault**:改玩電壓毛刺(VCC glitch);把密碼繞過升級成 secure-boot 繞過情境。
- **無人機**:見 [無人機安全研究延伸.md](無人機安全研究延伸.md)。
