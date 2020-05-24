from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from math import sin, cos
import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

coord_x = 100
coord_y = 100

count = 0

import random
def r():
    return random.randint(0, 255)
while running:
    # screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (r(), r(), r()), (coord_x, coord_y), 5)
    mouseX, mouseY = pygame.mouse.get_pos()
    coord_x = mouseX + int(sin(count)*40)
    coord_y = mouseY + int(cos(count)*40)
    count += 1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                pass


pygame.quit()


