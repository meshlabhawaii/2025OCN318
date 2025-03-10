import sys
sys.path.append ('/home/sierraal/Documents')

from tcs34725 import TCS34725
from datetime import datetime
import time

sensor = TCS34725()
sensor.gain(16)
sensor.integration_time(101)

print(sensor.read())

with open('color_data.csv', 'a') as f:
    while True:
        ts = time.time()
        r=sensor.read()
        line = '{:.4f},{:.4f},{:.4f}\n'.format(ts, r['r'],r['g'],r['b'])
        print(line.strip())
        f.write(line)
        f.flush()
        time.sleep(1)
        