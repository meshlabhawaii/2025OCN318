import time
import csv
import board
import busio
import sys
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

# Add BME280 module path and import sensor
sys.path.append("/home/daelinb/Desktop")
from bme280 import BME280

# Initialize I2C bus
i2cbus = busio.I2C(board.SCL, board.SDA)

# Set up ADS1115 (soil moisture sensor)
ads = ADS.ADS1115(i2cbus, address=0x48)
ch0 = AnalogIn(ads, ADS.P0)

# Set up BME280 (temperature and pressure sensor)
sensor = BME280(address=0x76)

#Pump
PUMP_PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)
GPIO.output(PUMP_PIN, GPIO.LOW)

# Define CSV file path
csv_file = "/home/daelinb/Desktop/environmental_readings.csv"

# Define CSV headers
csv_headers = ["Timestamp", "Soil Moisture (%)", "Voltage (V)", "Temperature (C)", "Pressure (hPa)"]

# Create file and write headers if it doesn't exist
try: 
    with open(csv_file, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
except FileExistsError:
    pass

# Run loop for 24 hours worth of readings at 20-minute intervals (72 iterations)
try:
    while True:
        # Get voltage from VH400
        voltage = ch0.voltage
    
        # Calculate soil moisture percentage
        if voltage < 1.1:
            moisture = 0
        elif voltage > 3.0:
            moisture = 100
        else:
            moisture = (voltage - 1.1) / (3.0 - 1.1) * 100
        
        if moisture < 15:
            GPIO.output(PUMP_PIN, GPIO.HIGH)
            time.sleep(20)
            GPIO.output(PUMP_PIN, GPIO.LOW)

        # Get temperature and pressure from BME280
        reading = sensor.read()
        temperature = reading['t']
        pressure = reading['p']

        # Create timestamp
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # Write to CSV
        with open(csv_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, round(moisture, 1), round(voltage, 3), temperature, pressure])

        # Print to console
        print(f"{timestamp} | Moisture: {moisture:.1f}% | Voltage: {voltage:.3f} V | Temp: {temperature} C | Pressure: {pressure} hPa")

        # Wait 20 min
        time.sleep(60 * 20)
    
except KeyboardInterrupt:
    print("Program interrupted. Cleaning up...")
finally:
    GPIO.output(PUMP_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up. Exiting.")
