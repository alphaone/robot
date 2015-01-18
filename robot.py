from fake_distance_sensor import *
from motor import *

class Robot(object):
  
  def __init__(self, distance_sensor=FakeDistanceSensor()):
    super(Robot, self).__init__()

    self.distance_sensor = distance_sensor
    self.motor_right = Motor('right')
    self.motor_left = Motor('left')

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
