import time
from robot import *
from strategy import *

try:
  robot = Robot()
  strategy = Strategy(robot)
  strategy.run()

except KeyboardInterrupt:
  print("Robot died.")
  #GPIO.cleanup()