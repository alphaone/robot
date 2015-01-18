##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)

#Motor 1 = Pins 17 and 18
#Motor 2 = Pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

fwd1 = GPIO.PWM(17, 50)
rev1 = GPIO.PWM(18, 50)
fwd2 = GPIO.PWM(22, 50)
rev2 = GPIO.PWM(23, 50)

fwd1.start(0)
fwd2.start(0)
rev1.start(0)
rev2.start(0)

speed = 90

#Now loop forever turning one direction for 5 seconds, then the other
try:
  while (True):
    #Sleep 1 second then turn 17 on
    
    rev1.ChangeDutyCycle(0)
    rev2.ChangeDutyCycle(0)
    time.sleep(1)

    fwd1.ChangeDutyCycle(speed)
    fwd2.ChangeDutyCycle(speed)
    time.sleep(3)

    fwd1.ChangeDutyCycle(0)
    fwd2.ChangeDutyCycle(0)
    time.sleep(1)

    rev1.ChangeDutyCycle(speed/2)
    rev2.ChangeDutyCycle(speed/2)
    time.sleep(3)

except KeyboardInterrupt:
    print("Fahrt vom User gestoppt")
    GPIO.cleanup()
