import random

# The condition is an empty list here.
# It's considered false
condition = []

if not condition:
    print("the condition is true")
else:
    print("the condition is not true")
#> the condition is true

# Here, the condition contains one element
# It's considered true
condition = {1}

if not condition:
    print("the condition is true")
else:
    print("the condition is not true")
#> the condition is not true