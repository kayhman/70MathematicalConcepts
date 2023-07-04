# compound\_interest calculates compound interest
# for a rate $r$
# a number of periods $n$ per year
# and a duration of $d$ years.
def compound_interest(r, n, d):
    return (1 + r/n)**(n*d)

# Gain for a one-year investment,
# at 5\%, with annual compounding.
compound_interest(0.05, 1, 1)
# > 1.05

# Gain for a one-year investment,
# at 5\%, with monthly compounding.
compound_interest(0.05, 12, 1)
# > 1.051161897881733

# What happens when n tends towards infinity?
compound_interest(1.0, 1, 1)
# > 2.0
compound_interest(1.0, 10, 1)
# > 2.5937424601000023
compound_interest(1.0, 100, 1)
# > 2.7048138294215285
compound_interest(1.0, 1000, 1)
# > 2.7169239322355936
compound_interest(1.0, 10000, 1)
# > 2.7181459268249255
compound_interest(1.0, 1000000, 1)
# > 2.7182804690957534


# Calculation of $e^x$ using the Euler method.
def exp_euler(r, max_iter=20):
    # max to avoid floating point overflow.
    fact = 1
    res = 0.0
    r_n = 1
    for n in range (0, max_iter):
        # calculate n! (factorial(n)).
        fact = fact * 1 if n == 0 else n
        res += r_n / fact
        r_n = r * r_n # calculate $x^n$.
    return res
