import busio
from adafruit_progressbar.verticalprogressbar import VerticalProgressBar
from adafruit_progressbar.progressbar import HorizontalProgressBar
from adafruit_st7789 import ST7789
from adafruit_display_text import label
import terminalio
import displayio
from adafruit_seesaw import seesaw, rotaryio
from adafruit_neokey.neokey1x4 import NeoKey1x4
import storage
import sdcardio
import os
import audiomixer
import audiomp3
import audiobusio
import board
import audiocore
import math
import array
import time
import supervisor
supervisor.disable_autoreload()  # type: ignore

# type: ignore
# from tape_display import TapeDisplay
# from dac import audiodac


num_voices = 1

audio = audiobusio.I2SOut(board.GP2, board.GP3, board.GP1)  # type: ignore

tone_volume = .1  # Increase this to increase the volume of the tone.
frequency = 550  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("h", [0] * length)
for i in range(length):
    sine_wave[i] = int((math.sin(math.pi * 2 * i / length))
                       * tone_volume * (2 ** 15 - 1))
sine_wave_sample = audiocore.RawSample(sine_wave)

i = 5
while i > 0:
    audio.play(sine_wave_sample, loop=True)
    time.sleep(.2)
    audio.stop()
    time.sleep(.2)
    i -= 1

time.sleep(1.0)


mixer = audiomixer.Mixer(voice_count=num_voices,
                         sample_rate=32000, channel_count=2)
audio.play(mixer)  # attach mixer to audio playback

print("audio is now playing")

# set some initial levels
mixer.voice[0].level = .1


data = open("Scarlet Fire (Sting).wav", "rb")
wav0 = audiocore.WaveFile(data) # type: ignore
mixer.voice[0].play(wav0, loop=False)

# audio.play(mp3)
# while True:
#     pass
time.sleep(10)

print("Done playing!")
