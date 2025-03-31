#Script to read the moisture/temp/humidity from the plant and the room
#packages to plot and handle dataframe
import pandas as pd
import matplotlib as plt
#packages to measure environtmental data
from bme280 import BME280
#packages to handle the 
from datetime import datetime
import time
#convert the voltage from the soil sensor from analog to digital using another script
import sampleanalogtodigital

#set up the gpio ports for sensors
sensorBME = BME280(address=0x76)
#sensorsoil = VH400()

# Create a file to log data.
f = open('plant_log.csv', 'w')
f.write("timestamp, temperature, humidity")
f.flush()

#Function to plot the data 
def plantplot(filelog, param, ax=None):
    if ax is None:
        ax = plt.gca()
    ax.set_xlabel(f"Time")
    ax.set_ylabel(f"{param}")
    return ax.plot(filelog['timestamp'], filelog[param])

#loop to write the data at specified intervals
while True:
    #adds the timestamp
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    rBME = sensorBME.read()
    #rSoil = sensorsoil.read()
    #write the data to a csv
    line = '\n{},{:.4f},{:.4f}'.format(formatted_time,rBME['t']""", rSoil""")
    print(line)
    f.write(line)
    f.flush()
    #time interval between reads
    time.sleep(360)
    
#create plot of humidity vs time and humidity vs time
fig, axs = plt.subplots(1,2)
plt.suptitle("Plant Log")
axs[0] = plantplot(f, 'temperature', axs=[0])
axs[1] = plantplot(f, 'humidity', axs=[1])