import pygame
import ludoGame,snakesAndLadders
import os
yellow=(255,255,0)


def selected(gameDisplay,rect):
    pygame.draw.rect(gameDisplay,yellow,rect,5)
    pygame.display.update()


def ludoPrompt(gameDisplay,bg,msg):
    gameDisplay.blit(bg,(0,0))
    gameDisplay.blit(msg,(60,370))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    return 1
                elif event.key==pygame.K_2:
                    return 2
                elif event.key==pygame.K_3:
                    return 3
                elif event.key==pygame.K_4:
                    return 4
                elif event.key==pygame.K_BACKSPACE:
                    return 0
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



def gameRules(gameDisplay,bg):
    with open('Instructions.txt','r') as filevar:
        text=filevar.readlines()
    text=[x.strip() for x in text]
    font = pygame.font.SysFont("microsoftsansserif", 16)
    gameDisplay.blit(bg,(0,0))
    y=0
    for line in text:
        color=(255,255,255)
        if y==0 or y==21:
            color=(0,200,100)
        elif y==18 or y==33:
            color=(200,0,0)
        textOnScreen = font.render(line, True, color)
        gameDisplay.blit(textOnScreen,(5,y*17))
        y+=1
    backspace=False
    while not backspace:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    backspace=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                backspace=True
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()    

    
    
    
def main():
    pygame.init()
    gameDisplay= pygame.display.set_mode((600, 600))
    pygame.display.set_caption("LUDO GAME")
    bg1 = pygame.image.load('icons/menubg.jpg')
    bg1 = pygame.transform.scale(bg1, (600, 600))
    bg2=pygame.transform.scale(pygame.image.load(os.path.join('icons','menubg1.jpg')),(600,600))
    bg3=pygame.transform.scale(pygame.image.load(os.path.join('icons','menubg2.jpg')),(600,600))
    play=pygame.transform.scale(pygame.image.load(os.path.join('icons','play.png')),(120,50))
    rules=pygame.transform.scale(pygame.image.load(os.path.join('icons','Rules.png')),(120,50))
    quit_=pygame.transform.scale(pygame.image.load(os.path.join('icons','quit.png')),(120,50))
    img1=pygame.transform.scale(pygame.image.load(os.path.join('Board','Board.jpeg')),(200,200))
    img2=pygame.transform.scale(pygame.image.load(os.path.join('Board','Board2.jpg')),(200,200))
    opt1=pygame.transform.scale(pygame.image.load(os.path.join('icons','opt1.png')),(120,30))
    opt2=pygame.transform.scale(pygame.image.load(os.path.join('icons','opt2.png')),(200,30))
    gattiselect = pygame.transform.scale(pygame.image.load(os.path.join('icons', 'message.png')), (450, 50))
    playerselect = pygame.transform.scale(pygame.image.load(os.path.join('icons', 'message.png')), (450, 50))

    while True:
        back=False
        gameDisplay.blit(bg1,(0,0))
        gameDisplay.blit(play,(10,10))
        gameDisplay.blit(rules,(10,110))
        gameDisplay.blit(quit_,(10,210))
        mx, my = pygame.mouse.get_pos()
        if (mx>=10 and mx<=130) and (my>=10 and my<=60):
            selected(gameDisplay,[10,10,120,50])
        elif (mx >= 10 and mx <= 130) and (my >= 110 and my <= 160):
            selected(gameDisplay,[10, 110, 120, 50])
        elif (mx >= 10 and mx <= 130) and (my >= 210 and my <= 260):
            selected(gameDisplay,[10, 210, 120, 50])
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
                            elif event2.type == pygame.MOUSEBUTTONDOWN:
                                if (newmx >= 20 and newmx <= 220) and (newmy >= 20 and newmy <= 220):
                                    ludoGame.n=ludoPrompt(gameDisplay,bg2,gattiselect)
                                    if ludoGame.n==0:
                                        back=True
                                        break
                                    else:
                                        ludoGame.players=ludoPrompt(gameDisplay,bg2,playerselect)
                                        ludoGame.main()
                                elif (newmx >= 360 and newmx <= 560) and (newmy >= 20 and newmy <= 220):
                                    snakesAndLadders.main()
                            elif event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_BACKSPACE:
                                    back=True
                        if back==True:
                            break
                        pygame.display.update()

                elif (mx >= 10 and mx <= 130) and (my >= 110 and my <= 160):
                    gameRules(gameDisplay,bg3)
                elif (mx >= 10 and mx <= 130) and (my >= 210 and my <= 260):
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()



if __name__=='__main__':
    main()











