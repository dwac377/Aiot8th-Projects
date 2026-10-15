from machine import Pin, PWM
import time

flash = PWM(Pin(4), freq=500, duty=0)  # 플래시를 PWM 으로 연결

levels = [0, 10, 30, 100, 300, 600, 700, 800, 900, 1000, 1023]  # duty 는 0 ~ 1023

for d in levels:
    flash.duty(d)
    print("duty", d, "→", d * 100 // 1023, "%")
    time.sleep_ms(500)

flash.duty(0)
flash.deinit()
print("끝")
