from fake_distance_sensor import *
from fake_motor import *

class Robot(object):
  
  def __init__(self, distance_sensor=FakeDistanceSensor(), motor_right=FakeMotor('right', 0, 0), motor_left=FakeMotor('left', 0, 0)):
    super(Robot, self).__init__()

    self.distance_sensor = distance_sensor
    self.motor_right = motor_right
    self.motor_left = motor_left

  def something_in_way(self):
    return self.distance_sensor.distance() < 5

  def stop(self):
    self.motor_right.stop()
    self.motor_left.stop()

  def drive_forward(self):
    self.motor_right.forward()
    self.motor_left.forward()

  def drive_right(self):
    self.motor_right.stop()
    self.motor_left.forward()
  
  def drive_left(self):
    self.motor_right.forward()
    self.motor_left.stop()
