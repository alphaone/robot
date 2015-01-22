from key_pressed_watcher import KeyPressedWatcher

class KeyboardStrategy(object):
  
  def __init__(self, robot):
    self.robot = robot

  def run(self):
    KeyPressedWatcher(onKeyPressed=self.onKeyPressed)

    while True:
      pass

  def onKeyPressed(self, key):
    if key == 'w':
      self.robot.faster()
    elif key == 's':
      self.robot.slower()
    elif key == 'a':
      self.robot.trim_left()
    elif key == 'd':
      self.robot.trim_right()
    elif key == ' ':
      self.robot.stop()

    
