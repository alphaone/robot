class Getch:
  def __init__(self):
    import tty, sys, termios  # import termios now or else you'll get the Unix version on the Mac

  def __call__(self):
    import sys, tty, termios, fcntl

    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    try:
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    return ch

