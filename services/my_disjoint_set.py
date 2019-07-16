from array import array
import numpy as np


class DisjointSet:
    __slots__ = 'rank', 'parent'

    def __init__(self, n):
        self.rank = array('L', [0] * n)
        self.parent = array('L', [])
        self.make_set(n)

    def make_set(self, n):
        for i in range(n):
            self.parent.insert(i, i)
        # print(self.parent)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1


matrix = np.zeros(3 * 5, dtype='uint8')
matrix[0] = 255
matrix[3 * 1 + 0] = 255
matrix[1] = 255
matrix[-1] = 255
matrix[-2] = 255
matrix[2 * 3 + 2] = 100
shape = (3, 5)
# print(matrix.reshape((5, 3)))

ds = DisjointSet(4000*4000)
print('find', ds.find(1500))
ds.union(1500, 3)
print('find', ds.find(3))

