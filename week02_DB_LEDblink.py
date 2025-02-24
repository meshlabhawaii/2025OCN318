import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

interval = 0.75

LED_PIN = 18
LED_PIN_2 = 12
LED_PIN_3 = 16

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN_2, GPIO.HIGH)
    GPIO.output(LED_PIN_3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(LED_PIN_2, GPIO.LOW)
    GPIO.output(LED_PIN_3, GPIO.LOW)
    time.sleep(0.5)
    

