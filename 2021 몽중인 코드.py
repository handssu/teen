import pygame, sys, random, time
from pygame.locals import*
pygame.init()
screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()
menu = "home"
font1 = pygame.font.SysFont("malgungothic", 60)
mc_lives=(
    pygame.image.load("images/life1.png").convert_alpha(),
    pygame.image.load("images/life2.png").convert_alpha(),
    pygame.image.load("images/life3.png").convert_alpha()
    )

home_image = pygame.image.load("images/home.png").convert()
apilog_image = pygame.image.load("images/apilog.jpg").convert()
apilog2_image = pygame.image.load("images/apilog2.png").convert()
stage1_image = pygame.image.load("images/stage1.jpg").convert()
stage1_bed_image = pygame.image.load("images/stage1_bed.jpg").convert()
stage1_book_image = pygame.image.load("images/stage1_book.jpg").convert()
stage1_flower_image = pygame.image.load("images/stage1_flower.jpg").convert()
stage2_image = pygame.image.load("images/stage2.png").convert()
stage3_image = pygame.image.load("images/stage3.jpg").convert()
stage3_before_image = pygame.image.load("images/stage3_before.png").convert()
add_image = pygame.image.load("images/add.png").convert()
add_bed_image = pygame.image.load("images/add_bed.png").convert()
add_book_image = pygame.image.load("images/add_book.png").convert()
add2_image = pygame.image.load("images/add2.png").convert()
add3_image = pygame.image.load("images/add3.png").convert()
star_image = pygame.image.load("images/star.png").convert_alpha()
star1_image = pygame.image.load("images/star1.png").convert_alpha()
star2_image = pygame.image.load("images/star2.png").convert_alpha()
star3_image = pygame.image.load("images/star3.png").convert_alpha()
star4_image = pygame.image.load("images/star4.png").convert_alpha()
twinkle_star_image = pygame.image.load("images/twinkle_star.png").convert_alpha()
addone_image = pygame.image.load("images/1add.png").convert()
addtwo_image = pygame.image.load("images/2add.png").convert()
addthree_image = pygame.image.load("images/3add.png").convert()
addfour_image = pygame.image.load("images/4add.png").convert()
gameover_image = pygame.image.load("images/gameover.jpg").convert()
finish1_image = pygame.image.load("images/finish1.jpg").convert()
finish2_image = pygame.image.load("images/finish2.jpg").convert()
finish3_image = pygame.image.load("images/finish3.jpg").convert()
fin_image = pygame.image.load("images/fin.png").convert()

class MC:
    def __init__(self):
        self.lives = 3
    def harm(self):
        self.lives -= 1

