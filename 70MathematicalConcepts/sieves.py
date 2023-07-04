# This function returns true if a is a multiple of b.
# That is, if a is different from b,
# and if the remainder of the division of a by b is 0.
def is_multiple(a, b):
  return a != b and a % b == 0


is_multiple(12, 3)
# -> true

is_multiple(13, 3)

# -> false


# This function sifts through the first n integers using the Eratosthenes method.
# It only keeps those that are not multiples of the preceding integers.
def sieves(n):
  # Build an array of integers from 2 to n.
  primes = list(range(2, n + 1))
  idx = 0
  while idx < len(primes):
    p = primes[idx]
    primes = list(filter(lambda x: not is_multiple(x, p), primes))
    idx = idx + 1
  return primes


print(sieves(19))
# -> 2  3  5  7  11  13  17  19
