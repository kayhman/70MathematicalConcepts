from math import floor


# Building the logarithm table
# for numbers from 1.0 to 1e-7.
# The position in the table corresponds to the exponent.
def log_table(min):
  # r is an approximation of e, the Euler's constant.
  # It is the base of the logarithms of our computers.
  r = (1 - 1 / 10**7)
  table = []
  i = 1
  s = 1
  while True:
    table.append(s)
    s = s * r
    i = i + 1
    if s < min:
      break
  return table


# Looking up the logarithm table for the value closest to v.
# The index of this value in the table gives the exponent.
# The method used for searching is dichotomy.
def lookup(table, v):
  up = len(table) - 1
  low = 0
  middle = round((up + low) / 2)
  idx = 1
  while True:
    if v <= table[low] and v > table[middle]:
      # The value is between the beginning and the middle of the table.
      # We narrow the search to this zone.
      up = middle
    else:
      # Otherwise, the value is between the middle and the end of the table.
      # We narrow the search to this zone.
      low = middle

    # We update the middle position.
    middle = round((up + low) / 2)
    if up - low == 1:
      # There is only one value left in the search zone.
      # We have found our exponent.
      return middle
  # If we reach this point, we haven't found anything.
  return -1


ln = log_table(1e-7)
v1 = 0.0004560
v2 = 0.0076890
l1 = lookup(ln, v1)
l2 = lookup(ln, v2)
print(l1, l2, len(ln))
print(ln[l1], ln[l2], ln[0], ln[-1], len(ln))
prod = ln[l1 + l2]
check = v1 * v2

print("log: ", int(floor(prod * 1e14)), ", real: ",
      int(floor(check * 1e14)))
print("error: ", abs(int(floor(prod * 1e14)) - int(floor(check * 1e14))))
# We obtain a very close approximate value.
# > log: 350618389, real : 350618400
