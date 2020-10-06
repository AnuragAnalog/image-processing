#!/usr/bin/python3

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def convolve2D(image, kernel, padding=0, stride=1):
    if isinstance(kernel, str):
        kernel = np.ones((3, 3))
    elif isinstance(kernel, np.ndarray):
        kernel = np.flipud(np.fliplr(kernel))
    else:
        raise ValueError("only numpy.ndarray dtypes are expected for kernel")
    
    if not isinstance(image, np.ndarray):
        raise ValueError("only numpy.ndarray dtypes are expected for image")

    x_oimg = int(((image.shape[0] + 2 * padding - kernel.shape[0]) / stride) + 1)
    y_oimg = int(((image.shape[1] + 2 * padding - kernel.shape[1]) / stride) + 1)

    out_img = np.zeros((x_oimg, y_oimg))
    if padding != 0:
        image = np.pad(image, padding)

    for x in range(0, out_img.shape[0], stride):
        for y in range(0, out_img.shape[1], stride):
            out_img[x, y] = np.sum(image[x:x + kernel.shape[0], y:y + kernel.shape[1]] * kernel)

    return out_img

if __name__ == "__main__":
    img = np.asarray(Image.open('sample.jpeg'))[:, :, 0]
    # img = np.round(np.random.randn(3, 3))
    kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])

    plt.imshow(convolve2D(img, kernel))
    plt.show()