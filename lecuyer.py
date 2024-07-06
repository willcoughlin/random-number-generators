class Lecuyer():
  def __init__(self, x0, x1):
    if len(x0) != 3:
      raise ValueError("Argument `x0` must be a list of 3 integers")
    if len(x1) != 3:
      raise ValueError("Argument `x1` must be a list of 3 integers")
    
    self.x0 = x0
    self.x1 = x1
    # self.i = 0
    self.i = 3

  def next(self):
    # if self.i >= 3:
    x0i = (1403580*self.x0[self.i-2] - 810728*self.x0[self.i-3]) % (2**32 - 209)
    x1i = (527612*self.x1[self.i-1] - 1370589*self.x1[self.i-3]) % (2**32 - 22853)

    self.x0.append(x0i)
    self.x1.append(x1i)

    y = (self.x0[self.i]-self.x1[self.i]) % (2**32 - 209)
    self.i += 1
    return y / (2**32 - 209)
  
gen = Lecuyer(x0=[1,2,3], x1=[4,5,6])

for _ in range(10):
  print(gen.next())