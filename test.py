#!/usr/bin/python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import sys
import cv2
import os

stepPin = 22
dircPin = 17
enabPin = 23

camLimit = 5

#GPIO.setup(17, GPIO.OUT)#17:MS1
#GPIO.setup(27, GPIO.OUT)#27:MS2
#GPIO.setup(22, GPIO.OUT)#22:MS3
GPIO.setmode(GPIO.BCM)  # GPIOで指定
GPIO.setup(enabPin, GPIO.OUT)   # 2:Enableに定義
GPIO.setup(dircPin, GPIO.OUT)   # 3:Dir
GPIO.setup(stepPin, GPIO.OUT)   # 4:Step

def main():
    print("escapeR")
    GPIO.output(dircPin, 1)
    for num in range(0,1000):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)
    time.sleep(1)


try:
        main()
except KeyboardInterrupt:
        print('interrupted!')
        GPIO.cleanup()

cv2.destroyAllWindows()