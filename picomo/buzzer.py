# SPDX-FileCopyrightText: 2025 Jacques Supcik <jacques.supcik@hefr.ch>
#
# SPDX-License-Identifier: MIT

"""
`buzzer`
=======================================================================

Interface to Picomo buzzer

* Author(s): Jacques Supcik <jacques.supcik@hefr.ch>

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import time

import board
import pwmio


class Buzzer:
    def __init__(self):
        self._buzzer = pwmio.PWMOut(board.BUZZER, variable_frequency=True)

    def __del__(self):
        self._buzzer.deinit()

    def play(self, duration=0.1, frequency=4000):
        self._buzzer.frequency = frequency
        self._buzzer.duty_cycle = 2**15
        time.sleep(duration)
        self._buzzer.duty_cycle = 0
