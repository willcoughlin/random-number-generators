# TODO: delete this?


import numpy as np

from generators.lecuyer import Lecuyer
from generators.mersenne_twister import MersenneTwister
from generators.tausworthe import Tausworthe

if __name__ == '__main__':
  seed = 0xabc

  # Init generators
  lecuyer = Lecuyer(seed)
  mersenne = MersenneTwister(seed)
  tausworthe = Tausworthe(r=7, q=15, l=32, seed=seed)

  # Init sample matrix
  N = 5000
  samples = np.zeros(shape=(N,3))

  # Sample from each
  for i in range(N):
    samples[i] = [lecuyer.next(), mersenne.next(), tausworthe.next()]

  np.save('./data/samples.npy', samples, allow_pickle=False)