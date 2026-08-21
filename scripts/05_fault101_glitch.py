#!/usr/bin/env python3
"""Fault101:時脈毛刺(clock glitch)攻擊 simpleserial-glitch 的 glitch_loop。
迴圈正常 cnt=2500;掃描 (width, offset, ext_offset) 找出讓 cnt!=2500(運算被改)
或晶片當機重置的毛刺參數。"""
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import chipwhisperer as cw

HEX = "/Users/dot1000110/chipwhisperer/firmware/mcu/simpleserial-glitch/simpleserial-glitch-CWLITEARM.hex"
FIG = "/private/tmp/claude-501/-Users-dot1000110/0a939d00-5ab8-479a-b780-8e21b676a9d6/scratchpad/fault101_glitch_map.png"

def reset_target(scope):
    scope.io.nrst = "low"
    time.sleep(0.03)
    scope.io.nrst = "high_z"
    time.sleep(0.03)

scope = cw.scope()
scope.default_setup()
scope.adc.timeout = 0.1                      # 當機時快速判定逾時
target = cw.target(scope, cw.targets.SimpleSerial)
print(">>> 燒錄 glitch 韌體")
cw.program_target(scope, cw.programmers.STM32FProgrammer, HEX)
reset_target(scope)

# --- 時脈毛刺設定 ---
scope.glitch.clk_src = "clkgen"
scope.glitch.output = "clock_xor"
scope.glitch.trigger_src = "ext_single"
scope.glitch.repeat = 1
scope.io.hs2 = "glitch"

def try_glitch(width, offset, ext_offset):
    scope.glitch.width = width
    scope.glitch.offset = offset
    scope.glitch.ext_offset = ext_offset
    target.flush()
    scope.arm()
    target.simpleserial_write("g", bytearray())
    timed_out = scope.capture()              # True = ADC 逾時(通常代表當機)
    val = target.simpleserial_read("r", 4, timeout=10)
    if timed_out or val is None or len(val) < 4:
        return "reset", None
    cnt = int.from_bytes(bytes(val[:4]), "little")
    if cnt != 2500:
        return "success", cnt
    return "normal", cnt

widths = list(range(-45, 46, 4))
offsets = list(range(-45, 46, 4))
ext_offsets = [0, 3, 6, 10, 15]

successes, resets, normals = [], 0, 0
attempts = 0
t0 = time.time()
print(f">>> 開始掃描:{len(widths)}×{len(offsets)}×{len(ext_offsets)} = "
      f"{len(widths)*len(offsets)*len(ext_offsets)} 次")
for w in widths:
    for o in offsets:
        for e in ext_offsets:
            attempts += 1
            try:
                res, cnt = try_glitch(w, o, e)
            except Exception:
                reset_target(scope)
                resets += 1
                continue
            if res == "success":
                successes.append((w, o, e, cnt))
                print(f"  *毛刺成功* width={w:>4} offset={o:>4} ext={e:>3}  cnt={cnt} (應為2500)")
            elif res == "reset":
                resets += 1
                reset_target(scope)
            else:
                normals += 1
    print(f"  ...width={w:>4} 掃完  (累計 成功{len(successes)} / 當機{resets} / 正常{normals})")

dt = time.time() - t0
print("\n=== Fault101 毛刺掃描結果 ===")
print(f"總嘗試      : {attempts}  (耗時 {dt:.1f}s)")
print(f"毛刺成功    : {len(successes)}  (cnt != 2500,運算被改)")
print(f"當機/重置   : {resets}")
print(f"正常        : {normals}")
if successes:
    print("成功範例(前 10 筆):")
    for s in successes[:10]:
        print(f"   width={s[0]:>4} offset={s[1]:>4} ext={s[2]:>3}  cnt={s[3]}")

# 畫 glitch map:成功參數散佈在 (width, offset) 平面
plt.figure(figsize=(7, 6))
if successes:
    sw = [s[0] for s in successes]; so = [s[1] for s in successes]
    plt.scatter(sw, so, c="#d62728", s=40, label=f"success (cnt!=2500)  n={len(successes)}")
plt.xlabel("glitch width (%)"); plt.ylabel("glitch offset (%)")
plt.title("Fault101 clock-glitch map: params that faulted the loop")
plt.grid(True, alpha=0.3); plt.legend(); plt.tight_layout(); plt.savefig(FIG, dpi=110)
print(">>> glitch map:", FIG)

scope.dis(); target.dis()
