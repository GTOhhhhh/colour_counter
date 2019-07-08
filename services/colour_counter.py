#!/usr/bin/env python3

import numpy as np
import argparse
from collections import deque

import sys

np.set_printoptions(threshold=sys.maxsize)


def colour_counter(matrix, shape):
    """Finds the number of continuous areas for each greyscale colour in an image

    Parameters:
        matrix (numpy ndarray): The file location of the spreadsheet
        shape (list): x, y dimensions of the array

    Returns:
        visited (numpy array): an array of length 256 representing the number of different sections for each colour
    """
    output = np.zeros(256)  # 0 is black, 255 is white
    visited = np.zeros(shape)
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):

            if visited[i, j]:
                continue
            else:
                visited = flood_fill(matrix, shape, visited, i, j)
                output[int(matrix[i, j])] += 1
                visited[i, j] = 1
    return output


def flood_fill(matrix, shape, visited, i, j):
    """Finds the area of continuous elements with a specific colour value"""
    stack = deque()
    stack.append((i, j))
    while stack:
        curr = stack.pop()
        if visited[curr[0], curr[1]]:
            continue
        else:
            visited[curr[0], curr[1]] = 1
            stack.extend(four_neighbours(matrix, shape, curr[0], curr[1]))
    return visited


def four_neighbours(matrix, shape, i, j):
    """Returns four adjacent elements with the same colour as the target element"""
    indexes = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]  # north, south, east, west
    indexes = [idx for idx in indexes if idx[0] > -1 and idx[1] > -1]  # remove negative indexes
    indexes = [idx for idx in indexes if idx[0] < shape[0] and idx[1] < shape[1]]  # remove out of bounds indexes
    neighbours = [idx for idx in indexes if matrix[idx[0], idx[1]] == matrix[i, j]]  # remove different colours
    return neighbours


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    shape = [int(i) for i in args.shape.split(',')]
    arr = np.fromfile(args.input_file, dtype='uint8', sep='')
    matrix = arr.reshape(shape)
    colour_counter(matrix, shape)
