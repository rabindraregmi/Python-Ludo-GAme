import pygame
import ludoGame,snakesAndLadders
import os
pygame.init()
yellow=(255,255,0)
gameDisplay= pygame.display.set_mode((600, 600))
pygame.display.set_caption("LUDO GAME")

def selected(rect):
    pygame.draw.rect(gameDisplay,yellow,rect,5)
    pygame.display.update()


def ludoPrompt():
    gameDisplay.blit(bg,(0,0))
    gameDisplay.blit(gattiselect,(10,100))
    pygame.display.update()
    flag=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                flag=100
                if event.key==pygame.K_1:
                    ludoGame.n=1
                elif event.key==pygame.K_2:
                    ludoGame.n=2
                elif event.key==pygame.K_3:
                    ludoGame.n=3
                elif event.key==pygame.K_4:
                    ludoGame.n=4
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if flag==100:
            break


bg = pygame.image.load('icons\menubg1.jpg')
bg = pygame.transform.scale(bg, (600, 600))
bg2=pygame.transform.scale(pygame.image.load(os.path.join('icons','menubg2.jpg')),(600,600))
play=pygame.transform.scale(pygame.image.load(os.path.join('icons','play.png')),(120,50))
rules=pygame.transform.scale(pygame.image.load(os.path.join('icons','rules.png')),(120,50))
quit_=pygame.transform.scale(pygame.image.load(os.path.join('icons','quit.png')),(120,50))
img1=pygame.transform.scale(pygame.image.load(os.path.join('Board','board.jpeg')),(200,200))
img2=pygame.transform.scale(pygame.image.load(os.path.join('Board','board2.jpg')),(200,200))
opt1=pygame.transform.scale(pygame.image.load(os.path.join('icons','opt1.png')),(120,30))
opt2=pygame.transform.scale(pygame.image.load(os.path.join('icons','opt2.png')),(200,30))
gattiselect=pygame.transform.scale(pygame.image.load(os.path.join('icons','message.png')),(450,50))
while True:

    gameDisplay.blit(bg,(0,0))
    gameDisplay.blit(play,(10,10))
    gameDisplay.blit(rules,(10,110))
    gameDisplay.blit(quit_,(10,210))
    mx, my = pygame.mouse.get_pos()
    if (mx>=10 and mx<=130) and (my>=10 and my<=60):
        selected([10,10,120,50])
    elif (mx >= 10 and mx <= 130) and (my >= 110 and my <= 160):
        selected([10, 110, 120, 50])
    elif (mx >= 10 and mx <= 130) and (my >= 210 and my <= 260):
        selected([10, 210, 120, 50])
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if (mx >= 10 and mx <= 130) and (my >= 10 and my <= 60):
                gameDisplay.blit(bg2, (0, 0))
                gameDisplay.blit(img1, (20, 20))
                gameDisplay.blit(img2, (360, 20))
                gameDisplay.blit(opt1,(20,230))
                gameDisplay.blit(opt2,(360,230))
                pygame.display.update()
                while True:
                    newmx, newmy = pygame.mouse.get_pos()
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event2.type == pygame.MOUSEBUTTONDOWN:
                            if (newmx >= 20 and newmx <= 220) and (newmy >= 20 and newmy <= 220):
                                ludoPrompt()
                                ludoGame.main()
                            elif (newmx >= 360 and newmx <= 560) and (newmy >= 20 and newmy <= 220):
                                snakesAndLadders.main()
                    pygame.display.update()

            elif (mx >= 10 and mx <= 130) and (my >= 110 and my <= 160):
                rules()
            elif (mx >= 10 and mx <= 130) and (my >= 210 and my <= 260):
                pygame.quit()
                quit()
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()















