from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode([WIDTH, HEIGHT])
running = True

def line(x1, y1, x2, y2, color=(255, 0, 0)):
    pygame.draw.line(screen, color, [x1, y1], [x2, y2], 5)

GRID_SPACE = 30
while running:
    screen.fill((255, 255, 255))

    for i in range(0, WIDTH, GRID_SPACE):
        line(i, 0, i, HEIGHT)

    for i in range(0, HEIGHT, GRID_SPACE):
        line(0, i, WIDTH, i)

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