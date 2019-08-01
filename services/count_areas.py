#!/usr/bin/env python3

import numpy as np
import argparse
# from disjoint_set import DisjointSet
from memory_profiler import profile
from disjoint_set import DisjointSet
from utils.union_find import UnionFind

np.set_printoptions(threshold=np.inf)


class ColourCounter():
    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape
        # self.copy = np.zeros(shape[0] * shape[1], dtype='uint8')
        self.output = np.zeros(256, dtype='uint8')
        self.ds = DisjointSet()
        self.uf = UnionFind(shape[0] * shape[1])

    def count_areas(self):
        """Finds the number of continuous areas for each greyscale colour in an image
        Parameters:
            matrix (numpy ndarray): A 2d array of 8 bit integers encoding a grey scale image
            shape (list): x, y dimensions of the array
        Returns:
            output (numpy array): an array of length 256 representing the number of different sections for each colour
        """
        # width * row + col
        for i, elem in enumerate(self.matrix):
            west = i - 1 if i % shape[1] != 0 else None
            west_elem = None if west is None else self.matrix[west]
            north = i - shape[1] if i - shape[1] >= 0 else None
            north_elem = None if north is None else self.matrix[north]
            if west_elem != elem and north_elem != elem:
                # largest_label = largest_label + 1
                # self.copy[i] = largest_label
                self.ds.find(i)
                self.uf.find(i)
            elif west_elem == elem and north_elem != elem:
                # self.copy[i] = self._find(west)
                self.ds.union(west, i)
                self.uf.union(west, i)
            elif west_elem != elem and north_elem == elem:
                self.ds.union(north, i)
                self.uf.union(north, i)
                # self.copy[i] = self._find(north)

            else:  # north and west are both neighbours
                # self._union(west, north)
                # self.copy[elem] = self._find(west_elem)
                self.ds.union(north, west)
                self.ds.union(north, i)

                self.uf.union(west, north)
                self.uf.union(i, west)

        result = [self.uf.find(i) for i in self.uf.elems]

        result = np.array(result).reshape(shape[0], shape[1])
        for idx, i in enumerate(result):
            print(idx)
            print([(j % 256, (j - j % 256) / 256) for j in i])
        print('labels')
        transform = [(i % 256, (i - i % 256) / 256) for i in result]
        # print(transform)
        a = np.unique(result)
        print(a)
        indexed = [(i % 256, (i - i % 256) / 256) for i in a]
        print(indexed)

        # print('iter sets')
        for i in self.ds.itersets():
            # print(i)
            colour = self.matrix[i.pop()]
            self.output[int(colour)] += 1

        # for i in a:
        #     colour = self.matrix[i]
        #     self.output[colour] += 1

        return self.output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()

    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='')

    # matrix = np.zeros(3 * 5, dtype='uint8')
    # matrix[0] = 255
    # matrix[3 * 1 + 0] = 255
    # matrix[1] = 255
    # matrix[-1] = 255
    # matrix[-2] = 255
    # matrix[2 * 3 + 2] = 100
    # shape = (5,3)
    # print(matrix.reshape((5, 3)))
    #
    # matrix = np.zeros(10 * 5, dtype='uint8')
    # shape = (10, 5)
    # matrix = matrix.reshape(shape)
    # matrix[1, 2] = 100
    # matrix[1, 1] = 100
    # matrix[0, 1] = 255
    # print(matrix)
    # matrix = matrix.flatten()
    colour_counter = ColourCounter(matrix, shape)
    print(colour_counter.count_areas())
