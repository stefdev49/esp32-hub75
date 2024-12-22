from machine import Pin, Timer

led = Pin(2, Pin.OUT)
tim = Timer(0)

def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
