#!/usr/bin/env python3
"""Step 1: 只連 scope,確認 USB / libusb 在 macOS 能通。"""
import chipwhisperer as cw

print(">>> 嘗試 cw.scope() 連線...")
scope = cw.scope()
print("OK: scope 連上了")
print("  scope 類型 :", type(scope).__name__)
try:
    print("  FW version:", scope.fw_version)
except Exception as e:
    print("  (讀 fw_version 失敗:", e, ")")
try:
    print("  sn        :", scope.sn)
except Exception:
    pass
print("  gain      :", scope.gain.gain)
print("  samples   :", scope.adc.samples)
print("  clkgen    :", scope.clock.clkgen_freq)
scope.dis()
print(">>> 已中斷連線,USB 通訊正常。")
