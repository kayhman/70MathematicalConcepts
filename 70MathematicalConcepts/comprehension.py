# Building a list of x coordinates.
X = [x - 25 for x in range(0, 51)]
print(X)
#> [-25, -24, ..., 24, 25]

# Y contains the absolute values of the elements in X.
Y = [x if x > 0 else -x for x in X]
print(Y)
#> [25, 24, ..., 24, 25]

# List comprehensions can also be used for filtering.
# Z contains only the non-negative elements of X.
Z = [x for x in X if x >= 0]
print(len(Z))
#> 26
print(Z)
#> [1, 2, 3, ..., 24, 25]

# The same mechanism is available for dictionaries.
tmp = {'key1' : 1, 'key2' : 2, 'key3' : 3}
dct = {key: val for key, val in tmp.items()}
print(dct)
#> {'key1': 1, 'key2': 2, 'key3': 3}

# Filtering is also possible for dictionaries.
dct = {key: val for key, val in tmp.items() if val > 2}
print(dct)
#> {'key3': 3}