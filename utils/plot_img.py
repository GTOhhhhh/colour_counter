#!/usr/bin/env python3

import numpy as np
from matplotlib import pylab as plt

import sys

np.set_printoptions(threshold=sys.maxsize)
A = np.fromfile('../services/sample.bin', dtype='uint8', sep="")
A = A.reshape([256, 256])
print(A)
plt.style.use('grayscale')
plt.imshow(A)
plt.show()
