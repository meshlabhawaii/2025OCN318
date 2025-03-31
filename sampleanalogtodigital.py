import time, busio, board
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
chan = AnalogIn(ads, ADS1115.P0)

while True:
    voltage = chan.voltage
    print(f"Voltage from VH400: {voltage:.3f} V")
    if voltage < 1.1:
        moisture = 0
    elif voltage > 3.0:
        moisture = 100
    else:
        moisture = (voltage - 1.1) / (3.0 - 1.1) * 100
    
    print(f"Soil Moisture: {moisture:.1f}%")
    time.sleep(60)