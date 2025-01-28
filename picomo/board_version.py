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

import board
import digitalio


class BoardVersion:
    version_map = {
        3: (2, 0),
        2: (3, 0),
        1: (-1, 1),
        0: (-1, 0),
    }

    def __init__(self):
        code = 0
        msb = digitalio.DigitalInOut(board.GP13)
        msb.switch_to_input(pull=digitalio.Pull.UP)
        if msb.value:
            code |= 2
        msb.deinit()
        lsb = digitalio.DigitalInOut(board.GP14)
        lsb.switch_to_input(pull=digitalio.Pull.UP)
        if lsb.value:
            code |= 1
        lsb.deinit()

        self.version = BoardVersion.version_map[code]
        self.major = self.version[0]
        self.minor = self.version[1]

    def is_v2(self):
        return self.major == 2

    def is_v3(self):
        return self.major == 3

    def check(self):
        b = board.board_id
        if b == "heiafr_picomo_v3" and self.is_v3():
            return
        if b == "heiafr_picomo_v2" and self.is_v2():
            return
        raise RuntimeError("Board version mismatch")

    def __str__(self):
        if self.version[0] == -1:
            return "Unknown"
        return f"v{self.version[0]}.{self.version[1]}"
