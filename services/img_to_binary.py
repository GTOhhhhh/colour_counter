import cv2 as cv
import numpy as np
import sys

# turn png to unsigned ints
np.set_printoptions(threshold=sys.maxsize)
im = cv.imread('../input_files/shades-of-grey.png')
# print(im)

# turn unsigned ints to image
input_file = '../input_files/sample.bin'
arr = np.fromfile(input_file, dtype='uint8', sep='')
# print(arr)
input_file = cv.imdecode(im, cv.IMREAD_GRAYSCALE)
matrix = arr.reshape([256,256])
print(matrix)

im1 = cv.imwrite('sample_image.jpeg', matrix)
