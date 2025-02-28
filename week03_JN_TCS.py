#imports
import sys
sys.path.append ('/home/jnishida/Desktop/python/node/drivers')

from tcs34725 import TCS34725
from datetime import datetime
import time

#configure sensor
sensor = TCS34725()
sensor.gain(16)
sensor.integration_time(101)

f = open('output_TCS.csv','a') # open file to append sensor data

while True:
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # get timestamp
    r = sensor.read() # read from light sensor
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(ts,r['r'],r['g'],r['b']) # assign light values to string
    print(line) # print light values
    f.write(line) # write light values to file
    f.flush()
    time.sleep(1)
   
f.close()