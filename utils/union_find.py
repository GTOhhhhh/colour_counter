from numba import jit
import sys
from array import array
import numpy as np


class UnionFind:
    __slots__ = 'elems', 'size'

    def __init__(self, n):
        self.elems = np.arange(n, dtype='uint32')
        self.size = np.ones(n, dtype='uint32')

    def find(self, x):
        root = x
        while root != self.elems[x]:
            root = self.elems[x]

        while x != root:
            next = self.elems[x]
            self.elems[x] = root
            x = next

        return root

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 == root2:
            return

        # merge smaller group into larger group
        if self.size[root1] < self.size[root2]:
            self.size[root2] += self.size[root1]
            self.elems[root1] = root2
        else:
            self.size[root1] += self.size[root2]
            self.elems[root2] = root1


# ds = UnionFind(10)
# ds.union(0,9)
# print(ds.elems)
# ds.union(5,6)
# print(ds.elems)
# ds.union(0,6)
# print(ds.elems)


