# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# type: ignore

"""CircuitPython Essentials Pin Map Script"""
import microcontroller
import board

board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        pins = []
        for alias in dir(board):
            if getattr(board, alias) is getattr(microcontroller.pin, pin):
                pins.append("board.{}".format(alias))
        if len(pins) > 0:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)


""" 
board.A0 board.GP26 board.GP26_A0
board.A1 board.GP27 board.GP27_A1
board.A2 board.GP28 board.GP28_A2
board.A3 board.BAT_SENSE
board.GP0
board.GP1
board.GP10
board.GP11
board.GP12
board.GP13
board.GP14
board.GP15
board.GP16
board.GP17
board.GP18
board.GP19
board.GP2
board.GP20
board.GP21
board.GP22
board.GP25 board.LED
board.GP3
board.GP4 board.SDA
board.GP5 board.SCL
board.GP6
board.GP7
board.GP8
board.GP9
board.USER_SW
board.VBUS_DETECT
 """



