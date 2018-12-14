import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

i=0

while True:
    if not GPIO.input(23):
        if not GPIO.input(23):
            i=i+1
            n = i%5
            print(n)

            if n == 0:
                GPIO.output(4,GPIO.HIGH)
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(20,GPIO.LOW)
                GPIO.output(21,GPIO.LOW)
            if n == 1:
                GPIO.output(4,GPIO.LOW)
                GPIO.output(5,GPIO.HIGH)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(20,GPIO.LOW)
                GPIO.output(21,GPIO.LOW)

            if n == 2:
                GPIO.output(4,GPIO.LOW)
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.HIGH)
                GPIO.output(20,GPIO.LOW)
                GPIO.output(21,GPIO.LOW)
            if n == 3:
                GPIO.output(4,GPIO.LOW)
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(20,GPIO.HIGH)
                GPIO.output(21,GPIO.LOW)
            if n == 4:
                GPIO.output(4,GPIO.LOW)
                GPIO.output(5,GPIO.LOW)
                GPIO.output(6,GPIO.LOW)
                GPIO.output(20,GPIO.LOW)
                GPIO.output(21,GPIO.HIGH)

                
            while not GPIO.input(23):
                time.sleep(0.01)
        
        
    

