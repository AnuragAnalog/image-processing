#!/usr/bin/python3

import numpy as np

def preprocess(image):
    if not isinstance(image, np.ndarray):
        raise TypeError("only numpy.ndarray dtypes are expected")

    image = image.astype('int32')

    return image

def negative(image, L=256):
    image = preprocess(image)

    return (L-1) - image

def log_transform(image, c=1):
    image = preprocess(image)

    return c * np.log(1 + image)

def identity(image):
    image = preprocess(image)

    return image

def power_transform(image, gamma=1, c=1):
    image = preprocess(image)

    return c * np.power(image, gamma)

def piecewise_transform(image, r1=64, r2=196, s1=64, s2=196, L=256):
    image = preprocess(image)

    lines = [([0, r1], [0, s1]), ([r1, r2], [s1, s2]), ([r2, L-1], [s2, L-1])]

    for point in lines:
        slope, intercept = np.polyfit(x=point[0], y=point[1], deg=1)

        mask = np.logical_and((point[0][0] <= image), (image <= point[0][0]))
        image[mask] = np.floor(slope * image[mask] + intercept)

    return image