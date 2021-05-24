# records and translates drawing data, returns c_n values for display.py

import pygame
import config

# Initialization
pygame.init()
clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((config.WIN_WIDTH, config.WIN_HEIGHT))
pygame.display.set_caption("Fourier Series (Draw something with one stroke!)")


# Function(s)
def filter_path(path):
    for p in range(len(path)):
        point = path[p]

        a = point[0] / config.WIN_WIDTH
        b = 1 - point[1] / config.WIN_HEIGHT
        path[p] = (a, b)

    if path[-1] != path[0]:
        path.append(path[0])

    return [tuple(point) for point in path]


def recorder():
    path = []  # element = (a, b) in a + bi
    drawn = False

    while True:
        clock.tick(int(1 / config.INTERVAL))

        for event in pygame.event.get():  # Event type
            if event.type == pygame.QUIT:
                return

        point = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(3)[0]:
            drawn = True
            if (not path) or (path[-1] != point):
                path.append(point)
                pygame.draw.circle(WINDOW, (255, 255, 255), point, 1)

                if len(path) > 1:
                    pygame.draw.line(WINDOW, (255, 255, 255), path[-2], path[-1], 3)

                pygame.draw.circle(WINDOW, (255, 0, 0), path[0], 3)  # starting point
                pygame.display.update()
        else:
            if drawn:
                break

    return filter_path(path)
