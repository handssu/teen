import pygame, sys
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((1600, 950))

while 1:
    pressed_keys = pygame.key.get_pressed
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    pygame.draw.aalines(screen, (255, 255, 108), True, ((16, 30), (44, 30), (20, 10), (30,40), (40, 10)) ,True)

    pygame.display.update()
