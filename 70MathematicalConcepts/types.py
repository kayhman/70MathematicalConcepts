# a is an integer
a = 12
print(type(a))
#> <class 'int'>

# x is a float
x = 3.5
print(type(x))
#> <class 'float'>

# c is a boolean
c = True
print(type(c))
#> <class 'bool'>

# l is a list
# lists can be heterogeneous
l = [1, 2, a, x, c]
print(type(l))
#> <class 'list'>

# A is a set
# unlike lists, sets guarantee uniqueness
# of the elements within it
A = {1, 1, 2, 3, 4, 5, 6}
print(type(A))
#> <class 'set'>

# s is a string
s = 'python'
print(type(s))
#> <class 'str'>

# D is a dictionary
D = {'key1' : 1, 'key2': 2, 'key3': 3}
print(type(D))
#> <class 'dict'>