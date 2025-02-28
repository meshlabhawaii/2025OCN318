#imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #align pins

#configure pins
LED_PIN_1 = 18  #pin 18, white
LED_PIN_2 = 23  #pin 23, red
LED_PIN_3 = 24  #pin 24, blue
SWITCH_PIN = 17  #pin 17, switch
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #pin 17, switch

#set interval
interval = 0.2                                                                 

while True:
    if not GPIO.input(SWITCH_PIN):
        print('blinking lights')
        GPIO.output(LED_PIN_1, GPIO.HIGH)  # turn on white
        time.sleep(interval)
        GPIO.output(LED_PIN_1, GPIO.LOW)                                                                                                                                                                                                                                    
        time.sleep(interval)
        GPIO.output(LED_PIN_2, GPIO.HIGH)  #turn on red
        time.sleep(interval)
        GPIO.output(LED_PIN_2, GPIO.LOW)                                                                                                                                                                                                                                    
        time.sleep(interval)
        GPIO.output(LED_PIN_3, GPIO.HIGH)  #turn on blue
        time.sleep(interval)
        GPIO.output(LED_PIN_3, GPIO.LOW)                                                                                                                                                                                                                                    
        time.sleep(interval)
    else:
        print('no lights')
        GPIO.output(LED_PIN_1, GPIO.LOW)
        GPIO.output(LED_PIN_2, GPIO.LOW)
        GPIO.output(LED_PIN_3, GPIO.LOW)       
        time.sleep(interval*10)