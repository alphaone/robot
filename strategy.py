import time
import random

class Strategy(object):
  
  def __init__(self, robot):
    super(Strategy, self).__init__()
    self.robot = robot

  def run(self):
    while True:
      self.drive_around()

      time.sleep(0.5)

  def drive_around(self):
    if not self.robot.something_in_way():
      self.robot.drive_forward()
    else:
      self.set_a_new_direction()
    
  def set_a_new_direction(self):
    direction = random.choice(["left", "right"])

    print "evade to %s" % direction

    while self.robot.something_in_way():
      if direction == "left":
        self.robot.drive_left()
      else:
        self.robot.drive_right()

      time.sleep(0.1)
