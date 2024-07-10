class Tausworthe:
  def __init__(self, r, q, l, seed):
    self.r = r
    self.q = q
    self.l = l

    self.trim_mask = int('1'*2*l, 2) # Int bitmask to cap state int at 2l bits.
    self.mask = int('1'*self.l, 2)  # Int bit mask to extract l bits at a time from current state
    self.state = seed #^ self.mask   # Use mask + seed to initialize state. Stores current bits stored as an integer.

  def __increment_bits(self):
    # Append l new bits to end of current state integer
    for _ in range(self.l):
      # b1 = (self.state >> (self.r-1)) & 1  # bit i-r
      # b2 = (self.state >> (self.q-1)) & 1  # bit i-q
      b1 = 1 if self.state & (1 << self.r-1) else 0
      b2 = 1 if self.state & (1 << self.q-1) else 0
      new_bit = b1 ^ b2
      self.state = (self.state << 1) | new_bit  # shift and put new bit in the LSB 
    self.state &= self.trim_mask

  def next(self):
    self.__increment_bits()
    numerator = self.state & self.mask
    return numerator / 2**self.l

if __name__ == '__main__':
  # Uncomment for simple run
  # gen = Tausworthe(r=3, q=5, l=4, seed=31)
  # for _ in range(20):
  #   print(gen.next())


  # Uncomment for large timed run
  gen = Tausworthe(r=8, q=15, l=32, seed=0xdeadbeef)
  def time_generator(gen_func, N, M):
    import timeit
    trials = timeit.repeat(stmt='gen_func()', number=N, repeat=M, globals={'gen_func': gen_func})
    min_trial = min(trials)
    return min_trial * 1000, min_trial * 1000 / N
  N = 10000
  M = 5
  print(time_generator(gen.next, N, M))

