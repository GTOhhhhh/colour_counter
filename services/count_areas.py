#!/usr/bin/env python3

import numpy as np
import argparse
from collections import deque
from bitarray import bitarray


def colour_counter(matrix, shape):
    """Finds the number of continuous areas for each greyscale colour in an image

    Parameters:
        matrix (numpy ndarray): A 2d array of 8 bit integers encoding a grey scale image
        shape (list): x, y dimensions of the array

    Returns:
        visited (numpy array): an array of length 256 representing the number of different sections for each colour
    """
    output = np.zeros(256)
    visited = bitarray((shape[0] * shape[1]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if visited[i * shape[1] + j]:
                continue
            else:
                visited[i * shape[1] + j] = 1
                # can return indexes and mark them as visited
                # or can mark as visited inside the function
                output[int(matrix[i, j])] += 1
    return output


def perimeter_walk(matrix, shape, visited, i, j):
    boundary = {(i, j)}
    colour = matrix[i, j]
    start_i = i
    start_j = j
    # we consider the first pixel was entered from the right
    # so we backtrack left
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
        print('boundary', boundary)
        print(c_i, c_j)
        if c_i == start_i and c_j == start_j and direction == 2:
            break
        # colour matches and inside the matrix
        if matrix[c_i, c_j] == colour and c_i > -1 and c_j > -1:
            boundary.add((c_i, c_j))
            p_i = c_i
            p_j = c_j
            print('backtrack!')
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
    return boundary


# def flood_fill(matrix, shape, visited, i, j):
#     """Finds the area of continuous elements with a specific colour value"""
#     stack = deque()
#     stack.append((i, j))
#     while stack:
#         curr = stack.pop()
#         if visited[curr[0] * shape[1] + curr[1]]:
#             continue
#         else:
#             visited[curr[0] * shape[1] + curr[1]] = 1
#             stack.extend(four_neighbours(matrix, shape, curr[0], curr[1]))
#     return visited

#
# def four_neighbours(matrix, shape, i, j):
#     """Returns four adjacent elements with the same colour as the target element"""
#     indexes = [[i - 1, j], [i + 1, j], [i, j + 1], [i, j - 1]]  # north, south, east, west
#     indexes = [idx for idx in indexes if idx[0] > -1 and idx[1] > -1]  # remove negative indexes
#     indexes = [idx for idx in indexes if idx[0] < shape[0] and idx[1] < shape[1]]  # remove out of bounds indexes
#     neighbours = [idx for idx in indexes if matrix[idx[0], idx[1]] == matrix[i, j]]  # remove different colours
#     return neighbours


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='').reshape(shape)
    for i in colour_counter(matrix, shape):
        print(int(i))
