from skimage import data, io, filters
import numpy as np
from math import pi, sqrt, exp

# Retrieving an image from the skimage library
image = data.brick()

def gaussian_weights(x, y, sigma):
    return 1.0 / sqrt(2 * pi * sigma) * exp(-2*(x**2+y**2)/sigma**2)

def average_weights(x, y, size):
    return 1.0 / size**2

def build_mask(size, fun):
    mask = np.zeros((size, size))
    half = size // 2
    for i in range(-half, half):
        for j in range(- half, half):
            mask[half + i, half + j] = fun(i, j)
    return mask

def convolution(img, mask):
    out = img.copy()
    msize = mask.shape[0]
    for i in range(img.shape[0]):
        # The edges of the image are ignored.
        for j in range(img.shape[1]):
            if i - msize < 0 or i + msize > img.shape[0]:
                continue
            if j - msize < 0 or j + msize > img.shape[1]:
                continue
            pixel = 0
            half = msize // 2
            for k in range(-half, half):
                for l in range(- half, half):
                    pixel +=  mask[half + k, half + l] * img[i + k, j + l]
            out[i, j] = pixel
    return out


# Application of a Gaussian filter
# This also performs a blur.
mask = build_mask(5, lambda x, y : gaussian_weights(x, y, 1))
blur = convolution(image, mask)
io.imsave('gaussian.png', blur)

# Application of a filter that takes the average.
# This also performs a blur, but it is coarser.
mask = build_mask(5, lambda x, y : average_weights(x, y, 5))
blur = convolution(image, mask)
io.imsave('blur.png', blur)

# Application of the Sobel filter
# which detects edges.
mask = np.matrix([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])

edges = convolution(blur, mask)
io.imsave('edges.png', edges)
