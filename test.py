import RPi.GPIO as GPIO
import time

stepPin = 22
dircPin = 17
enabPin = 23
num = 100

GPIO.setmode(GPIO.BCM)  # GPIOで指定
GPIO.setup(enabPin, GPIO.OUT)   # 2:Enableに定義
GPIO.setup(dircPin, GPIO.OUT)   # 3:Dir
GPIO.setup(stepPin, GPIO.OUT)   # 4:Step
print("setup was completed")

#GPIO.setup(17, GPIO.OUT)#17:MS1
#GPIO.setup(27, GPIO.OUT)#27:MS2
#GPIO.setup(22, GPIO.OUT)#22:MS3

def main():
    GPIO.output(enabPin, 1)
    print("enable setted 1")
    escapeR
    GPIO.cleanup()

#逆かもしれない
def escapeR():
    GPIO.output(dircPin, 0)
    for i in range(0,200):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)
    time.sleep(1)
def escapeL():
    GPIO.output(dircPin, 1)
    for i in range(0,200):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)
    time.sleep(1)

busy = True

try:
        main()
except KeyboardInterrupt:
        print('interrupted!')
        GPIO.cleanup()
