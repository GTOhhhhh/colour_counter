#!/usr/bin/env python3

import numpy as np
import argparse

import sys

np.set_printoptions(threshold=sys.maxsize)


def colour_counter(input_file, shape):
    arr = np.fromfile(args.input_file, dtype='uint8', sep='')
    matrix = arr.reshape([int(i) for i in args.shape.split(',')])
    print(matrix)
    output = np.zeros(256)  # 0 is black, 255 is white
    for row in matrix:
        for i in row:
            perimeter_walk(i)


def perimeter_walk(start):
    return start


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    colour_counter(args.input_file, args.shape)

    # print(A)
