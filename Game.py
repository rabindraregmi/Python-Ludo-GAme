import pygame
import ludoGame,snakesAndLadders
pygame.init()
SILVER=(100,100,100)
BLACK=(0,0,0)
gameDisplay= pygame.display.set_mode((600, 600))
pygame.display.set_caption("LUDO GAME")
global n
while True:
        
    bg = pygame.image.load('icons\menubg.jpg')
    bg = pygame.transform.scale(bg, (600, 600))
    gameDisplay.blit(bg,(0,0))
    pygame.draw.rect(gameDisplay,SILVER,[2,2,335,100],1)
    ludoGame.message(gameDisplay,"1.Play Ludo",BLACK,10,10)
    ludoGame.message(gameDisplay, "2.Play Snakes and Ladders", BLACK, 10, 40)
    ludoGame.message(gameDisplay, "3.Quit", BLACK, 10, 70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_1:
                    gameDisplay.fill(ludoGame.white)
                    ludoGame.message(gameDisplay, "Enter the no of gattis 1/2/3/4", ludoGame.red, 10, 200)
                    noResponse = True
                    pygame.display.update()
                    while noResponse:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    n = 1
                                    noResponse = False
                                elif event.key == pygame.K_2:
                                    n = 2
                                    noResponse = False
                                elif event.key == pygame.K_3:
                                    n = 3
                                    noResponse = False
                                elif event.key == pygame.K_4:
                                    n = 4
                                    noResponse = False
                    ludoGame.main()
                elif event.key ==pygame.K_2:
                    snakesAndLadders.main()
                elif event.key ==pygame.K_3:
                    quit()
    pygame.display.update()
















