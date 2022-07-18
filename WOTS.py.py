import json
import os
import random
import pygame
from pygame.locals import *

outc = False
inc = False
safe = False
apnum = 0
apnumst = str(apnum)
bigaps = False
em2 = "None"
global em3
em3 = "None"

def outcT():
    global outc
    outc = True
def outcF():
    global outc
    outc = False
def incT():
    global inc
    inc = True
def incF():
    global inc
    inc = False
def safeT():
    global safe
    safe = True
def safeF():
    global safe
    safe = False
def passenT():
    global passengerstat
    passengerstat = True
def reloadpass():
    global apnum
    global apnumst
    apnumst = str(apnum)
    if apnumst == "1":
        Text1o = font1.render(apnumst+" passenger", True, BLACK)
    else:
        Text1o = font1.render(apnumst+" passengers", True, BLACK)
    Text1oRect = Text1o.get_rect()
    Text1oRect.bottomright = (490, 21)
def passmethod():
    global em2
    global minimapos2
    global minimapos2rect
    em1 = ("Aero1", "Aero2", "Aero3", "Aero4", "Aero5", "Aero6")
    em2 = random.choice(em1)
    global apnum
    apnum = random.randint(1, 200)
    reloadpass()
    print (em2)
    if em2 == "Aero1":
        em3 = "Airport 1"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (414,402)
        xopos = 411
        yopos = 402
    if em2 == "Aero2":
        em3 = "Airport 2"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (451,412)
        xopos = 448
        yopos = 412
    if em2 == "Aero3":
        em3 = "Airport 3"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (477,429)
        xopos = 476
        yopos = 426
    if em2 == "Aero4":
        em3 = "Airport 4"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (403,455)
        xopos = 402
        yopos = 452
    if em2 == "Aero5":
        em3 = "Airport 5"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (412,470)
        xopos = 411
        yopos = 467
    if em2 == "Aero6":
        em3 = "Airport 6"
        textiii = font1.render(em3, True, BLACK)
        minimapos2rect.center = (464,460)
        xopos = 461
        yopos = 460
def bigapsT():
    global bigaps
    bigaps = True
def bigapsF():
    global bigaps
    bigaps = False


WIDTH = 500
HEIGHT = 500
WH = WIDTH,HEIGHT
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DODGERBLUE = (30, 144,255)
MAGENTA = (255, 0, 255)
GRAY = (195, 195, 195)
RCOLORL = (RED, GREEN, GRAY, WHITE, DODGERBLUE)
RCOLOR = random.choice(RCOLORL)


