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

coord_x = 100
coord_y = 100
while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0,0,255), (coord_x, coord_y, 50,50))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:

            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                coord_y -= 3
            if event.key == K_DOWN:
                coord_y += 3
            if event.key == K_RIGHT:
                coord_x += 3
            if event.key == K_LEFT:
                coord_x -= 3



pygame.quit()