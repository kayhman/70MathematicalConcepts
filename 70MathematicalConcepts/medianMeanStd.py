import math
import numpy as np

# Computation of cardinality
# i.e., simply the number of elements in an array.
def cardinality(data):
    return len(data)

# Computation of the mean.
def mean(data):
    sum = 0
    for d in data:
        sum += d
    n = cardinality(data)
    return sum / n

# Computation of the standard deviation.
def std(data):
    m = mean(data)
    n = cardinality(data)
    std = 0
    for d in data:
        std += (d - m)**2 / n
    return math.sqrt(std)

# Computation of the median.
def median(data):
    n = cardinality(data)
    data = sorted(data)
    if n % 2 == 1: # n is odd.
        return data[n // 2]
    else:
        return (data[n // 2  - 1] + data[n // 2]) / 2

# Comparison of the functions defined above
# with the standard implementations from numpy.
data = [1, 2, 3, 4, 5, 6]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
# > 1.7078251276599332 1.707825127659933
#> 3.5 3.5

# This new data set
# has the same mean
# but a zero standard deviation.
data = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
#> 0.0 0.0
#> 3.5 3.5

# This new data set
# has the same mean
# but this time a different median.
data = [0, 0, 0, 0, 0, 21]
print(cardinality(data))
print(mean(data), np.mean(data))
print(std(data), np.std(data))
print(median(data), np.median(data))
#> 6
#> 3.5 3.5
#> 7.826237921249264 7.826237921249264
#> 0.0 0.0