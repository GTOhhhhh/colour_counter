from numba import jitclass, uint32
import numpy as np

spec = [
    ('n', uint32),
    ('elems', uint32[:]),
    ('size', uint32[:]),
]


@jitclass(spec)
class UnionFind:
    def __init__(self, n):
        self.elems = np.empty(n, dtype=np.uint32)
        self.size = np.empty(n, dtype=np.uint32)
        for i in range(n):
            self.elems[i] = i
            self.size[i] = 1

    def find(self, x):
        x = np.uint32(x)
        root = x
        while root != self.elems[root]:  # until root is itself
            root = self.elems[root]  # root becomes the next root

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
