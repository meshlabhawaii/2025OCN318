#imports
import sys
sys.path.append ('/home/jnishida/Desktop/python/node/drivers')

from bme280 import BME280
import time

#configure sensor
bme = BME280(bus=1, address=0x76)

f = open('week04_JN_BME_output.csv','w') # open file to write sensor values
f.write('Timestamp,Temperature (C), Pressure (hPA), Humidity (%)\n')
end_time = time.time() + (24 * 60 * 60) # set the time limit (24 hours = 24 x 60 minutes)

# loop for 24 hours, taking readings every 5 minutes
while time.time() < end_time:
    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) # get timestamp
    r = bme.read() # read from sensor
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(ts,r['t'],r['p'],r['rh']) # assign values to string
    print(line)  # print values
    f.write(line) # write light values to file
    f.flush()
    time.sleep(300) # sleep for 5 minutes (300 seconds)
    
f.close()
