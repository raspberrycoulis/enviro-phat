from .i2c_bus import bus
from .ads1015 import ads1015
from .bmp280 import bmp280
from .leds import leds
from .lsm303d import lsm303d
from .tcs3472 import tcs3472


leds = leds()
light = tcs3472(bus)
weather = bmp280(bus)
analog = ads1015(bus)
motion = lsm303d(bus)

if bus == 1:
    lightalt = tcs3472(0)
    weatheralt = bmp280(0)
    analogalt = ads1015(0)
    motionalt = lsm303d(0)
