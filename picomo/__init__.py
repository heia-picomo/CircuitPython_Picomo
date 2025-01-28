# SPDX-FileCopyrightText: 2025 Jacques Supcik <jacques.supcik@hefr.ch>
#
# SPDX-License-Identifier: MIT

"""
`picomo`
=======================================================================

Interface to Picomo devices

* Author(s): Jacques Supcik <jacques.supcik@hefr.ch>

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit Deboucer library:
  https://github.com/adafruit/Adafruit_CircuitPython_Debouncer
* Adafruit SHTC3 library:
  https://github.com/adafruit/Adafruit_CircuitPython_SHTC3

"""

import adafruit_shtc3
import board
import digitalio
from adafruit_debouncer import Debouncer

from .board_version import BoardVersion
from .buzzer import Buzzer
from .led import RGBLed
from .logo import Logo

button_pins = {
    "sw_up": board.SW_UP,
    "sw_mid": board.SW_MID,
    "sw_down": board.SW_DOWN,
    "sw_right": board.SW_RIGHT,
    "sw_left": board.SW_LEFT,
    "sw_topl": board.SW_TOPL,
    "sw_topr": board.SW_TOPR,
}

buttons = {}

__all__ = [
    "logo",
    "buzzer",
    "led",
    "buttons",
    "sht",
    "board_version",
    "update",
]

logo = Logo()
buzzer = Buzzer()
led = RGBLed()
i2c = board.I2C()
sht = adafruit_shtc3.SHTC3(i2c)
board_version = BoardVersion()

for name, pin_name in button_pins.items():
    pin = digitalio.DigitalInOut(pin_name)
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    buttons[name] = Debouncer(pin)


def update():
    for name in button_pins.keys():
        buttons[name].update()
