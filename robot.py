from fake_distance_sensor import *
from fake_motor import *

class Robot(object):
  
  def __init__(self, distance_sensor=FakeDistanceSensor(), motor_right=FakeMotor('right', 0, 0), motor_left=FakeMotor('left', 0, 0)):
    self.distance_sensor = distance_sensor
    self.motor_right = motor_right
    self.motor_left = motor_left

    self.speed = 0
    self.trim = 0

  def __del__():
    del motor_left
    del motor_right
    del distance_sensor
    print "Robot died."

  def something_in_way(self):
    return self.distance_sensor.distance() < 5

  def adjust_motors(self):
    print "speed %s, trim %s", (self.speed, self.trim)
    self.motor_right.forward(self._right_speed())
    self.motor_left.forward(self._left_speed())

  def stop(self):
    self.speed = 0
    self.adjust_motors()

  def drive_forward(self):
    self.trim = 0
    self.speed = 50
    self.adjust_motors()

  def drive_right(self):
    self.trim = 20
    self.speed = 50
    self.adjust_motors()
  
  def drive_left(self):
    self.trim = -20
    self.speed = 50
    self.adjust_motors()

  def faster(self):
    self.speed += 5
    if self.speed >= 100:
      self.speed = 100
    self.adjust_motors()

  def slower(self):
    self.speed -= 5
    if self.speed <= -100:
      self.speed = -100
    self.adjust_motors()

  def trim_left(self):
    self.trim -= 5
    self.adjust_motors()

  def trim_right(self):
    self.trim += 5
    self.adjust_motors()

  def _right_speed(self):
    return self.speed + self.trim

  def _left_speed(self):
    return self.speed - self.trim
