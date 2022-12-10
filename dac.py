import time
import array
import math
import audiocore
import board
import audiobusio


class audiodac():
    audio = audiobusio.I2SOut(board.GP10, board.GP11, board.GP9) # type: ignore

    tone_volume = 0.5  # Increase this to increase the volume of the tone.
    frequency = 440  # Set this to the Hz of the tone you want to generate.
    length = 8000 // frequency
    sine_wave = array.array("h", [0] * length)
    for i in range(length):
        sine_wave[i] = int((math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))
    sine_wave_sample = audiocore.RawSample(sine_wave)

    while True:
        audio.play(sine_wave_sample, loop=True)
        time.sleep(1)
        audio.stop()
        time.sleep(1)