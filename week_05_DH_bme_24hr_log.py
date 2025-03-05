from bme280 import BME280
from datetime import datetime
import time

sensor = BME280 (address=0x76)

# Create a file to log data.
f = open('weather_log.csv', 'w')
f.write("timestamp, temperature, pressure")
f.flush()
counter = 0

while (counter < 241):
    current_time = datetime.now ()
    formatted_time = current_time.strftime ("%H:%M:%S")
    r = sensor.read ()
    line = '\n{},{:.4f},{:.4f}'.format(formatted_time,r['t'],r['p'])
    print (line)
    f.write (line)
    f.flush()
    counter += 1
    time.sleep (360)

print(f'Sampling done at {formatted_time}')
f.close ()
