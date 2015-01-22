class FakeMotor:

  def __init__(self, name, pin1, pin2):
    #super(FakeMotor, self).__init__()
    self.name = name
    self.speed = 0

  def __del__(self):
    print "Motor %s died." % self.name
    
  def stop(self):
    self.speed = 0
    print "Motor %s: stop!" % self.name

  def forward(self, speed):
    self.speed = speed
    if self.speed >= 0:
      print "Motor %s: forward with speed %s!" % (self.name, self.speed)
    else:
      print "Motor %s: reverse with speed %s!" % (self.name, -self.speed)

