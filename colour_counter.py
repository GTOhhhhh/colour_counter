#!/usr/bin/env python3

import numpy as np
import argparse


# import sys
# np.set_printoptions(threshold=sys.maxsize)

def colour_counter(input_file, shape):
    return 0

if name == main:


parser = argparse.ArgumentParser(description='Count the number of coloured areas in an image')
parser.add_argument('input_file', help='the binary input file')
parser.add_argument('--shape', required=True,
                    help='specifies the image shape of the provided binary file')
args = parser.parse_args()

A = np.fromfile(args.input_file, dtype='int8', sep='')
A = A.reshape([int(i) for i in args.shape.split(',')])
print(A)
