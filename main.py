import adafruit_dotstar # Our LED library
import digitalio
import board
import math
import time

print("LumiDrive v10") 

# Setting up the product's blue stat LED to blink
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# These two variables should be adjusted to reflect the number of LEDs you have
# and how bright you want them.
num_pixels = 60
brightness = 0.25

# This creates the instance of the DoTStar library. 
pixels = adafruit_dotstar.DotStar(board.SCK, board.MOSI, 
    num_pixels, brightness=brightness, auto_write=False)

# Some standard colors. 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)
GREEN = (0, 255, 0)
TEAL = (0, 255, 120)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 20)
WHITE = (255, 255, 255)

# A list of the ten colors. Use this if you want to cycle through the colors. 
colorList = [RED, YELLOW, ORANGE, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA,
                    WHITE]

# The travel function takes a color and the time between updating the color. It
# will start at LED one on the strand and fill it with the give color until it
# reaches the maximum number of pixels that are defined as "num_pixels".
def travel(color, wait):
    num_pixels = len(pixels)
    for pos in range(num_pixels):
        pixels[pos] = color 
        pixels.show() 
        time.sleep(wait)

# The travel_back function like the travel function takes a color and the time between 
# updating the color. However it unlike the travel function, it will start at
# the last LED and works its way to LED. Fill the LED with the given color.
def travel_back(color, wait):
    num_pixels = len(pixels)
    for pos in reversed(range(num_pixels)):
        pixels[pos] = color 
        pixels.show() 
        time.sleep(wait)

# This function may give you an idea of other functions to create. Here we're
# starting with green LEDs and then slowing filling the red color until we have
# a yellow color.  
def green_yellow_wheel(wait):
    for redColor in range(255):
        color = (redColor, 150, 0)
        pixels.fill(color)
        pixels.show()
        time.sleep(wait)

# You can use this function to get a custom color value. 
# value much in the form of a tuple, like the colors above. 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# This function takes a color and a dely and fills the entire strand with that color. 
# The delay is given in the case you use multiple color fills in a row.  
def color_fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)

# Fills the strand with two alternating colors and cycles through the 10 colors 
def slice_alternating(wait):

    num_pixels = len(pixels)

    pixels[::2] = [RED] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [ORANGE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [YELLOW] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [GREEN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [TEAL] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [CYAN] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [BLUE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [PURPLE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[::2] = [MAGENTA] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)
    pixels[1::2] = [WHITE] * (num_pixels // 2)
    pixels.show()
    time.sleep(wait)


# This function divides the given number of pixels and fills them as evenly as
# possible with a rainbow pattern (RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE) 
# which repeats every 6 LEDs.
def slice_rainbow(wait):

    num_pixels = len(pixels)

    pixels[::6] = [RED] * math.ceil(num_pixels / 6)
    pixels.show()
    time.sleep(wait)
    pixels[1::6] = [ORANGE] * math.ceil((num_pixels - 1) / 6)
    pixels.show()
    time.sleep(wait)
    pixels[2::6] = [YELLOW] * math.ceil((num_pixels -2) / 6)
    pixels.show()
    time.sleep(wait)
    pixels[3::6] = [GREEN] * math.ceil((num_pixels-3) / 6)
    pixels.show()
    time.sleep(wait)
    pixels[4::6] = [BLUE] * math.ceil((num_pixels-4) / 6)
    pixels.show()
    time.sleep(wait)
    pixels[5::6] = [PURPLE] * math.ceil((num_pixels-5) / 6)
    pixels.show()
    time.sleep(wait)

# This function makes a strand of LEDs look like a rainbow flag that travels
# along the length of the strand. It is not infinitely contniuous and will stop
# after any single LED has cycled through every color.  
def rainbow_cycle(wait):
    num_pixels = len(pixels)
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

print("Clearing LEDs.")
color_fill(BLACK,0) 

#Ah trusty ol' blink. 
while True: 
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)
