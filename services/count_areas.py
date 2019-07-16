#!/usr/bin/env python3

import numpy as np
import argparse
from bitarray import bitarray

np.set_printoptions(threshold=100000)


def colour_counter(matrix, shape):
    """Finds the number of continuous areas for each greyscale colour in an image

    Parameters:
        matrix (numpy ndarray): A 2d array of 8 bit integers encoding a grey scale image
        shape (list): x, y dimensions of the array

    Returns:
        output (numpy array): an array of length 256 representing the number of different sections for each colour
    """
    output = np.zeros(256)
    # visited = bitarray((shape[0] * shape[1]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if visited[i, j]:  # a perimeter point
                continue
                # if previous was visited and same colour
            elif visited[i, j] and j - 1 > 0 and matrix[i, j - 1] == matrix[i, j]:
                visited[i, j] = 1
            else:
                output[int(matrix[i, j])] += 1
                visited[i, j] = 1
                # can return indexes and mark them as visited
                # or can mark as visited inside the function
                visited = perimeter_walk(matrix, shape, i, j)
    return output


def perimeter_walk(matrix, shape,  i, j):
    colour = matrix[i, j]
    start_i = i
    start_j = j
    p_i = start_i
    p_j = start_j
    # we consider the first pixel was entered from the right
    # so we backtrack left
    c_i = p_i
    c_j = p_j - 1
    c_i -= 1
    # since we backtracked left, the first direction to look is up (clockwise rotation)
    direction = 1  # 0 is left, 1 is up, 2 is right, 3 is down
    while True:
        if c_i == start_i and c_j == start_j and direction == 2:
            break
        # colour matches and inside the matrix
        if -1 < c_i < shape[0] and -1 < c_j < shape[1] and matrix[c_i, c_j] == colour:
            visited[c_i, c_j] = 1
            if direction == 0:  # if left backtrack right
                c_j += 1
                direction = 2
            elif direction == 1:  # if up backtrack down
                c_i += 1
                direction = 3
            elif direction == 2:  # if right backtrack left
                c_j -= 1
                direction = 0
            elif direction == 3:  # if down backtrack up
                c_i -= 1
                direction = 1
        else:
            direction = (direction + 1) % 4  # rotate direction clockwise
            if direction == 0:
                c_j -= 1
            elif direction == 1:
                c_i -= 1
            elif direction == 2:
                c_j += 1
            elif direction == 3:
                c_i += 1
    return visiteda


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='').reshape(shape)
    visited = np.zeros((shape[0], shape[1]))
    for i in colour_counter(matrix, shape):
        print(int(i))
    # matrix = np.zeros((5, 3), dtype='uint8')
    # matrix[0, 0] = 255
    # matrix[1, 0] = 255
    # matrix[0, 1] = 255
    # matrix[-1, -1] = 255
    # matrix[-1, -2] = 255
    # matrix[2, 2] = 100
    # shape = [5, 3]

