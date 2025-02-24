import sys
sys.path.append ('/home/pi/node/drivers')
from bme280 import BME280
from datetime import datetime
import time

sensor = BME280 (address=0x76)

f = open('weather.csv', 'a')

while True:
    current_time = datetime.now ()
    formatted_time = current_time.strftime ("%H:%M:%S")
    r = sensor.read ()
    line = '{},{:.4f},{:.4f},{:.4f}'.format(formatted_time,r['t'],r['p'],r['rh'])
    print (line)
    f.write (line)
    f.flush()
    time.sleep (1)
    
f.close ()