mc = MC()

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
    
    if menu == "home":
        screen.blit(home_image, (0, 0))
        txt100000 = font1.render("START", True, (255, 255, 255))
        buttonrect100000 = pygame.Rect((500, 400), txt100000.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect100000)
        screen.blit(txt100000, (500, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect100000.collidepoint(pygame.mouse.get_pos()):
            menu = "apilog"

    if menu == "apilog":
        screen.blit(apilog_image, (0, 0))
        if pressed_keys[K_1]:
            menu = "apilog2"

    if menu == "apilog2":
        screen.blit(apilog2_image, (0, 0))
        if pressed_keys[K_2]:
            menu = "stage1"

    if menu == "stage1":
        screen.blit(stage1_image, (0, 0))
        screen.blit(star1_image, (480, 30))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(480, 30, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "clock"
        screen.blit(star2_image, (200, 600))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(200, 600, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "bed"
        screen.blit(star3_image, (70, 0))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(70, 0, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "book"
        screen.blit(star4_image, (950, 200))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(950, 200, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "flower"

    if menu == "clock":
        screen.blit(add_image, (0, 0))
        txt1 = font1.render("시침의 위치를 바꿔볼까?", True, (255, 255, 255))
        screen.blit(txt1, (200, 150))
        
        txt2 = font1.render("YES", True, (255, 255, 255))
        buttonrect2 = pygame.Rect((400, 400), txt2.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect2)
        screen.blit(txt2, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect2.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "stage1"
        
        txt3 = font1.render("NO", True, (255, 255, 255))
        buttonrect3 = pygame.Rect((700, 400), txt3.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect3)
        screen.blit(txt3, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect3.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1"

    if menu == "bed":
        screen.blit(add_image, (0, 0))
        txt4 = font1.render("이불을 정리할까?", True, (255, 255, 255))
        screen.blit(txt4, (200, 150))
        
        txt5 = font1.render("YES", True, (255, 255, 255))
        buttonrect5 = pygame.Rect((400, 400), txt5.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect5)
        screen.blit(txt5, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect5.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1_bed"
        
        txt6 = font1.render("NO", True, (255, 255, 255))
        buttonrect6 = pygame.Rect((700, 400), txt6.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect6)
        screen.blit(txt6, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect6.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1"

    if menu == "stage1_bed:":
        screen.blit(stage1_bed_image, (0, 0))
        screen.blit(star1_image, (480, 30))
        screen.blit(star2_image, (200, 600))
        screen.blit(star3_image, (70, 0))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(70, 0, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "book"
        screen.blit(star4_image, (950, 200))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(950, 200, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "flower"

    if menu == "book":
        screen.blit(add_bed_image, (0, 0))
        txt7 = font1.render("다른 책을 꽂을까?", True, (255, 255, 255))
        screen.blit(txt7, (200, 150))
        
        txt8 = font1.render("YES", True, (255, 255, 255))
        buttonrect8 = pygame.Rect((400, 400), txt8.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect8)
        screen.blit(txt8, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect8.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1_book"
        
        txt9 = font1.render("NO", True, (255, 255, 255))
        buttonrect9 = pygame.Rect((700, 400), txt9.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect9)
        screen.blit(txt9, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect9.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1_bed"

    if menu == "stage1_book:":
        screen.blit(stage1_book_image, (0, 0))
        screen.blit(star1_image, (480, 30))
        screen.blit(star2_image, (200, 600))
        screen.blit(star3_image, (70, 0))
        screen.blit(star4_image, (950, 200))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(950, 200, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "flower"

    if menu == "flower":
        screen.blit(add_book_image, (0, 0))
        txt10 = font1.render("꽃 하나를 꽂을까?", True, (255, 255, 255))
        screen.blit(txt10, (200, 150))
        
        txt11 = font1.render("YES", True, (255, 255, 255))
        buttonrect11 = pygame.Rect((400, 400), txt11.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect11)
        screen.blit(txt11, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect11.collidepoint(pygame.mouse.get_pos()):
            menu = "stage2"
        
        txt12 = font1.render("NO", True, (255, 255, 255))
        buttonrect12 = pygame.Rect((700, 400), txt12.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect12)
        screen.blit(txt12, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect12.collidepoint(pygame.mouse.get_pos()):
            menu = "stage1_book"

    if menu == "stage2":
        screen.blit(stage2_image, (0, 0))
        screen.blit(star1_image, (200, 200))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(200, 200, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "lighter"
        screen.blit(star2_image, (300, 600))
        screen.blit(star3_image, (900, 350))
        screen.blit(star4_image, (800, 150))

    if menu == "lighter":
        screen.blit(add2_image, (0, 0))
        txt13 = font1.render("책상 밑을 조사할까?", True, (255, 255, 255))
        screen.blit(txt13, (200, 150))
        
        txt14 = font1.render("YES", True, (255, 255, 255))
        buttonrect14 = pygame.Rect((400, 400), txt14.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect14)
        screen.blit(txt14, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect14.collidepoint(pygame.mouse.get_pos()):
            menu = "lighter_add"
        
        txt15 = font1.render("NO", True, (255, 255, 255))
        buttonrect15 = pygame.Rect((700, 400), txt15.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect15)
        screen.blit(txt15, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect15.collidepoint(pygame.mouse.get_pos()):
            menu = "stage2"

    if menu == "lighter_add":
        screen.blit(addone_image, (0, 0))
        screen.blit(star1_image, (200, 200))
        screen.blit(star2_image, (300, 600))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(300, 600, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "crown"
        screen.blit(star3_image, (900, 350))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(900, 250, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "triangle"
        screen.blit(star4_image, (800, 150))

    if menu == "crown":
        screen.blit(add2_image, (0, 0))
        txt16 = font1.render("카페트 밑을 조사할까?", True, (255, 255, 255))
        screen.blit(txt16, (200, 150))
        
        txt17 = font1.render("YES", True, (255, 255, 255))
        buttonrect17 = pygame.Rect((400, 400), txt17.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect17)
        screen.blit(txt17, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect17.collidepoint(pygame.mouse.get_pos()):
            menu = "crown_add"
        
        txt18 = font1.render("NO", True, (255, 255, 255))
        buttonrect18 = pygame.Rect((700, 400), txt18.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect18)
        screen.blit(txt18, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect18.collidepoint(pygame.mouse.get_pos()):
            menu = "lighter_add"

    if menu == "crown_add":
        screen.blit(addtwo_image, (0, 0))
        screen.blit(star1_image, (200, 200))
        screen.blit(star2_image, (300, 600))
        screen.blit(star3_image, (900, 350))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(900, 350, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "triangle"
        screen.blit(star4_image, (800, 150))

    if menu == "triangle":
        screen.blit(add2_image, (0, 0))
        txt19 = font1.render("소파를 조사할까?", True, (255, 255, 255))
        screen.blit(txt19, (200, 150))
        
        txt20 = font1.render("YES", True, (255, 255, 255))
        buttonrect20 = pygame.Rect((400, 400), txt20.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect20)
        screen.blit(txt20, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect20.collidepoint(pygame.mouse.get_pos()):
            menu = "triangle_add"
        
        txt21 = font1.render("NO", True, (255, 255, 255))
        buttonrect21 = pygame.Rect((700, 400), txt21.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect21)
        screen.blit(txt21, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect21.collidepoint(pygame.mouse.get_pos()):
            menu = "crown_add"

    if menu == "triangle_add":
        screen.blit(addthree_image, (0, 0))
        screen.blit(star1_image, (200, 200))
        screen.blit(star2_image, (300, 600))
        screen.blit(star3_image, (900, 350))
        screen.blit(star4_image, (800, 150))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(800, 150, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "circle"

    if menu == "circle":
        screen.blit(add2_image, (0, 0))
        txt22 = font1.render("서랍을 조사할까?", True, (255, 255, 255))
        screen.blit(txt22, (200, 150))
        
        txt23 = font1.render("YES", True, (255, 255, 255))
        buttonrect23 = pygame.Rect((400, 400), txt23.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect23)
        screen.blit(txt23, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect23.collidepoint(pygame.mouse.get_pos()):
            menu = "circle_add"
        
        txt24 = font1.render("NO", True, (255, 255, 255))
        buttonrect24 = pygame.Rect((700, 400), txt24.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect24)
        screen.blit(txt24, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect24.collidepoint(pygame.mouse.get_pos()):
            menu = "triangle_add"

    if menu == "circle_add":
        screen.blit(addfour_image, (0, 0))
        screen.blit(star_image, (650, 150))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(650, 150, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "put"

    if menu == "put":
        screen.blit(add2_image, (0, 0))
        txt25 = font1.render("조각들을 끼울까?", True, (255, 255, 255))
        screen.blit(txt25, (200, 150))
        
        txt26 = font1.render("YES", True, (255, 255, 255))
        buttonrect26 = pygame.Rect((400, 400), txt26.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect26)
        screen.blit(txt26, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect26.collidepoint(pygame.mouse.get_pos()):
            menu = "stage3_before"
        
        txt27 = font1.render("NO", True, (255, 255, 255))
        buttonrect27 = pygame.Rect((700, 400), txt27.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect27)
        screen.blit(txt27, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect27.collidepoint(pygame.mouse.get_pos()):
            menu = "circle_add"

    if menu == "stage3_before":
        screen.blit(stage3_before_image, (0, 0))
        screen.blit(star_image, (20, 550))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(20, 550, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "stage3_before2"

    if menu == "stage3_before2":
        screen.blit(stage3_before_image, (0, 0))
        txt28 = font1.render("라이터를 사용할까?", True, (255, 255, 255))
        screen.blit(txt28, (200, 150))
        
        txt29 = font1.render("YES", True, (255, 255, 255))
        buttonrect29 = pygame.Rect((400, 400), txt29.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect29)
        screen.blit(txt29, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect29.collidepoint(pygame.mouse.get_pos()):
            menu = "stage3"
        
        txt30 = font1.render("NO", True, (255, 255, 255))
        buttonrect30 = pygame.Rect((700, 400), txt30.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect30)
        screen.blit(txt30, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect30.collidepoint(pygame.mouse.get_pos()):
            menu = "stage3_before"

    if menu == "stage3":
        screen.blit(stage3_image, (0, 0))
        screen.blit(twinkle_star_image, (0, 0))
        if pygame.mouse.get_pressed()[0] and pygame.Rect(0, 0, 100, 100).collidepoint(pygame.mouse.get_pos()):
            menu = "Q1_before"
        

    if menu == "Q1_before":
        screen.blit(add3_image, (0, 0))
        txt111 = font1.render("그럼 시작해 볼까요?", True, (255, 255, 255))
        screen.blit(txt111, (200, 150))
        
        txt1111 = font1.render("네!!!!!!!!!!!!!", True, (255, 255, 255))
        buttonrect1111 = pygame.Rect((400, 400), txt1111.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect1111)
        screen.blit(txt1111, (400, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect1111.collidepoint(pygame.mouse.get_pos()):
            menu = "Q1"
        
        txt222 = font1.render("아뇨.", True, (255, 255, 255))
        buttonrect222 = pygame.Rect((700, 400), txt222.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect222)
        screen.blit(txt222, (700, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect222.collidepoint(pygame.mouse.get_pos()):
            menu = "stage3"
            
    if menu == "Q1":
        screen.blit(add3_image, (0, 0))
        txt31 = font1.render("TG는 무엇의 약자인가요?", True, (255, 255, 255))
        screen.blit(txt31, (150, 100))
        
        txt32 = font1.render("1. Technology Ggirickggicick\n(테크놀로지 끼릭끼릭)", True, (255, 255, 255))
        buttonrect32 = pygame.Rect((200, 250), txt32.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect32)
        screen.blit(txt32, (200, 250))
        if pygame.mouse.get_pressed()[0] and buttonrect32.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q1"
        
        txt33 = font1.render("2. Technology Growth\n(기술 성장)", True, (255, 255, 255))
        buttonrect33 = pygame.Rect((200, 350), txt33.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect33)
        screen.blit(txt33, (200, 450))
        if pygame.mouse.get_pressed()[0] and buttonrect33.collidepoint(pygame.mouse.get_pos()):
            menu = "A1"

        txt34 = font1.render("3. Tell me Gorilla\n(나한테 말해줘 고릴라야)", True, (255, 255, 255))
        buttonrect34 = pygame.Rect((200, 450), txt34.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect34)
        screen.blit(txt34, (200, 650))
        if pygame.mouse.get_pressed()[0] and buttonrect34.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q1"

    if menu == "A1":
        screen.blit(add3_image, (0, 0))
        txt35 = font1.render("""맞습니다! TG는 Technology Growth의\n약자로 기술을 배움으로써 성장하겠\n다는 의미로 지었습니다만 사실\n기술로 끼릭끼릭\n(Technology Ggirickggrick)을\n하고 싶지만 차마 실천하지 못해서\n틀어서 지은 이름이랍니다 ㅋㅋㅋ""", True, (255, 255, 255))
        screen.blit(txt35, (100, 100))

        txt36 = font1.render("다음 질문으로", True, (255, 255, 255))
        buttonrect36 = pygame.Rect((400, 600), txt36.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect36)
        screen.blit(txt36, (400, 600))
        if pygame.mouse.get_pressed()[0] and buttonrect36.collidepoint(pygame.mouse.get_pos()):
            menu = "Q2"
        
    if menu == "Q2":
        screen.blit(add3_image, (0, 0))
        txt37 = font1.render("TG 동아리와 관련된 계열은?", True, (255, 255, 255))
        screen.blit(txt37, (150, 100))
        
        txt38 = font1.render("1. 교육계열", True, (255, 255, 255))
        buttonrect38 = pygame.Rect((250, 200), txt38.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect38)
        screen.blit(txt38, (250, 200))
        if pygame.mouse.get_pressed()[0] and buttonrect38.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q2"
        
        txt39 = font1.render("2. 자연과학계열", True, (255, 255, 255))
        buttonrect39 = pygame.Rect((250, 300), txt39.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect39)
        screen.blit(txt39, (250, 300))
        if pygame.mouse.get_pressed()[0] and buttonrect39.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q2"

        txt40 = font1.render("3. 답뭐계열", True, (255, 255, 255))
        buttonrect40 = pygame.Rect((250, 400), txt40.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect40)
        screen.blit(txt40, (250, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect40.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q2"

        txt41 = font1.render("4. 공학계열", True, (255, 255, 255))
        buttonrect41 = pygame.Rect((250, 500), txt41.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect41)
        screen.blit(txt41, (250, 500))
        if pygame.mouse.get_pressed()[0] and buttonrect41.collidepoint(pygame.mouse.get_pos()):
            menu = "A2"
        
        txt42 = font1.render("5. 예체능계열", True, (255, 255, 255))
        buttonrect42 = pygame.Rect((250, 600), txt42.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect42)
        screen.blit(txt42, (250, 600))
        if pygame.mouse.get_pressed()[0] and buttonrect42.collidepoint(pygame.mouse.get_pos()):
            mc.harm()
            menu = "Q2"

    if menu == "A2":
        screen.blit(add3_image, (0, 0))
        txt43 = font1.render("""맞습니다! TG는 이름에서부터\n알 수 있듯이 전체적으로 관련된\n계열은 공학 계열이나 활동은\n동아리원들의 진로에 맞춰 유연하게\n하기 때문에 다른 계열의 진로를\n가진 학생들도 동아리 활동 세부 능력\n특기사항을 진로에 맞게\n작성할 수 있습니다!""", True, (255, 255, 255))
        screen.blit(txt43, (100, 100))

        txt44 = font1.render("다음 질문으로", True, (255, 255, 255))
        buttonrect44 = pygame.Rect((400, 600), txt44.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect44)
        screen.blit(txt44, (400, 600))
        if pygame.mouse.get_pressed()[0] and buttonrect44.collidepoint(pygame.mouse.get_pos()):
            menu = "Q3"

    if menu == "Q3":
        screen.blit(add3_image, (0, 0))
        txt45 = font1.render("숫자 5가 제일 싫어하는 집은?", True, (255, 255, 255))
        screen.blit(txt45, (150, 100))
        
        txt46 = font1.render("1. 우리집", True, (255, 255, 255))
        buttonrect46 = pygame.Rect((200, 250), txt46.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect46)
        screen.blit(txt46, (300, 400))
        if pygame.mouse.get_pressed()[0] and buttonrect46.collidepoint(pygame.mouse.get_pos()):
            menu = "Q3"
        
        txt47 = font1.render("2. 오페라하우스", True, (255, 255, 255))
        buttonrect47 = pygame.Rect((200, 350), txt47.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect47)
        screen.blit(txt47, (200, 350))
        if pygame.mouse.get_pressed()[0] and buttonrect47.collidepoint(pygame.mouse.get_pos()):
            menu = "A3"

        txt48 = font1.render("3. 오 님 좀 짱인듯 집)", True, (255, 255, 255))
        buttonrect48 = pygame.Rect((200, 450), txt48.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect48)
        screen.blit(txt48, (200, 450))
        if pygame.mouse.get_pressed()[0] and buttonrect48.collidepoint(pygame.mouse.get_pos()):
            menu = "Q3"

    if menu == "A3":
        screen.blit(add3_image, (0, 0))
        txt49 = font1.render("""맞습니다! 5는 오페라하우스\n(5를 패라 집)을 싫어합니다\n우리집을 싫어할 리는 없고\n오 님 좀 짱인듯 집은 어디일까요..?""", True, (255, 255, 255))
        screen.blit(txt49, (100, 100))

        txt50 = font1.render("마지막으로", True, (255, 255, 255))
        buttonrect50 = pygame.Rect((400, 600), txt50.get_size())
        pygame.draw.rect(screen, (72, 72, 72), buttonrect50)
        screen.blit(txt50, (400, 600))
        if pygame.mouse.get_pressed()[0] and buttonrect50.collidepoint(pygame.mouse.get_pos()):
            menu = "Fin1"

    if menu == "Fin1":
        screen.blit(finish1_image, (0,0))
        if pressed_keys[K_3]:
            menu = "Fin2"

    if menu == "Fin2":
        screen.blit(finish1_image, (0,0))
        if pressed_keys[K_4]:
            menu = "Fin3"

    if menu == "Fin3":
        screen.blit(finish1_image, (0,0))
        if pressed_keys[K_5]:
            menu = "Fin"

    if menu == "Fin":
        screen.blit(fin_image, (0,0))
        
    screen.blit(mc_lives[mc.lives-1], (900, 600))
    if mc.lives == 0:
        menu = "gameover"
    if menu == "gameover":
        screen.blit(gameover_image, (0, 0))
        if pygame.mouse.get_pressed()[0] and pygame.Rect((555, 444), (333, 88)).collidepoint(pygame.mouse.get_pos()):
            menu = "apilog"
    
    pygame.display.update()
