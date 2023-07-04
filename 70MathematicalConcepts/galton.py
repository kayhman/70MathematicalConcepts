import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# This function follows the drop of a ball
# and counts the number of times it chooses the left path.
def galton_drop(depth):
    nb_left = 0
    for i in range(0, depth):
        direction = np.random.choice(['L', 'R'])
        if direction == 'L':
            nb_left += 1
    return nb_left

# This function simulates the throwing
# of $nb_{balls}$ on a Galton board
# with $depth$ levels.
def galton_board(nb_balls, depth):
    counter = {idx: 0 for idx in range(0, depth+1)}
    for ball in range(nb_balls):
        nb_left = galton_drop(depth)
        counter[nb_left] += 1
    # Normalization
    keys = list(counter.keys())
    for key in keys:
        counter[(key - depth/2) / depth] = counter.pop(key) / nb_balls

    return counter

# This function draws a Galton board.
def draw_galton_board(depth):
    X = []
    Y = []
    for step in range(0, depth):
        X += [-step / 2.0 + point for point in range(0,step+1)]
        Y += [-step for _ in range(0,step+1)]

    plt.scatter(X, Y)
    plt.xlabel('Galton Board')
    plt.show()

depth = 30
counter = galton_board(20000, depth)
X = np.linspace(-0.6, 0.6, 100)
plt.bar(counter.keys(), counter.values(), label='number of balls per cell', width=1.0 / (3*depth))
plt.plot(X, [1/math.sqrt(2 * math.pi) * math.exp(-1/2.0 * x**2) for x in X])
plt.xlabel('cells')
plt.legend()
plt.show()
print(max(counter.keys()))

draw_galton_board(10)