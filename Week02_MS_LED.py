import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 24
GPIO.setup(LED_PIN, GPIO.OUT)

print("help")

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD.UP)
while True:
    if not GPIO.input(17):
        print("Ding")
    time.sleep(0.01)