# This line won't be understood 
# because it starts with a space.
# Indentation is incorrect
variable_2 = 2
#> IndentationError: unexpected indent

# This loop calculates the sum of numbers from 1 to 100
# using brute force, unlike what Gauss 
# did when he was a young student
sum = 0
for i in range(1, 101):
    # this block, identified by the 4 character indentation
    # is executed as many times as the loop dictates
    sum += i

print(sum)
# > 5050

# A function's body is always defined
# within an indented block
def gauss_sum():
    sum = 0
    for i in range(1, 101):
        # this block, identified by the 4 character indentation
        # is executed as many times as the loop dictates
        sum += i
    return sum
# the function block ends here

print(gauss_sum())
# > 5050