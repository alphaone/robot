from getch import Getch
import threading

class KeyPressedWatcher:
  def __init__(self, onKeyPressed):
    print('Create input watcher %s ' % threading.current_thread().name)
    self.onKeyPressed = onKeyPressed
    self.start_thread()

  def start_thread(self):
    thread = threading.Thread(target=self.wait_for_input)
    thread.daemon = True
    thread.start()

  def wait_for_input(self):
    keyReader = Getch()
    while True:
      self.onKeyPressed(keyReader())