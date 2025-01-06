import pygame, sys, random, time
from pygame.locals import*
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Man")
screen = pygame.display.set_mode((1200, 700))
last_alien_spawn_time = 0
score = 0
font = pygame.font.SysFont("malgungothic", 40)
font_s = pygame.font.SysFont("gulim.ttc", 95)

space_image = pygame.image.load("images/space.jpg").convert()
alien_image = pygame.image.load("images/alien.png").convert_alpha()
spaceman_image = pygame.image.load("images/spaceman.png").convert_alpha()
missile_image = pygame.image.load("images/missile.png").convert_alpha()
game_over_image = pygame.image.load("images/gameover.png").convert()

class Alien:
    def __init__(self):
        self.y = random.randint(0,630)
        self.x = -100
        self.dx = random.randint(2,4)
        self.dy = random.choice((-1,1))*self.dx

    def move(self):
        self.dx += 0.00000000000001
        self.x += self.dx
        if self.x < 100:
            self.y += self.dy
        if self.x > 100 and self.x < 250:
            self.y += self.dy*(-1)
        if self.x > 250 and self.x < 400:
            self.y += self.dy
        if self.x > 400 and self.x < 550:
            self.y += self.dy*(-1)
        if self.x > 550 and self.x < 700:
            self.y += self.dy
        if self.x > 700 and self.x < 850:
            self.y += self.dy*(-1)
        if self.x > 850 and self.x < 900:
            self.y += self.dy
        if self.x > 900 and self.x < 1050:
            self.y += self.dy*(-1)
        if self.x > 1050 and self.x < 1200:
            self.y += self.dy

    def draw(self):
        screen.blit(alien_image, (self.x, self.y))

    def bounce(self):
        if self.y < 0 or self.y > 660:
            self.dy *= -1

    def touching(self,missile):
        return (self.x+35-missile.x+4)**2+(self.y+22.5-missile.y+10)**2 < 1225

    def off_screen(self):
        return self.x > 1200
    
    def score(self):
        global score
        score += 10

class Spaceman:
    def __init__(self):
        self.y = 350

    def move(self):
        if pressed_keys[K_UP] and self.y > 0:
            self.y -= 5
        if pressed_keys[K_DOWN] and self.y < 600:
            self.y += 5

    def draw(self):
        screen.blit(spaceman_image, (1062, self.y))

    def fire(self):
        missiles.append(Missile(self.y-50))

    def hit_by(self,alien):
        return (
            alien.x > 1030 and
            alien.y > self.y - 15 and
            alien.y < self.y + 70
        )

class Missile:
    def __init__(self,y):
        self.x = 1062
        self.y = y
    
    def move(self):
        self.x -= 10
    
    def off_screen(self):
        return self.x < -8
    
    def draw(self):
        screen.blit(missile_image, (self.x+25,self.y+80))

aliens = []
spaceman = Spaceman()
missiles = []

while 1:
    clock.tick(60)
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            spaceman.fire()

    if time.time() - last_alien_spawn_time > 0.5:
        aliens.append(Alien())
        last_alien_spawn_time = time.time()
    screen.blit(space_image, (0, 0))

    spaceman.move()
    spaceman.draw()

    i = 0
    while i < len(aliens):
        aliens[i].move()
        aliens[i].draw()
        aliens[i].bounce()
        if aliens[i].off_screen():
            del aliens[i]
            i -= 1
        i += 1

    i = 0
    while i < len(missiles):
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].off_screen():
            del missiles[i]
            i -= 1
        i += 1

    i = 0
    while i < len(aliens):
        j = 0
        while j < len(missiles):
            if aliens[i].touching(missiles[j]):
                aliens[i].score()
                del aliens[i]
                del missiles[j]
                i -= 1
                break
            j += 1
        i += 1

    screen.blit(font.render("점수: "+str(score),True,(224, 254, 224)),(5,5))

    for alien in aliens:
        if spaceman.hit_by(alien):
            screen.blit(game_over_image,(0,0))
            screen.blit(font_s.render(str(score),True,(255,255,0)),(650,380))
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                pygame.display.update()

    pygame.display.update()

#alien class에 touching 함수 손봐야 됨
#강화된 alien 1000점 넘을 시 만들자 - 속도 높이기