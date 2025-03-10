import sys, time, csv, neopixel, board
sys.path.append("/home/daelinb/Desktop")
from bme280 import BME280

sensor = BME280(address=0x76)

csv_file = "/home/daelinb/Desktop/bme280readings.csv"
TEMP_LOW = 18.0
TEMP_HIGH = 26.0
LED_COUNT = 8
LED_PIN = board.D18
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=0.2, auto_write=False)

csv_headers = ["Timestamp", "Temperature (C)", "Pressure (hPa)"]
try: 
    with open(csv_file, "x", newline ="") as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
except FileExistsError:
    pass
    
def temperature_to_color(temp):
    temp = max(min(temp, TEMP_HIGH), TEMP_LOW)
    ratio = (temp - TEMP_LOW) / (TEMP_HIGH - TEMP_LOW)
    red = int(255 * ratio)
    green = int(255 * (1-ratio))
    blue = int(255 * (1-ratio) if ratio < 0.5 else 0)
    return (red, green, blue)

def update_neopixels(temp):
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(0.1)
    active_leds = int(((temp - TEMP_LOW) / (TEMP_HIGH - TEMP_LOW)) * LED_COUNT)
    active_leds = max(1, min(active_leds, LED_COUNT))
    color = temperature_to_color(temp)
    for i in range(LED_COUNT):
        pixels[i] = color if i < active_leds else (0, 0, 0)
    print(f"Updating NeoPixels with {active_leds} LEDs, color: {color}")
    pixels.show()

for a in range(240):
    reading = sensor.read()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    temperature = reading['t']
    pressure = reading['p']

    print(f"Debug: {a}")

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temperature, pressure])
        if isinstance(temperature, (int, float)):
            print(f"Read temperature: {temperature}")
            update_neopixels(temperature)
        print(f"{timestamp} | Temp: {temperature} C | Pressure: {pressure} hPa")
    
        time.sleep(60*6)

