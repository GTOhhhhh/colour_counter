#!/usr/bin/env python3

import numpy as np
import argparse

if __name__ == "__main__":
    from utils.union_find import UnionFind
else:
    from colour_counter.services.utils.union_find import UnionFind


def count_areas(matrix, shape):
    output = np.zeros(256, dtype='uint8')
    uf = UnionFind(shape[0] * shape[1])
    for i in range(shape[0] * shape[1]):
        elem = matrix[i]
        west = i - 1 if i % shape[1] != 0 else None  # bound check: dont step left off the matrix
        west_elem = None if west is None else matrix[west]
        north = i - shape[1] if i - shape[1] >= 0 else None  # bound check: dont step up off the matrix
        north_elem = None if north is None else matrix[north]

        if west_elem != elem and north_elem != elem:
            continue

        elif west_elem == elem and north_elem != elem:
            uf.union(west, i)  # current belongs to same region as left

        elif west_elem != elem and north_elem == elem:
            uf.union(north, i)  # current belongs to same region as north

        else:  # north and west are both neighbours
            uf.union(west, north)
            uf.union(i, west)

    # resolve all labels to their parent
    result = set()
    for i in uf.elems:
        result.add(uf.find(i))

    # count up the regions
    for i in result:
        colour = matrix[i]
        output[colour] += 1

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
    parser.add_argument('input_file', help='the binary input file')
    parser.add_argument('--shape', required=True,
                        help='specifies the image shape of the provided binary file')
    args = parser.parse_args()
    shape = [int(i) for i in args.shape.split(',')]
    matrix = np.fromfile(args.input_file, dtype='uint8', sep='')
    for i in count_areas(matrix, shape):
        print(i)
