import cv2 as cv


def png_to_ints(input_file):
    """takes an image and converts it in to a matrix of 8 bit integers"""
    im = cv.imread(input_file, cv.IMREAD_GRAYSCALE)  # reshape(shape)
    return im
