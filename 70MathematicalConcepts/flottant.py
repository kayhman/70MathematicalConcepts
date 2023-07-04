import ctypes
import numpy as np

# Display the code of 42 on 32 bits.
print("{0:32b}".format(42))
# > 00000000000000000000000000101010

# On 16 bits,
# the largest natural number
# is $2^{16}-1 = 65535$.
print("{0:14b}".format(65535))
# > 1111 1111 1111 1111
# There are not enough bits
# to store a larger number.
print(np.uint16(65536))
# > 0


real = 0.3
# Display the first 17 decimal places.
print("{0:.17f}".format(real))
# > 0.29999999999999999

# Floats are encoded in the form of $s \times m \times 2^{e-127}$
# $s$ indicates the sign and is coded on the $1^{st}$ bit
# $e$ is the exponent and is coded on 8 bits
# $m$ is the mantissa and is coded on the following 23 bytes.
print(bin(ctypes.c_uint.from_buffer(ctypes.c_float(real)).value))
# > '0b1111101 00110011001100110011010'

# Let's express our float in base 10
# from its encoding according to the IEEE 754 standard.
print((1.0 + 2.0**-3 +  2.0**-4 + 2.0**-7 + 2.0**-8 + 2.0**-11 + 2.0**-12 + 2.0**-15 + 2.0**-16 + 2.0**-19 + 2.0**-20 + 2.0**-22) * 2.0**-2)
# > 0.30000001192092896

# Likewise, but using the
# built-in Python functions.
significand, exp = np.frexp(real)
print(significand * 2.0**exp)
# > 0.3