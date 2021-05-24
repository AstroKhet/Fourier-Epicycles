# File that draws the epicycles given the inputs of constants c_n: Complex

import pygame
import config
from math import cos, sin, pi, sqrt


# Initialization
pygame.init()
clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
pygame.display.set_caption("Fourier Series (Enjoy!)")


# Functions
def vector_add(v1, v2):
    # vector addition of two 2D vectors
    v_sum_0 = v1[0] + v2[0]
    v_sum_1 = v1[1] + v2[1]
    return [v_sum_0, v_sum_1]


def vector_distance(v1, v2):
    # returns the distance between two vectors/coordinates
    return sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)


def translate(a, b):
    # Translates imaginary coordinates to pygame xy coordinates
    x = a * config.WIN_WIDTH
    y = (1 - b) * config.WIN_HEIGHT

    return x, y


def identity(c, n, t):
    # Calculates Euler's identity for c_n cycles
    k = 2 * pi * n * t
    c_real, c_imag = c

    a = c_real*cos(k) - c_imag*sin(k)
    b = c_imag*cos(k) + c_real*sin(k)

    return [a, b]


def fourier(n_values, c_of_n, t, canvas):
    #  Displays a sum of cycle/vectors given a specified t
    epicycles = [(c, n) for c, n in zip(c_of_n, n_values)]
    epicycles = sorted(epicycles, key=lambda e: abs(e[0][0]), reverse=True)  # Sort by magnitude

    # v_a = [0, 0] // vector_alpha or origin vector, not used since it ugly
    v_b = identity(epicycles[0][0], epicycles[0][1], t)  # vector_beta // center of mass

    for i in range(1, len(n_values)):
        # print(translate(*v_a), translate(*v_b))
        v_a = v_b
        v_b = vector_add(v_b, identity(epicycles[i][0], epicycles[i][1], t))

        v_at = translate(*v_a)
        v_bt = translate(*v_b)

        # cycle =
        cycle_radius = vector_distance(v_at, v_bt)
        if cycle_radius >= 1:  # optimization
            pygame.draw.circle(WINDOW, (0, 0, 155, 10), v_at, cycle_radius, width=2)

        pygame.draw.line(WINDOW, (255, 255, 255), v_at, v_bt, width=2)

    v_res = translate(*v_b)
    if v_res not in canvas:
        canvas.append(v_res)

    return canvas


def display(c_of_n, path_len):
    vectors = len(c_of_n)
    n_values = [n - vectors//2 for n in range(vectors)]

    t_delta = 0  # time
    canvas = []  # spots drawn by fourier series

    while True:
        clock.tick(int(1 / config.INTERVAL))
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get():  # Event type
            if event.type == pygame.QUIT:
                return

        canvas = fourier(n_values, c_of_n, t_delta * config.INTERVAL, canvas)
        for i, ink in enumerate(canvas):
            pygame.draw.circle(WINDOW, (255, 255, 0), ink, 1)

            if i > 0:
                pygame.draw.line(WINDOW, (255, 255, 0), canvas[i-1], canvas[i], 3)

        pygame.display.update()

        # still need to fix this time issue here
        t_delta += config.REPLAY_SPEED
        if t_delta >= path_len:
            t_delta = 0
            canvas = []




