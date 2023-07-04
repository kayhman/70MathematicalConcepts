# This function performs an operation that is impossible between an integer
# and a string
def this_codes_fails():
    a = 12
    b = 'rabbit'
    return a + b

# the type of a variable can change dynamically during the program
var1 = 12
print(type(var1))
#> <class 'int'>
var1 = 'rabbit'
print(type(var1))
#> <class 'str'>

print('everything is fine so far')
#> everything is fine so far
# The interpreter will fail here by raising an exception
print(this_codes_fails())
#> TypeError: unsupported operand type(s) for +: 'int' and 'str'