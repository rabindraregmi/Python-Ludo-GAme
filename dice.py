#Code for dice design. Creates several image files for dice animation
import pygame
green = (0,255,0)
blue = (0,0,128)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)
grey=(10,10,10)
big_rectangle=240
hole_radius=30
dice_size = 80
x =  0
y = 0
gameDisplay= pygame.display.set_mode((dice_size,dice_size))
pygame.display.set_caption("LUDO FOR EVERYONE")
gameDisplay.fill(white)




dot_size = dice_size // 10
mid = dice_size // 2
left = top = dice_size // 4
right = bottom = dice_size - left
def dice_roll(num):
    pygame.draw.rect(gameDisplay,white,(x , y, dice_size, dice_size))
    pygame.draw.rect(gameDisplay, grey, (x+1 , y+1, dice_size-2, dice_size-2))
    if num == 1:
        pygame.draw.circle(gameDisplay, white, (x + mid, y + mid), dot_size)
    else:
        if num == 2 or num == 3:
            pygame.draw.circle(gameDisplay, white, (x + right, y + mid), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + mid), dot_size)
            if num == 3:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + mid), dot_size)
        else:
            pygame.draw.circle(gameDisplay, white, (x + right, y + top), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + top), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + left, y + bottom), dot_size)
            pygame.draw.circle(gameDisplay, white, (x + right, y + bottom), dot_size)
            if num == 5:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + mid), dot_size)
            elif num == 6:
                pygame.draw.circle(gameDisplay, white, (x + mid, y + top), dot_size)
                pygame.draw.circle(gameDisplay, white, (x + mid, y + bottom), dot_size)
    pygame.display.update()

halfArr=[]
fullArr=[]

for dicenum in xrange(1,7):
    dice_roll(dicenum)
    pygame.image.save(gameDisplay, "dice"+str(dicenum)+".jpeg")

pygame.draw.rect(gameDisplay,grey,(x , y, dice_size, dice_size))
pygame.image.save(gameDisplay,"dicemid.jpeg")



























