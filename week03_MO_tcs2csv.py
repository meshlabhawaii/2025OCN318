import sys

sys.path.append ('/home/pi/node/drivers')

from tcs34725 import TCS34725
from datetime import datetime
import time

sensor = TCS34725 ()
sensor.gain (16)
sensor.integration_time(101)

f = open ('truth.csv','a')

while True:
    current_time = datetime.now ()
    formatted_time = current_time.strftime ("%H:%M:%S")
    r = sensor.read ()
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(formatted_time,r['r'],r['g'],r['b'])
    print (line)
    f.write (line)
    f.flush()
    time.sleep (1)

f.close()

# Print to python, creates file, is not writing to file though. 

