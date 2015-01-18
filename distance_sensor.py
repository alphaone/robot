from random import randint

class DistanceSensor(object):

  def __init__(self):
    super(DistanceSensor, self).__init__()
    
  def distance(self):
    return randint(0,9)

