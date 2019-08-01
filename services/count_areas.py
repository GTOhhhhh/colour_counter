#!/usr/bin/env python3

import numpy as np
import argparse
from utils.union_find import UnionFind
from numba import jit, njit, jitclass
from numbba import


spec = [
    ('value', int32),               # a simple scalar field
    ('array', float32[:]),          # an array field
]

@jitclass
class ColourCounter(object):
    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape
        self.output = np.zeros(256, dtype='uint8')
        self.uf = UnionFind(shape[0] * shape[1])

    # @jit
    # def count_areas(self):
    #     for i in range(shape[0] * shape[1]):
    #         elem = self.matrix[i]

    @njit
    def count_areas(self):
        for i in range(shape[0]*shape[1]):
            elem = self.matrix[i]
            west = i - 1 if i % shape[1] != 0 else None
            west_elem = None if west is None else self.matrix[west]
            north = i - shape[1] if i - shape[1] >= 0 else None
            north_elem = None if north is None else self.matrix[north]
            if west_elem != elem and north_elem != elem:
                continue

            elif west_elem == elem and north_elem != elem:
                self.uf.union(west, i)

            elif west_elem != elem and north_elem == elem:
                self.uf.union(north, i)

            else:  # north and west are both neighbours
                self.uf.union(west, north)
                self.uf.union(i, west)

        result = set()
        for i in self.uf.elems:
            result.add(self.uf.find(i))

        for i in result:
            colour = self.matrix[i]
            self.output[colour] += 1

        return self.output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='')
    colour_counter = ColourCounter(matrix, shape)
    print(colour_counter.count_areas())
