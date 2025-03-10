import time # used for runtime
from datetime import datetime # used to record clock time
import csv
import sys
sys.path.append('/home/tbeal/Downloads/node/drivers') # to import BME280



# BME280 configuration
from bme280 import BME280

sensor = BME280(address=0x76)



# setting up runtime
total_runtime = 60 * 60 * 24 # total runtime (1 day) in seconds 
interval = 15 * 60 # 15 minutes in seconds
start_time = time.time()


# CSV file setup
with open('BME280_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    if csvfile.tell() == 0: # checks if file is empty
        writer.writerow(["Time", "Temperature (°C)", "Pressure (kPa)"])


while True:
    # current time
    current_time = time.time()
    
    # elapsed time
    elapsed_time = current_time - start_time
    
    # checks if 24 hrs have passed
    if elapsed_time >= total_runtime:
        print('All done! :D')
        break
    
    # clock setup
    now = datetime.now() # current date & time
    clock = now.strftime("%H:%M:%S") # used to print time data is recorded
    
    
    
    # BME280 reading
    reading = sensor.read() # prints as t = [temperature value], p = [pressure value], h = [humidity value]; note: this sensor does not read humidity
    temperature = reading['t']
    pressure = reading['p']
    
    

    # output
    print("Time: ", clock)
    print(f'Temperature: {temperature} °C | Pressure: {pressure} kPa')
    print("")



    # append data to CSV file
    with open('BME280_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([clock, temperature, pressure])



    # repeats code every 15 minutes
    time.sleep(interval)
    
