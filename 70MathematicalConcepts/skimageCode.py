from skimage import data, io
import numpy as np

# Retrieving an image from the Skimage library.
image = data.brick()

# Images are loaded as NumPy arrays, which is convenient for manipulation.
print(type(image))
#> <class 'numpy.ndarray'>

# Saving the image.
io.imsave('test.png', image)
