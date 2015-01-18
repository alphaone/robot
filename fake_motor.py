class FakeMotor:

  def __init__(self, name, pin1, pin2):
    #super(FakeMotor, self).__init__()
    self.name = name
    
  def stop(self):
    print "Motor %s: stop!" % self.name

  def forward(self):
    print "Motor %s: forward!" % self.name

