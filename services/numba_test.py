from numba import jit, uint32
import numpy as np
from timeit import timeit


@jit(nopython=True, cache=True)
def go_fast():  # Function is compiled to machine code when called the first time
    x = np.arange(100, dtype=np.uint32).reshape(10, 10)
    trace = 0
    for i in range(x.shape[0]):  # Numba likes loops
        trace += np.tanh(x[i, i])  # Numba likes NumPy functions
    return x + trace  # Numba likes NumPy broadcasting


def go_slow():  # Function is compiled to machine code when called the first time
    x = np.arange(100).reshape(10, 10)
    trace = 0
    for i in range(x.shape[0]):  # Numba likes loops
        trace += np.tanh(x[i, i])  # Numba likes NumPy functions
    return x + trace  # Numba likes NumPy broadcasting


@jit(nopython=True, cache=True)
def no_loop():
    x = np.arange(10 ** 5)
    return x

@jit(nopython=True, cache=True)
def loop():
    x = np.empty(10**5, dtype=np.uint32)
    for i in range(10**5):
        x[i] = i
    return x

# @jit(nopython=True, cache=True)
def slow_no_loop():
    x = np.arange(10 ** 5)
    return x

# @jit(nopython=True, cache=True)
def slow_loop():
    x = np.empty(10**5, dtype=np.uint32)
    for i in range(10**5):
        x[i] = i
    return x


for i in range(3):
    # print(timeit(go_fast))
    # print(timeit(go_slow))
    print('jit')
    print(timeit(no_loop))
    print(timeit(loop))
    print('no jit')
    print(timeit(slow_no_loop))
    print(timeit(slow_loop))


