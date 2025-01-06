import pygame, sys
from pygame.locals import*
pygame.init()
pygame.display.set_caption("박준용 선생님")
screen = pygame.display.set_mode((1280, 758))
clock = pygame.time.Clock()

fishing_image = pygame.image.load("images/fishing.png").convert()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    screen.blit(fishing_image, (0, 0))

    pygame.display.update()

pygame.display.update()
