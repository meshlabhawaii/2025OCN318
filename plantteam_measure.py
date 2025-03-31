#Script to read the moisture/temp/humidity from the plant and the room
#packages to plot and handle dataframe
import pandas as pd
import matplotlib as plt
#packages to measure environtmental data
from bme280 import BME280
#packages to handle the 
from datetime import datetime
import time

#set up the gpio ports for sensors
sensorBME = BME280(address=0x76)
#sensorsoil = VH400()

# Create a file to log data.
f = open('weather_log.csv', 'w')
f.write("timestamp, temperature, pressure")
f.flush()
counter = 0

#convert the voltage from the soil sensor from analog to digital


#loop to write the data at specified intervals
while True:
    #adds the timestamp
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    r = sensorBME.read ()
    #write the data to a csv
    line = '\n{},{:.4f},{:.4f}'.format(formatted_time,r['t'],r['p'])
    print(line)
    f.write(line)
    f.flush()
    counter += 1
    #time interval between reads
    time.sleep(360)
    
    
#Plot the data to a dataframe/csv 
plt.plot(f['timestamp'], f['temperature'])