class Plane1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane1Uimg
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        global Plane1Rect
        Plane1Rect = self.rect
        Plane1Rect.x = self.rect.x
        Plane1Rect.y = self.rect.y
        Plane1Rect.center = self.rect.center
        Plane1Rect.top = self.rect.top
        Plane1Rect.bottom = self.rect.bottom
        Plane1Rect.left = self.rect.left
        Plane1Rect.right = self.rect.right
    def update(self):
        if safe == False:
            keys1 = pygame.key.get_pressed()
            if keys1[K_UP]:
                self.image = plane1Uimg
                if oiro == "Aero4":
                    if Plane1Rect.x > 417:
                        if Plane1Rect.y > 382:
                            Plane1Rect.y -= 2
                        if Plane1Rect.y > 254 and Plane1Rect.y < 384:
                            Plane1Rect.y -= 4
                        if Plane1Rect.y > 126 and Plane1Rect.y < 256:
                            Plane1Rect.y -= 6
                        if Plane1Rect.y < 128:
                            Plane1Rect.y -= 8
                if oiro == "Aero6":
                    if Plane1Rect.x > 450:
                        if Plane1Rect.y > 382:
                            Plane1Rect.y -= 2
                        if Plane1Rect.y > 254 and Plane1Rect.y < 384:
                            Plane1Rect.y -= 4
                        if Plane1Rect.y > 126 and Plane1Rect.y < 256:
                            Plane1Rect.y -= 6
                        if Plane1Rect.y < 128:
                            Plane1Rect.y -= 8
                    else:
                        Plane1Rect.y -= 2
                else:
                    self.rect.y -= 2
                if inc == True:
                    print ("Your Y position on the Airport : ", self.rect.y)
            if keys1[K_DOWN]:
                self.image = plane1Dimg
                self.rect.y += 2
                if inc == True:
                    print ("Your Y position on the Airport : ", self.rect.y)
            if keys1[K_RIGHT]:
                self.image = plane1Rimg
                self.rect.x += 2
                if inc == True:
                    print ("Your X position on the Airport : ", self.rect.x)
            if keys1[K_LEFT]:
                self.image = plane1Limg
                if oiro == "Aero1":
                    if Plane1Rect.y > 400:
                        if Plane1Rect.x > 382:
                            Plane1Rect.x -= 2
                        if Plane1Rect.x > 254 and Plane1Rect.x < 384:
                            Plane1Rect.x -= 4
                        if Plane1Rect.x > 126 and Plane1Rect.x < 256:
                            Plane1Rect.x -= 6
                        if Plane1Rect.x < 128:
                            Plane1Rect.x -= 8
                    else:
                        self.rect.x -= 2
                if oiro == "Aero2":
                    if Plane1Rect.y < 37:
                        if Plane1Rect.x > 382:
                            Plane1Rect.x -= 2
                        if Plane1Rect.x > 254 and Plane1Rect.x < 384:
                            Plane1Rect.x -= 4
                        if Plane1Rect.x > 126 and Plane1Rect.x < 256:
                            Plane1Rect.x -= 6
                        if Plane1Rect.x < 128:
                            Plane1Rect.x -= 8
                    else:
                        self.rect.x -= 2
                if oiro == "Aero3":
                    if Plane1Rect.y < 267 and Plane1Rect.y > 215:
                        if Plane1Rect.x > 382:
                            Plane1Rect.x -= 2
                        if Plane1Rect.x > 254 and Plane1Rect.x < 384:
                            Plane1Rect.x -= 4
                        if Plane1Rect.x > 126 and Plane1Rect.x < 256:
                            Plane1Rect.x -= 6
                        if Plane1Rect.x < 128:
                            Plane1Rect.x -= 8
                    else:
                        self.rect.x -= 2
                if oiro == "Aero4":
                    self.rect.x -= 2
                if oiro == "Aero5":
                    if Plane1Rect.y > 429:
                        if Plane1Rect.x > 382:
                            Plane1Rect.x -= 2
                        if Plane1Rect.x > 254 and Plane1Rect.x < 384:
                            Plane1Rect.x -= 4
                        if Plane1Rect.x > 126 and Plane1Rect.x < 256:
                            Plane1Rect.x -= 6
                        if Plane1Rect.x < 128:
                            Plane1Rect.x -= 8
                    else:
                        self.rect.x -= 2
                if oiro == "Aero6":
                    self.rect.x -= 2
                if inc == True:
                    print ("Your Y position on the Airport : ", self.rect.x)
            if keys1[K_UP] and keys1[K_LEFT]:
                self.image = plane1ULimg
            if keys1[K_UP] and keys1[K_RIGHT]:
                self.image = plane1URimg
            if keys1[K_DOWN] and keys1[K_LEFT]:
                self.image = plane1DLimg
            if keys1[K_DOWN] and keys1[K_RIGHT]:
                self.image = plane1DRimg


airport = pygame.Surface((275,65))
airportrect = airport.get_rect()
airportrect.center = (275, 151)

garage = pygame.Surface((79,46))
garagerect = garage.get_rect()
garagerect.center = (419, 64)

ct = pygame.Surface((36, 38))
ctr = ct.get_rect()
ctr.center = (443, 149)

airport2 = pygame.Surface((65, 275))
airport2rect = airport2.get_rect()
airport2rect.topleft = (4, 219)

garage2 = pygame.Surface((46, 77))
garage2rect = garage2.get_rect()
garage2rect.topleft = (246, 420)

ct2 = pygame.Surface((37, 35))
ctr2 = ct2.get_rect()
ctr2.topleft = (16, 171)

airport3 = pygame.Surface((275, 65))
airport3rect = airport3.get_rect()
airport3rect.topleft = (102, 426)

garage3 = pygame.Surface((45, 77))
garage3rect = garage3.get_rect()
garage3rect.topleft = (23, 412)

airport41 = pygame.Surface((275, 65))
airport41rect = airport41.get_rect()
airport41rect.topleft = (103, 2)

airport42 = pygame.Surface((275, 65))
airport42rect = airport42.get_rect()
airport42rect.topleft = (107, 433)

