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


while running:
    screen.fill((255, 255, 255))


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





'''
s = pygame.Surface((10,100))  # the size of your rect
s.set_alpha(200)                # alpha level
s.fill((255,255,255))           # this fills the entire surface
screen.blit(s, (0,0)) 
pygame.draw.rect(screen, (255,255,255), (200,150,100,50))

pygame.draw.circle(screen, (0), (10, 10), 20)



red = (180, 50, 50)
size = (0, 0, 300, 200)

#drawing an ellipse onto the 
ellipse = pygame.draw.ellipse(surface, red, size)

#new surface variable for clarity (could use our existing though)
#we use the pygame.transform module to rotate the original surface by 45°
surface2 = pygame.transform.rotate(surface, 45)

pygame.draw.circle(screen, (255, 255, 255), (cx, cy), 20)
    if cx < 0 or cx > WIDTH:
        vx *= -1
    if cy < 0 or cy > WIDTH:
        vy *= -1

    cx += vx
    cy += vy

pygame.draw.line(screen, (255, 0, 0), [0, 0], [50,30], 5)
'''