import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Motor(object):

  def __init__(self, name, fwd_pin, rev_pin):
    self.name = name
    GPIO.setup(fwd_pin, GPIO.OUT)
    GPIO.setup(rev_pin, GPIO.OUT)

    self.fwd = GPIO.PWM(fwd_pin, 50)
    self.rev = GPIO.PWM(rev_pin, 50)

    self.fwd.start(0)
    self.fwd.start(0)

    self.speed = 75

    
  def stop(self):
    self.fwd.ChangeDutyCycle(0)
    self.rev.ChangeDutyCycle(0)

  def forward(self):
    self.fwd.ChangeDutyCycle(self.speed)
    self.rev.ChangeDutyCycle(0)
    

