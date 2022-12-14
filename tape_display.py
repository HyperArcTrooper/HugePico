import board
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7789 import ST7789

class TapeDisplay():
    # Release any resources currently in use for the displays
    displayio.release_displays()

    tft_cs = board.GP9
    tft_dc = board.GP8
    spi_mosi = board.GP11
    spi_clk = board.GP10
    spi = busio.SPI(spi_clk, spi_mosi)
    backlight = board.GP13

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs)

    display = ST7789(
        display_bus, rotation=90, width=320, height=240, backlight_pin=backlight
    )

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(320, 240, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x00FF00  # Bright Green

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)


    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(280, 200, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0xAA0088  # Purple
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
    splash.append(inner_sprite)

    # Draw a label
    text_group = displayio.Group(scale=3, x=57, y=120)
    text = "Hello World!"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

    # while True:
    #     pass
     
