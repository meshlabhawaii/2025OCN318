import sys
import csv

desktop_path = "/home/daelinb/Desktop"
sys.path.append(desktop_path)

from tcs34725 import TCS34725
import time

sensor = TCS34725()
sensor.gain(16)
sensor.integration_time(101)

csv_file = "/home/daelinb/Desktop/truth.csv"

f = open(csv_file, 'a')

while True:
    ts = time.time()
    r = sensor.read ()
    line = '{},{:.4f},{:.4f},{:.4f}\n'.format(ts, r['r'], r['g'], r['b'])
    print(line)
    f.write(line)
    f.flush()
    time.sleep(1)

f.close()