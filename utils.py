#!/usr/bin/python3

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

def convolve2D(image, kernel, padding=0, stride=1, kernel_size=None):
    if isinstance(kernel, str):
        kernel_type = kernel
        if kernel_size is None:
            kernel = np.ones((3, 3))
        else:
            kernel = np.ones((kernel_size, kernel_size))
    elif isinstance(kernel, np.ndarray):
        kernel_type = None
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
            if isinstance(kernel_type, str):
                if kernel_type == 'max':
                    kernel_funct = np.max
                elif kernel_type == 'mix':
                    kernel_funct = np.min
                elif kernel_type == 'median':
                    kernel_funct = np.median
                elif kernel_type in ['mean', 'average']:
                    kernel_funct = np.mean
                else:
                    raise ValueError("Kernel can only be anyone of [max, min, mean, median]")
                out_img[x, y] = kernel_funct(image[x:x + kernel.shape[0], y:y + kernel.shape[1]] * kernel)
            elif isinstance(kernel, np.ndarray):
                out_img[x, y] = np.sum(image[x:x + kernel.shape[0], y:y + kernel.shape[1]] * kernel)
            else:
                raise ValueError("Kernel dtype can only be str or numpy.ndarray")

    return out_img

if __name__ == "__main__":
    img = np.asarray(Image.open('sample.jpeg'))[:, :, 0]
    kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])

    plt.imshow(convolve2D(img, kernel))
    plt.show()