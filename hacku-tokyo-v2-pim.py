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

GPIO.setmode(GPIO.BCM)  # GPIOで指定
GPIO.setup(enabPin, GPIO.OUT)   # 2:Enableに定義
GPIO.setup(dircPin, GPIO.OUT)   # 3:Dir
GPIO.setup(stepPin, GPIO.OUT)   # 4:Step

#GPIO.setup(17, GPIO.OUT)#17:MS1
#GPIO.setup(27, GPIO.OUT)#27:MS2
#GPIO.setup(22, GPIO.OUT)#22:MS3

def main():
    GPIO.output(enabPin, 0)
    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        mos = mosaic(gray)
        count = dump(gray, keep)

        print('{0} {1}'.format(count,busy))
        if busy and count==0:
            busy = False

        if busy == False and count > 5:
            busy = True
            kora()

        cv2.imshow('frame',frame)
        cv2.imshow('mos',mos)

        if cv2.waitKey(1) != -1:
            break
    
    GPIO.cleanup()

#逆かもしれない
def escapeR():
    GPIO.output(dircPin, 0)
    for num in range(0,200):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)
    time.sleep(1)
def escapeL():
    GPIO.output(dircPin, 1)
    for num in range(0,200):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)
    time.sleep(1)

def mosaic(src):
    dst = cv2.resize(src, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(dst, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def difference(a, b):
    if(a < b):
        return b - a
    return a - b

def kora():
    os.system('mpg321 -q /home/pi/camera/kora.mp3&')

def dump(src, keep):
    os.system('clear')
    RightCount = 0
    LeftCount = 0
    for x in range(0, 32):
        str = ''
        for y in range(0, 24):
            target = src[y*10][x*10]    
            diff = difference(keep[y][x],target)
            if diff > 50:
                str += '{:02} '.format(diff) 
                if(y >= 12):
                     RightCount += 1
                else:
                     LeftCount += 1
            else:
                str += '-- '
            keep[y][x] = target
        print(str)
    count=[RightCount,LeftCount]
    return count
# 仕様メモcount=[RightCount,LeftCount]

cap = cv2.VideoCapture(0)

cap.set(3,320) # WIDTH
cap.set(4,240) # HEIGHT
cap.set(5,30) # FPS

keep = [[0] * 32 for i in range(24)]

busy = True

try:
        main()
except KeyboardInterrupt:
        print('interrupted!')
        GPIO.cleanup()

cap.release()
cv2.destroyAllWindows()