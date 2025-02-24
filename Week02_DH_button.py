import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


LED_PINS = [24, 18, 25]
i = 1
while True:
    if not GPIO.input(12):
        print(f'DING {i}')
        GPIO.output(LED_PINS[(i%3-1)], GPIO.HIGH)
        i+=1
    time.sleep(0.1)
    GPIO.output(LED_PINS[0], GPIO.LOW)
    GPIO.output(LED_PINS[1], GPIO.LOW)
    GPIO.output(LED_PINS[2], GPIO.LOW)

