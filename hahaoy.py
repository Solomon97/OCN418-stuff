import time
import RPi.GPIO as GPIO


button = 23
N = 6
counter = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [4,5,6,20,21]

for pin in pins:
    GPIO.setup(pin,GPIO.OUT)


def f(counter):
        
    for pin in pins:
        GPIO.output(pin,GPIO.LOW)
    for i in range(counter):
        GPIO.output(pins[i],GPIO.HIGH)
        print(pins[i])
    


while True:
    if not GPIO.input(button):
        print('{} hit'.format(counter))
        
        counter = (counter+1) % N
        i = list(range(counter))
        f(counter)
        
        while not GPIO.input(button):
            time.sleep(0.2)
