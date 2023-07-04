import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')

n = 1.0 # amount of substance in mole.
R = 8.314 # constant in J K\textsuperscript{-1} mol\textsuperscript{-1}

# Calculation of pressure based on
# temperature and volume.
def pression(T, V):
    return n * R * T / V

# Calculation of volume based on
# temperature and pressure.
def volume(T, P):
    return n * R * T / P

# Calculation of temperature based on
# pressure and volume.
def temperature(P, V):
    return P * V / (n * R)

# Standard temperature and
# pressure conditions.
T0 = 273.15 # in Kelvin, which is 0° Celsius
P0 = 101325 # in Pascal, which is 1 atmosphere

# With these few functions
# virtual experiments can easily be conducted.

# For example, we can simply obtain the volume
# occupied by one mole of gas under standard
# conditions:
print(volume(T0, P0))
#> 0.022412722427831235 (in litres)

# We can verify that the temperature is
# correct for standard pressure
# and volume:
print(temperature(P0,volume(T0, P0)))
#> 273.15

# Doubling the pressure
# yields the following temperature:
print(temperature(2 * P0,
                  volume(T0, P0)))
#> 546.3

vs = np.linspace(0.01, 1, 100)
plt.plot(vs,
         [pression(T0, v) for v in vs],
         label='')
plt.xlabel('Volume')
plt.ylabel('Pressure')
plt.legend()
plt.show()