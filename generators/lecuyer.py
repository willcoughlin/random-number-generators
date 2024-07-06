class Lecuyer():
  def __init__(self, seed):
    # Create 6 ints using seed
    x0 = [seed << n for n in range(3)]
    x1 = [seed << n for n in range(3, 6)]
    
    self.x0 = x0
    self.x1 = x1
    self.i = 3

  def next(self):
    x0i = (1403580*self.x0[self.i-2] - 810728*self.x0[self.i-3]) % (2**32 - 209)
    x1i = (527612*self.x1[self.i-1] - 1370589*self.x1[self.i-3]) % (2**32 - 22853)

    self.x0.append(x0i)
    self.x1.append(x1i)

    y = (self.x0[self.i]-self.x1[self.i]) % (2**32 - 209)
    self.i += 1
    return y / (2**32 - 209)
  
if __name__ == '__main__':
  gen = Lecuyer(seed=3245)
  for _ in range(10):
    print(gen.next())