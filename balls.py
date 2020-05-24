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

coord_x = 10
coord_y = 10
vel_x = 1
vel_y = 2
acc_x = 1

frame_count = 0
while running:
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (100, 100, 100), (coord_x, coord_y), 20)

    # if frame_count % 2 == 0:
    coord_x += vel_x
    coord_y += vel_y

    if coord_x > WIDTH or coord_x < 0:
        vel_x *= -1
    if coord_y > HEIGHT or coord_y < 0:
        vel_y *= -1

    frame_count += 1
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