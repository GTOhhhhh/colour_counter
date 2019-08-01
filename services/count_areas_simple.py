#!/usr/bin/env python3

import numpy as np
import argparse
# from disjoint_set import DisjointSet
from memory_profiler import profile
from utils.disjoint_set import DisjointSet
from utils.union_find import UnionFind
from disjoint_set import DisjointSet


class ColourCounter():
    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape
        # self.copy = np.zeros(shape[0] * shape[1], dtype='uint8')
        self.output = np.zeros(256, dtype='uint8')
        self.ds = UnionFind(shape[0] * shape[1])
        self.dss = DisjointSet()

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
        for i, elem in enumerate(self.matrix):  # TODO FASTER ITERATION?
            # @todo yikes it thinks 0 from the top row is left of 255 from the next row
            # need to bound the neighbour checks
            west = i - 1
            west_elem = None if west < 0 else self.matrix[west]
            north = i - shape[0]
            north_elem = None if north < 0 else self.matrix[north]
            if west_elem != elem and north_elem != elem:
                self.ds.find(i)
                self.dss.find(i)

            elif west_elem == elem and north_elem != elem:
                self.ds.union(i, west)
                self.dss.union(i, west)


            elif west_elem != elem and north_elem == elem:
                self.ds.union(i, north)
                self.dss.union(i, north)


            else:  # north and west are both neighbours
                self.ds.union(west, north)
                self.dss.union(west, north)

                self.ds.union(i, west)
                self.dss.union(i, west)


        # print(self.ds.size)
        print(self.ds.elems.reshape(10,5))

        for i in self.dss.itersets():
            print(i)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()

    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='')

    matrix = np.zeros(3 * 5, dtype='uint8')
    matrix[0] = 255
    matrix[3 * 1 + 0] = 255
    matrix[1] = 255
    matrix[-1] = 255
    matrix[-2] = 255
    matrix[2 * 3 + 2] = 100
    shape = (3, 5)
    print(matrix.reshape((5, 3)))

    matrix = np.zeros(10 * 5, dtype='uint8')
    shape = (10, 5)
    matrix = matrix.reshape(shape)
    matrix[1,2] = 100
    matrix[1,1] = 100
    matrix[0,1] = 255
    matrix = matrix.flatten()
    colour_counter = ColourCounter(matrix, shape)
    print(colour_counter.count_areas())
