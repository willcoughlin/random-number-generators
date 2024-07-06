# This generator is adapted from the Mersenne Twister paper: http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/ARTICLES/mt.pdf

class MersenneTwister:
  # Magic numbers
  N = 624
  M = 397
  MATRIX_A = 0x9908b0df
  UPPER_MASK = 0x80000000
  LOWER_MASK = 0x7fffffff
  
  TEMPERING_MASK_B = 0x9d2c5680
  TEMPERING_MASK_C = 0xefc60000
  TEMPERING_SHIFT_U = lambda _, y: y >> 11
  TEMPERING_SHIFT_S = lambda _, y: y << 7
  TEMPERING_SHIFT_T = lambda _, y: y << 15
  TEMPERING_SHIFT_L = lambda _, y: y >> 18

  def __init__(self, seed):
    self.mt = [0]*self.N
    self.mt[0] = seed & 0xffffffff
    for i in range(1, self.N):
      self.mt[i] = (69069 * self.mt[i-1]) & 0xffffffff
    self.mti = self.N

  def next(self):
    y = 0
    mag01 = [0, self.MATRIX_A]
    
    if self.mti >= self.N:
      for kk in range(self.N-1):
        y = (self.mt[kk] & self.UPPER_MASK) | (self.mt[kk+1] & self.LOWER_MASK)

        if kk < self.N - self.M:
          self.mt[kk] = self.mt[kk+self.M] ^ (y >> 1) ^ mag01[y & 1]
        else:
          self.mt[kk] = self.mt[kk+self.M-self.N] ^ (y >> 1) ^ mag01[y & 1]
      
      y = (self.mt[self.N-1] & self.UPPER_MASK) | (self.mt[0] & self.LOWER_MASK)
      self.mt[self.N-1] = self.mt[self.M-1] ^ (y >> 1) ^ mag01[y & 1]
      self.mti = 0

    y = self.mt[self.mti]
    self.mti += 1

    y ^= self.TEMPERING_SHIFT_U(y)
    y ^= self.TEMPERING_SHIFT_S(y) & self.TEMPERING_MASK_B
    y ^= self.TEMPERING_SHIFT_T(y) & self.TEMPERING_MASK_C
    y ^= self.TEMPERING_SHIFT_L(y)

    return y / 0xffffffff
  
if __name__ == '__main__':
  gen = MersenneTwister(4357)
  for _ in range(10):
    print(gen.next())