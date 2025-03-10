from bme280 import BME280
import time
from datetime import datetime
#import board
#import neopixel
#pixels = neopixel.NeoPixel(board.D5, 30)    # Feather wiring!
# pixels = neopixel.NeoPixel(board.D18, 30) # Raspberry Pi wiring!

sensor = BME280(address=0x76)

f = open('tempdata.csv','a')

while True:
    current_time = datetime.now()
    ts = current_time.strftime('%H:%M:%S')
    r = sensor.read()
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(ts,r['t'],r['p'],r['rh'])
    print(line)
    f.write(line)
    f.flush()
    time.sleep(600)

f.close()