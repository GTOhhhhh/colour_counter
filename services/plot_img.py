#!/usr/bin/env python3

import numpy as np
from matplotlib import pylab as plt

A = np.fromfile('sample.bin', dtype='int8', sep="")
A = A.reshape([256, 256])
plt.imshow(A)
