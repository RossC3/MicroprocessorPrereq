#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)

while True:
    #S ...
    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(1);

    #O ---

    GPIO.output(4,True);
    time.sleep(1)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1)
    GPIO.output(4,False);

    time.sleep(1);
    #S ...
    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(1/3);

    GPIO.output(4,True);
    time.sleep(1/3)
    GPIO.output(4,False);

    time.sleep(7);

