import time
from robot import *
from keyboard_strategy import *

try:

  robot = Robot()
  strategy = KeyboardStrategy(robot)
  strategy.run()

except KeyboardInterrupt:
  del robot
  print("Exiting ...")
  #GPIO.cleanup()