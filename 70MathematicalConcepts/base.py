# Return the list of digits composing an integer.
# E.g.: digits(123) -> [3, 2, 1]
def digits(n):
    return [int(c) for c in reversed(str(n))]

# from\_base converts an integer n encoded in base b
# to base 10.
def from_base(n, b):
    value = 0
    for (idx, digit) in enumerate(digits(n)):
        # idx: the position of the digit
        # digit: the digit itself
        value += digit * b**idx
    return value

# Compute the value in base 8 of 12.
from_base(12, 8)
# -> $10 = 1 * 8^1 + 2 * 8^0$

# Compute the value in base 8 of 1234.
from_base(1234, 8)
# -> $668 = 1 * 8^3 + 2 * 8^2 + 3 * 8^1 + 4 * 8^0$

# to\_base converts an integer n encoded in base 10
# to base b.
def to_base(n, b):
    digits = [] # will contain the list of digits, in reverse order.
    while n > b:
        digit = n % b
        n = n // b
        digits.append(digit)
    digits.append(n)
    value = 0
    # We reverse and iterate over the list of digits.
    for digit in reversed(digits):
        value = 10 * value + digit
    return value


# Convert 10 in base 10 to base 8.
to_base(10, 8)
# -> $12$ We indeed get the same value as with {\em from\_base}.

# Let's verify that the combination of from\_base and to\_base is the identity.
identity = lambda n, b: from_base(to_base(n, b), b)
identity(12, 8)
# -> $12$ {\em identity} correctly left 12 invariant.

# Same verification, but with the operations in reverse order.
# We don't have a choice of base, as n is necessarily encoded in base 10.
identity = lambda n: to_base(from_base(n, 10), 10)
identity(12)
# -> $12$ {\em identity} correctly left 12 invariant.
