from math import log
from sieves import sieves
import matplotlib.pyplot as plt

# We create a list of integers from 10 to 1,000,000, every 10.
max = 10000
ns = [n for n in range(10, max, 10)]
# -> 500-element Vector{Int64}:10 20 30 40 50 ... 5000.

# We calculate the ratio $\frac{\pi(n)}{n}$ for each of these integers.
primes = sieves(max)
pi = [len([x for x in primes if x <= n]) for n in ns]
freq = [pi[i] / n for (i, n) in enumerate(ns)]
chck = [freq[i] * log(i+1)  for (i, n) in enumerate(ns)]

# And we plot the curve of this ratio as a function of n.
plt.plot(ns, chck)
plt.show()