ct4 = pygame.Surface((29, 30))
ctr4 = ct4.get_rect()
ctr4.topleft = (393, 38)

airport5 = pygame.Surface((275, 65))
airport5rect = airport5.get_rect()
airport5rect.topleft = (29, 18)

garage51 = pygame.Surface((45, 65))
garage51rect = garage51.get_rect()
garage51rect.topleft = (333, 20)

garage52 = pygame.Surface((45, 65))
garage52rect = garage52.get_rect()
garage52rect.topleft = (419, 19)

cs6 = pygame.Surface((144, 80))
cs6rect = cs6.get_rect()
cs6rect.topleft = (69, 38)

mac61 = pygame.Surface((29, 9))
mac61rect = mac61.get_rect()
mac61rect.topleft = (225, 52)

mac62 = pygame.Surface((20, 10))
mac62rect = mac62.get_rect()
mac62rect.topleft = (235, 75)

garage6 = pygame.Surface((77, 46))
garage6rect = garage6.get_rect()
garage6rect.topleft = (5, 155)

airport6 = pygame.Surface((66, 276))
airport6rect = airport6.get_rect()
airport6rect.topleft = (2, 218)

minimapos = pygame.Surface((2, 2))
minimapos.fill(RED)
minimaposrect = minimapos.get_rect()
xopos = 10000
yopos = 10000
minimaposrect.topleft = (xopos, yopos)

minimapos2 = pygame.Surface((6, 6))
minimapos2.fill(MAGENTA)
minimapos2rect = minimapos2.get_rect()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wings of the Sky")
filedir = os.path.dirname(__file__)
game_folder = os.path.join(filedir, 'assets')
bin_folder = os.path.join(game_folder, 'bins')
bino = os.path.join(bin_folder, 'bin.json')
islandimg = pygame.image.load(os.path.join(game_folder, 'Island.png'))
righto = islandimg.get_rect().right
downo = islandimg.get_rect().bottom
airport1img = pygame.image.load(os.path.join(game_folder, 'Airport1.png'))
airport2img = pygame.image.load(os.path.join(game_folder, 'Airport2.png'))
airport3img = pygame.image.load(os.path.join(game_folder, 'Airport3.png'))
airport4img = pygame.image.load(os.path.join(game_folder, 'Airport4.png'))
airport5img = pygame.image.load(os.path.join(game_folder, 'Airport5.png'))
airport6img = pygame.image.load(os.path.join(game_folder, 'Airport6.png'))
plane1Uimg = pygame.image.load(os.path.join(game_folder, 'plane1U.png'))
plane1Dimg = pygame.image.load(os.path.join(game_folder, 'plane1D.png'))
plane1Limg = pygame.image.load(os.path.join(game_folder, 'plane1L.png'))
plane1Rimg = pygame.image.load(os.path.join(game_folder, 'plane1R.png'))
plane1ULimg = pygame.image.load(os.path.join(game_folder, 'plane1UL.png'))
plane1URimg = pygame.image.load(os.path.join(game_folder, 'plane1UR.png'))
plane1DLimg = pygame.image.load(os.path.join(game_folder, 'plane1DL.png'))
plane1DRimg = pygame.image.load(os.path.join(game_folder, 'plane1DR.png'))
enterkeyimg = pygame.image.load(os.path.join(game_folder, 'enterkey.png'))
bckgrndimg = pygame.image.load(os.path.join(game_folder, 'BackGround.png'))
bckgrnd2img = pygame.image.load(os.path.join(game_folder, 'BackGround2.png'))
minimapimg = pygame.image.load(os.path.join(game_folder, 'minimap.png'))
backgrndlist = (bckgrndimg, bckgrnd2img)
bckgrndlist = random.choice(backgrndlist)
logoimg = pygame.image.load(os.path.join(game_folder, 'Logo.png'))
pygame.display.set_icon(logoimg)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
plane1 = Plane1()
all_sprites.add(plane1)
oiror = ("Aero1", "Aero2", "Aero3", "Aero4", "Aero5", "Aero6")
oiro = "Aero1"
global x
global y
if oiro == "Aero1":
    x = -1500
    y = -1065
    Plane1Rect.center = (450, 460)
if oiro == "Aero2":
    x = -3295
    y = -1555
    Plane1Rect.center = (435, 40)
