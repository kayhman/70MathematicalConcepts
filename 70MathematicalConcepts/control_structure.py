import random

# The condition is the result of a test,
# meaning it's an object that can be interpreted
# as a boolean. Two values are possible: true or false
condition = True

# The basic control structure in Python
# takes the following form
if condition:
    # then we execute the code in the following block
    print("the condition is true")
#> the condition is true

# It's also possible to have an alternative
# in case the condition is false. 
# This is what the else keyword allows
if condition:
    # then we execute the code in the following block
    print("the condition is true")
else:
    # otherwise this block executes
    print("the condition is false")
#> the condition is true

# It's possible to include the condition code
# directly on the if line
x = random.random()
if x < 0.5:
    # then we execute the code in the following block
    print(f"{x} is strictly less than 0.5")
else:
    # otherwise this block executes
    print(f"{x} is greater than 0.5")
#> result depends on the value of x

# It's also possible to chain multiple tests with {\em elif}
if x < 0.5:
    # then we execute the code in the following block
    print(f"{x} is strictly less than 0.5")
elif x < 0.6:
    print(f"{x} is between 0.5 and 0.6")
else:
    # otherwise this block executes
    print(f"{x} is greater than 0.5")
#> result depends on the value of x