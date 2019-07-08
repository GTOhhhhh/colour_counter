import cv2 as cv
import numpy as np
import sys

# turn png to unsigned ints
np.set_printoptions(threshold=sys.maxsize)


def png_to_ints(input_file):
    im = cv.imread(input_file, cv.IMREAD_GRAYSCALE) # reshape(shape)
    return im
