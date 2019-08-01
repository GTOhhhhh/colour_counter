from array import array


class DisjointSet:
    __slots__ = 'ranks', 'parents'

    def __init__(self, n):
        self.ranks = array('L', [0] * n)
        self.parents = array('L', [])
        self.make_set(n)

    def make_set(self, n):
        for i in range(n):
            self.parents.insert(i, i)

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    # assign label of label of x to y
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.ranks[x_root] < self.ranks[y_root]:
                self.parents[x_root] = y_root
            elif self.ranks[x_root] > self.ranks[y_root]:
                self.parents[y_root] = x_root
            else:
                self.parents[y_root] = x_root
                self.ranks[x_root] += 1


