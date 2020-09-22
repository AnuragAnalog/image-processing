#!/usr/bin/python3

import numpy as np

def negative(image, L=256):
    return (L-1) - image

def log_transform(image, c=1):
    return c * np.log(1 + image)

def identity(image):
    return image

def power_transform(image, gamma=1, c=1):
    return c * np.power(image, gamma)