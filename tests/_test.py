# from services.count_areas_simple_clone import ColourCounter
import numpy as np
from utils.union_find import UnionFind


def test_union_find():
    ds = UnionFind(10)
    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(8, 9)
    assert all(ds.elems == [0, 0, 2, 2, 4, 4, 6, 6, 8, 8])
    ds.union(6, 9)
    assert all(ds.elems == [0, 0, 2, 2, 4, 4, 6, 6, 6, 8]) # 9 points to 8, 8 points to 6
    assert ds.find(9) == 6
    assert all(ds.elems == [0, 0, 2, 2, 4, 4, 6, 6, 6, 6]) # 9 points to 8, 8 points to 6

    ds.union(7, 5)
    ds.union(0, 2)
    ds.union(3, 4)
    ds.union(6, 1)
    ds.union(8, 9)

# def test_colour_counter():
#     """
#     [255, 255, 0],
#     [255, 0, 0],
#     [0, 0, 100],
#     [0, 0, 0],
#     [0, 255, 255]
#     """
#     matrix = np.zeros((5, 3), dtype='uint8')
#     matrix[0, 0] = 255
#     matrix[1, 0] = 255
#     matrix[0, 1] = 255
#     matrix[-1, -1] = 255
#     matrix[-1, -2] = 255
#     matrix[2, 2] = 100
#     shape = [5, 3]
#
#     output = np.zeros(256, dtype='uint8')
#     output[0] = 1
#     output[-1] = 2
#     output[100] = 1
#     result = ColourCounter(matrix, shape).count_areas()
#     for i, val in enumerate(output):
#         assert result[i] == val
#
#     """
#     [0, 255, 0, 0, 0],
#     [0, 100, 100, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
#     """
#
#     matrix = np.zeros(10 * 5, dtype='uint8')
#     shape = (10, 5)
#     matrix = matrix.reshape(shape)
#     matrix[1, 2] = 100
#     matrix[1, 1] = 100
#     matrix[0, 1] = 255
#
#     output = np.zeros(256)
#     output[0] = 1
#     output[-1] = 1
#     output[100] = 1
#     print(matrix)
#     result = ColourCounter(matrix, shape).count_areas()
#     print(result)
#     for i, val in enumerate(output):
#         assert result[i] == val
