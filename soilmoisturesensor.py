import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2cbus = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2cbus, address=0x48)

ch0 = AnalogIn(ads, ADS.P0)

while True:
    voltage = ch0.voltage
    if voltage < 1.1:
        moisture = 0
    elif voltage > 5.0:
        moisture = 100
    else:
        moisture = (voltage - 1.1) / (5.0 - 1.1) * 100
    print(f"Soil Moisture: {moisture:.1f}%")
    print(f"Voltage from VH400: {voltage:.3f} V")
    time.sleep(6)
