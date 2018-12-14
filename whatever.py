import time 
import RPi.GPIO as GPIO
import random
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)


pin=1

while True:
    for i in range (100):
        interval= random.randint(1,100)
        GPIO.output(4,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.LOW)
        time.sleep(interval)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(6,GPIO.LOW)
        time.sleep(interval)
        GPIO.output(4,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(interval)
    
    





GPIO.cleanup(4)
GPIO.cleanup(5)
GPIO.cleanup(6)
