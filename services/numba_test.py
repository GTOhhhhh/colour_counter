from numba import njit
import numpy as np


@njit
def go_fast(): # Function is compiled to machine code when called the first time
    x = np.arange(100).reshape(10, 10)
    trace = 0
    for i in range(x.shape[0]):   # Numba likes loops
        trace += np.tanh(x[i, i]) # Numba likes NumPy functions
    return x + trace              # Numba likes NumPy broadcasting

print(go_fast())


