import pygame, sys
from pygame.locals import*
pygame.init()
pygame.display.set_caption("Joy program")
screen = pygame.display.set_mode((640, 480))
xpos = 50
ypos = 200
clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_RIGHT]:
            xpos += 5
        if pressed_keys[K_LEFT]:
            xpos -= 5
        if pressed_keys[K_UP] :
            ypos -= 5
        if pressed_keys[K_DOWN] :
            ypos += 5
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 228, 0), (xpos, ypos), 20)
        pygame.display.update()
