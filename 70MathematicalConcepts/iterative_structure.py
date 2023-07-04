# The most classic form of an iteration loop is as follows:
# it consists of repeating the same code block for $n$ times.
n = 5
for i in range(0, n):
    print(i)
#> 0
#> 1
#> 2
#> 3
#> 4

# Using {\em while} allows to achieve the same result
# with a slightly less readable formulation.
i = 0
while i < 5:
    print(i)
    i += 1
#> 0
#> 1
#> 2
#> 3
#> 4

# Python allows to iterate directly over
# iterable data structures, such as lists.
data = [0, 1, 2, 3, 4]
for i in data:
    print(i)
#> 0
#> 1
#> 2
#> 3
#> 4

# The {\em continue} keyword allows to skip
# directly to the next iteration.
# In the following example, it is used
# to only display even numbers.
for i in range(0, 5):
    if i % 2 == 1:
        # for odd numbers, the loop stops here
        continue
    print(i)
#> 0
#> 2
#> 4

# The {\em break} keyword allows to interrupt
# a loop completely.
# Above, we search for a number in an array,
# and once found, the loop stops.
data = [6, 2, 1, 3, 0, 4, 5]
for d in data:
    if d == 0:
        print("found 0")
        break
# > found 0