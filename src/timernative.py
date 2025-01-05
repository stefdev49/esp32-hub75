from machine import Timer
import micropython
from time import time_ns

@micropython.native
def isr():
    print('Timer interrupt!')

# if you remove the @micropython.native decorator,
# there will be 4 isr() messages as expected
@micropython.native
def long_lived_function():
    start = time_ns()
    while time_ns() - start < 2_000_000_000:
        pass

# launch timer interrupt every 500 ms
tim0 = Timer(0)
tim0.init(period=500, mode=Timer.PERIODIC, callback=lambda t: isr())

long_lived_function()
