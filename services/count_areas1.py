#!/usr/bin/env python3

import numpy as np
import argparse
# from disjoint_set import DisjointSet
from memory_profiler import profile
from .my_disjoint_set import DisjointSet


class ColourCounter():
    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape
        # self.copy = np.zeros(shape[0] * shape[1], dtype='uint8')
        self.output = np.zeros(256, dtype='uint8')
        self.ds = DisjointSet(shape[0]*shape[1])


    def count_areas(self):
        """Finds the number of continuous areas for each greyscale colour in an image

        Parameters:
            matrix (numpy ndarray): A 2d array of 8 bit integers encoding a grey scale image
            shape (list): x, y dimensions of the array

        Returns:
            output (numpy array): an array of length 256 representing the number of different sections for each colour
        """

        # ds to find returns the set id/label by following the pointers to the root label'
        # if you find on a new element it becomes a new root
        # ds union merges to sets to the same label
        # ds = DisjointSet()
        # width * row + col
        for i, elem in enumerate(self.matrix):
            west = i - 1
            west_elem = None if west < 0 else self.matrix[west]
            north = i - shape[0]
            north_elem = None if north < 0 else self.matrix[north]
            if west_elem != elem and north_elem != elem:
                # largest_label = largest_label + 1
                # self.copy[i] = largest_label
                self.ds.find(i)
                self.output[elem] += 1
            elif west_elem == elem and north_elem != elem:
                # self.copy[i] = self._find(west)
                self.ds.union(i, west)
            elif west_elem != elem and north_elem == elem:
                self.ds.union(i, north)
                # self.copy[i] = self._find(north)

            else:  # north and west are both neighbours
                # self._union(west, north)
                # self.copy[elem] = self._find(west_elem)
                self.ds.union(i, west)

        # print(ds)
        # # print('copy', self.copy)
        # for i in ds.itersets():
        #     colour = self.matrix[i.pop()]
        #     self.output[int(colour)] += 1

        return self.output

    # def _union(self, x, y):
    #     self.copy[self._find(x)] = self._find(y)

    # def _find(self, x):
    #     y = x
    #     while self.copy[y] != y:
    #         y = self.copy[y]
    #     while self.copy[x] != x: # we get stuck in this loop
    #         z = self.copy[x]
    #         self.copy[x] = y
    #         x = z
    #     return y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                    help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    # shape = [int(i) for i in args.shape.split(',')]
    # matrix = np.fromfile(args.input_file, dtype='uint8', sep='')
    matrix = np.zeros(3 * 5, dtype='uint8')
    matrix[0] = 255
    matrix[3 * 1 + 0] = 255
    matrix[1] = 255
    matrix[-1] = 255
    matrix[-2] = 255
    matrix[2 * 3 + 2] = 100
    shape = (3, 5)
    print(matrix.reshape((5, 3)))
    colour_counter = ColourCounter(matrix, shape)
    print(colour_counter.count_areas())
