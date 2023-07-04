import numpy as np
import random
from itertools import cycle

# Random generator initialization
# is fixed to make the code reproducible.
random.seed(42)

txt = 'python'

def error(candidate, target):
    err = 0
    if len(candidate) < len(target):
        candidate = cycle(candidate)
    for c, t in zip(candidate, target):
        err += (ord(c) - ord(t))**2
    return err

print(error('python', 'python'))
#> 0

print(error('python', 'golang'))
#> 344

def merging(candidateA, candidateB):
    split = random.choice(range(0, max(len(candidateA), len(candidateB))))
    return candidateA[:split] + candidateB[split:]

child = merging('python', 'golang')
print(child)
#> pythog


def mute(candidate):
    if random.random() < 0.5:
        return candidate
    mutation = random.choice(range(0, 26))
    index = random.choice(range(0, len(candidate)))
    replacement = chr(random.choice(range(97, 123)))
    return candidate[:index] + replacement + candidate[index+1:]

mutant = mute('python')
# No mutation this time.
print(mutant)
#> python
mutant = mute('python')
# A mutation here.
print(mutant)
#> pethon


def evolve(population, max_steps):
    for step in range(0, max_steps):
        scores = [error(indiv, 'python') for indiv in population]
        population = [indiv for _, indiv in sorted(zip(scores, population))]
        # Removing the 10 least adapted individuals.
        population = population[:-10]
        for idx in range(0, 10):
            indA = random.choice(population)
            indB = random.choice(population)
            population.append(merging(mute(indA), mute(indB)))
    return population

def random_candidate():
    txt = ""
    for i in range(0, random.randint(4, 8)):
        txt += chr(random.choice(range(97, 123)))
    return txt

population = [random_candidate() for i in range(0, 100)]
print(population)
#> ['vxrc', 'nbacghqt', 'rgwu', 'nhosizay'...
population = evolve(population, 100)
print(population)
#> ['pyrhonzl', 'oyrhon', 'oyrhon', 'oyrhon'...
population = evolve(population, 150)
print(population)
#> ['python', 'python', 'python'...