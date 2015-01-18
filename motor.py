class Motor(object):

  def __init__(self, name):
    super(Motor, self).__init__()
    self.name = name
    
  def stop(self):
    print "Motor %s: stop!" % self.name

  def forward(self):
    print "Motor %s: forward!" % self.name

