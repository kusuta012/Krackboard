from machine import Pin
import time

led = Pin(16, Pin.OUT)
led.off()
time.sleep(1)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
