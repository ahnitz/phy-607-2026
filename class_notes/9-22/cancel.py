import math

for k in range(1, 12):
    x = 10.0 ** -k
    print(k, (1 - math.cos(x)) / x**2, 2 * math.sin(x / 2)**2 / x**2)
