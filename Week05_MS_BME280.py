import sys
sys.path.append('/home/micahsor/Desktop/fishie/drivers')
from bme280 import BME280

sensor = BME280(address=0x76)

r = sensor.read()

print(r)
print('temperature={}'.format(r['t']))
print('pressure={}'.format(r['p']))
print('relative humidity={}'.format(r['rh']))




