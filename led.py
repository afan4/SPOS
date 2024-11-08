'''import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        GPIO.output(21, GPIO.low)
        GPIO.output(20, GPIO.low)
        print("LED Off")
        time.sleep(1)
except:
    GPIO.cleanup()'''
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
GPIO.cleanup()
GPIO.setup(21, GPIO.IN)

try:
    while True:
        if (GPIO.input(21)):
            print("No object")
        else: print("Object Detected")

except KeyboardInterrupt:
    GPIO.cleanup()

'''

