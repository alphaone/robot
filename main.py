import time
from robot import *
from motor import *
from strategy import *

try:
  motor_right = Motor('R', 17, 18)
  motor_left = Motor('L', 22, 23)


  robot = Robot(motor_right=motor_right, motor_left=motor_left)
  strategy = Strategy(robot)
  strategy.run()

except KeyboardInterrupt:
  print("Robot died.")
  #GPIO.cleanup()