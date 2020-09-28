#!/usr/bin/python3

import numpy as np

from PIL import Image
from matplotlib import pyplot as plt

def bit_plane(image, n):
    return ((image >> n) & 1).astype('bool')

def n_bit_planes(image):

    if not isinstance(image, np.ndarray):
        raise ValueError("Expects only numpy ndarray's")

    bit_planes = list()

    for n in range(8):
        plane = image.copy()

        mask = bit_plane(plane, n)
        plane[mask] = 255
        plane[~mask] = 0

        bit_planes.append(plane)

    return bit_planes


if __name__ == "__main__":
    image = Image.open('sample.jpeg')
    image = np.asarray(image)

    planes = n_bit_planes(image)

    fig, ax = plt.subplots(nrows=2, ncols=4)

    for i in range(2):
        for j in range(4):
            ax[i][j].set_title(str(i*4+j)+" plane")
            ax[i][j].imshow(planes[i*4+j], cmap='gray')

    plt.show()