if oiro == "Aero3":
    x = -4585
    y = -2205
    Plane1Rect.center = (450, 270)
if oiro == "Aero4":
    x = -1070
    y = -3480
    Plane1Rect.center = (34, 60)
if oiro == "Aero5":
    x = -1475
    y = -4395
    Plane1Rect.center = (433,478)
if oiro == "Aero6":
    x = -3890
    y = -3830
    Plane1Rect.center = (475,455)
righto = x + 6000
downo = y + 6000
sc1 = False
sc2 = False
def sc1T():
    global sc1
    sc1 = True
def sc1F():
    global sc1
    sc1 = False
def sc2T():
    global sc2
    sc2 = True
def sc2F():
    global sc2
    sc2 = False
sc1T()
incT()
listt2 = (1,2)
listt22 = random.randint(1,2)
font1 = pygame.font.Font(os.path.join(game_folder, 'AgencyFB.ttf'), 20)


def MainScreen():
    all_sprites.draw(screen)
    global xp_points
    global strxp
    font1 = pygame.font.Font(os.path.join(game_folder, 'AgencyFB.ttf'), 20)
    Text1 = font1.render("XP :"+strxp, True, BLACK)
    Text1Rect = Text1.get_rect()
    Text1Rect.topleft = (1,1)
    screen.blit(Text1, Text1Rect)
def StartScreen():
    global bckgrndlist
    screen.fill(BLACK)
    screen.blit(bckgrndlist, (0,0))
    if bckgrndlist == bckgrnd2img:
        screen.blit(logoimg, (375, 100))
    else:
        screen.blit(logoimg, (375, 25))
    fonto = pygame.font.Font((os.path.join(game_folder, 'AgencyFB.ttf')), 34)
    Text1 = fonto.render("Play", True, BLUE)
    Text1Rect = Text1.get_rect()
    Text1Rect.center = (250, 350)
    Button1 = pygame.Surface((100,50))
    Button1Rect = Button1.get_rect()
    Button1Rect.center = (250,350)
    mousex, mousey = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (mousex > 200 and mousex < 300)and(mousey > 325 and mousey < 375):
        pygame.draw.rect(screen, RCOLOR, (200, 325, 100,50))
        screen.blit(Text1, Text1Rect)
        if click[0] == 1:
            sc1F()
            sc2T()
    else:
        screen.blit(Button1,Button1Rect)
        screen.blit(Text1, Text1Rect)
        pygame.draw.line(screen, WHITE, (200, 325), (300, 325), 5)
        pygame.draw.line(screen, WHITE, (200, 375), (300, 375), 5)
        pygame.draw.line(screen, WHITE, (200, 323), (200, 377), 5)
        pygame.draw.line(screen, WHITE, (300, 323), (300, 377), 5)
    kkk = pygame.key.get_pressed()
    if kkk[K_RETURN]:
        sc1F()
        sc2T()
    if kkk[K_p]:
        sc1F()
        sc2T()
