from distance_sensor import *

class FakeDistanceSensor(DistanceSensor):

  def __init__(self):
    super(FakeDistanceSensor, self).__init__()
    self.current = 0
    
  def distance(self):
    distance_list = [10,9,8,7,6,5,4,3,2,1,5,6]
    self.current += 1
    self.current = self.current % len(distance_list)
    return distance_list[self.current]