import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

pin = 4
interval = 0.1

dot = .2
dash = .6

text = 'sos-sos-sos-sos'

def s ():
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dot)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    
def o():
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)def o():
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(dash)
    GPIO.output(4, GPIO.LOW)
    time.sleep(interval)
    
for c in text:
    if 's' == c:
        print('s')
        s()
    if 'o' == c:
        print('o')
        o()
  
exit()

while True:
    print('s')
    s()
    print('o')
    o()
    print('s')
    s()
    print('...---...')
    GPIO.output(4, GPIO.LOW)
    time.sleep(2)

GPIO.cleanup(4)

while True:
    print('s')
    s()
    print('o')
    o()
    print('s')
    s()
    print('...---...')
    GPIO.output(4, GPIO.LOW)
    time.sleep(2)
