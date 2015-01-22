import time
from robot import *
from motor import *
from keyboard_strategy import *

try:
  motor_right = Motor('R', 22, 23)
  motor_left = Motor('L', 17, 18)


  robot = Robot(motor_right=motor_right, motor_left=motor_left)
  strategy = KeyboardStrategy(robot)
  strategy.run()

except KeyboardInterrupt:
  print("Robot died.")
  GPIO.cleanup()