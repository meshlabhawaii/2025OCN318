import time
import board
import neopixel
import sys
sys.path.append ('/home/pi/node/drivers')
from bme280 import BME280
from datetime import datetime 

# NeoPixel configuration
LED_COUNT = 8
LED_PIN = board.D18
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness = 0.5, auto_write = False)
    
# BME280 Sensor Setup
sensor = BME280 (address=0x76)

# Temperature Range
TEMP_MIN = 19
TEMP_MAX = 25

# Function to map temp to color.
def temperature_to_color (temp):
    
    # Ensure temp is within range.
    temp = max(TEMP_MIN, min (TEMP_MAX, temp))
    
    # Normalize temperature between 0 and 1. 
    normalized = (temp - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)
    
    # Interpolate colors (Blue to Red)
    red = int(normalized * 255)
    blue = int((1 - normalized) * 255)
    green = 0
    
    return (red, green, blue)

# Main loop.

while True:
    # Read temp.
    r = sensor.read ()
    temp = r['t']
    print(f"Temperature: {temp:.2f} deg C")
    
    # Get color based on temp.
    color = temperature_to_color(temp)
    print(f"LED Color: {color}")
    
    # Apply color to all LEDs
    pixels.fill ((0,0,225))
    pixels.show ()
    time.sleep (1)