def MAINSCREEN():
    global x
    global y
    global righto
    global downo
    global oiro
    global xp_points
    global strxp
    global font1
    global em3
    global textiii, textiiirect
    crighto = (6290-righto)
    cdowno = (6290-downo)
    MainScreen()
    if apnumst == "1":
        Text1o = font1.render(apnumst+" passenger", True, BLACK)
    else:
        Text1o = font1.render(apnumst+" passengers", True, BLACK)
    Text1oRect = Text1o.get_rect()
    Text1oRect.bottomright = (490, 21)
    pays = pygame.key.get_pressed()
    if em2 == "Aero1":
        em3 = "Airport 1"
        textiii = font1.render(em3, True, BLACK)
    if em2 == "Aero2":
        em3 = "Airport 2"
        textiii = font1.render(em3, True, BLACK)
    if em2 == "Aero3":
        em3 = "Airport 3"
        textiii = font1.render(em3, True, BLACK)
    if em2 == "Aero4":
        em3 = "Airport 4"
        textiii = font1.render(em3, True, BLACK)
    if em2 == "Aero5":
        em3 = "Airport 5"
        textiii = font1.render(em3, True, BLACK)
    if em2 == "Aero6":
        em3 = "Airport 6"
        textiii = font1.render(em3, True, BLACK)
    if bigaps == False:
        passmethod()
        textiii = font1.render(em3, True, BLACK)
        textiiirect = textiii.get_rect()
        textiiirect.center = (250, 10)
        bigapsT()
    if oiro == em2:
        global apnum
        if oiro == "Aero1":
            if Plane1Rect.x > 140 and Plane1Rect.x < 220 and Plane1Rect.y > 180 and Plane1Rect.y < 260:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
        elif oiro == "Aero2":
            if Plane1Rect.x > 70 and Plane1Rect.x < 130 and Plane1Rect.y > 420 and Plane1Rect.y < 490:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
        elif oiro == "Aero3":
            if Plane1Rect.x > 310 and Plane1Rect.x < 380 and Plane1Rect.y > 370 and Plane1Rect.y < 440:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
        elif oiro == "Aero4":
            if Plane1Rect.x > 100 and Plane1Rect.x < 160 and Plane1Rect.y > 60 and Plane1Rect.y < 120:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
            if Plane1Rect.x > 330 and Plane1Rect.x < 390 and Plane1Rect.y > 60 and Plane1Rect.y < 110:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
            if Plane1Rect.x > 110 and Plane1Rect.x < 160 and Plane1Rect.y > 390 and Plane1Rect.y < 440:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
            if Plane1Rect.x > 235 and Plane1Rect.x < 280 and Plane1Rect.y > 390 and Plane1Rect.y < 440:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
            if Plane1Rect.x > 330 and Plane1Rect.x < 385 and Plane1Rect.y > 390 and Plane1Rect.y < 440:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
        elif oiro == "Aero5":
            if Plane1Rect.x > 30 and Plane1Rect.x < 90 and Plane1Rect.y > 80 and Plane1Rect.y < 140:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
            if Plane1Rect.x > 260 and Plane1Rect.x < 320 and Plane1Rect.y > 80 and Plane1Rect.y < 140:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
        elif oiro == "Aero6":
            if Plane1Rect.x > 60 and Plane1Rect.x < 120 and Plane1Rect.y > 430 and Plane1Rect.y < 490:
                if pays[K_t]:
                    xp_points += 20
                    strxp = str(xp_points)
                    xpo = {
                        "xp":xp_points
                    }
                    with open((bin_folder+'/bin.json'), "w") as FILE:
                        json.dump(xpo, FILE, skipkeys=True, indent=4)
                    Text1 = font1.render("XP :"+strxp, True, BLACK)
                    Text1Rect = Text1.get_rect()
                    Text1Rect.topleft = (1,1)
                    screen.blit(Text1, Text1Rect)
                    apnum = 0
                    reloadpass()
                    bigapsF()
    if outc == True:
        global xopos, yopos
        global minimapos, minimaposrect
        screen.fill(BLACK)
        screen.blit(islandimg, (x,y))
        keys2 = pygame.key.get_pressed()
        if keys2[K_UP]:
            downo += 5
            print ("Your Y position on the Island: ",downo)
            y += 5
            yopos = (cdowno/48)
            screen.blit(islandimg, (x,y))
            minimaposrect.topleft = (xopos+375, yopos+375)
            screen.blit(minimapos, minimaposrect)
        if keys2[K_DOWN]:
            downo -= 5
            print ("Your Y position on the Island : ",downo)
            y -= 5
            yopos = (cdowno/48)
            screen.blit(islandimg, (x,y))
            minimaposrect.topleft = (xopos+375, yopos+375)
            screen.blit(minimapos, minimaposrect)
        if keys2[K_LEFT]:
            righto += 5
            print ("Your X position on the Island : ",righto)
            x += 5
            xopos = (crighto/48)
            screen.blit(islandimg, (x,y))
            minimaposrect.topleft = (xopos+375, yopos+375)
            screen.blit(minimapos, minimaposrect)
        if keys2[K_RIGHT]:
            righto -= 5
            print ("Your X position on the Island: ",righto)
            x -= 5
            xopos = (crighto/48)
            screen.blit(islandimg, (x,y))
            minimaposrect.topleft = (xopos+375, yopos+375)
            screen.blit(minimapos, minimaposrect)
        all_sprites.draw(screen)
        Text1 = font1.render("XP :"+strxp, True, BLACK)
        Text1Rect = Text1.get_rect()
        screen.blit(Text1, Text1Rect)
        screen.blit(Text1o, Text1oRect)
        screen.blit(textiii, textiiirect)
        Plane1Rect.center = (255, 255)
        if righto < 4540 and righto > 4275:
            if downo < 4965 and downo > 4910:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero1"
                    incT()
                    Plane1Rect.center = (450, 460)
        if righto < 2730 and righto > 2470:
            if downo < 4470 and downo > 4420:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero2"
                    incT()
                    Plane1Rect.center = (435, 40)
        if righto < 1440 and righto > 1385:
            if downo < 3825 and downo > 3560:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero3"
                    incT()
                    Plane1Rect.center = (450, 270)
        if righto < 4960 and righto > 4900:
            if downo < 2545 and downo > 2285:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero4"
                    incT()
                    Plane1Rect.center = (34, 60)
        if righto < 4560 and righto > 4500:
            if downo < 1830 and downo > 1565:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero5"
                    incT()
                    Plane1Rect.center = (433, 478)
        if righto < 2140 and righto > 1880:
            if downo < 2200 and downo > 2140:
                ThisText1 = font1.render("press", True, BLACK)
                ThisText1Rect = ThisText1.get_rect()
                ThisText1Rect.center = (435, 30)
                screen.blit(ThisText1, ThisText1Rect)
                ThisText2 = font1.render("to enter airport", True, BLACK)
                ThisText2Rect = ThisText2.get_rect()
                ThisText2Rect.center = (435, 100)
                screen.blit(ThisText2, ThisText2Rect)
                screen.blit(enterkeyimg, (395,45))
                if keys2[K_RETURN]:
                    outcF()
                    oiro = "Aero6"
                    incT()
                    Plane1Rect.center = (450, 460)
        if x > 0:
            x = 0
            righto = 6000
        if y > 0:
            y = 0
            downo = 6000
        if righto < 500:
            righto = 500
            x = -5500
        if downo < 500:
            downo = 500
            y = -5500
        screen.blit(minimapimg, (375,375))
        screen.blit(minimapos2, minimapos2rect)
        pygame.draw.line(screen, WHITE, (411, 402),(415, 402))
        pygame.draw.line(screen, WHITE, (448, 412),(453, 412))
        pygame.draw.line(screen, WHITE, (476, 426), (476, 430))
        pygame.draw.line(screen, WHITE, (402, 452), (402, 457))
        pygame.draw.line(screen, WHITE, (411, 467), (411, 472))
        pygame.draw.line(screen, WHITE, (461, 460), (465, 460))
        screen.blit(minimapos, minimaposrect)
        pygame.draw.line(screen, BLACK, (374, 374), (374, 500))
        pygame.draw.line(screen, BLACK, (374,374), (500, 374))
    if inc == True:
        if oiro == "Aero1":
            screen.fill(BLACK)
            screen.blit(airport1img, (0,0))
            if Plane1Rect.colliderect(airportrect):
                Plane1Rect.center = (Plane1Rect.x, 255)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(garagerect):
                Plane1Rect.center = (Plane1Rect.x, 255)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(ctr):
                Plane1Rect.center = (Plane1Rect.x, 255)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x < 0:
                if Plane1Rect.y > 400:
                    incF()
                    outcT()
        if oiro == "Aero2":
            screen.fill(BLACK)
            screen.blit(airport2img, (0,0))
            if Plane1Rect.colliderect(garage2rect):
                Plane1Rect.center = (Plane1Rect.x,250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(airport2rect):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(ctr2):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x < 0:
                if Plane1Rect.y < 37:
                    incF()
                    outcT()
        if oiro == "Aero3":
            screen.fill(BLACK)
            screen.blit(airport3img, (0,0))
            if Plane1Rect.colliderect(airport3rect):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(garage3rect):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x < 0:
                if Plane1Rect.y < 267 and Plane1Rect.y > 215:
                    incF()
                    outcT()
        if oiro == "Aero4":
            screen.fill(BLACK)
            screen.blit(airport4img, (0,0))
            if Plane1Rect.colliderect(airport41rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(airport42rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(ctr4):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x > 417:
                if Plane1Rect.y < 0:
                    incF()
                    outcT()
        if oiro == "Aero5":
            screen.fill(BLACK)
            screen.blit(airport5img, (0,0))
            if Plane1Rect.colliderect(airport5rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.center = (25,10)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(garage51rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(garage52rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x < 0:
                if Plane1Rect.y > 429:
                    incF()
                    outcT()
        if oiro == "Aero6":
            screen.fill(BLACK)
            screen.blit(airport6img, (0,0))
            if Plane1Rect.colliderect(garage6rect):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(airport6rect):
                Plane1Rect.center = (250, Plane1Rect.y)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(mac61rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(mac62rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.colliderect(cs6rect):
                Plane1Rect.center = (Plane1Rect.x, 250)
                xp_points -= 10
                strxp = str(xp_points)
                xpo = {
                    "xp":xp_points
                }
                with open((bin_folder+'/bin.json'), "w") as FILE:
                    json.dump(xpo, FILE, skipkeys=True, indent=4)
                Text1 = font1.render("XP :"+strxp, True, BLACK)
                Text1Rect = Text1.get_rect()
                Text1Rect.topleft = (1,1)
                screen.blit(Text1, Text1Rect)
            if Plane1Rect.x > 450:
                if Plane1Rect.y < 0:
                    incF()
                    outcT()
        all_sprites.draw(screen)
        font1 = pygame.font.Font(os.path.join(game_folder, 'AgencyFB.ttf'), 20)
        Text1 = font1.render("XP :"+strxp, True, BLACK)
        Text1Rect = Text1.get_rect()
        Text1Rect.topleft = (1,1)
        screen.blit(Text1, Text1Rect)
        screen.blit(Text1o, Text1oRect)
        screen.blit(textiii, textiiirect)
        if oiro == "Aero1":
            if Plane1Rect.y < 400:
                if Plane1Rect.x < 0:
                    Plane1Rect.left = 0
            if Plane1Rect.x > 450:
                Plane1Rect.right = 490
            if Plane1Rect.y < 0:
                Plane1Rect.top = 0
            if Plane1Rect.y > 450:
                Plane1Rect.bottom = 500
        if oiro == "Aero2":
            if Plane1Rect.y > 37:
                if Plane1Rect.x < 0:
                    Plane1Rect.left = 0
            if Plane1Rect.x > 450:
                Plane1Rect.x = 450
            if Plane1Rect.y < 0:
                Plane1Rect.y = 0
            if Plane1Rect.y > 450:
                Plane1Rect.y = 450
        if oiro == "Aero3":
            if Plane1Rect.x < 0:
                if Plane1Rect.y > 267 or Plane1Rect.y < 215:
                    Plane1Rect.left = 0
            if Plane1Rect.x > 450:
                Plane1Rect.x = 450
            if Plane1Rect.y < 0:
                Plane1Rect.y = 0
            if Plane1Rect.y > 450:
                Plane1Rect.y = 450
        if oiro == "Aero4":
            if Plane1Rect.y < 0:
                if Plane1Rect.x < 417:
                    Plane1Rect.y = 0
            if Plane1Rect.y > 450:
                Plane1Rect.y = 450
            if Plane1Rect.x < 0:
                Plane1Rect.x = 0
            if Plane1Rect.x > 450:
                Plane1Rect.x = 450
        if oiro == "Aero5":
            if Plane1Rect.x < 0:
                if Plane1Rect.y < 429:
                    Plane1Rect.x = 0
            if Plane1Rect.x > 450:
                Plane1Rect.x = 450
            if Plane1Rect.y < 0:
                Plane1Rect.y = 0
            if Plane1Rect.y > 450:
                Plane1Rect.y = 450
        if oiro == "Aero6":
            if Plane1Rect.y < 0:
                if Plane1Rect.x < 450:
                    Plane1Rect.y = 0
            if Plane1Rect.y > 450:
                Plane1Rect.y = 450
            if Plane1Rect.x < 0:
                Plane1Rect.x = 0
            if Plane1Rect.right > 500:
                Plane1Rect.right = 500

file_exists = os.path.exists(bino)
if file_exists == True:
    global xp_points
    b1 = open(bino)
    b = json.load(b1)
    xp_points = b["xp"]
else:
    xp = {
        "xp":100
    }
    with open(bino, "w") as FILE:
        json.dump(xp, FILE, skipkeys=True, indent=4)
    b1 = open(bino)
    b = json.load(b1)
    xp_points = b["xp"]
strxp = str(xp_points)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if sc1 == True:
        StartScreen()
        safeT()
    if sc2 == True:
        MAINSCREEN()
        safeF()
    all_sprites.update()
    pygame.display.flip()
pygame.quit()