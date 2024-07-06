class tausworthe:
  def __init__(self, r, q, l, seed=1):
    self.r = r
    self.q = q
    self.l = l

    self.i = self.q

    if type(seed) is int:
      # TODO: error check 0 or 1?
      self.bits = [seed]*self.q
    if type(seed) is list:
      if len(seed) != q: 
        raise ValueError("Length of given `seed` must be equal to `q`")
      # TODO: error check 0 or 1?
      self.bits = seed[:q]

  def __bits_to_int(self, bits_to_convert):
    bit_str = ''.join(map(str, bits_to_convert))
    return int(bit_str, 2)
  
  def __increment_bits(self):
    stop = self.i+self.l
    while self.i < stop:
      self.bits.append(self.bits[self.i-self.r] ^ self.bits[self.i-self.q])
      self.i += 1

  def next(self):
    bits_to_convert = self.bits[self.i-self.l-1:self.i-1]
    self.__increment_bits()

    numerator = self.__bits_to_int(bits_to_convert)
    return numerator / 2**self.l

gen = tausworthe(r=3, q=5, l=4, seed=[1,0,1,0,1])

for _ in range(10):
  print(gen.next())