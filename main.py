import pygame
import sys
import random
from time import sleep

padWidth = 480
padHeight = 640
rockImage = ['rock01.png', 'rock02.png', 'rock03.png', 'rock04.png', 'rock05.png',\
             'rock06.png', 'rock07.png', 'rock08.png', 'rock09.png', 'rock10.png',\
             'rock11.png', 'rock12.png', 'rock13.png', 'rock14.png', 'rock15.png',\
             'rock16.png', 'rock17.png', 'rock18.png', 'rock19.png', 'rock20.png',\
             'rock21.png', 'rock22.png', 'rock23.png', 'rock24.png', 'rock25.png',\
             'rock26.png', 'rock27.png', 'rock28.png', 'rock29.png', 'rock30.png']


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))



def initGame(): # 게임 초기화 하는 부
    global gamePad, clock, background, fighter, missile
    pygame.init() # 라이브러리 초기화
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting') # 창의 제목 설정
    background = pygame.image.load('./PyShooting/background.png')
    fighter = pygame.image.load('./PyShooting/fighter.png')
    missile = pygame.image.load('./PyShooting/missile.png')
    clock = pygame.time.Clock()


def runGame():
    global gapdPad, clock, background, fighter, missile

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    missileXY = []

    onGame = False
    while not onGame:
        # 이벤트 처리
        for event in pygame.event.get(): # 게임 종료시키는 이벤트
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX += 5

                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0

        drawObject(background, 0, 0)

        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        # gamePad.fill(BLACK) # 창을 검정색으로 만듦

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


initGame()
runGame()