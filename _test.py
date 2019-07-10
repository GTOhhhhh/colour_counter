from .services.count_areas import colour_counter
import numpy as np
import bitarray

matrix = np.zeros((5, 3))
matrix[0, 0] = 255
matrix[1, 0] = 255
matrix[0, 1] = 255
matrix[-1, -1] = 255
matrix[-1, -2] = 255
matrix[2, 2] = 100
shape = [5,3]


# [[255. 255.   0.]
#  [255.   0.   0.]
#  [  0.   0. 100.]
#  [  0.   0.   0.]
#  [  0. 255. 255.]]


# def test_four_neighbours():
#     assert sorted(four_neighbours(matrix, shape, 0, 0)) == sorted([[1, 0], [0, 1]])
#     assert sorted(four_neighbours(matrix, shape, 4, 2)) == sorted([[4, 1]])
#     assert sorted(four_neighbours(matrix, shape, 2, 1)) == sorted([[2, 0], [1, 1], [3, 1]])

def test_perimeter_walk():
    visited = bitarray((shape[0] * shape[1]))
    assert test_perimeter_walk(matrix, shape, visited, )

# def test_flood_fill():
#     visited = np.zeros((5, 3))
#     visited[2, 2] = 1
#     assert flood_fill(matrix, shape, visited, 2, 2)[2, 2] == visited[2, 2]
#
#     visited[0, 0] = 1
#     visited[1, 0] = 1
#     visited[0, 1] = 1
#     for i, row in enumerate(flood_fill(matrix, shape, visited, 0, 0)):
#         for j, elem in enumerate(row):
#             assert visited[i, j] == elem
#
#     for i, row in enumerate(flood_fill(matrix, shape, visited, 0, 0)):
#         for j, elem in enumerate(row):
#             assert visited[i, j] == elem
#
#     for i, row in enumerate(matrix):
#         for j, elem in enumerate(row):
#             if elem == 0:
#                 visited[i, j] = 1
#
#     for i, row in enumerate(flood_fill(matrix, shape, visited, 0, 2)):
#         for j, elem in enumerate(row):
#             assert visited[i, j] == elem


# def test_colour_counter():
#     output = np.zeros(256)
#     output[0] = 1
#     output[-1] = 2
#     output[100] = 1
#     for i, val in enumerate(output):
#         assert colour_counter(matrix, shape)[i] == val

