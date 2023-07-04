import numpy as np

mu = 10
sigma = 3
size = 100000


# This function counts the number of points
# from this normal distribution
# included between the mean and $n$ sigma.
def percentage_n_sigma(n_sigma, n_iter=1):
    counts = []
    for i in range(0, n_iter):
        # s contains $n$ random picks
        # following a normal distribution
        # with a mean of 10 and a standard deviation of 3.
        s = np.random.normal(mu, sigma, size)
        countSigma = 0
        for e in s:
            countSigma += 1 if abs(e - mu) < n_sigma * sigma else 0
        counts += [countSigma]
    return np.mean(counts)

count1Sigma = percentage_n_sigma(1)
print(count1Sigma * 100 / size)
#> 68.54

count2Sigma = percentage_n_sigma(2)
print(count2Sigma * 100 / size)
#> 95.33

count3Sigma = percentage_n_sigma(3)
print(count3Sigma * 100 / size)
#> 99.71

count6Sigma = percentage_n_sigma(6)
print(count6Sigma * 100.0 / size)
#>100.0


# Some outliers are introduced
# in the distribution.
s = list(np.random.normal(mu, sigma, size)) + [100, 1000, 333]

# the 6 sigma filter allows them to be found.
one_sigma_outliers = [x for x in s if abs(x-mu) >= 6 * sigma]
print(one_sigma_outliers)
#> [100, 1000, 333]

def normality_test(samples, mu, sigma, n_sigma):
    countSigma = 0
    for e in s:
        countSigma += 1 if abs(e - mu) < n_sigma * sigma else 0
    return countSigma / len(samples)

# A uniform distribution
# does not pass the normality test
# based on the $n$ sigma.
u = list(np.random.uniform(1, 10, size))
mu = np.mean(u)
sigma = np.std(u)

print(normality_test(u, mu, sigma, 1))
#> 0.25403
print(normality_test(u, mu, sigma, 2))
#> 0.59365
print(normality_test(u, mu, sigma, 3))
#> 0.86571