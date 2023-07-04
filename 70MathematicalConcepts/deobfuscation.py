def mean(xs):
    """
    This function calculates the sum
    of the elements in the array xs.
    """
    sum = 0
    for x in xs:
        sum += x
    return sum / len(xs)

print(mean([1, 2, 3, 4, 5]))
#> 3
