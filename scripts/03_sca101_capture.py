#!/usr/bin/env python3
"""SCA101 第一步:抓 N 條功耗波形(固定金鑰、隨機明文),存成 npz。"""
import numpy as np
import chipwhisperer as cw

HEX = "/Users/dot1000110/chipwhisperer/firmware/mcu/simpleserial-aes/simpleserial-aes-CWLITEARM.hex"
OUT = "/private/tmp/claude-501/-Users-dot1000110/0a939d00-5ab8-479a-b780-8e21b676a9d6/scratchpad/sca101_traces.npz"
N = 100

scope = cw.scope()
scope.default_setup()
target = cw.target(scope, cw.targets.SimpleSerial)
print(">>> 燒錄 AES 韌體")
cw.program_target(scope, cw.programmers.STM32FProgrammer, HEX)

ktp = cw.ktp.Basic()          # 固定金鑰 + 每次隨機明文(SCA101 標準設定)
traces, textins = [], []
key = None
print(f">>> 開始擷取 {N} 條波形...")
for i in range(N):
    k, t = ktp.next()
    tr = cw.capture_trace(scope, target, t, k)
    if tr is None:
        print(f"  第 {i} 條逾時,略過")
        continue
    traces.append(tr.wave)
    textins.append(tr.textin)
    key = tr.key
    if (i + 1) % 20 == 0:
        print(f"  已擷取 {i+1}/{N}")

traces = np.array(traces)
textins = np.array([list(t) for t in textins], dtype=np.uint8)
key = np.array(list(key), dtype=np.uint8)
np.savez(OUT, traces=traces, textins=textins, key=key)
print(">>> 擷取完成")
print("  traces shape:", traces.shape)
print("  真實金鑰    :", bytes(key).hex())
print("  存檔        :", OUT)
scope.dis(); target.dis()
