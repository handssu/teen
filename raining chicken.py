import pygame, sys, random
from pygame.locals import*
pygame.init()
pygame.display.set_caption("Raindrop")
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
raindrop_spawn_time=0
zh_image = pygame.image.load("images/ABChicken.png").convert()

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = -5
        self.speed = random.randint(5, 18)

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > 800

    def draw(self):
        pygame.draw.line(screen, (92, 209, 229), (self.x, self.y), (self.x, self.y+5), 5)

class Staystay:
    def __init__(self):
        self.x = 400
        self.y = 400
    def draw(self):
        screen.blit(zh_image, (self.x, self.y))

raindrops = []
zh = Staystay()
        
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        raindrops.append(Raindrop())
        screen.fill((255, 255, 255))
        zh.draw()
        
        i = 0
        while i <len(raindrops):
            raindrops[i].move()
            raindrops[i].draw()
            if raindrops[i].off_screen():
                del raindrops[i]
                i -= 1
            i += 1

        pygame.display.update()
