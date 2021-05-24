# calculates fourier coefficients from recorder.py for display.py

import config
from math import ceil, cos, sin, pi


# Functions
def summation(n, path):
    c = [0, 0]
    delta = 1/len(path)

    for p in range(len(path)):
        k = 2 * pi * n * (delta * p)
        c[0] += (path[p][0]*cos(k) + path[p][1]*sin(k)) * delta
        c[1] += (path[p][1]*cos(k) - path[p][0]*sin(k)) * delta

    return tuple(c)


def coeff(path):
    vectors = min(ceil(len(path)/2)*2, config.VECTORS)
    c_of_n = []

    for n in range(int(-vectors/2), int(vectors/2)+1):
        c_of_n.append(summation(n, path))

    return c_of_n
