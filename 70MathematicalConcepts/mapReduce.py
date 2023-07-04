from functools import reduce

X = [x - 25 for x in range(0, 51)]
X2 = map(lambda x: x**2, X)
print(list(X2))
#> [625, 576, ...]

# Calculation of the famous sum
# of numbers from 1 to 100
# that Gauss solved when he was young.
X = [x for x in range(1, 101)]
sum = reduce(lambda x, y: x + y, X)
print(sum)
#> 5050


# Weighted sum case.
X = [x for x in range(1, 101)]
weights = [0 if x%2 == 0 else 1 for x in range(1, 101)]
sum = reduce(lambda x, y: x + y,
             map(lambda x: x[0] * x[1], zip(X, weights)))
print(sum)
#> 2500
