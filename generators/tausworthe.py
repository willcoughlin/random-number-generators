class Tausworthe:
  def __init__(self, r, q, l, seed=31):
    self.r = r
    self.q = q
    self.l = l

    self.i = self.q

    # Convert seed to q-length bit list
    seed_str = f'{seed % 2**q:0{q}b}'
    self.bits = list(map(int, seed_str))

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

  def get_bits(self): return self.bits

if __name__ == '__main__':
  gen = Tausworthe(r=3, q=5, l=4, seed=31)
  for _ in range(10):
    print(gen.next())