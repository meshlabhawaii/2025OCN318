from bme280 import BME280
import time

sensor = BME280(address=0x76)

f = open('truth.csv', 'a')

while True:
    ts = time.time()
    r = sensor.read()
    line='{},{:.4f},{:.4f},{:.4f}\n'.format(ts, r['t'], r['p'], r['rh'])
    print(line)
    f.write(line)
    f.flush()
    time.sleep(1)
    
f.close()