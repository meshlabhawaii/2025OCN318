import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 18
LED_PIN2 = 24
LED_PIN3 = 16

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN2, GPIO.HIGH)
    GPIO.output(LED_PIN3, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(LED_PIN2, GPIO.LOW)
    GPIO.output(LED_PIN3, GPIO.LOW)
    time.sleep(0.5)
    