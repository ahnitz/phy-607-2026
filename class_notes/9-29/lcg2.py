import sys
import numpy
from matplotlib import pyplot as plt

m = 2**31
a = 1103515245
c = 12345
seeds = numpy.arange(0, 200000, 1)

def rand(x):
    x = (a * x + c) % m
    return x / m

nums = rand(seeds)

plt.hist(nums, bins=200)
plt.show()
