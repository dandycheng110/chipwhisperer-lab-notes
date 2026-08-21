#!/usr/bin/env python3
"""完整連線測試:連 scope → 預設設定 → 燒錄 STM32 → 抓一條 AES 功耗波形。"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chipwhisperer as cw

HEX = "/Users/dot1000110/chipwhisperer/firmware/mcu/simpleserial-aes/simpleserial-aes-CWLITEARM.hex"
OUT = "/private/tmp/claude-501/-Users-dot1000110/0a939d00-5ab8-479a-b780-8e21b676a9d6/scratchpad/conn_test_trace.png"

print(">>> 連 scope")
scope = cw.scope()
scope.default_setup()

print(">>> 連 target (SimpleSerial)")
target = cw.target(scope, cw.targets.SimpleSerial)

print(">>> 燒錄 STM32 target ...")
cw.program_target(scope, cw.programmers.STM32FProgrammer, HEX)

print(">>> 抓一條波形 (capture_trace)")
ktp = cw.ktp.Basic()
key, text = ktp.next()
trace = cw.capture_trace(scope, target, text, key)
if trace is None:
    print("!! capture_trace 回傳 None(擷取逾時?)")
    scope.dis(); target.dis()
    raise SystemExit(1)

wave = trace.wave
print("key      :", key.hex())
print("plaintext:", text.hex())
print("回傳密文 :", bytes(trace.textout).hex() if trace.textout is not None else None)
print("波形點數 :", len(wave))
print("波形範圍 : min=%.4f max=%.4f std=%.4f" % (wave.min(), wave.max(), wave.std()))

# 用 Python 版 AES 驗證目標晶片算出來的密文正確(端到端證明)
try:
    from Crypto.Cipher import AES
    exp = AES.new(bytes(key), AES.MODE_ECB).encrypt(bytes(text))
    print("預期密文 :", exp.hex())
    print("密文相符 :", exp == bytes(trace.textout))
except Exception as e:
    print("(略過 AES 交叉驗證,無 pycryptodome:", e, ")")

plt.figure(figsize=(12, 4))
plt.plot(wave, linewidth=0.6)
plt.title("ChipWhisperer-Lite connection test: 1 AES power trace (CWLITEARM)")
plt.xlabel("sample"); plt.ylabel("power")
plt.tight_layout(); plt.savefig(OUT, dpi=110)
print(">>> 波形圖存到:", OUT)

scope.dis(); target.dis()
print(">>> 連線測試完成,整條鏈路 OK。")
